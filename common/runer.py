# -*- coding: utf-8 -*-
'''
运行模块
'''
import datetime
import io
import os
import sys
import time
import json
import shutil
import jinja2
import unittest
import functools
import traceback
import common.setting as ST
from common.globall import g
from airtest.report.report import nl2br
from airtest.cli.info import get_script_info
from airtest.core.api import G, auto_setup, log,snapshot
from airtest.report.report import (LogToHtml,decode_path,script_dir_name,STATIC_DIR,HTML_TPL)
__import__("common.globall")


class BaseCase(unittest.TestCase):

    #指向脚本文件，由子类初始化。
    file=None #type:str

    @classmethod
    def setUpClass(cls):
        #由子类构造日志目录和脚本目录
        #取得case相关信息
        if ST.REPORT_PATH:
            #生成日志需要配置这些信息  如果不配置日志路径  将不会生成报告和日志
            infor=json.loads(get_script_info(cls.file)) #获得脚本信息
            cls.__logPath, cls.__reportPath = makePath(cls.file)
            # 是否录像标志
            cls.__recording=ST.RECORDING #type:bool
            makeCaseInfo(cls.file, cls.__reportPath,infor)
            auto_setup(basedir=cls.file, logdir=cls.__logPath)
        else:
            auto_setup()

    def setUp(self):
        if self.__logPath and self.__recording:
            for dev in G.DEVICE_LIST:
                try:
                    dev.start_recording()
                except:
                    traceback.print_exc()

    def tearDown(self):
        if self.__logPath and self.__recording:
            for k, dev in enumerate(G.DEVICE_LIST):
                try:
                    output = os.path.join(self.__logPath, "recording_%d.mp4" % k)
                    dev.stop_recording(output)
                except:
                    traceback.print_exc()
    @classmethod
    def tearDownClass(cls) -> None:
        if ST.REPORT_PATH:
            #改为脚本执行完成，统一生成报告
            save((cls.file,cls.__logPath,cls.__reportPath,ST.REPORT_FILE_NAME))
            # genReport(cls.file,cls.__logPath,cls.__reportPath,ST.REPORT_FILE_NAME)
        #将数据值恢复初始值
        cls.__logPath = None
        cls.file = None
        cls.__recording = None
        cls.__reportPath = None


def save(reportInfor):
    '''
    将报告信息放置到报告列表
    :param reportInfor:
    :return:
    '''
    g().report_list.append(reportInfor)

def makePath(fileName):
    '''
    返回日志存储路径和报告存储路径
    :param fileName:脚本路径
    :return:
    '''
    timePath = ST.TIME
    casePath = os.path.split(fileName)[1].split(".")[0]
    logPath = os.path.join(ST.LOG_DIR, timePath, casePath)
    reportPath=None
    if ST.REPORT_PATH!=None and ST.REPORT_PATH!='':
        reportPath=os.path.join(ST.REPORT_PATH,timePath,casePath)
        g().real_log_path = os.path.join(ST.REPORT_PATH, timePath)
    if not os.path.exists(logPath):
        os.makedirs(logPath)
    return logPath,reportPath

def makeCaseInfo(caseMoudleName,logPath,infor,status="成功",class_status="td_success"):
    '''
    构造脚本信息
    :param caseMoudleName: 脚本名
    :param logPath: 报告路径
    :param infor: 脚本信息
    :param status: 脚本执行状态
    :param class_status: 脚本状态格式
    :return: 
    '''
    caseName=os.path.splitext(os.path.basename(caseMoudleName))[0]
    log=os.path.join(logPath,ST.REPORT_FILE_NAME)
    log=log.replace(g().real_log_path,"").replace("/","",1).replace("\\","",1)
    desc=infor["desc"]
    author=infor["author"]
    title=infor["title"]
    g().data[caseName]={
        "status":status if status!=None else "",
        "desc":desc if desc!=None else "",
        "author":author if author!=None else "",
        "title":title if title!=None else "",
        "log":log,
        "class_status":class_status if class_status!=None else ""
    }

def genReport(script,logPath,reportPath,outFile='log.html',lang='zh'):
    '''
    生成详细报告
    :param script:脚本路径
    :param logPath:日志路径
    :param reportPath:报告路径
    :param outFile:输出名字
    :param lang:语言
    :return:
    '''
    # script filepath
    path, name = script_dir_name(script)   #name  脚本的名字
    record_list = []
    log_root = decode_path(logPath)
    static_root = STATIC_DIR
    static_root = decode_path(static_root)
    export = decode_path(reportPath)
    lang = lang if lang in ['zh', 'en'] else 'en'
    plugins = ("poco.utils.airtest.report",)

    # gen html report
    rpt = LogToHtml(path, log_root, static_root, export_dir=export, script_name=name, lang=lang, plugins=plugins)
    rpt.report(HTML_TPL, output_file=outFile, record_list=record_list)

def genTotalReport(logPath,result):
    '''
    生成汇总报告
    :param logPath: 
    :param result: 运行结果
    :return: 
    '''
    errors=result.errors
    infor=g().data
    failures=result.failures
    for error in errors:
        model=error[0].__module__
        modelData=infor[model]
        modelData['status']='错误'
        modelData['class_status']='td_error'
        infor[model]=modelData
    for failur in failures:
        model=failur[0].__module__
        modelData=infor[model]
        modelData['status']='失败'
        modelData['class_status'] = 'td_fail'
        infor[model]=modelData
    #构造渲染模板数据
    data={}
    data["infor"]=infor
    data["title"]=ST.TOTAL_REPORT_FILE_NAME.split(".")[0]
    total = result.testsRun
    error = len(errors)
    fail = len(failures)
    success=total-error-fail
    data["error"]=error
    data["fail"]=fail
    data["success"]=success
    data["begin_time"]=g().beginTime
    data["end_time"]=g().endTime
    data["duration"]=g().duration
    render(ST.TOTAL_REPORT_TEMPL,logPath,**data)

def render(template_name, output_file=None, **template_vars):
        """ 用jinja2渲染html"""
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
            extensions=(),
            autoescape=True
        )
        env.filters['nl2br'] = nl2br
        template = env.get_template(template_name)
        html = template.render(**template_vars)
        #将报告写出来
        if output_file:
            with io.open(output_file, 'w', encoding="utf-8") as f:
                f.write(html)
            print("\n${报告路径:%s}\n" % output_file)
        return html

def testLog(f=None):
    '''
    case装饰器，用例需要装饰
    :param f: 
    :return:
    '''
    @functools.wraps(f)
    def wrapper(*args,**kwargs):
        try:
            f(*args,**kwargs)
        except:
            tb = traceback.format_exc()
            log("Final Error", tb)
            raise
        finally:
            try:
                snapshot(msg="Final Snapshot")
            except:
                log("无最终截图")

    return wrapper

def clean(real_log_path):
    '''
    清理生成的报告，减小所占空间
    :param real_log_path: 原始报表路径
    :return:
    '''
    willMoveFile = None
    willDelFile = []
    willChangeFile = []
    for maindir, subdir, file_name_list in os.walk(real_log_path):
        for path in subdir:
            apath = os.path.join(maindir, path)  # 合并成一个完整路径
            if (path == 'static') and (willMoveFile == None):
                willMoveFile = apath
                continue
            if path == 'static':
                willDelFile.append(apath)
        for file in file_name_list:
            apath = os.path.join(maindir, file)  # 合并成一个完整路径
            if '.py' in file:
                willDelFile.append(apath)
            if '.txt' in file:
                willDelFile.append(apath)
            if '.html' in file:
                willChangeFile.append(apath)
    # 移动static文件
    os.rename(willMoveFile, "%s/static" % real_log_path)
    for file in willDelFile:
        # 删除不必要的文件
        try:
            shutil.rmtree(file)
        except:
            pass
        try:
            os.remove(file)
        except:
            pass
        dirName = os.path.dirname(file)
        try:
            os.remove(dirName)
        except:
            pass
    # 修改html文件的路径
    for name in willChangeFile:
        with open(name, encoding='utf-8') as file_obj:
            contents = file_obj.read()
            contents = contents.replace("static", "../static")
        with open(name, encoding='utf-8', mode='w') as file_obj:
            file_obj.write(contents)
    #移动每个case目录下的html和其他日志
    willMoveFile = []
    for maindir, subdir, file_name_list in os.walk(real_log_path):
        for path in subdir:
            apath = os.path.join(maindir, path)  # 合并成一个完整路径
            if path == "log":
                willMoveFile.append(apath)
        for file in file_name_list:
            apath = os.path.join(maindir, file)  # 合并成一个完整路径
            if ST.REPORT_FILE_NAME in file:
                willMoveFile.append(apath)
    for i in willMoveFile:
        temp = os.path.dirname(os.path.dirname(i))
        shutil.move(i, temp)


def main():
    #记录脚本开始时间
    g().beginTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #载入和运行脚本
    suite = unittest.TestSuite()
    for case in ST.CASE_MATCHER:
        suite.addTest(unittest.TestLoader().discover(ST.CASE_PATH,pattern=case))
    result = unittest.TextTestRunner(verbosity=0).run(suite)

    #记录脚本结束时间
    g().endTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    exeStart = datetime.datetime.strptime(g().beginTime, "%Y-%m-%d %H:%M:%S")
    exeEnd = datetime.datetime.strptime(g().endTime, "%Y-%m-%d %H:%M:%S")
    g().duration = str(exeEnd - exeStart)
    ###生成详细报告
    for report in g().report_list:
        genReport(report[0], report[1], report[2],report[3])
    ##生成汇总报告
    if ST.REPORT_PATH and len(g().report_list)>0:
        genTotalReport(os.path.join(g().real_log_path,ST.TOTAL_REPORT_FILE_NAME), result)
        ###处理生成的报告，节约空间
        #删除不必要的文件
        print("清理不必要的文件中。。。")
        clean(g().real_log_path)
        print("清理完成")
    if not result.wasSuccessful():
        sys.exit(-1)


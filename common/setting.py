
'''
框架配置数据，如需修改，请前往项目路径下的/conf/config.py
'''

import re
import os
import time
import configparser
def initDevice(DEVICE):
    if DEVICE!="None":
        DEVICE=str(DEVICE)
        #解析设备列表
        device_list=DEVICE.split("|")
        temp_device={}
        for device in device_list:
            loc=device.find(":")
            if loc==-1:
                raise BaseException("设备配置字符串不正确，请检查！")
            temp_device[device[:loc]]=device[loc+1:]
        return temp_device
    else:
        return None

def initProtectPocoService(protectFlag:str):
    #值校验
    protectFlag=protectFlag.lower()
    if protectFlag!="false" and protectFlag!="true":
        raise BaseException("保护poco service配置只能为false或者true")
    flag=protectFlag=="true"
    return flag

#汇总报告模板
TOTAL_REPORT_TEMPL="total_template.html"
#时间
TIME=time.strftime("%Y%m%d%H%M%S")
#报告文件名
REPORT_FILE_NAME="log.html"
#poot解析的起始字符串
POOT_BEGIN_HEAD='g().activePoot('
#poco解析的起始字符串
POCO_BEGIN_HEAD='g().activePoco('
#项目根目录
BASE_PATH=os.path.dirname(os.path.dirname(__file__))
#配置文件
CONFIG_FILE="%s/conf/config.cfg" % BASE_PATH

#-------------------其他配置------------------------#
###默认配置值
DEFAULT_CONFIG={
    "log_dir":"%s/log" % BASE_PATH,
    "recording":"false",
    "case_dir":"%s/case" % BASE_PATH,
    "report_path":"%s/report" % BASE_PATH,
    "report_name":"report",
    "device":"None",
    "test_data_file":"%s/conf/test_data.xml" % BASE_PATH,
    "picture_dir":"%s/conf/template" % BASE_PATH,
    "test_data_use_set":"None",
    "case_matcher_str":"test*",
    "time_out_about_wait_method":"60",
    "find_time_gaps":"0.3",
    "android_resource_dir":"%s/conf/android" % BASE_PATH,
    "ios_resource_dir":"%s/conf/ios" % BASE_PATH,
    "protect_poco_service":"false",
    "app_package_name":"None",
"cap_method":"MINICAP_STREAM",
    "touch_method":"MINITOUCH",
    "ori_method":"MINICAPORI"
}
conf=configparser.ConfigParser(DEFAULT_CONFIG)
conf.read(CONFIG_FILE,encoding='utf-8')
#等待方法的超时时间
TIME_OUT_ABOUT_WAIT_METHOD=conf.getfloat("DEFAULT","time_out_about_wait_method")
#查找时间间隙
FIND_TIME_GAPS=conf.getfloat("DEFAULT","find_time_gaps")
#日志目录
LOG_DIR=conf.get("DEFAULT","log_dir")
#是否录制屏幕
RECORDING=conf.getboolean("DEFAULT","recording")
#是否保护poco servcie
PROTECT_POCO_SERVICE=initProtectPocoService(str(conf.getboolean("DEFAULT","protect_poco_service")))
#CASE目录
CASE_PATH=conf.get("DEFAULT","case_dir")
#报告目录
REPORT_PATH=conf.get("DEFAULT","report_path")
if REPORT_PATH=='None':
    REPORT_PATH=None
#汇总报告文件名
TOTAL_REPORT_FILE_NAME="%s.html" % conf.get("DEFAULT","report_name")
#设备列表
DEVICE=conf.get("DEFAULT","device")
DEVICE=initDevice(DEVICE)
#测试数据文件
TEST_DATA_FILE=conf.get("DEFAULT","test_data_file")
#图片识别资源文件目录
PICTURE_DIR=conf.get("DEFAULT","picture_dir")
#待运行CASE匹配字符串
CASE_MATCHER=conf.get("DEFAULT","case_matcher_str")
CASE_MATCHER=str(CASE_MATCHER)
if CASE_MATCHER!="None":
    #解析字符串
    case_list=CASE_MATCHER.split("|")
    temp_case=[]
    for case in case_list:
        temp_case.append(case)
    CASE_MATCHER=temp_case
#-----------------相关字符串配置---------------------------
#数据文件测试数据默认使用sheet名
TEST_DATA_USE_SHEET_NAME=conf.get("DEFAULT","test_data_use_set")
if TEST_DATA_USE_SHEET_NAME=="None":
    TEST_DATA_USE_SHEET_NAME=None
#安卓UI定位资源信息文件
ANDROID_DIR=conf.get("DEFAULT","android_resource_dir")
#苹果UI定位资源信息文件
IOS_RESOURCE_DIR=conf.get("DEFAULT","ios_resource_dir")
#配置项名
SHEET_KEY_NAME="配置项"
#配置值名
SHEET_VALUE_NAME="配置值"
#默认包名读取
TEST_APP_PACKAGE_NAME=conf.get("DEFAULT","app_package_name")
if TEST_APP_PACKAGE_NAME=="None":
    raise BaseException("app包名未配置，请前往conf/config.cfg配置")
#连接配置项（仅仅无配置连接起作用,有配置时使用连接uri进行配置）
CAP_METHOD=conf.get("DEFAULT","cap_method")  #可选MINICAP、MINICAP_STREAM、ADBCAP、JAVACAP
TOUCH_METHOD=conf.get("DEFAULT","touch_method")   #可选配置MINITOUCH、ADBTOUCH
ORI_METHOD=conf.get("DEFAULT","ori_method")        #可选配置MINICAPORI、ADBORI

"""
不同类型的ui实体类
"""
import os

# 有名字的变量正则
import re

from airtest.core.cv import Template

var_name_pattern = re.compile(r'\$\{([0-9a-zA-Z]+)\}')
var_pattern = re.compile(r'\$\{\}')

class PootUi(object):

    def __init__(self,name,info):
        #初始化
        self.__name=name
        self.__info="poot{}".format(info)

    def replace_var(self,*args,**kw):
        #先替换变量
        value=self.__info
        orderMatcher = var_pattern.findall(value)
        nameMatcher = var_name_pattern.findall(value)
        if len(orderMatcher) != len(args):
            raise BaseException("需要的顺序变量数{%s},实际有{%s}" % (len(orderMatcher), len(args)))
        if len(nameMatcher) != len(kw):
            raise BaseException("需要的命名变量数{%s},实际有{%s}" % (len(nameMatcher), len(kw)))
        # 先替换顺序变量
        if args != None:
            for a in args:
                value = value.replace("${}", a, 1)
        # 再替换命名变量
        if kw != None:
            for k, v in kw.items():
                # 提取value中的变量
                # #如果变量名存在于字符串中，则进行替换
                if k in nameMatcher:
                    value = value.replace("${%s}" % k, str(v))
        self.__info=value

    @property
    def info(self):
        return self.__info

    @property
    def name(self):
        return self.__name

    @property
    def print(self):
        return self.__info

class PocoUi(object):

    def __init__(self,name,info):
        #初始化
        self.__name=name
        self.__info="poco{}".format(info)
        self.__resource=self.__info

    def replace_var(self, *args, **kw):
        # 先替换变量
        value = self.__resource
        orderMatcher = var_pattern.findall(value)
        nameMatcher = var_name_pattern.findall(value)
        if len(orderMatcher) != len(args):
            raise BaseException("需要的顺序变量数{%s},实际有{%s}" % (len(orderMatcher), len(args)))
        if len(nameMatcher) != len(kw):
            raise BaseException("需要的命名变量数{%s},实际有{%s}" % (len(nameMatcher), len(kw)))
        # 先替换顺序变量
        if args != None:
            for a in args:
                value = value.replace("${}", a, 1)
        # 再替换命名变量
        if kw != None:
            for k, v in kw.items():
                # 提取value中的变量
                # #如果变量名存在于字符串中，则进行替换
                if k in nameMatcher:
                    value = value.replace("${%s}" % k, str(v))
        self.__info = value

    @property
    def info(self):
        return self.__info

    @property
    def name(self):
        return self.__name

    @property
    def print(self):
        return self.__info

class Coordinate(object):
    def __init__(self,name,coordinate):
        self.__name=name
        #解析坐标
        x,y=coordinate.split(",")
        if "/" in x:
            a,b=x.split("/")
            x=float(a)/float(b)
        if "/" in y:
            a,b=y.split("/")
            y=float(a)/float(b)
        self.__x=float(x)
        self.__y=float(y)

    def replace_var(self, *args, **kw):
        pass

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def name(self):
        return self.__name

    @property
    def print(self):
        return "({},{})".format(self.__x,self.__y)

base_path = os.path.dirname(os.path.dirname(__file__))
class Picture(object):
    def __init__(self,name,path):
        self.__name=name
        #处理路径
        self.__path=os.path.join(base_path,path)
        #Template
        self.__template=None


    def getTemplate(self):
        if self.__template is None:
            self.__template=Template(self.__path)
        return self.__template

    @property
    def name(self):
        return self.__name

    def replace_var(self, *args, **kw):
        pass

    @property
    def print(self):
        return self.__name



class Key(object):
    def __init__(self,name,value):
        self.__name=name
        self.__value=value

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value

    def replace_var(self, *args, **kw):
        pass

    @property
    def print(self):
        return self.__value
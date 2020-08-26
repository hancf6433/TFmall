#工具模块
import functools
import json
import os
import re
import xml.sax
import requests
#项目根目录
BASE_PATH=os.path.dirname(os.path.dirname(__file__))
#atestVcfFile
atestVcfFile=os.path.join(BASE_PATH,"static","Atest.vcf")
#初始化文件
afile=os.path.join(BASE_PATH,"static",".A")
a1file=os.path.join(BASE_PATH,"static",".A1")

class readUiXml(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self._rootName=None
        self._lements={}
        self._name=None
        self._content=None

    def startElement(self,tag,attributes):
        if tag=="page":
            self._rootName=attributes["name"]
        if tag=="ui":
            self._name=attributes["name"]

    def characters(self, content):
        if self._name:
            self._content=content
            self.__saveUi()

    def __saveUi(self):
        self._lements[self._name]=self._content
        self._name, self._content = None, None


class readTestDataXml(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self._data_set_list=[]
        self._now_data_set=None
        self._lements={}
        self._name=None
        self._content=None

    def startElement(self,tag,attributes):
        if tag=="data_set":
            if self._now_data_set!=attributes["name"]:
                self._data_set_list.append(attributes["name"])
                self._now_data_set=attributes["name"]
        if tag=="data":
            temp=self._lements.get(self._now_data_set)
            if not temp:
                temp={}
            temp[attributes["name"]]=attributes["value"]
            self._lements[self._now_data_set]=temp


class tools(object):
    #单个汉字的正则表达式
    p1=re.compile(r"[\u4e00-\u9fa5]")
    #单个字母的正则表达式
    p2=re.compile(r"[a-zA-Z]")
    #单个空白符的正则表达式
    p3=re.compile(r"\s")
    #其他符号
    p4=re.compile(r"[,]")

    @classmethod
    def extractingNumbers(cls,string:str):
        '''
        从字符串中提取数字
        :param String:
        :return:
        '''
        #将汉字替换成空白
        string=cls.p1.sub("",string)
        #将英文字母替换成空白
        string=cls.p2.sub("",string)
        #将空白字符替换成空白
        string=cls.p3.sub("",string)
        #将其他符号替换成空白
        string=cls.p4.sub("",string)
        return float(string)

    @classmethod
    def textProgress(cls,string):
        stringList = list(string)
        lists = []
        capsFlag = False  # 指示是否位于大写状态
        tempValue = []    # 指示参数
        tempFlag = False  # 指示是否位于参数状态



        while stringList:
            temp: str = stringList.pop()
            if tempFlag and temp == "{":
                tempValue.append(temp)
                lists.append("".join(tempValue[::-1]))
                tempValue = []
                tempFlag = False
                continue
            if tempFlag and not (temp == "{" or temp == "}"):
                tempValue.append(temp)
                continue
            if tempFlag and temp == "}":
                raise BaseException("输入不正确，特殊按键的括号不完整，请检查：{%s}" % string)
            if not tempFlag and temp.isupper() and capsFlag:
                lists.append(temp)
                continue
            if not tempFlag and temp.isupper() and not capsFlag:
                capsFlag = True
                lists.append("{ca}")
                lists.append(temp)
                continue
            if not tempFlag and not temp.isupper() and capsFlag:
                capsFlag = False
                lists.append("{ca}")
            if not tempFlag and not temp.isupper() and temp == "}":
                tempValue.append(temp)
                tempFlag = True
                continue
            if not tempFlag and not temp.isupper() and temp == "{":
                raise BaseException("输入不正确，特殊按键的括号不完整，请检查：{%s}" % string)
            if not tempFlag and not temp.isupper() and not (temp == "}" or temp == "{"):
                lists.append(temp)
                continue


        return lists


    @classmethod
    def newTextProgress(cls, str, letterKeyboard=True):
        para = None
        firstChar = None
        lists = []
        while (len(str) > 0):
            firstChar = str[0]
            str = str[1:]
            if firstChar == "{":
                if para != None:
                    raise BaseException("待输入字符串格式不正确")
                para = ""
            if para != None and firstChar != "}":
                firstChar = firstChar.lower()
                para += firstChar
            if firstChar == "}":
                if para == None:
                    raise BaseException("待输入字符串格式不正确")
                para += "}"
                lists.append(para)
                para = None
            if firstChar.isdigit() and letterKeyboard:
                lists.append('{nu}')
                letterKeyboard = False
            if firstChar.isalpha() and not letterKeyboard:
                lists.append('{le}')
                letterKeyboard = True
            if (para == None or para == "{") and (
                    (firstChar.isupper() and len(lists) > 0 and not lists[-1].isupper()) or (
                    firstChar.isupper() and len(lists) == 0)):
                lists.append('{ca}')
            if firstChar != "}" and (not firstChar.isupper() and len(lists) > 0 and lists[-1].isupper()):
                lists.append('{ca}')
            if para == None and firstChar not in ['{', '}']:
                lists.append(firstChar)
        if firstChar.isupper():
            lists.append('{ca}')
        if para != None:
            raise BaseException("待输入字符串格式不正确")
        return lists

    @classmethod
    def resolveUiXml(cls,xmlFile):
        # 创建一个 XMLReader
        parser = xml.sax.make_parser()
        # turn off namepsaces
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        # 重写 ContextHandler
        handler = readUiXml()
        parser.setContentHandler(handler)
        parser.parse(xmlFile)
        return str(handler._rootName).lower(),handler._lements

    @classmethod
    def resolveTestDataXml(cls,xmlFile):
        # 创建一个 XMLReader
        parser = xml.sax.make_parser()
        # turn off namepsaces
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        # 重写 ContextHandler
        handler = readTestDataXml()
        parser.setContentHandler(handler)
        parser.parse(xmlFile)
        return handler._lements

    @classmethod
    def delDevice(self,phone: str):
        '''
        删除演练环境该手机号的常用设备，
        :param phone:
        :return: 无常用设备或者删除成功返回True,否则返回False
        '''
        try:
            S = requests.session()
            url = "http://172.32.12.243:27004/cas/login?service=http://172.32.12.243:20529/operation/v2/casIndex.htm"
            headers = {
                'Referer': 'http://172.32.12.243:27004/cas/login?service=http://172.32.12.243:20529/operation/v2/casIndex.htm',
                'Cache-Control': 'max-age=0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'zh-Hans-CN,zh-Hans;q=0.5',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',
                'Accept-Encoding': 'gzip, deflate',
                'Content-Length': '6511',
                'Host': '172.32.12.243:27004',
                'Connection': 'Keep-Alive',
                'Cookie': 'JSESSIONID=5E59A8CA26092764C45590DBFC53C2EE; user=sj0003&96e79218965eb72c92a549dd5a330112; check=1; scanBool=0'
            }
            data = {
                'username': 'sj0003',
                'password': '8cdcdb7c81b91c94508eb29044bf24f6',
                'telNumber': '',
                'verifyCode': '',
                'validateCode': '',
                'execution': '7908d24f-38c2-415a-8138-5cf9522ad286_ZXlKaGJHY2lPaUpJVXpVeE1pSjkuSzFVNVRHUlJiVXB4ZGt0T1Z6azBaaXRMTkZSRGVHTmFUbXhHYWt0MVpITkNXbEZPTUdJd2EzUjRaa1lyVlNzMFIwdG1VbTQyWTJ4S05tdGxSbWRyVW1ad2MxUjNVa1JDYlRSU2FpOUZXV00wY0dReVNHOW5jV1JqTkV0M1NWVjJUQ3RIVW5SVFVEQXJWbmxpYkRaWlkwaEJUVzl2TDFnd2N5dHpZbFZ5ZWpCRFpUUldiR3RuWVhKcE1WUmpTRWRwT1c5YWFsQTNhak5FWlZrMFJYbFNSRFpKU0VKeWJUSTFaakY1ZUZKd2NHOXZXRWQzZDFneWNERjJRMGwzV0ZRck1UbERTMjloVlZReGFqTkxaMHRQVUdsQ1NWZ3ZhV05DYmxBMlpFUk1ORk5xWmxSaVRVeEllREZOUTNwQ1QzRTBUamMyVG1wb1V5OXNOQ3RuYnpsR1NXNDNSMU0xV1VFdmIyUXpRM2RMYmxwR1Z6QmFiVlkxY2xKVEsydGhWRXA0ZEZWRVNUSm5OVWh1ZURCR09GYzRjRXR4WjJJNVIySllka2R5YzIxek5HTk5ZMDVzYkZkTlMyMUxRVk5MVG1OcGFsaDVWbk5TUkV4VlRsaHFPWEV2VldWS1ZYcDFiMFpVVlRoeFFsWTFURlphU1VWWFJFTlJPV055WTBWRU5rTTJRV1V3VnpSRFQyWnJUbk5GVkhsd1ZXZ3JaMGc1UzBNcmMzaFZjSFIyTXpkcVNTOURVMkZLUnpneWRGQkNVSEpZYWpKalEzWnZVakYxVWtsMmJreDRkSG9yV0V4SWFXMXNUSEpGUlhaa1kxZFJjblJZTlRWVFowbFZaelpvV1ZCTU4xbHZla0Z1VVVKdk9XcHpVVzVMY21ObFNFd3JSMVpZVW5BdmR5OW5WelV3U1dKME1DczJVbXRMZUVaMmQxRkRWVEEyVEhnd2J6ZFJUbGxXUTFOVFZtOXplREpNVDNwRVdIcExUSGszVkRsVE1pOWxiR2RrYVhGeFdWaHVNa1EwU1V4V1JsRmllRkE1VUdodWRsbEdiMHhPZHpkSVNVc3JhM2hwUkM5VlJGWjZPWEpTYVhkcWNHZ3Zja2cxYTJWVFZFVnJha1U1T0dNcllYa3lTMnQwTVUxS1REZzNSall6VkZoUGVFSnZUbXgxU21oUlIycGtabkp0YlcxT01YSmtWRFpFUWtOcFp6azFiMk5VU1VzM1dUWm5Na2xWVmxFNFNFSktTMlo0UW5WUmRHZHVNa2QzYjBwM1kyMUxNVUpoZUdoc1JqaFNUVFl5WTB4aFdEVkdMMGROYzJGb1QzVkNTamhyWW1oek1FdDZha0l4UTJoUFdGSk5kREY0VlZWRWNFNXpjblJwTkhjeEx6RkRNa2R3Ym04MlUwOUlVV3hXVW0wekwxWTBRVk5qVEV4Mll6bENWbkJJU1VoUEt6ZG9PVTVVS3pNMlRFNUZha1kyUzBST04zRmpjVloxZUZSaWNHODNZMFpWUVV0TWR6QlZNRkZ1YWxOREx6VXpUbUpDTlZSVVNGQkhRMlpVV2tkSVJtWXZSMW8yUWtoR1JXdHBabTB2YjJKNlZsUnZSU3R2TDNaMFIyd3ZOVWhXZGtkSFQyNURURlJQYjFoeUt5OUlWbXRyTW14dWNtNXJZeXRKYjJnclJsQldPWFpKUW14dE5IWTRlR3BKTlhwS05ETldWalkxZEhKTmREZFJVQ3MzV1ZoVGFEZHBTMlZLYTBkNVFWZG9ZV2hDV21Ob2NFRTRaMUZFWmpOSWRURnFXRUZOY1RKV09YQjFaazlwVFRCWlRHSlFjWGhLTUUwNE5WZzRTbXBGV0hkMk0ydEVOVmhsUTBwT2FqRnhWR3RJT0VoSWR6aENhV2Q1YzA1c05GbEdPVFpTUkd4eloyUmlkVzVMY2pBM1NucDJRa3RJUkhKNFdYbEVNazFKZDFnNWFERTBLemxzWlRRM1pGbElielIxU0hOeGMyTktZMjFFZVZKUFluVk1WekZUVjBoR2JuVk5kVVpwYmt0T05YWXJaM0IyVUVwbWNYUjRUbTFrYldKRE1rZERVSE5YUjJkd05WUmFZVFEyV21odlowb3hORkl5TW1kdmVrTklkVzVhUjIxMlpVaGhORVJYY0U0eFRXOWxUMlJQV2xSVWRFSk5ZMnhaVlZKTU1Gb3ZUbWRwVGt4WFdrNW5UM2xpUTJOUWFXSk9NbTlyVEdsS1NVUkpSM2M0ZFVvMVNUVktPRWhtY2twRlMzQXhhRGR4ZW5nck1FRlJUSEZ1VVVjNGVUbFZVR1JDU3l0WlJEa3JaMFV5TlRFeGFrRmpUelZHY0hOb0wyeFlWbEUwZVdaVGJFWlFRaTlSVEVnek1HNVVOVmxDTkdoc1dqUmpVMWt2VHpGVFlsZExTbEp1WmtzNVJrWndRVGRFZFZGUVFsSkpUMHB3ZVRkeGQyY3pOemxCY2s4M1JsZFhiREZ3ZEdGTVpqaFdSMFJGZWtSeGNXa3hTV3Q1YjFCVWQzbEliRXh3T1hwc1QyWk1iR3BrYlV4dlF6WlpjalZrTmxWWlVVSlljMDFFYTJGaFRHeEhOMlpQTTNCek5GSm5kbXM1U1c5TGREQktaeTlTZDBWSlkyZzVUMmRHZVZKS2QwbEVRbEZyVnpOWlNtZHhTVGxTZGtFM04wcHRjVFpaVkZwcWRsWmxTMXA0T0ZSMmJWZHNVbk5zV1hkclJWSkxMM2xKZFhGeFprczNjM1JpWjJKTlFXVlljR001TkZVNVEyVnBTMVZqY1hoMU1FSkhXakJEZWpSRldFOUlNSEpRTldZNVFuTm1OVlIyUlU5cGQzQmpZblFyYXpCME5HMXVhbU5KZDNCTWNWWnpXbEZHVW1kNU1XOWxTbWRTZWpkUVpXdzJRMWhRVDNScVVISnJkWHBMU0Rac2ExbG5VSFpsVHpCaFMwZ3dWM1pJZEZVNVVGRlZMMVJHUkZNMmRXdEJNbXBTZGxGWVdFMWFZa1l6Vml0bVpsZDRUalJRZEZGVE1ucEVWVVpxY1hWWGRVUm5OekpKUTNaaFNsQkJaWEIxY1VWTGMyMW5UVEY1U25sbVkxaG1NMkZsWlVsRk9XOXlUVGRFTDBKTFduQkNUM2d6VVROc09WazVkVk5yVmtkRVFYTlVjVXhRVVZSNFUxUm9ZV2xoSzJKUGRuSnhOM0E0YzBsaVVrNU9ZalJhT1ZkVE0wWllkVmN3UjJodU5scGlXRXRyUzNnd1VXOUNWV1pFVldGUFIwUkNaelU0YTBORlNIbFhWV2xaUm1GQ2JIZDFWMHhSWlRneWJVeHhkV2haWXpKbVVqSXZWU3RoYWk5cVMzTTFZbVF3Umt4cWNVSnJWMDVRTWxKMFYwVk9UMmxEUlhCWWJsaGhZVEpxTTJsMlQwdG9aVXd2Y1dwdWNVVnpSWG81V0daMWR6TnRSR3hEVVhWU1FsRkZiR2xZZVc0M2VrWlBkWFp4Unl0RE0ycGpaazFTV1hOYWVrRkdkSGhWU2pWR1dYTnplVzR6TkdKcFZXWjFNa3RQTVRka1YxSkxWakJsZUUwemVEQnVablpKWm1ONFIzcHpjamRpU2tSSlJqWm9WVmM0VkZCa1pERklPR0pvYUU1TGNYTXhUR3BoV0dGUlozcG1kRmRMUjA1VlZuWlhNbVp2WnpseU0xVXdURk5qY1dOUFMwVm1PRkZJVmtKS1NVVkVXamhLYnpKMFl5dE1NSHBTZEZoUFZYUjNObTFhVEZaVFdFTTJVME0zVkZGWGNsWkpTR296ZVRKcU1qbGFORVptVEZoRGFtNW1ibGhLV25nemN6RXdVaTg1ZFRGUFFtSktRaXRtYzBaeU1UaEtOWFIyVVRCM2VUZzVRVFpvVUVOVWNTczRNbTFvYlVoMFNEQXhlVGRTT1VKaVpXa3ljM2gwU0VOV1VVcHhUV3RqTmxJMFdFTnpaekpuVWpRMlNITTBNMDFqUzJ0Tk1XSlljMVJpZERRd0t6aDJSMWR1TnpGeVExRnhNbEJJTDI1alkxSnVhbEJMVG1OR2IxZElZVUpJVWs5U2FXeGtZVTlITVVsd2RFeFFPVU5QZWpaT2VqbDJSa05ZTTJSMU0wSkpiazFyYW5SSWNsUXJTakptUldFM2RDOU1ZekZFVlZKUWREQmxPVkpxVDNseVUzUkxlRzR5SzNaTlVFOXRZVUZaTkZabVltMU1NVmwyUzBkbWJrOVJlVFZqWTFsR1RuTjVOM1ZFZFVWVVpqQkdjMlV3ZGpSbkx6WXhNSGg1WXpsQmMzQmFMMVI0VGxkWlpsQnFkVXM0ZEdwU0wyaHVOazFtT1VsVVNWRlFXVEExYlRJek0zRmxOVlppVFU1aU0zcEpRMkl4ZUdOblpUZEJMMXBFU0hFNWVsWk5VMFJhSzJKME56bDRWRU5QZHpNNFp6bHRjVmRuVGtaWVltSk5MMlIxZWxWQlZYZDVjbWc0U1VsUmMyRmxiRlZhUVRCc05tTkJibk41TUN0YVZrVjJkRmRPTkhSbmN5dDFRbXhQZURKSFdqaHVLMGR1ZEdKVVVqQnlaVGR3YlhORk5UTlpha0ZHVVRkV2EyVnNOWEo0TW5CMFFreEpSa0UwVFc5M1VsTmhUbmRVY0hCdVVVTXlURFZ6WVZsUVYzZG5Sa0ZSTVZjeFdYUldlRzF0ZERneU1UTkRZMDVOZVhSTFR6bGhTVU5HV25GbGRFaHlkMU40UTNObVIwRk1XREI0TVZCVWJVdFVjRFJNVVdwRmQwUm1UMjkwZFdGTlFUTjZTSGxaV1ZkMFJtWktUMk5UVUVSbVYxVnRLMWhwZW1wMmRUTk5UbnBhWW14MFkyNW9TVGQ1Wkd4dk1EVlBOekV6Y1hWcmIzZEdZVnB3YWpWRFJrMTVhSEE1WTAwNU9FZHNWV0p2U1Rod1VsY3JZVFIxVWtkaWJqQkNWM05STDNabVVVWjRTbmR4VFhkUVRuZFhWa2hhUVZNcmFqaHdabFpGVVV4b1pFUnRWa2xJVTJkNlUwRkVRelJZY25ONUwwMHZVMGRPT1U5cGR6QjNRVmd2VUVKc1kyRmxOalpRUVRsWU9FMUdhV1JwY1c5U1QzUXpRbEl4VUhwRGVuWlRSVE5tTWpZMGJDdElZM2hHY214RlNVMTVSR2QxVDJGT2FsVk1VV1l4VVV3M1pHeG9XRkpuYkRoTU5HRTRVWE56WmxST05sTXlhVWx6WTBoNVZHNHpkR2hrZFdWV1NVMWFZVmRqUWpsbFpFNVRlV05TVFRsNFVVWXhSbGxRYzFwT1QzSjFVbTFQTm5WM2FsUjBaa05CVTFOM1EzQTBhRTFUU0U0NFZteFRVbUp6ZEhJeldFNHpPWG95Wmtsb2RXUkZUaTl2U2toRU1YUTVURFJYYWpGUWJucDBTMEo0U1daV1VYWnpUbGRRY3k4eE9EZHlOVTFaTTFKSE1sWjFiVEpXUlN0Uk9XWlZNV1UwYldaRVlrNURTekp6V0hCeVdGRldhRVZMYlhKalkwOW9NR1JKYm01eVpqaDZiVEozT0dKb1pYQnNSR2xVZEU5TWFWVlJUVXRrY25GdVMwSTJja015YmtwR1RXaDJZM1JhVG5oWFRrUTRUVGxCYkZWV1JTODNXVkpTTmxocWNEbHBXRlZ0V2pOVVpsZHpRbkJaTUhwb05WbEdlRUZhV1VodmNWUnJOR2MwT0VGcVEwWm1lak5xWmxVNFMweE1MMnh5Y21FM2RVcERPVXBNUzFscU1FTnVVVkZRUm1SQ1QyVmFOWGcwVFhJM2JrcFdhRE5QUkZaWGVERjVlbmREY25GaVNFUTFjV2hxTXpScGQzbHdTamRMTWxsaFMwZG9NREU0VUN0T1UyeEpZMlZaTVZveU4zWkVkeTl4VHpscmRGcFJTMWxwSzJ4U2FVbHFkM1pJZEN0RlRGUkVVRUpWUVc1MFJtdEdOek5tZEVremJIRklWVzQ0WVZCV2FXZHpPWEZOVlRkdU5IVlJkVkJhVjJKeE1YUnFPVXB0TVhKc2JDOUZVMFJSWm5obGQxTjJZM05oYzNrMk1qVlpUbmhTVjNsUVUwUXhTRzVaVWxoT2VHSkNkbTE0WWpSSVFsUnNiWEZSZUdWSk1rWTNOVU5ZLjdrRVR5Z2tIbmp5MUp6djNFX3l3THpQa0FpcjYwUUNXeUQwdGJ3T05zeFFFRkFlYnhqdGZxU0pqMVpEclBCbkt5WDR3Zzg3UVRibmttQ1VzajI5NWp3',
                '_eventId': 'submit',
                'geolocation': '',
                'prcflag': 0,
                'client_id': '',
                'login_name': '',
                'timestamp': '',
                'signed': ''
            }
            S.post(url, data=data, headers=headers,timeout=3)
            getTockerHeaders = {
                'Origin': 'http://172.32.12.243:20529',
                'Referer': 'http://172.32.12.243:20529/operation/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'zh-Hans-CN,zh-Hans;q=0.5',
                'Content-Type': 'application/json; charset=UTF-8',
                'tokenId': '',
                'Accept-Encoding': 'gzip, deflate',
                'Content-Length': '39',
                'Host': '172.32.12.243:20529',
                'Connection': 'Keep-Alive',
                'Pragma': 'no-cache'
            }
            getTockerData = {"userNo": "sj0003"}
            response = S.post("http://172.32.12.243:20529/operation/system/casLogin.htm", data=json.dumps(getTockerData),
                              headers=getTockerHeaders)
            atoken = response.json()['atoken']
            # 拼接查询字符串
            getIMEIHeaders = {
                'Origin': 'http://172.32.12.243:20529',
                'Referer': 'http://172.32.12.243:20529/operation/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362',
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'zh-Hans-CN,zh-Hans;q=0.5',
                'Content-Type': 'application/json; charset=UTF-8',
                'tokenId': '%s' % atoken,
                'Accept-Encoding': 'gzip, deflate',
                'Content-Length': '39',
                'Host': '172.32.12.243:20529',
                'Connection': 'Keep-Alive',
                'Pragma': 'no-cache'
            }
            getIMEIData = {"phone": phone, "queryType": "1"}
            response = S.post('http://172.32.12.243:20529/operation/faceCheck/queryUserFaceCheckInfo.htm',
                              data=json.dumps(getIMEIData), headers=getIMEIHeaders)
            imei = response.json()['context']['userInfo']['imeiOid']
            if not imei:
                print("无需清除常用设备")
                return True
                # 删除常用设备
            delDeviceHeaders = getIMEIHeaders
            delData = {"imeiOid": "%s" % imei}
            response = S.post('http://172.32.12.243:20529/operation/faceCheck/deleteDevice.htm', data=json.dumps(delData),
                              headers=delDeviceHeaders)
            if response.json()['code'] == "00":
                print("清除常用设备成功")
                return True
            print("清除常用设备失败")
            return False
        except:
            print("清除常用设备失败")
            return False

    @classmethod
    def importAContact(cls,page):
        '''
        向手机插入联系人
        :return:
        '''
        from common.globall import g
        g().activePoot.adb.exe_shell_adb('pm','clear','com.android.providers.contacts')
        g().activePoot.adb.exe_cmd('push',atestVcfFile,'/sdcard/contacts.vcf')
        g().activePoot.adb.exe_shell_adb('am','start','-t','"text/x-vcard"',
                                         '-d','"file:///sdcard/Atest.vcf"',
                                         '-a','android.intent.action.VIEW',
                                         'com.android.contacts')
        if page._exists("poot(text='确定')"):
            page._click("poot(text='确定')")
        page._startTFAnYi()


    @classmethod
    def pushInitFile(cls):
        '''
        向手机推送初始化文件
        :return:
        '''
        from common.globall import g
        if g().activePoot.adb.exe_shell_adb("ls","/mnt/sdcard/.A",success="No such"):
            g().activePoot.adb.exe_cmd('push',afile,'/mnt/sdcard/')
        if g().activePoot.adb.exe_shell_adb("ls", "/mnt/sdcard/.A1", success="No such"):
            g().activePoot.adb.exe_cmd('push',a1file,'/mnt/sdcard/')

#装饰器指定ui组的方法
def ui(*module):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self,*args,**kwargs):
            from common.globall import g
            tempModule=g().module
            g().clearModule()
            for m in module:
                g().addModule(m)
            try:
                ret=func(self,*args,**kwargs)
            except:
                raise
            else:
                return ret
            finally:
                g().module=tempModule
        return wrapper
    return decorator


# tools().textProgress("123456")
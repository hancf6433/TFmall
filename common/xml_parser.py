# -*- coding:utf-8 -*-
"""
    author: Li Junxian
    function: parse xml file
"""
import os
from xml.sax.handler import ContentHandler, feature_namespaces
from xml.sax import make_parser


class XmlHandler(ContentHandler):
    """
    xml handler
    """

    def __init__(self):
        super().__init__()
        # 当前节点的字典结构
        self.__active_element = None
        # 用来保存当前节点的文本
        self.__active_element_text = ""
        # 用来保存xml结构的栈区
        self.__stack_of_saving_xml_structure = []

    def startElement(self, name, attribute):
        # 遇到一个节点，以节点的名字作为参数,属性值为其字典内容
        if self.__active_element:
            # 如果当前节点不为空，则将当前节点置入栈区
            self.__stack_of_saving_xml_structure.append(self.__active_element)
        at=getattr(attribute, "_attrs")
        self.__active_element = {name: at}

    def characters(self, content):
        if content=="\n":
            return
        if content.strip()=="":
            return
        if content is None or len(content.strip()) == 0:
            return
        if content[-1]=="|":
            self.__active_element_text +=content[:-1]
        else:
            self.__active_element_text += content.strip()

    def endElement(self, name):
        # 其节点的文本内容作为value值,当节点只有文本内容时，则直接赋值给当前节点
        active_element = self.__active_element
        active_element_name = self.__active_element.copy().popitem()[0]
        if self.__active_element_text is not "":
            active_element_value = self.__active_element[active_element_name]
            if len(active_element_value) <= 0:
                active_element[active_element_name] = self.__active_element_text
            else:
                active_element_value['$value'] = self.__active_element_text
            self.__active_element_text = ""
        # 如果堆栈里还有元素，需要处理
        if len(self.__stack_of_saving_xml_structure) <= 0:
            return
        # 从堆栈里弹出最顶上的元素
        pre_element = self.__stack_of_saving_xml_structure.pop()
        pre_element_name = pre_element.copy().popitem()[0]
        # 判断最顶上元素的节点名字对应的值是否为空
        pre_element_value = pre_element[pre_element_name]
        # 再判断对应值是否存在当前元素的名字
        if not pre_element_value.get(active_element_name):
            # 当没有时，将当前元素直接写入
            pre_element_value[active_element_name] = active_element[active_element_name]
        else:
            # 当有时，将其提取出来的值判断是否是数组
            temp = pre_element_value.get(active_element_name)
            if type(temp) == list:
                # 是数组，追加当前元素内容
                temp.append(active_element[active_element_name])
            else:
                # 是字典，合并两个元素内容为数组
                pre_element_value[active_element_name] = [temp, active_element[active_element_name]]
        # 再将当前元素替换为最顶元素
        self.__active_element = pre_element

    @property
    def xml(self):
        return self.__active_element


class XmlParser(object):
    """
    xml 解析器
    """

    def __init__(self, xml_file: str):
        """
        xml 解析器
        :param xml_file: 需要解析的xml文件
        :return: None
        """
        self.__xml_file = xml_file

    def parse_xml(self) -> dict:
        """
        取得xml解析的结果
        :return: 由xml文件构成的字典值
        """
        parser = make_parser()
        parser.setFeature(feature_namespaces, 0)
        handler = XmlHandler()
        parser.setContentHandler(handler)
        if not os.path.exists(self.__xml_file):
            raise BaseException("对应的数据xml文件[{}]不存在，请检查test_data目录".format(self.__xml_file))
        try:
            parser.parse(self.__xml_file)
        except BaseException as e:
            raise BaseException("解析xml文件[{}]错误，错误原因：{}".format(self.__xml_file,str(e)))
        return handler.xml

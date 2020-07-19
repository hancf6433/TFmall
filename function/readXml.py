# -*- coding: utf-8 -*-
"""
    解析xml元素
    @Author  : hancf
    @Time    : 2020/7/17
    @Comment : 商家登录、券码等信息
"""

from xml.dom.minidom import parse
import os
def readxml(tagName):
    '''登录信息'''
    file_path=os.path.dirname(__file__)
    data_path=os.path.join(os.path.dirname(file_path),"data")
    xml=os.path.join(data_path,"test_data.xml")
    domTree = parse(xml)                                               # minidom解析器打开xml文档并将其解析未内存中的一棵树
    rootNode = domTree.documentElement                                 # 获取xml文档对象，就是难道树的根
    data = rootNode.getElementsByTagName(tagName)[0].firstChild.data   #获取rootnode对象中所有节点的集合
    return data
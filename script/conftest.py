# -*- coding: utf-8 -*- 
# @Time : 2021/9/18 17:41 
# @Author : Corn
# @File : conftest.py
'''
conftest.py固定的名字
钩子函数(hook)
pytest_collection_modifyitems(items):这个函数的运行机制
收集测试用例[,,,,]
items：测试用例
'''
def pytest_collection_modifyitems(items):
    '''
        收集测试用例,对每一个测试用例进行处理
    	encode编码都是utf-8的一个编码
    	unicode_escape将unicode的内存编码值进行存储，读取文件的时候再反向转换回来，
        :param items: 测试用例集合
        :return:
        '''
    print('测试用例的集合是:',items)
    for item in items:
        item.name = item.name.encode().decode('unicode_escape')
        item._nodeid = item.nodeid.encode().decode('unicode_escape')
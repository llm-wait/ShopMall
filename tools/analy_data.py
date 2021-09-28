# -*- coding: utf-8 -*- 
# @Time : 2021/9/23 15:38 
# @Author : Corn
# @File : analy_data.py
import yaml

from Review.Week9.apiFrame import config


def analyze_data(filename,key):
    '''
        解析yml文件，得到一个列表嵌套字典的数据格式
        :param filename: login_data.yml
        :param key: test_login
        :return: 列表嵌套字典的数据格式
    '''
    with open(config.DIR_NAME + '/data/%s.yml' % filename, 'r', encoding='utf-8') as f:
        data_list = list()
        yaml_data = yaml.load(f, Loader=yaml.FullLoader)
        # print(f'yaml_data的值是{yaml_data}')
        pre_value = yaml_data.get(key)
        li = pre_value.values()
        data_list.extend(li)
        return data_list

if __name__ == '__main__':
    filename= "logindata"
    a=analyze_data(filename, "test_login")
    print(a)
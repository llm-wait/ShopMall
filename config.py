# -*- coding: utf-8 -*- 
# @Time : 2021/9/23 10:59 
# @Author : Corn
# @File : config.py
import os

IP="http://121.42.15.146:9090"
HEADERS = {'X-Requested-With':'XMLHttpRequest'}
ABS_PATH=os.path.abspath(__file__)
DIR_NAME=os.path.dirname(ABS_PATH)
JUMP_URL=None
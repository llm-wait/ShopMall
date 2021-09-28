# -*- coding: utf-8 -*- 
# @Time : 2021/9/23 11:03 
# @Author : Corn
# @File : loginapi.py
import requests

from Review.Week9.apiFrame.config import IP, HEADERS


class MTXLogin:
    def __init__(self):
        self.url=IP+'/mtx/index.php?s=/index/user/login.html'
    def login(self,session,data):
        resp_login=session.post(self.url,data=data,headers=HEADERS)
        return  resp_login
    def login_success(self,session):
        data={'accounts': 'yaoyao', 'pwd':'yaoyao'}
        resp_login_success=session.post(self.url,data=data,headers=HEADERS)
        return resp_login_success

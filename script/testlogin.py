# -*- coding: utf-8 -*- 
# @Time : 2021/9/23 11:10 
# @Author : Corn
# @File : testlogin.py
import os

import allure
import pytest
import requests

from Review.Week9.apiFrame.api.loginapi import MTXLogin
from Review.Week9.apiFrame.tools.analy_data import analyze_data

login_data=analyze_data('logindata',"test_login")
ids=['账号有误','密码格式错误','账号不存在','密码错误']
class TestLogin:
    def setup_class(self):
        self.session=requests.Session()
        self.login_obj=MTXLogin()

    @pytest.mark.parametrize("args",login_data,ids=ids)
    @allure.title("异常登录接口测试用例,测试数据是{args}")
    @allure.story('登录逆向接口的测试')
    def testlogin(self,args):
        data = {'accounts':args["accounts"], 'pwd': args["pwd"]}
        resp_login = self.login_obj.login(self.session,data)
        assert  resp_login.json()["msg"] ==args["exp"]

    @allure.story('登录正向接口的测试')
    @allure.title("正向登录接口测试用例,测试数据是用户名：yaoyao,密码：yaoyao")
    def testlogin_success(self):
        resp_login=self.login_obj.login_success(self.session)
        assert  resp_login.json()["msg"] =="登录成功"


# -*- coding: utf-8 -*- 
# @Time : 2021/9/24 14:41 
# @Author : Corn
# @File : testorder.py
import allure
import requests

from Review.Week9.apiFrame.api.loginapi import MTXLogin
from Review.Week9.apiFrame.api.orderapi import Order


class TestOrder:
     def setup_class(self):
         self.session=requests.Session()
         self.order_obj=Order()
         # 调用成功的登录接口
         MTXLogin().login_success(self.session)

     @allure.story('提交订单接口的测试')
     @allure.title('提交订单正向接口测试用例')
     def testorder(self):
         '''
            依赖于登录：api级别的，请求级别，完全独立
            :return:
        '''
         resp_order=self.order_obj.order(self.session)
         print(resp_order.json())
         assert resp_order.json()["msg"]=="提交成功"

     @allure.story('提交订单接口的测试')
     @allure.title('提交订单逆向接口测试用例')
     def test_order_error(self):
         # 调用成功的登录接口
         # MtxLogin().login_success(self.session)
         pass


# -*- coding: utf-8 -*- 
# @Time : 2021/9/24 15:18 
# @Author : Corn
# @File : testpayorder.py
import allure
import requests

from Review.Week9.apiFrame.api.loginapi import MTXLogin
from Review.Week9.apiFrame.api.orderapi import Order
from Review.Week9.apiFrame.api.payorderapi import PayOrder
class TestPayOrder:
    def setup_class(self):
        self.session = requests.Session()
        # 实例化支付接口
        self.payorder_obj = PayOrder()
        # 调用成功的登录接口
        MTXLogin().login_success(self.session)
        # 调用提交订单的接口--->jump_url 数据提取 数据关联
        Order().order(self.session)

    @allure.story('支付接口的测试')
    @allure.title('支付接口测试用例')
    def test_payorder(self):
        '''
        对支付接口进行测试
        :return:
        '''
        # 请求支付接口
        resp_pay = self.payorder_obj.pay_order(self.session)
        # 断言
        assert "支付成功" in resp_pay.text


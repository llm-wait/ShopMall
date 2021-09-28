# -*- coding: utf-8 -*- 
# @Time : 2021/9/24 15:03 
# @Author : Corn
# @File : payorderapi.py
import allure
import requests

from Review.Week9.apiFrame import config
from Review.Week9.apiFrame.api.loginapi import MTXLogin
from Review.Week9.apiFrame.api.orderapi import Order
from Review.Week9.apiFrame.config import IP
from Review.Week9.apiFrame.tools.logger import GetLog

log = GetLog().get_logger()
class PayOrder:
    def __init__(self):
        '''
        这个支付接口是需要重定向，302的url是从提交订单的接口里面获取jump_url
        '''
        # 消费数据
        self.url = config.JUMP_URL
        log.info(f'支付接口的url是{self.url}')

    @allure.story('支付接口的测试')
    @allure.title('支付接口测试用例')
    def pay_order(self, session):
        # 对302接口进行处理，不让其重定向 allow_redirects=False
        resp = session.get(self.url,allow_redirects=False)
        log.info(f'支付的302跳转接口的响应是{resp}')
        log.info(f'支付的302跳转接口的响应头的location是{resp.headers["location"]}')
        resp_pay = session.get(resp.headers['location'])
        return resp_pay

if __name__ == '__main__':
    print(config.JUMP_URL)
    s = requests.Session()
    MTXLogin().login_success(s)
    Order().order(s)
    print(config.JUMP_URL)
    print(PayOrder().pay_order(s).text)
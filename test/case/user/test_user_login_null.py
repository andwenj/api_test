"""
import unittest  # 导入unittest
import requests
import json
import os
import sys
sys.path.append("../..")
from lib.read_excel import *
from config.config import  *
from lib.case_log import log_case_info

class TestUserLoginnull(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path,"test_user_data.xlsx"),"TestUserLoginnull")

    def test_user_login_name_null(self):
        case_data = get_test_data(self.data_list,'test_user_login_name_null')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')

        res = requests.post(url=url,data=json.loads(data))
        log_case_info('test_user_login_name_null', url, data, expect_res, res.text)
        self.assertIn(expect_res,res.text)

    def test_user_login_pwd_null(self):
        case_data = get_test_data(self.data_list,'test_user_login_pwd_null')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')

        res = requests.post(url=url,data=json.loads(data))
        log_case_info('test_user_login_pwd_null', url, data, expect_res, res.text)
        self.assertIn(expect_res,res.text)


#==============================最原始的请求==============================
class TestUserLoginnull(unittest.TestCase):  # 类必须Test开头，继承TestCase才能识别为用例类
    url = 'http://127.0.0.1:8888/login'

    def test_user_login_name_null(self):  # 一条测试用例，必须test_开头
        data = {"name": "", "pwd": "111"}
        res = requests.post(url=self.url, data=data)
            self.assertIn('参数不能为空', res.text)  # 断言,assertIn(a,b) b中是否包含a

    def test_user_login_pwd_null(self):
        data = {"name": "张三", "pwd": ""}
        res = requests.post(url=self.url, data=data)
        self.assertIn('参数不能为空', res.text)  # 断言
#================================请求的结束=================================
"""


from test.case.basecase import BaseCase

class TestUserLoginNull(BaseCase):
    def test_user_login_name_null(self):
        """Level1 用户名为空"""
        case_data = self.get_case_data("test_user_login_name_null")
        self.send_request(case_data)

    def test_user_login_pwd_null(self):
        """密码为空"""
        case_data = self.get_case_data("test_user_login_pwd_null")
        self.send_request(case_data)

if __name__ == '__main__':  # 如果是直接从当前模块执行（非别的模块调用本模块）
    unittest.main(verbosity=2)

"""
import unittest
import requests
import  json
import  os
import  sys
sys.path.append("../..")    #提升两级到跟目录下
from lib.read_excel import *  #从项目路径下导入
from config.config import *  #从项目路径下导入
from lib.case_log import log_case_info  #从项目路径下导入

class TestUserLogin(unittest.TestCase):  # 类必须Test开头，继承TestCase才能识别为用例类

    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list(os.path.join(data_path,"test_user_data.xlsx"),"TestUserLogin")

    def test_user_login_normal(self):
        case_data = get_test_data(self.data_list,'test_user_login_normal')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')

        res = requests.post(url=url,data=json.loads(data))
        log_case_info('test_user_login_normal',url,data,expect_res,res.text)
        self.assertIn(expect_res,res.text)

    def test_user_login_wrong(self):
        case_data = get_test_data(self.data_list,'test_user_login_wrong')
        if not case_data:
            logging.error("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')

        res = requests.post(url=url,data=json.loads(data))
        log_case_info('test_user_login_wrong', url, data, expect_res, res.text)
        self.assertIn(expect_res,res.text)


##最原始的request请求
    url = 'http://127.0.0.1:8888/login'

    def test_user_login_normal(self):  # 一条测试用例，必须test_开头
        data = {"name": "xiaoming", "pwd": "111"}
        res = requests.post(url=self.url, data=data)
        self.assertIn('登录成功', res.text)  # 断言,assertIn(a,b) b中是否包含a

    def test_user_login_password_wrong(self):
        data = {"name": "张三", "pwd": "1234567"}
        res = requests.post(url=self.url, data=data)
        self.assertIn('账号密码错误', res.text)  # 断言

"""



#以下是分割线
from test.case.basecase import BaseCase

class TestUserLogin(BaseCase):
    def test_user_login_normal(self):
        """Level1 正常登陆"""
        case_data = self.get_case_data("test_user_login_normal")
        self.send_request(case_data)

    def test_user_login_wrong(self):
        """密码错误登陆"""
        case_data = self.get_case_data("test_user_login_wrong")
        self.send_request(case_data)




if __name__ == '__main__':  # 如果是直接从当前模块执行（非别的模块调用本模块）
    unittest.main(verbosity=2)
















import unittest

'''
#TestSuite

from test_user_login import TestUserLogin
from test_user_login_null import TestUserLoginnull

suite = unittest.TestSuite()
suite.addTest(TestUserLogin('test_user_login_normal'))#添加单个用例
suite.addTests([TestUserLoginnull('test_user_login_name_null'),TestUserLoginnull('test_user_login_pwd_null')])#添加多个用例

unittest.TextTestRunner(verbosity=2).run(suite)

'''

#使用discover（用例发现）遍历所有的用例
#子目录中需要包含__init__.py文件，及应为的Python包
#所有用例因为test_*.py,包含测试类应以Test开头，并继承unittest.TestCase, 用例应以test_开头

suite = unittest.defaultTestLoader.discover("./")#遍历当前目录及子目录中所有test_*.py中的所有unit test用例
unittest.TextTestRunner(verbosity=2).run(suite)

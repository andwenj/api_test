import  unittest
import  sys
sys.path.append("../..")

from test.case.user.test_user_login import TestUserLogin
from test.case.user.test_user_login_null import TestUserLoginNull
smoke_suite = unittest.TestSuite()
smoke_suite.addTests([TestUserLogin('test_user_login_normal'),TestUserLoginNull('test_user_login_name_null')])

def get_suite(suite_name):
    return globals().get(suite_name)
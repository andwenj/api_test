import  logging
import os
import time
from optparse import OptionParser


today = time.strftime('%Y%m%d',time.localtime())
now = time.strftime('%Y%m%d_%H%M%S',time.localtime())

#项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #当前文件的绝对路径的上一级，__file__指当前文件
#print(prj_path)

data_path = os.path.join(prj_path,'data')   #数据目录
test_path = os.path.join(prj_path,'test')   #用例目录
test_case_path = os.path.join(prj_path, 'test', 'case')   # 用例目录


data_file = os.path.join(prj_path, 'data', 'test_user_data.xlsx')
last_fails_file = os.path.join(prj_path, 'last_failures.pickle')

log_file = os.path.join(prj_path,'log','log_{}.txt'.format(today))   #日志路径，按天保存
report_file = os.path.join(prj_path,'report','report_{}.html'.format(now))     #报告路径,按当前时间保存

#log配置
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s [%(funcName)s:%(filename)s,%(lineno)d] %(message)s',#log对格式
                    datefmt='%Y-%m-%d %H:%M:%S',#日期格式
                    filename=log_file,#日志输出文件
                    filemode='a'#追加模式
                    )

#数据库配置
db_host = '127.0.0.1'
db_port = 3306
db_user = 'test'
db_passwd = '123456'
db = 'test_db'

#邮件配置
send_email_after_run = True
smtp_server = 'smtp.163.com'
smtp_user = 'andwenj@163.com'
smtp_passwd = 'wj252310' # 授权码，非邮箱登陆密码

sender = 'andwenj@163.com'
receiver = '1184865395@qq.com'
subject = '接口测试报告1212'


# 命令行选项
parser = OptionParser()

parser.add_option('--collect-only', action='store_true', dest='collect_only', help='仅列出所有用例')
parser.add_option('--rerun-fails', action='store_true', dest='rerun_fails', help='运行上次失败的用例')
parser.add_option('--testlist', action='store_true', dest='testlist', help='运行test/testlist.txt列表指定用例')

parser.add_option('--testsuite', action='store', dest='testsuite', help='运行指定的TestSuite')
parser.add_option('--tag', action='store', dest='tag', help='运行指定tag的用例')

(options, args) = parser.parse_args()  # 应用选项（使生效）

'''

--conllect-only'是参数名，dest='collect-only'指存储到 options.collect_only变量中，'store_true'指，如果有该参数，options.collect_only=True
'store'指将--testsuite='smoke_suite'，参数的值'smoke_suite'存到options.testsuite变量中

作者：韩志超
链接：<a href='https://www.jianshu.com/p/ed82716eef58'>https://www.jianshu.com/p/ed82716eef58</a>
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
#if __name__=="__main__":
#   logging.info("hello")
'''

print("1")
"""
Log Level:

CRITICAL: 用于输出严重错误信息
ERROR: 用于输出错误信息
WARNING: 用于输出警示信息
INFO: 用于输出一些提升信息
DEBUG: 用于输出一些调试信息

优先级 CRITICAL > ERROR > WARNING > INFO > DEBUG
指定level = logging.DEBUG   所有等级大于等于DEBUG的信息都会输出
若指定level = logging.ERROR   WARNING,INFO,DEBUG小于设置级别的信息不会输出

日志格式:

%(levelno)s: 打印日志级别的数值
%(levelname)s: 打印日志级别名称
%(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s: 打印当前执行程序名
%(funcName)s: 打印日志的当前函数
%(lineno)d: 打印日志的当前行号
%(asctime)s: 打印日志的时间
%(thread)d: 打印线程ID
%(threadName)s: 打印线程名称
%(process)d: 打印进程ID
%(message)s: 打印日志信息

"""
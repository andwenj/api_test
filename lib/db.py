import  pymysql
import  sys
sys.path.append('..')   #提升一级到项目跟目录下
from config.config import  *   #从项目根目录下导入

#获取连接方法
def get_db_conn():
    conn = pymysql.connect(host=db_host,
                           port=db_port,
                           user=db_user,
                           passwd=db_passwd,
                           db=db,
                           charset='utf-8')

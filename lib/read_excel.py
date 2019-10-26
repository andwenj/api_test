import  xlrd
import json


def excel_to_list(data_file,sheet):
    data_list = []#新建个空列表，用来装所有数据
    wb = xlrd.open_workbook(data_file)#打开Excel
    sh = wb.sheet_by_name(sheet)#获取工作簿
    header = sh.row_values(0)#获取标题行数据

    for i in range(1,sh.nrows):#跳过标题行，从第二行开始取数据
        d = dict(zip(header , sh.row_values(i)))#将标题每行数据组成字典
        data_list.append(d)

    return data_list  #列表嵌套字典格式，每个元素是一个字典
#data_list = ['{"method": "post", "data": {"name": "xiaoming", "pwd": "111"}, "expect_res": "登录成功"}','{"method": "post", "data": {"name": "xiaoming", "pwd": "111"}, "expect_res": "登录成功"}']


def get_test_data(data_list,case_name):
    for case_data in data_list:
        if case_name == case_data['case_name']:  #如果字典数据中case _name与参数一致
            return case_data
        #查询不到会返回none


if __name__=="__main__":
    data_list = excel_to_list("test_user_data.xlsx","TestUserLogin") #读取aaa.xlsx文件名叫b的sheet页

    case_data = get_test_data(data_list,"test_user_login_normal")#查找用例a的数
    print(case_data)

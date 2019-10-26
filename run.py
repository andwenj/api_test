import unittest

from lib.HTMLTestReportCN import  HTMLTestRunner
from config.config import *
from lib.sendEmail import  send_email
from  test.suite.test_suites import *
import time
import pickle
import sys
from config.config import *



def discover():
    return  unittest.defaultTestLoader.discover(test_case_path)

def run(suite):
    logging.info("=====================================测试开始=====================================")

    with open(report_file, 'wb') as f:
        #结果赋予result变量
        result = HTMLTestRunner(stream=f, title="API Test", description="测试描述", tester='文静').run(suite)
    if result.failures:
        save_failures(result,last_fails_file)

    if send_email_after_run:#是否发送邮件，默认是关闭的
        send_email(report_file)
    logging.info('=====================================测试结束=====================================')

def run_all():
    run(discover())


def run_suite(suite_name):
    suite = get_suite(suite_name)
    if suite:
        run(suite)
    else:print("TestSuite不存在")


def collect():
    suite = unittest.TestSuite()

    def _collect(tests):
        if isinstance(tests,unittest.TestSuite):
            if tests.countTestCases() != 0:
                for i in tests:
                    _collect(i)
        else:
            suite.addTest(tests)
    _collect(discover())
    return suite

def collect_only():
    t0 = time.time()
    i =0
    for case in collect():
        i+=1
        print("{}.{}".format(str(i),case.id()))
        print("-------------------------------------------------------------------------")
        print("Collect {} tests is {:.3f}s".format(str(i),time.time()-t0))


def makesuite_by_testlist(testlist_file):  # test_list_file配置在config/config.py中
    with open(testlist_file) as f:
        testlist = f.readlines()

    testlist = [i.strip() for i in testlist if not i.startswith("#")]   # 去掉每行结尾的"/n"和 #号开头的行

    suite = unittest.TestSuite()
    all_cases = collect()  # 所有用例
    for case in all_cases:  # 从所有用例中匹配用例方法名
        if case._testMethodName in testlist:
            suite.addTest(case)
    return suite


def makesuite_by_tag(tag):
    suite = unittest.TestSuite()
    for case in collect():
        if case._testMethodDoc and tag in case._testMethodDoc:  # 如果用例方法存在docstring,并且docstring中包含本标签
            suite.addTest(case)
    return suite

def save_failures(result, file):   # file为序列化保存的文件名，配置在config/config.py中
    suite = unittest.TestSuite()
    for case_result in result.failures:   # 组装TestSuite
        suite.addTest(case_result[0])   # case_result是个元祖，第一个元素是用例对象，后面是失败原因等等

    with open(file, 'wb') as f:
        pickle.dump(suite, f)    # 序列化到指定文件

def rerun_fails():  # 失败用例重跑方法
    sys.path.append(test_case_path)   # 需要将用例路径添加到包搜索路径中，不然反序列化TestSuite会找不到用例
    with open(last_fails_file, 'rb') as f:
        suite = pickle.load(f)    # 反序列化得到TestSuite
    run(suite)


def main():
    if options.collect_only:    # 如果指定了--collect-only参数
        collect_only()
    elif options.rerun_fails:    # 如果指定了--rerun-fails参数
        rerun_fails()
    elif options.testlist:    # 如果指定了--testlist参数
        run(makesuite_by_testlist(testlist_file))
    elif options.testsuite:  # 如果指定了--testsuite=***
        run_suite(options.testsuite)
    elif options.tag:  # 如果指定了--tag=***
        run(makesuite_by_tag(options.tag))
    else:   # 否则，运行所有用例
        run_all()

if __name__ == '__main__':
    main()   # 调用main()


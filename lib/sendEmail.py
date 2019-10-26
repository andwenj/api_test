"""
发送邮件分3步
    编写邮件内容（Email邮件需要专门的MIME格式）
    组装Email头（发件人，收件人，主题）
    连接smtp服务器并发送邮件

import smtplib #用于建立smtp连接
from email.mime.text import MIMEText #引入邮件专门需要的 MIME格式

#1 编写邮件内容
msg = MIMEText('this is a email','plain','utf-8')#plain指普通文本格式邮件内容

#2 组装Email头 （发件人，收件人，主题）
msg['From'] = 'andwenj@163.com' #发件人
msg['To'] = '1184865395@qq.com'#收件人
msg['Subject'] = 'APi Test Report -----wenjing'#邮件主题

#3 连接smtp服务器并发送邮件
smtp = smtplib.SMTP_SSL('smtp.163.com') #smtp服务器地址，使用SSL模式
smtp.login('andwenj@163.com','wj252310')#登陆自己的邮箱地址和授权码——注意，不是邮箱密码
smtp.sendmail("andwenj@163.com","1184865395@qq.com",  msg.as_string())#发送固定格式：(sender, receivers, message.as_string())
#smtp.sendmail('1184865395@qq.com', msg.as_string())
smtp.quit()

"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 混合MIME格式，支持上传附件
from email.header import Header  # 用于使用中文邮件主题
from config.config import *


def send_email(report_file):
    msg = MIMEMultipart()  # 混合MIME格式
    msg.attach(MIMEText(open(report_file, encoding='utf-8').read(), 'html', 'utf-8'))  # 添加html格式邮件正文（会丢失css格式）

    msg['From'] = 'andwenj@163.com'  # 发件人
    msg['To'] = '1184865395@qq.com'  # 收件人
    msg['Subject'] = Header(subject, 'utf-8')  # 中文邮件主题，指定utf-8编码

    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')  # 二进制格式打开
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="{}"'.format(report_file)  # filename为邮件中附件显示的名字
    msg.attach(att1)

    try:
        smtp = smtplib.SMTP_SSL(smtp_server)  # smtp服务器地址 使用SSL模式
        smtp.login(smtp_user,smtp_passwd)  # 用户名和密码
        smtp.sendmail(sender,receiver, msg.as_string())
        #smtp.sendmail("test_results@sina.com", "superhin@126.com", msg.as_string())  # 发送给另一个邮箱
        logging.info("邮件发送完成！")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()

#if __name__=='__main__':
#   send_email('report.html')

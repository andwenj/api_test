import requests

'''

s = requests.session() # 新建一个会话
s.post(url="https://demo.fastadmin.net/admin/index/login.html",data={"username":"admin","password":"123456"}) # 发送登录请求
res = s.get("https://demo.fastadmin.net/admin/dashboard?ref=addtabs") # 使用同一个会话发送get请求，可以保持登录状态
print(res.text)
'''


cookies = {"PHPSESSID":"0cece3c6f8b704992591d3169fb69b1a"}
url = "https://demo.fastadmin.net/admin/dashboard?ref=addtabs"
res = requests.get(url=url,cookies=cookies)
print(res.text)

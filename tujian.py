
# -!- coding: utf-8 -!- 
# @Author:r90tpass
#本脚本使用的是图鉴的接口，直接在60行，写上自己的账号密码就能使用了。
#可以把方法嵌套在爆破脚本中使用学习。姿势很多自行扩展
import base64
import json
import requests
import random
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def getHead():
    head = {
        "Cookie":"sensorsdata2020jssdkcross=%7B%22distinct_id%22%3A%223178031982343587%22%2C%22%24device_id%22%3A%2217567e94572894-055c8dc0f3c8da-c781f38-1327104-17567e94573a0d%22%2C%22props%22%3A%7B%7D%2C%22first_id%22%3A%2217567e94572894-055c8dc0f3c8da-c781f38-1327104-17567e94573a0d%22%7D; OMS_SESSION_ID=a3686c44Zec3b1a52Z17596455d4fZ87e2; Hm_lvt_6629c25d74c5fd41b0603042cc6e5eea=1604546450,1604546454,1604546463,1604546515; Hm_lpvt_6629c25d74c5fd41b0603042cc6e5eea=1604559201",
        "User-Agent": "Mozilla@2f5.0%20%28Macintosh%3b%20Intel%20Mac%20OS%20X%2010_15_6%29%20AppleWebKit@2f537.36%20%28KHTML,%20like%20Gecko%29%20Chrome@2f79.0.3945.79%20Safari@2f537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
           }
    return head
def ranstr(num):
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    salt = ''
    for i in range(num):
        salt += random.choice(H)

    return salt
#获取新的图片验证码
def getNewVerImg():
    try:
        head = getHead()
        #输入产生验证码的地址
        res = requests.get('https://xxx'+ranstr(12), headers=head, verify=False)
        try:
            return res.content
            print(res.content)
        except:
            return res.content
    except Exception as err:
        print(err)
        print('xxxx')
        exit()
        return getNewVerImg()
#进行图片验证码识别
def base64_api(uname,pwd):
    base64_data = base64.b64encode(getNewVerImg())
    b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "image": b64}
    #验证码类型typeid(默认 3 数英混合)：7:无感学习（最吊的）66: 问答题，34:多缺口滑块(返回X轴坐标)， 33:单缺口滑块(返回X轴坐标)， 32:通用文字识别(证件、单据)， 16:汉字， 14:图片旋转， 1005:快速计算题，11:计算题，4:闪动GIF， 1003:数英混合2，3:数英混合， 1002:纯英文2，2:纯英文，1001:纯数字2， 1:纯数字
    result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
    if result['success']:
        print("识别成功，验证码是：")
        print(result["data"]["result"])
        return result["data"]["result"]
    else:
        print("识别失败，错误信息是：")
        print(result["message"])
        return result["message"]
    return ""
if __name__ == "__main__":
    result = base64_api(uname='', pwd='')
    # print(result)
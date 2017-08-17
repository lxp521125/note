# -*- coding: utf-8 -*-
import requests
# 引入NLP SDK
from aip import AipNlp

# 定义常量
APP_ID = '10005313'
API_KEY = 'Xpoe4WK3gewhgF1wCE9R6T1d'
SECRET_KEY = '6x6sNMMXvUWkvRw7Zjf3E1mqijjmus0i'

# 初始化AipNlp对象
aipNlp = AipNlp(APP_ID, API_KEY, SECRET_KEY)


def toword(title):
    # result = aipNlp.dnnlm(title)
    result = aipNlp.lexer(title)
    # result = aipNlp.sentimentClassify(title)
    print(result)
    # url = "http://apis.baidu.com/apistore/pullword/words"
    # headers = { "apikey" : "02b4266363907681c6582d605b6dabb1" }
    # # req = urllib.request.Request(url, 'data', headers)
    # params = { "source": title, "param1" : 0.8, "param2" : 1}
    # response = requests.get(url, params = params , headers = headers)
    # the_page = response.text.encode('utf-8')
    # print(the_page)
    # if len(the_page)>300:
    #     return
    # new_s = the_page.split()
    # for i in new_s:
    #     print(i)

if __name__ == '__main__':
    toword('挺好的，乐捐要继续执行下去，每星期周会不参加的都要乐捐')
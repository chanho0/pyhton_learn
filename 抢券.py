import datetime
import os
import re
import requests

#os.environ['JD_COOKIE']=""
url="https://api.m.jd.com/client.action?functionId=lite_newBabelAwardCollection&body=%7B%22activityId%22%3A%22UEro4WAa7vEhMypakgZQQDqfZhU%22%2C%22scene%22%3A%221%22%2C%22args%22%3A%22key=48BCEF1C9DFC2F254CD64C68D27A373E8419F6EC4E850C8035BC1671F5D6E4F2A3254C1957F77E9B9946E36A0A5967AB_bingo,roleId=DB74E57324B1DD95676E8AD1799695AC_bingo,strengthenKey=D6E5C5BA40D5F2138DE98E6FD33F0645DBA58C31063210FCADC4BDDB9932C0170524FB5AFF9AB805449CC46BDC3C44B0_bingo%22%2C%22mitemAddrId%22%3A%22%22%2C%22geo%22%3A%7B%22lng%22%3A%22%22%2C%22lat%22%3A%22%22%7D%7D&client=wh5&clientVersion=1.0.0"
targettime = '18:00:00'
def main():
    countdown(targettime)
    cookie_list=get_cookie()
    for e,cookie in enumerate(cookie_list):
        print(f'******开始【账号 {e+1}】 {get_pin(cookie)} *********\n')
        print(task_url(url,cookie))

def task_url(url,cookie):
    payload={}
    headers = {
    'cookie': cookie,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return(response.text)


def countdown(targettime):
    nowtime = datetime.datetime.now()
    starttime =nowtime.strftime('%Y-%m-%d ')+targettime
    starttime_format = datetime.datetime.strptime(starttime,"%Y-%m-%d %H:%M:%S")
    waittime = starttime_format - nowtime
    print(waittime)

def get_pin(cookie):
    return re.compile(r'pt_pin=(.+?);').findall(cookie)[0]

def get_cookie():
    cookie_list= os.environ['JD_COOKIE'].split('&')
    return cookie_list


if __name__ == '__main__':
    main()
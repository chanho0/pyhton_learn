#https://www.wrnxr.cn/456.html教程
import json
from random import randint
import requests
import time
from flask import Flask, make_response, request
#wrnxr.cn仙人小站欢迎您的光临
app = Flask(__name__)

img_path = str(r'E:/二次元图包20652张/P4-5467/A/')#这里是图片包的路径，改成你自己的


@app.route('/', methods=['GET'])
def display_img():
    fn = randint(1, 2000)#这里(1,2000)是图片ID范围
    filename = (str(fn) + '.jpg')
    image_data = open(img_path + filename, "rb").read()
    response = make_response(image_data)
    response.headers['Content-Type'] = 'image/jpg'
    time_now=(time.strftime('%Y-%m-%d %H:%M:%S'))
    result = time_now + '  请求的图片ID：' + str(fn)+ ' \n'
    print(time_now + '  请求的图片ID：' + str(fn) )
    write_log = open('log.txt', mode='a+')
    write_log.write(result.__str__())
    write_log.close()
    return response


if __name__ == '__main__':
    app.run()


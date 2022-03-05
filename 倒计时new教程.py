import datetime  #时间戳
import time  #时间包，控制程序休眠

now = datetime.datetime.now()
print('logintime:',now.strftime('%Y-%m-%d %H:%M:%S'))
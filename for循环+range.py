from cgi import print_directory
from msilib.schema import Directory
from tokenize import Number


#列表
list=['1','2']
contact ={'陈':'130','方':'132'} 

#字典读取
contact.keys()#所有键
contact.values()#所有值
contact.items()#所有键值对

#两种表达方式
for name,Number in contact:
    if name == "":
        print(Number)
for contact_tuple in contact:
    name = contact_tuple[0]
    Number = contact_tuple[1]
    if name == "":
        print(Number)

#range(起始值，结束值,布长)左闭右开
for i in range(5,10):
    print(i)#5-9
for i in range(5,10,2):
    print(i)#5 7 9
    
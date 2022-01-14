#字典，可变
contact ={'陈':'130','方':'132'}
#列表，内部可变
list = ['abc','cde']
#元组，不可变(不能添加删除)
tuple=('键帽','键盘')
#元组使用
contracts={
    ('张伟',22):'1302222',
    ('张伟',30):'1350000'
}
#读出字典
phonenum=contact['陈']
phonenum=contracts[('张伟',22)]
#添加字典
contracts['小明']='1892000'

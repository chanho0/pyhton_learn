#高级教程https://www.jianshu.com/p/20d1b512b8b2

#def定义功能函数
def math(a,b):
    c=a+b
    print(c)

#调用
#如果执行该脚本的时候，该if 判断语句将会是 True,那么内部的代码将会执行。 如果外部调用该脚本，if判断语句则为False,内部代码将不会执行。
if __name__ == '__main__':
    first=1
    second=2
    math(a=first,b=second)
    #print(math())

#如果想要函数有返回值, 用return 返回。
#全局变量
APPLE = 100 # 全局变量
a = None
def fun():
    global a    # 使用之前在全局里定义的 a
    a = 20      # 现在的 a 是全局变量了
    return a+100

print(APPLE)    # 100
print('a past:', a)  # None
fun()
print('a now:', a)   # 20
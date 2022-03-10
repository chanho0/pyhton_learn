#正则表达式匹配某个文本模式，但是它找到的是模式的最长可能匹配（因为是贪婪匹配 ）。 而你想修改它变成查找最短的可能匹配。

# import re
# text2 = 'Computer says "no." Phone says "yes."'
# str_pat=re.compile(r'"(.*)"')   # 匹配引号包裹的任意文本，并编译
# print(str_pat.findall(text2))   #['no." Phone says "yes.'],并不是我们想要的['no.', 'yes.']，由于正则表达式* 匹配0到人一多次，是贪婪匹配
# # 解决方式
# new_str_pat=re.compile(r'"(.*?)"')
# print(new_str_pat.findall(text2))  # ['no.', 'yes.']


with open("cookie0.txt", "r") as cookie:
        cks = cookie.read()
        newck = re.sub('\n','&',cks)
with open("cookies.txt", "w") as newtxt:
        newtxt.writelines(newck)


#布尔判断
str = '2/2/1/1/1'
str1 = None
if bool(str1) == True:
    print('成功')
else:
    print('Flase')

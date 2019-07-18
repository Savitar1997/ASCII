# -*- coding: UTF-8 -*-
a=str(input('a.字符串转换成ASCII码\nb.ASCII码转换成字符串\n请输入你需要的模式：'))
def zhuana(x):
        b=list(x)
        for i in range(len(x)):
            print(ord(b[i]),end='')
            print(' ',end='')
def zhuanb(x):
        for i in range(len(x)):
            z=chr(int(x[i]))
            print(z,end='')
if a=='a' :
    x = str(input('请输入：'))
    zhuana(x)
else :
    y = input('请输入：')
    x=y.split()
    zhuanb(x)


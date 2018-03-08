# _*_ coding:utf-8 _*_
'''主要练习字符串的使用，本节主要为字符串的连接和分割'''
__author__: 'zll'

if __name__ == '__main__':
    t = ['1','2','3','4','5','a','b','exp']
    a = ('q','w','e')
    #用"_"连接t，组成新的字符串
    str1 = "周".join(t)
    str2 = "_".join(a)
    print(str1)
    print(str2)

    #直接组成新的字符串
    str3 = "".join(t)
    print(str3)

    #分割字符串
    list_data = str1.split("周")
    print(list_data)



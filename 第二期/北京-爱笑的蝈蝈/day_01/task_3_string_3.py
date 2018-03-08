# _*_ coding:utf-8 _*_
'''主要练习字符串的使用,本节主要为去除字符串空格'''
__author__: 'zll'

if __name__ == '__main__':
    str = " 我叫 你好 哈哈 我 不知道 我是谁 "
    print("benben"+ str)
    #去掉左边的空格
    lstr = str.lstrip()
    print("benben" + lstr)

    #去掉右边的空格
    rstr = str.rstrip()
    print(rstr + "benben")

    #去掉两边的空格
    str_new = str.strip()
    print("benben" + str_new + "benben")


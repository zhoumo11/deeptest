# _*_ coding:utf-8 _*_
'''主要练习字符串的使用,本节主要判断字符串的类型,以及大小写转换'''
__author__: 'zll'

if __name__ == '__main__':
    #判断字符串只有包含字母或者数字
    str1 = "weee3434"
    str2 = "dd eer"
    print(str1.isalnum())
    print(str2.isalnum())

    #判断字符串是否只有字母
    str3 = "efrfrfr"
    str4 = "!crrr"
    print(str3.isalpha())
    print(str4.isalpha())

    #将小写转换为大写
    str5 = "weweweef"
    print(str5.upper())

    #将大写转换为小写
    str6 = "UUeddHd"
    print(str6.lower())
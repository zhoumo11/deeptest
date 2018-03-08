# _*_ coding:utf-8 _*_
'''主要练习字符串的使用，本节主要为字符串的查找和替换'''
__author__: 'zll'

#字符串的查找功能
if __name__ == '__main__':
    str_source = "i love xiao, i love da, i love ben, i hate gua"
    #find从左边查找
    find = str_source.find("love")
    print(find)
    #find从右边查找
    rfind = str_source.rfind("love")
    print(rfind)
    #find找不到指定字符转
    find_null = str_source.find("you")
    print(find_null)

    #index从左边查找
    lindex = str_source.index("love")
    print(lindex)
    #index从右边查找
    rindex = str_source.rindex("love")
    print(rindex)
    #index找不到指定字符串,会报错  ValueError: substring not found
    # index_null = str_source.index("you")
    # print(index_null)

    #找到字符串指定位置的字符
    a = str_source[0]
    print(a)

    #字符串的替换功能
    str_new = str_source.replace("love","hate")
    print(str_new)
    #替换一次
    str_new1 = str_source.replace("love","hate",1)
    print(str_new1)

    #检查字符串是否以某个字符串开头
    bool_start = "amazing".startswith("am")
    bool_end = "amazing".endswith("ing")
    print(bool_start)
    print(bool_end)
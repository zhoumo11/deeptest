# _*_ coding:utf-8 _*_
'''元组的使用,元组主要特点是，数据不能被修改'''
__author__ : 'zll'
if __name__ == '__main__':

    '''元组的取值和索引'''
    tuple_info = ("lucy",18,"女")
    #获取元组中的数据
    name = print(tuple_info[0])
    #获取索引值
    index = print(tuple_info.index(18))
    #获取不存在字段的索引值（报错ValueError: tuple.index(x): x not in tuple）
    #index_null = print(tuple_info.index("18"))
    #统计元组长度
    len = print(len(tuple_info))
    #获取元组中的最大值
    max = print(max('34','33','23'))

    '''元组的合并和删除'''
    #元组的合并
    tuple_1 = ('ni','hao')
    tuple_2 = ('lucy','and','lily')
    tuple_3 = tuple_1 + tuple_2
    print(tuple_3)

    #可以删除某个元组,再用到这个元组时，提示NameError: name 'tuple_1' is not defined
    del(tuple_1)
    #print(tuple_1)

    print("---------------------------------------------------------------------")

    '''元组的运算'''
    #元组的复制
    tuple_copy = tuple_2 * 3
    print(tuple_copy)
    #判断元素是否在元组中
    result = "lily" in tuple_2
    print(result)
    #遍历元组
    for i in tuple_2:
        print(i)

    '''列表转元组'''
    list = ['as','oms','wms','tms']
    tuple = tuple(list)
    print(tuple)

    print("---------------------------------------------------------------------")
    '''元组切片'''
    num_list = "0123456789"
    # 1,截取2-5位置的字符串
    str1 = num_list[2:6]
    print(str1)
    # 截取2-末尾的字符串
    str2 = num_list[2:]
    print(str2)
    # 截取开始位置-5的字符串
    str3 = num_list[:6]
    print(str3)
    # 截取完整的字符串
    str4 = num_list[:]
    print(str4)
    # 从开始位置，每隔一个字符截取字符串
    str5 = num_list[::2]
    print(str5)
    # 从索引1的位置开始，每隔一个字符截取字符串
    str6 = num_list[1::2]
    print(str6)
    # 截取从2到末尾-1的字符串
    str7 = num_list[2:-1]
    print(str7)
    # 截取字符串末尾2个字符
    str8 = num_list[-2:]
    print(str8)
    # 字符串的逆序（字符串逆序输出），字符串逆序相当于倒着切，步长-1
    str9 = num_list[::-1]
    print(str9)
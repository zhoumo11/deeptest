# _*_ coding:utf-8 _*_
'''列表的使用'''
__author__ : 'zll'

if __name__ == '__main__':
    '''列表的索引和取值'''
    list_source = ['1','as','2','oms','3','wms','4','tms']
    #获取元素在列表中的索引值
    index = list_source.index('oms')
    print(index)
    #根据索引值取到列表中的值
    str = list_source[1]
    print(str)
    #获取列表元素个数
    print(len(list_source))
    #返回列表中的最大值
    print(max(["22","33","11"]))

    print("---------------------------------------------------------------------------")

    '''list中的方法'''
    #append追加一个元素
    list_1 = ['i','love','you']
    list_2 = ['i','like','dog']
    list_2.append('too')
    list_2.append(list_1)
    print(list_2)
    #extend，将list2追加到list_1中
    list_3 = ['i', 'love', 'you']
    list_4 = ['i', 'like', 'dog']
    list_3.extend(list_4)
    print(list_3)
    #count统计某个出现的次数
    count = list_3.count('i')
    print(count)
    #insert某个位置插入
    list_3.insert(2,"amazing")
    print(list_3)
    #删除最后一个元素
    list_3.pop()
    print(list_3)
    #删除指定元素
    list_3.pop(2)
    print(list_3)
    #删除指定值
    list_3.remove("you")
    print(list_3)
    #清除所有元素
    list_3.clear()
    print(list_3)

    print("---------------------------------------------------------------------------")

    '''list中的方法2'''
    list_new = ['23','22','44','45','1']
    #列表反向
    list_new.reverse()
    print(list_new)
    #列表排序
    list_new.sort()
    print(list_new)
    #列表拷贝
    list_copy = list_new.copy()
    print(list_new)
    print(list_copy)

    print("---------------------------------------------------------------------------")
    '''列表更新'''
    list_new[3] = "ben"
    print(list_new)

    print("---------------------------------------------------------------------------")
    '''列表切片，同元组'''

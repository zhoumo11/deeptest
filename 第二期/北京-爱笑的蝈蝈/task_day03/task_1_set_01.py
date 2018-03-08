# _*_ coding:utf-8 _*_
'''集合set的使用,set中的元素是无序，并且唯一的'''
__author__ : 'zll'

if __name__ == '__main__':
    #创建一个集合
    set1 = set('hello,hello')
    print(set1)

    #集合中增加1个元素
    set1.add('n')
    print(set1)

    #update  用于新增多个元素值，参数为list
    list = ['4','d','g','e']
    set1.update(list)
    print(set1)

    #从set中删除指定的元素
    set1.remove('4')
    print(set1)

    #issubset 判断s1中的每个元素是否都在s2中 ,即，s1 <= s2
    s1 = set('hello')
    s2 = set('hello world')
    print(s1.issubset(s2))

    #issuperset判断s2元素是否都在s1中，即s1 >= s2
    print(s1.issuperset(s2))
    print(s2.issuperset(s1))

    #取交集
    set_in = s1.intersection(s2)
    print(set_in)

    #取并集
    set_union = s1.union(s2)
    print(set_union)

    #difference返回s3中有，但是s4中没有的元素
    s3 = set('234')
    s4 = set('456')
    print(s3.difference(s4))

    #清空set集合
    set1.clear()
    print(set1)
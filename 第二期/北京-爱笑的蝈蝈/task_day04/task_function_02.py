# _*_ coding:utf-8 _*_
'''函数的定义'''
__author__ : 'zll'

#求元组内值的和
def sum_add(tuple_one):
    sum = 0
    for i in tuple_one:
        sum = sum + i
    return sum

#拼接字符串
def str_jion(str1,str2):
    str = str1 + str2
    return str


if __name__ == '__main__':
    tuple = (1,2,3,4,5,6,7,8,9,10)
    print(sum_add(tuple))

    str1 = '你好,'
    str2 = '周杰伦'
    print(str_jion(str1,str2))
# _*_ coding:utf-8 _*_
'''函数的定义'''
__author__ : 'zll'

def mul():
    data = []
    for i in range(1,10):
        line = []
        for j in range(i,10):
            line.append('%d * %d = %d' % (i , j , i*j))
            print('')
        data.append(line)
    return data

if __name__ == '__main__':
    list = mul()
    for b in list:
        print(b)
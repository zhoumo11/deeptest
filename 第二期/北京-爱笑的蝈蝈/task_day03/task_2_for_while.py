# _*_ coding:utf-8 _*_
'''循环的使用'''
__author__ : 'zll'

if __name__ == '__main__':
    #for循环打印九九乘法表
    for i in range(1,10):
        for j in range(i,10):
            print('%d * %d = %d' % (i,j,i*j) , end='\t')
        print('')

    #while循环打印九九乘法表
    i = 1
    while i < 10:
        j = 1
        while j <= i:
            print('%d * %d = %d' % (j,i,i*j) , end='\t')
            j = j + 1
        print('')
        i = i + 1
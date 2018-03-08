#数值函数表示

import math
import random
# _*_ coding:ytf-8 _*_
if __name__ == '__main__':
    x = -12.39
    y = 3.44
    z = 100

    #获取某数的绝对值
    print(abs(x))

    #返回最大值
    print(max(x,y,z))

    #返回最小值
    print(min(x,y,z))

    #计算y的平方
    print(pow(y,2))

    #返回平方根
    print(math.sqrt(z))

    #随机数
    a = [1,2,3,4,5,6,7,8,9,0]
    print(random.choice(a))

    #从指定范围（2-100）按5递增的数据中，随机选择一个
    print(random.randrange(2,100,5))

    #生成一个随机数，在（0，1）之间
    print(random.random())

    #生成10个随机数
    for i in range(10):
        list_data = []
        list_data.append(random.randrange(10,60))
        print(list_data)
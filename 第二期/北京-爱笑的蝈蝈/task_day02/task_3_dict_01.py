# _*_ coding:utf-8 _*_
'''字典的使用'''
__author__ : 'zll'

if __name__ == '__main__':
    '''常用内置函数'''
    dict_1 = {'access_token':'111','version' : '7.0.0', 'session':''}
    #len函数计算key的个数
    print(len(dict_1))
    #将字典转换为字符串
    dict_2 = str(dict_1)
    print(dict_2)
    #查看类型
    print(type(dict_1))
    print(type(dict_2))

    print("------------------------------------------------------------------")

    '''字典常用方法'''
    dict_info = {'name':'小明', 'age' : 18, 'score':100}
    #复制字典
    print(dict_info)
    print(dict_info.copy())

    #fromkeys  创建字典{'ee': 20, 'rr': 20}
    list = ['ee','rr']
    dict_fromkey = dict_info.fromkeys(list,20)
    print(dict_fromkey)

    #字典的取值
    str = dict_info.get('name')
    print(str)

    #字典增加/修改（如果key存在，则字典修改；key不存在，字典增加）
    dict_info['grade'] = 2
    print(dict_info)
    dict_info['score'] = 98
    print(dict_info)

    #判断key是否存在
    bool = 'name' in dict_info
    print(bool)

    #以元组的形式，返回所有的key，value
    items = dict_info.items()
    print(items)

    #以列表的形式，返回所有的key
    list = dict_info.keys()
    print(list)

    #返回字典中的所有values
    values = dict_info.values()
    print(values)

    #更新字典
    dict_new = {'math': 139}
    dict_info.update(dict_new)
    print(dict_info)

    #setdefult如果key存在，则返回对应的value
    #如果key不存在，则插入对应的key和默认值，并返回默认值
    value = dict_info.setdefault('grade')
    print(value)
    value_new = dict_info.setdefault('chinese')
    print(value_new)
    print(dict_info)

    print("-------------------------------------------------------------------------------")

    '''字典的删除和遍历'''
    #删除字典
    del(dict_info['grade'])
    print(dict_info)

    #字典遍历
    for keys in dict_info:
        print('%s : %s' % (keys,dict_info[keys]))

    for (key,value) in dict_info.items():
        print('%s : %s' % (key,value))

    for key in dict_info.keys():
        print('%s : %s' % (key,dict_info[key]))

    #清空字典
    dict_info.clear()
    print(dict_info)
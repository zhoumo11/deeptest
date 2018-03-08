# _*_ coding:utf-8 _*_
'''类的定义'''
__author__ : 'zll'

class Animal:
    def __init__(self):
        print("animal初始化。。。。。。。。。")

    def eat(self,food):
        print('正在吃' + food)

    def run(self):
        print('动物会跑步')

class Dog(Animal):
    def __init__(self):
        print("dog初始化。。。。。。。。。。。")

    def spark(self,name):
        print(name + '汪汪叫')

    def run(self):
        print('小狗会跑步')

if __name__ == '__main__':
    animal = Animal()
    animal.eat('零食')
    animal.run()

    print("-----------------------------------------------")

    dog = Dog()
    dog.spark('挂挂')
    dog.eat('西瓜')   #调用父类方法
    dog.run()
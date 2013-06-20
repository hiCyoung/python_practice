#内置函数
__author__ = 'hiCyoung'

#绝对值
print(abs(1+2j))

def a():
    print("aa")

def b():
    return 3
#判断一个函数能否被调用
print(callable(a()))

#返回商、余
print(divmod(10,3))
print(divmod(-10,3))

#类型判断
print(isinstance(12,int))
print(isinstance(12,str))
print(isinstance(12,(str,int)))  #判断12的类型是不是在元组内
print(isinstance(a(),str))
print(isinstance(b(),int))
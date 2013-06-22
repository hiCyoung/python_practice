#函数
__author__ = 'hiCyoung'
def f(x,y):
    return x+y

def sayHello():
    print("Hello,Cyoung")
#           没有返回值的函数默认会加上 return None

#给参数设置默认值
def defaultValue(x,y=3):  #不能是(x=3,y)
         print("x=",x," y=",y)
         return x**2+y**3
print(f(1,2))
sayHello()
print(3**3)
print(defaultValue(2))
print(defaultValue(2,1))
print(defaultValue(y=2,x=3)) #关键字，破除了函数参数定义顺序的限制
print(defaultValue(x=2,y=3))
###递归函数##
def jc(n):
    if n ==1:
        return 1
    else:
        return n*jc(n-1)
print(jc(5))

###匿名函数##
user=[
    ("tom",20,1000),
    ("aom",24,1900),
    ("vom",23,1800),
    ("com",21,1400),
    ("bom",25,1700),
    ]
# user.sort() //默认按第一个元素排序
# user.sort(key=lambda x:x[2]) #按第二个元素排序
#以上等同于
# def f1(cc):
#     return cc[1]
# user.sort(key=f1)
print(user)

##generator生成器
#在 python 中，generator function 是一个可以保存状态的函数，
# 用 yield 指令(不是 return )返回一个值，保存当前整个函数执行状态，等待下一次调用，
# 当需要该函数返回值时，该 generator function 恢复整个函数执行状态，
# 直至再次遇到 yield 指令，再次返回一个值，再次保存当前函数执行状态，再次等待。
# 如此循环往复，直至函数末尾，发生　StopIteration　异常。
def gn():
    for i in list(range(10)):
        yield  i*2

g=gn()
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
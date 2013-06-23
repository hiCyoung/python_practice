#COPY
__author__ = 'hiCyoung'
import  copy

x=[123,234]
y=x
print(id(x))
print(id(y))
y.append(456)
print(x)   ###浅拷贝，不同的变量对象对应相同的数据

#切片处理仍然是浅拷贝
y=x[:]
y.append("789")
print(x)
print(y)  ##执行到此处貌似x,y独立了，但是
print(id(x[0]))
print(id(y[0])) ##二者仍相等

z = copy.deepcopy(x)
z.append("1110")
z[0]="0000"
print(z)
print(x)
print(id(z))
print(id(x))

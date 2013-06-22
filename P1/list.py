#列表部分##########################################
x = ["tom","jack"]
print(type(x))
#列表添加元素
x.append("cy")
x.append("bb")
#按照索引插入
x.insert(1,"zh")
#默认按照添加顺序输出
print(x)
x.sort(reverse=False)
print(x)
print(x[3])
del x[0]
print(x)
x.remove("jack")
print(x)
print(x.index("tom"))

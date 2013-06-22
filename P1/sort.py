__author__ = 'hiCyoung'

a=[1,3,2,5,7,4,9,8,6]

######选择排序########
for i in list(range(1,len(a))):
    if a[i]<a[i-1]:
        temp = a[i]
        a[i]=a[i-1]
        for j in list(range(i-1,-1,-1)):
            if a[j]>=temp:
                a[j+1] =a[j]
                a[j]=temp
print(a)
#######################
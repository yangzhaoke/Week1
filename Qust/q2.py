import  random
list=[]
for i in range(50):
    a=random.choice(range(-10,10))
    list.append(a)
print(list)
zhengshu=[]
fushu=[]
for i in list:
    if i>0:
        zhengshu.append(i)
    else:
        fushu.append(i)
print(zhengshu)
print(fushu)

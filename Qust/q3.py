import  random
list=[]
for i in range(20):
    a=random.choice(range(10))
    list.append(a)
print(list)
list[::2]=sorted(list[::2],reverse=True)
print(list)
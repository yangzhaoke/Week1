import  random
str='abcdefghijklmnopqrstuvwxyz'
str1=''
for i in range(1000):
    str1+=random.choice(str)
print(str1)
dict={}
for i in str1:
    key = dict.get(i)
    # 每个字母的数量，
    if(key==None):
        dict[i] = 1
    else:
        dict[i] += 1

print(dict)
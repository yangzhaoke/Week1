s='The column above illustrates apparently' \
  ' the polularity of people ' \
  'doing exercise in a certain year ' \
  'from 2013 to 2018.Based upon the data,' \
  'we can see that python is wonderful. ' \
  'python is wonderful. Python '
s=s.split(' ',s.count(' ')-1)
print(s)
dict={}
for i in s:
    key = dict.get(i)
    # 每个单词的数量，
    if (key == None):
        dict[i] = 1
    else:
        dict[i] += 1

dict1 = {}

sv = list(dict.values())
sv.sort()


sv = set(sv)
sv = list(sv)

# 实现单词升序
for i in sv:
    for j in dict:
        if (dict[j] == i):
            dict1[j] = i


print(dict1)

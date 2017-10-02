dic = {}
k = []
n = int(input())
for i in range(n):
    x = int(input())
    k.append(x)
for j in range(0,len(k)):
    key = k[j]
    if  key in dic:
        print(dic[key])
    else:
        a = k[j]
        dic[key] = f(a)
print(dic.get(key))
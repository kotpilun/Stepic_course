a = []
a = input().split()
b = {}
mlist = []
for i in a:
    b[i] =  a.count(i)
for i in b:
   if b.get(i) == max(b.values()):
       mlist.append(i)
c = max(b.values())
print(min(mlist), b[min(mlist)])

d = ''
with open('F:\Py_projects\Stepic_course\datasets\dataset_3363_3.txt') as inf:
   for line in inf:
        d += line.strip()
a = []
a = d.lower().split()
b = {}
mlist = []
for i in a:
    b[i] =  a.count(i)
for i in b:
   if b.get(i) == max(b.values()):
       mlist.append(i)
print(min(mlist), b[min(mlist)])

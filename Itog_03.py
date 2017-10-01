lst = [int(i) for i in input().split()]
x = int(input())
f = False

for i in range(0,len(lst)):
    if lst[i] == x:
        print(i, end=' ')
        f = True
if f == False:
    print("Отсутствует")

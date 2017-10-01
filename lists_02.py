a = [int(i) for i in input().split()]

if len(a) == 1:
    print(a[0])
else:
    a.append(a[0])
    a.insert(0,a[-2])
    for i in range(1,len(a)-1):
        print(a[i-1] + a[i+1], end=' ')


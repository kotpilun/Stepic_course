a = [int(i) for i in input().split()]
b = []

for i in range(len(a)):
    n = a.count(a[i])
    m = b.count(a[i])
    if n > 1:
        if m == 0:
            b.append(a[i])
            print(a[i], end=' ')


print()
print(set(a))
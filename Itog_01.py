sum = 0
b = []
sum_s =0

while True:
    a = int(input())
    sum += a
    b.append(a)
    if sum == 0:
        break

for i in b:
    sum_s += i ** 2

print(sum_s)


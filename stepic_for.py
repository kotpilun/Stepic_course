a, b = (int(input()) for i in range(2))

sum_ab = 0
mean = 0
count = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        sum_ab += i
        count += 1

if count != 0:
    mean = sum_ab / count
    print(mean)
else:
    print("Нельзя делить на ноль!")

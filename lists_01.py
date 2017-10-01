a = [int(i) for i in input().split()]
sum = 0


for i in a:
    sum += i

print(sum)

#Better
#print(sum(int(i) for i in input().split()))
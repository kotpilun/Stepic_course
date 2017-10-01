a = input()
sum_gc =0
sum_length = 0

for i in (a):
    sum_length += 1
    if i == "c" or i == "g":
        sum_gc += 1

print(sum_gc / sum_length * 100)



# Better decision

#s = input().upper()
#print((s.count('G') + s.count('C'))/len(s) * 100)
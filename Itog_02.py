# a = int(input())
# j = 0
# col = 0
# for i in range(1,a+1):
#     if col >= a:
#         break
#     while j < i:
#         if col >= a:
#             break
#         print(i)
#         j += 1
#         col += 1
#     j = 0

n = int(input())
a = []
i = 0
while len(a) < n:
    a += [i] * i
    i += 1
print(*a[:n])
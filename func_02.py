# def modify_list(l):
#     for i  in range(len(l)-1,-1,-1):
#         if l[i] % 2 == 1:
#             l.remove(l[i])
#     for i in range(len(l)):
#         l[i] = int(l[i] / 2)
#
# a = [int(i) for i in input().split()]
# #print(len(a))
# modify_list(a)
# print(a)
#
# # modify_list(a)
# # print(a)

def modify_list(l):
    l[:] = [i//2 for i in l if not i % 2]

a = [int(i) for i in input().split()]
modify_list(a)
print(a)

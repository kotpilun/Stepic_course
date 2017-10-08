# Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования
# повторов, и производит обратную операцию, получая исходный текст.
#
# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
#
# В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
#

#
# def char_int(x):
#     result = ''
#     count = 1
#     dig = ''
#     f = False
#     i = 0
#     #for i in range(len(x)):
#     while i < len(x):
#         if x[i] in '1234567890': #если x[i] - число
#             count = 0
#             while (x[i] in '1234567890'): # идем дальше, ищем числа
#                 if count == 0:
#                     j = i - 1  # запоминаем каким было последнее и с буквой
#                 count += 1 #считаем количество чисел
#                 dig += str(x[i]) #запоминаем цифру в виде строки для соединения нескольких цифр в одну
#                 if i < len(x)-1: #проверяем на выход из диапазона списка
#                     i += 1
#                 else:
#                     f = True # дошли до конца. выходить из for.
#                     break
#             result += str(x[j]) * int(dig)
#             dig = ''
#         if f == True:
#             break
#         i += 1
#     return result
#
# # a = input()
# # a = list(a)
# with open('F:\Py_projects\Stepic_course\datasets\dataset_3363_2.txt') as inf:
#      for line in inf:
#          line = line.strip()
#          a = list(line)
# # print(line)
# # print(char_int(a))
# with open('F:\Py_projects\Stepic_course\datasets\out.txt', 'w') as outf:
#     outf.write(char_int(a))

#####################################################################
#Это решение понравилось
# with open('dataset_3363_2.txt', 'r') as f:
#     s = f.readline().strip()
# i = 0
# while i < len(s):
#     j = i + 1
#     while j < len(s) and s[j].isdigit():
#         j += 1
#     print(s[i] * int(s[i+1:j]), end='')
#     i = j
######################################################
#GREAT!
s, d = input(), []
for i in s:
    if not i.isdigit(): d.append(i)
    else: d[-1] += i
print(*[i[0]*int(i[1:]) for i in d], sep='')
print(d)
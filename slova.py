# Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой
# строке число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
# Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться только один раз.

#USING DICT
a = input().lower().split()
dict = {}
k = 0

for i in a:
    if i in dict:
        k = dict.get(i) + 1
        dict[i] = k
        k = 0
    else:
        k = 1
        dict[i] = k

for key, value in dict.items():
    print (key, value)

#USING SET:
# s = input().lower().split()
# for i in set(s):
# print(i, s.count(i))

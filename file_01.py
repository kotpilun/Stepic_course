# Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования
# повторов, и производит обратную операцию, получая исходный текст.
#
# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
#
# В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

with open('F:\Py_projects\Stepic_course\datasets\dataset_3363_2.txt') as inf:
    for line in inf:
        line = line.strip()
        a = list(line)
print(a)

#проверяю число-не число текущий символ и следующий, если текущий не последний
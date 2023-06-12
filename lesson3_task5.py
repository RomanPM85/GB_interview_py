"""
5. Усовершенствовать первую функцию из предыдущего примера.
Необходимо просканировать текстовый файл, созданный на предыдущем задании
и реализовать создание и запись нового текстового файла
В новый текстовый файл обеспечить запись строк вида:
zmsebjvdgi zmsebjvdgi
ychpwljtzn ychpwljtzn
...
Т.е. извлекаются строки из первого текстового файла,
а в новый они записываются в виде, где вместо числа ставится строка
Здесь необходимо использовать регулярные выражения.
"""
import re

import lesson3_task4


def print_text_file(desc):
    """
    Функция, которая производит чтение файла, и создания нового файла с заменой
    цифр в новый текстовый файл вида:
    zmsebjvdgi zmsebjvdgi
    ychpwljtzn ychpwljtzn

    :param desc:
    :return:
    """
    f_in = open(desc, 'r')
    f_out = open("replace_file.txt", 'w')

    for line in f_in:
        numb = re.search(r'\d*', line)
        string = re.search(r'\s\w*', line)
        line = line.replace(numb.group(0), string.group(0))
        f_out.write(line)

    f_in.close()
    f_out.close()

    with open("replace_file.txt", encoding='utf-8') as descr:
        for elem in descr:
            print(elem)



if __name__=="__main__":
    search_file = 'test_task5.txt'
    lesson3_task4.main(search_file, lesson3_task4.open_file, 10, 10)
    print_text_file(search_file)

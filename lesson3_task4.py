"""
4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение.
Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение.
Вызвать вторую функцию.
В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.
Вся программа должна запускаться по вызову первой функции.
"""

import random
from pathlib import Path
from functools import reduce

def main(filename, readfile, word, count):
    """
    Главная функция по созданию файла со списком
    :param count:
    :param word:
    :param filename:
    :param readfile:
    :return:
    """
    file = Path(filename)
    if Path.exists(file):
        return  print(f"Файл {file} существует")
    else:
        file.touch(exist_ok=True)
        with open(file, 'w', encoding='utf-8', newline='') as fp:
            employee_names = get_random_string(word, count)
            employee_numbers = [x+1 for x in range(len(employee_names))]
            fp.writelines(['{} {}\n'.format(number, text) for number, text in zip(employee_numbers, employee_names)])

    readfile(filename)

def open_file(filename):
    """
    Функция для чтения файла
    :param filename:
    :return:
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line)


def get_random_string(len_word, count):
    """
    Генератор слов и символов
    :param len_word:
    :param count:
    :return:
    """
    words = []
    while count > 0:
        words.append(reduce(lambda string, char: string + char,
                            [chr(random.randint(ord('a'), ord('z'))) for _ in range(len_word)]))
        count = count -1
    return words



if __name__=="__main__":
    search_file = 'test_task4.txt'
    main(search_file,open_file, 10, 10)

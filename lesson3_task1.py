"""
Урок 3. Python - стандартная библиотека Python.
Задание 1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться имя файла с расширением. В функции необходимо
реализовать поиск полного пути по имени файла, а затем «выделение» из этого пути имени файла (без расширения).
"""
import os
from pathlib import Path, PurePath

def file_search(filename):
    path = Path.cwd()
    files = os.listdir(path)

    for file in files:
        if file !=filename:
            pass
        else:
            print(path)
            print(path.joinpath(file))
            print(PurePath(file).stem)


if __name__=="__main__":
    search = "README.md"
    file_search(search)


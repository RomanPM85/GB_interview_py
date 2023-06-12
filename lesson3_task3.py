"""
3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь.
Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
Значения, которым не хватило ключей, необходимо отбросить.
"""
import random


def create_dict(keys, values):
    values.extend([None] * (len(keys) - len(values)))
    dictionary = dict(map(lambda i, j: (i, j), keys, values))
    return print(f"словарь {dictionary}")


if __name__=="__main__":
    list_keys = []
    list_values = []

    count_keys = input(f"Введите количество ключей>>")
    count_values = input(f"Введите количество значений>>")

    for key in range(int(count_keys)):
        list_keys.append("key-"+str(key+1))

    for value in range(int(count_values)):
        list_values.append("values-"+str(value+1))

    print(list_keys)
    print(list_values)
    create_dict(list_keys, list_values)

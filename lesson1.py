import glob
import os


def multiplication_table(a, b):
    """
    Функция, реализующую вывод таблицы умножения размерностью AｘB.
    Первый и второй множитель должны задаваться в виде аргументов функции.
    Значения каждой строки таблицы должны быть представлены списком, который формируется в цикле.
    После этого осуществляется вызов внешней lambda-функции, которая формирует на основе списка строку.
    Полученная строка выводится в главной функции.
    Элементы строки (элементы таблицы умножения) должны разделяться табуляцией.
    :param a:
    :param b:
    :return:
    """
    # pass
    tabl = ''
    for y in range(a, b):
        for x in range(a, b):
            tabl += f'{x * y}\t'
        tabl += f'\n'
    return tabl

def print_directory_contents(spath):
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    """
    # pass
    for item in glob.iglob(f'{spath}/**/*', recursive=True):
        return print(item)

def directory_contents(spath):
    list_file = os.listdir(spath)
    complete_file_list = list()
    for file in list_file:
        complete_path = os.path.join(spath, file)
        if os.path.isdir(complete_path):
            complete_file_list = complete_file_list + directory_contents(complete_path)
        else:
            complete_file_list.append(complete_path)

    return complete_file_list



def generate_random_num(start_num, stop_num):
    """
    В функцию передавать начальное и конечное число генерации (нуль необходимо исключить).
    Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
    Вывести содержимое созданных списка и словаря.
    :param start_num:
    :param stop_num:
    :return:
    """
    if start_num == 0 or stop_num == 0:
        return print("Ошибка! нуль нельзя вводить")
    else:
        list_key = []
        list_value = []
        count = 1
        for item in range(start_num, stop_num):
            list_key.append("elem_" + str(count))
            list_value.append(item)
            count += 1

        dict1 = dict(zip(list_key, list_value))
        return print(f"Словарь>>{dict1}\nСписок элементов>>{list_value}")

def bank_deposit(deposit_sum, deposit_term):
    """
    Клиент банка делает депозит на определенный срок.
    В зависимости от суммы и срока вклада определяется процентная ставка:
    1000–10000 руб.(6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых).
    10000–100000 руб.(6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых).
    100000–1000000 руб.(6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых).
    Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада.
    Каждый из трех банковских продуктов должен быть представлен в виде словаря с ключами(begin_sum, end_sum, 6, 12, 24).
    Ключам соответствуют значения начала и конца диапазона суммы вклада и значения процентной ставки для каждого срока.
    В функции необходимо проверять принадлежность суммы вклада к одному из диапазонов и выполнять расчет
    по нужной процентной ставке. Функция возвращает сумму вклада на конец срока.
    :param deposit_sum:
    :param deposit_term:
    :return:
    """
    banking_products = [
        {'begin_sum': 1000, 'end_sum': 10000, '6': 0.05, '12': 0.06, '24': 0.05},
        {'begin_sum': 10000, 'end_sum': 100000, '6': 0.06, '12': 0.07, '24': 0.065},
        {'begin_sum': 100000, 'end_sum': 1000000, '6': 0.07, '12': 0.08, '24': 0.075}
    ]
    selected_product = {}
    for item in banking_products:
        if int(deposit_sum) >= item.get('begin_sum'):
            if int(deposit_sum) <= item.get('end_sum'):
                selected_product = item
    # print(selected_product)

    selected_percentage = 0
    for key in selected_product:
        if key != deposit_term:
            continue
        else:
            selected_percentage = selected_product[key]
            # print(selected_percentage)

    output_deposit_sum = float(deposit_sum) * selected_percentage + float(deposit_sum)
    return print(f"Сумма вклада {deposit_sum}, срок хранения {deposit_term} месяца,\n"
                 f"процентная ставка составит {selected_percentage}%,\n"
                 f"сумма в конце срока составит {output_deposit_sum:.2f}")

def upgrade_bank_deposit():
    """
    Усовершенствовать программу «Банковский депозит».
    Третьим аргументом в функцию должна передаваться фиксированная ежемесячная сумма пополнения вклада.
    Необходимо в главной функции реализовать вложенную функцию подсчета процентов для пополняемой суммы.
    Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего.
    Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев.
    Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами),
    а главная функция — общую сумму по вкладу на конец периода.
    :return:
    """
    pass



if __name__=='__main__':
    # pass
    path = os.getcwd()
    start_fun = int(input(f"Выберите функцию для запуска по коду:\n"
                          f"multiplication_table код=1\n"
                          f"print_directory_contents код=2\n"
                          f"directory_contents код=3\n"
                          f"generate_random_num код=4\n"
                          f"bank_deposit код=5\n"
                          f"upgrade_bank_deposit код=6\n"
                          f"Введите код>>"))
    if start_fun == 1:
        a = int(input(f"Введите ширину таблицы"))
        b = int(input(f"Введите высоту таблицы"))
        print(multiplication_table(a, b))

    elif start_fun == 2:
        print_directory_contents(path)

    elif start_fun == 3:
        second = directory_contents(path)
        # print(f'Второй вариант {second}')
        for i in second:
            print(i)

    elif start_fun == 4:
        start = int(input('начальное число генерации: '))
        stop = int(input('конечное число генерации: '))
        generate_random_num(start,stop)

    elif start_fun == 5:
        input_deposit_sum=input(f"Сумма вклада:")
        input_deposit_term=input(f"срок хранения 6, 12, 24 месяца:")
        bank_deposit(input_deposit_sum, input_deposit_term)

    elif start_fun == 6:
        pass

    else:
        print(f"Доступной функции по коду {start_fun} нет! Введите цифру от 1 до 6")


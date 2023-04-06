
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
    pass


def print_directory_contents(sPath):
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    """
    pass


def generate_random_num():
    """
    В функцию передавать начальное и конечное число генерации (нуль необходимо исключить).
    Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
    Вывести содержимое созданных списка и словаря.
    :return:
    """
    pass


def bank_deposit(deposit_sum, deposit_term):
    """
    Клиент банка делает депозит на определенный срок.
    В зависимости от суммы и срока вклада определяется процентная ставка: 1000–10000 руб.
    (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых). 10000–100000 руб.
    (6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых). 100000–1000000 руб.
    (6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых).
    Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада.
    Каждый из трех банковских продуктов должен быть представлен в виде словаря с ключами(begin_sum, end_sum, 6, 12, 24).
    Ключам соответствуют значения начала и конца диапазона суммы вклада и значения процентной ставки для каждого срока.
    В функции необходимо проверять принадлежность суммы вклада к одному из диапазонов и выполнять расчет
    по нужной процентной ставке. Функция возвращает сумму вклада на конец срока.
    :param deposit_sum:
    :param deposit_term:
    :return:
    """
    pass


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
    pass
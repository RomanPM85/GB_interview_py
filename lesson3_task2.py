"""
2. Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением,
целое оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False.
"""

def int_frac_number():
    number = input(f"Введите число>>")
    try:
        float(number)
        if number.isdigit():
            print(f"число {number} целое")
        else:
            print(f"число {number} дробное")
            left, right = number.split('.')
            if left == right:
                print(f"число {left} до разделителя и число {right} после разделителя равны: {True}")
            print(f"число {left} до разделителя и число {right} после разделителя равны: {False}")

    except ValueError:
        return print(f"это не число")


if __name__=="__main__":
    int_frac_number()

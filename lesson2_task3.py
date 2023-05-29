"""
Урок 2. Python - парадигма ООП особенности и отличия от других ЯП.

1. Проверить механизм наследования в Python. Для этого создать два класса. Первый — родительский (ItemDiscount),
должен содержать статическую информацию о товаре: название и цену. Второй — дочерний (ItemDiscountReport), должен
содержать функцию (get_parent_data), отвечающую за отображение информации о товаре в одной строке. Проверить работу
программы, создав экземпляр (объект) родительского класса.
2. Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться, что при сохранении
текущей логики работы программы будет сгенерирована ошибка выполнения.
3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.
4. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский, и дочерний
классы получили новое значение цены. Следует проверить это, вызвав соответствующий метод родительского класса
и функцию дочернего (функция, отвечающая за отображение информации о товаре в одной строке).
5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента
в дочерний класс. Выполнить перегрузку методов конструктора дочернего класса (метод init, в который должна
передаваться переменная — скидка), и перегрузку метода str дочернего класса. В этом методе должна пересчитываться
цена и возвращаться результат — цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать
дочерний и родительский классы (вторая и третья строка после объявления дочернего класса).
6. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport
на два класса. Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в
первом классе будет отвечать за вывод названия товара, а вторая — его цены. Далее реализовать выполнение каждой
из функции тремя способами.
"""

class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get__price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    @staticmethod
    def get_parent_data():
        return print(f" Товар {fruit.get_name()}, с ценною {fruit.get__price()} руб")



if __name__ == "__main__":
    fruit = ItemDiscountReport("яблоко", "660")
    fruit.get_parent_data()

import csv
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: int, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        if len(name) > 10:
            name = name[:10]
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            new_name = new_name[:10]
        self.__name = new_name


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        if self.pay_rate != 0.0 or self.pay_rate != 0:
            self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path):

        with open(f'{path}', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if 'name' and 'price' and 'quantity' in row:
                    continue
                else:
                    cls(row[0], row[1], row[2])

    @staticmethod
    def string_to_number(number: str) -> int:
        return int(float(number))


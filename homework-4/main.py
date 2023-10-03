from src.item import Item
from src.phone import Phone

class Test:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity

if __name__ == '__main__':

    # смартфон iPhone 14, цена 120_000, количество товара 5, симкарт 2
    phone1 = Phone("iPhone 14", 120_000, 5, 2)

    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2

    phone1 = Test(20)

    item1 = Item("Смартфон", 10000, 20)
    if isinstance(item1, Item) and isinstance(phone1, Item):
        assert item1 + phone1 == 25
        assert phone1 + phone1 == 10

    else:
        print('Один из классом не принадлежит к родительскому классу Item')

    phone2 = Phone("iPhone 14", 120_000, 5, 2)
    phone2.number_of_sim = 0
    # ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.

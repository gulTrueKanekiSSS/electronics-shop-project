"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

a_test_1 = Item("Test1", 200, 5)
a_test_2 = Item("Test2", 500, 2)
a_test_3 = Item("Test3", 2, 0)

b_test_1 = Item("Test1", 20000, 1)



def test_answer_of_calculate_total_price():

    assert a_test_1.calculate_total_price() == 1000
    assert a_test_2.calculate_total_price() == 1000
    assert a_test_3.calculate_total_price() == 0

    Item.pay_rate = 0.8
    assert b_test_1.apply_discount() == 16000

def test_apply_discount():
    Item.pay_rate = 1
    assert b_test_1.apply_discount() == 20000



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

def test_apply_discount():
    native_price = b_test_1.price * b_test_1.pay_rate
    b_test_1.apply_discount()
    price = b_test_1.price
    assert native_price == price

def test_name():
    assert a_test_1.name == "Test1"
    assert a_test_2.name == "Test2"
    assert a_test_3.name == "Test3"


test_len_item = Item('tredcvbnjuytfcvbnm', 2000, 5000)


def test_cut_name():
    assert test_len_item.name == 'tredcvbnju'


def test_floats_numbers():
    assert Item.string_to_number('5.0') == 5


class TestItemClass:
    def __init__(self):
        self.__item = Item("test", 10000, 20)
    def test__repr__method(self):
        # item = Item("test", 10000, 20)
        assert repr(self.__item) == "Item('test', 10000, 20)"

    def test__str__method(self):
        # item = Item("test", 10000, 20)
        assert str(self.__item) == "test"
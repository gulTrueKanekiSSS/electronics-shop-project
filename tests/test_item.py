"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone


class TestUsualMethodsItems:
    def test_answer_of_calculate_total_price(self):
        a_test_1 = Item("Test1", 200, 5)
        a_test_2 = Item("Test2", 500, 2)
        a_test_3 = Item("Test3", 2, 0)
        assert a_test_1.calculate_total_price() == 1000
        assert a_test_2.calculate_total_price() == 1000
        assert a_test_3.calculate_total_price() == 0

    def test_apply_discount(self):

        b_test_1 = Item("Test1", 20000, 1)

        native_price = b_test_1.price * b_test_1.pay_rate
        b_test_1.apply_discount()
        price = b_test_1.price
        assert native_price == price

    def test_name(self):

        a_test_1 = Item("Test1", 200, 5)
        a_test_2 = Item("Test2", 500, 2)
        a_test_3 = Item("Test3", 2, 0)

        assert a_test_1.name == "Test1"
        assert a_test_2.name == "Test2"
        assert a_test_3.name == "Test3"

    def test_cut_name(self):
        test_len_item = Item('tredcvbnjuytfcvbnm', 2000, 5000)
        assert test_len_item.name == 'tredcvbnju'

    def test_floats_numbers(self):
        assert Item.string_to_number('5.0') == 5


class TestMagicMethodsItemClass:

    def test__repr__method(self):
        item = Item("test", 10000, 20)
        assert repr(item) == "Item('test', 10000, 20)"

    def test__str__method(self):
        item = Item("test", 10000, 20)
        assert str(item) == "test"


class TestMagicMethodsPhoneClass:
    def test__str_method(self):
        phone = Phone('iPhone15', 200000, 20, 1)
        assert str(phone) == 'iPhone15'
    def test__repr__method(self):
        phone = Phone('iPhone15', 200000, 20, 1)
        assert repr(phone) == "Phone('iPhone15', 200000, 20, 1)"

    def test__add__method(self):
        phone = Phone('iPhone15', 200000, 20, 1)
        item = Item("Test1", 20000, 1)

        assert phone + item == 21
        assert item + phone == 21

    def test__get__set__methods(self):
        phone = Phone('iPhone15', 200000, 20, 1)
        assert phone.number_of_sim == 1

        try:
            phone.number_of_sim = 0
        except ValueError:
            assert 0 == 0


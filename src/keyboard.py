from abc import ABC, abstractmethod
from src.item import Item


class Mixin:

    def __init__(self):
        self.__language = "EN"


    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"

        elif self.language == "RU":
            self.language = "EN"


class Keyboard(Item, Mixin):
    def __init__(self, name: str, price: int, quantity: int):
        super().__init__(name, price, quantity)
        self.__name = name
        self.__language = 'EN'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new):
        self.name = new

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, new):
        if new not in ['EN', 'RU']:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")
        self.__language = new

    def __str__(self):
        return f"{self.name}"





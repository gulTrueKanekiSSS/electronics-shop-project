from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: int, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim
        self.__number_of_sim = number_of_sim

    def __add__(self, other):
        if isinstance(self, Item) and isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            return 'Один из классом не принадлежит к родительскому классу Item'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, num):
        if num <= 0:
            raise ValueError('Error')
        self.__number_of_sim = num
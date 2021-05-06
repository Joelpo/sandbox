# FactoryMethod.py / Factory method design pattern implementation

from abc import ABC, abstractmethod

# Abstract interface that describes products
class AbstractProduct(ABC):

    @staticmethod
    @abstractmethod
    def create_object():
        # create obj method
        pass


# Example product A
# a concrete class that implements the Abstract Product interface
class ConcreteProductA(AbstractProduct):
    # a concrete class that implements the Abstract Product interface

    def __init__(self):
        self.name = "Concrete Product A"

    def create_object(self):
        return self

# Example product B
# a concrete class that implements the Abstract Product interface
class ConcreteProductB(AbstractProduct):

    def __init__(self):
        self.name = "Concrete Product B"

    def create_object(self):
        return self

# FACTORY class
class Creator:

    @staticmethod
    def create_object(product_type):
        if product_type == 'a':
            return ConcreteProductA()
        if product_type == 'b':
            return ConcreteProductB()
        return None


# CLIENT
productA = Creator().create_object('a')
productB = Creator().create_object('b')
productBB = Creator().create_object('b')
print(productA.name)
print(productB.name)
print(productBB.name)

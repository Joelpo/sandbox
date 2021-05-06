# Implementation of the strategy design pattern

from abc import ABC, abstractmethod

# context in which the programe executes
class Context():

   # The request is handled by the class passed in
    @staticmethod
    def request(strategy):
        return strategy()

# Abstract strategy class
class IStrategy(ABC):

    @staticmethod
    @abstractmethod
    def __str__(self):
        pass


class StrategyA(IStrategy):
    def __str__(self):
        return "Executing concrete strategy A"


class StrategyB(IStrategy):
    def __str__(self):
        return "Executing concrete strategy B"


# Client : chooses which strategy he wants to execute
print(Context().request(StrategyA))
print(Context().request(StrategyB))

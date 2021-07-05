from decimal import Decimal
from abc import ABCMeta, abstractmethod


class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def build_sequence(self):
        pass

    def build(self, string):
        pass


class DecimalFactory(AbstractFactory):
    def build_sequence(self):
        return []

    def build(self, string):
        return Decimal(string.lstrip('$'))


class Loader(object):
    @staticmethod
    def load(string, factory):
        sequence = factory.build_sequence()
        for substr in string.rstrip(',').split(','):
            element = factory.build(substr)
            sequence.append(element)
        return sequence


f = DecimalFactory()
result = Loader.load('464.80, 993.68', f)
print(result)

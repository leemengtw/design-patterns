from decimal import Decimal


# Restriction: outlaw passing callables


def build_decimal(string):
    return Decimal(string.lstrip('$'))

# In some legacy languages: the code must
# move inside a class method instead.


class DecimalFactory(object):
    @staticmethod
    def build(string):
        return Decimal(string.lstrip('$'))


class Loader(object):
    @staticmethod
    def load(string, factory):
        string = string.rstrip(',')  # allow trailing comma
        return [factory.build(item) for item in string.split(',')]


result = Loader.load('464.80, 993.68', DecimalFactory)
print(result)

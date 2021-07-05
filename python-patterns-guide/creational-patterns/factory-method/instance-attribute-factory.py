class JSONDecoder(object):
    ...
    def __init__(self, ... parse_float=None, ...):
        ...
        self.parse_float = parse_float or float
        ...


from decimal import Decimal
from json import JSONDecoder

my_decoder = JSONDecoder(parse_float=Decimal)


# 貌似 class attribute factory 的 code 也能用 instance attribute, 只要你知道要改哪個 attribute
conn = HTTPConnection()
conn.response_class = SpecialHTTPResponse


# 不管是 instance / class attribute factory 都能傳入任意 callables
def parse_number(string):
    if '.' in string:
        return Decimal(string)
    return int(string)


my_decoder = JSONDecoder(parse_float=parse_number)



#  functional programming: partial application
from decimal import Context, ROUND_DOWN
from functools import partial

parse_number = partial(Decimal, context=Context(2, ROUND_DOWN))
my_decoder = JSONDecoder(parse_float=parse_number)
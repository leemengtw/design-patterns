import json
from decimal import Decimal


text = '{"total": 9.61, "items": ["American", "Omelet"]}'

# 新手 python engineer 會自己寫一個 factory ( a routine build and return objects )


def build_decimal(string):
    return Decimal(string)


print(json.loads(text, parse_float=build_decimal))

# 更 pythonic 的寫法
print(json.loads(text, parse_float=Decimal))

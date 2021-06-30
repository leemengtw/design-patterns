import calendar
import pickle
import pkgutil

print(calendar.January)

calendar.January = 100

print(calendar.January)

del calendar.January

try:
    print(calendar.January)
except AttributeError as e:
    print(e)

print('-' * 50)
print(pickle.bytes_types)

print('-' * 50)
print(__file__)
# print(pkgutil.get_data())




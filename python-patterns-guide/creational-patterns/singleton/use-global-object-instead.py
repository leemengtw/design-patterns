https://docs.python.org/3/faq/programming.html#how-do-i-share-global-variables-across-modules

config.py:

x = 0   # Default value of the 'x' configuration setting
mod.py:

import config
config.x = 1
main.py:

import config
import mod
print(config.x)
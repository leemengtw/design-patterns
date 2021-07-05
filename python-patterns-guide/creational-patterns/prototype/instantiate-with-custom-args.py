class Sharp(object):
    "The symbol ♯."


class Flat(object):
    "The symbol ♭."


class Note(object):
    "Musical note 1 ÷ `fraction` measures long."
    def __init__(self, fraction):
        self.fraction = fraction


# 假設只需要客製化 positional arguments
menu = {
    'whole note': (Note, 1),
    'half note': (Note, 2),
    'quarter note': (Note, 4),
    'sharp': (Sharp,),
    'flat': (Flat,),
}

tup = menu['whole note']
new_instance = tup[0](*tup[1:])


# 使用 lambda 客製化 keyword arguments
menu = {
    'whole note': lambda: Note(fraction=1),
    'half note': lambda: Note(fraction=2),
    'quarter note': lambda: Note(fraction=4),
    'sharp': Sharp,
    'flat': Flat,
}


from functools import partial

# Keyword arguments for illustration only;
# in this case could instead write ‘partial(Note, 1)’

menu = {
    'whole note': partial(Note, fraction=1),
    'half note': partial(Note, fraction=2),
    'quarter note': partial(Note, fraction=4),
    'sharp': Sharp,
    'flat': Flat,
}
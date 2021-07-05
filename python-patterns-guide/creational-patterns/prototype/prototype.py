# The Prototype pattern: teach each object
# instance how to build copies of itself.


class Note(object):
    "Musical note 1 ÷ `fraction` measures long."
    def __init__(self, fraction):
        self.fraction = fraction

    def clone(self):
        return Note(self.fraction)


class Sharp(object):
    "The symbol ♯."
    def clone(self):
        return Sharp()


class Flat(object):
    "The symbol ♭."
    def clone(self):
        return type(self)()


# What the Prototype pattern avoids:
# needing one factory for every class.

class NoteFactory(object):
    def __init__(self, fraction):
        self.fraction = fraction

    def build(self):
        return Note(self.fraction)

class SharpFactory(object):
    def build(self):
        return Sharp()

class FlatFactory(object):
    def build(self):
        return Flat()
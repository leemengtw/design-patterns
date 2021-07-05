class Handler(Filterer):
    ...
    def __init__(self, level=NOTSET):
        ...
        self.createLock()
    ...
    def createLock(self):
        """
        Acquire a thread lock for serializing access to the underlying I/O.
        """
        self.lock = threading.RLock()
    ...


class HandlerWithNewlock(Handler):

    def createLock(self):
        self.lock = NewKindOfLock
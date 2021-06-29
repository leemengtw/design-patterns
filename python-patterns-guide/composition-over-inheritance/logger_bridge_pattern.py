import sys
from abc import ABC, abstractmethod

# The “abstractions” that callers will see.


class Logger(object):
    def __init__(self, handler):
        self.handler = handler

    def log(self, message):
        self.handler.emit(message)


class FilteredLogger(Logger):
    def __init__(self, pattern, handler):
        self.pattern = pattern
        super().__init__(handler)

    def log(self, message):
        if self.pattern in message:
            super().log(message)


# The “implementations” hidden behind the scenes.


class AbstractHandler(ABC):
    @abstractmethod
    def emit(self):
        pass


class FileHandler(AbstractHandler):
    def __init__(self, file):
        self.file = file

    def emit(self, message):
        self.file.write(message + "\n")
        self.file.flush()


class SocketHandler:
    def __init__(self, sock):
        self.sock = sock

    def emit(self, message):
        self.sock.sendall((message + '\n').encode('ascii'))


class SyslogHandler:
    def __init__(self, priority):
        self.priority = priority

    def emit(self, message):
        syslog.syslog(self.priority, message)


if __name__ == "__main__":
    handler = FileHandler(sys.stdout)
    logger = FilteredLogger('Error', handler)
    logger.log('Ignored: This is not important.')
    logger.log('Error: this is very important!')

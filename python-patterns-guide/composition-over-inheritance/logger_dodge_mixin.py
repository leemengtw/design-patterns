import socket

# Our original example’s base class and subclasses.


class Logger(object):
    def __init__(self, file):
        self.file = file

    def log(self, message):
        self.file.write(message + '\n')
        self.file.flush()


class SocketLogger(Logger):
    def __init__(self, sock):
        self.sock = sock

    def log(self, message):
        self.sock.sendall((message + '\n').encode('ascii'))


class FilterMixin:
    pattern = ''

    def log(self, message):
        if self.pattern in message:
            super().log(message)

# A class derived through multiple inheritance.


class FilteredSocketLogger(FilterMixin, SocketLogger):
    pass  # Again, the subclass needs no extra code.

# Works just fine.


sock1, sock2 = socket.socketpair()

logger = FilteredSocketLogger(sock1)
logger.pattern = "Error"

logger.log('Warning: not that important')
logger.log('Error: this is important')

print('The socket received: %r' % sock2.recv(512))

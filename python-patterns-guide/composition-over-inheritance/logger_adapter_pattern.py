import syslog
import socket
from logger_inheritance import FilteredLogger


class FileLikeSocket(object):
    def __init__(self, socket):
        self.socket = socket

    def write(self, message_and_newline):
        self.socket.sendall(message_and_newline.encode('ascii'))

    def flush(self):
        pass


class FileLikeSyslog(object):
    def __init__(self, priority):
        self.priority = priority

    def write(self, message):
        syslog.syslog(self.priority, message)

    def flush(self):
        pass


if __name__ == "__main__":
    sock1, sock2 = socket.socketpair()

    fs = FileLikeSocket(sock1)
    logger = FilteredLogger('Error', fs)
    logger.log('Warning: message number one')
    logger.log('Error: message number two')

    print('The socket received: %r' % sock2.recv(512))

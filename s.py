import rpyc
from rpyc.utils.server import ThreadedServer

class ServerService(rpyc.Service):
    def exposed_foo(self, x, y):
        return x + y
    def exposed_bar(self, x):
        y = self.conn.root.client_method(x + 12)
        return y + 1

s = ThreadedServer(ServerService, port = 18893)
s.start()

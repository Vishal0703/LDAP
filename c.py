import rpyc
class ClientService(rpyc.Service):
     def exposed_client_method(self, x):
        print ("this was called by the server with x = " +str(x))
        return x * 2

c = rpyc.connect("localhost", 18893, ClientService)

# foo is a simple function that just returns a value
print (c.root.foo(1, 2))

# bar will invoke the client's client_method (defined in the client's service)
print (c.root.bar(18))

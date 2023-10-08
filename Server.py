import socket

class Server():
    def __init__(self):
        self.ip = socket.getfqdn()
        self.port = "1201"
        print(f'server started: {self.ip}:{self.port}')    

    def accept_clients(self):
        pass

    def receive_data(self):
        pass

    def send_data(self):
        pass

    def start(self):
        self.root.mainloop()

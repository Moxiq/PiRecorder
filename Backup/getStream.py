import socket


class Capture:

    def __init__ (self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ('192.168.0.32', 5000)
        self.sock.bind(self.server_address)
        return

    def get_stream_image(self):
        return self.sock.recv(65507)
        



    # # Create a TCP/IP socket
    # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # # Bind the socket to the port
    # server_address = ('192.168.0.32', 5000)
    # print("starting up UDP on " + server_address[0] + " on port " + str(server_address[1]))
    # sock.bind(server_address)

    # while True:
    #     data, addr = sock.recvfrom(65507) # buffer size is 1024 bytes
    #     print("received message: %s" % data)


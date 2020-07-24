import socket

class IP_address:
    def __init__(self):
        hostn= socket.gethostname()
        IPadd= socket.gethostbyname(hostn)
        print("IP Address:"+IPadd)
        print(hostn)

if __name__ == "__main__":
    IP1=IP_address()

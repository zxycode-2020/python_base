import socket

udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpServer.bind(('10.0.142.171', 8900))

while True:
    data, addr = udpServer.recvfrom(1024)
    print("客户端说：", data.decode("utf-8"))


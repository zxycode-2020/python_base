import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input("请输入数据")
    client.sendto(data.encode("utf-8"), ('10.0.142.171', 8900))



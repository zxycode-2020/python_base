import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('10.0.142.171',8081))
server.listen(5)

def run(ck):
  data = clientSocket.recv(1024)
  print("客户端说：" + data.decode("utf-8"))
  #sendData = input("输入返回给客户端的数据")
  clientSocket.send("sunck is a goood man".encode("utf-8"))

print("服务器启动成功，等待客户端的链接")
while True:
  clientSocket, clientAddress = server.accept()
  #print("%s --  %s 链接成功" % (str(clientSocket), clientAddress))
  t = threading.Thread(target=run, args=(clientSocket,))
  t.start()





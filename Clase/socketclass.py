import socket

s=socket.socket()
s.bind(("localhost", 8020))
s.listen()
c, addr = s.accept()
with c:
    data=c.recv(1024)
    print(data)
s.close()
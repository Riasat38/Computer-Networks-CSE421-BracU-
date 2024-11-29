import socket as sc

socket = sc.socket()
host = sc.gethostname()
ip = sc.gethostbyname(host)
socket.connect(('localhost',8989))

msg = input("Enter hours wokred:")
socket.send(msg.encode())

response = socket.recv(2048).decode()

print(response)
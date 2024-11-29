import socket as sc

socket = sc.socket()

socket.bind(('localhost', 8989)) 
socket.listen(1)    

connection , address = socket.accept()     

print("Connected to :",address)
message = connection.recv(20480) 

print(message.decode())
connection.close()
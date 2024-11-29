import socket as sc
import threading
socket = sc.socket()

socket.bind(('localhost', 8989)) 

socket.listen(1)    

connection , address = socket.accept()    
print("Connected to :",address)

message = connection.recv(20480).decode()
try:
    hour = int(message.strip())
    salary = 0
    if hour <= 40:
        salary = hour * 200
    elif hour>40:
        salary = (hour*300) + 8000
    
    connection.send(str(salary).encode())
except ValueError:
    connection.send("age kam kor".encode())


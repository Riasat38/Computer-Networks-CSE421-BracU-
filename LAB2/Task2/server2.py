import socket as sc

socket = sc.socket()

socket.bind(('localhost', 8989)) 
socket.listen(1)    

connection , address = socket.accept()     

print("Connected to :",address)
message = connection.recv(20480).decode()

count = 0
for i in message:
    if i  in  "aeiouAEIOU":
        count+=1

reply = ""
if count<1:
    reply += "Not Enough Vowels"
elif count>2:
    reply += "Too many vowels"
else:
    reply += "Enough vowels I guess"

connection.send(reply.encode())

connection.close()
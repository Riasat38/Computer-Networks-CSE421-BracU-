import socket as sc
import threading
import time
import sys

def connecting_client(sock,addr):
          #connection object and address

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


socket = sc.socket()
socket.bind(('localhost', 8989)) 
socket.listen(1) 
start = time.time()
while True: #connection window 30s
    if time.time() - start <30:
        connection , address = socket.accept()
        print("Accepted at:",time.time()-start)
        threading.Thread(target=connecting_client,  args=(socket,address)).start()
    else:
        break
connection.close()



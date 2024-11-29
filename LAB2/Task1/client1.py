import socket as sc

socket = sc.socket()
host = sc.gethostname()
ip = sc.gethostbyname(host)
socket.connect(('localhost',8989))

socket.send(f"IP : {ip} \nHostName : {host}".encode())
import socket
import threading

def receive_data():
	while True:
	    	data = sock.recv(1024)
    		if data:
        		print(data.decode())

def send_data():
	while True:
    		message = input()
    		sock.sendall(message.encode())
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.1.77', 2261)
print('connexion à %s port %s' % server_address)
sock.connect(server_address)
getPseudo = input("Veuillez saisir votre pseudo:")
sock.sendall(getPseudo.encode())
receive_thread = threading.Thread(target=receive_data)
send_thread = threading.Thread(target=send_data)
receive_thread.start()
send_thread.start()

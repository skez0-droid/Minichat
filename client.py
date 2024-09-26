import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.1.77', 2261)
print('connexion à %s port %s' % server_address)
sock.connect(server_address)

getPseudo = input("Veuillez saisir votre pseudo:")
sock.sendall(getPseudo.encode())


def receive_data():
	while True:
	    	data = sock.recv(1024)
    		if data:
        		print(data.decode())

receive_thread = threading.Thread(target=receive_data)
receive_thread.start()


def send_data():
	while True:
    		message = input()
    		sock.sendall(message.encode())
send_thread = threading.Thread(target=send_data)
send_thread.start()


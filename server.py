
import socket
import threading
from datetime import datetime

clients = []
pseudo = ''

# Création d'un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison du socket à une adresse et un port
server_address = ('192.168.1.77', 2261)
print('démarrage sur %s port %s' % server_address)
sock.bind(server_address)

# Écoute des connexions entrantes
sock.listen(1)

# thread pour gerer les connexions
threading.Thread(target=new_client,args=(sock,)).start()

# Fonction exécutée pour la connexion des clients
def new_client(sock):
	while True:
   		 # Attente d'une connexion
		print('Wait for connexion...')
		connection, client_address = sock.accept()
		pseudo = connection.recv(1024)
		pseudotamp = pseudo.decode()
		print(client_address,pseudotamp, 'is connected.')
		threading.Thread(target=receive_data,args=(connection, client_address, pseudo.decode())).start()
		clients.append(connection)

		
# fonction exécutée pour recevoir les messages
def receive_data(connection, address, pseudo):
	while True:
    		data = connection.recv(1024)
   	 	# si un message est reçu
    		if data:
        		a = '['+str(datetime.now()) +']'+ pseudo + ' >> ' + data.decode()
        		print(a)
   		 	# boucle pour envoyer le message à tous les clients
        		for client in clients:
       		 		client.sendall(a.encode())







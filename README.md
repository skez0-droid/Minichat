# Minichat

Ce projet consiste en la création de deux programmes en Python, un serveur (server.py) et un client (client.py), dans le but de réaliser un mini-chat simpliste en utilisant des sockets. Les sockets sont des interfaces de programmation réseau qui permettent la communication entre différents ordinateurs via un réseau. Le serveur est responsable de recevoir les messages des clients et de les redistribuer à tous les autres clients connectés, tandis que le client permet à l'utilisateur d'envoyer et de recevoir des messages via une interface en ligne de commande.

Le serveur utilise un socket TCP/IP pour écouter les connexions entrantes.Il peut gérer plusieurs clients simultanément en utilisant des threads. Chaque fois qu'un nouveau client se connecte, celui-ci choisi un pseudo et le serveur en prend compte.Celui-ci lance alors un thread pour gérer la réception des messages de ce client. Les messages reçus sont ensuite diffusés à tous les autres clients connectés.

Le client, quant à lui, se connecte au serveur en utilisant l'adresse IP et le port du serveur. L'utilisateur peut saisir un pseudo pour identifier ses messages. Le client utilise également deux threads, un pour recevoir les messages du serveur et les afficher à l'utilisateur, et un autre pour permettre à l'utilisateur de saisir des messages à envoyer au serveur.

Il est important de noter que les adresses IP utilisées dans les codes sont à modifier pour correspondre aux adresses IP réelles du réseau sur lequel le serveur et le client seront exécutés.

Ce projet peut être utilisé comme base pour comprendre les concepts de base des sockets en Python et pour développer des applications de communication réseau plus complexes. 

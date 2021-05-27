import socket
from Cliente_Thread import Th
from threading import Thread

address = ("localhost", 30000)

# Cria o socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Passa endereço IP e número da porta
server_socket.bind(address)

server_socket.listen()

print('SERVER-GAMER WORKING...')

# Loop de execução do servidor
while True:
    # Servidor agurdando conexão
    conectionSocket, adress = server_socket.accept()
    print("Nova conexão recebida de {}".format(adress))
   
    # Instanciando uma Client-Thread
    client_thread = Th(conectionSocket, adress)
    client_thread.start()

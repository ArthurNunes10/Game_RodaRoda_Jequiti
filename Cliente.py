import socket

address = ("localhost", 30000)

# Cria o socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Faz a conexão com o servidor no endereço de destino
client_socket.connect(address)
print('CLIENTE CONECTADO...')

while True:
    from_server = client_socket.recv(1024).decode()
    print(from_server)
    if 'Conexão Finalizada' in from_server:
        client_socket.close()
        break
    else:
        client_socket.send(input('').encode())


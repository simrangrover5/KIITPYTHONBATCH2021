

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET --> IPv4, sock_stream --> TCP

host = "192.168.1.7"
port = 12345

server.bind((host, port))
server.listen()

print(f"\n Server is ready to listen at host {host} and port {port}")

client_socket, client_addr = server.accept()
print(f"\n The client is running IP --> {client_addr[0]} and PORT --> {client_addr[1]}")

client_socket.send("YOU REQUEST IS ACCEPTED".encode())

msg = client_socket.recv(1024).decode()
print(f"\n MESSAGE --> {msg}")

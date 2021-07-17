
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
print(f"\n CLIENT --> {msg}")

bye_cond = ['bye', 'byebye', 'bubye', 'tata', 'see you', 'talk to you later']
flag = False
while True:
    # this code is to send msg from server to client
    smsg = input("\n SERVER --> ".ljust(50))
    client_socket.send(smsg.encode())
    for i in bye_cond: # i = "bye"
        if i in smsg.strip().lower():  # 'bye' in 'okay bye'
            print("\n SERVER DISCONNECTED...")
            flag = True
            break

    if flag:
        break
    # this code is to receive msg from client
    cmsg = client_socket.recv(1024).decode()
    print(f"\n CLIENT --> {cmsg}")
    for i in bye_cond: # i = "bye"
        if i in cmsg.strip().lower():  # 'bye' in 'okay bye'
            print("\n CLIENT DISCONNECTED...")
            flag = True
            break
    if flag:
        break


import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET --> IPv4, sock_stream --> TCP

host = input("\n Enter Server Ip --> ") # server IP and port
port = int(input("\n Enter Server Port --> "))

client.connect((host, port))

msg = client.recv(1024).decode()
print(f"\n SERVER --> {msg}")

client.send("THANKYOU FOR ACCEPTING MY REQUEST".encode())
bye_cond = ['bye', 'byebye', 'bubye', 'tata', 'see you', 'talk to you later']
flag = False
while True:
    # code to receive message from server
    smsg = client.recv(1024).decode()
    print(f"\n SERVER --> {smsg}")
    for i in bye_cond:
        if i in smsg.strip().lower():
            print("\n SERVER DISCONNECTED...")
            flag = True
            break
    if flag:
        break
    # code to send message to server
    cmsg = input("\n CLIENT --> ".ljust(50))
    client.send(cmsg.encode())
    for i in bye_cond:
        if i in cmsg.strip().lower():
            print("\n CLIENT DISCONNECTED...")
            flag = True
            break
    if flag:
        break

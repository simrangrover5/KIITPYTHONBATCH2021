
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET --> IPv4, sock_stream --> TCP

host = input("\n Enter Server Ip --> ") # server IP and port
port = int(input("\n Enter Server Port --> "))

client.connect((host, port))

msg = client.recv(1024).decode()
print("\n MESSAGE --> ", msg)

client.send("THANKYOUR FOR ACCEPTING MY REQUEST".encode())

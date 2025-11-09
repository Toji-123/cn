import socket

# Create TCP socket
s = socket.socket()
s.bind(("0.0.0.0", 5000))
s.listen(1)

print("Server waiting for connection...")
conn, addr = s.accept()
print("Client connected:", addr)

# Receive message
client_msg = conn.recv(1024).decode()
print("Client says:", client_msg)

# Send reply
server_msg = "Hello from Server!"
conn.send(server_msg.encode())

conn.close()
s.close()

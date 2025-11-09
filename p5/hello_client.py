import socket

# Enter Server IP (use ipconfig on server)
server_ip = input("Enter Server IP: ")

s = socket.socket()
s.connect((server_ip, 5000))

# Send hello message
msg = "Hello from Client!"
s.send(msg.encode())

# Receive reply
reply = s.recv(1024).decode()
print("Server says:", reply)

s.close()

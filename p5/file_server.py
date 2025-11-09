import socket

s = socket.socket()
s.bind(("0.0.0.0", 6000))
s.listen(1)

print("Server ready. Waiting for client...")
conn, addr = s.accept()
print("Connected with:", addr)

# Receive file name
filename = conn.recv(1024).decode()
file = open(filename, "wb")

# Receive file data
while True:
    data = conn.recv(1024)
    if not data:
        break
    file.write(data)

file.close()
conn.close()
s.close()

print("File received successfully as:", filename)

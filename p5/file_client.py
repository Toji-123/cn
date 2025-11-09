import socket
import os

server_ip = input("Enter Server IP: ")
filename = input("Enter File Name to Send: ")

s = socket.socket()
s.connect((server_ip, 6000))

# Send filename
s.send(filename.encode())

# Send file data
file = open(filename, "rb")
data = file.read(1024)
while data:
    s.send(data)
    data = file.read(1024)

file.close()
s.close()

print("File sent successfully!")

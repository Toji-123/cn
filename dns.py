import socket

print("1. Domain to IP")
print("2. IP to Domain")
choice = int(input("Enter your choice (1/2): "))

if choice == 1:
    domain = input("Enter Domain Name: ")
    try:
        ip = socket.gethostbyname(domain)
        print("IP Address of", domain, "is:", ip)
    except:
        print("Invalid Domain Name or Lookup Failed!")

elif choice == 2:
    ip = input("Enter IP Address: ")
    try:
        domain = socket.gethostbyaddr(ip)
        print("Domain Name for IP", ip, "is:", domain[0])
    except:
        print("Invalid IP Address or Lookup Failed!")

else:
    print("Invalid Choice!")

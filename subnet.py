# Program to demonstrate Subnetting and find Subnet Mask

ip = input("ENTER IP: ")

# Extract the first octet and convert to int
first_octet = int(ip.split(".")[0])

mask = ""

# Determine the class and default subnet mask
if first_octet > 0 and first_octet <= 127:
    mask = "255.0.0.0"
    print("Class A IP Address")
    print("SUBNET MASK:", mask)

elif first_octet >= 128 and first_octet <= 191:
    mask = "255.255.0.0"
    print("Class B IP Address")
    print("SUBNET MASK:", mask)

elif first_octet >= 192 and first_octet <= 223:
    mask = "255.255.255.0"
    print("Class C IP Address")
    print("SUBNET MASK:", mask)

elif first_octet >= 224 and first_octet <= 239:
    mask = "255.0.0.0"
    print("Class D IP Address (Used for Multicasting)")

elif first_octet >= 240 and first_octet <= 254:
    mask = "255.0.0.0"
    print("Class E IP Address (Experimental Use)")

# Calculate Network Address and Broadcast Address
ip_parts = list(map(int, ip.split(".")))
mask_parts = list(map(int, mask.split(".")))

network_addr = []
last_addr = []

for i in range(4):
    net = ip_parts[i] & mask_parts[i]
    network_addr.append(str(net))
    broad = net | (255 - mask_parts[i])
    last_addr.append(str(broad))

print("First IP of block:", ".".join(network_addr))
print("Last IP of block:", ".".join(last_addr))

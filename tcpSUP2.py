import socket
# import tqdm

hostname = socket.gethostname()
ipAddr = socket.gethostbyname(hostname)

# Create a client socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Specify the server's IP address and port
print(f"server ip address: {ipAddr}")
server_ip = ipAddr # localhost (you can change it)
server_port = int(input("enter the server port like(4444): "))

# bind the server socket to the ip address and port
server_socket.bind((server_ip, server_port))

# Start listening for incoming connections (accept up to 1)
server_socket.listen()
print(f"Server is listening on {server_ip}:{server_port}...")

# Accept incoming connections from clients
client_socket, client_address = server_socket.accept()
print(f"Accepted a connection from {client_address} $$$")

username = client_socket.recv(1024).decode()

# file_name = client_socket.recv(1024).decode()
# file_size = client_socket.recv(1024).decode()
# file = open(file_name, "wb")
# file_bytes = b""
# done = False
# progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=int(file_size))

# while not done:
# 	data = client_socket.recv(1024).decode
# 	if file_bytes[-5:] == b"<END>":
# 		done = True
# 	else:
# 		file_bytes += data
# 	progress.update(1024)

# file.write(file_bytes)
# file.close()

# Receive data from the client and print it
while True:
	data = client_socket.recv(1024).decode()
	if not data:
		break
	print(f"{username}: {data}")

# Close the connection
client_socket.close()
server_socket.close()
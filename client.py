import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = socket.gethostname()
host = "192.168.0.5"

print(host)
port = 444

client_socket.connect((host, port))

message = client_socket.recv(1024) # 1024 is maximun quanntity of data t>

client_socket.close()

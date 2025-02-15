import socket
import threading
import configparser

# load config info
config = configparser.ConfigParser()
config.read("config.ini")

host = config.get("General", "host")
port = config.getint("General", "port")

# Initialize server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)
print(f"Binded server to: {host}:{port}")

# Worker thread function
def handle_client(client_socket):
    data = client_socket.recv(1024).decode("utf-8")
    print(f"Received: {data}")

    # Echoing the data back
    client_socket.sendall(data.encode('utf-8'))
    print("Data echoed back")

    client_socket.close()

# Main server loop

print("Server started.")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from: {client_address}")

    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

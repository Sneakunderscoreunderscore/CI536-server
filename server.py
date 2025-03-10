import socket
import threading
import configparser
import json
import request_handler

# load config info
config = configparser.ConfigParser()
config.read("config.ini")

debug = config.getboolean("General", "debug")
host = config.get("General", "host")
port = config.getint("General", "port")

# Initialize server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)
print(f"Binded server to: {host}:{port}")

# debug printing function
def Dprint(msg):
    if debug:
        print(msg)

# Worker thread function
def handle_client(client_socket):
    data = client_socket.recv(1024).decode("utf-8")
    Dprint(f"Received: {data}")
    # load JSON into a python dictionary to make it usable by python
    loaded_data = json.loads(data)

    # call the function from 'request_handler.py' corresponding to the request type
    process = getattr(request_handler, loaded_data["type"])
    return_data = process(loaded_data["data"])

    # send back the response from the function above
    client_socket.send(return_data.encode('utf-8'))
    Dprint(f"Returned response to a client: {return_data}")

    client_socket.close()

# Main server loop
print("Server started.")

while True:
    # accept a connection request
    client_socket, client_address = server_socket.accept()
    print(f"Connection from: {client_address}")

    # create a new thread to handle the connection
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

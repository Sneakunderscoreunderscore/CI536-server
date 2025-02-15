import socket
import configparser

# load config info
config = configparser.ConfigParser()
config.read("config.ini")

host = config.get("General", "host")
port = config.getint("General", "port")

# create socket connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
client_socket.connect((host, port))

# send test message
data = "test"
client_socket.send(data.encode('utf-8'))
responce = client_socket.recv(1024).decode("utf-8")
print(f"Receved data: {responce}")


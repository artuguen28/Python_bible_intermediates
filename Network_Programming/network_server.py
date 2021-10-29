#Sockets are the endpoints of the communication channels or basically, the endpoints that talk to each other.
import socket


#       Creating a server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# AF_INET - Working with internet
# SOCK_STREAM - Working with TCP

s.bind(("127.0.0.1", 9999))
s.listen()
print("Listening...")

while True:
    client, address = s.accept()
    print(f"Connected to {address}")
    message = "Hello Client!"
    client.send(message.encode('ascii'))
    client.close()


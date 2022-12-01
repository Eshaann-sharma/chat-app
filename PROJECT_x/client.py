import socket

HEADER = 64 
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"
SERVER = "127.0.0.1"
ADDR = (SERVER , PORT)

#Connecting to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    #getting lenght and making it 64
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    
    client.send(send_len)
    client.send(message)


send("Hello world")
send("YOur mom  so fat")
send(DISCONNECT_MSG)
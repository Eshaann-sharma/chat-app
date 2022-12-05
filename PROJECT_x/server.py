import socket
import threading
#import time

HEADER = 64 
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #getting local ip address
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(ADDR)

clients = []

def broadcast(msg):
    for conn in clients:
        conn.send((msg).encode(FORMAT))


def handle_client(conn , addr):
    
    print(f"NEW CONNECTION {addr} connected ...")
    connected = True
    while connected:
        #recieve msg from client
        msg = conn.recv(2048).decode(FORMAT)
        broadcast(msg)
            
        if msg == DISCONNECT_MSG:
            connected = False
                
        print(f"[{addr}] : {msg}") 
        conn.send((msg).encode(FORMAT))
        print("msg sent")
    
    conn.close() #closing connection

def start():
    server.listen()
    print(f"SERVER IS LISTENING ON {SERVER}")
    while True:
        conn , addr = server.accept()
        clients.append(conn)
        print(conn) #wait for new connection and info of connection
        thread = threading.Thread(target=handle_client , args=(conn , addr))
        thread.start()
        
        print(f"ACTIVE CONNECTION = { threading.active_count()-1 }")
         
print("STARTING SERVER ......")
start()
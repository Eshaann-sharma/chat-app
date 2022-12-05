import socket
import threading

HEADER = 64 
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"
SERVER = "127.0.0.1"
ADDR = (SERVER , PORT)

#Connecting to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

msg_list = []

def read():
    
    msg_r = client.recv(2048).decode(FORMAT)
    #print(msg_r)
    
    if msg_r not in msg_list:
        print(f" ANNONYMUSS : {client.recv(2048).decode(FORMAT)}")
        

def send(msg):
    
    message = msg.encode(FORMAT)
    
    #getting lenght and making it 64
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))

    #client.send(send_len)
    client.send(message)
    

print("********************************************")
print("         WELCOME TO CHAT_APP !!!!")
print("********************************************")
print()
print("Enter Nickname and Server [ 1 or 2 ]")
print(f"Use {DISCONNECT_MSG} to disconnect from server and exit the chat_App")
print()
print("********************************************")
print("                    RULES            ")
print()
print("1. No swearing or use of curse words")
print("2. No targeting to any religious or cultural ")
print("3. HAVE FUNNNNNN !!!!")
print()
print("********************************************")
print()
nick =input("         Nickname:")
sname = int(input("         Server :"))
print()
print("********************************************")



if sname == 1:
            
    while True:
        smsg = input()
        send(smsg)
        msg_list.append(smsg)
        thread = threading.Thread(target=read)
        thread.start()
        #read()
        
        if smsg == DISCONNECT_MSG:
            print("       THANKS FOR USING CHAT_APP         ")
            break
        else :
            continue

elif sname != 1 :
    print("Enter a valid server Number" )

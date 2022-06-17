# server.py
import time, socket, subprocess, sys
from cryptography.fernet import Fernet
import ecdsa, pickle, hashlib, hmac

#global variables
key = Fernet.generate_key()
f = Fernet(key)                             #fernet key to share
name = "SERVER"                             #name for server
P=23
G=9                                        #G and P are public numbers

#encrypt message using fernet
def encrypt(message):
    token = f.encrypt(message)
    return token

#decrypt message using fernet
def decrypt(token):
    message = f.decrypt(token)
    return message

#client authentication
def ecdsaAuthenticate():
    sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    sig = sk.sign(b"SERVER")
    conn.send(sig)
    time.sleep(0.2)
    conn.send(pickle.dumps(vk))

    sig = conn.recv(2048)
    vk = pickle.loads(conn.recv(65536))
    try: 
        vk.verify(sig, b"CLIENT")
        print("Client is valid!")
    except:
        try:
            print("Client verification denied!")
            s = input("Enter [e] to exit")
            if(s=="[e]"):
                sys.exit()
        except:
            print("Something went wrong!")

#Diffie-Hellman key exchange
def Authenticate():
    a = 4                                   #private key for server
    x = int(pow(G, a, P))                   #gets the key generated
    y = int(conn.recv(2048).decode())            #getting key of client
    ka = int(pow(y, a, P))
    conn.send(str(x).encode())
    time.sleep(0.2)
    conn.send(str(ka).encode())
    print("sent ka")

    if(conn.recv(2048).decode() == "unauthorized"):
        sys.exit("\Client rejected your authentication\n")

    print("you got authecticated")

    kb = int(conn.recv(2048).decode())           #getting secret key of client
    if(ka!=kb):
        time.sleep(0.2)
        conn.send("unauthorized".encode())
        sys.exit("\Client is not authenticated is not authenticated\n")
    else:
        conn.send("authorized".encode())


print("\nWelcome to Chat Room\nInitialising....\n")
time.sleep(1)

#Steps for connection
server = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 12345
server.bind((host, port))
print(host, "(", ip, ")\n")
           
server.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = server.accept()
ecdsaAuthenticate()
Authenticate()
time.sleep(0.1)
conn.send(key)
print("key sent")
s_name = conn.recv(2048).decode()
subprocess.run(["clear"])
print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
conn.send(name.encode())


# Chatting with message encryption and decryption
while True:
    message = input('')
    if message == "[e]":
        message = "Left chat room!"
        conn.send(encrypt(message.encode()))
        print("\n")
        break

    server_hmac = hmac.new(bytes(message, 'utf-8'), key, hashlib.sha256).digest()
    message = encrypt('{} : {}'.format(name, message).encode('UTF-8'))
    conn.send(message)
    time.sleep(0.3)
    conn.send(server_hmac)

    message = decrypt(conn.recv(2048)).decode()
    shaMsg = str(message.split(':')[1][1:])
    client_hmac = conn.recv(1024)
    my_hmac = hmac.new(bytes(shaMsg, 'utf-8'), key, hashlib.sha256).digest()
    if(my_hmac == client_hmac):
        print('\r-----[' + '{}'.format(message) + ' ]-----\n-----[' +' {} : '.format(name), end='')
    else:
        print("message authentication failed!")
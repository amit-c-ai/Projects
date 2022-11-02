# client.py
import time, socket, subprocess, sys
from cryptography.fernet import Fernet
import ecdsa, pickle, hashlib, hmac

P=23
G=9                                                 #G and P are public numbers

#encrypt message using fernet
def encrypt(message):
    token = f.encrypt(message)
    return token

#decrypt message using fernet
def decrypt(token):
    message = f.decrypt(token)
    return message

#server authentication
def ecdsaAuthenticate():
    sig = client.recv(2048)
    vk = pickle.loads(client.recv(65536))
    try:
        vk.verify(sig, b"SERVER")
        print("Server is valid!")
    except:
        try:
            print("Server verification denied!")
            s = input("Enter [e] to exit")
            if(s=="[e]"):
                sys.exit()
        except:
            print("Something went wrong!")

    sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    sig = sk.sign(b"CLIENT")
    client.send(sig)
    time.sleep(0.2)
    client.send(pickle.dumps(vk))
    time.sleep(0.5)


# Diffie-Hellman key exchange
def Authenticate():
    b = 3                                           #private key for client
    y = int(pow(G, b, P))                           #gets the key generated
    client.send(str(y).encode())                    #sending key to server
    x = int(client.recv(2048).decode())            #getting key of server
    ka = int(client.recv(2048).decode())           #getting secret key of server
    kb = int(pow(x, b, P))
    if(kb!=ka):
        client.send("unauthorized".encode())
        sys.exit("\nServer is not authenticated\n")
    else:
        client.send("authorized".encode())

    time.sleep(0.2)
    print("\nServer is authenticated\n")
    client.send(str(kb).encode())
    if(client.recv(2048).decode() == "unauthorized"):
        sys.exit("\nServer rejected your authentication\n")

print("\nWelcome to Chat Room\nInitialising....\n")
time.sleep(1)

#connecting using socket
client = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = "127.0.1.1"
name = subprocess.check_output(['whoami']).decode('UTF-8')[:-1]
port = 12345
print("\nTrying to connect to ", host, "(", port, ")\n")
time.sleep(1)
client.connect((host, port))
ecdsaAuthenticate()
Authenticate()
print("Connected with Server\n")

key = client.recv(2048)
print("Got key : {key}\n")
f = Fernet(key)

client.send(name.encode())
s_name = client.recv(2048).decode()
subprocess.run(["clear"])
print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n")

# Chatting with message encryption and decryption
while True:
    message = decrypt(client.recv(2048)).decode()
    shaMsg = str(message.split(':')[1][1:])
    server_hmac = client.recv(2048)
    my_hmac = hmac.new(bytes(shaMsg, 'utf-8'), key, hashlib.sha256).digest()
    if(my_hmac == server_hmac):
        print('\r-----[' + '{}'.format(message) + ' ]-----\n-----[' +' {} : '.format(name), end='')
    else:
        print("Message authentication failed")
    message = input('')
    if message == "[e]":
        message = "Left chat room!"
        client.send(message.encode())
        print("\n")
        break
    client_hmac = hmac.new(bytes(message, 'utf-8'), key, hashlib.sha256).digest()
    message = encrypt('{} : {}'.format(name, message).encode('UTF-8'))
    client.send(message)
    time.sleep(0.3)
    client.send(client_hmac)

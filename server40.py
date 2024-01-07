from socket import*
connection = socket(AF_INET,SOCK_STREAM)
ip="127.0.0.1"
port=1212
connection.bind((ip,port))
connection.listen(1)
print(f"server runing on port {port}")
client,raddr=connection.accept()
print(f"client connected on port :{raddr[1]}")
while(True):
    cmd=str(input("server:"))
    client.send(bytes(cmd,'utf-8'))
    msgclient=client.recv(1024)
    print(f"client:{msgclient.decode('utf-8')}")
connection.close()
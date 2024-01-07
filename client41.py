from socket import*
connection=socket(AF_INET,SOCK_STREAM)
connection.connect(("127.0.0.1",1212))
while(True):
    data=connection.recv(1024)
    print(f"server :{data.decode('utf-8')}")
    message=str(input("client:"))
    connection.send(bytes(message,'utf-8'))
connection.close()

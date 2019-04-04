import socket

try:
    Sck= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host= socket.gethostbyname('0.0.0.0')
    port= 2233
    Sck.bind((host,port))
    while True:
        Sck.listen(5)
        conn, addr= Sck.accept()
        data= conn.recv(1000)
        print(data.decode('utf-8'))
except:
    print("User is offline!!")

conn.close()
Sck.close()

import socket

try:
    ipadd='192.168.1.20'
    #print("Connected to IPv4 : %s" % ipadd)
    
    Sck= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Sck.connect((ipadd,2233))
    print("Connected to IPv4 : %s" % ipadd)
    while True:
        msg= str(input("Message: "))
        Sck.sendall(msg.encode('utf-8'))
except:
    print("\nServer is offline !!")
finally:
    Sck.close()

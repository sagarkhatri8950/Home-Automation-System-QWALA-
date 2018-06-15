import socket
 
def Main():
        while True:
                host = '192.168.43.125'
                port = 21567

                message = input(" -> ")  
                mySocket = socket.socket()
                mySocket.connect((host,port))
                mySocket.send(message.encode())
                mySocket.close()
                
if __name__ == '__main__':
    Main()

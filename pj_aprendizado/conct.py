import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "0.0.0.0"
port = 8888

try:
    server.bind((ip, port))
    server.listen(5)
    print(f"escutando:{ip}:{port}")

    (client_socket, address)=server.accept()

    while True:
        data = client_socket.recv(1500)
        
        if data == "exit":
            server.close()
    
except Exception as error:
    print (error)
    server.close()
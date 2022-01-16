import socket
from urllib import request, response
import MyPcWrapped


HOST = '0.0.0.0'
PORT = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))

server_socket.listen(1)

print(f"Listening on Port {PORT}")

while True:
    client_conn, client_addr = server_socket.accept()

    request = client_conn.recv(1024).decode()
    
    response = f"HTTP/1.0 200 OK\n\nMy Pc Wrapped\n\n{MyPcWrapped.apps_data}"
    client_conn.sendall(response.encode())
    client_conn.close()
server_socket.close()

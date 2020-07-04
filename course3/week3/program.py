import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(('data.pr4e.org', 80))
connection.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode())

while True:
    response = connection.recv(512)

    if len(response) < 1:
        break

    print(response.decode())

connection.close()
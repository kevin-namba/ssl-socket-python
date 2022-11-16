import socket, ssl

URL = '127.0.0.1'
PORT = 10025

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="keys/server.crt", keyfile="keys/server.key")

bindsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
bindsocket.bind((URL, PORT))
bindsocket.listen(5)

while True:
    newsocket, fromaddr = bindsocket.accept()
    connstream = context.wrap_socket(newsocket, server_side=True)
    try:
        data = connstream.read()
        print(data)
        connstream.write(data)
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()
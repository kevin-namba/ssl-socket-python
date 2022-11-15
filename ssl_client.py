import ssl
import socket
import pprint

URL = '127.0.0.1'
PORT = 10025

input_message = input()
context = ssl.create_default_context()
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.verify_mode = ssl.CERT_NONE 
context.check_hostname = False
conn = context.wrap_socket(socket.socket(socket.AF_INET),
           server_hostname=URL)
conn.connect((URL, PORT))
cert = conn.getpeercert()
pprint.pprint(cert)
# conn.sendall(b"HEAD / HTTP/1.0\r\nHost: linuxfr.org\r\n\r\n")
conn.sendall(input_message.encode('utf-8'))
pprint.pprint(conn.recv(1024).split(b"\r\n"))
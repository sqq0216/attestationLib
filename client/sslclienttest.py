import socket, ssl

# context = ssl.create_default_context()

# conn = context.wrap_socket(socket.socket(socket.AF_INET),server_hostname="127.0.0.1")
# conn.connect(("127.0.0.1", 10023))
# cert = conn.getpeercert()
# pprint.pprint(cert)
# conn.sendall(b"HEAD / HTTP/1.0\r\nHost: linuxfr.org\r\n\r\n")
# pprint.pprint(conn.recv(1024).split(b"\r\n"))


import socket
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
# I'm assuming this is not necessary, but I'd like to load the system provided CAs
context.set_default_verify_paths()
# Require CA validation to prevent MITM.
context.verify_mode = ssl.CERT_REQUIRED

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_client = context.wrap_socket(client_socket)
ssl_client.connect(('127.0.0.1', 23000))
ssl_client.send(bytes('hello, world!', 'UTF-8'))
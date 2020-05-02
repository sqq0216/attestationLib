# import socket, ssl
# # 服务端操作

# # 1.创建一个包含密钥和证书的上下文，以便客户检查该服务端真实性
# context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# context.load_cert_chain(certfile="./certs/server.crt", keyfile="./certs/server_rsa_private.pem.unsecure")

# # 2.创建一个socket并绑定端口进行监听
# bindsocket = socket.socket()
# bindsocket.bind(('127.0.0.1', 10023))
# bindsocket.listen(5)

# # 3. 使用accept与新的客户端建立连接
# while True:
#     newsocket, fromaddr = bindsocket.accept()
#     connstream = context.wrap_socket(newsocket, server_side=True)
#     try:
#         deal_with_client(connstream)
#     finally:
#         connstream.shutdown(socket.SHUT_RDWR)
#         connstream.close()

# # 4. 从connstream中读取数据
# def deal_with_client(connstream):
#     data = connstream.recv(1024)
#     # empty data means the client is finished with us
#     while data:
#         if not do_something(connstream, data):
#             # we'll assume do_something returns False
#             # when we're finished with client
#             break
#         data = connstream.recv(1024)
#     # finished with client
#     return data



# res = deal_with_client(connstream)
# print("jiehsou shuju is :",res)

import socket
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
print("./")
context.load_cert_chain(certfile="./certs/server.crt", keyfile="./certs/server_rsa_private.pem.unsecure")
context.load_verify_locations('./certs/ca.crt')
context.set_default_verify_paths()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 23000))
server_socket.listen(socket.SOMAXCONN)

def handle_client(ssl_socket):
    data = ssl_socket.read()
    while data:
        print("%s" % (str(data)))
        data = ssl_socket.read()

while True:
    client_socket, addr = server_socket.accept()
    ssl_client_socket = context.wrap_socket(client_socket, server_side=True)
    handle_client(ssl_client_socket)
# -*- coding: utf-8 -*-

import socket, time
import threading
import requests
import random
import string



#tcp连接处理
def tcplink(sock, addr):
    print("从%s %s...接收新的连接：" % addr)
    if sock.recv(1024).decode('utf-8')[0:6] == 'attest':
        sock.send(b'welcom')
        print("recv attest success")
        while True:
            data = sock.recv(1024)
            time.sleep(1)
            if not data or data.decode('utf-8') == 'exit':
                break
            print("server recv data",data,type(data))        
            #向服务端发送请求进行认证，认证接收到的数据
            attest_res = requests.get("https://www.baidu.com/")
            print("attest_res status_code is :", attest_res.status_code)
            if attest_res.status_code == 200:
                print("认证成功")
                salt = ''.join(random.sample(string.ascii_letters + string.digits, 6))
                sock.send(salt.encode(encoding='utf-8'))
            else:
                sock.send(b'failed')
                break
        sock.close()
        print('Connection from %s:%s closed.' % addr)
    else:
        sock.send(b'please')
        while True:
            data = sock.recv(1024)
            time.sleep(1)
            if not data or data.decode('utf-8') == 'exit':
                break
            sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
        sock.close()
        print('Connection from %s:%s closed.' % addr)
     


#创建socket并监听
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('等待连接')
while True:
    sock, addr = s.accept()
    print("sock is:", sock)
    print("and addr :", addr)
    tcplink(sock,addr)
    
s.close()
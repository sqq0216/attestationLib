# -*- coding: utf-8 -*-

import socket
import csv
import os

# 读取enclave认证报告相关数据
csv_reader_quote = csv.reader(open("./quote_data.csv"))
quote_data = []
attest_data = ''
for row in csv_reader_quote:
    quote_data.append(row)
for i in quote_data:
    attest_data += '  '+ attest_data.join(i)
# 读取程序运行数据
csv_reader_run_data = csv.reader(open("./run_data.csv"))
run_data = []
for row in csv_reader_run_data:
    run_data.append(row)


# 建立认证socket连接,并将结果存入buffer中
def attest_soc(s):
    
    s.send(b'attest')
    # 接收欢迎消息:
    print("welcom: ",s.recv(1024).decode('utf-8'))
    s.send(attest_data.encode(encoding='utf-8'))
    #接收success消息
    attest_res = s.recv(1024).decode('utf-8')
    print("attest_res",attest_res)
    if attest_res == 'failed':
        s.close()
    elif attest_res:
        s.send(b'exit')
        s.close()
    return attest_res

# 建立数据传输连接
def data_soc(s):
    s.send(b'rundat')
    # 接收欢迎消息:
    print("please: ",s.recv(1024).decode('utf-8'))
    for data in run_data:
        send_data = ''.join(data)
        s.send(send_data.encode(encoding='utf-8'))
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()
    

# main
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(attest_soc(s))
s.close()
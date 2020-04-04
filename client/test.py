# -*- coding: utf-8 -*-

import socket
import csv
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('127.0.0.1', 9999))
# s.send(b'rundat')
# # 接收欢迎消息:
# print("please: ",s.recv(1024).decode('utf-8'))
# for data in [b'1', b'2', b'3']:
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
# s.send(b'exit')
# s.close()

# 读取enclave认证报告相关数据
csv_reader_quote = csv.reader(open("./quote_data.csv"))
quote_data = []
attest_data = ''
for row in csv_reader_quote:
    quote_data.append(row)
for i in quote_data:
    print(i)
    attest_data += '  '+ attest_data.join(i)
    print("+++++++++",attest_data)

print(attest_data)
# 读取程序运行数据
csv_reader_run_data = csv.reader(open("./run_data.csv"))
run_data = []
for row in csv_reader_run_data:
    run_data.append(row)
print(run_data)

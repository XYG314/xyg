# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 12:09:02 2021

@author: 22972
"""

import socket
'''服务器地址'''

host = '82.156.28.204' #服务器地址
port = 2021 #端口号
addr = (host, port)

host2 = '103.46.128.46' #服务器地址
port2 = 47872 #端口号
addr2 = (host2, port2)


'''设置接受缓存'''
bufsize = 4096 

'''创建套接字，开始连接'''
tcpsock = socket.socket() 
tcpsock.connect(addr2)

'''接受服务器消息，根据指令进行输入'''
datare = tcpsock.recv(bufsize)
print(datare.decode('utf-8'))

'''输入提示指令并返回提示'''
while(True):
    data = input('请输入：')
    if not data:
        break
    tcpsock.send(data.encode('utf-8'))
    datare = tcpsock.recv(bufsize)
    print(datare.decode('utf-8'))
    '''
    datare2 = tcpsock.recv(bufsize)
    print(datare2.decode('utf-8'))
    '''
tcpsock.close()
    

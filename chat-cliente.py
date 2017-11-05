from socket import *
from threading import Thread
import os

flag = 0

def recebimento():
    global flag
    mensagem = ""
    while True:
        if flag == 1:
            flag=0
            break
        elif mensagem == "163563vxdgrw56732fdrwet4":
            os._exit(1)
            
        data = s.recv(1024)
        mensagem = str(data)
        print(mensagem)

s = socket()
server = 'localhost'
port = 7214
s.connect((server,port))
Thread(target=recebimento).start()
nick = raw_input("Digite seu nickname: ")
s.send(nick)
while True:
    mensagem = raw_input()
    if mensagem == "sair()":
        flag = 1
        s.send(mensagem)
        s.close()
        os._exit(1)
    else:
        s.send(mensagem)


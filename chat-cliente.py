from socket import *
from threading import Thread
import sys

flag = 0

def recebimento():
    global flag
    while True:
        if flag == 1:
            flag=0
            break
        data = s.recv(1024)
        mensagem = str(data)
        print(mensagem)

s = socket()
server = 'localhost'
port = 7212
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
        sys.exit()
    else:
        s.send(mensagem)


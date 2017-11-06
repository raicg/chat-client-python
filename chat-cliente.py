#Chat Client, its a client that connects to the chat server
#so it needs the chat server running to connect with
#The chat server, its a room chat that unlimited clients can connect to it
#All commented in portuguese-BR
#Created by: Rai Gondim

from socket import *
from threading import Thread
import os

flag = 0 #flag, quando ela for 1 o cliente quer sair, entao a thread de recebimento dele deve ser finalizada

def recebimento(): #thread de recebimento de mensagens
    global flag
    mensagem = ""
    while True: #ficar sempre aqui ate finalizar a thread
        if flag == 1: #se flag == 1 a thread sera finalizada
            flag=0
            break #quebra o ciclo do while, finalizado a thread
        elif mensagem == "163563vxdgrw56732fdrwet4": #se esse codigo for recebido, o cliente deve ser finalizado pois o servidor foi finalizado
            os._exit(1) #finaliza o cliente
            
        data = s.recv(1024) #recebe os dados do socket
        mensagem = str(data) #transforma os dados em uma string
        print(mensagem) #printa a mensagem no cliente

s = socket() #cria o socket
server = 'localhost' #endereco de ip do servidor
port = 7214 #porta do servidor
s.connect((server,port)) #conecta o socket
Thread(target=recebimento).start() #cria a thread do recebimento de mensagens
nick = raw_input("Digite seu nickname: ") #pede e recebe o nick do cliente
s.send(nick) #primeira mensagem a ser enviada e o nick
while True: #fica sempre aqui ate o cliente ser finalizado
    mensagem = raw_input() #recebe a mensagem
    if mensagem == "sair()": #se mensagem for == sair(), o cliente deve finalizar a thread de recebimento e depois finalizar o cliente
        flag = 1 #sinaliza flag=1 para que a thread seja finalizada
        s.send(mensagem) #envia ao servidor, para que o mesmo sinalize que o cliente esta saindo do bate papo
        s.close() # finaliza a conexao do socket
        os._exit(1) #finaliza o cliente
    else: #se mensagem nao for sair, envie a mensagem
        s.send(mensagem) #envia mensagem


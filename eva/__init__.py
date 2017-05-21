import codecs
import blowfish
import socket
import sys
import os
import random
import skippy

scriptpath = "../core/__init__.py.py"
sys.path.append(os.path.abspath(scriptpath))
import core

# __MAIN__
beta_a, beta_b, p, alpha = core.getEvaFiles()

sock = socket.socket()
sock.bind(('', 3333))
sock.listen(1)

print('Сервер запущен на 127.0.0.1:3333')
client, addr = sock.accept()

while True:
    data = client.recv(1024)

    if not data:
        break

    print('[<-----] ' + str(data))

    encdata = str(data, 'utf-8')

    if(encdata == '{service_message}'):

        client.send('{ready}'.encode())

        server = socket.socket()
        server.connect(('localhost', 8080))

        beta_c = pow(1, 1, p)

        # [client->eva] получаем ключ от клиента
        R_a = client.recv(1024)
        R_a = int(R_a)

        # [eva->server] пересылаем полученный ключ серверу
        server.send('{service_message}'.encode())
        server.recv(1024)

        server.send(str(R_a).encode())

        # [server->eva] получаем ключ от сервера
        R_b = server.recv(1024)
        R_b = int(R_b)

        # [eva->client] пересылаем ключ от сервера клиенту
        client.send(str(R_b).encode())

        # вырабатываем уникальный ключ




        # пересылаем клиенту 1







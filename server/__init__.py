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
b, alpha, beta_a, beta_b, p, y, q = core.getServerFiles()

sock = socket.socket()
sock.bind(('', 8080))
sock.listen(1)
print('Сервер запущен на 127.0.0.1:8080')
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)

    if not data:
        break

    print('[<-----] ' + str(data))

    encdata = str(data, 'utf-8')

    if(encdata == '{service_message}'):

        conn.send('{ready}'.encode())

        # step c-1
        R_a = conn.recv(1024)
        R_a = int(R_a)

        # check
        if (1 < R_a and beta_a < p and pow(R_a, q, p) == 1 and pow(beta_a, q, p) == 1):
            print('ok')
        else:
            print('error')
            exit()


        # step c-2
        r_b = random.randint(2, q-2)
        R_b = pow(alpha, r_b, p)
        conn.send(str(R_b).encode())

        # step e
        t_BA = pow(R_a, b, p)
        print('t_BA - %d' % t_BA)

        # step f
        u_BA = pow(beta_a, r_b, p)
        print('u_BA - %d' % u_BA)

        # step g
        w = pow(t_BA + u_BA, 1, p)
        print('w - %d' % w)
        # check
        if(w == 0):
            print('error')
            exit()

        # step h
        temp_l = w // pow(2, 1024 - 80)
        temp_r = pow(2, 80)
        v_1 = pow(temp_l, 1, temp_r)
        print('v_1 - %d' % v_1)

        temp_l = w // pow(2, 1024 - 160)
        temp_r = pow(2, 80)
        v_2 = pow(temp_l, 1, temp_r)
        print('v_2 - %d' % v_2)

        # MTI ADDED
        k = pow(beta_a, r_b, p)
        t_r = pow(R_a, b, p)
        k += t_r

        print('k - %d' % k)

print('finished')

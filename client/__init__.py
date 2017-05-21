import codecs
import blowfish
import socket
import sys
import os
import random

scriptpath = "../core/__init__.py.py"
sys.path.append(os.path.abspath(scriptpath))
import core

# __MAIN__
a, alpha, beta_a, beta_b, p, x, q = core.getClientFiles()

conn = socket.socket()
# conn.connect(('localhost', 8080))
# todo: uncomment for attack
conn.connect(('localhost', 3333))

conn.send('{service_message}'.encode())
conn.recv(1024)


# step c-1
r_a = random.randint(2, q-2)
R_a = pow(alpha, r_a, p)
conn.send(str(R_a).encode())

# step c-2
R_b = conn.recv(1024)
R_b = int(R_b)

# check
# todo: comment for attack
if(1 < R_b and beta_b < p and pow(R_b, q, p) == 1 and pow(beta_b, q, p) == 1):
    print('ok')
else:
    print('error')
    exit()

# step e
t_AB = pow(beta_b, r_a, p)
print('t_AB - %d' % t_AB)

# step f
u_AB = pow(R_b, a, p)
print('u_AB - %d' % u_AB)

# step g
w = pow(t_AB + u_AB, 1, p)
print('w - %d' % w)
# check
if(w == 0):
    print('error')
    exit()

# step h
temp_l = w // pow(2, 1024-80)
temp_r = pow(2, 80)
v_1 = pow(temp_l, 1, temp_r)
print('v_1 - %d' % v_1)

temp_l = w // pow(2, 1024-160)
temp_r = pow(2, 80)
v_2 = pow(temp_l, 1, temp_r)
print('v_2 - %d' % v_2)

# step i
pad = "0x72f1a87e92824198ab0b"
pad_i = int(pad, 16)

v1_b = int.to_bytes(v_1, v_1.bit_length() // 8 + 1, 'big')
v2_b = int.to_bytes(v_2, v_2.bit_length() // 8 + 1, 'big')

# v_2 // 2^16 mod 2^64
temp_l = pow(2, 16)
temp_l = v_2 // temp_l

temp_r = pow(2, 64)
temp_r = pow(temp_l, 1, temp_r)

# pad
temp_r = [int.to_bytes(a ^ b, 1, 'big') for (a, b) in zip(
    int.to_bytes(pad_i, pad_i.bit_length() // 8 + 1, 'big'),
    int.to_bytes(temp_r, temp_r.bit_length() // 8 + 1, 'big'))]

temp_r = b"".join(temp_r)

# MTI ADDED
k = pow(beta_b, r_a, p)
t_r = pow(R_b, a, p)
k += t_r

print('k - %d' % k)

print('finished')
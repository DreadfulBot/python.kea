# ПЭП Esign
import random
import math
import pickle
import sympy
from os import urandom
from math import sqrt
from itertools import count, islice
import chilkat

def GetRand(k1):
    a=random.randint(2**(k1-1),(2**k1)-1)
    return a
def primFerma(a,n):
    if pow(a,n-1,n)==1:
        return 2
    else:
        return 1
def GetP(q):
    N=pow(2,768)
    while(True):
        p=N*q+1
        if primFerma(3,p)==2:
            break
        else:
            N+=2
    return p,N
def getG(N,q,p):
    count=0
    while (True):
        a=random.randint(2,p)
        g=pow(a,N,p)
        if g==1:
            print("(((")
            continue
        else:
            break
    return g


def keyGeneration():
    # p - простое, p >= 1024 бит
    # q - делитель p-1

    q = GetRand(256)
    p, N = GetP(q)
    alpha = getG(N, q, p)

    # check alpha
    # t = pow(g, q, p)

    print ('p[%d] - %d' % (p.bit_length(), p))
    print ('q[%d] - %d' % (q.bit_length(), q))
    print ('alpha[%d] - %d' % (alpha.bit_length(), alpha))

    a = random.randint(1, q-1)
    b = random.randint(1, q-1)
    # a = random.randint(1, p-2)
    # b = random.randint(1, p-2)

    # beta_a, beta_b
    beta_a = pow(alpha, a, p)
    beta_b = pow(alpha, b, p)

    # x, y
    x = random.randint(1, p-2)
    y = random.randint(1, p-2)

    return beta_a, beta_b, a, b, alpha, x, y, p, q

# __MAIN__
beta_a, beta_b, a, b, alpha, x, y, p, q = keyGeneration()

print('Параметры успешно сгенерированы:\n'
        'beta_a[%d] - %d\n'
        'beta_b[%d] - %d\n'
        'a[%d] - %d\n'
        'b[%d] - %d\n'
        'alpha[%d] - %d\n'
        'x[%d] - %d\n'
        'y[%d] - %d\n'
        'p[%d] - %d\n'
        'q[%d] - %d' %
        (
        beta_a.bit_length(), beta_a,
        beta_b.bit_length(), beta_b,
        a.bit_length(), a,
        b.bit_length(), b,
        alpha.bit_length(), alpha,
        x.bit_length(), x,
        y.bit_length(), y,
        p.bit_length(), p,
        q.bit_length(), q))

# for client
pickle.dump(a, open('client/keys/a.key', 'wb'))
pickle.dump(beta_a, open('client/keys/beta_a.key', 'wb'))
pickle.dump(p, open('client/keys/p.key', 'wb'))
pickle.dump(x, open('client/keys/x.key', 'wb'))
pickle.dump(alpha, open('client/keys/alpha.key', 'wb'))
pickle.dump(beta_b, open('client/keys/beta_b.key', 'wb'))
pickle.dump(q, open('client/keys/q.key', 'wb'))

# for server
pickle.dump(b, open('server/keys/b.key', 'wb'))
pickle.dump(beta_b, open('server/keys/beta_b.key', 'wb'))
pickle.dump(p, open('server/keys/p.key', 'wb'))
pickle.dump(y, open('server/keys/y.key', 'wb'))
pickle.dump(alpha, open('server/keys/alpha.key', 'wb'))
pickle.dump(beta_a, open('server/keys/beta_a.key', 'wb'))
pickle.dump(q, open('server/keys/q.key', 'wb'))

# for eva
pickle.dump(beta_b, open('eva/keys/beta_b.key', 'wb'))
pickle.dump(p, open('eva/keys/p.key', 'wb'))
pickle.dump(alpha, open('eva/keys/alpha.key', 'wb'))
pickle.dump(beta_a, open('eva/keys/beta_a.key', 'wb'))

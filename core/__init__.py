import pickle
import skippy
import math

def getClientFiles():
    a = pickle.load(open('../client/keys/a.key', 'rb'))
    alpha = pickle.load(open('../client/keys/alpha.key', 'rb'))
    beta_a = pickle.load(open('../client/keys/beta_a.key', 'rb'))
    p = pickle.load(open('../client/keys/p.key', 'rb'))
    x = pickle.load(open('../client/keys/x.key', 'rb'))
    beta_b =  pickle.load(open('../client/keys/beta_b.key', 'rb'))
    q =  pickle.load(open('../client/keys/q.key', 'rb'))

    return a, alpha, beta_a, beta_b, p, x, q

def getServerFiles():
    b = pickle.load(open('../server/keys/b.key', 'rb'))
    alpha = pickle.load(open('../server/keys/alpha.key', 'rb'))
    beta_b = pickle.load(open('../server/keys/beta_b.key', 'rb'))
    p = pickle.load(open('../server/keys/p.key', 'rb'))
    y = pickle.load(open('../server/keys/y.key', 'rb'))
    beta_a = pickle.load(open('../server/keys/beta_a.key', 'rb'))
    q = pickle.load(open('../server/keys/q.key', 'rb'))

    return b, alpha, beta_a, beta_b, p, y, q

def getEvaFiles():
    beta_b = pickle.load(open('../eva/keys/beta_b.key', 'rb'))
    beta_a = pickle.load(open('../eva/keys/beta_b.key', 'rb'))
    p = pickle.load(open('../eva/keys/p.key', 'rb'))
    alpha = pickle.load(open('../eva/keys/alpha.key', 'rb'))

    return beta_a, beta_b, p, alpha

def skipjackEncrypt(key, val):
    block_size = 32
    res = b""

    cipher = skippy.Skippy(key)

    val_b = int.to_bytes(val, val.bit_length() // 8 + 1, 'big')
    i = math.ceil(len(val_b) / block_size)





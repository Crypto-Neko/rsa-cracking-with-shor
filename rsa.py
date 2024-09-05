from sage.all import *

class RSA():
    def __init__(self, size):
        self.size = size
        self.gen(self.size)
        
    def gen(self, size):
        p = random_prime(2**size, lbound=2**(size-1))
        q = random_prime(2**size, lbound=2**(size-1))
        
        self.n = p*q
        self.phi_n = (p-1)*(q-1)
        self.e = 65537
        self.d = inverse_mod(self.e, self.phi_n)

    def enc(self, m):
        return power_mod(m, self.e, self.n)

    def dec(self, c):
        return power_mod(c, self.d, self.n)

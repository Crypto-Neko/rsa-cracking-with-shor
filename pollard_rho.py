from math import gcd
from random import randint

def pollard_rho(n):
    x = randint(1, n-1)
    y = x
    c = randint(1, n-1)
    d = 1
    
    while d == 1:
        x = (x**2 + c) % n
        y = ((y**2 + c)**2 + c) % n
        d = gcd(abs(x - y), n)
        
    return d

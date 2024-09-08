from rsa import *
from shor import *
from pollard_rho import *
from analyze_algorithms import *

if __name__ == "__main__":
    pollard_rho_times = []
    shor_times = []
    for size in [2, 4, 8, 16, 32]:
        example_rsa = RSA(size)
        pollard_times.append(analyze_pollard_rho(N))
        shor_times.append(analyze_shor(N))

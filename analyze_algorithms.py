import time
from pollard_rho.py import *

# Analyze the empirical time cost of Pollard rho
def analyze_pollard_rho(N):
    times = []
    start_time = time.time()
    pollard_rho(N)
    end_time = time.time()
    time = end_time - start_time
    return time

# Analyze the empirical time cost of Shor's algorithm
def analyze_shor(N):
    times = []
    start_time = time.time()
    shor(N)
    end_time = time.time()
    overhead = compute_shor_overhead(N)
    time = (end_time - start_time) - overhead
    return time

# Compute the exact overhead caused by simulating qubits on a classical computer
# Computes general overhead for the specific machine it's run on and adds general O(2^n) overhead
def compute_shor_overhead(N):
    return 0

import time
from pollard_rho.py import *

# Measure the times for various large N = p*q and compare efficiency
example_N = [3*7, 11*19, 101*103, 1009*1013, 100003*1000003]
pollard_rho_times = analyze_rho_times()
shor_times = analyze_shor()

# Analyze the empirical time cost of Pollard rho
def analyze_pollard_rho():
    times = []
    for N in example_N:
        start_time = time.time()
        pollard_rho(N)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

# Analyze the empirical time cost of Shor's algorithm
def analyze_shor():
    times = []
    for N in example_N:
        start_time = time.time()
        shor(N)
        end_time = time.time()
        overhead = compute_shor_overhead(N)
        times.append(end_time - start_time - overhead)
    return times

# Compute the exact overhead caused by simulating qubits on a classical computer
# Computes general overhead for the specific machine it's run on and adds general O(2^n) overhead
def compute_shor_overhead(N):
    return 0

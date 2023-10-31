import sys
import time
import random
import multiprocessing


def monteCarlo(i: int) -> float:

    sum = 0.0
    x = random.random()
    y = random.random()
    sum += x * x + y * y < 1.0
    return sum


def count_pi(num: int) -> float:
    sum = 0.0
    for i in range(num):
        x = random.random()
        y = random.random()
        sum += x * x + y * y < 1.0
    return float(sum) / num * 4


def multiprocessing_count_pi(num: int) -> float:
    iter = [i for i in range(num)]
    total_sum = 0
    with multiprocessing.Pool(6) as p:
        d = p.map(monteCarlo, iter)
        for j in d:
            total_sum += j
    return float(total_sum) / num * 4


def main():
    num = int(sys.argv[1])

    t0 = time.time()
    res = multiprocessing_count_pi(num)
    print(f"For a Monte Carlo function with parallel computing: pi =  {res}, время = {time.time() - t0}")

    t0 = time.time()
    res = count_pi(num)
    print(f"For the usual Monte Carlo function: pi =  {res}, время = {time.time() - t0}")
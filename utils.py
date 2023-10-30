import multiprocessing
import random
from math import pi


def monteCarlo(i):
    sum = 0.0
    x = random.random()
    y = random.random()
    sum += (x * x +y * y < 1.0)
    return sum


def main():
    num = int(input("Enter the number of points to generate: "))
    iter = [i for i in range(num)]
    total_sum = 0
    with multiprocessing.Pool(multiprocessing.cpu_count() * 2) as p:
        # n_cores = multiprocessing.cpu_count()*2
        # print(f'Number of logical CPU cores: {n_cores}')
        d = p.map(monteCarlo, iter)
        for j in range(len(d)):
            total_sum += d[j]
        result = (total_sum/num) * 4
        print(f'pi method Monte-Carlo: {result}')
        print(f'pi: {pi}')
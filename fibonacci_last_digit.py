# Uses python3
import sys
import time
import math


def calc_fast(n):
    a = [0, 1, 0]

    for i in range(2, n + 1):
        a[2] = a[0] + a[1]
        a[0] = a[1]
        a[1] = a[2]
    return a[2] % 10




if __name__ == '__main__':
    n = int(input())
    print(calc_fast(n))





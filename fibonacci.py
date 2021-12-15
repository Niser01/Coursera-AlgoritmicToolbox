# Uses python3
import time


def calc_fast(n):
    a = []
    a.append(0)
    a.append(1)
    for i in range(2, n+1):
        a.append(a[i-1]+a[i-2])
    return a[n]


n = int(input())
print(calc_fast(n))



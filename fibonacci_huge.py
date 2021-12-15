# Uses python3
import math
import sys


def calc_fast(n):
    a = [0, 1, 0]
    for i in range(2, n + 1):
        a[2] = a[0] + a[1]
        a[0] = a[1]
        a[1] = a[2]
    return a[2]


def fibo(n, m):
    patron = [0, 1]
    i = 2
    while (True):
        fib = calc_fast(i)
        patron.append(fib % m)
        if (patron[i - 1] == 0 and patron[i] == 1):
            if (n < (i - 1)):
                return (patron[n])
            else:
                pasos = math.floor(n/(i-1))
                pos= n-(pasos*(i-1))
                return (patron[pos])

        else:
            i += 1


if __name__ == '__main__':

    input = input()
    n, m = map(int, input.split())
    print(fibo(n, m))

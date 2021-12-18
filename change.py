# Uses python3
import sys


def get_change(m):
    cant = 0
    while (m != 0):
        if (m - 10 >= 0):
            m = m - 10
            cant = cant + 1
        elif (m - 5 >= 0):
            m = m - 5
            cant = cant + 1
        else:
            m = m - 1
            cant = cant + 1
    return cant


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))

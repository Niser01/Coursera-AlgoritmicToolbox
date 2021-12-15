# Uses python3
import sys


def maine(a, b):
    while(True):
        c=a%b
        a= b
        b=c
        if (b==0):
            return a


if __name__ == "__main__":
    input = input()
    a, b = map(int, input.split())

    print(maine(a,b))

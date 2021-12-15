# Uses python3
import sys


def lcm(a,b):
    maxi=max(a,b)
    mini=min(a,b)
    lcm=maxi
    while(lcm%mini !=0):
        lcm+=maxi

    return lcm




if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())
    print(lcm(a, b))

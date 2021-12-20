# python3
import sys


def compute_min_refills(distance, tank, stops):
    distRecorida = 0
    resultado = 0
    contador = 0

    if (tank >= distance):
        return 0

    distRecorida = distRecorida + tank

    for i in range(len(stops)):

        if (stops[i] > distRecorida):

            if (stops[i] - distRecorida > tank):
                return -1

            distRecorida = stops[i - 1]
            resultado += 1
            distRecorida = distRecorida + tank

    if (distance - distRecorida < tank):
        return resultado


if __name__ == '__main__':
    d = input()
    m = input()
    n = input()
    stops = list(map(int, input().split()))
    stops.insert(0, 0)
    stops.append(int(d))
    print(compute_min_refills(int(d), int(m), stops))

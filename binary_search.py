import math


def binary_search(keys, low, high, query):
    if (high < low):
        return - 1
    mid = math.floor(low + ((high - low) / 2))

    if (query == keys[mid]):
        return mid

    if (high == low):
        return -1

    elif (query < keys[mid]):

        return binary_search(keys, low, (mid - 1), query)
    else:

        return binary_search(keys, (mid + 1), high, query)


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    input_keys.sort()
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries
    low = 0
    high = len(input_keys) - 1

    for q in input_queries:
        print(binary_search(input_keys, low, high, q), end=' ')

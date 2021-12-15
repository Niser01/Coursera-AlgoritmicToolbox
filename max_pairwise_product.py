def max_pairwise_product(numbers):
    n = len(numbers)
    max1 =0
    max2=0
    pos=0

    for i in range(n):
        if(numbers[i]>max1):
            max1=numbers[i] 
            pos = i

    for j in range(n):
        if(numbers[j]>max2 and j != pos):                     
            max2=numbers[j]

    return max1*max2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    
    print(max_pairwise_product(input_numbers))

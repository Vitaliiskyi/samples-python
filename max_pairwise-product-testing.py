import numpy

def max_pairwise_product_slow(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
             max_product = max(max_product, numbers[first] * numbers[second])

    return max_product


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    num1 = 0
    num2 = 0
    for i in range(n):
        if numbers[i] >= num1:
            num2 = num1
            num1 = numbers[i]
        elif num1 > numbers[i] > num2:
            num2 = numbers[i]
    max_product = num1*num2

    return max_product




# Testing
flag = True
while flag == True:
    
    # Generate random list integers
    l = list(numpy.random.randint(1, 10000, 100))
    if max_pairwise_product(l) == max_pairwise_product_slow(l):
        print()
        print(l)
        print(max_pairwise_product(l),  max_pairwise_product_slow(l))
        print("Ok")
        print()
    elif max_pairwise_product(l) != max_pairwise_product_slow(l):
        flag = False
        print()
        print(l)
        print(max_pairwise_product(l),  max_pairwise_product_slow(l))
        print("Error")
        print()

#if __name__  == '__main__' :
#    _ = int(input())
#    input_numbers = list(map(int, input().split()))
#    print(max_pairwise_product(input_numbers))
















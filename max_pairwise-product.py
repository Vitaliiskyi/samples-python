def max_pairwise_product(numbers):
    
    '''Finds the two largest numbers in a list, 
    and returns their product. 
    The function is optimized for speed, 
    tests from Coursera.'''

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

if __name__  == '__main__' :
    #_ = int(input())
    input_numbers = list(map(int, input().split())) # Enter numbers separated by spaces
    print(max_pairwise_product(input_numbers))
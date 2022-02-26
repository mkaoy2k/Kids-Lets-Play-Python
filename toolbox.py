import random
import traceback


def get_function_name():
    return traceback.extract_stack(None, 2)[0][2]

# 函式: 求兩整數的最大公約數


def gcd(a, b):
    """ This is a recursive function
    to determin the greatest common divisor among 2 integers
    """
    if not isinstance(a, int):
        print(f'{get_function_name()}: Invalid integer {a}!')
        return

    if not isinstance(b, int):
        print(f'{get_function_name()}: Invalid integer {b}!')
        return

    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# Example gcd
if __name__ == '__main__':
    print(f'gcd(16,4) = {gcd(16, 4)}\n')
    print(f'gcd(20,30) = {gcd(20, 30)}\n')


def factorial(num):
    """ This is a recursive function
    to find the factorial of a positive integer
    """
    if isinstance(num, int) and num > 0:
        if num == 1:
            return 1
        return (num * factorial(num - 1))
    else:
        print(f'{get_function_name()}: Invalid positive integer!')


# Example factorial
if __name__ == '__main__':
    num = 7
    print(f'{num}! = {factorial(num)}\n')

    num = 'string'
    print(f'{num}! = {factorial(num)}\n')

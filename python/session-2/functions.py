# def greeting(name, age):
#     print("hello " + name)
#     return age + 1
#
# def example():
#     return True
#
# age = greeting("Matthew", 18)
# name = "Matthew"
# print("Your age next year will be 19")
#
# if example():
#     print("printing")

#f(x) = x^2 + 6x + 3
#
# import math
#
# def f(x):
#     return math.pow(x, 2) + 6 * x + 3
#
#
# print(f(1))

# def print_numbers(count):
#
#     if (count == 0):
#         return
#
#     count = count - 1
#     print(count)
#     print_numbers(count)
#
# print_numbers(1)


# def recursive_mult(number, times):
#     if (times == 1):
#         return number
#     else:
#         return number + recursive_mult(number, times - 1)
#
# print(recursive_mult(5, 2)) # 10
'''
print(recursive_mult(5, 2))
    NUMBER = 5
    TIMES = 2

    TIMES != 1, SO RETURN: 5 + recursive_mult(number, times - 1)
                                    NUMBER = 5
                                    TIMES = 1

                                    TIMES == 1, SO RETURN 5
'''

# def reverse_string(word, length):
#     if (length == 1):
#         return word[0]
#     else:
#         return word[length - 1] + reverse_string(word, length - 1)
#
#
# word = "Matthew"
# print(reverse_string(word, len(word)))

# 0, 1, 1, 2, 3, 5, 8, 13, 21
def fib(n):

    if(n == 0):
        return 0

    elif (n == 1):
        return 1

    else:
        return fib(n-1) + fib(n-2)

print(fib(5))
fib(5)

'''
#     5 != 0 and 5 != 1 so RETURN:    fib(4)                  +                                   fib(3)
#                                         fib(3)              +           fib(2)                      fib(2)                  +       fib(1)
#                                             fib(2)          +           fib(1)     +                    fib(1) + fib(0)                 fib(1) + fib(0)     +            1
#                                                 fib(1)  + fib(0)    +       1       +                       1       0                   1           0
#                                                     1   +   0
#
# '''

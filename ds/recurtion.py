# def factorial(n):
#     if n < 0:
#         return None
#     if n in [0, 1]:
#         return 1
#     return n * factorial(n - 1)
# fact=factorial(5)
# print(fact)

# def test_factorial():
#     assert factorial(5) == 120
#     assert factorial(4) == 24
#     assert factorial(3) == 6
#     assert factorial(-1) == None

# stack overflow
# def fuc():
#     fuc()
# if __name__ == '__main__':
#     fuc()

# fibonacci
# def fibonacci(n):
#     if n in [1,2]:
#         return 1
#     return fibonacci(n-1)+fibonacci(n-2)

# def test_fibonacci():
#     fib=[1,1,2,3,5,8,13,21,34,55]
#     for k,v in enumerate(fib):
#         assert fibonacci(k+1) == v


# def fibonacci(n):
#     print('Trying to fibonacci for', n)
#     if n in [1, 2]:
#         return 1
#     return fibonacci(n - 2) + fibonacci(n - 1)
# if __name__ == '__main__':
#     print('Print fibonacci number is:',fibonacci(5))

def print_number(n):
    if n==0:
        return
   
    print_number(n-1)
    print(n)
if __name__ == '__main__':
    print_number(5)
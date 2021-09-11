# Exercise 1: Create a function that can accept two arguments name and age and print its value

def func(name, age):
    print(name, age)
func("John", 30)


# Exercise 2: Write a function func1() such that it can accept a variable length of  argument and print all arguments value
list_of_nums = []
def func1(*args):
    for i in args:
        if i not in list_of_nums:
            list_of_nums.append(i)
    
func1(1,2,3,4,5,6,7,8,9,10,10,11,9,8)
print(list_of_nums)  

# Exercise 3: Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of them. And also it must return both addition and subtraction in a single return call

def calculation(a, b):
    return a + b, a - b ,a * b 
add, sub, mul = calculation(10, 20)
print(add, sub, mul)



# Exercise 4: Create a function showEmployee() in such a way that it should accept employee name, and its salary and display both. If the salary is missing in the function call assign default value 9000 to salary
def showEmployee(name, salary = 9000):
    print(name, salary)
showEmployee("John", "1000")
showEmployee("John")



# Exercise 5: Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it

def addition(a, b):
    def inner(a, b):
        return a + b
    return inner(a, b) + 5
print(addition(10, 20))


# Exercise 6: Write a recursive function to calculate the sum of numbers from 0 to 10

def sum(n):
    if n:
        return n + sum(n-1)
    else:
        return 0
result = sum(10)
print(result)


# Exercise 7: Assign a different name to function and call it through the new name

def display(name):
    print(name)
display("John")
show=display
show("mark")


# Exercise 8: Generate a Python list of all the even numbers between 4 to 30
print(list(range(4,31,2)))































# user define 

# def sum_of_nums(nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total
# nums = [1,2,3,4,5,6,7,8]
# print(sum_of_nums(nums))

# build in 

# def sum_of_numbers(nums):
#     total = sum(nums)
#     return total
# print(sum_of_numbers([1,2,3,4,5,6,7,8]))

# user defined
# def get_largest_value(nums):
#     largest = nums[0]
#     for num in nums:
#         if num > largest:
#             largest = num
#     return largest
# print(get_largest_value([1,2,3,4,5,6,7,8]))


# build in
# def get_largest_value(nums):
#     largest = max(nums)
#     return largest
# print(get_largest_value([1,2,3,4,5,6,7,8]))
    


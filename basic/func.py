
# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters ( hours and  rate).
# def pay(hours, rate):
#     return hours * rate + (hours - 40) * rate * 0.5

# print(pay(45,10))



# *args
# def displayPerson(*args):
#     for i in args:
#         print(i)

# displayPerson(1,2,'atik')




# Python program to illustrate
# *kargs for variable number of keyword arguments

# def myFun(**bal):
# 	for key, value in bal.items():
# 		   print ("%s == %s" %(key, value))
# myFun(first ='Geeks', mid ='for', last='Geeks',bal='hi')


# def display(**kwargs):
#     for i in kwargs:

#         return i
# print( display(emp="Kelly", salary=9000))


# def fun1(num):
#     return num + 25

# fun1(5)
# print(num)

# def outerFun(a, b):
#     def innerFun(c, d):
#         return c + d
#     return innerFun(a, b)
    

# result = outerFun(5, 10)
# print(result)







# lambda function
# a=(lambda a,b:a+b)(2,3)
# print(a)




# map function
# number_list = [1,2,3,4,5,6,7,8,9,10]

# def square(num):
#     	return num % 2 == 0
# a=map(square, number_list)

# b=map(lambda num: num ** 2, number_list)
# print(list(a),list(b))




# filter 
# numbers = [1,2,3,4,5,6,7,8,9,10]

# def even(num):
#     	return num % 2 == 0

# even_numbers = filter(even, numbers)
# print(list(even_numbers))

# numbers = filter(lambda num: num % 2 == 0, numbers)
# print(list(numbers))



# The filter() and map() functions are a little bit different. While Maps takes a normal function, Filter takes Boolean functions. As a matter of fact, filter are maps with conditional logic, a Boolean logic

# def check(num):
#     return num*1

# nums = [0,2, 4, 6, 7, 8]
# result = filter(check, nums)
# print(list(result))



# def check(num):
#     return num*1
# nums = [0,2, 4, 6, 7, 8]
# result = map(check, nums)

# print(list(result))



#  list comprehension [expr for val in collection if condition]

# num=[1,2,3,4,5,6,7,8,9,10]
# numbers = filter(lambda num: num % 2 == 0, num)

# result =[x for x in num if x%2==0]
# print(result,list(numbers))


# map1= map(lambda num: num*num, num)
# result1= [x*x for x in num]
# print(list(map1),result1)





# zip functions

# roll=[101,102,103,104]
# name=['mark','harry','larry','john']
# print(list(zip(roll,name,'ahlj')))





# Factorial using recursive
# number = int(input("Enter a number: "))
# def factorial(number):
# 	if number == 1:
# 		return number
# 	else:
# 		return number * factorial(number-1)
# print(factorial(number))



# callback function

def callbackFunc(s):
    print('Length of the text file is : ', s)


def printFileLength(path, callback):
    f = open(path, "r")
    length = len(f.read())
    f.close()
    callback(length)

if __name__ == '__main__':
    printFileLength("sample.txt", callbackFunc)













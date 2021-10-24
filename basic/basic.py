# num=int(input("Enter a number: "))
# for i in range(1,11):
#     print(num,"x",i,"=",num*i)

# my_list = []
# for i in range(1,100):
#     if i%3 == 0 and i % 5 != 0:
#         my_list.append(i)
# print(my_list)

# Read 2 variables, named A and B and make the sum of these two variables, assigning its result to the variable X. Print X as shown below. Print endline after the result otherwise you will get “Presentation Error”

# A=int(input())
# B=int(input())
# X=A+B
# print('X','=',X,'\n')

# a = [40, 45, 33, 34, 8, 38, 28, 22, 1, 7, 49, 41, 14, 5, 22, 39, 15, 19, 36, 37, 43, 2, 5, 42, 46, 48, 49, 12, 48, 37, 8, 20, 30, 20, 4, 37, 27, 29, 7, 44, 15, 32, 35, 10, 28, 18, 2, 15, 36, 38]


# my_list=[]
# for i in a:
#     if i not in my_list:
#             my_list.append(i)
# print(my_list)


# input row many value are there in a list then insert one by one value
# list_of_nums = []
# def func1(*args):
#     for i in args:
#         if i not in list_of_nums:
#             list_of_nums.append(i)
    
# func1(1,2,3,4,5,6,7,8,9,10,10,11,9,8)
# print(list_of_nums)  


# def student(*details):
#     sum=0
#     for i in details:
#         sum=sum+i
#     print(sum)
      
# student(1,2,3,4,5,6,7,8,9,10,10,11,9,8)  
# print(student(1,2,3,4,5,6,7,8,9,10,10,11,9,8))

# Python program to illustrate
# *args with first extra argument
# def myFun(arg1, *argv):
#   print ("First argument :", arg1)
#   for arg in argv:
#       print("Next argument through *argv :", arg)

# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


def voter(age):
    if age<18:
        raise ValueError ("Invalid")
    return "Your are allow"
try:
    age=int(input("enter age"))
    print(voter(age))
except ValueError as e:
    print(e)
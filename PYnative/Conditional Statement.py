# Exercise 1: Print First 10 natural numbers using while loop
# n = 0
# while n <= 10:
#     print(n)
#     n += 1
    
    
# Exercise 3: Accept number from user and calculate the sum of all number from 1 to a given number
# sum=0
# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     sum=sum+i
# print("The sum of all natural numbers from 1 to",n,"is",sum)


# Exercise 4: Print multiplication table of a given number
# n=int(input("Enter a number: "))
# for i in range(1,11):
#     product=n*i
#     print(n,"*",i,"=",product)


# Exercise 5: Given a list, iterate it, and display numbers divisible by five, and if you find a number greater than 150, stop the loop iteration.
# list=[10,20,30,40,50,60,70,80,90,100,101,102,103,109,140,150,155,160]
# for i in list:
#     if i > 150:
#         break
#     if i%5==0:
#      print(i)


# Exercise 6: Given a number count the total number of digits in a number
# number=int(input("Enter the number"))
# count=0
# while number !=0:
#     number=number//10
#     count=count+1
# print("Total number of digits in the number:",count)

# Exercise 8: Reverse the following list using for loop
# list1=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(list1)-1,-1,-1):
#     print(list1[i])


# Exercise 9: Display numbers from -10 to -1 using for loop
# n=-10 
# while n <= -1:
#     print(n)
#     n=n+1
# print("End of loop")



# Exercise 11: Write a program to display all prime numbers within a range
# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))
# print("Prime numbers between {start} and {end} are displayed".format(start=start, end=end))

# for i in range(start, end+1):
#     if i > 1:
#         for j in range(2,i):
#             if (i % j) == 0:
#                 break
#         else:
#             print(i)


# Exercise 12: Display Fibonacci series up to 10 terms
# terms=int(input("Enter the number of terms: "))
# number1,number2=0,1
# next_term=number1+number2
# for i in range(terms):
#     print(next_term)
#     next_term=number1+number2
#     number1=number2
#     number2=next_term


# Exercise 13: Write a loop to find the factorial of any number
# number=int(input("Enter a number: "))
# while number !=0:
#     factorial=1
#     while number >=1:
#         factorial=factorial*number
#         number=number-1
#     print("Factorial of",number,"is",factorial)


# Exercise 14: Reverse a given integer number
# number=int(input("Enter a number: "))
# reverse=0
# while number !=0:
#     rem=number%10   #123%10=3 #12%10=2 #1%10=1
#     reverse=reverse*10+rem #0=0*10+3=3 #3=3*10+2=32 #32=32*10+1=321
#     number=number//10 #123//10=12 #12//10=1 #1//10=0
# print("Reverse of the number:",reverse)


# Exercise 15: Use a loop to display elements from a given list that are present at odd index positions
# list = [1,2,3,4,5,6,7,8,9,10]
# for i in list[1::2]:
#     print(i)

# Exercise 16: Display the cube of the number up to a given integer

# number = int(input("Enter a number: "))
# for i in range(1,number+1):
#     print('This {} Cube is {}'.format(i,i**3))

# Exercise 17: Find the sum of the series 2 +22 + 222 + 2222 + .. n terms

# terms=int(input("Enter the number of terms: "))
# start=2
# sum=0
# for i in range(0,terms):
#     sum=sum+start
#     start=(start*10)+2
# print("Sum of even terms is:",sum)



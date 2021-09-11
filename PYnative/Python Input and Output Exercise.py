# Exercise 1: Accept two numbers from the user and calculate multiplication
num1, num2 = input("Enter two numbers to multiply: ").split()
mul = int(num1) * int(num2)
print("{} * {} = {}".format(num1, num2, mul))


# Exercise Question 2: Display “My Name Is James” as “My**Name**Is**James” using output formatting of a print() function
print('My', 'name', 'is','Atik',sep="-")


# Exercise 3: Convert decimal number to octal using print() output formatting
print('%o,' % (8))
print('%x,' % (9))

# Exercise 4: Display float number with 2 decimal places using print()
num=float(input("Enter a number: "))
print('{:.2f}'.format(num))


# Exercise 5: Accept a list of 5 float numbers as an input from the user
list =[]
num=int(input("Enter list size: "))

for i in range(0,num):
    print("Enter number",i+1,": ",end="")
    list.append(float(input()))

print(list)


# Exercise 7: Accept any three string from one input() call
str1, str2, str3 = input("Enter three strings: ").split()
print("{} {} {}".format(str1, str2, str3))



# Exercise 8: Format the following data using a string.format() method.
totalMoney = int(input("Enter total money: "))
quantity = int(input("Enter quantity: "))
price = int(input("Enter price: "))

print('I have {} dollar.so I can buy  {} football for  {} dollars'.format(totalMoney, quantity, price))



# Exercise 9: How to check file is empty or not
import os
print(os.stat('test.txt').st_size==0)



# Exercise 10: Read line number 4 from the following file
with open('test.txt') as f:
    print(f.readlines()[3])
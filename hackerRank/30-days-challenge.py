# 3# inputString = input()
# print('Hello, World.')
# print(inputString)

# 2# first_int = 4
# first_float = 4.0
# first_str = 'HackerRank'

# second_int = int(input())
# second_float = float(input())
# second_str = str(input())

# int_sum = first_int + second_int
# float_sum = float(first_float + second_float)
# str_sum = first_str + " " + second_str

# print(int_sum)
# print(float_sum)
# print(str_sum)


# 3# meal_cost = float(input())

# tip_percent = int(input())

# tax_percent = int(input())

# def solve(meal_cost, tip_percent, tax_percent):

#     tip=meal_cost*tip_percent/100
#     tax=meal_cost*tax_percent/100
#     total_cost = meal_cost + tip + tax

#     return round(total_cost)

# print(solve(meal_cost, tip_percent, tax_percent))

# num=int(input())
# if num%2!=0:
#     print("Weird")
# elif num%2==0 and num>=2 and num<=5:
#     print("Not Weird")
# elif num%2==0 and num>=6 and num<=20:
#     print("Weird")
# elif num%2==0 and num>20:
#     print("Not Weird")


# def string_XOR(str1, str2):
#     xor_str = ''
#     for i in range(len(str1)):
#         if str1[i] == str2[i]:
#             xor_str += '0'
#         else:
#             xor_str += '1'
#     return xor_str
# str1 = input()
# str2 = input()
# print(string_XOR(str1, str2))

# class Person:
#     def __init__(self, initialAge):
#         if initialAge < 0:
#             print("Age is not valid, setting age to 0.")
#             self.age = 0
#         else:
#             self.age = initialAge
        
#     def amIOld(self):
#         if self.age < 13:
#             print("You are young.")
#         elif self.age >= 13 and self.age < 18:
#             print("You are a teenager.")
#         else:
#             print("You are old.")
#     def yearPasses(self):
#         self.age += 1

# if __name__ == '__main__':
#     t = int(input())
#     for i in range(0, t):
#         age = int(input())
#         p = Person(age)
#         p.amIOld()


# num=int(input())
# for i in range (1,11):
#     print(num,'x',i,'=',num*i)


# def evenOddCharacterIndex(str):
#     even_index = ""
#     odd_index = ""
#     for i in range(len(str)):
#         if i % 2 == 0:
#             even_index += str[i]
#         else:
#             odd_index += str[i]
#     return even_index, odd_index

# if __name__ == '__main__':
#     num=int(input())
#     for _ in range(num):
#         str=input()
#         even_index, odd_index = evenOddCharacterIndex(str)
#         print(even_index, odd_index)



# n = int(input().strip())
# arr = list(map(int, input().rstrip().split()))
# arr.reverse()
# for i in range(len(arr)):
#         print(arr[i], end = " ")


# n=int(input().strip())
# arr1=list(map(int,input().strip().split()))
# arr2=list(map(int,input().strip().split()))
# for i in range(n):
#     # op same line as below
#     print(arr1[i]+arr2[i],sep=" ",end=" ")


# n=int(input())
# phone_book = {}
# for i in range(n):
#     li=list(map(str, input().split()))
#     key = li[0]
#     value= li[1]
#     phone_book[key] = value
    
# while True:
#     try:
#         name=input()
#         if name in phone_book:
#             print(name+"="+str(phone_book[name]))
#         else:
#             print("Not found")
#     except:
#         break


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)


# class Person:
#     def __init__(self, firstName, lastName, idNumber):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.idNumber = idNumber
#     def printPerson(self):
#         print("Name:", self.lastName + ",", self.firstName)
#         print("ID:", self.idNumber)
  
# class Student(Person):
#     def __init__(self, firstName, lastName, idNumber, scores):
#         super().__init__(firstName, lastName, idNumber)
#         self.scores = scores
#     def calculate(self):
#         avg = sum(self.scores)/len(self.scores)
#         if avg < 40:
#             return 'T'
#         elif avg < 55:
#             return 'D'
#         elif avg < 70:
#             return 'P'
#         elif avg < 80:
#             return 'A'
#         elif avg < 90:
#             return 'E'
#         else:
#             return 'O'
# line = input().split()
# firstName = line[0]
# lastName = line[1]
# idNum = line[2]

# numScores = int(input()) # not needed for Python
# scores = list( map(int, input().split()) )
# s = Student(firstName, lastName, idNum, scores)
# s.printPerson()
# print("Grade:", s.calculate())
# class Triangle:
from django.core.files import temp


class Triangle:
    # constructor
    def __init__(self,base,height):
        self.base = base
        self.height = height
        # method
    def area(self):
        return (self.base*self.height)/2
    def display(self):
        print(f'Area of Triangle is {self.area()}')
T1=Triangle(10,20)
T2=Triangle(20,30)
T1.display()
T2.display()

# triangle without constructor

class Triangle:
    base = 10
    def area(self):
        return (self.base*self.height)/2
    def display(self):
        print(f'Area of Triangle is {self.area()}')

T1 = Triangle()
T2 = Triangle()
T1.height = 20
T2.height = 30
T1.display()
T2.display()


# Inheritance example
class Men:
    def walk(self):
        print('I cam walk')
    def talk(self):
        print('I cam talk')
class Student(Men):
    def read(self):
        print('I cam read')

s1=Student()
s1.read()
s1.talk()
s1.walk()

# class Phone:
class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def fullname(self):
        print(f'{self.brand} {self.model}')

class Smartphone(Phone):
    def __init__(self,brand,model,price,ram,internal):
        Phone.__init__(self,brand,model,price)
        self.ram = ram
        self.internal = internal
    def fullname(self):
        print(f'Brand:{self.brand} Model: {self.model} {self.price}')

S1=Smartphone('Nokia','1100',10000,4,16)

S2=Smartphone('Samsung','Galaxy',20000,8,32)
S1.fullname()
S2.fullname()


# Method overriding
class Phone:
    def __init__(self):
        print('Phone class')

class Smartphon(Phone):
    # inherited from Phone class
    def __init__(self):
        super().__init__()
        print('Smartphone class')

s1=Phone()
s2=Smartphon()


# inherited

class Shape:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(f'Area of shape is {self.area()}')

class Triangle(Shape):
    def area(self):
       area= (self.length*self.breadth)/2
       print(f'Area of Triangle is {area}')

class Rectangle(Shape):
    def area(self):
       area= (self.length*self.breadth)
       print(f'Area of Rectangle is {area}')

t1=Triangle(20,30)
r1=Rectangle(20,30)
t1.area()
r1.area()


# class A:
#     def display(self):
#         print('I am A class')
# class B(A):
#     def display1(self):
#         print('I am B class')
# class C(B):
#     def display2(self):
#         super().display()
#         super().display1()
#         print('I am C class')

# obj1 = C()
# obj1.display2()


# class A:
#     def display(self):
#         print('I am A class')

# class B:
#     def display(self):
#         print('I am B class')

# class C(A,B):
#     pass

# obj1 = C()
# obj1.display()


# # abstraction example
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     def __init__(self,length,breadth):
#         self.length = length
#         self.breadth = breadth
#     @abstractmethod
#     def area(self):
#         pass

# class Triangle(Shape):
#     def area(self):
#         area = (self.length*self.breadth)/2
#         print(f'Area of Human is {area}')

# class Rectangle(Shape):
#     def area(self):
#         area = (self.length*self.breadth)
#         print(f'Area of rectangle is {area}')


# # Driver code
# R = Triangle(10,20)
# R.area()

# S=Rectangle(10,20)
# S.area()


# Polymorphic example

# Built in Polymorphic
# print(len('Hello'))
# print(len([1,2,3]))

# user define polymorphic
# def add(x,y,z=0):
#     return x+y+z
#
# print(add(1,2,3))
# print(add(1,2))
#
# def add(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum
# print(add(1,2,3,4,5))


# Magic method
# class Bike:
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
#     def __eq__(self, other):
#         return self.name == other.name and self.color == other.color
#     # def __str__(self):
#     #     return f'Bike name is {self.name} and color is {self.color}'
#     def __repr__ (self):
#         return f'Bike name is {self.name} and color is {self.color}'
# bike1 = Bike('Pulsar', 'Red')
# bike2 = Bike('Pulsar', 'Red')
# print(bike1 == bike2)


# Regular expression
# import re
#
# pattern = r"color"
# if re.search(pattern, 'Red is a color'):
#     print("Match")
# else:
#     print("Not a color")



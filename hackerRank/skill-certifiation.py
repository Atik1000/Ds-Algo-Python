# Given a number n,for each number i in the range 1 to n inclusive, print one value per line as follows:
# if i is a multiple of both 3 and 5, print "FizzBuzz"
# if i is a multiple of 3, print "Fizz"
# if i is a multiple of 5, print "Buzz"
# if i is a multiple of 3 or 5, print the value of i

# def fizzBuzz(n):
#     # Write your code here
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)
# if __name__ == '__main__':
#     n = int(input())
#     fizzBuzz(n)



# A multiset is the same as a set except that an element might occur more than once in a multiset.Implement a multiset data structure in python.Given a template for multiset class, implement a multiset class , implement 4 methods:
# add(self,value):adds a value to the multiset
# remove(self,value):removes a value from the multiset;otherwise,do nothing
# __contains__(self,value):returns True if value is in the multiset,otherwise,return False
# __len__(self):returns the number of elements in the multiset


# class Multiset:
#     def __init__(self):
#         self.set = set()

#     def add(self, value):
#         self.set.add(value)

#     def remove(self, value):
#         if value in self.set:
#             self.set.remove(value)

#     def __contains__(self, value):
#         return value in self.set

#     def __len__(self):
#         return len(self.set)


# if __name__ == '__main__':

#   m=Multiset()
#   n=int(input())
#   for i in range(n):
#     s=input().split()
#     if s[0]=="add":
#       m.add(int(s[1]))
#     elif s[0]=="remove":
#       m.remove(int(s[1]))
#     elif s[0]=="query":
#       print(m.__contains__(int(s[1])))
#     elif s[0]=="size":
#       print(m.__len__())
        

# Implement the class :VendingMachine according the following conventions

# can be instantiated using the constructor:
# VendingMachine(num_items,items price) where num_items denotes the number of items in the machine and items price is a list of prices denotes the required number of coins to buy a single item
# has a method buy (req_items,money) that represents a buy request where req_items denotes the request number of items and money denotes the number of coins inserted by the customer puts into the machine,one of the following conditions must be satisfied:
# if there are enough items in the machine to serve the requested number of items. The method returns a integer denotes the change given back after the purchase 
# If there are fewer items in the machine than requested number,it raise a value error  exception with the message "Not enough items in the machine"
# if there are enough items in the machine to serve the request but the given amount of money is less than their cost,it raise a value error exception with the message "Not enough coins"

# class VendingMachine:
#     def __init__(self, num_items, items_price):
#         self.num_items = num_items
#         self.items_price = items_price
#         self.items_in_machine = [0] * num_items
#         self.coins_in_machine = 0

#     def buy(self, req_items, money):
#         if req_items > self.num_items:
#             raise ValueError("Not enough items in the machine")
#         if money < self.items_price[req_items]:
#             raise ValueError("Not enough coins")
#         self.items_in_machine[req_items] += 1
#         self.coins_in_machine += money - self.items_price[req_items]
#         return money - self.items_price[req_items]


# if __name__ == '__main__':
#     m = VendingMachine(int(input()), list(map(int, input().split())))
#     for _ in range(int(input())):
#         try:
#             print(m.buy(int(input()), int(input())))
#         except ValueError as e:
#             print(e)



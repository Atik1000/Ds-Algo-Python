# List
# ADD method

# list append method
# Syntax append(object)
# The append() method adds an item to the end of the list.
# Add last an element to the list
animals =['dog', 'cat', 'mouse', 'horse', 'cow']
animals.append('pig')
# print(animals)




# list extend method
# Syntax extend(list)
# The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
# add a list to another list

number=[1,2,3,4,5,6,7,8,9,10]
number.extend('MyNAme')

# print(len(number) )


# list insert method
# Syntax: list.insert(index, element)
# The insert() method inserts an element to the list at the specified index.
vowel = ['a', 'e', 'i', 'u']


# 'o' is inserted at index 3 (4th position)
# vowel.insert(3, 'o')
# print('List:', vowel+['o'])


# Remove

# list remove method
# Syntax list.remove(element)
number = [1,2,3,4,5,6,7,8,9,10]
# number.remove(5)
# print(number)

# list pop method
# Syntax list.pop(index)
# In this tutorial, we will learn about the Python List pop() method with the help of examples.
prime_numbers = [2, 3, 5, 7]
# print(prime_numbers.pop(0))
# print(prime_numbers)


# Count 

# list count method
# The count() method returns the number of times the specified element appears in the list.
# Syntax list.count(element)
number = [1,2,3,4,5,6,7,8,9,10,1,22,2,2]
# print(number.count(2))


# List index methods 
# Searching for a letter in a list
# The index() method returns the index of the specified element in the list.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
index = alphabet.index('1', 0, len(alphabet))
# index =alphabet.index('k',15,20)
print(index)


# Another

# list reverse method
# Syntax list.reverse()
number=[1,2,3,4,5,6,7,8,9,10]
# number.reverse()
# print(number)

# list short method
# syntax list.sort()
# The sort() method sorts the elements of a given list in a specific ascending or descending order
prime_numbers = [11, 3, 7, 5, 2]
# prime_numbers.sort(reverse=True)
# print(prime_numbers)



#list copying method
# syntax: list1 = list2.copy()
list = ['cat', 0, 6.7]
# new_list = list.copy()
# # Adding an element to the new list
# new_list.append('dog')
# print('Old List:', list)
# print('New List:', new_list)


# list cleared method
# syntax list.clear()
prime_numbers = [2, 3, 5, 7, 9, 11]
# remove all elements
prime_numbers.clear()
# Updated prime_numbers List
# print('List after clear():', prime_numbers)

# Sum of  list 
# number=input('Enter Number:')
# list=number.split()
# sum=0
# for i in list:
#     sum=sum+int(i)
# print(sum)


# numOfWords =0
# numOfLetter=0
# numOfDigits=0

# text = input('Enter Text:')
# for x in text:
#     x=x.lower()
#     if x>='a' and x<='z':
#         numOfLetter+=1
#     elif x>='0' and x<='9':
#         numOfDigits+=1
#     elif x==' ':
#         numOfWords+=1
# print('Number of words:',numOfWords+1)
# print('Number of letters:',numOfLetter)
# print('Number of digits:',numOfDigits)



# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# for i in range(3):
#     for j in range(3):
#         print(matrix[i][j],'\t')
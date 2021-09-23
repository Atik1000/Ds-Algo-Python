# class Stack:

#     def __init__(self):
#         self.stack = []

#     def is_empty(self):
#         return self.stack == []

#     def push(self, data):
#         self.stack.append(data)

#     # def pop(self):
#     #     data = self.stack[-1]
#     #     del self.stack[-1]
#     #     return data

#     def pop(self):
#         return self.stack.pop()

#     def peek(self):
#         return self.stack[-1]

#     def size(self):
#         return len(self.stack)

# s=Stack()
# s.push(10)
# s.push(20)
# s.push([1,2,3,4,5,6,7,8,9,10])
# print(s.size(),'first element')
# print(s.pop(),'remove last')
# print(s.size(),'check size')
# print(s.pop(),'remove last')
# print(s.peek(),'show last')
# print(s.size(),'check size')



class Stack:

    def __init__(self):
        # defining a list which is act as stack container
        self.items = []

    def is_empty(self):
         # checks whether the stack is empty or not
        if self.size() > 0:
            return False
        else:
            return True

    def size(self):
         # returns the size of stack
        return len(self.items)
    
    def push(self,item):
        # push an item to the defined stack
        self.items.append(item)
    
    def pop(self):
        # pop an item to the defined stack
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.items.pop()
    def peek(self):
        # peek an item to the defined stack
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.items[-1]
    
    def display(self):
        # display the stack
        print(self.items)

def main():
    s=Stack()
   
    while True:
        print("1.Push \n2.pop \n3.peek \n4.show \n5.quit")
        case=int(input("\nEnter your choice"))
        
        if case==1:
            print("Enter the element to be pushed")
            element=int(input())
            s.push(element)
            print(f"\n Congo! {element} has been pushed successfully", element)

        elif case==2:
            if s.is_empty():
                print("Stack is empty")
            else:
                element=s.pop()
                print("\nCongo! {element} has been popped successfully", element)

        elif case==3:
            if s.is_empty():
                print("Stack is empty")
            else:
                print("\nCongo! {element} has been peeked successfully", element)

        elif case == 4:
            # in this case, we will print the current condition of our
            # stack
            if s.is_empty():
                print("Sorry, the stack is empty.")
            else:
                print("The current condition of our stack:", s.items)

        elif case == 5:
            # in this case, we will quit our script
            print("The script is gonna quit.")
            quit()

        else:
            print("Oops! Wrong Choice.")
            main()

if __name__ == "__main__":
    main()
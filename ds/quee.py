
class Queue():
    def __init__(self):
        self.items = []

    def size(self):
      return len(self.items)

    def isEmpty(self):
         # checks whether the stack is empty or not
        if self.size() > 0:
            return False
        else:
            return True
        
    def enqueue(self, item):
        return self.items.append(item)
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def sizeQueue(self):
       return len(self.items)


def main():
    q=Queue()
    while True:
        print("1. Enqueue \n2. Dequeue \n3. Show \n4. Peek \n5. Size \n6. Quit")
        print("\nWhat do you wanna do now?")

        choice = int(input())

        if choice == 1:
            print("Enter the item to be enqueued")
            item = input()
            q.enqueue(item)
            print("Item enqueued", item)

        elif choice == 2:
            if q.isEmpty():
                print("Queue is empty")
            else:
                print("Item dequeued", q.dequeue())

        elif choice == 3:
            # in this case, we will print the current condition of our queue
            if q.isEmpty():
                print("Sorry, the queue is empty.")
            else:
                print("The current condition of our queue:",
                      q.items)
        elif choice == 4:
             if q.isEmpty():
                    print("Sorry, the queue is empty.")
             else:
                print("The last element of our queue:",q.peek())

        elif choice == 5:
            if q.isEmpty():
                print('Sorry, the queue is empty')
            else:
                print('Current size of the queue',q.size())
            

        elif choice == 6:
            # in this case, we will quit our script
            print("The script is gonna quit.")
            quit()

        else:
            print("Oops! Wrong Choice.")
            main()

if __name__ == "__main__":
    main()


























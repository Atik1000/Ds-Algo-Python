class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
    # 0(1)
    def insertStart(self, data):
        self.size += 1
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    # 0(1)
    def size(self):
        return self.size
    #  0(N)
    def size2(self):
        actualNode = self.head
        size = 0
        
        while actualNode is not None:
            size += 1
            actualNode = actualNode.next
        return size
    

    def remove(self,data):
        if self.head is None:
            return
        self.size -= 1
        currentNode = self.head
        previousNode = None
        
        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.next
        if previousNode is None:
            self.head = currentNode.next
        else:
            previousNode.next = currentNode.next
        
  
    
    
    def insertEnd(self, data):
        self.size += 1
        newNode = Node(data)
        actualNode = self.head
        
        while actualNode.next is not None:
            actualNode = actualNode.next
        actualNode.next = newNode 
        
    def traverseList(self):
        actualNode = self.head
        while actualNode is not None:
            print("%d" % actualNode.data)
            actualNode = actualNode.next
            
    
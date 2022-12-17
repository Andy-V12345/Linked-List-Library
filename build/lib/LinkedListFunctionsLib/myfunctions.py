class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
    
    def print(self):
        if self.head:
            curr = self.head
            print(curr.data)
            while curr.next:
                curr = curr.next
                print(curr.data)
        else:
            print("The linked list does not have a head yet")

    # returns number of nodes in a linked list
    def count(self):
        if self.head == None:
            raise TypeError("The linked list does not have a head yet")
        counter = 1
        curr = self.head
        while curr.next:
            counter += 1
            curr = curr.next
        return counter

    # returns a node at a specified index
    def access(self, index):
        if self.head == None:
            raise TypeError("The linked list does not have a head yet")
        
        if type(index) != int:
            raise TypeError("Expected an integer in second argument")

        if index < 0:
            raise TypeError("Index cannot be negative")

        lenOfLL = self.count()

        if index >= lenOfLL:
            raise TypeError("Index out of range")
        
        curr = self.head
        for i in range(index+1):
            if i == index:
                return curr
            else:
                curr = curr.next
    
    # replaces a node at a specified index with another node
    def replace(self, index, newNode):
        if not(isinstance(newNode, Node)):
            raise TypeError("Expected type Node in third argument")

        oldNode = self.access(index)
        if index == 0:
            oldNode.data = newNode.data
        else:
            prevNode = self.access(index-1)
            prevNode.next = newNode
            newNode.next = oldNode.next

    # insert a new node at a given index
    def insert(self, index, newNode):
        if not(isinstance(newNode, Node)):
            raise TypeError("Expected type Node in third argument")

        if type(index) != int:
            raise TypeError("Expected an integer in second argument")

        if index < 0:
            raise TypeError("Index cannot be negative")

        lenOfLL = self.count()

        if index > lenOfLL:
            raise TypeError("Index out of range")

        if index == 0:
            newNode.next = self.head
            self.head = newNode
        elif index == lenOfLL:
            lastNode = self.access(index-1)
            lastNode.next = newNode
        else:
            prevNode = self.access(index-1)
            currNode = self.access(index)
            prevNode.next = newNode
            newNode.next = currNode

    # deletes a node at a given index in a linked list
    def delete(self, index):
        if type(index) != int:
            raise TypeError("Expected an integer in second argument")

        if index < 0:
            raise TypeError("Index cannot be negative")

        lenOfLL = self.count()

        if index > lenOfLL:
            raise TypeError("Index out of range")
        
        if index == 0:
            self.head = self.head.next
        elif index == lenOfLL - 1:
            prevNode = self.access(index-1)
            prevNode.next = None
        else:
            prevNode = self.access(index-1)
            nextNode = self.access(index+1)
            prevNode.next = nextNode

    # returns a new sub linked list of a bigger linked list when given an index range
    def subLL(self, startIndex, endIndex):
        if type(startIndex) != int or type(endIndex) != int:
            raise TypeError("Expected an integer in second and third arguments")
        
        if startIndex >= endIndex:
            raise TypeError("Use a valid index range")
        
        if startIndex < 0:
            raise TypeError("Integer in second argument cannot be negative")
        
        lenOfLL = self.count()

        if endIndex >= lenOfLL:
            raise TypeError("Index is out of range")
        
        newLL = LinkedList()
        newLL.add(self.access(startIndex).data)

        for i in range(startIndex+1, endIndex+1):
            curr = self.access(i)
            newLL.add(curr.data)
        
        return newLL

        

# creates a linked list from a list and returns it
def createLL(normList):
    ll = LinkedList()
    if not(type(normList) == list):
        raise TypeError("Expected argument of type list")
    
    for i in range(len(normList)):
        ll.add(normList[i])
    
    return ll


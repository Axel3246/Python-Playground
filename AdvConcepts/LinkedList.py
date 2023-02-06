# Como crear una Linked List (y operaciones)

# Clase Nodo
class Node:
    # constructor
    def __init__(self, data):
        self.data = data # Insert Data
        self.next = None # Declare Next Node (Null if None)

class LinkedList:
    # constructor
    def __init__(self):
        self.head = None 

 # insertion method for the linked list
    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # print method for the linked list
    def printLL(self):
        current = self.head
        while (current):
            print(current.data)
            current = current.next



LL = LinkedList()
LL.insert(10)
LL.insert(11)
LL.printLL()

'''
Linked List with 1 Node

LL = LinkedList()
LL.head = Node(3)
print(LL.head.value)
'''

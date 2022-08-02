class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Creation
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node
        return "DLL Created"

    # Insertion
    def insertNode(self, nodeValue, loc):
        if self.head is None:
            print("Node cant inserted")
        else:
            newNode = Node(nodeValue)
            if loc == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif loc == 1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < loc - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                tempNode.next = newNode
                newNode.next.prev = newNode

    # Traversal
    def traverseDLL(self):
        if self.head is None:
            print('There is no elements to traverse')
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    # Reverse Traversal
    def RevtraverseDLL(self):
        if self.head is None:
            print('There is no elements to traverse')
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    # Searching NOde
    def searchNode(self,nodeValue):
        if self.head is None:
            print('No nodes to search')
        else:
            tempNode=self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode=tempNode.next
            return "Node doesnot exist"
    # Delete a node
    def deleteNode(self,location):
        if self.head is None:
            print('There is not any element')
        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.head.prev=None
            elif location==1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.tail=self.tail.prev
                    self.tail.next=None
            else:
                curNode=self.head
                index=0
                while index< location-1:
                    curNode=curNode.next
                    index+=1
                curNode.next=curNode.next.next
                curNode.next.prev=curNode
            print('Node deleted successfully')

    # Delete entire
    def deleteDLL(self):
        if self.head is None:
            print('No nodes to delete')
        else:
            tempNode=self.head
            while tempNode:
                tempNode.prev=None
                tempNode=tempNode.next
            self.head=None
            self.tail=None
            print("DLL successfully deleted")


DLL = DoublyLL()
DLL.createDLL(7)
# print([node.value for node in DLL])
DLL.insertNode(0, 0)
DLL.insertNode(2, 1)
DLL.insertNode(9, 2)
print([node.value for node in DLL])
# DLL.traverseDLL()
# DLL.RevtraverseDLL()
# print(DLL.searchNode(5))
# DLL.deleteNode(-2)
# print([node.value for node in DLL])
DLL.deleteDLL()
print([node.value for node in DLL])
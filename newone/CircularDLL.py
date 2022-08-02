class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class circularDoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    # Creation'
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        newNode.prev = newNode
        return "CDLL Created success"

    # Insertion
    def insertNode(self, value, loc):
        if self.head is None:
            print("Node cant inserted")
        else:
            newNode = Node(value)
            if loc == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif loc == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index=0
                while index< loc-1:
                    tempNode=tempNode.next
                    index+=1
                newNode.next=tempNode.next
                newNode.prev=tempNode
                newNode.next.prev=newNode
                tempNode.next = newNode
            return "Node Inserted"

    # Traversal
    def traverseCDLL(self):
        if self.head is None:
            print('No nodes to traverse')
        else:
            tempNode=self.head
            while tempNode:
                print(tempNode.value)
                if tempNode==self.tail:
                    break
                tempNode=tempNode.next

    # Reverse traverse
    def reverseTraverseCDLL(self):
        if self.head is None:
            print('No nodes to traverse')
        else:
            tempNode=self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode==self.head:
                    break
                tempNode=tempNode.prev

    # Searching a node
    def searchNode(self,nodeValue):
        if self.head is None:
            print('No nodes')
        else:
            tempNode=self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                if tempNode==self.tail:
                    return "value not found/exist"
                tempNode=tempNode.next


    # Delete a node
    def deleteNode(self,loc):
        if self.head is None:
            print('No nodes to delete')
        else:
            if loc==0:
                if self.head == self.tail:
                    self.head.prev=None
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.head.prev=self.tail
                    self.tail.next=self.head
            elif loc==1:
                if self.head == self.tail:
                    self.head.prev=None
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    self.tail=self.tail.prev
                    self.tail.next=self.head
                    self.head.prev=self.tail
            else:
                tempNode=self.head
                index=0
                while index < loc-1:
                    tempNode=tempNode.next
                    index+=1
                tempNode.next=tempNode.next.next
                tempNode.next.prev=tempNode
            print('Node delete success')

    # Delete Entire CDLL
    def deleteCDLL(self):
        if self.head is None:
            print('No nodes to delete')
        else:
            self.tail.next=None
            tempNode=self.head
            while tempNode:
                tempNode.prev=None
                tempNode=tempNode.next
            self.head=None
            self.tail=None
            print('CDLL Deleted sucessfully')





circularDLL = circularDoublyLL()
print([node.value for node in circularDLL])
print(circularDLL.createCDLL(5))
# print([node.value for node in circularDLL])
circularDLL.insertNode(0,0)
circularDLL.insertNode(1,1)
circularDLL.insertNode(2,2)
print([node.value for node in circularDLL])
# circularDLL.traverseCDLL()
# circularDLL.reverseTraverseCDLL()
# print(circularDLL.searchNode(7))
# circularDLL.deleteNode(-1)
# print([node.value for node in circularDLL])
circularDLL.deleteCDLL()
print([node.value for node in circularDLL])
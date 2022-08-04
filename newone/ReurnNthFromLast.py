# from LinkedList import LinkedList

# def nthToLast(ll,n):
#     pointer1 = ll.head
#     pointer2 = ll.head
#
#     for i in range(n):
#         if pointer2 is None:
#             return None
#         pointer2 = pointer2.next
#     while pointer2:
#         pointer1 = pointer1.next
#         pointer2 = pointer2.next
#     return pointer1
#
# customLL=LinkedList()
# customLL.generate(10,0,99)
# print(customLL)
# print(nthToLast(customLL,3))








# ####    PARTITION QN
#
#
# def partition(ll,x):
#     curNode = ll.head
#     ll.tail = ll.head
#
#     while curNode:
#         nextNode = curNode.next
#         curNode.next = None
#         if curNode.value < x:
#             curNode.next = ll.head
#             ll.head = curNode
#         else:
#             ll.tail.next = curNode
#             ll.tail = curNode
#         curNode = nextNode
#
#     if ll.tail.next is not None:
#         ll.tail.next = None
#
# customLL = LinkedList()
# customLL.generate(10,0,99)
# print(customLL)
# partition(customLL,10)
# print(customLL)








# ####  SUM LINKED LISTS
#
#
# def sumList(llA,llB):
#     n1 = llA.head
#     n2 = llB.head
#     carry = 0
#     ll = LinkedList()
#
#     while n1 or n2 :
#         result = carry
#         if n1:
#             result += n1.value
#             n1 = n1.next
#         if n2:
#             result += n2.value
#             n2 = n2.next
#         ll.add(int(result % 10))
#         carry = result / 10
#
#     return ll
#
# llA = LinkedList()
# llA.add(7)
# llA.add(1)
# llA.add(6)
#
# llB = LinkedList()
# llB.add(5)
# llB.add(9)
# llB.add(2)
#
# print(llA)
# print(llB)
# print(sumList(llA,llB))






#######   INTERSECTION


from LinkedList import LinkedList,Node
def intersection(llA,llB):
    if llA.tail is not llB.tail:
        return False
    lenA = len(llA)
    lenB = len(llB)

    short = llA if lenA < lenB else llB
    long = llA if lenA > lenB else llB

    diff = len(long) - len(short)
    longNode = long.head
    shortNode = short.head

    for i in range(diff):
        longNode = longNode.next
    while shortNode is not longNode:
        shortNode = shortNode.next
        longNode = longNode.next
    return longNode

#### helper func add method
def addSameNode(llA,llB,value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode

llA = LinkedList()
llA.generate(3,0,10)

llB = LinkedList()
llB.generate(4,0,10)

addSameNode(llA,llB,11)
addSameNode(llA,llB,14)

print(llA)
print(llB)

print(intersection(llA,llB))
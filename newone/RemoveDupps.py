from LinkedList import LinkedList


def removedupps(ll):
    if ll.head is None:
        return
    else:
        currNode = ll.head
        vis = set([currNode.value])
        while currNode.next:
            if currNode.next.value in vis:
                currNode.next = currNode.next.next
            else:
                vis.add(currNode.next.value)
                currNode = currNode.next
        return ll


#### Without Temp Buffer
def removedupps11(ll):
    if ll.head is None:
        return

    currNode = ll.head
    while currNode:
        run = currNode
        while run.next:
            if run.next.value == currNode.value:
                run.next=run.next.next
            else:
                run = run.next
        currNode = currNode.next
    return ll

customLL= LinkedList()
customLL.generate(10,0,7)
print(customLL)
removedupps11(customLL)
print(customLL)




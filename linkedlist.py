class Element:
    def __init__(self, value):
        self.val = value
        self.next = None

    def getVal(self):
        return self.val

    def getNext(self):
        return self.next

    def setNext(self, element):
        self.next = element

    def setVal(self, value):
        self.val = value


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def getHead(self):
        return self.head

    def append(self, val):
        element = Element(val)
        curr = self.head
        if self.head:
            while curr.next:
                curr = curr.next
            curr.next = element
        else:
            self.head = element

    def size(self):
        cur = self.head
        size = 0;
        while cur:
            size += 1
            cur = cur.getNext()
        return size

    def delete(self, val):
        cur = self.head
        if cur.getVal() == val:
            self.head = cur.getNext
            del cur
        else:
            while cur.getNext() and cur.getNext().getVal() != val:
                cur = cur.getNext()
            if not cur.getNext():
                return "value not found"
            else:
                cur.next = cur.getNext().getNext()


l = LinkedList()
l.append(1)
l.append(2)
l.append('sajid')

myNode = l.getHead()
while myNode:
    print(myNode.val)
    myNode = myNode.next
print(l.size())

l.delete(2)

myNode = l.getHead()
while myNode:
    print(myNode.val)
    myNode = myNode.next
print(l.size())
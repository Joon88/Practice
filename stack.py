class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.top = None

    def push(self, val):
        newNode = Node(val)
        if self.top:
            cur = self.top
            self.top = newNode
            self.top.next = cur
        else:
            self.top = newNode
            self.head = newNode

    def pop(self):
        cur = self.top
        self.top = self.top.next
        cur.next = None
        return cur.val


s = Stack()
s.push(5)
s.push(6)
s.push(7)
s.push(8)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())




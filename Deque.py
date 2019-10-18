from collections import deque
l = [1,2,3,4,5,6,9]
s = set([1,1,5,8,9,7,6,6])
myQueue = deque(s)
myQueue.append(100)
myQueue.appendleft(200)

print(myQueue.pop())
print(myQueue.popleft())
print(myQueue)
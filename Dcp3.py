class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    if root:
        return str(root.val) + " " + serialize(root.left) + " " + serialize(root.right)
    else:
        return str(-1)


def deserialize(string):

node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))

'''
node = Node('root', Node('left', Node('left.left')), Node('right'))


                root
            /           \
        left            right
        /
    left.left
'''
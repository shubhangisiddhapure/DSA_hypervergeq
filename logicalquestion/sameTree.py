# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
def isIdentical(x, y):

    if x is None and y is None:
        return True
    elif x is not None and y is not None:
        return (x and y) and (x.key == y.key) and isIdentical(x.left, y.left) and isIdentical(x.right, y.right)
 
 
if __name__ == '__main__':
 
    # construct the first tree
    x = Node(15)
    x.left = Node(10)
    x.right = Node(20)
 
    # construct the second tree
    y = Node(15)
    y.left = Node(10)
    y.right = Node(20)

 
    if isIdentical(x, y):
        print("The given binary trees are identical")
    else:
        print("The given binary trees are not identical")

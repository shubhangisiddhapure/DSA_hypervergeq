# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def maxDepth(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    else:
        num = maxDepth(root.left);
        nums = maxDepth(root.right);
        if (num > nums):
            return num+1
        else:
            return nums+1
        

 
 
# Driver program to test above function
root = Node(3)
root.left = Node(20)
root.right = Node(9)
root.left.left=Node(7)
root.left.right=Node(15)

 
 
print ("Height of tree is %d" %(maxDepth(root)))

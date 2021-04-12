class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
  
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

  
def inorder(root):
    if root:
        inorder(root.left)
        print("inorder",root.val)
        inorder(root.right)
        
def get_min(root):
        current = root
        while current.left is not None:
            current = current.left
        return current.val
def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val 
 

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

inorder(r)
print("min value is",get_min(r))
print("max value is",get_max(r))
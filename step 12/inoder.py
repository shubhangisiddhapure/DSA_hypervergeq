class Node:
    def __init__(self, key):
        self.key = key
def inorder(root):
 
    if root is None:
        return
 
    inorder(root.left)
    print(root.key)
    inorder(root.right)

def constructBST(preorder, start, end):
 
    if start > end:
        return None
    node = Node(preorder[start])

    i = start
    while i <= end:
        if preorder[i] > node.key:
            break
        i = i + 1

    node.left = constructBST(preorder, start + 1, i - 1)

    node.right = constructBST(preorder, i, end)
    return node
if __name__ == '__main__':
 
    preorder = [15, 10, 8, 12, 20, 16, 25]
 
    root = constructBST(preorder, 0, len(preorder) - 1)

    inorder(root)
 
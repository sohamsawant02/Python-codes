# Tree traversal in Python


class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


def postorder(root):

    if root:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print(str(root.val) + "->", end='')

def inorder(root):

    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse right
        inorder(root.right)
        
def preorder(root):

    if root:
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)


root = Node("2")
root.left = Node("7")
root.left.left = Node("2")

root.left.right=Node("6")
root.left.right.left=Node("5")
root.left.right.right=Node("11")

root.right = Node("5")
root.right.right = Node("9")
root.right.right.left = Node("4")


print("\nPreorder traversal ")
preorder(root)

print("Inorder traversal ")
inorder(root)

print("\nPostorder traversal ")
postorder(root)

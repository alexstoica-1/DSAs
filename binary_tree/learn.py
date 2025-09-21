from typing import Optional
from utils import (
    inorder,
    preorder,
    postorder, 
    level_order,
    printer
)
from depth import (
    height_rec,
    height_level
)

class Node:
    def __init__(self, d):
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None
        self.data = d

# Works if you run the file directly.
if __name__ == '__main__':
     #      5
    #     / \
    #   12   13
    #   /  \    \
    #  7    14   2
    # /  \   /  \  / \
    #17 23 27  3  8  11

    root = Node(5)
    root.left = Node(12)
    root.right = Node(13)

    root.left.left = Node(7)
    root.left.right = Node(14)

    root.right.right = Node(2)

    root.left.left.left = Node(17)
    root.left.left.right = Node(23)

    root.left.right.left = Node(27)
    root.left.right.right = Node(3)

    root.right.right.left = Node(8)
    root.right.right.right = Node(11)

    preorder(root)
    print()
    inorder(root)
    print()
    postorder(root)
    print()

    # Perform level order traversal and get the result
    res = level_order(root)
    printer(res)

    print(f"\nThe depth of the tree is: {height_level(root)}.")

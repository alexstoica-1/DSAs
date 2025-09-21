def preorder(node):
    if node is None:
        return
    
    print(node.data, end = " ")

    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node is None:
        return
    
    inorder(node.left)

    print(node.data, end = " ")

    inorder(node.right)

def postorder(node):
    if node is None:
        return
    
    postorder(node.left)

    postorder(node.right)

    print(node.data, end = " ")

def level_order(root):
    if root is None:
        return 
    
    q = []
    res = []

    q.append(root)
    level = 0

    while q:
        length = len(q)
        res.append([])

        for _ in range(length):
            node = q.pop(0)
            res[level].append(node.data)

            if node.left is not None:
                q.append(node.left)

            if node.right is not None:
                q.append(node.right)
        
        level +=1
    
    return res


def printer(res):
    for level in res:
        print('[', end='')
        print(', '.join(map(str, level)), end='')
        print('] ', end='')
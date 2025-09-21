def height_rec(root):
    if root is None:
        return -1
    
    left = height_rec(root.left)
    right = height_rec(root.right)

    return max(left, right) + 1

from collections import deque

def height_level(root):
    if root is None:
        return -1
    
    q = deque([root])
    depth = 0

    while q:
        level_size = len(q)

        for _ in range(level_size):
            current = q.popleft()

            if current.left:
                q.append(current.left)
            
            if current.right:
                q.append(current.right)

        depth += 1

    return depth - 1
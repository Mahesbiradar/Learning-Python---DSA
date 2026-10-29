# DAY 80
# Status:
# Time Taken:
# Time Complexity:
# Space Complexity:
# Submitted to LC:
# Result:
# Pattern:
# Variant:
# Mistakes / Confusion:



# Trees:



class TreeNode:

    def __init__(self,value):

        self.val = value
        self.left = None
        self.right = None


root = TreeNode(10)

root.left = TreeNode(5)

root.right = TreeNode(20)

root.left.left = TreeNode(3)

root.left.right = TreeNode(7)

# root.left.right.left = TreeNode(6)

root.right.left = TreeNode(30)




def dfs(root):
    if root is None:
        return

    print("ENTER", root.val)

    dfs(root.left)

    print("BACK LEFT", root.val)

    dfs(root.right)

    print("BACK RIGHT", root.val)




dfs(root)


from collections import deque

def bfs(root):


    queue = deque()

    queue.append(root)


    while queue:


        node = queue.popleft()

        print(node.val)


        if node.left:

            queue.append(node.left)

        if node.right:

            queue.append(node.right)


bfs(root)




def bfs(root):

    if root is None:
        return []

    queue = deque([root])

    result = []
    
    while queue:


        level_size = len(queue)

        level = []

        for _ in range(level_size):
        
            node = queue.popleft()

            level.append(node.val)

            if node.left:

                queue.append(node.left)

            if node.right:

                queue.append(node.right)

        result.append(level)

    return result


print(bfs(root))

  

def maxDepth(root):

    if not root:
        return 0


    left_height = maxDepth(root.left)

    right_height = maxDepth(root.right)


    return 1 + max(left_height,right_height)


print(maxDepth(root))




root1 = TreeNode(10)

root1.right = TreeNode(20)

root1.right.right = TreeNode(30)


print(maxDepth(root1))




# maxDepth(6) = 1

# maxDepth(7) = 2

# maxDepth(3) = 1

# maxDepth(5) = 3

# maxDepth(30) = 1

# maxDepth(20) = 2

# maxDepth(10) = 4


# 1. --- LC --- 104 Maximum Depth of Binary Tree --- Tree DFS --- Depth / height


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:

        if not root:
            return 0

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        return 1 + max(left_height,right_height)


# Status: Independent
# Time Taken: 10m
# Time Complexity: O(n)
# Space Complexity: O(h)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Tree DFS
# Variant: Depth / height
# Mistakes / Confusion: Na



# 🧪 Hands-on #1

# Does a path sum of 22 exist? Yes

# 10 -> 5 -> 7 = 22



def hasPathSum(root, target):

    if root is None:
        return False


    if root.left is None and root.right is None:

        return target == root.val

    remaining = target - root.val

    return (hasPathSum(root.left,remaining) or hasPathSum(root.right,remaining))


print(hasPathSum(root,22))

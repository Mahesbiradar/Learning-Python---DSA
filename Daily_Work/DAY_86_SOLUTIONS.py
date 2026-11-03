


# 1	-	144	-	Binary Tree Preorder Traversal	-	Tier-3



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
         
        result = []

        if not root:
            return result

        stack = []

        stack.append(root)

        while stack:

            node = stack.pop()

            result.append(node.val)

            if node.right:

                stack.append(node.right)

            if node.left:

                stack.append(node.left)
        
        return result


# Status: independent
# Time Taken: 5m
# Time Complexity: O(n) n = number nodes oin tree
# Space Complexity: 0(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Tree Preodres DFS traversal using Stack
# Variant: Tree traversal 
# Mistakes / Confusion:Na

# 2	-	94	-	Binary Tree Inorder Traversal	-	Tier-3

# Using DFS recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        
        result = []

        def dfs(node):

            if not node:
                return 
            
            dfs(node.left)

            result.append(node.val)

            dfs(node.right)

        dfs(root)

        return result


# Status: independent
# Time Taken: 8m
# Time Complexity: O(n) n = number nodes oin tree
# Space Complexity: 0(n) recusrsion stack in worst case
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Tree inorder DFS traversal using recursion
# Variant: Tree traversal 
# Mistakes / Confusion:Na


# Iterative solution 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        
        result = []

        if not root:

            return result

        stack = []

        current = root

        while current or stack:


            while current:

                stack.append(current)

                current = current.left
            
            node = stack.pop()

            result.append(node.val)

            current = node.right
        
        return result



# Status: independent
# Time Taken: 5m
# Time Complexity: O(n) n = number nodes oin tree
# Space Complexity: 0(n) stack space in worst case
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Tree inorder DFS traversal using iterative search
# Variant: Tree traversal 
# Mistakes / Confusion:Na



# 3	-	145	-	Binary Tree Postorder Traversal	-	Tier-3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        
        result = []

        def dfs(node):

            if not node:

                return
            
            dfs(node.left)

            dfs(node.right)

            result.append(node.val)
        
        dfs(root)

        return result
    
# Status: independent
# Time Taken: 5m
# Time Complexity: O(n) n = number nodes oin tree
# Space Complexity: 0(n) recusrsion stack in worst case
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Tree postorder DFS traversal using recursion
# Variant: Tree traversal 
# Mistakes / Confusion:Na


# Iterative search

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        
        result = []

        if not root:

            return result

        stack = []

        stack.append(root)

        while stack:

            node = stack.pop()

            result.append(node.val)

            if node.left:

                stack.append(node.left)
            
            if node.right:

                stack.append(node.right)
        
        result.reverse()

        return result


# Status: independent
# Time Taken: 5m
# Time Complexity: O(n) n = number nodes oin tree
# Space Complexity: 0(n) stack space in worst case
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Tree postorder DFS traversal using iterative search
# Variant: Tree traversal 
# Mistakes / Confusion:Na


# 4	-	105	-	Construct Binary Tree from Preorder and Inorder Traversal	-	Tier-3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        
        root_index = 0

        inorder_dict = {}

        for i in range(len(inorder)):

            inorder_dict[inorder[i]] = i

        def dfs(left,right):

            nonlocal root_index

            if left > right:

                return 
            
            value = preorder[root_index]

            mid = inorder_dict[value]

            node = TreeNode(value)

            root_index += 1

            node.left = dfs(left, mid-1)

            node.right = dfs(mid+1,right)

            return node
        
        return dfs(0,len(inorder)-1)

# Status: independent
# Time Taken: 10m
# Time Complexity: O(n) n = number nodes oin tree
# Space Complexity: 0(n) recursion stack space in worst case
# Submitted to LC:Yes
# Result:Accepted
# Pattern: construction of tree
# Variant: Tree traversal 
# Mistakes / Confusion:Na


"""
6	-	695	-	Max Area of Island	-	Tier-1
7	-	733	-	Flood Fill	-	Tier-1
8	-	547	-	Number of Provinces	-	Tier-1
9	-	1020	-	Number of Enclaves	-	Tier-1
10	-	127	-	Word Ladder	-	Tier-1
11	-	433	-	Minimum Genetic Mutation	-	Tier-1
12	-	994	-	Rotting Oranges	-	Tier-1
13	-	1091	-	Shortest Path in Binary Matrix	-	Tier-1

"""

# 5	-	200	-	Number of Islands	-	Tier-1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # set up
        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        rows = len(grid)

        cols = len(grid[0])

        def dfs(r,c):

            grid[r][c] = "0"

            for dr, dc in directions:

                nr = r + dr

                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":

                    dfs(nr,nc)
        

        # Traversing the islands

        islands = 0

        for r in range(rows):

            for c in range(cols):

                if grid[r][c] == "1":

                    dfs(r, c)

                    islands += 1
        
        return islands


# Status: independent
# Time Taken: 8m
# Time Complexity: O(r * c) ,recusrsion stack O(r * c) visiting each cell and its 4 nebours , outer for lopp (r * c) 
# Space Complexity: O(r * c) recusrsion call stack  
# Submitted to LC:Yes
# Result:Accepted
# Pattern: graph grid traversal
# Variant: Tree traversal 
# Mistakes / Confusion:Na



# 7	-	733	-	Flood Fill	-	Tier-1


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    

        if not image or not image[0]:

            return image
        
        if image[sr][sc] == color:

            return image
        
        base_color = image[sr][sc]

        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        rows = len(image)

        cols = len(image[0])

        def dfs(r,c):

            image[r][c] = color

            for dr,dc in directions:

                nr = r + dr 

                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == base_color:

                    dfs(nr, nc)
        
        dfs(sr,sc)

        return image


# Status: independent
# Time Taken: 8m
# Time Complexity: O(r * c) , recusrsion call visiting all pixes in image in worst case and visiting its 4 nebours 
# Space Complexity: O(r * c) recusrsion call stack  
# Submitted to LC:Yes
# Result:Accepted
# Pattern: graph grid traversal
# Variant: graph traversal 
# Mistakes / Confusion:Na

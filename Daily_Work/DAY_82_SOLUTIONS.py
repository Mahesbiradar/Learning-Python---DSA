# DAY 82
# Status:
# Time Taken:
# Time Complexity:
# Space Complexity:
# Submitted to LC:
# Result:
# Pattern:
# Variant:
# Mistakes / Confusion:

# Tier-2 

"""
1	-	LC	-	410	-	Split Array Largest Sum
2	-	LC	-	203	-	Remove Linked List Elements
3	-	LC	-	82	-	Remove Duplicates from Sorted List II
4	-	LC	-	61	-	Rotate List
5	-	LC	-	86	-	Partition List

"""

# 1	-	LC	-	410	-	Split Array Largest Sum


class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        

        def isfeasible(subarrysum):

            count_of_array = 1

            prefix = 0

            for i in range(len(nums)):

                if prefix + nums[i] <= subarrysum:

                    prefix += nums[i]
                
                else:

                    count_of_array += 1

                    prefix = nums[i]
            
            return count_of_array <= k
        

        
        left = max(nums)

        right = sum(nums)

        while left < right:

            mid = (right+left)//2

            if isfeasible(mid):

                right = mid
            else:

                left = mid + 1
        
        return left 

# Status: Independent
# Time Taken: 8M
# Time Complexity: O(nlog(sum(nums)))
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Binary search
# Variant: Helper + boundry search
# Mistakes / Confusion:Na

# 2	-	LC	-	203	-	Remove Linked List Elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:


        dummynode = ListNode(0)

        current = dummynode

        dummynode.next = head

        while current.next:

            if current.next.val != val:

                current = current.next
            else:
                current.next = current.next.next

        return dummynode.next

# Status: Independent
# Time Taken: 10M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Linked list
# Variant: remove nth Node
# Mistakes / Confusion:Na


# 3	-	LC	-	82	-	Remove Duplicates from Sorted List II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        
        dummynode = ListNode(0)

        dummynode.next = head

        current = dummynode

        while current.next and current.next.next:

            if current.next.val != current.next.next.val:

                current = current.next
            else:

                duplicate = current.next

                while duplicate.next and duplicate.val == duplicate.next.val:
                    
                    duplicate = duplicate.next
                
                current.next = duplicate.next
        
        return dummynode.next


# Status: Independent
# Time Taken: 5M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Linked list
# Variant: remove nth Node
# Mistakes / Confusion:Na


# 4	-	LC	-	61	-	Rotate List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        
        if not head or not head.next or k == 0:
            return head

        n = 0

        current = head

        prev = None

        while current:

            n += 1

            prev = current

            current = current.next

        k = k % n

        if k == 0:
            return head 

        prev.next = head
        
        pos = n - k

        current = head

        while pos > 1:

            pos -= 1

            current = current.next

        new_head = current.next

        current.next = None

        return new_head



# Status: Hint
# Time Taken: 10M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Linked list
# Variant: roate the list
# Mistakes / Confusion:Na


# 5	-	LC	-	86	-	Partition List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        
        dummynode_less = ListNode(0)

        current_less = dummynode_less

        dymmynode_more = ListNode(0)

        current_more = dymmynode_more

        current = head

        while current:

            if current.val < x:

                current_less.next = current

                current_less = current_less.next
            else:

                current_more.next = current

                current_more = current_more.next
            
            current = current.next
        
        current_more.next = None

        current_less.next = dymmynode_more.next

        return dummynode_less.next

# Status: Independent
# Time Taken: 15M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Linked list
# Variant: split the list
# Mistakes / Confusion:Na


class Tree:

    def __init__(self,value):

        self.val = value
        self.left = None
        self.right = None


root = Tree(10)

root.left = Tree(5)

root.left.left = Tree(3)

root.left.right = Tree(7)

root.left.right.right = Tree(6)

root.right = Tree(20)

root.right.right = Tree(30)


def pathSum(root, targetSum):
    result = []
    path = []

    def dfs(node, remaining):

        if not node:
            return

        path.append(node.val)

        remaining -= node.val

        if node.left is None and node.right is None:

            if remaining == 0:

                result.append(path.copy())


        dfs(node.left,remaining)
        dfs(node.right,remaining)

        path.pop()


    dfs(root, targetSum)

    return result


print(pathSum(root, 18))



# 2 --- LC --- 111 --- Minimum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        
        if not root:
            return 0
      
        if root.left is None:

            return 1 + self.minDepth(root.right)
        
        if root.right is None:

            return 1 + self.minDepth(root.left)
        
        return 1 + min(self.minDepth(root.right),self.minDepth(root.left))


# 3 --- LC --- 543 --- Diameter of Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0

        def dfs(node):

            nonlocal diameter

            if not node:
                return 0
            
            left_node = dfs(node.left)
            right_node = dfs(node.right)

            diameter = max(diameter,left_node+right_node)

            return 1 + max(left_node,right_node)
            
        dfs(root)
        
        return diameter
            


# 4 --- LC --- 110 --- Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:

        def dfs(node):
            if node is None:
                return 0
            
            left = dfs(node.left)

            if left == -1:
                return -1
            
            right = dfs(node.right)

            if right == -1:
                return  -1
            
            if abs(left-right) > 1:
                return -1
            
            return 1 + max(left,right)
        
        return dfs(root) != -1



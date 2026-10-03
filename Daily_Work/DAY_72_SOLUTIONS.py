# DAY 72

# Status:
# Time Taken:
# Time Complexity:
# Space Complexity:
# Submitted to LC:
# Result:
# Pattern:
# Variant:
# Mistakes / Confusion:

# New

"""
1	-	LC	-	2	-	Add Two Numbers	-	Traversal + basic ops	-	Reverse a list
2	-	LC	-	83	-	Remove Duplicates from Sorted List	-	Traversal + basic ops	-	Reverse a list
3	-	LC	-	203	-	Remove Linked List Elements	-	Dummy node	-	Remove Nth / merge
4	-	LC	-	82	-	Remove Duplicates from Sorted List II	-	Dummy node	-	Remove Nth / merge

"""

# 2	-	LC	-	83	-	Remove Duplicates from Sorted List	-	Traversal + basic ops	-	Reverse a list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        current = head

        while current and current.next:

            if current.val == current.next.val:

                current.next = current.next.next
            
            else:

                current = current.next
        
        return head
        
# Status: Independent
# Time Taken: 10 m
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result:Aceepted
# Pattern: Linked List
# Variant:traversal + basic ops
# Mistakes / Confusion:Na


# 1	-	LC	-	2	-	Add Two Numbers	-	Traversal + basic ops	-	Reverse a list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummyhead = ListNode(0)

        current = dummyhead

        carry = 0

        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0

            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carry

            digit = sum % 10

            carry = sum // 10

            New_node = ListNode(digit)

            current.next = New_node

            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        
        current.next = None

        return dummyhead.next


# Status: Independent
# Time Taken: 15 m
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC:Yes
# Result:Aceepted
# Pattern: Linked List
# Variant:traversal + basic ops
# Mistakes / Confusion:Na


# 3	-	LC	-	203	-	Remove Linked List Elements	-	Dummy node	-	Remove Nth / merge

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummynode = ListNode(0)

        dummynode.next = head

        current = dummynode

        while current.next:

            if current.next.val == val:

                current.next = current.next.next
            else:

                current = current.next
        
        return dummynode.next

# Status: Independent
# Time Taken: 10 m
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result:Aceepted
# Pattern: Linked List
# Variant:Dummy node + Remove Nth / merge
# Mistakes / Confusion:Na


# 4	-	LC	-	82	-	Remove Duplicates from Sorted List II	-	Dummy node	-	Remove Nth / merge

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
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

# Status: Hint
# Time Taken: 20 m
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result:Aceepted
# Pattern: Linked List
# Variant:Dummy node + Remove Nth / merge
# Mistakes / Confusion:Na




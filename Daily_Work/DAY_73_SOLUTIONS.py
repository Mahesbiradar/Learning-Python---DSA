# DAY 73

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
1	-	LC	-	25	-	Reverse Nodes in k-Group	-	In-place manipulation	-	Reorder / reverse groups
2	-	LC	-	61	-	Rotate List	-	In-place manipulation	-	Reorder / reverse groups
3	-	LC	-	86	-	Partition List	-	In-place manipulation	-	Reorder / reverse groups

"""

# 3	-	LC	-	86	-	Partition List	-	In-place manipulation	-	Reorder / reverse groups


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """

        smalldummy = ListNode(0)
        smallcurrent = smalldummy

        largedummy = ListNode(0)
        largecurrent = largedummy


        current = head

        while current:

            if current.val < x:

                next_node = current.next

                smallcurrent.next = current

                smallcurrent = smallcurrent.next

                current = next_node
            else:

                next_node = current.next

                largecurrent.next = current

                largecurrent = largecurrent.next

                current = next_node
        
        # print(smalldummy)
        # print(smallcurrent)
        # print(largedummy)
        # print(largecurrent)

        largecurrent.next = None

        smallcurrent.next = largedummy.next

        return smalldummy.next

# Status: Independent
# Time Taken: 25M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Linked list
# Variant:Dummy Nodes + Existing Node Re-linking(Two Chains + In-place Reordering)
# Mistakes / Confusion:Na


# 2	-	LC	-	61	-	Rotate List	-	In-place manipulation	-	Reorder / reverse groups

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        if not head or not head.next or k == 0:
            return head
        
        n = 1

        current = head

        while current.next:

            current = current.next

            n += 1
        

        k = k % n

        if k == 0:
            return head
        
        current.next = head

        current = head

        pos = n - k

        while pos > 1:

            current = current.next

            pos -= 1
        
        new_head = current.next

        current.next = None

        return new_head


# Status: Independent
# Time Taken: 35M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Linked list
# Variant:Circular Connection + Reconnection (Find Tail + Make Circular + Find New Tail + Break)
# Mistakes / Confusion:Na

# 1	-	LC	-	25	-	Reverse Nodes in k-Group	-	In-place manipulation	-	Reorder / reverse groups




# DAY 74

# Status:
# Time Taken:
# Time Complexity:
# Space Complexity:
# Submitted to LC:
# Result:
# Pattern:
# Variant:
# Mistakes / Confusion:



# Tier - 1

"""
2	-	LC	-	15	-	3Sum
3	-	LC	-	2	-	Add Two Numbers
4	-	LC	-	83	-	Remove Duplicates from Sorted List
5	-	LC	-	203	-	Remove Linked List Elements
6	-	LC	-	82	-	Remove Duplicates from Sorted List II
7	-	LC	-	61	-	Rotate List
8	-	LC	-	86	-	Partition List

"""

# 2	-	LC	-	15	-	3Sum

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        result = []

        for i in range(len(nums)):

            left = i+1 

            right = len(nums)-1

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            while left < right:

                sum_of_triplates = nums[i] + nums[left]+nums[right]

                if sum_of_triplates > 0:

                    right -= 1

                elif sum_of_triplates < 0:

                    left += 1
                else:

                    result.append([nums[i],nums[left],nums[right]])

                    left += 1

                    right -= 1

                    while left < right and nums[left] == nums[left-1]:

                        left += 1
                    
                    while left < right and nums[right] == nums[right+1]:

                        right -= 1
        
        return result
                    
# Status: Independent
# Time Taken: 10m
# Time Complexity: O(n^2)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Two pointers
# Variant:sorting + three pointers
# Mistakes / Confusion:Na

# 3	-	LC	-	2	-	Add Two Numbers

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
        
        dummynode = ListNode(0)

        current = dummynode

        carry = 0

        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum_of_two = val1 + val2 + carry

            digit = sum_of_two % 10

            carry = sum_of_two // 10

            new_node = ListNode(digit)

            current.next = new_node

            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        current.next = None

        return dummynode.next


# Status: Independent
# Time Taken: 15m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Linked list
# Variant:Dummy node + traversal
# Mistakes / Confusion:Na

# 4	-	LC	-	83	-	Remove Duplicates from Sorted List

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
        if not head or not head.next:
            return head
        
        current = head

        while current.next:

            if current.val == current.next.val:

                current.next = current.next.next
            else:

                current = current.next
        
        return head

    
# Status: Independent
# Time Taken: 6m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Linked list
# Variant: removing duplicates in place rewiring
# Mistakes / Confusion:Na


# 5	-	LC	-	203	-	Remove Linked List Elements

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
# Time Taken: 8m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Linked list
# Variant: Dummy node + Remove Nth / merge
# Mistakes / Confusion:Na

# 6	-	LC	-	82	-	Remove Duplicates from Sorted List II

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

                while duplicate.next and  duplicate.val == duplicate.next.val:

                    duplicate = duplicate.next
                
                current.next = duplicate.next
        
        return dummynode.next

# Status: Independent
# Time Taken: 15m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Linked list
# Variant: Dummy node + Remove Nth / merge
# Mistakes / Confusion:Na

# 7	-	LC	-	61	-	Rotate List

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
        
        n = 0

        current = head

        prv = None

        while current:

            prv = current

            current = current.next

            n += 1
        

        k = k % n

        if k == 0:
            return head

        prv.next = head
        
        pos = n - k

        current = head

        while pos > 1:

            current = current.next

            pos -= 1

        new_head = current.next

        current.next = None

        return new_head


# Status: Independent
# Time Taken: 10m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Linked list
# Variant: Circular Connection + Reconnection (Find Tail + Make Circular + Find New Tail + Break)
# Mistakes / Confusion:Na

# 8	-	LC	-	86	-	Partition List

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
        smallerdummy = ListNode(0)
        small_current = smallerdummy

        largerdummy = ListNode(0)
        larger_current = largerdummy

        current = head

        while current:

            if current.val >= x:

                larger_current.next = current

                larger_current = larger_current.next
            
            else :

                small_current.next = current

                small_current = small_current.next
            
            current = current.next
        

        larger_current.next = None

        small_current.next = largerdummy.next

        return smallerdummy.next

# Status: Independent
# Time Taken: 10m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Linked list
# Variant: Dummy Nodes + Existing Node Re-linking(Two Chains + In-place Reordering)
# Mistakes / Confusion:Na



# Tier - 2

"""
9	-	LC	-	325	-	Maximum Size Subarray Sum Equals k
10	-	LC	-	16	-	3Sum Closest

"""
# 9	-	LC	-	325	-	Maximum Size Subarray Sum Equals k


def maximum_size_subarray_sum_equals_k(nums: list[int], k: int) -> int:

    prefix = 0

    seen = {0:-1}

    max_subarry = float('-inf')

    for i in range(len(nums)):

        prefix += nums[i]

        needed = prefix - k 

        if needed in seen:

            max_subarry = max(max_subarry,i-seen[needed])

        if prefix not in seen:

            seen[prefix] = i
            
    return 0 if max_subarry == float('-inf') else max_subarry

# Status: Independent
# Time Taken: 5m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:prefix sum
# Variant: Hash map
# Mistakes / Confusion:Na

# 10	-	LC	-	16	-	3Sum Closest

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        differance = float('inf')

        closest = None


        for i in range(len(nums)):

            left = i + 1

            right = len(nums)-1


            while left < right:

                total_sum = nums[i]+nums[left]+nums[right]

                diff = abs(total_sum - target)

                if diff == 0:
                    return target
                
                if diff < differance:

                    differance = diff

                    closest = total_sum
                
                if total_sum > target:

                    right -= 1
                else:
                    left += 1
        
        return closest
                
# Status: Independent
# Time Taken: 8m
# Time Complexity: O(n^2)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Two pointers
# Variant: sortiong + two pointers
# Mistakes / Confusion:Na


# New


"""
1 - LC - 918 - Maximum Circular Subarray - Running State - Kadane / min-max tracking
2 - LC - 25 - Reverse Nodes in k-Group - In-place manipulation - Reorder / reverse groups

"""

# 1 - LC - 918 - Maximum Circular Subarray - Running State - Kadane / min-max tracking

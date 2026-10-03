# DAY 77
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

1	-	LC	-	2483	-	Minimum Penalty for a Shop
2	-	LC	-	2845	-	Count of Interesting Subarrays
3	-	LC	-	918	-	Maximum Circular Subarray

"""

# Tier - 2 

"""
4	-	LC	-	1991	-	Find the Middle Index in Array
5	-	LC	-	2270	-	Number of Ways to Split a String
6	-	LC	-	83	-	Remove Duplicates from Sorted List
7	-	LC	-	203	-	Remove Linked List Elements
8	-	LC	-	82	-	Remove Duplicates from Sorted List II
9	-	LC	-	61	-	Rotate List
10	-	LC	-	86	-	Partition List

"""



# 1	-	LC	-	2483	-	Minimum Penalty for a Shop

class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """

        penality = customers.count("Y")

        min_hours = 0

        min_penality = penality


        for i in range(len(customers)):

            if customers[i] == "N":

                penality += 1

            else: 

                penality -= 1
            
            if penality < min_penality:

                min_penality = penality

                min_hours = i + 1
        
        return min_hours

# Status: Independent
# Time Taken: 10M 
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Prefix sum 
# Variant: Pivot / eqibliriam 
# Mistakes / Confusion:Na

# 2	-	LC	-	2845	-	Count of Interesting Subarrays

class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        """
        :type nums: List[int]
        :type modulo: int
        :type k: int
        :rtype: int
        """
        
        intresting =[]

        for i in nums:

            if i % modulo == k:

                intresting.append(1)
            else:
                intresting.append(0)
        

        count = 0

        prefix = 0

        seen = {0:1}

        for i in range(len(intresting)):

            prefix += intresting[i]

            current = prefix % modulo

            needed = (current - k) % modulo

            if needed in seen:

                count += seen[needed]
            
            seen[current] = seen.get(current,0)+1
        
        return count


# Status: Independent
# Time Taken: 15M 
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Prefix sum 
# Variant: Modulo
# Mistakes / Confusion:Na

# 3	-	LC	-	918	-	Maximum Circular Subarray

class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_global = float('-inf')
        max_current = 0

        min_global = float('inf')
        min_current = 0

        current_sum = 0

        for i in range(len(nums)):

            max_current = max(nums[i],nums[i]+max_current)
            max_global = max(max_global,max_current)

            min_current = min(nums[i],nums[i]+min_current)
            min_global = min(min_global,min_current)

            current_sum += nums[i]
        
        circular_sum = current_sum - min_global

        result = max(circular_sum,max_global)

        if max_global < 0:
            return max_global
        
        return result



# Status: Independent
# Time Taken: 10M 
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Prefix sum 
# Variant: Kadanes Max/min
# Mistakes / Confusion:Na



# 4	-	LC	-	1991	-	Find the Middle Index in Array

class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total_sum = sum(nums)

        left = 0

        for i in range(len(nums)):

            right = total_sum - left - nums[i]

            if right == left:

                return i
            
            left += nums[i]
        
        return -1

# Status: Independent
# Time Taken: 5M 
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Prefix sum 
# Variant: Pivot
# Mistakes / Confusion:Na

# 5	-	LC	-	2270	-	Number of Ways to Split a String

class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = nums[0]

        count = 0

        totalsum = sum(nums)

        for i in range(1,len(nums)):

            right = totalsum - left 

            if left >= right:

                count += 1
            
            left += nums[i]
        
        return count

# Status: Independent
# Time Taken: 10M 
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Prefix sum 
# Variant: Pivot 
# Mistakes / Confusion:Na

# 6	-	LC	-	83	-	Remove Duplicates from Sorted List

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
# Time Taken: 8M 
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Linked list
# Variant: Traversal + basic ops
# Mistakes / Confusion:Na



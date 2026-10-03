# DAY 76
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
1	-	LC	-	1413	-	Minimum Value to Get Positive Step by Step Sum
2	-	LC	-	1371	-	Find the Longest Substring Containing Vowels in Even Counts
3	-	LC	-	918	-	Maximum Circular Subarray

"""



# 1	-	LC	-	1413	-	Minimum Value to Get Positive Step by Step Sum

class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        prefix = 0

        min_prefix = float('inf')

        for i in range(len(nums)):

            prefix += nums[i]

            min_prefix = min(min_prefix,prefix)
        
        answer = max(1,1-min_prefix)

        return answer

# Status: Independenr
# Time Taken: 8M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Prefix sum
# Variant: running prefix
# Mistakes / Confusion:Na

# 2	-	LC	-	1371	-	Find the Longest Substring Containing Vowels in Even Counts


class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        vowerl_to_bit = {"a":1,"e":2,"i":4,"o":8,"u":16}

        seen = {0:-1}

        compliment = 0

        max_len = 0

        for char in range(len(s)):

            if s[char] in "aeiou":
                
                compliment ^= vowerl_to_bit[s[char]]

            if compliment in seen:

                max_len = max(max_len,char-seen[compliment])

            else:

                seen[compliment] = char
        
        return max_len


# Status: Independent
# Time Taken: 10M
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Prefix sum
# Variant: Hash map
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

        min_global = float("inf")
        min_current = 0

        current_sum = 0

        for i in nums:

            max_current = max(i,max_current+i)
            max_global = max(max_global,max_current)

            min_current = min(i,min_current+i)
            min_global = min(min_global,min_current)

            current_sum += i
        
        circularsum = (current_sum-min_global)

        result = max(max_global,circularsum)

        if max_global < 0:
            return max_global
        
        return result

# Status: Hint
# Time Taken: 15M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Prefix sum
# Variant: Kadanes Min/max
# Mistakes / Confusion:Na

# Tier - 2

"""

5	-	LC	-	2	-	Add Two Numbers
6	-	LC	-	83	-	Remove Duplicates from Sorted List
7	-	LC	-	203	-	Remove Linked List Elements
8	-	LC	-	82	-	Remove Duplicates from Sorted List II
9	-	LC	-	61	-	Rotate List
10	-	LC	-	86	-	Partition List

"""

# 4	-	LC	-	15	-	3Sum

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        result = []


        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums)-1


            while left < right:

                sum_of_triplates = nums[i] + nums[left] + nums[right]

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
# Time Taken: 10M
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Two pointers
# Variant: sort + two pointers
# Mistakes / Confusion:Na

# 5		LC	-	2	-	Add Two Numbers

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

            New_node = ListNode(digit)

            current.next = New_node

            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        

        current.next = None

        return dummynode.next


# Status: Independent
# Time Taken: 5M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Linked List
# Variant: DummyNode + Traversal + basic ops.
# Mistakes / Confusion:Na
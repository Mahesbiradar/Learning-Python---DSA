# DAY 66

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

1	-	LC	-	680	-	Valid Palindrome II
2	-	LC	-	345	-	Reverse Vowels of a String
3   -   LC  -   42  -   Trapping Rain Water

"""



# 1	-	LC	-	680	-	Valid Palindrome II

class Solution(object):

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def ispalindrome(left,right):

            while left < right:

                if s[left] != s[right]:

                    return False

                left += 1

                right -= 1
            
            return True
        
        left = 0

        right = len(s)-1
        
        while left < right:

            if s[left] == s[right]:

                left += 1

                right -= 1
            else:

                return ispalindrome(left+1,right) or ispalindrome(left,right-1)

        return True


# Status: Hint 
# Time Taken: 25M
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Two pointers
# Variant: One mismatch/one deletion
# Mistakes / Confusion:Na

# 2	-	LC	-	345	-	Reverse Vowels of a String

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0

        right = len(s)-1

        s_list = list(s)

        vowels = set("aeiouAEIOU")

        while left < right:

            while left < right and  s_list[left] not in vowels :

                left += 1

            while left < right and s_list[right] not in vowels:

                right -= 1
            
            s_list[left],s_list[right] = s_list[right],s_list[left] 

            left += 1

            right -= 1
        
        return "".join(s_list)

# Status: independent
# Time Taken: 20M
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Two pointers
# Variant: Two Pointers + Skip Non-target Elements
# Mistakes / Confusion:Na


# 3   -   LC  -   42  -   Trapping Rain Water


# Brute Force:

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        total_water = 0

        for i in range(len(height)):


            left_max = 0

            right_max = 0

            for j in range(i,-1,-1):

                left_max = max(left_max,height[j])
            
            for k in range(i+1,len(height)):

                right_max = max(right_max,height[k])
            
            water = min(left_max,right_max) - height[i]

            if water > 0:

                total_water += water
                
        return total_water

# optimized:

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = [0]*len(height)

        left[0] = height[0]

        for i in range(1,len(height)):

            left[i] = max(left[i-1],height[i])
        

        right = [0]*len(height)

        right[-1] = height[-1]

        for j in range(len(height)-2,-1,-1):

            right[j] = max(right[j+1],height[j])
        

        total_water = 0

        for k in range(len(height)):

            water = min(left[k],right[k]) - height[k]

            if water > 0:

                total_water += water
        
        return total_water

# Optimal solution:

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        total_water = 0

        left_max = 0
        right_max = 0

        left = 0
        right = len(height)-1

        while left <= right:

            if left_max <= right_max:

                left_max = max(left_max,height[left])

                total_water += left_max - height[left]

                left += 1

            else:

                right_max = max(right_max,height[right])

                total_water += right_max - height[right]

                right -= 1
        
        return total_water


# Status: hint
# Time Taken: 45M
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Two pointers
# Variant: Two Pointers + Running Left/Right Maximum
# Mistakes / Confusion:Na


# Tier - 2

"""
1	-	1590	-	Make Sum Divisible by P
2	-	143	-	Reorder List
3	-	328	-	Odd Even Linked List
4	-	24	-	Swap Nodes in Pairs

"""

# 1	-	1590	-	Make Sum Divisible by P

class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """

        totalsum = sum(nums)

        target = totalsum % p

        if target == 0:
            return 0
        
        len_sub = len(nums)

        seen = {0:-1}

        prefix = 0

        for i in range(len(nums)):

            prefix += nums[i]

            current = prefix % p

            needed = (current-target) % p

            if needed in seen:

                len_sub = min(len_sub,i-seen[needed])
            
            seen[current] = i
        
        return -1 if len_sub == len(nums) else len_sub

# Status: independent
# Time Taken: 8M
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: prefix sum
# Variant: modulo
# Mistakes / Confusion:Na

# 2	-	143	-	Reorder List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return head
        
        slow = head

        fast = head

        while fast.next and fast.next.next:

            slow = slow.next

            fast = fast.next.next

        
        current = slow.next

        slow.next = None

        prev = None 

        while current:

            next_node = current.next

            current.next = prev

            prev = current

            current = next_node
        
        first = head

        second = prev

        while first and second:

            first_next = first.next

            second_next = second.next

            first.next = second

            second.next = first_next

            first = first_next

            second = second_next
        
        return head

# Status: independent
# Time Taken: 15M
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Linked list
# Variant: fast & slow + reversal + rewiring
# Mistakes / Confusion:Na

# 3	-	328	-	Odd Even Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head or not head.next:
            return head

        even_head = head.next

        odd = head

        even = head.next

        while even and even.next:

            odd_next = even.next

            even_next = odd_next.next

            odd.next = odd_next

            even.next = even_next

            odd = odd.next

            even = even.next
        
        odd.next = even_head

        return head

# Status: independent
# Time Taken: 10M
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Linked list
# Variant: Nodes rewiring
# Mistakes / Confusion:Na

# 4	-	24	-	Swap Nodes in Pairs

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)

        current = dummy

        dummy.next = head

        while current.next and current.next.next:

            first = current.next

            second = first.next

            first.next = second.next

            second.next = first

            current.next = second

            current = first

        return dummy.next

# Status: independent
# Time Taken: 5M
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Linked list
# Variant: Nodes rewiring
# Mistakes / Confusion:Na


# Tier - 1

"""
1	-	239	-	Sliding Window Maximum
2	-	1438	-	Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
3	-	862	-	Shortest Subarray with Sum at Least K
4	-	1696	-	Jump Game VI

"""

# 1	-	239	-	Sliding Window Maximum

from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dq = deque()

        result = []

        left = 0

        for right in range(len(nums)):

            left = right - k + 1

            while dq and dq[0] < left:

                dq.popleft()
            
            while dq and nums[right] >= nums[dq[-1]]:

                dq.pop()
            
            dq.append(right)

            if right >= k-1:

                result.append(nums[dq[0]])
        
        return result

# Status: independent
# Time Taken: 10M
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: sliding window
# Variant: Monotonic deque
# Mistakes / Confusion:Na

# 2	-	1438	-	Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit


from collections import deque
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """

        max_dq = deque()

        min_dq = deque()

        max_len = 0

        left = 0

        for i in range(len(nums)):

            while max_dq and nums[i] > nums[max_dq[-1]]:

                max_dq.pop()
            
            max_dq.append(i)

            while min_dq and nums[i] < nums[min_dq[-1]]:

                min_dq.pop()
            
            min_dq.append(i)

            while nums[max_dq[0]] - nums[min_dq[0]] > limit:

                if min_dq[0] == left:

                    min_dq.popleft()
                
                if max_dq[0] == left:

                    max_dq.popleft()
                
                left += 1
            
            max_len = max(max_len,i-left+1)
        
        return max_len

# Status: independent
# Time Taken: 15M
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: sliding window
# Variant: variable size + Monotonic deque
# Mistakes / Confusion:Na

# 3	-	862	-	Shortest Subarray with Sum at Least K

from collections import deque
class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = [0]

        for i in range(len(nums)):

            prefix.append(prefix[i]+nums[i])

        
        dq = deque()

        min_len = float('inf')

        for j in range(len(prefix)):

            while dq and prefix[j] <= prefix[dq[-1]]:

                dq.pop()
            
            dq.append(j)

            while dq and prefix[j] - prefix[dq[0]] >= k:

                min_len = min (min_len,j-dq[0])

                dq.popleft()
            
        return -1 if min_len == float('inf') else min_len


# Status: hint
# Time Taken: 10M
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: sliding window
# Variant: variable size + Monotonic deque
# Mistakes / Confusion:Na

# 4	-	1696	-	Jump Game VI

from collections import deque
class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        dp = [0]*len(nums)

        dp[0] = nums[0]

        dq = deque([0])


        for i in range(1,len(nums)):

            while dq and dq[0] < i-k:

                dq.popleft()
            
            dp[i] = nums[i] + dp[dq[0]]

            while dq and dp[dq[-1]] < dp[i]:

                dq.pop()
            
            dq.append(i)
        
        return dp[-1]


# Status: hint
# Time Taken: 15M
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: DP
# Variant:Monotonic deque
# Mistakes / Confusion:Na


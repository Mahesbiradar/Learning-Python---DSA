### Tier 4

# 1. LC 53 — Maximum Subarray

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        prefix = 0

        max_subarry = float('-inf')


        for i in range(len(nums)):

            prefix = max(nums[i],prefix + nums[i])

            max_subarry = max(max_subarry,prefix)
        
        return max_subarry

# Status: Independent
# Time Taken: 10m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Running state
# Variant:Prefix sum
# Mistakes / Confusion:Na

# 2. LC 724 — Find Pivot Index

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        totalsum = sum(nums)

        for i in range(len(nums)):

            right = totalsum - left - nums[i]

            if left == right:
                return i
            
            left += nums[i]
        
        return -1

# Status: Independent
# Time Taken: 5m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:prefix sum
# Variant:pivot index
# Mistakes / Confusion:Na

### Tier 1

# 1. LC 2262 — Total Appeal of A String

class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0

        for i in range(len(s)):

            seen = set()

            for j in range(i,len(s)):

                seen.add(s[j])

                answer += len(seen)
                
        return answer

# Status: Independent
# Time Taken: 10m
# Time Complexity: O(n^2)
# Space Complexity:O(n)
# Submitted to LC:Na
# Result:NA
# Pattern:Brute Force(Nested Loop)
# Variant:
# Mistakes / Confusion:Na


# Optimal Solution:

class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0
        last = {}

        for i in range(len(s)):

            previous = last.get(s[i],-1)

            left = i - previous
            right = len(s) - i

            contribution = left * right

            answer += contribution

            last [s[i]] = i

        return answer

# Status: hint
# Time Taken: 30m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Contribution Technique
# Variant:Previous Occurrence + Counting
# Mistakes / Confusion:Na

# 2. LC 862 — Shortest Subarray with Sum at Least K

#Brute Force

class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        subarray = float('inf')

        for i in range(len(nums)):

            prefix = 0

            for j in range(i,len(nums)):

                prefix += nums[j]

                if prefix >= k:
                    subarray = min (subarray,j-i+1)
        return subarray if subarray != float('inf') else -1


# Status: independent
# Time Taken: 5m
# Time Complexity: O(n^2)
# Space Complexity:O(1)
# Submitted to LC:Na
# Result:Na
# Pattern:Brute Force
# Variant:Nested Loop.
# Mistakes / Confusion:Na

# Optimal solution:


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

        answer = float('inf')

        for i in range(len(prefix)):

            while dq and prefix[i] - prefix[dq[0]] >= k:

                answer = min(answer,i-dq[0])

                dq.popleft()
            
            while dq and prefix[i]<=prefix[dq[-1]]:

                dq.pop()
            
            dq.append(i)

        return answer if answer != float('inf') else -1


# Status: Hint
# Time Taken: 30m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Sliding window
# Variant:Deque
# Mistakes / Confusion:Na



### Tier 2

# 1. LC 84 — Largest Rectangle in Histogram

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Find the right Boundry
        stack = []
        right = [len(heights)]*len(heights)

        for i in range(len(heights)):

            while stack and heights[i] <= heights[stack[-1]]:

                right[stack[-1]] = i

                stack.pop()
            
            stack.append(i)
        
        # Find teh left boundry

        stack = []
        left = [-1]*len(heights)

        for j in range(len(heights)-1,-1,-1):

            while stack and heights[j] < heights[stack[-1]]:

                left[stack[-1]] = j

                stack.pop()
            
            stack.append(j)
        
        #Calculate the area and largest rctangle histogram.

        largest = 0

        for k in range(len(heights)):

            width = (right[k]-left[k])-1

            area = heights[k]*width
            
            largest = max(largest,area)
        
        return largest

# Status: independent
# Time Taken: 15m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Monotonic stack
# Variant:Boundary-based width calculation
# Mistakes / Confusion:Na

# 2. LC 85 — Maximal Rectangle

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Find the right Boundry
        stack = []
        right = [len(heights)]*len(heights)

        for i in range(len(heights)):

            while stack and heights[i] <= heights[stack[-1]]:

                right[stack[-1]] = i

                stack.pop()
            
            stack.append(i)
        
        # Find teh left boundry

        stack = []
        left = [-1]*len(heights)

        for j in range(len(heights)-1,-1,-1):

            while stack and heights[j] < heights[stack[-1]]:

                left[stack[-1]] = j

                stack.pop()
            
            stack.append(j)
        
        #Calculate the area and largest rctangle histogram.

        largest = 0

        for k in range(len(heights)):

            width = (right[k]-left[k])-1

            area = heights[k]*width
            
            largest = max(largest,area)
        
        return largest
        
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        height = [0]*len(matrix[0])
        
        max_rectangle = 0

        for rows in matrix:


            for row in range(len(rows)):

                if rows[row] == "0":
                    height[row] = 0
                else:
                    height[row] += 1
            

            rectacngle = self.largestRectangleArea(height)

            max_rectangle = max(max_rectangle,rectacngle)
        
        return max_rectangle


# Status: independent
# Time Taken: 20m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Monotonic stack 
# Variant:Histogram + Monotonic Stack
# Mistakes / Confusion:Na

# 3. LC 239 — Sliding Window Maximum

from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dq = deque()

        answer = []


        for i in range(len(nums)):

            left = i - k + 1

            while dq and left > dq[0]:
                dq.popleft()
            
            while dq and nums[i] >= nums[dq[-1]]:

                dq.pop()

            dq.append(i)
            
            if left >= 0:
                answer.append(nums[dq[0]])
            
            
        return answer


# Status: independent
# Time Taken: 10m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: Deque
# Variant:Monotonmic deque
# Mistakes / Confusion:Na


# 4. LC 1438 — Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit


from collections import deque
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """

        maxdeque = deque()
        mindeque = deque()

        answer = 0

        left = 0

        for right in range(len(nums)):

            while maxdeque and nums[right] >= nums[maxdeque[-1]]:

                maxdeque.pop()
            
            maxdeque.append(right)

            while mindeque and nums[right] <= nums[mindeque[-1]]:

                mindeque.pop()

            mindeque.append(right)


            while nums[maxdeque[0]]-nums[mindeque[0]] > limit:


                if maxdeque[0] == left:

                    maxdeque.popleft()
                
                if mindeque[0] == left:

                    mindeque.popleft()
                
                left +=1
                
            answer = max(answer,right-left+1)


        return answer


# Status: hint
# Time Taken: 15m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: Deque
# Variant:Monotonmic deque
# Mistakes / Confusion:Na


### Tier 3

# 1. LC 20 — Valid Parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seen = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        stack =[]

        for i in s:

            if i in seen:

                if not stack: 
                    return False
                elif seen[i] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        
        return False if stack else True



# Status: independent
# Time Taken: 10m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: stack
# Variant:Basic ops
# Mistakes / Confusion:Na

# 2. LC 206 — Reverse Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        prev = None
        current = head

        while current:

            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev


# Status: independent
# Time Taken: 5m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: Linked List
# Variant:reversal
# Mistakes / Confusion:Na

# 3. LC 11 — Container With Most Water

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0

        right = len(height)-1

        max_water = 0

        while left < right:

            water = min(height[left],height[right])*(right-left)

            if height[right] > height[left] :
                left += 1
            else:
                right -= 1

            max_water = max(max_water,water)

        return max_water


# Status: independent
# Time Taken: 5m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: Two poinetrs
# Variant: Maximum/minimum
# Mistakes / Confusion:Na



## New Problems added manually:

# 1.LC 283 Move Zeroes

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        write = 0

        for i in range(len(nums)):

            if nums[i] != 0:
                nums[write] = nums[i]
                write += 1
        
        for j in range(write,len(nums)):

            nums[j] = 0



# Status: independent
# Time Taken: 5m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: Two poinetrs
# Variant: WRITE POINTER
# Mistakes / Confusion:Na

# 2. LC 80. Remove Duplicates from Sorted Array II


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        write = 0

        for i in range(len(nums)):

            if write < 2:
                write += 1
            else:
                if nums[i] != nums[write-2]:
                    nums[write] = nums[i]
                    write += 1
        
        return write


# Status: independent
# Time Taken: 10m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: Two poinetrs
# Variant: WRITE POINTER
# Mistakes / Confusion:Na



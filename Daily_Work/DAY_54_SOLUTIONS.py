### Tier 3 Revisions (Due Aug 4 — fill to target workload)

# 6. **LC 875 — Koko Eating Bananas**

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def isfeasible(speed):

            count = 0

            for i in piles:

                divisor = i // speed
                remainder = 0 if i % speed == 0 else 1
                count += divisor + remainder
            
            return False if count > h else True
        
        left = 1
        right = max(piles)

        while left < right:

            mid = (right+left)//2

            if isfeasible(mid):
                right = mid  
            else:
                left = mid + 1
        return left

# Status:independent
# Time Taken: 15m
# Time Complexity:O(n*log(piles))
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Binary search
# Variant:Boundry Search
# Mistakes / Confusion:Na

# 7. **LC 852 — Peak Index in Mountain Array**

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left = 0
        right = len(arr)-1

        while left < right:

            mid = (right+left)//2

            if arr[mid]>arr[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left

# Status:independent
# Time Taken: 3m
# Time Complexity:O(logn)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Binary search
# Variant:boundry search
# Mistakes / Confusion:Na

# 8. **LC 11 — Container With Most Water**

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

            area = (min(height[left],height[right]))*(right-left)

            max_water = max(max_water,area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_water

# Status:independent
# Time Taken: 8m
# Time Complexity:O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Two pointers
# Variant:opposite ends
# Mistakes / Confusion:Na

# 9. **LC 974 — Subarray Sums Divisible by K**

class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = {0:1}

        prefix = 0

        count = 0

        for i in range(len(nums)):

            prefix += nums[i]

            needed = prefix % k

            if needed in seen:
                count += seen[needed]
            
            seen[needed] = seen.get(needed,0)+1
        
        return count

# Status:independent
# Time Taken: 6m
# Time Complexity:O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Prefix sum
# Variant:Modulo
# Mistakes / Confusion:Na

# 10. **LC 1590 — Make Sum Divisible by P**
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
        
        n = len(nums)

        best = n

        prefix = 0

        seen = {0:-1}

        for i in range(len(nums)):

            prefix += nums[i]
            
            current = prefix % p

            needed = (current-target) % p

            if needed in seen:
                best = min(best,i-seen[needed])
            
            seen[current] = i

        if best == len(nums):
            return -1
        else:
            return best

# 11. **LC 141 — Linked List Cycle**

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
                
        return False

# Status:independent
# Time Taken:5m
# Time Complexity:O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Linked list
# Variant:Slow and fast pointers
# Mistakes / Confusion:Na

# 12. **LC 1047 — Remove All Adjacent Duplicates In String**


class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for i in s:

            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        
        return "".join(stack)

# Status:independent
# Time Taken: 10
# Time Complexity:O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Stack
# Variant:basic stack operation
# Mistakes / Confusion:Na

### Tier 1 (Mandatory — all due today)

# 1. **LC 84 — Largest Rectangle in Histogram**

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        nse = [len(heights)]*len(heights)

        stack = []

        for i in range(len(heights)):

            while stack and heights[i] <= heights[stack[-1]]:
                
                nse[stack[-1]] = i

                stack.pop()
            
            stack.append(i)
        
        stack = []

        pse = [-1]*len(heights)

        for j in range(len(heights)-1,-1,-1):

            while stack and heights[j] < heights[stack[-1]]:

                pse[stack[-1]] = j

                stack.pop()
            
            stack.append(j)
        
        largest_histogram = 0
        
        for k in range(len(heights)):

            width = nse[k]-pse[k]-1
            area =  heights[k]*width

            largest_histogram = max(largest_histogram,area)
        
        return largest_histogram

# Status:independent
# Time Taken: 20m
# Time Complexity:O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Stack
# Variant:Monotonic stack
# Mistakes / Confusion:Na


# 2. **LC 85 — Maximal Rectangle**

class Solution(object):
    
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        nse = [len(heights)]*len(heights)

        stack=[]

        for i in range(len(heights)):

            while stack and heights[i] <=  heights[stack[-1]]:

                nse[stack[-1]] = i
                stack.pop()
            
            stack.append(i)
        
        pse = [-1]*len(heights)

        stack = []

        for j in range(len(heights)):

            while stack and heights[stack[-1]] >= heights[j] :

                # pse[stack[-1]] = j

                stack.pop()
            if stack:
                pse[j] = stack[-1]
                
            stack.append(j)

        output = 0

        for k in range(len(heights)):

            width = nse[k]-pse[k]-1
          
            area = width * heights[k]
            
            output = max(output,area)
        return output

    def maximalRectangle(self, matrix):
            """
            :type matrix: List[List[str]]
            :rtype: int
            """
            if not matrix:
                return 0
            
            max_rectangle = 0
            heights = [0]*len(matrix[0])

            for raws in matrix:

                for raw in range(len(raws)):

                    if raws[raw] == "0":
                        heights[raw] = 0
                    else:
                        heights[raw] += 1
                
                area = self.largestRectangleArea(heights)

                max_rectangle = max(max_rectangle,area)

            return max_rectangle

# Status:independent
# Time Taken: 25
# Time Complexity:O(n*m) n=rows m=columns
# Space Complexity: O(m)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Stack
# Variant:Monotonis stack
# Mistakes / Confusion:Na

# 3. **LC 239 — Sliding Window Maximum**

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

            left = i-k+1

            if dq and left > dq[0]:
                dq.popleft()
            
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            
            dq.append(i)

            if left >= 0 :
                answer.append(nums[dq[0]])
        
        return answer

# Status:independent
# Time Taken: 30
# Time Complexity:O(n)
# Space Complexity: O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:queues
# Variant:deque
# Mistakes / Confusion:Na

### New Problems (Deque / Sliding Window Max — current variant)

# 4. **LC 1438 — Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit**

#Brute Force

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        answer = 0

        for i in range(len(nums)):

            maximum = float('-inf')
            minimum = float('inf')

            for j in range(i,len(nums)):

                maximum = max(maximum,nums[j])
                minimum = min(minimum,nums[j])

                if maximum-minimum <= limit:
                    answer = max(answer,j-i+1)
        
        return answer

# Status:independent
# Time Taken: 15
# Time Complexity:O(n^2)
# Space Complexity: O(1)
# Submitted to LC: No
# Result:Na
# Pattern:Brute Force
# Variant:Nested Loop
# Mistakes / Confusion:Na

#Optimal solution:

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

            while nums[maxdeque[0]] - nums[mindeque[0]] > limit:

                if maxdeque[0] == left:
                    maxdeque.popleft()
                
                if mindeque[0] == left:
                    mindeque.popleft()
                
                left += 1
            
            answer = max(answer,right-left+1)
        
        return answer

# Status:Hint
# Time Taken: 20
# Time Complexity:O(n)
# Space Complexity: O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Sliding Window
# Variant:Variable Sliding Window + Two Monotonic Deques
# Mistakes / Confusion:Na




# DAY 68

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

1	-	15	-	3Sum	-	Two Pointers	-	Maximize/minimize between ends
2	-	16	-	3Sum Closest	-	Two Pointers	-	Maximize/minimize between ends

"""


# New 

# 1	-	15	-	3Sum	-	Two Pointers	-	Sort + Fixed Pointer + Two-Pointer Pair Sum


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []

        for i in range(len(nums)):

            for j in range(i+1,len(nums)):

                for k in range(j+1,len(nums)):

                    if nums[i] + nums[j] + nums[k] == 0:

                        result.append([nums[i],nums[j],nums[k]])
        
        return result


# optimal

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

            right = len(nums) - 1


            while left < right:


                sum_of_tripalates = nums[i] + nums[left] + nums[right]

                if sum_of_tripalates > 0:

                    right -= 1
                
                elif sum_of_tripalates < 0:

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
            
# Status: Hint 
# Time Taken:50m
# Time Complexity: O(n^2)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: Two poinetrs
# Variant: sort + Fixed Pointer + two pointers
# Mistakes / Confusion:Na

# 2	-	16	-	3Sum Closest	-	Two Pointers	-	Maximize/minimize between ends

# Brute Force:

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        closest = None

        diffrence = float('inf')


        for i in range(len(nums)):


            for j in range(i+1,len(nums)):


                for k in range(j+1,len(nums)):

                    current_sum = nums[i] + nums[j] + nums[k]

                    diff = abs(current_sum-target)

                    if diff < diffrence:

                        diffrence = diff

                        closest = current_sum
            
        return closest


# Optimal:

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        closest = None

        distance = float('inf')

        for i in range(len(nums)):

            left = i + 1

            right = len(nums)-1


            while left < right:

                current_sum = nums[i] + nums[left] + nums[right]

                current_distance =  abs(current_sum-target)

                if current_distance == 0:

                    closest = current_sum

                    return closest

                elif current_distance < distance:

                    closest = current_sum

                    distance = current_distance
                
                
                if current_sum > target:

                    right -= 1
                else :

                    left += 1
        
        return closest

                
# Status: Independent 
# Time Taken:40m
# Time Complexity: O(n^2)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: Two poinetrs
# Variant: sort + Fixed Pointer + two pointers closest
# Mistakes / Confusion:Na


# Tier - 1

"""
1	-	862	-	Shortest Subarray with Sum at Least K
2	-	1696	-	Jump Game VI
3	-	680	-	Valid Palindrome II
4	-	42	-	Trapping Rain Water

"""

# 1	-	862	-	Shortest Subarray with Sum at Least K

# Brute force:

class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        min_len = float('inf')

        for i in range(len(nums)):

            prefix = 0

            for j in range(i,len(nums)):

                prefix += nums[j]

                if prefix >= k:

                    min_len = min(min_len,j-i+1)

                    break

        return -1 if min_len == float('inf') else min_len


# Optimal:

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

            while dq and prefix[i] <= prefix[dq[-1]]:

                dq.pop()
            
            dq.append(i)

            while dq and prefix[i] - prefix[dq[0]] >= k:

                answer = min(answer,i-dq[0])

                dq.popleft()
            
        
        return -1 if answer == float('inf') else answer


# Status: Independent 
# Time Taken:10m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: Sliding window
# Variant: prefix sum + monotonic deque
# Mistakes / Confusion:Na

# 2	-	1696	-	Jump Game VI


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
             
            while dq and dp[i] >= dp[dq[-1]]:

                dq.pop()

            dq.append(i)
        
        return dp[-1]


# Status: hint
# Time Taken:20m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: Sliding window
# Variant: DP + monotonic deque
# Mistakes / Confusion:Na


# 3	-	680	-	Valid Palindrome II

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def ispalindrom(left,right):

            while left < right:

                if s[left] != s[right]:
                    return False
                else:
                    left += 1
                    right -=1
            
            return True
            
        left = 0

        right = len(s)-1

        while left < right:

            if s[left] == s[right]:

                left += 1
                right -= 1
            
            else:
                
                return ispalindrom(left+1,right) or ispalindrom(left,right-1)

        return True

# Status: indpendent
# Time Taken:10m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: Two pointers
# Variant: Opposite ends — palindrome/reverse
# Mistakes / Confusion:Na


# 4	-	42	-	Trapping Rain Water

# Brute Force:


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        nums = height    
        total_water = 0

        for i in range(len(nums)):

            left_max = 0

            right_max = 0

            for j in range(0,i+1):

                left_max = max(left_max,nums[j])
            
            for k in range(len(nums)-1,i,-1):

                right_max = max(right_max,nums[k])
            

            water = min(left_max,right_max) - nums[i]

            if water > 0:

                total_water += water
        
        
        return total_water


# Independent

# Optimized:

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 3:
            return 0
            
        nums = height

        left = [0]*len(nums)

        left[0] = nums[0]

        right = [0]*len(nums)

        right[-1] = nums[-1]


        for i in range(1,len(nums)):

            left[i] = max(nums[i],left[i-1])
        
        
        for j in range(len(nums)-2,-1,-1):

            right[j] = max(nums[j],right[j+1])


        total_water = 0

        for k in range(len(nums)):

            water = min(left[k],right[k]) - nums[k]

            total_water += water
        
        return total_water

# Independent

# Optimal:


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left_max = 0

        right_max = 0

        left = 0

        right = len(height)-1

        total_water = 0


        while left <= right:

            if  left_max <= right_max:

                left_max = max(left_max,height[left])

                water = left_max - height[left]

                total_water += water

                left += 1

            else:

                right_max = max(right_max,height[right])

                water =  right_max - height[right]

                total_water += water

                right -= 1
                
        return total_water

# Status: indpendent
# Time Taken:15m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: Two pointers
# Variant: Opposite ends —  left_max/right_max
# Mistakes / Confusion:Na


# Tier - 2


"""
1	-	2262	-	Total Appeal of A String

"""

class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        seen = {}

        total_appel = 0

        for i in range(len(s)):

            prev = seen.get(s[i],-1)

            left = i - prev

            right = len(s) - i

            contribution = left * right

            total_appel += contribution

            seen[s[i]] = i
        
        return total_appel

# Status: indpendent
# Time Taken:3m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: string traversal
# Variant: contribution technnique
# Mistakes / Confusion:Na


# Tier - 3

"""
1	-	560	-	Subarray Sum Equals K
2	-	525	-	Contiguous Array
3	-	80	-	Remove Duplicates from Sorted Array II

"""

# 1	-	560	-	Subarray Sum Equals K

class Solution(object):
    def subarraySum(self, nums, k):
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

            needed = prefix - k

            if needed in seen:

                count += seen[needed]
            
            seen[prefix] = seen.get(prefix,0)+1
        
        return count


# Status: indpendent
# Time Taken:5m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: prefix
# Variant: hash map
# Mistakes / Confusion:Na


# 2	-	525	-	Contiguous Array

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        seen = {0:-1}

        prefix = 0

        max_len = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1
            
            if prefix in seen:
                max_len = max(max_len,i-seen[prefix])
            else:

                seen[prefix] = i
        
        return max_len

# Status: indpendent
# Time Taken:7m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: prefix
# Variant: hash map
# Mistakes / Confusion:Na

# 3	-	80	-	Remove Duplicates from Sorted Array II

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        write = 2

        for i in range(write,len(nums)):

            if nums[i] != nums[write-2]:

                nums[write] = nums[i]

                write += 1
        
        return write

# Status: indpendent
# Time Taken:3m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: Two pointers
# Variant: Write pointer
# Mistakes / Confusion:Na



# Tier - 4

"""
1	-	3	-	Longest Substring Without Repeating
2	-	209	-	Minimum Size Subarray Sum

"""

# 1	-	3	-	Longest Substring Without Repeating

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen =set()

        left = 0

        max_len = 0

        for i in range(len(s)):

            while s[i] in seen:

                seen.remove(s[left])

                left += 1
            
            seen.add(s[i])

            max_len = max(max_len,i-left+1)
        
        return max_len


# Status: indpendent
# Time Taken:4m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: sliding window
# Variant: variable size
# Mistakes / Confusion:Na


# 2	-	209	-	Minimum Size Subarray Sum

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        prefix = 0

        min_len = float('inf')

        left = 0

        for i in range(len(nums)):

            prefix += nums[i]

            while prefix >= target:

                min_len = min(min_len,i-left+1)

                prefix -= nums[left]

                left += 1
        
        return 0 if min_len == float('inf') else min_len

# Status: indpendent
# Time Taken:5m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: sliding window
# Variant: variable size
# Mistakes / Confusion:Na



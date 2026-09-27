# DAY 71

# Status:
# Time Taken:
# Time Complexity:
# Space Complexity:
# Submitted to LC:
# Result:
# Pattern:
# Variant:
# Mistakes / Confusion:

# Tier-1

"""

1	-	LC	-	325	-	Maximum Size Subarray Sum Equals k
2	-	LC	-	15	-	3Sum
3	-	LC	-	16	-	3Sum Closest

"""


# 1	-	LC	-	325	-	Maximum Size Subarray Sum Equals k


def maximum_size_subarray_sum_equals_k(nums: list[int], k: int) -> int:

    prefix = 0

    seen = {0:-1}

    max_subarray_len = float('-inf')


    for i in range(len(nums)):

        prefix += nums[i]

        needed = prefix - k

        if needed in seen:

            max_subarray_len = max(max_subarray_len,i-seen[needed])


        if prefix not in seen:

            seen[prefix] = i

    return 0 if max_subarray_len == float('-inf') else max_subarray_len


# Status: Indpendent
# Time Taken: 10m
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC:No 
# Result:NA
# Pattern:Prefix sum
# Variant:Hash map
# Mistakes / Confusion:Na


# 2	-	LC	-	15	-	3Sum

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        result = []


        for i in range(len(nums)-2):

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

                        right -=1
        
        return result



# Status: Hint
# Time Taken: 15m
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Two pointers
# Variant:sorting + maximize and minimize b/w ends
# Mistakes / Confusion:Na

# 3	-	LC	-	16	-	3Sum Closest

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        
        closest = None

        difference = float('inf')

        for i in range(len(nums)):


            left = i + 1

            right = len(nums)-1


            while left < right:

                sum_of_triplates = nums[i] + nums[left] + nums[right]

                diff = abs(sum_of_triplates-target)

                if diff == 0:
                    return sum_of_triplates
                
                if diff < difference:

                    difference = diff

                    closest = sum_of_triplates
                
                if sum_of_triplates > target:

                    right -= 1
                else:
                    left += 1
        
        return closest

# Status: Indpendent
# Time Taken: 10m
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Two pointers
# Variant:sorting + maximize and minimize b/w ends
# Mistakes / Confusion:Na



# Tier - 2

"""
4	-	LC	-	862	-	Shortest Subarray with Sum at Least K
5	-	LC	-	1696	-	Jump Game VI
6	-	LC	-	1636	-	Find Smallest Integer Missing from Array
7	-	LC	-	1099	-	Two Sum Less Than K
8	-	LC	-	680	-	Valid Palindrome II
9	-	LC	-	42	-	Trapping Rain Water
10	-	LC	-	1343	-	Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
11	-	LC	-	1052	-	Grumpy Bookstore Owner
12	-	LC	-	2379	-	Minimum Recolors to Get K Consecutive Black Blocks

"""

# 4	-	LC	-	862	-	Shortest Subarray with Sum at Least K

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

            prefix.append(nums[i]+prefix[i])
        
        dq = deque()

        min_len = float('inf')

        for i in range(len(prefix)):

            while dq and prefix[i] <= prefix[dq[-1]]:

                dq.pop()
            
            dq.append(i)

            while dq and prefix[i] - prefix[dq[0]] >= k:

                min_len = min(min_len,i-dq[0])

                dq.popleft()
        
        return -1 if min_len == float('inf') else  min_len


# Status: Indpendent
# Time Taken: 15m
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:sliding winodow 
# Variant: Prefix + monotonic deque
# Mistakes / Confusion:Na


# 5	-	LC	-	1696	-	Jump Game VI

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

            left = i - k

            while dq and dq[0] < left:

                dq.popleft()
            
            dp[i] = nums[i] + dp[dq[0]]

            while dq and dp[dq[-1]] <= dp[i]:

                dq.pop()
            
            dq.append(i)
        
        return dp[-1]

# Status: Indpendent
# Time Taken: 10m
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:sliding winodow 
# Variant: Prefix + monotonic deque(decreasing)
# Mistakes / Confusion:Na


# 6	-	LC	-	1636	-	Find Smallest Integer Missing from Array

class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        seen = {}

        for i in nums:

            seen[i] = seen.get(i,0)+1

        sorted_seen = sorted(seen.items(),key=lambda x: (x[1],-x[0]))


        result = []

        for key,freq in sorted_seen:

            for i in range(freq):

                result.append(key)
        
        return result

# Status: Indpendent
# Time Taken: 5m
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Freqeuncy hashing 
# Variant: sorting.
# Mistakes / Confusion:Na

# 7	-	LC	-	1099	-	Two Sum Less Than K

def two_sum_less_than_k(nums: list[int], k: int) -> int:

    nums.sort()
    
    left = 0

    right = len(nums)-1

    max_sum_less_than_k = float('-inf')

    while left < right:

        sum_of_two = nums[left] + nums[right]

        if sum_of_two < k:

            max_sum_less_than_k = max(max_sum_less_than_k,sum_of_two)

            left += 1

        else:

            right -= 1

    return -1 if max_sum_less_than_k == float('-inf') else max_sum_less_than_k


# Status: Indpendent
# Time Taken: 6m
# Time Complexity: O(n log n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Two pointers
# Variant: sorting + minimize and maximize
# Mistakes / Confusion:Na

# 8	-	LC	-	680	-	Valid Palindrome II

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def ispalindorme(left,right):

            while left < right:

                if s[left] != s[right]:

                    return False           
                else :

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

                return ispalindorme(left+1,right) or ispalindorme(left,right-1)
        
        return True


# Status: Indpendent
# Time Taken: 10m
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Two pointers
# Variant: palindorme 2
# Mistakes / Confusion:Na

# 9	-	LC	-	42	-	Trapping Rain Water

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        nums = height

        left = 0

        right = len(nums)-1

        left_max = 0

        right_max = 0

        total_water = 0

        while left <= right:

            if left_max <= right_max:
                
                left_max = max(left_max,nums[left])

                water = left_max - nums[left]

                total_water += water

                left += 1
            else:
                
                right_max = max(right_max,nums[right])

                water = right_max - nums[right]

                total_water += water

                right -= 1
        
        return total_water


# Status: Indpendent
# Time Taken: 15m
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Two pointers
# Variant: minimize/maximize
# Mistakes / Confusion:Na

# 10	-	LC	-	1343	-	Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold


class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        
        prefix = 0

        left = 0

        max_subarrays = 0

        for right in range(len(arr)):

            prefix += arr[right]

            while right - left + 1 > k:

                prefix -= arr[left]

                left += 1

            if right-left+1 > k-1:

                if prefix / k >= threshold:

                    max_subarrays += 1
        
        return max_subarrays



# Status: Indpendent
# Time Taken: 10m
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:sliding window
# Variant: fixed size
# Mistakes / Confusion:Na

# 11	-	LC	-	1052	-	Grumpy Bookstore Owner

class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """

        happy_customners = 0

        for i in range(len(customers)):

            if grumpy[i] == 0:

                happy_customners += customers[i]
        
        max_customers = 0

        left = 0

        cutomers = 0

        for right in range(len(customers)):

            if grumpy[right] == 1:

                cutomers += customers[right]
            
            while right - left + 1 > minutes:

                if grumpy[left] == 1:

                    cutomers -= customers[left]

                left += 1
            
            if right-left+1 >= minutes:

                max_customers = max(max_customers,cutomers)
            
        
        return happy_customners + max_customers


# Status: Indpendent
# Time Taken: 8m
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:sliding window
# Variant: fixed size
# Mistakes / Confusion:Na

# 12	-	LC	-	2379	-	Minimum Recolors to Get K Consecutive Black Blocks

class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        
        left = 0

        black = 0

        min_recolors = float('inf')

        for right in range(len(blocks)):

            if blocks[right] == "B":

                black += 1
            
            while right -left +1 > k:

                if blocks[left] == "B":

                    black -= 1

                left += 1

            if right-left+1 == k:

                if (right-left+1) - black == 0:

                    return 0
                else:

                    min_recolors = min(min_recolors,(right-left+1)-black)
        
        return min_recolors

# Status: Indpendent
# Time Taken: 10m
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:sliding window
# Variant: fixed size
# Mistakes / Confusion:Na


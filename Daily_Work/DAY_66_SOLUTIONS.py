
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

# Tier-1 

"""

1	-	LC	-	2262	-	Total Appeal of A String
2	-	LC	-	239	-	Sliding Window Maximum
3	-	LC	-	1438	-	Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
4	-	LC	-	862	-	Shortest Subarray with Sum at Least K
5	-	LC	-	1696	-	Jump Game VI

"""

# Tier-4

"""

6	-	LC	-	11	-	Container With Most Water
7	-	LC	-	643	-	Maximum Average Subarray I
8	-	LC	-	567	-	Permutation in String
9	-	LC	-	219	-	Contains Duplicate II

"""

# New 

"""

10	-	LC	-	680	-	Valid Palindrome II
11	-	LC	-	345	-	Reverse Vowels of a String

"""

# Solutions


# 2	-	LC	-	239	-	Sliding Window Maximum


# Brute Force:

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        result = []

        n = len(nums)

        for i in range(n-k+1):

            max_num = float('-inf')

            for j in range(i,i+k):

                max_num = max(nums[j],max_num)


            result.append(max_num)
        
        return result

# Optimal:

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

        for i in range(len(nums)):

            left = i-k+1

            while dq and dq[0] < left:

                dq.popleft()
            
            while dq and nums[i] >= nums[dq[-1]]:

                dq.pop()

            dq.append(i)

            if i >= k-1:

                result.append(nums[dq[0]])

        return  result

# Status: Hint
# Time Taken: 40m
# Time Complexity:O(n)
# Space Complexity:0(k)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Sliding window
# Variant:Monotonic Deque / Monotonic Queue
# Mistakes / Confusion:Na


# 3	-	LC	-	1438	-	Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

# Brute Force:

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        max_len = 0


        for i in range(len(nums)):

            min_num = nums[i]

            max_num = nums[i]

            for j in range(i,len(nums)):

                min_num = min(min_num,nums[j])

                max_num = max(max_num,nums[j])

                if max_num - min_num <= limit:

                    max_len = max(max_len,j-i+1)
        return max_len

# Optimal:

from collections import deque
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        
        left = 0

        mindq = deque()

        maxdq = deque()

        max_len = 0

        for right in range(len(nums)):

            while maxdq and nums[right] >= nums[maxdq[-1]]:

                maxdq.pop()
            
            maxdq.append(right)

            while mindq and nums[right] <= nums[mindq[-1]]:

                mindq.pop()

            mindq.append(right)

            while (nums[maxdq[0]] - nums[mindq[0]]) > limit:

                if maxdq[0] == left:

                    maxdq.popleft()
                
                if mindq[0] == left:

                    mindq.popleft()
                
                left += 1
            
            max_len = max(max_len,right-left+1)

        return max_len


# Status: Hint
# Time Taken: 30m
# Time Complexity:O(n)
# Space Complexity:0(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Sliding window
# Variant:Variable-size Sliding Window + Two Monotonic Deques
# Mistakes / Confusion:Na



# 4	-	LC	-	862	-	Shortest Subarray with Sum at Least K


from collections import deque
class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        prefix =[0]

        for i in range(len(nums)):

            prefix.append(prefix[i]+nums[i])

        min_len = float('inf')

        dq = deque()

        for i in range(len(prefix)):

            while dq and prefix[i] - prefix[dq[0]] >= k:

                min_len = min(min_len,i-dq[0])

                dq.popleft()

            while dq and prefix[i] <= prefix[dq[-1]]:

                dq.pop()
            
            dq.append(i)
            
           
        
        return -1 if min_len == float('inf') else min_len


# Status: Hint
# Time Taken: 40m
# Time Complexity:O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Prefix sum
# Variant:Monotonic Deques
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

            while dq and dq[0] < i-k:

                dq.popleft()

            dp[i] = nums[i] + dp[dq[0]]

            while dq and dp[dq[-1]] <= dp[i]:

                dq.pop()

            dq.append(i)

        return dp[-1]


# Status: Hint
# Time Taken: 40m
# Time Complexity:O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:DP
# Variant:Monotonic Deques
# Mistakes / Confusion:Na

# 1	-	LC	-	2262	-	Total Appeal of A String

# Brute Force:

class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        total_appeal = 0


        for i in range(len(s)):

            seen = set()

            for j in range(i,len(s)):

                seen.add(s[j])

                total_appeal += len(seen)
        
        return total_appeal


# Optimal:

class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_occurace = {}

        total_appel = 0

        n = len(s)

        for i in range(len(s)):

            prev = last_occurace.get(s[i],-1)

            left = i - prev

            right = n - i

            contribution = left * right

            total_appel += contribution
       
            last_occurace[s[i]] = i
    
        return total_appel

# Status: Independent
# Time Taken: 10m
# Time Complexity:O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:CONTRIBUTION TECHNIQUE
# Variant:Previous Occurrence / Last Seen Contribution
# Mistakes / Confusion:Na



# Tier-4

"""

6	-	LC	-	11	-	Container With Most Water
7	-	LC	-	643	-	Maximum Average Subarray I
8	-	LC	-	567	-	Permutation in String
9	-	LC	-	219	-	Contains Duplicate II

"""

# 6	-	LC	-	11	-	Container With Most Water

# Brute Force:

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        
        max_water = 0

        for i in range(n):

            for j in range(i,n):

                water = min(height[i],height[j])*(j-i)

                max_water = max(max_water,water)
        

        return max_water
    
# Optimal:


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

            max_water = max(max_water,water)

            if height[left] <= height[right]:

                left +=1

            else:
                
                right -= 1
        
        return max_water


# Status: Independent
# Time Taken: 5m
# Time Complexity:O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Two pointers
# Variant: Maximize/minimize 
# Mistakes / Confusion:Na


# 7	-	LC	-	643	-	Maximum Average Subarray I


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        prefix = 0

        left = 0

        max_sum = float('-inf')

        for right in range(len(nums)):

            prefix += nums[right]

            while right-left+1 > k:

                prefix -= nums[left]

                left += 1
            
            if right-left+1 >= k:

                max_sum = max(max_sum,prefix)
        
        return max_sum/float(k)

# Status: Independent
# Time Taken: 4m
# Time Complexity:O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:sliding window
# Variant: fixed size
# Mistakes / Confusion:Na

# 8	-	LC	-	567	-	Permutation in String

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        freq_s1 = {}

        for i in s1:

            freq_s1[i] = freq_s1.get(i,0)+1
        
        freq_s2 = {}

        left = 0

        for j in range(len(s2)):

            freq_s2[s2[j]] = freq_s2.get(s2[j],0)+1

            while j-left+1 > len(s1):

                freq_s2[s2[left]] -= 1

                if freq_s2[s2[left]] == 0:

                    del freq_s2[s2[left]]

                left += 1

            if freq_s2 == freq_s1:

                return True 
                
        return False

# Status: Independent
# Time Taken: 5m
# Time Complexity:O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:sliding window
# Variant: fixed size
# Mistakes / Confusion:Na


# 9	-	LC	-	219	-	Contains Duplicate II


def containsNearbyDuplicate(nums,k):

    seen = set()

    left = 0

    for i in range(len(nums)):

        if nums[i] in seen:

            return True

        seen.add(nums[i])

        while i-left+1 > k:

            seen.remove(nums[left])

            left += 1

    return False

print(containsNearbyDuplicate([1, 2, 3, 1],3))
print(containsNearbyDuplicate([1, 0, 1, 1],1))
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3],2))
print(containsNearbyDuplicate(nums = [1, 2, 3, 4, 5], k = 3))
print(containsNearbyDuplicate(nums = [1, 2, 3, 4, 1], k = 3))
print(containsNearbyDuplicate(nums = [1, 2, 1], k = 5))

# Status: Independent
# Time Taken: 6m
# Time Complexity:O(n)
# Space Complexity:O(k)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:sliding window
# Variant: fixed size
# Mistakes / Confusion:Na



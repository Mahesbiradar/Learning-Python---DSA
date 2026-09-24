# DAY 69

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

1	-	LC	-	1343	-	Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold	-	Sliding Window	-	Fixed size
2	-	LC	-	1052	-	Grumpy Bookstore Owner	-	Sliding Window	-	Fixed size
3	-	LC	-	2379	-	Minimum Recolors to Get K Consecutive Black Blocks	-	Sliding Window	-	Fixed size

"""

# 3	-	LC	-	2379	-	Minimum Recolors to Get K Consecutive Black Blocks	-	Sliding Window	-	Fixed size

class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        left = 0

        min_ops  = float('inf')

        white = 0
        
        for right in range(len(blocks)):

            if blocks[right] == "W":
                white += 1
            
            while right - left + 1 > k:

                if blocks[left] == "W":
                    white -= 1
                left += 1
            
            if right - left + 1 == k:

                min_ops  = min(min_ops ,white)
        
        return min_ops 

# Status: Indpendent
# Time Taken: 10 m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern:Sliding window 
# Variant:Fixed size
# Mistakes / Confusion:Na


# 1	-	LC	-	1343	-	Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold	-	Sliding Window	-	Fixed size


class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        left = 0

        window_sum  = 0

        number_of_subarrays = 0

        for right in range(len(arr)):

            window_sum  += arr[right]

            while right-left+1 > k:

                window_sum  -= arr[left]

                left += 1
            
            if right-left+1 == k:

                if window_sum >= k * threshold:
                    number_of_subarrays += 1
        
        return number_of_subarrays

# Status: Indpendent
# Time Taken: 5m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern:Sliding window 
# Variant:Fixed size
# Mistakes / Confusion:Na

# 2	-	LC	-	1052	-	Grumpy Bookstore Owner	-	Sliding Window	-	Fixed size

class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """

        base = 0

        for i in range(len(grumpy)):

            if grumpy[i] == 0:
                base += customers[i]
        
        recovered = 0

        max_recovered = 0

        left = 0

        for right in range(len(grumpy)):

            if grumpy[right] == 1:

                recovered += customers[right]
            
            while right -left + 1 > minutes :

                if grumpy[left] == 1:

                    recovered -= customers[left]
                
                left += 1
            
            if right -left + 1 == minutes :

                max_recovered = max(max_recovered,recovered)

        return base + max_recovered


# Status: Indpendent
# Time Taken: 20m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern:Sliding window 
# Variant:Fixed size
# Mistakes / Confusion:Na

# Tier - 1

"""
1	-	LC	-	1696	-	Jump Game VI
2	-	LC	-	15	-	3Sum

"""

# 1	-	LC	-	1696	-	Jump Game VI

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


# Status: Indpendent
# Time Taken: 20m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern:Sliding window 
# Variant:Monotonic deque.
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

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:

                continue

            left = i+1

            right = len(nums)-1

            while left < right:

                sum_triplates = nums[i] + nums [left] + nums[right]

                if sum_triplates > 0:

                    right -= 1
                elif sum_triplates < 0:
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

# Status: hint
# Time Taken: 15m
# Time Complexity: O(n^2)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: Two pointers 
# Variant:Sorting + Maximize/minimize between ends
# Mistakes / Confusion:Na

# Tier - 2

"""
3	-	LC	-	1002	-	Find Common Characters
4	-	LC	-	239	-	Sliding Window Maximum
5	-	LC	-	1438	-	Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
6	-	LC	-	345	-	Reverse Vowels of a String
7	-	LC	-	16	-	3Sum Closest

"""
# 3	-	LC	-	1002	-	Find Common Characters

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []

        common = {}

        for i in words[0]:

            common[i] = common.get(i,0)+1
        

        for word in range(1,len(words)):

            word_freq = {}

            for j in words[word]:

                word_freq[j] = word_freq.get(j,0)+1
            
            for char,freq in common.items():

                if char in word_freq:

                    common[char] = min(common[char],word_freq[char])

                else:

                    del common[char]
        
        answer = []

        for char,freq in common.items():

            for i in range(freq):
                answer.append(char)
        
        return answer

# Status: independent
# Time Taken: 10m
# Time Complexity: O(n*l) number of words in list and max len of word
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: Frequency hashing
# Variant: Count+query
# Mistakes / Confusion:Na


# 4	-	LC	-	239	-	Sliding Window Maximum

# Brute Force:

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        result = []

        for i in range(len(nums)-k+1):
            
            max_num = nums[i]

            for j in range(i+k):

                max_num = max(max_num,nums[j])
            
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

            left = i - k + 1

            while dq and dq[0] < left:

                dq.popleft()  

            while dq and nums[i] >= nums[dq[-1]]:

                dq.pop()      
            
            dq.append(i)

            if i-k+1 >= 0:

                result.append(nums[dq[0]])

        return result

# Status: independent
# Time Taken: 20m
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: sliding window
# Variant: Monotonic Deque
# Mistakes / Confusion:Na


# 5	-	LC	-	1438	-	Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

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

        max_subarray = 0

        left = 0

        for i in range(len(nums)):

            while max_dq and nums[i] >= nums[max_dq[-1]]:

                max_dq.pop()

            max_dq.append(i)

            while min_dq and nums[i] <= nums[min_dq[-1]]:

                min_dq.pop()
            
            min_dq.append(i)

            while nums[max_dq[0]] - nums[min_dq[0]] > limit:

                if max_dq[0] == left:

                    max_dq.popleft()
                
                if min_dq[0] == left:

                    min_dq.popleft()
                
                left += 1
            
            max_subarray = max(max_subarray,i-left+1)
        
        return max_subarray

# Status: independent
# Time Taken: 10m
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: sliding window
# Variant: Monotonic Deque
# Mistakes / Confusion:Na


# 6	-	LC	-	345	-	Reverse Vowels of a String

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_list = []

        for i in s:
            char_list.append(i)

        left = 0

        right = len(char_list)-1

        vowels = set("aeiouAEIOU")

        while left < right:

            while left < right and char_list[left] not in vowels:

                left += 1
            
            while left < right and char_list[right] not in vowels:

                right -= 1
            
            char_list[left], char_list[right] = char_list[right], char_list[left]

            left += 1
            right -= 1

        return "".join(char_list)



# Status: independent
# Time Taken: 5m
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: Two pointers
# Variant: palindorm reversal
# Mistakes / Confusion:Na

# 7	-	LC	-	16	-	3Sum Closest

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        
        closest_sum = None

        diff_min = float('inf')

        for i in range(len(nums)):


            left = i + 1

            right = len(nums)-1

            while left < right:

                current_sum = nums[i] + nums[left] + nums[right]

                diff = abs(current_sum-target)

                if diff == 0:

                    closest_sum = current_sum

                    return closest_sum

                elif diff < diff_min:

                    diff_min = diff

                    closest_sum = current_sum
                
                if current_sum > target:
                    
                    right -= 1
                else:
                    left += 1

        
        return closest_sum


# Status: Hint
# Time Taken: 15m
# Time Complexity: O(n^2) 
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: Two pointers
# Variant: 3 sum closest
# Mistakes / Confusion:Na


# Tier - 3

"""
8	-	LC	-	152	-	Maximum Product Subarray
9	-	LC	-	33	-	Search in Rotated Sorted Array

"""
# 8	-	LC	-	152	-	Maximum Product Subarray

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_product = nums[0]

        current_max = nums[0]

        current_min = nums[0]


        for i in range(1,len(nums)):

            temp_min = min(nums[i],nums[i]*current_min,nums[i]*current_max)

            temp_max = max(nums[i],nums[i]*current_min,nums[i]*current_max)

            current_max = temp_max

            current_min = temp_min

            max_product = max(max_product,current_max)

        return max_product

# Status: indpendent
# Time Taken: 15m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: running state 
# Variant:kadanes algo
# Mistakes / Confusion:Na

# 9	-	LC	-	33	-	Search in Rotated Sorted Array

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left = 0

        right = len(nums)-1

        while left <= right:

            mid = (right+left)//2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > nums[right]:

                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else:

                if nums[mid] <= target <= nums[right]:

                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1

# Status: indpendent
# Time Taken: 10m
# Time Complexity: O(log n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: Binary search
# Variant:Applied target search
# Mistakes / Confusion:Na



# Tier - 4

"""
10	-	LC	-	904	-	Fruits Into Baskets
11	-	LC	-	744	-	Find Smallest Letter Greater
12	-	LC	-	875	-	Koko Eating Bananas

"""

# 10	-	LC	-	904	-	Fruits Into Baskets

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left = 0

        max_fruits = 0

        nums = fruits
        
        fruits = {}

        for i in range(len(nums)):

            fruits[nums[i]] = fruits.get(nums[i],0)+1

            while len(fruits) > 2:

                fruits[nums[left]] -= 1

                if fruits[nums[left]] == 0:
                    del fruits[nums[left]]
                
                left += 1
            
            max_fruits = max(max_fruits,i-left+1)
        
        return max_fruits



# Status: indpendent
# Time Taken: 5m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: sliding window
# Variant:fixed size
# Mistakes / Confusion:Na


# 11	-	LC	-	744	-	Find Smallest Letter Greater


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        left = 0

        right = len(letters)-1

        result = None

        while left <= right:

            mid = (right+left)//2

            if letters[mid] > target:
                result = letters[mid]
                right = mid - 1
            else:
                left = mid + 1
        
        return letters[0] if not result else result

# Status: indpendent
# Time Taken: 5m
# Time Complexity: O(logn)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: Binary search
# Variant: Applied Boundry search
# Mistakes / Confusion:Na


# 12	-	LC	-	875	-	Koko Eating Bananas

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

                remainder = 1 if i % speed != 0 else 0

                divisor = i // speed

                count += divisor + remainder
            
            return True if count <= h else False
        
        left = 1
        right = max(piles)

        while left < right:

            mid = (right+left)//2

            if isfeasible(mid):

                right = mid
            else:
                left = mid + 1
        
        return left 

# Status: indpendent
# Time Taken: 10m
# Time Complexity: O(n log(max(piles)))
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Aceepted
# Pattern: Binary search
# Variant: Applied Boundry search
# Mistakes / Confusion:Na
## Schedule


# 1	-	LC	-	11	-	Container With Most Water

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = height
        left = 0
        right = len(n)-1
        max_water = 0

        while left < right:

            area = min(n[left],n[right])* (right-left)


            if n[left] <= n[right]:
                left += 1
            else:
                right -= 1
            
            max_water = max(max_water,area)

        return max_water

# Status: independent
# Time Taken: 5M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:Two pointers
# Variant: Min/Max
# Mistakes / Confusion:Na

# 2	-	LC	-	643	-	Maximum Average Subarray I

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        prefix = 0

        max_sum  = float('-inf')

        left = 0

        for i in range(len(nums)):

            prefix += nums[i]

            while i-left+1 > k:

                prefix -= nums[left]
                left += 1
            
            if i-left+1 == k:
                max_sum = max(max_sum,prefix)
        
        return max_sum/float(k)

# Status: independent
# Time Taken: 5M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:sliding window
# Variant: fixed size
# Mistakes / Confusion:Na

# 3	-	LC	-	567	-	Permutation in String


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
        
        left = 0

        freq_s2 = {}

        for i in range(len(s2)):

            freq_s2[s2[i]] = freq_s2.get(s2[i],0)+1

            while i-left+1 > len(s1):

                freq_s2[s2[left]] -= 1

                if freq_s2[s2[left]] == 0:
                    del freq_s2[s2[left]]
                
                left += 1
            
            if freq_s1 == freq_s2:
                return True
        
        return False

# Status: independent
# Time Taken: 5M
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:sliding window
# Variant: fixed size
# Mistakes / Confusion:Na


# 4	-	LC	-	438	-	Find All Anagrams

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        freq_p ={}

        for i in p:
            freq_p[i] = freq_p.get(i,0)+1
        
        left = 0

        answer = []

        freq_s = {}

        for i in range(len(s)):

            freq_s[s[i]] = freq_s.get(s[i],0)+1


            while i-left+1 > len(p):
                freq_s[s[left]] -=1 

                if freq_s[s[left]] == 0:
                    del freq_s[s[left]]
                left += 1
            
            if freq_p == freq_s:

                answer.append(left)
        
        return answer


# Status: independent
# Time Taken: 10 M
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:sliding window
# Variant: fixed size
# Mistakes / Confusion:Na

# 5	-	LC	-	219	-	Contains Duplicate II

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = set()

        left = 0

        for i in range(len(nums)):

            if nums[i] in seen:
                return True
            
            seen.add(nums[i])

            if i-left+1 > k:

                seen.remove(nums[left])

                left += 1
        
        return False


# Status: independent
# Time Taken: 15 M
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:sliding window
# Variant: fixed size
# Mistakes / Confusion:Na

# 6	-	LC	-	1456	-	Maximum Number of Vowels

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0

        max_vowels = 0

        count = 0

        for i in range(len(s)):

            if s[i] in ["a","e","i","o","u"]:
                count += 1
            
            while i-left+1 > k:

                if s[left] in ["a","e","i","o","u"]:
                    count -=1 
                left += 1
            
            if i-left+1 == k:
                max_vowels = max(max_vowels,count)
        
        return max_vowels

# Status: independent
# Time Taken: 6 M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:sliding window
# Variant: fixed size
# Mistakes / Confusion:Na

# 7	-	LC	-	3	-	Longest Substring Without Repeating

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()

        left = 0

        max_substring = 0

        for i in range(len(s)):

            while s[i] in seen:

                seen.remove(s[left])

                left += 1
            
            seen.add(s[i])

            max_substring = max(max_substring,i-left+1)
        
        return max_substring

# Status: independent
# Time Taken: 6 M
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:sliding window
# Variant: variable size
# Mistakes / Confusion:Na

# 8	-	LC	-	209	-	Minimum Size Subarray Sum


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        min_size = float('inf')

        left = 0

        prefix = 0

        for i in range(len(nums)):

            prefix += nums[i]

            while prefix >= target:

                min_size = min(min_size,i-left+1)

                prefix -= nums[left]

                left += 1
            
        return 0 if min_size == float('inf') else min_size

# Status: independent
# Time Taken: 10 M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:sliding window
# Variant: variable size
# Mistakes / Confusion:Na

# 9	-	LC	-	904	-	Fruits Into Baskets

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        seen = {}

        max_fruits = 0

        left = 0

        for i in range(len(fruits)):
            
            seen[fruits[i]] = seen.get(fruits[i],0)+1


            while len(seen) > 2:

                seen[fruits[left]] -= 1

                if seen[fruits[left]] == 0:
                    del seen[fruits[left]]
                left += 1
            
            max_fruits = max(max_fruits,i-left+1)
        
        return max_fruits


# Status: independent
# Time Taken: 10 M
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:sliding window
# Variant: variable size
# Mistakes / Confusion:Na

# 10	-	LC	-	1004	-	Max Consecutive Ones III


class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0

        zeros = 0

        max_ones = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                zeros += 1
            
            while zeros > k:

                if nums[left] == 0:
                    zeros-= 1
                left += 1
            
            max_ones = max(max_ones,i-left+1)
        
        return max_ones


# Status: independent
# Time Taken: 10 M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:sliding window
# Variant: variable size
# Mistakes / Confusion:Na

# 11	-	LC	-	424	-	Longest Repeating Char Replacement

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        seen = {}

        max_subarry = 0

        left = 0

        for i in range(len(s)):

            seen[s[i]] = seen.get(s[i],0)+1

            max_char = max(seen.values())
            while (i-left+1) - max_char > k:

                seen[s[left]] -= 1

                left += 1
            
            max_subarry = max(max_subarry,i-left+1)

        return max_subarry

# Status: independent
# Time Taken: 10 M
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:sliding window
# Variant: variable size
# Mistakes / Confusion:Na

# 12	-	LC	-	121	-	Best Time to Buy and Sell Stock

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]

        max_profit = 0

        for i in range(1,len(prices)):

            if prices[i] < min_price:
                min_price = min(min_price,prices[i])
            else:
                
                profit = prices[i] - min_price

                max_profit = max(max_profit,profit)
        
        return max_profit

# Status: independent
# Time Taken: 10 M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:Running state 
# Variant: Kadane/min-max
# Mistakes / Confusion:Na

# 13	-	LC	-	53	-	Maximum Subarray

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = float('-inf')

        prefix = 0

        for i in range(len(nums)):

            prefix = max(nums[i],prefix+nums[i])

            max_sum = max(max_sum,prefix)
        
        return max_sum

# Status: independent
# Time Taken: 10 M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:Running state 
# Variant: Kadane/min-max
# Mistakes / Confusion:Na

# 14	-	LC	-	152	-	Maximum Product Subarray

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_product = nums[0]
        current_min = nums[0]
        current_max = nums[0]

        for i in range(1,len(nums)):

            temp_min = current_min
            temp_max = current_max

            current_max = max(nums[i],temp_min*nums[i],nums[i]*temp_max)
            current_min = min(nums[i],temp_min*nums[i],nums[i]*temp_max)

            max_product = max(max_product,current_max)

        return max_product

# Status: independent
# Time Taken: 10 M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:Running state 
# Variant: Kadane/min-max
# Mistakes / Confusion:Na

# 15	-	LC	-	704	-	Binary Search

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
            print(mid)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        return -1


# Status: independent
# Time Taken: 10 M
# Time Complexity: O(logn)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:Binary search 
# Variant: Applied Target Search
# Mistakes / Confusion:Na

# 16	-	LC	-	35	-	Search Insert Position

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        while left<= right:

            mid = (right+left)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

# Status: independent
# Time Taken: 10 M
# Time Complexity: O(logn)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:Binary search 
# Variant: Applied Target Search
# Mistakes / Confusion:Na

# 17	-	LC	-	278	-	First Bad Version

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n

        while left < right:

            mid = (right+left)//2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left 

# Status: independent
# Time Taken: 10 M
# Time Complexity: O(logn)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:Binary search 
# Variant: Applied Boundry Search
# Mistakes / Confusion:Na

# 18	-	LC	-	69	-	Sqrt(x)

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        left = 0
        right = x

        while left <= right:

            mid = (right+left)//2

            sqrt_of_mid = mid * mid

            if sqrt_of_mid == x:
                return mid
            elif sqrt_of_mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right

# Status: independent
# Time Taken: 10 M
# Time Complexity: O(logn)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:Binary search 
# Variant: Applied Boundry Search
# Mistakes / Confusion:Na


# 19	-	LC	-	744	-	Find Smallest Letter Greater

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = 0
        right = len(letters)-1
        greater = None

        while left <= right:

            mid = (right+left)//2

            if letters[mid] > target :
                greater = letters[mid]
                right = mid - 1
            else:
                left = mid + 1
        
        return greater if greater else letters[0]


# Status: independent
# Time Taken: 10 M
# Time Complexity: O(logn)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:Binary search 
# Variant: Applied Boundry Search
# Mistakes / Confusion:Na

# 20	-	LC	-	162	-	Find Peak Element

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(nums)-1

        while left < right:

            mid = (left+right)//2

            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        
        return left

# Status: independent
# Time Taken: 10 M
# Time Complexity: O(logn)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:Binary search 
# Variant: Applied Boundry Search
# Mistakes / Confusion:Na

# 21	-	LC	-	367	-	Valid Perfect Square

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 0
        right = num

        while left <= right:

            mid = (left+right)//2

            srrt = mid*mid
            if srrt == num:
                return True
            elif srrt > num:
                right = mid - 1
            else:
                left = mid + 1
        return False 

# Status: independent
# Time Taken: 10 M
# Time Complexity: O(logn)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:Binary search 
# Variant: Applied Target Search
# Mistakes / Confusion:Na


# 22	-	LC	-	441	-	Arranging Coins


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        # coins = 0

        while left <= right:

            mid = (left+right)//2

            coins_needed = mid*(mid+1)//2

            if coins_needed == n:
                return mid 
            elif coins_needed > n:
                right = mid - 1
            else:
                left = mid + 1
        
        return right

# Status: independent
# Time Taken: 10 M
# Time Complexity: O(logn)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:Binary search 
# Variant: Applied Target Search
# Mistakes / Confusion:Na

# 23	-	LC	-	374	-	Guess Number Higher or Lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num):
    pass

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n

        while left <= right:

            mid = (left+right)//2

            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                left = mid + 1
            else:
                right = mid - 1


# Status: independent
# Time Taken: 10 M
# Time Complexity: O(logn)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:Binary search 
# Variant: Applied Target Search
# Mistakes / Confusion:Na

# 24	-	LC	-	852	-	Peak Index in Mountain Array

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left = 0
        right = len(arr)-1

        while left < right:

            mid = (left+right)//2

            if arr[mid] > arr[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left 


# Status: independent
# Time Taken: 10 M
# Time Complexity: O(logn)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:Binary search 
# Variant: Applied Boundry Search
# Mistakes / Confusion:Na

# 25	-	LC	-	58	-	Length of Last Word

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = 0

        count = 0

        for i in range(len(s)):

            if s[i] != " ":
                count += 1
            else:
                count = 0
            
            if count != 0:
                last = count 
        return last


# Status: independent
# Time Taken: 10 M
# Time Complexity: O(logn)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:String Traversal 
# Variant: Na
# Mistakes / Confusion:Na


# 26	-	LC	-	33	-	Search in Rotated Sorted Array

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


            mid = (left+right)//2

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


# Status: independent
# Time Taken: 10 M
# Time Complexity: O(logn)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:Binary search 
# Variant: Applied Target search
# Mistakes / Confusion:Na

# 27	-	LC	-	153	-	Find Minimum in Rotated Sorted Array

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        while left < right:

            mid = (right+left)//2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

# Status: independent
# Time Taken: 10 M
# Time Complexity: O(logn)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:Binary search 
# Variant: Applied Boundry search
# Mistakes / Confusion:Na


# 28	-	LC	-	875	-	Koko Eating Bananas

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def countspeed(speed):

            count = 0

            for i in piles:

                remainder = 1 if i % speed != 0 else 0
                devisor = i // speed
                count += devisor + remainder
            
            return True if count<= h else False
        
        left = 1
        right = max(piles)

        while left < right:

            mid = (right+left)//2

            if countspeed(mid):
                right = mid
            else:
                left = mid + 1
        return left 



# Status: independent
# Time Taken: 10 M
# Time Complexity: O(logn)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:Binary search 
# Variant: Applied Boundry search
# Mistakes / Confusion:Na

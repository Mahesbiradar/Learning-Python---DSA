## Tier 3 — Revision (Backlog Clearance)

"""
### 1. K Divisible Elements Subarrays (LC 2261)

Given an integer array `nums` and two integers `k` and `p`, return the number of **distinct subarrays** which have **at most** `k` elements divisible by `p`.

Two subarrays are **distinct** if they have different elements or different lengths.

**Example 1:**
Input: nums = [2,3,3,2,2], k = 2, p = 2
Output: 11

**Example 2:**
Input: nums = [1,2,3,4], k = 4, p = 1
Output: 10

# Status: 
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Brute Force
# Variant: Subarray enumeration
# mistakes/confusion: ___

"""
class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        seen = set()

        for i in range(len(nums)):

            count = 0

            for j in range(i,len(nums)):

                if nums[j] % p == 0:
                    count += 1
                
                if count > k:
                    break
                
                seen.add(tuple(nums[i:j+1]))

        return len(seen)

# Status: Independent
# Time taken: 25 min
# Time complexity: O(n^3)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Brute Force
# Variant: Subarray enumeration
# mistakes/confusion: Na

"""
### 2. Two Sum II — Input Array Is Sorted (LC 167)

Given a **1-indexed** array of integers `numbers` that is already sorted in **non-decreasing order**, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 &lt;= index1 &lt; index2 &lt;= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, **added by one** as an integer array `[index1, index2]` of length 2.

**Example 1:**
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

**Example 2:**
Input: numbers = [2,3,4], target = 6
Output: [1,3]

**Example 3:**
Input: numbers = [-1,0], target = -1
Output: [1,2]

# Status: 
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Two Pointers
# Variant: Opposite ends
# mistakes/confusion: ___

"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers)-1

        while left < right:

            sum_of_two = numbers[left]+numbers[right]

            if sum_of_two == target:
                return [left+1,right+1]
            elif sum_of_two > target:
                right -= 1
            else:
                left += 1

# Status: independent
# Time taken: 10 min
# Time complexity: O(n)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Two Pointers
# Variant: Opposite ends
# mistakes/confusion: Na

"""
### 3. Unique Number of Occurrences (LC 1207)

Given an array of integers `arr`, return `true` if the number of occurrences of each value in the array is **unique**, or `false` otherwise.

**Example 1:**
Input: arr = [1,2,2,1,1,3]
Output: true

**Example 2:**
Input: arr = [1,2]
Output: false

**Example 3:**
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

"""

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        seen ={}

        for i in arr:
            seen[i]= seen.get(i,0)+1
        
        seen_set = set()
        
        for key,value in seen.items():

            if value in seen_set:
                return False
            
            seen_set.add(value)
        return True

# Status: independent
# Time taken: 15 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Frequency Hashing
# Variant: Count + query
# mistakes/confusion: Na

"""
### 4. Subarray Sums Divisible by K (LC 974)

Given an integer array `nums` and an integer `k`, return the number of non-empty subarrays that have a sum divisible by `k`.

**Example 1:**
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7

**Example 2:**
Input: nums = [5], k = 9
Output: 0

# Status: 
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Prefix Sum
# Variant: Modulo
# mistakes/confusion: ___

"""

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

# Status: independent
# Time taken: 25 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Prefix Sum
# Variant: Modulo
# mistakes/confusion: Na

"""
### 5. Continuous Subarray Sum (LC 523)

Given an integer array `nums` and an integer `k`, return `true` if `nums` has a **good subarray** or `false` otherwise.

A **good subarray** is a subarray where:
- its length is **at least two**, and
- the sum of the elements of the subarray is a multiple of `k`.

**Example 1:**
Input: nums = [23,2,4,6,7], k = 6
Output: true

**Example 2:**
Input: nums = [23,2,6,4,7], k = 6
Output: true

**Example 3:**
Input: nums = [23,2,6,4,7], k = 13
Output: false

"""

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen ={0:-1}

        prefix = 0

        for i in range(len(nums)):

            prefix += nums[i]

            remainder = prefix % k

            if remainder in seen:
                if i-seen[remainder] > 1:
                    return True   
            else:
                seen[remainder]=i

        return False

# Status: independent
# Time taken: 25 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Prefix Sum
# Variant: Modulo
# mistakes/confusion:Na

"""
### 6. Container With Most Water (LC 11)

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Example 1:**
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

**Example 2:**
Input: height = [1,1]
Output: 1

"""

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

            water = min(height[left],height[right]) * (right - left)

            print (water)

            if height[right] < height[left]:
                right -=1
            else:
                left += 1
            max_water = max(max_water,water)

        return max_water
    
# Status: Independent
# Time taken: 15 min
# Time complexity: O(n)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Two Pointers
# Variant: Maximize/minimize between ends
# mistakes/confusion:Na

"""
### 7. Isomorphic Strings (LC 205)

Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

**Example 1:**
Input: s = "egg", t = "add"
Output: true

**Example 2:**
Input: s = "foo", t = "bar"
Output: false

**Example 3:**
Input: s = "paper", t = "title"
Output: true

"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        seens = {}

        seent = {}

        for i in range(len(s)):

            if s[i] in seens and seens[s[i]] != t[i]:
                return False
            else:
                seens[s[i]] = t[i]
            
            if t[i] in seent and seent[t[i]] != s[i]:
                return False
            else:
                seent[t[i]] = s[i]
                
        return True
    
# Status: independent
# Time taken: 20 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Grouping Hash Map
# Variant: Canonical key
# mistakes/confusion: Na

"""
### 8. Remove Element (LC 27)

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place**. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

**Example 1:**
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

**Example 2:**
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]

"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        write = 0

        for i in range(len(nums)):

            if nums[i] != val:
                nums[write] = nums[i]
                write +=1
        return write

# Status: independent
# Time taken: 15 min
# Time complexity: O(n)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Two Pointers
# Variant: Write pointer — compact/remove
# mistakes/confusion: Na

"""
### 9. Arranging Coins (LC 441)

You have `n` coins and you want to build a staircase with these coins. The staircase consists of `k` rows where the `ith` row has exactly `i` coins. The last row of the staircase **may be** incomplete.

Given the integer `n`, return the number of **complete rows** of the staircase you will build.

**Example 1:**
Input: n = 5
Output: 2

**Example 2:**
Input: n = 8
Output: 3

"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n

        best = 0

        while left <= right:

            mid = (right+left)//2

            coinsneeded = mid*(mid+1)//2

            if coinsneeded == n:
                return mid
            elif coinsneeded > n:
                right = mid -1
            else:
                best = max(best,mid)
                left = mid + 1
        return best

# Status: independent
# Time taken: 20 min
# Time complexity: O(logn)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted 
# Pattern: Binary Search
# Variant: Lower bound — first position
# mistakes/confusion: Na

"""
### 10. Find Smallest Letter Greater Than Target (LC 744)

You are given an array of characters `letters` that is sorted in **non-decreasing order**, and a character `target`. There are **at least two different characters** in `letters`.

Return the **smallest** character in `letters` that is lexicographically **greater than** `target`. If such a character does not exist, return the first character in `letters`.

**Example 1:**
Input: letters = ["c","f","j"], target = "a"
Output: "c"

**Example 2:**
Input: letters = ["c","f","j"], target = "c"
Output: "f"

**Example 3:**
Input: letters = ["x","x","y","y"], target = "z"
Output: "x"

"""

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = 0
        right = len(letters)-1
        best = None

        while left <= right :

            mid = (right + left)//2

            if letters[mid]>target:
                best = letters[mid]
                right = mid -1
            else:
                left = mid + 1
        
        if best == None:
            return letters[0]
        else:
            return best

# Status: Independent
# Time taken: 10 min
# Time complexity: O(logn)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Binary Search
# Variant: Lower bound — first position
# mistakes/confusion: NA

"""
### 11. Guess Number Higher or Lower (LC 374)

We are playing the Guess Game. The game is as follows:

I pick a number from `1` to `n`. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API `int guess(int num)`, which returns 3 possible results:
- `-1`: Your guess is higher than the number I picked (i.e. `num &gt; pick`).
- `1`: Your guess is lower than the number I picked (i.e. `num &lt; pick`).
- `0`: your guess is equal to the number I picked (i.e. `num == pick`).

Return the number that I picked.

**Example 1:**
Input: n = 10, pick = 6
Output: 6

**Example 2:**
Input: n = 1, pick = 1
Output: 1

**Example 3:**
Input: n = 2, pick = 1
Output: 1

"""

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

            mid = (right + left)//2

            num = guess(mid)

            if num == 0:
                return mid
            elif num == -1:
                right = mid -1
            else:
                left = mid + 1

# Status: Independent
# Time taken: 15 min
# Time complexity: O(logn)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Binary Search
# Variant: Standard — find target
# mistakes/confusion: Na

"""
### 12. Make Sum Divisible by P (LC 1590)

Given an array of positive integers `nums`, remove the **smallest** subarray (possibly **empty**) such that the **sum** of the remaining elements is divisible by `p`. It is **not** allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or `-1` if it's impossible.

**Example 1:**
Input: nums = [3,1,4,2], p = 6
Output: 1

**Example 2:**
Input: nums = [6,3,5,2], p = 9
Output: 2

**Example 3:**
Input: nums = [1,2,3], p = 3
Output: 0

"""

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
        
        best = len(nums)

        prefix = 0

        seen = {0:-1}

        for i in range(len(nums)):

            prefix += nums[i]

            current  = prefix % p

            needed = (current - target) % p

            if needed in seen:

                best = min(best,i-seen[needed])
            
            seen[current] = i
        
        if best == len(nums):
            return -1
        else :
            return best

# Status: independent
# Time taken: 25 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Prefix Sum
# Variant: Modulo
# mistakes/confusion: Na





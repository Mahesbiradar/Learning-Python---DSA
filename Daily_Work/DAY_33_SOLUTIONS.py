## Concept Refresher — PATTERNS.md gap (no block exists yet for these two patterns)

"""
**Warm-up protocol (answer all 3 before coding):**
1. Write the template from memory.
2. "The invariant this template maintains is: ___"
3. "If I changed [specific line] to [wrong version], it would fail because: ___"

"""

#For the sequnce Expansion:
# 1. Write the template from memory.

# for i in seen:

#     if i-1 not in seen:
#         firstnumber = i
#         length = 1

#         while firstnumber + 1 in seen:
#             firstnumber += 1
#             length += 1
#         best = max ( best, length)

#2. "The invariant this template maintains is: ___"

# if i-1 not in seen

# 3. "If I changed [specific line] to [wrong version], it would fail because: ___"

# firstnumber + 1 to firstnumber + length it would fail bcz length it will skip some sequnce Numbers and lenght of the sequncy will be wrong


# For the binary search (Arranging Coins)
# 1. Write the template from memory.


# left = 0
# right = n

# while left <= right:

#     mid = (right+left)//2

#     coinsneeded = mid(mid+1)//2

#     if coinsneeded == n:
#         return mid
#     elif coinsneeded > n:
#         right = mid - 1
#     else:
#         best = max (best,mid)
#         left = mid + 1
# return best

# 2. "The invariant this template maintains is: ___"

# whenever the coins needed is less than the n the best varibale captures the max mid number.

# 3. "If I changed [specific line] to [wrong version], it would fail because: ___"

# if we dont capture the mid while the cn < n thene we will not going to capture correct answer.

## TIER 1 — Priority Revision (solve both, no hints — 2nd/3rd consecutive attempt on both

"""
### 1. Longest Consecutive Sequence (LC 128) — Medium
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence. Your algorithm must run in O(n) time.

Example 1: `nums = [100,4,200,1,3,2]` → Output: `4` (the sequence is 1,2,3,4)
Example 2: `nums = [0,3,7,2,5,8,4,6,0,1]` → Output: `9`

Constraints: `0 <= nums.length <= 10^5`, `-10^9 <= nums[i] <= 10^9`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        seen = set()

        for i in nums:
            seen.add(i)
        best = 0

        for num in seen:

            if num - 1 not in seen:
                startnumber = num
                lenght = 1

                while  startnumber + lenght in seen:
                    lenght += 1
                best = max( best,lenght)
        return best

# Status: Independent
# Time taken: 15 min
# Tier:
# Time complexity: O(n)
# Space complexity: O(n)
# LC status: Accepted 
# Pattern: Sequnce Expansion
# Variant:
# mistakes/confusion: Na

"""
### 2. Arranging Coins (LC 441) — Easy
You have `n` coins and want to build a staircase with `k` rows where the `i`th row has exactly `i` coins. The last row may be incomplete. Given `n`, return the number of complete rows.

Example 1: `n = 5` → Output: `2`
Example 2: `n = 8` → Output: `3`

Constraints: `1 <= n <= 2^31 - 1`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:

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
# Time taken: 15 min
# Tier:
# Time complexity: O(logn)
# Space complexity: O(1)
# LC status:Accepted
# Pattern:Binary search 
# Variant:Na
# mistakes/confusion:Na

## TIER 3 — Revision (3 problems)

"""
## TIER 3 — Revision (3 problems)

### 1. Find Smallest Letter Greater Than Target (LC 744) — Easy
Given a characters array `letters` sorted in non-decreasing order and a character `target`, return the smallest character in the array that is larger than `target`. If no such character exists, return the first character in `letters` (wrap around).

Example 1: `letters = ["c","f","j"], target = "a"` → `"c"`
Example 2: `letters = ["c","f","j"], target = "c"` → `"f"`
Example 3: `letters = ["c","f","j"], target = "d"` → `"f"`

Constraints: `2 <= letters.length <= 10^4`, letters are lowercase, sorted, contain at least 2 distinct characters.

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:

"""

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        best = None 

        left = 0
        right = len(letters)-1

        while left <= right:

            mid = (right +left)//2 

            if letters[mid]>target:
                best = letters[mid]
                right = mid - 1
            else:
                left = mid + 1
        if best == None :
            return letters[0]
        else: 
            return best

# Status: Independent
# Time taken: 20 min
# Tier:
# Time complexity: O(logn)
# Space complexity: O(1)
# LC status:Accepted
# Pattern:Binary Search
# Variant:Upper bound
# mistakes/confusion:Na

"""
### 2. Guess Number Higher or Lower (LC 374) — Easy
Pick a number from 1 to `n`. A pre-built API `guess(num)` returns `-1` (pick is lower), `1` (pick is higher), or `0` (correct). Return the number.

Example 1: `n = 10, pick = 6` → Output: `6`

Constraints: `1 <= n <= 2^31 - 1`, `1 <= pick <= n`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```

"""
def guess(num):
    pass

class Solution:
    def guessNumber(self, n: int) -> int:

        left = 0
        right = n

        while left <= right:

            mid = (right+left)//2

            num = guess(mid)

            if num == 0:
                return mid
            elif num == -1:
                right = mid -1
            else:
                left = mid +1

# Status: Independent
# Time taken: 10 min
# Tier:
# Time complexity: O(logn)
# Space complexity: O(1)
# LC status:Accepted
# Pattern:Binary search 
# Variant:
# mistakes/confusion:Na

"""
### 3. Maximum Number of Vowels in a Substring of Given Length (LC 1456) — Medium
Given a string `s` and an integer `k`, return the maximum number of vowel letters in any substring of `s` with length `k`.

Example 1: `s = "abciiidef", k = 3` → Output: `3`
Example 2: `s = "aeiou", k = 2` → Output: `2`
Example 3: `s = "leetcode", k = 3` → Output: `2`

Constraints: `1 <= s.length <= 10^5`, lowercase letters, `1 <= k <= s.length`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```
"""

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        count = 0
        best = 0

        for right in range(len(s)):

            if s[right] in 'aeiou':
                count += 1
            
            while right-left+1 > k:

                if s[left] in 'aeiou':
                    count -=1
                left +=1
            if right-left+1 == k:
                best = max(best,count)
        return best

# Status: independent
# Time taken: 20 min
# Tier:
# Time complexity: O(n)
# Space complexity: O(1)
# LC status:Accepted
# Pattern:Sliding Window 
# Variant:Fixed Size 
# mistakes/confusion:Na

## New Problems (3 problems)

"""
### 1. Search in Rotated Sorted Array — Medium
There is an integer array `nums` sorted in ascending order (distinct values), rotated at an unknown pivot. Given the rotated array and an integer `target`, return the index of `target` if found, or `-1`. Must run in O(log n).

Example 1: `nums = [4,5,6,7,0,1,2], target = 0` → Output: `4`
Example 2: `nums = [4,5,6,7,0,1,2], target = 3` → Output: `-1`
Example 3: `nums = [1], target = 0` → Output: `-1`

Constraints: `1 <= nums.length <= 5000`, `-10^4 <= nums[i] <= 10^4`, all values unique, array is rotated at some pivot, `-10^4 <= target <= 10^4`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:

"""

def roatedarray(nums,target):


    left=0
    right=len(nums)-1

    while left <= right:

        mid = (right+left)//2

        if nums[mid]==target:
            return mid
        elif nums[left]<=nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right= mid-1
            else:
                left = mid + 1
        else:
            if nums[mid]<= target<=nums[right]:
                left = mid +1
            else:
                right = mid -1
    return -1

print(roatedarray([4,5,6,7,0,1,2],0))
print(roatedarray(nums = [4,5,6,7,0,1,2], target = 3))
print(roatedarray(nums = [1], target = 0))


# Status: hint 
# Time taken: 30 min
# Tier:
# Time complexity: O(log n)
# Space complexity: O(1)
# LC status:Accepted
# Pattern:Binary search
# Variant: Exact search
# mistakes/confusion:

"""
### 2. Find Minimum in Rotated Sorted Array — Medium
Suppose an array of length `n` sorted in ascending order is rotated between 1 and `n` times. Given the rotated sorted array `nums` of unique elements, return the minimum element. Must run in O(log n).

Example 1: `nums = [3,4,5,1,2]` → Output: `1`
Example 2: `nums = [4,5,6,7,0,1,2]` → Output: `0`
Example 3: `nums = [11,13,15,17]` → Output: `11`

Constraints: `n == nums.length`, `1 <= n <= 5000`, `-5000 <= nums[i] <= 5000`, all unique, rotated between 1 and n times.

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:

"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        while left < right :

            mid = (right+left)//2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid 
        return nums[left]

# Status: Hint
# Time taken: 25 min
# Tier:
# Time complexity: O(logn)
# Space complexity: O(1)
# LC status:Accepted
# Pattern:Binary search
# Variant:boundry search
# mistakes/confusion:Na

"""
### 3. Koko Eating Bananas — Medium
There are `n` piles of bananas, `piles[i]` bananas in the `i`th pile. Koko eats at a speed of `k` bananas per hour: each hour she picks one pile and eats `k` bananas from it (or all of it if fewer than `k` remain), and does not eat from another pile that hour. Koko wants to finish all bananas within `h` hours. Return the minimum integer `k` such that she can finish within `h` hours.

Example 1: `piles = [3,6,7,11], h = 8` → Output: `4`
Example 2: `piles = [30,11,23,4,20], h = 5` → Output: `30`
Example 3: `piles = [30,11,23,4,20], h = 6` → Output: `23`

Constraints: `1 <= piles.length <= 10^4`, `piles.length <= h <= 10^9`, `1 <= piles[i] <= 10^9`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:

"""

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        def feasible(speed):

            hourstaken=0

            for pile in piles:

                quotient = pile // speed
                remainder = 0

                if pile % speed ==0:
                    remainder = 0
                else:
                    remainder = 1
                
                hourstaken += quotient + remainder
            
            # if hourstaken > h:
            #     return False
            # else:
            #     return True
            return hourstaken <= h
            
        lo = 1
        hi = max(piles)

        while lo < hi:

            mid = (hi+lo)//2

            work = feasible(mid)

            if work:
                hi = mid
            else:
                lo = mid + 1
        return lo
    
# Status: Hint
# Time taken: 30 min
# Tier:
# Time complexity: O(n x log(max(piles)))
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Binary search
# Variant: Boundry Search 
# mistakes/confusion:


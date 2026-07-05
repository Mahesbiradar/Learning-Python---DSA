

# **Step 1 — Write the derivation by hand, from memory, before opening PATTERNS.md:**

# If prefix[j] % k = prefix[i] % k
# Then (prefix[j] - prefix[i]) % k = ...
# And  prefix[j] - prefix[i] = ...
# Therefore prefix[j] - prefix[i]= subarray(nums(i+1....j))

#If Two Prefix remainder belongs to same remainder family then difrrence b/w These Two subarrys is dividible by k.

# total_sum % p = target        (what does this represent?)

#the target reprent the Remainder family of Subarray which need to be removed from arry to make the arry divisible by k.

# We need: subarray_sum % p = target
# prefix[j] - prefix[i] = subarray_sum
# → prefix[i] % p = needed 

# Here How it Goes is 

# Now to if we need a subarry the we have

# subarry = prefix[j]-prefix[i]

# and we know if Two frefix remainder belongs to same remainder family then we know the diff b/w Those prefixes is divisible by k

#Now 

# subarry = current - previous

# and we need The current % k -previou %k need tp be = to Target Family.

#Since we Know Target Family Therefor 

#Rearrangig the Equation

# Needed = (current-target+k) %k # +k  is added is to wrap the negative family.

# if needed in seen Then we store the min lenght of the subarry  

# and With each iteration we store the current prefix remainder with its latest index.

"""
### A. Continuous Subarray Sum (LC 523) — Medium [revision — already Tier 3, solve cold as reinforcement]

Given an integer array `nums` and an integer `k`, return `true` if `nums` has a continuous subarray
of size **at least two** whose elements sum up to a multiple of `k`, or `false` otherwise.

An integer `x` is a multiple of `k` if there exists an integer `n` such that `x = n * k`. `0` is
always a multiple of `k`.

**Example 1:**
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2,4] is a continuous subarray of size 2 whose elements sum up to 6.

**Example 2:**
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23,2,6,4,7] is a continuous subarray of size 5 whose elements sum up to 42, and 42 is
a multiple of 6.

**Example 3:**
Input: nums = [23,2,6,4,7], k = 13
Output: false

**Constraints:**
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
- 0 <= sum(nums[i]) <= 2^31 - 1
- 1 <= k <= 2^31 - 1

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

"""
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {0:-1}

        prefix = 0

        for i in range(len(nums)):

            prefix += nums[i]

            needed = prefix % k

            if needed in seen:
                if i- seen[needed]>1:
                    return True
            else:
                seen[needed]=i
            
        return False 


# Status: Independent
# Time taken: 20 min
# Tier: ___
# Time complexity: O(n) — iterating each element in the list only once
# Space complexity: O(n) — Additional Sequencial data structure is used.
# LC status: Accepted
# Pattern: Prefix sum + Modulo
# Variant: Modulo
# mistakes/confusion: Na ran a Dedicated Session on Chatgpt for Prefix sum + modulo varient and all the concept is internalized now.


"""
### B. Subarray Sums Divisible by K (LC 974) — Medium [revision — already Tier 3, solve cold as reinforcement]

Given an integer array `nums` and an integer `k`, return the number of non-empty **subarrays**
that have a sum divisible by `k`.

A subarray is a contiguous part of an array.

**Example 1:**
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4,5,0,-2,-3,1], [5], [5,0], [5,0,-2,-3], [0], [0,-2,-3], [-2,-3]

**Example 2:**
Input: nums = [5], k = 9
Output: 0

**Constraints:**
- 1 <= nums.length <= 3 * 10^4
- -10^4 <= nums[i] <= 10^4
- 2 <= k <= 10^4

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

"""
class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen={0:1}

        prefix = 0

        count = 0

        for i in range(len(nums)):

            prefix += nums[i]

            needed = prefix % k

            if needed in seen:
                count+=seen[needed]
            
            seen[needed]= seen.get(needed,0)+1
           
        return count

# Status: Independent
# Time taken: 20 min
# Tier: ___
# Time complexity: O(n) — one single pass over a array
# Space complexity: O(n) — Hash map ussed to store the remainders withs its Frequency.
# LC status: Accepted
# Pattern: Refix sum + modulo
# Variant: Modulo varient
# mistakes/confusion: Na

"""
### C. Make Sum Divisible by P (LC 1590) — Medium ⚠️ USO STANDALONE TARGET — up to 90 min

Given an array of positive integers `nums`, remove the **smallest** subarray (possibly empty) such
that the **sum** of the remaining elements is divisible by `p`. It is **not** allowed to remove
the whole array. Return the length of the smallest subarray to remove, or **-1** if impossible.

A **subarray** is a contiguous block of elements in the array.

**Example 1:**
Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: Sum is 10. Remove [4] → remaining sum = 6, divisible by 6.

**Example 2:**
Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: Remove [5,2] → remaining sum = 9, divisible by 9.

**Example 3:**
Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Sum = 6 is already divisible by 3. Remove nothing (return 0).

**Constraints:**
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= p <= 10^9

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

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

        seen={0:-1}

        for i in range(len(nums)):

            prefix += nums[i]

            current = prefix % p

            needed = (current-target+p) % p

            if needed in seen:

                best = min(best,i-seen[needed])
            
            seen[current]=i
        
        if best==len(nums):
            return -1
        else:
            return best
        

# Status: Independent
# Time taken: 30 min
# Tier: ___
# Time complexity: O(n) — single pass over a array
# Space complexity: O(n) —  Hash map 
# LC status: Accepted 
# Pattern: Prefix + modulo
# Variant: __
# mistakes/confusion: Na

# **Step 4 — Only mark the USO row "Standalone Session Done: Yes" if tomorrow (next study day) you can

# I had Standalone Session to understand the intution and the basics behind the modulo varient for more than 5-6 Hrs Then all internalized.

## TIER 1 — Priority Revision (solve first, all of them)

"""
### 1. Longest Consecutive Sequence (LC 128) — Medium ⚠️ Hint D31 — solve cold today, no video/notes

Given an unsorted array of integers `nums`, return the length of the **longest consecutive
elements sequence**.

You must write an algorithm that runs in **O(n)** time.

**Example 1:**
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4]. Its length is 4.

**Example 2:**
Input: nums = [0,3,7,2,5,8,1,9,6,4]
Output: 10

**Example 3:**
Input: nums = []
Output: 0

**Constraints:**
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        seen= set()

        for i in nums:
            seen.add(i)
        best=0
        
        for i in seen:

            if i-1 not in seen:
                startnum= i
                lenght = 1

                while startnum + 1 in seen:

                    startnum +=1
                    lenght +=1
                best= max(best,lenght)
        return best

# Status: Hint
# Time taken: 20 min
# Tier: ___
# Time complexity: O(n) — single pass over array
# Space complexity: O(n) — Hash map used 
# LC status: Accepted 
# Pattern: Hash Map + Sequnece Expansion
# Variant: ___
# mistakes/confusion: Na

"""
### 2. Arranging Coins (LC 441) — Easy [OVERDUE since Jun 27]

You have `n` coins and you want to build a staircase with these coins. The staircase consists of
`k` rows where the `i`th row has exactly `i` coins. The last row of the staircase may be
incomplete.

Given the integer `n`, return the number of **complete rows** of the staircase you will build.

**Example 1:**
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

**Example 2:**
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.

**Constraints:**
- 1 <= n <= 2^31 - 1

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

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

        while left <= right :

            mid = (right + left) //2

            coinsneeded = mid*(mid+1)/2

            if coinsneeded == n:
                return mid
            elif coinsneeded > n:
                right = mid -1
            else:
                best = max(best,mid)
                left = mid + 1
        return best
# Status:Hint ( For the Formula for coins Needed)
# Time taken: 25 min
# Tier: ___
# Time complexity: O(log n) — Search Spave Becomes Half 
# Space complexity: O(1) — 
# LC status: Accepted 
# Pattern: Binary search
# Variant: ___
# mistakes/confusion: Na

"""
### 3. Remove Element (LC 27) — Easy [OVERDUE since Jun 28]

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums`
**in-place**. The order of the elements may be changed. Then return the number of elements in
`nums` which are not equal to `val`.

**Example 1:**
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

**Example 2:**
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]

**Constraints:**
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

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
                nums[write]=nums[i]
                write +=1
        return write
    
# Status: Independent
# Time taken: 10 min
# Tier: ___
# Time complexity: O(n) — single pass on array
# Space complexity: O(1) — No sequnecial data structure is used.
# LC status: Accepted
# Pattern: Write Pointer
# Variant: 
# mistakes/confusion:Na

"""
### 4. Total Appeal of A String (LC 2262) — Hard [OVERDUE since Jul 2 — optimal not yet submitted]

The **appeal** of a string is the number of **distinct** characters found in the string.
Given a string `s`, return the **total appeal** of all of its **substrings**.
A substring is a contiguous sequence of characters within a string.

**Example 1:**
Input: s = "abbca"
Output: 28
Explanation: The following are the substrings of "abbca":
- Substrings of length 1: "a", "b", "b", "c", "a" have an appeal of 1, 1, 1, 1, and 1 respectively.
- Substrings of length 2: "ab", "bb", "bc", "ca" have an appeal of 2, 1, 2, and 2 respectively.
- Substrings of length 3: "abb", "bbc", "bca" have an appeal of 2, 2, and 3 respectively.
- Substrings of length 4: "abbc", "bbca" have an appeal of 3 and 3 respectively.
- Substrings of length 5: "abbca" has an appeal of 3.
The total appeal is 1+1+1+1+1 + 2+1+2+2 + 2+2+3 + 3+3 + 3 = 28.

**Example 2:**
Input: s = "code"
Output: 20

**Constraints:**
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.

```python
# Your solution here (attempt the optimal this time — last-index-of-char + contribution counting)
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___
"""
class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0

        for i in range(len(s)):

            seen=set()

            for j in range(i,len(s)):

                seen.add(s[j])

                count+=len(seen)

                print(i,j,seen,count)
        return count
    
# Status: Independent
# Time taken: 20 min
# Tier: ___
# Time complexity: O(n^2) — [Nested Loop
# Space complexity: O(n) — Used Hash map
# LC status:Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: Na

## TIER 3 — Revision (4 problems — doubled today to cover the 2-day gap)

"""
### 5. Two Sum II — Input Array Is Sorted (LC 167) — Medium [Due Jul 4]

Given a **1-indexed** array of integers `numbers` that is already sorted in **non-decreasing
order**, find two numbers such that they add up to a specific `target` number. Return the indices
of the two numbers, `index1` and `index2`, **added by one**, as an integer array
`[index1, index2]` of length 2.

**Example 1:**
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

**Example 2:**
Input: numbers = [2,3,4], target = 6
Output: [1,3]

**Example 3:**
Input: numbers = [-1,0], target = -1
Output: [1,2]

**Constraints:**
- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order
- -1000 <= target <= 1000
- Exactly one solution exists.

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
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

        while left <= right:

            sumoftwo = numbers[left] + numbers[right]

            if sumoftwo > target:
                right -=1
            elif sumoftwo == target:
                return [left+1,right+1]
            else:
                left +=1

# Status: Independent
# Time taken: 10 min
# Tier: ___
# Time complexity: O(n) — Single pass over list
# Space complexity: O(1) — 
# LC status: Accepted
# Pattern: Two pointers
# Variant: 
# mistakes/confusion: Na

"""
### 6. Unique Number of Occurrences (LC 1207) — Easy [Due Jul 4]

Given an array of integers `arr`, return `true` if the number of occurrences of each value in the
array is **unique**, or `false` otherwise.

**Example 1:**
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: 1 occurs 3 times, 2 occurs 2 times, 3 occurs 1 time. No two values have the same
number of occurrences.

**Example 2:**
Input: arr = [1,2]
Output: false

**Example 3:**
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

**Constraints:**
- 1 <= arr.length <= 1000
- -1000 <= arr[i] <= 1000

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

"""

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen={}

        for i in arr:
            seen[i]= seen.get(i,0)+1
        
        seen_set=set()

        for key,value in seen.items():

            if value in seen_set:
                return False
            seen_set.add(value)
        return True        
    
# Status: Independent
# Time taken:10 min
# Tier: ___
# Time complexity: O(n) — single pass over list
# Space complexity: O(n) — Hash map is used
# LC status: Accepted
# Pattern: Frequncy Hashing with second Pass
# Variant: ___
# mistakes/confusion: Na


"""
### 7. Isomorphic Strings (LC 205) — Easy [Due Jul 5 — regression risk, appeared in Regression Log twice before]

Given two strings `s` and `t`, determine if they are **isomorphic**.
Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.
All occurrences of a character must be replaced with another character while preserving the order
of characters. No two characters may map to the same character, but a character may map to itself.

**Example 1:**
Input: s = "egg", t = "add"
Output: true

**Example 2:**
Input: s = "foo", t = "bar"
Output: false

**Example 3:**
Input: s = "paper", t = "title"
Output: true

**Constraints:**
- 1 <= s.length <= 5 * 10^4
- t.length == s.length
- s and t consist of any valid ASCII character.

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

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

        seen_s={}

        seen_t={}

        for i in range(len(s)):

            if s[i] in seen_s and seen_s[s[i]] != t[i]:
                return False
            
            seen_s[s[i]]=t[i]

            if t[i] in seen_t and seen_t[t[i]] != s[i]:
                return False
            
            seen_t[t[i]]=s[i]
        return True
    

# Status: Independent
# Time taken: 15 min
# Tier: ___
# Time complexity: O(n) — single pass over the list
# Space complexity: O(n) — Hash map used
# LC status: Accepted
# Pattern: Frequncy Hashing
# Variant: ___
# mistakes/confusion: Na

"""
### 8. Container With Most Water (LC 11) — Medium [Due Jul 5]

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such
that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains
the most water. Return the maximum amount of water a container can store.

Notice that you may not slant the container.

**Example 1:**
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

**Example 2:**
Input: height = [1,1]
Output: 1

**Constraints:**
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0

        right = len(height)-1

        best=0

        while left <= right :

            maxwater = min(height[left],height[right])*(right-left)

            best = max(best,maxwater)

            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return best
    

# Status: Independent
# Time taken: 15 min
# Tier: ___
# Time complexity: O(n) — single pass over list
# Space complexity: O(1) —
# LC status: Accepted 
# Pattern: Two pointers
# Variant: ___
# mistakes/confusion: Na


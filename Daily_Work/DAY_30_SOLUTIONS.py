"""
## Warm-Up — Prefix Sum Modulo Template (5 min, write from memory)
Before the Tier 1 problems, write the core Prefix Sum + Modulo template from memory.
Key: what is `needed`, how does `seen` get initialized, why store `index` not `count`?

[ Write template here ]

"""

#Template

"""
## TIER 4 Recalls (5 min each, no full solve)
Write the template from memory. If you can't in 3 min → flag as Tier 2 and add to next day.

1. Sliding Window (Variable size)
2. Prefix Sum + Hash Map (560 style — subarray sum equals k)

"""
# 1. Sliding Window (Variable size)

def slidingwindow(nums,k):

    countofzeros=0

    best=0

    left=0

    for right in range(len(nums)):

        if nums[right] == 0:
            countofzeros += 1
        
        while countofzeros>k:

            if nums[left] == 0:
                countofzeros -= 1
            left += 1
        
        best = max(best,right-left+1)
    
    return best

# The issues i faced to remide template is i have to see the problem on same concept therefor i used LC 1004 To write this temeplate.

# 2. Prefix Sum + Hash Map (560 style — subarray sum equals k)

def prefixsum_hashmpa(nums, k):

    seen={0:1}

    prefix=0

    count=0


    for i in range(len(nums)):

        prefix += nums[i]

        needed = prefix - k

        if needed in seen:
            count+=seen[needed]
        
        seen[prefix]=seen.get(prefix,0)+1
    
    return count

print(prefixsum_hashmpa([1,2,3], k = 3))

#this also same i used the problem to write the template.

## TIER 1 — Priority Revision (solve ALL 5 before anything else)

"""

### 1. Make Sum Divisible by P (LC 1590) — Medium
Given an array of positive integers `nums`, remove the **smallest** subarray (possibly empty) such
that the **sum** of the remaining elements is divisible by `p`. It is **not** allowed to remove
the whole array. Return the length of the smallest subarray that you need to remove, or `-1` if
it is impossible.

A **subarray** is defined as a contiguous block of elements in the array.

**Example 1:**
Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum is 10. Remove [4] → remaining sum = 6, divisible by 6.

**Example 2:**
Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: Remove [5,2] → remaining sum = 9, divisible by 9.

**Example 3:**
Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Sum = 6 is already divisible by 3. Remove nothing.

**Constraints:**
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= p <= 10^9

**Recovery note:** Yesterday you needed a full ChatGPT session. Today: no hints. Think:
  1. What is `target = total % p`?
  2. What does `current - target (mod p)` tell you?
  3. Why initialize `seen = {0: -1}` and store index, not count?

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

"""

def minSubarray(nums,p):

    seen={0:-1}

    totalsum = sum(nums)

    target = totalsum % p

    if target == 0:
        return 0

    best = len(nums) 

    prefix = 0

    for i in range(len(nums)):

        prefix += nums[i]

        current = prefix % p

        needed = (current - target) % p

        if needed in seen:

            best = min (best, i-seen[needed])
        
        seen[current] = i
    
    if best == len(nums):
        return -1
    else:
        return best
    

print(minSubarray(nums = [3,1,4,2], p = 6))

# Status:Hint
# Time taken: 35 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(n)
# LC status: Accepted 
# Pattern: Prefix modulo
# Variant: ___
# mistakes/confusion: Still the entire solution is no intution just with memory is solved but ill take seperate sessionon this varient apart from regular TASK .


"""
### 2. Contiguous Array (LC 525) — Medium
Given a binary array `nums`, return the maximum length of a contiguous subarray with an equal
number of `0` and `1`.

**Example 1:**
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

**Example 2:**
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

**Constraints:**
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1

**Recovery note:** Yesterday the optimal needed a video. Key idea: treat 0 as -1, track balance.
When does the same balance appear twice? What does that mean for the subarray between them?

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___

"""

#Brute Force

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best = 0

        for i in range(len(nums)):

            prefix = 0

            for j in range(i,len(nums)):

                if nums[j] == 0:
                    prefix -= 1
                else:
                    prefix += 1

                if prefix == 0:
                    best = max(best, j-i+1 )
        return best
    

#optimal solution 

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {0:-1}

        prefix = 0

        best = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1
            
            if prefix in seen:
                best = max(best, i-seen[prefix])
            else:
                seen[prefix] = i
        return best

# Status: Independent
# Time taken: 25 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(n)
# LC status: Accepted 
# Pattern: Prefix sum + Hash Map
# Variant: 
# mistakes/confusion: NA

"""
### 3. Range Sum Query - Immutable (LC 303) — Easy
Given an integer array `nums`, handle multiple queries of the following type:
Calculate the sum of the elements of `nums` between indices `left` and `right` **inclusive**.

Implement the `NumArray` class:
- `NumArray(int[] nums)` — Initializes the object with the integer array `nums`.
- `int sumRange(int left, int right)` — Returns the sum of elements between indices `left` and
  `right` inclusive (O(1) per query).

**Example 1:**
Input:
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output: [null, 1, -1, -3]
Explanation:
numArray = NumArray([-2, 0, 3, -5, 2, -1])
numArray.sumRange(0, 2) → (-2) + 0 + 3 = 1
numArray.sumRange(2, 5) → 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5) → (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

**Constraints:**
- 1 <= nums.length <= 10^4
- -10^5 <= nums[i] <= 10^5
- 0 <= left <= right < nums.length
- At most 10^4 calls will be made to sumRange

**Recovery note:** Yesterday: couldn't access class variable in `sumRange`. Key: store prefix
array as `self.prefix` in `__init__`, access via `self.prefix` in `sumRange`.

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) init | O(?) query
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

"""

#Brute Force:

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        prefix=0
        for i in range(left,right+1):

            prefix += self.nums[i]
        
        return prefix


#optimal solution 

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix=[0]
       

        for i in range(len(nums)):
            self.prefix.append(self.prefix[i]+nums[i])

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix[right+1]-self.prefix[left]

"""
### 4. Find the Divisibility Array of a String (LC 2575) — Medium
You are given a **0-indexed** string `word` of length `n` consisting of digits, and a positive
integer `m`.

The **divisibility array** `div` of `word` is an integer array of length `n` such that:
- `div[i] = 1` if the numeric value of `word[0,...,i]` is divisible by `m`, or
- `div[i] = 0` otherwise.

Return the divisibility array of `word`.

**Example 1:**
Input: word = "998244353", m = 3
Output: [1,1,0,0,0,1,1,0,0]
Explanation:
word[0..0] = "9"      → 9 % 3 = 0  → div[0] = 1
word[0..1] = "99"     → 99 % 3 = 0 → div[1] = 1
word[0..2] = "998"    → 998 % 3 = 2 → div[2] = 0

**Example 2:**
Input: word = "1010", m = 10
Output: [0,1,0,1]

**Constraints:**
- 1 <= n <= 10^5
- word consists of digits from '0' to '9'
- 1 <= m <= 10^9

**Recovery note:** Yesterday needed ChatGPT for the math. Key formula: to append digit d to
number n → `new_number = n * 10 + d`. Therefore `new_remainder = (old_remainder * 10 + int(d)) % m`.
You do NOT need to build the full number — only track the running remainder.

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

"""
#optimal

class Solution(object):
    def divisibilityArray(self, word, m):
        """
        :type word: str
        :type m: int
        :rtype: List[int]
        """
        remainder = 0

        out = []

        for i in range(len(word)):

            remainder = (remainder * 10 + int(word[i])) % m

            if remainder == 0:
                out.append(1)
            else:
                out.append(0)
        return out


#Brute force 

def divisibilityArray(word, m):
        """
        :type word: str
        :type m: int
        :rtype: List[int]
        """
        prefix=0

        out=[]


        for i in range(len(word)):

            prefix = (prefix * 10 + int(word[i])) 

            print(f"i: {prefix}")

            if prefix % m == 0:
                out.append(1)
            else:
                out.append(0)

        return out

print(divisibilityArray("1010", m = 10))


# Status: Independent (just fomrula seen for optimal solution)
# Time taken: 25 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted 
# Pattern: prefix running state
# Variant: 
# mistakes/confusion: NA

## TIER 2 — Revision (3 problems)

"""
### 6. Top K Frequent Words (LC 692) — Medium
Given an array of strings `words` and an integer `k`, return the `k` most frequent strings.
Return the answer sorted by frequency from highest to lowest. Sort words with the same frequency
by their **lexicographical** (alphabetical) order.

**Example 1:**
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent. "i" before "love" due to lower alpha order.

**Example 2:**
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]

**Constraints:**
- 1 <= words.length <= 500
- 1 <= words[i].length <= 10
- words[i] consists of lowercase English letters
- k is in the range [1, number of unique words]

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

"""

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        seen={}

        output=[]

        for i in words:
            seen[i]=seen.get(i,0)+1
        
        sorted_seen=sorted(seen.items(),key=lambda x : (-x[1],x[0]))

        for key,value in sorted_seen:
            output.append(key)

            if len(output) == k:
                return output
            
# Status: Independent
# Time taken: 20 min
# Tier: ___
# Time complexity: O(m+logn)
# Space complexity: O(n)
# LC status: Accepted 
# Pattern: Frequncy Hashing + Sorting
# Variant: ___
# mistakes/confusion: Just I confused for sorting (-x[1],x[0]) i tried to sort -x[0],x[1] then saw on prev and corrected.

"""
### 7. Max Number of K-Sum Pairs (LC 1679) — Medium
You are given an integer array `nums` and an integer `k`. In one operation, you can pick two
numbers from the array whose sum equals `k` and remove them from the array. Return the maximum
number of operations you can perform on the array.

**Example 1:**
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: [1,4] removed → [2,3] removed. 2 operations total.

**Example 2:**
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: [3,3] removed. 1 operation total.

**Constraints:**
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= 10^9

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

"""

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0

        right = len(nums)-1

        count=0

        sorted_num = sorted(nums)

        while left < right :

            num= sorted_num[left] + sorted_num[right]

            if num == k  :
                count += 1
                left += 1
                right -= 1
            elif num > k:
                right -= 1
            else:
                left += 1
        return count
    

# Status: Independent
# Time taken: 25 min
# Tier: ___
# Time complexity: O(nlogn)
# Space complexity: O(1)
# LC status: Accepted 
# Pattern: Two pointers
# Variant: ___
# mistakes/confusion: NA

"""
### 8. Minimize Maximum Pair Sum in Array (LC 1877) — Medium
The **pair sum** of a pair `(a, b)` is equal to `a + b`. The **maximum pair sum** is the largest
pair sum in a list of pairs. For example, if we have pairs `(1,5)`, `(2,3)`, and `(4,4)`, the
maximum pair sum would be `max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8`.

Given an array `nums` of **even** length `n`, pair up the elements into `n / 2` pairs such that:
- Each element is in exactly one pair, and
- The **maximum pair sum** is **minimized**.

Return the minimized maximum pair sum after optimally pairing up the elements.

**Example 1:**
Input: nums = [3,5,2,3]
Output: 7
Explanation: Pair [3,3] and [5,2]. Maximum pair sum = max(6,7) = 7.

**Example 2:**
Input: nums = [3,5,4,2,4,6]
Output: 8
Explanation: Pair [3,6], [5,4], [2,4]. Maximum sum = max(9,9,6) = 9. Wait — optimal is [2,6],[3,5],[4,4] → max = 8.

**Constraints:**
- n == nums.length
- 2 <= n <= 10^5
- n is even
- 1 <= nums[i] <= 10^5
"""

class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0

        right = len(nums)-1

        maxpair = 0

        sorted_nums=sorted(nums)

        while left < right :

            num = sorted_nums[left] + sorted_nums[right]

            maxpair = max(maxpair,num)

            left += 1
            right -= 1
        return maxpair

# Status: Independent 
# Time taken: 15 min
# Tier: ___
# Time complexity: O(nlogn)
# Space complexity: O(1)
# LC status: Accepted 
# Pattern: Two Pointers
# Variant: 
# mistakes/confusion: Na

## TIER 3 — Revision (2 problems)

"""
### 9. Peak Index in Mountain Array (LC 852) — Medium
An array `arr` is a **mountain** if:
- `arr.length >= 3`
- There exists some `i` with `0 < i < arr.length - 1` such that:
  `arr[0] < arr[1] < ... < arr[i-1] < arr[i] > arr[i+1] > ... > arr[arr.length-1]`

Given a mountain array `arr`, return the index `i` such that the above conditions hold.
You must solve it in **O(log n)** time.

**Example 1:**
Input: arr = [0,1,0]
Output: 1

**Example 2:**
Input: arr = [0,2,1,0]
Output: 1

**Example 3:**
Input: arr = [0,10,5,2]
Output: 1

**Constraints:**
- 3 <= arr.length <= 10^5
- 0 <= arr[i] <= 10^6
- arr is guaranteed to be a mountain array

```python
# Your solution here
```
"""

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

            if arr[mid] > arr[mid+1]:
                right = mid
            else:
                left = mid+1
        return left
    
# Status: Independent
# Time taken: 15 min
# Tier: ___
# Time complexity: O(log n)
# Space complexity: O(1)
# LC status: Accepted 
# Pattern: Binary search
# Variant: ___
# mistakes/confusion:NA


"""
### 10. Remove Duplicates from Sorted Array (LC 26) — Easy
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates **in-place**
such that each unique element appears only once. The relative order of the elements should be
kept the same. Return the number of unique elements `k`.

The first `k` elements of `nums` must contain the unique elements in order. The remaining
elements are not important. Return `k`.

**Example 1:**
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

**Example 2:**
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

**Constraints:**
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order

```python
# Your solution here
```
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        write = 1

        for i in range(1,len(nums)):

            if nums[i] != nums[write-1]:

                nums[write] = nums[i]

                write += 1
        
        return write
    
# Status: Independent 
# Time taken: 10 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted #
# Pattern: Write Pointer
# Variant: ___
# mistakes/confusion: NA

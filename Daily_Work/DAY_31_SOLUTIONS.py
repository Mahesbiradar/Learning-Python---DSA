"""
## ⚠️ PRE-SESSION: Prefix Sum + Modulo Derivation (5 min — do this before Tier 1)

UNRESOLVED-SINCE-ORIGIN flag is active for Prefix Sum + Modulo.
Before attempting LC 1590, write the 4-line algebraic proof from memory below.
Do NOT open PATTERNS.md until you have tried. After writing, verify against PATTERNS.md.

```
[ Write proof here ]
If prefix[j] % k = ...
Then ...
And ...
Therefore ...
```

Only proceed to LC 1590 once you can write this proof correctly without looking.
Time for LC 1590 today is NOT capped at 40 min — give it up to 90 min.

"""

# if prefix[j] % k == prefix[i] % K:

#     best = max(best, i-seen[needed])
# else:
#     seen[needed]=i

# return best

#Exactly what your asking 

# current= Prefix % k

# nedded = (current-Target) % k

# if nedded in seen:

#     best = max(best, i-seen[needed])
# else:
#     seen[current] = i

#This is what i remembered from the memory.


"""
## TIER 4 Recalls — Warm-Up Templates (5 min each)
Complete all 3 steps for each template. A recall is only complete when all 3 are answered.
  Step 1: Write the template from memory.
  Step 2: "The invariant this template maintains is: ___"
  Step 3: "If I changed [specific line] to [wrong version], it would fail because: ___"

If you cannot write the template in 3 min → write "FAILED" and flag as Tier 2 for tomorrow.

"""
### Recall 1: Sliding Window (Variable size)

def slidingwindow(nums,k):

    left = 0
    
    countofzeros = 0

    best = 0

    for right in range(len(nums)):

        if nums[right] == 0:
            countofzeros += 1
        
        while right-left+1 > k:

            if nums[left] == 0:
                countofzeros -= 1
            left += 1
        best = max(best , right-left+1)
    
    return best

# Invariant: slidining window variable size

# If I changed updating best after window validity checked to befor, it would fail because: its will count the window not a valid one.

#Failed taken 6-7 mins to write whole.

"""
### Recall 2: Prefix Sum + Hash Map (560 style)

```python
# Write template from memory here
```

Invariant: ___
If I changed ___ to ___, it would fail because: ___

"""

def prefixsum(nums,k):

    seen = {0:1}

    prefix = 0

    count = 0

    for i in range(len(nums)):

        prefix += nums[i]

        needed = prefix - k 

        if needed in seen:
            count+=seen[needed]
        
        seen[prefix] = seen.get(prefix,0)+1

    return count


# Invariant: Prefix sum + hashmap

# If I changed seen[prefix] to seen[needed], it would fail because: the hash map store the required prefix not the current subarray prefix.


#Failed taken 4 mins to write whole.

## TIER 1 — Priority Revision (solve ALL 3 first — no skipping)

"""
## TIER 1 — Priority Revision (solve ALL 3 first — no skipping)

### 1. Make Sum Divisible by P (LC 
) — Medium ⚠️ USO STANDALONE — Write derivation proof above first

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

**Recovery questions (answer in comments before coding):**
1. What is `target = total % p` telling you?
2. What does `needed = (current - target) % p` find?
3. Why is `seen` initialized as `{0: -1}` and stores index, not count?

```python

"""

# Answer the 3 recovery questions here as comments first:
# 1. The target is the Remainder which tells if we remove the remainder then we can make the array divisible by p.
# 2.The needed find the remainder of current subarry.
# 3.seen is initialized with {0:-1} bcz if we get remainder at intaill element is dont initialize this then we going to iss the valid answer.Here we are storing index bcz we want the len of subarry not the count.


class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        totalsum = sum (nums)

        seen = {0:-1}

        target = totalsum % p

        if target == 0:
            return 0
        
        best = len(nums)

        prefix = 0

        for i in range(len(nums)):

            prefix += nums[i]

            current = prefix % p

            needed = (current-target) % p

            if needed in seen:

                best = min (best, i-seen[needed])
        
            seen[current] = i

        if best == len(nums):
            return -1
        else:
            return best
        
# Status: Hint
# Time taken: 40 min
# Tier: ___
# Time complexity: O(n) — single loop is iterating over all elements and only once.
# Space complexity: O(n) — used the dict data type 
# LC status: Accepted
# Pattern: Prefix sum + modulo varient
# Variant: 
# mistakes/confusion: (initailly i wa updating the current is needed in not found.) Now i undertood the derivation why we used but How it came still need to internelize.

"""
### 2. Range Sum Query - Immutable (LC 303) — Easy ⚠️ D30 UNVERIFIED — solve fresh, fill ALL fields

Day 30 had code written (brute + optimal both) but comment fields were blank.
Solve independently today from scratch. Do not look at D30 code first.
If you cannot solve it independently, mark Status: Hint.

Given an integer array `nums`, handle multiple queries of the following type:
Calculate the sum of elements of `nums` between indices `left` and `right` **inclusive**.

Implement the `NumArray` class:
- `NumArray(int[] nums)` — Initializes the object with the integer array `nums`.
- `int sumRange(int left, int right)` — Returns the sum of elements between `left` and `right`
  inclusive. Must be **O(1)** per query.

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
- At most 10^4 calls will be made to sumRange.

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) __init__ | O(?) sumRange — [justify each]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

"""

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
        

# Status: Independent
# Time taken: 20 min
# Tier: ___
# Time complexity: O(n) __init__ | O(1) sumRange — we are running a loop in init where as in sumrange we are just accesing two elements.
# Space complexity: O(n) — list is used to store the prefix sum of of each iteration.
# LC status: Accepted
# Pattern: prefix sum
# Variant: range sub query
# mistakes/confusion: Here i got all the solution including the brute force and the optimal but still not ingerited the why we intiallized the list with 0.

"""
### 3. K Divisible Elements Subarrays (LC 2261) — Medium ⚠️ Overdue since Jun 30

Given a **0-indexed** integer array `nums` and two positive integers `k` and `p`.

Return the number of **distinct** subarrays of `nums` which have **at most** `k` elements
that are divisible by `p`.

Two arrays are distinct if there exists some index `i` where `a[i] != b[i]`.

**Example 1:**
Input: nums = [2,3,3,2,2], k = 2, p = 2
Output: 6

**Example 2:**
Input: nums = [1,2,3,4], k = 4, p = 1
Output: 10
Explanation: All subarrays qualify (all elements divisible by 1). 4 elements → 10 distinct subarrays total.

**Constraints:**
- 1 <= nums.length <= 200
- 1 <= p, k <= nums.length
- 1 <= nums[i] <= 200

**Recovery note:** D29 — brute force was independent, optimal was hint-based.
Attempt brute force first independently. Then attempt optimal if you recall it.

```python
# Brute force solution (attempt independently first):
```

```python
# Optimal solution (only if recalled from D29 — mark Hint if needed reference):
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) brute | O(?) optimal — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
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

            divisiblebyp = 0

            out=[]

            for j in range(i,len(nums)):

                if nums[j] % p ==0:
                    divisiblebyp +=1
                
                if divisiblebyp > k:
                    break
                out.append(nums[j])

                seen.add(tuple(out))
        return len(seen)


# Status: Independent 
# Time taken: 20 min
# Tier: ___
# Time complexity: O(n^2) brute | O(?) optimal- only brute force solved and used nested loop there for n^2
# Space complexity: O(n) — used set and list 
# LC status: Accepted
# Pattern: Nested loop
# Variant: ___
# mistakes/confusion: Na 

## TIER 2 — Revision (3 problems — most overdue picked)

"""
### 4. Two Sum (LC 1) — Easy [OVERDUE since Jun 27]

Given an array of integers `nums` and an integer `target`, return the **indices** of the two
numbers that add up to `target`. You may assume that exactly one solution exists. You may not
use the same element twice. Return the answer in any order.

**Example 1:**
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

**Example 2:**
Input: nums = [3,2,4], target = 6
Output: [1,2]

**Example 3:**
Input: nums = [3,3], target = 6
Output: [0,1]

**Constraints:**
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

```python
# Your solution here
```

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}

        for i in range(len(nums)):

            needed = target - nums[i]

            if needed in seen:
                return [seen[needed],i]
 
            seen[nums[i]] = i

# Status: Independent
# Time taken: 15 min
# Tier: ___
# Time complexity: O(n) — we have used loop to iterate over each element 
# Space complexity: O(n) — used hash map to store current element with its index.
# LC status: Accepted 
# Pattern: complement lookup
# Variant: ___
# mistakes/confusion: Na

"""
### 5. Valid Perfect Square (LC 367) — Easy [OVERDUE since Jun 27]

Given a positive integer `num`, return `true` if `num` is a perfect square, or `false` otherwise.
Do **not** use any built-in library function such as `sqrt`.

**Example 1:**
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16, and 4 is an integer.

**Example 2:**
Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14, and 3.742 is not an integer.

**Constraints:**
- 1 <= num <= 2^31 - 1

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
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 0
        right = num

        while left <= right :

            mid = (right + left) // 2

            sqrt = mid * mid

            if sqrt == num:
                return True
            elif sqrt > num:
                right = mid - 1
            else :
                left = mid + 1
        return False 
    
# Status: Independent
# Time taken: 15 min
# Tier: ___
# Time complexity: O(logn) — which makes search space half with each iteration 
# Space complexity: O(1) — used variables with interget num.
# LC status: Accepted
# Pattern: Binary search
# Variant: ___
# mistakes/confusion:NA

"""
### 6. Ransom Note (LC 383) — Easy [OVERDUE since Jul 1]

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed
by using the letters from `magazine` and `false` otherwise. Each letter in `magazine` can only
be used **once**.

**Example 1:**
Input: ransomNote = "a", magazine = "b"
Output: false

**Example 2:**
Input: ransomNote = "aa", magazine = "ab"
Output: false

**Example 3:**
Input: ransomNote = "aa", magazine = "aab"
Output: true

**Constraints:**
- 1 <= ransomNote.length, magazine.length <= 10^5
- ransomNote and magazine consist of lowercase English letters.

```python
# Your solution here
```
"""
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        seen={}

        for i in ransomNote:
            seen[i]=seen.get(i,0)+1
        seen2={}

        for j in magazine:
            seen2[j]=seen2.get(j,0)+1
        
        for k in range(len(ransomNote)):

            if ransomNote[k] not in seen2:
                return False
            elif seen[ransomNote[k]] > seen2[ransomNote[k]]:
                return False
        return True

# Status: Independent
# Time taken: 15 min
# Tier: ___
# Time complexity: O(n) — iterating only one time on each elemets
# Space complexity: O(n) — Hash map is used to store key value pair
# LC status: Accepted 
# Pattern: Hash Map
# Variant: ___
# mistakes/confusion: Na

## TIER 3 — Revision (2 problems — due Jul 4, pulling 2 days early)

"""
### 7. First Bad Version (LC 278) — Easy [Due Jul 4]

You are a product manager and currently leading a team to develop a new product. Unfortunately,
the latest version of your product fails the quality check. Since each version is developed based
on the previous version, all the versions after a bad version are also bad.

You are given `n` versions `[1, 2, ..., n]` and a provided API `isBadVersion(version)` which
returns whether version is bad. Find the **first bad version** while minimizing API calls.

**Example 1:**
Input: n = 5, bad = 4
Output: 4
Explanation: isBadVersion(3) → false, isBadVersion(4) → true. First bad version is 4.

**Example 2:**
Input: n = 1, bad = 1
Output: 1

**Constraints:**
- 1 <= bad <= n <= 2^31 - 1

```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# Your solution here
"""
def isBadVersion(num):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0

        right = n

        badversion =0

        while left <= right:

            mid = (right+left)//2

            res = isBadVersion(mid)

            if res == True:
                badversion = mid
                right = mid - 1
            else:
                left = mid + 1
        return badversion

# Status: Independent
# Time taken: 20 min
# Tier: ___
# Time complexity: O(logn) — With each iteration search space becomes half
# Space complexity: O(1) — varibels used with sinle integers
# LC status: Accepted
# Pattern: Binary search
# Variant: ___
# mistakes/confusion: Na
      
"""
### 8. Find Peak Element (LC 162) — Medium [Due Jul 4]

A peak element is an element that is **strictly greater** than its neighbors.

Given a **0-indexed** integer array `nums`, find a peak element and return its index. If the array
contains multiple peaks, return the index of **any** of the peaks.

You may imagine that `nums[-1] = nums[n] = -∞`. An element is always greater than a neighbor
outside the array boundary.

You must write an algorithm that runs in **O(log n)** time.

**Example 1:**
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and the function should return index 2.

**Example 2:**
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Either index 1 (value 2) or index 5 (value 6) is acceptable.

**Constraints:**
- 1 <= nums.length <= 1000
- -2^31 <= nums[i] <= 2^31 - 1
- nums[i] != nums[i + 1] for all valid i.

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
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        while left < right:

            mid = (right+left)//2

            if nums[mid] > nums[mid+1]:
                right = mid
            else :
                left = mid + 1
        return right
    
# Status: Independent
# Time taken: 15 min
# Tier: ___
# Time complexity: O(logn) — with each iteration search space reduced to half
# Space complexity: O(1) — varibales used with integer data
# LC status: Accepted
# Pattern: Binary search
# Variant: ___
# mistakes/confusion: Na

## New Problems (1 problem — Phase 1 must-solve gap-fill)

"""
### 9. Longest Consecutive Sequence (LC 128) — Medium [Phase 1 must-solve — FIRST ATTEMPT]

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
- O(n) time required — sorting-based solutions do not meet the constraint.

```python
# Brute force first (words only — do not code the brute force, just state the approach):
# Brute force: ___
# Why brute force fails: ___

# Optimal solution:
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
        seen = set()
        best=0

        for i in nums:

            seen.add(i)

        for num in seen:

            if num-1 not in  seen:
                number = num
                length = 1

                while number + 1 in seen:
                    number +=1
                    length +=1
                best = max(best,length)
        return best
                
# Status: Hints
# Time taken: 40 min
# Tier: ___
# Time complexity: O(n) — iterating each elemet only once
# Space complexity: O(1) — 
# LC status: Accepted 
# Pattern: Hash set 
# Variant: sequnce Expansion 
# mistakes/confusion: The pattern and varient seen in the video solution.




 
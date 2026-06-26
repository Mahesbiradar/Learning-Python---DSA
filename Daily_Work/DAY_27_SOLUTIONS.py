## TIER 4 Recalls (5 min each — write from memory, no notes)

"""
### Recall 1 — Frequency Hashing
Write the full Frequency Hashing template from memory.
Include: dict setup, count pass, answer pass.

```python
# Write here from memory


```
Time taken: ___ min | Result: Recalled clean / Struggled (→ Tier 2)

---

"""

def frequncy_hashing(s):

    seen={}
    
    for i in s:
        seen[i]=seen.get(i,0)+1
    
    for j in range(len(s)):

        if seen[s[i]]==1:
            return j

# Time taken: 5 min | Result: Recalled clean

"""
### Recall 2 — Complement Lookup
Write the Complement Lookup template from memory.
Include: seen dict, check-then-store order, what gets stored as key vs value.

```python
# Write here from memory


```
Time taken: ___ min | Result: Recalled clean / Struggled (→ Tier 2)

---
"""

def compliment_lookup(nums,target):

    seen={}

    for i in range(len(nums)):

        nedded=target-nums[i]

        if nedded in seen: 
            return [seen[nedded],i]
        
        seen[nums[i]]=i

# Time taken: 5 min | Result: Recalled clean


"""
## PATTERN WARM-UP — Two Pointers: Maximize/Minimize (5 min, before Tier 1)

This was introduced yesterday. Write the template from memory before touching any problems.

```python
def two_pointer_maximize(height):
    # Write from memory

```
Key rules (recite before writing):
- Start: left = 0, right = len - 1
- Value = ________________
- Move the ________ side inward
- Stop when ________________

If you cannot write it in 3 min → re-read yesterday's concept block in DAY_26.md, then continue.

---
"""
    
def two_pointers(nums):

    left=0
    right=len(nums)-1
    best=0

    while left<right:

        value=min(nums[left],nums[right])

        area=value*(right-left)

        if nums[left]<nums[right]:
            left+=1
        else: 
            right-=1
        
        best= max(best,area)
    return best

# Key rules (recite before writing):
# - Start: left = 0, right = len - 1
# - Value = min(nums[left],nums[right])*(Right-left)
# - Move the lower side inward
# - Stop when left  => right.

"""
## PATTERN WARM-UP — Prefix Sum Modulo (3 min, before LC 974)

Two versions exist — pick the right one:

| Version | Seen init | What it answers |
|---------|-----------|----------------|
| EXISTS (LC 523) | `{0: -1}` | Is there a subarray with sum divisible by k? (True/False) |
| COUNT (LC 974) | `{0: 1}` | How many subarrays have sum divisible by k? (int) |

The sign of `remainder` matters — if negative, add k before using:
`if remainder < 0: remainder += k`

"""

#Second Problem Count (lC 974)

"""
### T1-1. Guess Number Higher or Lower — LC 374
Easy | Binary Search

Solve completely blind — no looking at yesterday's code, no template.

We play a guessing game. I pick a number from 1 to n.
Each call to `guess(num)` returns:
  -1  → your guess is higher than the answer
   1  → your guess is lower than the answer
   0  → you guessed correctly

Find the number I picked.

```
# The guess API is already defined:
# def guess(num: int) -> int:

n=10, pick=6  →  6
n=1,  pick=1  →  1
n=2,  pick=2  →  2
```

Constraints: 1 <= n <= 2^31-1. 1 <= pick <= n.

What to fix from yesterday:
- Loop condition: `left <= right`
- Adjust correctly: if guess(mid)==-1 → high, if ==1 → low, if ==0 → return

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___
```
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

def guess(nums):

    pass

def guessNumber(n: int) -> int:

        left=0
        right=n

        while left<=right:

            mid=(right+left)//2

            pick=guess(mid)

            if pick == 0:
                return mid
            elif pick==-1:
                right=mid-1
            elif pick==1:
                left=mid+1

# Status: Independent
# Time taken: 25 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Binary search
# Variant: 
# mistakes/confusion: Intially unconciouslly i have written mid formula mid=(right-left)//2  and the loop condition was left<right.

#Now test cases equired bcz i have the write the one more function here and i have submitted in LC.

"""
### T1-2. Peak Index in a Mountain Array — LC 852
Medium | Binary Search

Solve in O(log n) this time. Not O(n). The O(n) version is wrong for this problem.

A mountain array increases to a peak then strictly decreases.
Return the index of the peak element.

```
arr = [0,1,0]      →  1
arr = [0,2,1,0]    →  1
arr = [0,10,5,2]   →  1
arr = [3,4,5,1]    →  2
arr = [24,69,100,99,79,78,67,36,26,19]  →  2
```

Constraints: 3 <= arr.length <= 10^5. 0 <= arr[i] <= 10^6. Guaranteed mountain.

What to fix from yesterday:
- Loop: `while left < right` (NOT `<=`)
- If arr[mid] > arr[mid+1] → peak is AT or LEFT of mid → `right = mid`
- If arr[mid] < arr[mid+1] → peak is RIGHT of mid → `left = mid + 1`
- Return: `return left` (NOT `return mid`)

Write the full O(log n) solution cold. No hints.

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___
```
"""
def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left=0
        right=len(arr)-1

        while left<right:

            mid=(left+right)//2

            if arr[mid]>arr[mid+1]:
                right=mid
            elif arr[mid]<arr[mid+1]:
                left=mid+1
        return left

# Status: Independent
# Time taken: 15 min
# Tier: ___
# Time complexity: O(log n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Binary search
# Variant: NA
# mistakes/confusion: After Dry run i come to know to set the loop condition to < instead of <=

"""
### T1-3. Subarray Sums Divisible by K — LC 974
Medium | Prefix Sum

Retry completely blind — no looking at yesterday's template. Use the warm-up above.

Given integer array nums and integer k, return the number of non-empty subarrays
that have a sum divisible by k.

```
nums=[4,5,0,-2,-3,1], k=5   →  7
nums=[5], k=9                →  0
nums=[7,3,-5,6,-9], k=3     →  4
```

Constraints: 1 <= nums.length <= 3×10^4. -10^4 <= nums[i] <= 10^4. 2 <= k <= 10^4.

Edge cases to test:
- Negative numbers in array (remainder goes negative → add k)
- Single element divisible by k
- All elements 0

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___
```
"""

def subarraysDivByK(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen={0:1}

        count=0
        prefix=0

        for i, num in enumerate(nums):

            prefix+=num

            remainder= prefix % k

            if remainder<0:
                remainder+=k
            
            if remainder in seen:
                count+=seen[remainder]

            seen[remainder]=seen.get(remainder,0)+1
        return count



# Status:Hint
# Time taken: 40 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted 
# Pattern: Prefix sum
# Variant: modulo varient
# mistakes/confusion: Basically i solved with prev memory not with intution so i made mistake for see[prefix]=seen.get(prefix,0)+1 the i saw video on solution.



## TIER 2 — Revision (3 problems — identify the pattern yourself)


"""
### T2-1. LC 26
Easy

Given an integer array nums sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once.
Return the number of unique elements.

The first k elements of nums must contain the unique elements in the original order.
It does not matter what you leave beyond the first k elements.

```
[1,1,2]             →  2  (nums becomes [1,2,_])
[0,0,1,1,1,2,2,3,3,4]  →  5  (nums becomes [0,1,2,3,4,_,_,_,_,_])
```

Constraints: 1 <= nums.length <= 3×10^4. -100 <= nums[i] <= 100. Sorted.

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___
```
---
"""

def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        write=1

        for i in range(1,len(nums)):

            if nums[i]!=nums[write-1]:
                nums[write]=nums[i]
                write+=1
        return write

# Status: Independent
# Time taken: 15 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Write Pointer
# Variant: Inplace owerite
# mistakes/confusion: Na

"""
### T2-2. LC 278
Easy

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions
after a bad version are also bad.

You have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether version is bad.
Implement a function to find the first bad version. Minimize the number of API calls.

```
# The isBadVersion API is defined:
# def isBadVersion(version: int) -> bool:

n=5, bad=4  →  4  (versions: [good, good, good, bad, bad])
n=1, bad=1  →  1
```

Constraints: 1 <= bad <= n <= 2^31-1.

```python
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

def isBadVersion(mid):
     pass

def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left=0
        right=n

        while left<right:

            mid=(left+right)//2

            result=isBadVersion(mid)

            if result==False:
                left=mid+1
            elif result==True:
                right=mid
        return left

# Status: Independent
# Time taken: 15 min
# Tier: ___
# Time complexity: O(log n)
# Space complexity: O(1)
# LC status: Accepted 
# Pattern: Binary search
# Variant: Lower Bound.
# mistakes/confusion: Intially the while condition was <= the after dry run come to know this will end with infinite loop.

"""
### T2-3. LC 162
Medium

A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index of any of them.

You may imagine that nums[-1] = nums[n] = -∞ (elements outside are minus infinity).
Solve in O(log n) time.

```
nums=[1,2,3,1]   →  2  (nums[2]=3 is a peak)
nums=[1,2,1,3,5,6,4]  →  1 or 5 (both valid peaks)
nums=[1]          →  0
```

Constraints: 1 <= nums.length <= 1000. -2^31 <= nums[i] <= 2^31-1. nums[i] ≠ nums[i+1].

```python
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

def findPeakElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1

        while left<right:

            mid=(left+right)//2

            if nums[mid]<nums[mid+1]:
                left=mid+1
            else:
                right=mid
        return left
        

# Status: Independent
# Time taken: 20 min
# Tier: ___
# Time complexity: O(log n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Binary search
# Variant: upper bound
# mistakes/confusion: intially i was retunring mid.


## TIER 3 — Revision (2 problems — identify the pattern yourself)


"""
### T3-1. LC 167
Medium

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Return the indices of the two numbers [index1, index2] (1-indexed).

The tests are generated such that there is exactly one solution.
You may not use the same element twice.
Use only constant extra space.

```
[2,7,11,15], target=9    →  [1,2]
[2,3,4], target=6        →  [1,3]
[-1,0], target=-1        →  [1,2]
[1,3,4,5,7,11], target=9 →  [3,5]
```

Constraints: 2 <= numbers.length <= 3×10^4. Exactly one solution.

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___
```
"""


def twoSum(numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=0
        right=len(numbers)-1

        while left<right:

            num=numbers[left]+numbers[right]

            if num==target:
                return [left+1,right+1]
            elif num>target:
                right-=1
            else:
                left+=1

# Status: Independent
# Time taken: 10 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Two pointers
# Variant: 
# mistakes/confusion: NA


"""
### T3-2. LC 1207
Easy

Given an array of integers arr, return true if the number of occurrences of each value
in the array is unique (no two values have the same occurrence count), or false otherwise.

```
[1,2,2,1,1,3]               →  True   (1→3, 2→2, 3→1 — all unique counts)
[1,2]                        →  False  (both appear once)
[-3,0,1,-3,1,1,1,-3,10,0]   →  True
[3,3,3,3,3,3]               →  True   (only one value)
```

Constraints: 1 <= arr.length <= 1000. -1000 <= arr[i] <= 1000.

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___
```
"""
def uniqueOccurrences(arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen={}
        for i in arr:
            seen[i]=seen.get(i,0)+1
        
        seen_set=set()

        for key,value in seen.items():
            if value in seen_set:
                return False
            seen_set.add(value)
        return True      

# Status: Independent
# Time taken: 10 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(n)
# LC status: Accepted.
# Pattern: Frquncy Hashing 
# Variant:
# mistakes/confusion: Na

## New Problems (2 problems — identify the pattern yourself)

# Both problems are Medium difficulty. Apply full SOP — dry run before coding.

"""
### N1. Max Number of K-Sum Pairs — LC 1679
Medium

You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k
and remove them from the array.

Return the maximum number of operations you can perform on the array.

```
nums=[1,2,3,4], k=5          →  2   (remove [1,4] first, then [2,3])
nums=[3,1,3,4,3], k=6        →  1   (remove [3,3])
nums=[1,1,1,1], k=2          →  2
nums=[2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2], k=3  →  5
```

Constraints: 1 <= nums.length <= 10^5. 1 <= nums[i] <= 10^9. 1 <= k <= 10^9.

Brute force hint (words only, don't code): check every pair → O(n²). Too slow for 10^5.
Think: can you sort and then use two ends?

```python
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

def maxOperations(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        count=0
        sorted_nums=sorted(nums)

        while left<right:

            num=sorted_nums[left]+sorted_nums[right]

            if num==k:
                left+=1
                right-=1
                count+=1
            elif num>k:
                right-=1
            else:
                left+=1
        return count
print(maxOperations(nums=[1,2,3,4], k=5 ))
print(maxOperations(nums=[3,1,3,4,3], k=6  ))
print(maxOperations(nums=[1,1,1,1], k=2  ))
print(maxOperations(nums=[2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2], k=3 ))

# Status: Independent
# Time taken: 30 min
# Tier: ___
# Time complexity: O(m+logn)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Two pointers
# Variant: Not sure
# mistakes/confusion: No confusion with given hint above as for sorted arrey then i got with dry run but not able to implement the brute Force.

"""
### N2. Minimize Maximum Pair Sum in Array — LC 1877
Medium

The pair sum of a pair (a, b) is equal to a + b.
The maximum pair sum is the largest pair sum in a list of pairs.
Given an array nums of even length n, pair up the elements such that:
- Each element belongs to exactly one pair
- The maximum pair sum is minimized

Return the minimized maximum pair sum after optimally pairing up the elements.

```
nums=[3,5,2,3]       →  7    (pairs: [3,3] and [2,5] → max pair sum is max(6,7)=7)
nums=[3,5,4,2,4,6]   →  8    (pairs: [2,6],[3,5],[4,4] → max is 8)
nums=[1,2]           →  3
nums=[1,1,1,1]       →  2
```

Constraints: n is even. 2 <= nums.length <= 10^5. 1 <= nums[i] <= 10^5.

Brute force hint (words only): try every possible pairing → exponential. Too slow.
Think: what if you sorted the array? What would the optimal pairing look like?

```python
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

def minPairSum(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1

        sorted_seen=sorted(nums)
        maximum_pair=0

        while left<right:

            num=sorted_seen[left]+sorted_seen[right]
            left+=1
            right-=1
            maximum_pair=max(maximum_pair,num)
        return maximum_pair

# Status: Independent
# Time taken: 20 min
# Tier: ___
# Time complexity: O(m+logn)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Two Pointers
# Variant: ___
# mistakes/confusion: NA but not able to think the brute Force solution.


#If i have not added the Testcases here for Print bcz all the solutions are submitted to LC and all are Accepted.

#Still i have not mentioned the Tiers you can assing based on the status and other parameters mentioned.
## TIER 4 Recalls (5 min each — write from memory, no notes)

"""
### Recall 1 — Running State (Kadane / min-max tracking)
Write the Best Time to Buy and Sell Stock template from memory.
Include: initial state, loop body, update order (check BEFORE updating min).

```python
# Write here from memory


```
Time taken: ___ min | Result: Recalled clean / Struggled (→ Tier 2)

---

"""

def running_state(nums):

    min_value=float('inf')
    max_value=float('-inf')
    max_profit=0

    for i in range(len(nums)):

        if nums[i]<min_value:
            min_value=nums[i]
        else:
            if nums[i]>max_value:
                max_value=nums[i]
            
            profit=max_value-min_value

            if profit>max_profit:
                max_profit=profit
    return max_profit

print(running_state([7,1,5,3,6,4]))
print(running_state([7,6,4,3,1]))

# Time taken: 7 min | Result: Recalled clean

"""
### Recall 2 — Prefix Sum (Pivot / equilibrium)
Write the Find Pivot Index template from memory.
Include: total sum, left_sum, update-after-compare rule.

```python
# Write here from memory

```
Time taken: ___ min | Result: Recalled clean / Struggled (→ Tier 2)

"""
def pivotindex(nums):

    left = 0

    totalsum = sum(nums)


    for i in range(len(nums)):

        right=totalsum-nums[i]-left

        if left==right:
            return i

        left+=nums[i]
    
    return -1

print(pivotindex([1,7,3,6,5,6]))
print(pivotindex([1,2,3]))
print(pivotindex([2,1,-1]))

# Time taken: 4 min | Result: Recalled clean

"""
## PATTERN WARM-UP — Prefix Sum Modulo (3 min before LC 974)

Fill this from memory before touching any problem. No notes.

**Two versions — which do you use when?**

| Version | `seen` init | Loop body: `seen` update | Use when |
|---------|------------|--------------------------|----------|
| EXISTS (LC 523) | `{0: ___}` | Only if NOT in seen | True/False |
| COUNT (LC 974, 560) | `{0: ___}` | Always add/increment | Count |

**The key mistake from D27:** you wrote `seen[prefix]` instead of `seen[remainder]`.
The KEY is always the **remainder**, not the prefix. Prefix changes every step. Remainder is what you store and look up.

"""
# | Version | `seen` init | Loop body: `seen` update | Use when |
# |---------|------------|--------------------------|----------|
# | EXISTS (LC 523) | `{0: -1}` | Only if NOT in seen | True/False |
# | COUNT (LC 974, 560) | `{0:1}` | Always add/increment | Count |

## TIER 1 — Priority Revision (solve before anything else)


"""
### T1-1. Subarray Sums Divisible by K — LC 974
Medium | Prefix Sum

Third attempt. Solve completely from scratch — no notes, no warm-up visible.
Close this out today.

Given integer array nums and integer k, return the number of non-empty subarrays
that have a sum divisible by k.

```
nums=[4,5,0,-2,-3,1], k=5   →  7
nums=[5], k=9                →  0
nums=[7,3,-5,6,-9], k=3     →  4
nums=[0,0,0,0,0], k=3       →  15
```

Constraints: 1 <= nums.length <= 3×10^4. -10^4 <= nums[i] <= 10^4. 2 <= k <= 10^4.

Before coding — say aloud:
1. I use `seen = {0: 1}` because I'm COUNTING
2. I store and look up `remainder = prefix % k`
3. Negative remainder → add k
4. I always update `seen[remainder]` after checking

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

        for i in range(len(nums)):

            prefix += nums[i]

            if prefix < 0:
                prefix += k
            reminder=prefix % k

            if reminder in seen:
                count+=seen[reminder]
            
            seen[reminder]=seen.get(reminder,0)+1
        return count


# Status: Independent
# Time taken: 12 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(n)
# LC status: Accepted
# Pattern: Prefix sum + Hashmap
# Variant: Modulo varient
# mistakes/confusion: NA

## TIER 2 — Revision (3 problems — identify the pattern yourself)

"""
### T2-1. LC 523
Medium

Given an integer array nums and integer k, return true if nums has a good subarray:
a contiguous subarray of length at least 2 whose sum is a multiple of k.

```
nums=[23,2,4,6,7], k=6    →  True   ([2,4] sums to 6)
nums=[23,2,6,4,7], k=6    →  True   (entire array sums to 42 = 7×6)
nums=[23,2,6,4,7], k=13   →  False
nums=[5,0,0,0], k=3       →  True   ([0,0] sums to 0)
nums=[0,1,0], k=2         →  False
```

Constraints: 1 <= nums.length <= 10^5. 0 <= nums[i] <= 10^9. 1 <= k <= 2^31-1.

This had a Wrong Answer on LC. Resubmit after fixing — see warm-up block above.
Key difference from LC 974: you return True/False, not count. Use `seen = {0: -1}`.

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

            reminder = prefix % k
           

            if reminder in seen:
                if i - seen[reminder] > 1:
                    return True
            else:
                seen[reminder]=i
        return False

# Status: Independent 
# Time taken: 25 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(n)
# LC status: Accepted 
# Pattern: Prefix sum + Hash Map
# Variant: Modulo
# mistakes/confusion: The mistake i made intially was i was varidating two conditions parrallay if reminder in seen and i-seen[remainder]>1 Therefor the else block was executing and index numbers are overwriding during LC Submission failded with some edgecases then realized.


"""
### T2-2. LC 744
Easy

You are given a characters array letters that is sorted in non-decreasing order,
and a character target.
Return the smallest character in letters that is strictly greater than target.
If such a character does not exist, return the first character in letters.

```
letters=["c","f","j"], target="a"   →  "c"
letters=["c","f","j"], target="c"   →  "f"
letters=["c","f","j"], target="d"   →  "f"
letters=["c","f","j"], target="j"   →  "c"  (wraps around)
letters=["x","x","y","y"], target="z"  →  "x"
```

Constraints: 2 <= letters.length <= 10^4. letters[i] is a lowercase English letter.
letters is sorted. letters has at least two different characters.

Solve in O(log n).

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
"""
class Solution(object):
    def nextGreatestLetter(self, letters, target):
     
      
        left=0
        right=len(letters)-1

        while left < right:

            mid=(left+right)//2

            if letters[mid] <= target:
                left=mid+1
            else:
                right=mid

                
        if letters[mid]>target:
            return letters[mid]
        else:
            return letters[0]

            """
#The above solution is earliers solution i Here one is i have not saved the >ans and the right=mid was wrong.


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left=0
        right=len(letters)-1
        ans=None

        while left <= right:

            mid=(left+right)//2

            if letters[mid] > target:
                ans= letters[mid]
                right=mid-1
            else:
                left=mid+1

                
        if ans== None:
            return letters[0]
        else:
            return ans

# Status:Hint
# Time taken: 20 min
# Tier: ___
# Time complexity: O(log n)
# Space complexity: O(1)
# LC status: Accepted 
# Pattern: Binary Searach
# Variant: ___
# mistakes/confusion: The brute Force with linear search was correct but optimal solution made mistake here you can see the wrong code 2edge cases were correct but 1 was failed.

"""
### T2-3. LC 11
Medium

You are given an integer array height of length n. There are n vertical lines drawn
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container that holds the most water.
Return the maximum amount of water the container can store.

```
height=[1,8,6,2,5,4,8,3,7]   →  49
height=[1,1]                   →  1
height=[4,3,2,1,4]            →  16
height=[1,2,1]                 →  2
```

Constraints: n >= 2. 0 <= height[i] <= 10^4.

Submit to LC after solving — this is still marked NA in STATUS.

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

def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        best = 0

        while left < right :

            area = min(height[left],height[right]) * (right-left)

            best=max(best,area)

            if height[left] > height[right]:
                right-=1
            else:
                left+=1
        return best


# Status: Independent
# Time taken: 12 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Two pointers
# Variant: Min/max Varient 
# mistakes/confusion: NA 

## TIER 3 — Revision (2 problems — identify the pattern yourself)

"""
### T3-1. LC 560
Medium

Given an array of integers nums and an integer k, return the total number of
subarrays whose sum equals to k.

```
nums=[1,1,1], k=2       →  2
nums=[1,2,3], k=3       →  2
nums=[1,-1,0], k=0      →  3
nums=[0,0,0,0], k=0     →  10
```

Constraints: 1 <= nums.length <= 2×10^4. -1000 <= nums[i] <= 1000.

This is Tier 3 — should be fast. If it takes >15 min, it drops to Tier 2.

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
def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen={0:1}

        prefix=0
        
        count=0

        for i in range(len(nums)):

            prefix+=nums[i]

            needed = prefix - k

            if needed in seen:
                count+=seen[needed]
            
            seen[prefix]=seen.get(prefix,0)+1
            
        return count

# Status: Independent
# Time taken: 25 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(n)
# LC status: Accepted 
# Pattern: Prefix sum + Hash Map
# Variant: 
# mistakes/confusion: intially i made misate prefix=nums[i] insterd prefix+=nums[i] Thats why the count returing 0 as the o/p

"""
### T3-2. LC 205
Easy

Given two strings s and t, return true if s is isomorphic to t.
Two strings are isomorphic if the characters in s can be replaced to get t,
preserving order. No two characters may map to the same character.
A character may map to itself.

```
s="egg", t="add"      →  True
s="foo", t="bar"      →  False
s="paper", t="title"  →  True
s="badc", t="baba"    →  False
```

Constraints: 1 <= s.length <= 5×10^4. t.length == s.length.

This is Tier 3 — should be fast. If it takes >15 min, it drops to Tier 2.

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

def isIsomorphic(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return  False

        seen1={}
        seen2={}

        for i in range(len(s)):

            if s[i] in seen1 and seen1[s[i]] != t[i]:
                return False
            else:
                seen1[s[i]] = t[i]
            
            if t[i] in seen2 and seen2[t[i]] != s[i]:
                return False
            else:
                seen2[t[i]] = s[i]
        return True


# Status: Independent
# Time taken: 15 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(n)
# LC status: Accepted
# Pattern: Frequncy Hashing
# Variant: ___
# mistakes/confusion: Na

## New Problems (2 problems — identify the pattern yourself)


"""
### N1. Binary Subarrays With Sum — LC 930
Medium

Given a binary array nums and an integer goal, return the number of non-empty
subarrays with a sum equal to goal.

A subarray is a contiguous part of the array.

```
nums=[1,0,1,0,1], goal=2   →  4
nums=[0,0,0,0,0], goal=0   →  15
nums=[1,0,1], goal=1       →  4
nums=[0,1,0,1,0], goal=2   →  4
```

Constraints: 1 <= nums.length <= 3×10^4. nums[i] is 0 or 1. 0 <= goal <= nums.length.

Note: This looks similar to LC 560 but the array is binary and contains many zeros.
Brute force: O(n²) nested loops. There is an O(n) solution.

"""

def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        prefix=0
        count=0
        seen={0:1}

        for i in range(len(nums)):

            prefix+=nums[i]

            needed= prefix - goal

            if needed in seen:
                count+=seen[needed]
            
            seen[prefix]=seen.get(prefix,0)+1
        return count

# Status: Independent
# Time taken: 15 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(n)
# LC status: Accepted
# Pattern: Prefix sum + Hash map
# Variant: 
# mistakes/confusion: Both the LC 560 AND 930 ARE SAME.


"""
### N2. Make Sum Divisible by P — LC 1590
Medium

Given an array of positive integers nums, remove the smallest subarray (possibly empty)
such that the sum of the remaining elements is divisible by p.
It is not allowed to remove the whole array.
Return the length of the smallest subarray that you need to remove, or -1 if impossible.

```
nums=[3,1,4,2], p=6     →  1   (remove [4], remaining sum = 6)
nums=[6,3,5,2], p=9     →  2   (remove [5,2], remaining sum = 9)
nums=[1,2,3], p=3       →  0   (sum = 6, already divisible)
nums=[1,2,3], p=7       →  -1  (impossible)
nums=[1000000000,1000000000,1000000000], p=3  →  0
```

Constraints: 1 <= nums.length <= 10^5. 1 <= nums[i] <= 10^9. 1 <= p <= 10^9.

Harder variant — think step by step:
Step 1: total_remainder = sum(nums) % p. If 0 → return 0.
Step 2: You need to find the shortest subarray whose sum ≡ total_remainder (mod p).
Step 3: Use prefix sum + hash map to find shortest such subarray.

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

# brute force solution
def Divisiblebyp(nums,p):
     

    totalsum=sum(nums)

    remain = totalsum % p

    if remain == 0:
        return 0
    
    n=len(nums)
    min_subarray=n

    for i in range(len(nums)):
         
         prefix=0
         
         for j in range(i,len(nums)):
              
              prefix+=nums[j]

              if (totalsum - prefix) % p == 0:
                   
                minlen=j-i+1

                min_subarray=min(min_subarray,minlen)
    return min_subarray if min_subarray < n else -1
              

print("This is Division")
print(Divisiblebyp([3,1,4,2], p = 6))
print(Divisiblebyp([6,3,5,2], p = 9))
print(Divisiblebyp([1,2,3], p = 3))
print(Divisiblebyp(nums=[1,2,3], p=7  ))
     
          
# Status:Hint
# Time taken: 30 min
# Tier: ___
# Time complexity: O(n^2)
# Space complexity: O(1)
# LC status:Not submitted
# Pattern: Nested Loop
# Variant: ___
# mistakes/confusion: As of now the optimal solution is not understood keep it for next day ill watch solution and then try to solve.





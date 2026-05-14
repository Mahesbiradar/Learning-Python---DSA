"""
## Concept Block Warm-Up

Before touching any problem file, write both templates from memory below.
If you cannot write them, open `DSA_DAILY_EXECUTION_SYSTEM.md`, read the relevant block, close it, then write here.

### Frequency Hashing Template (write from memory)

```python
# Write here without reading old code

s=[1,2,2,3,4,5]
seen={}
    for i in s:
        if i in seen:
            seen[i]+=1
        else:
            seen[i]=1
    
```

### Prefix Sum — Pivot Index Template (write from memory)

```python
# Write here without reading old code

nums=[1,3,5,6,7]
totalsum=sum(nums)
left=0

for i in range(len(nums)):

    right=totalsum-left-nums[i]

    if left==right:
        return i
    left+=nums[i]

return -1


```
Complexity check (fill before moving on):
- Frequency Hashing: Time = `O(n)`, Space = `O(n)`
- Prefix Sum (Pivot Index): Time = `O(n)`, Space = `O(1)`

---


"""

"""
## Problem 1: Valid Anagram

Topic: Frequency Hashing
Pattern: Build frequency maps, compare maps directly
Difficulty: Easy
LeetCode: [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)
Status target: Independent (no hints, no old code)

### Problem

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

Two strings are anagrams if they contain the same characters with the same frequencies.

### Examples

```
s = "anagram", t = "nagaram"  →  True
s = "rat",     t = "car"      →  False
```

### Constraints

- `1 <= len(s), len(t) <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters only.

### Required Approach Today

Build two frequency dictionaries. Compare them directly.

Forbidden today:
```python
# DO NOT use this pattern — it is O(k) string scan, not O(1)
if char not in t:
    ...
if char not in s:
    ...
```

Required today:
```python
# Build freq_s and freq_t using .get(x, 0) + 1
# Then compare: freq_s == freq_t
```

### Edge Cases to Test Before Submitting

```python
("anagram", "nagaram")  →  True
("rat", "car")          →  False
("", "")                →  True
("a", "ab")             →  False   # length differs
("aa", "a")             →  False   # same chars, different count
("ab", "ba")            →  True
```

### Brute Force Idea (write before optimized)

```
Sort both strings and compare.
Time: O(n log n)   Space: O(n)
```

### Optimized Idea (write before coding)

```
Build two frequency maps. Compare maps.
Time: O(n)   Space: O(n)
```

### Dry Run (trace for "rat" vs "car")

| Step | Action | freq_s | freq_t |
| --- | --- | --- | --- |
| Build freq_s | ... | | |
| Build freq_t | ... | | |
| Compare | ... | | |

### Solution

Write your solution in `DAY_08_SOLUTIONS.py`.

### Status

- [ ] Independent solve
- [ ] Hint used
- [ ] Solution viewed
- [ ] Unsolved

LeetCode result: `Accepted` / `Wrong Answer` / `Not submitted`
LeetCode submission link or problem number: 242

### Mistake Note

```
What went wrong (if anything):
What the fix was:
```

---

"""

#1.Brute force approch.

def isAnagram(s, t):
       
        if len(s)!=len(t):
            return False
        
        for i in s:

            count_s=0
            for j in s:
                if i==j:
                    count_s+=1
            count_t=0
            for k in t:
                if i==k:
                    count_t+=1
            
            if count_s!=count_t:
                return False 
        return True

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
print(isAnagram("a", "ab"))
print(isAnagram("ab", "a"))
print(isAnagram("ab", "ba"))
print(isAnagram("", ""))

# Status:Independent solve

# Time complexity: O(n^2)

# Space complexity:O(1)

# Mistakes/confusions:

# Pattern trigger:Membership and frequncy Check

# LeetCode submission status: Time Limit Exceeded due to brute Force.

#2.optimal approch (Using hashing)

def isanagram(s,t):
     
        if len(s)!=len(t):
            return False
        
        
        seen_s={}

        for i in s:
            if i in seen_s:
                seen_s[i]+=1
            else:
                seen_s[i]=1
        seen_t={}
        for j in t:
            if j in seen_t:
                seen_t[j]+=1
            else:
                seen_t[j]=1
        
        if seen_s!=seen_t:
            return False
        else: 
            return True

print(isanagram("anagram", "nagaram"))
print(isanagram("rat", "car"))
print(isanagram("a", "ab"))
print(isanagram("ab", "a"))
print(isanagram("ab", "ba"))
print(isanagram("", ""))        
        
# Status:Independent solve

# Time complexity: O(n)

# Space complexity:O(n)

# Mistakes/confusions:

# Pattern trigger:Membership and frequncy Check

# LeetCode submission status: Accepted.

"""
## Problem 2: Find Pivot Index

Topic: Prefix Sum
Pattern: Left sum equals right sum — compare before updating left_sum
Difficulty: Easy
LeetCode: [724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)
Status target: Independent (the logic is known — this is a correctness fix)

### Problem

Given an array `nums`, return the leftmost index where the sum of all elements strictly to the left equals the sum of all elements strictly to the right.

If no such index exists, return `-1`.

Elements directly at the index do not count toward either side.

### Examples

```
[1, 7, 3, 6, 5, 6]  →  3
  left of 3: 1+7+3 = 11
  right of 3: 5+6 = 11  ✓

[1, 2, 3]           →  -1
  no index where left == right

[2, 1, -1]          →  0
  left of 0: (empty) = 0
  right of 0: 1 + (-1) = 0  ✓
```

### Constraints

- `1 <= len(nums) <= 10^4`
- `-1000 <= nums[i] <= 1000`

### Critical Ordering Rule

```
Step 1: right_sum = total_sum - left_sum - nums[i]
Step 2: if left_sum == right_sum → return i
Step 3: left_sum += nums[i]      ← update AFTER comparing
```

Adding nums[i] to left_sum BEFORE comparing is the bug from before. It counts the current element in the left side, which is wrong.

### Edge Cases to Test Before Submitting

```python
[1, 7, 3, 6, 5, 6]   →   3
[1, 2, 3]             →  -1     ← must return -1, not 0
[2, 1, -1]            →   0
[0, 0, 0]             →   0
[-1, -1, -1, 0, 1, 1] →   0
[1]                   →   0     ← single element: both sides are 0
[]                    →  -1
```

"""
#Brute Force approch

def pivot_index(nums):

    for i in range(len(nums)):
        left=0

        for j in range(0,i):
            left+=nums[j]
        right=0
        for k in range(i+1,len(nums)):
            right+=nums[k]
        if left==right:
            return i
        
    return -1

# print(pivot_index([1, 7, 3, 6, 5, 6]))
# print(pivot_index([1, 2, 3] ))
# print(pivot_index([2, 1, -1]))
# print(pivot_index([0, 0, 0] ))
# print(pivot_index([-1, -1, -1, 0, 1, 1]))
# print(pivot_index([1]))
# print(pivot_index([]))  

# Status:Independent solve

# Time complexity: O(n^2)

# Space complexity:O(1)

# Mistakes/confusions:

# Pattern trigger:left & right sum /Two pointers

# LeetCode submission status: Time Limit Exceeded

#Optimal Solution: Here ill use Total sum by traversing all the elements or using the sum method.


def pivot_index(nums):

    totalsum=0
    for i in nums:
        totalsum+=i
    left=0

    for j in range(len(nums)):

        right=totalsum-left-nums[j]

        if left==right:
            return j
        
        left+=nums[j]
    return -1

print(pivot_index([1, 7, 3, 6, 5, 6]))
print(pivot_index([1, 2, 3] ))
print(pivot_index([2, 1, -1]))
print(pivot_index([0, 0, 0] ))
print(pivot_index([-1, -1, -1, 0, 1, 1]))
print(pivot_index([1]))
print(pivot_index([])) 

# Status:Independent solve

# Time complexity: O(n)

# Space complexity:O(1)

# Mistakes/confusions:

# Pattern trigger:left & right sum /Two pointers

# LeetCode submission status: Accepted
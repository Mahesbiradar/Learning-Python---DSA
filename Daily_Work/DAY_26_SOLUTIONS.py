## TIER 4 Template Recalls (5 min each — write from memory, no notes)

"""
## TIER 4 Template Recalls (5 min each — write from memory, no notes)

### Recall 1 — Sliding Window (Variable size)
Write the full variable-size sliding window template from memory.
Include: state setup, loop structure, shrink condition, answer update.
If you cannot write it in 3 min → mark as Tier 2 and add to revision pool.

```python
# Write here from memory



```
Time taken: ___ min | Result: Recalled clean / Struggled (→ Tier 2)

---

"""

def slidingwindow(nums,k):

    left=0
    countzeros=0
    best=0

    for right in range(len(nums)):

        if nums[right]==0:
            countzeros+=1

        while countzeros>k:

            if nums[left]==0:
                countzeros-=1
            left+=1
        
        best=max(best,right-left+1)
    return best

#Time taken: 10 min | Result: Recalled clean / Struggled (→ Tier 2)

#The Diffculty wan unleas i see the question on same pattern unable to recall the pattern.

"""
### Recall 2 — Prefix Sum + Hash Map (560 style)
Write the template from memory.
Include: seen dict initialization, prefix accumulation, needed calculation, count update.

```python
# Write here from memory



```
Time taken: ___ min | Result: Recalled clean / Struggled (→ Tier 2)

---

"""

def prefixsumandhashmap(nums,k):

    seen={0:1}
    prefix=0
    count=0

    for i in range(len(nums)):
        prefix+=nums[i]

        needed=prefix-k

        if needed in seen:
            count+=seen[needed]
        seen[prefix]=seen.get(prefix,0)+1
    return count

# Time taken: 5 min | Result:Struggled

#Found difficult withou Problems and still not sure the frequncy hashing part is correct or not.





#Brute Force SOLUTION Where each pair is Cheked to find the container with most water.

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
best=0

for i in range(len(height)):


    for j in range(i+1,len(height)):

        value=min(height[i],height[j])

        count=value*(j-i)

        if count>best:
            best=count

print(best)


### Template (fill after watching — write from memory)


def two_pointer_maximize(arr):
    left = 0
    right = len(arr) - 1
    best = 0

    while left < right:
        # calculate current value
        value = min(arr[left],arr[right]) * (right-left)

        best = max(best, value)

        # move the side that limits the value
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1

    return best


### Dry run — height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# Trace the first 4 steps manually before coding LC 11:

# | left | right | h[l] | h[r] | area | best | move |
# |------|-------|------|------|------|------|------|
# | 0 | 8 | 1 | 7 |min(1,7)*(8-0)=1*8=8 |8 |left |
# | 1| 8| 8|7 |min(8,7)*(8-1)=7*7=49 |49 |right |

# Expected final answer: 49


"""
## NEW CONCEPT 2 — Prefix Sum: Modulo Variant

This is what LC 523 needed. Your sliding window approach cannot solve this.

### Where to learn
Neetcode.io → search "Continuous Subarray Sum" → watch concept explanation only.
Stop before he codes. Then fill below.

### Trigger words
"multiple of k", "divisible by k", "subarray sum divisible",
"contiguous subarray sum is a multiple", "sum % k == 0"

### Mental model
If prefix[i] % k == prefix[j] % k,
then the subarray between j+1 and i has sum divisible by k.

Why? prefix[i] - prefix[j] = sum(j+1..i)
If both have same remainder when divided by k → their difference is divisible by k.

Store the EARLIEST index where each remainder was seen.
Check if gap between current index and stored index >= 2 (length at least 2).

### Why it exists
Sliding window cannot handle "divisible by k" — shrinking the window
doesn't give you control over divisibility.
Prefix + modulo converts the divisibility check into an equality check on remainders.

### Template

```python
def prefix_modulo(nums, k):
    seen = {0: -1}   # remainder 0 seen before index 0
    prefix = 0

    for i, num in enumerate(nums):
        prefix += num
        remainder = prefix % k

        if remainder in seen:
            if i - seen[remainder] >= 2:   # length must be at least 2
                return True
        else:
            seen[remainder] = i   # store EARLIEST index only — never update

    return False
```

### Dry run — nums = [23, 2, 4, 6, 7], k = 6

| i | num | prefix | prefix%6 | seen | in seen? | gap>=2? |
|---|-----|--------|----------|------|----------|---------|
| — | — | 0 | 0 | {0:-1} | — | — |
| 0 | 23 | 23 | 5 | | | |
| 1 | 2 | 25 | 1 | | | |
| 2 | 4 | 29 | 5 | | | |
| 3 | 6 | 35 | 5 | | | |

Expected: True (subarray [2,4] sums to 6, which is 1×6)

### Common mistakes
1. Updating seen[remainder] every time — only store EARLIEST index
2. Forgetting the gap >= 2 check — subarray must have length >= 2
3. Using sliding window — this problem cannot be solved with sliding window
4. Not initializing seen = {0: -1} — misses subarrays starting from index 0

---

"""

#Status Done:


## TIER 1 — Priority Revision (solve all 4 before moving to anything else)

"""

### T1-1. Container With Most Water — LC 11
Medium | Two Pointers — Maximize variant

You attempted this before and did not recognize the pattern.
Now you have the concept. Solve it using the template above.

Given n vertical lines where the ith line has height height[i].
Find two lines that form a container holding the most water.
Return the maximum amount of water the container can store.

Examples:
```
height = [1,8,6,2,5,4,8,3,7]  →  49
height = [1,1]                 →  1
height = [4,3,2,1,4]          →  16
height = [1,2,1]               →  2
```

Constraints: n >= 2. 0 <= height[i] <= 10^4.

Dry run before coding. Fill the table in the concept block above.
Submit to LC after local solve.

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: Two Pointers
# Variant: Maximize/minimize between ends
# mistakes/confusion:
```

"""

#Brute Force:using Nested Loop

def containerwithmostwater(nums):

    best=0

    for i in range(len(nums)):

        count=0

        for j in range(i+1,len(nums)):

            min_height=min(nums[i],nums[j])
            count=min_height*(j-i)

            best=max(best,count)
    return best

print(containerwithmostwater([1,8,6,2,5,4,8,3,7]))
print(containerwithmostwater([1,1]))

# Status: Independent
# Time taken:10 min
# Tier: ___not sure
# Time complexity: O(n^2)
# Space complexity: O(1)
# LC status:Not submitted
# Pattern: Nested loop 
# Variant: Maximize/minimize between ends
# mistakes/confusion: No

#optimal solution using the two pointers.

def containmaxwater(nums):

    left=0
    right=len(nums)-1
    best=0

    while left<right:

        area=(min(nums[left],nums[right]))*(right-left)

        best=max(best,area)

        if nums[left]<nums[right]:
            left+=1
        else:
            right-=1
    return best

print(containmaxwater([4,3,2,1,4]))
print(containmaxwater([1,2,1] ))
print(containmaxwater([1,1] ))

# Status: Independent
# Time taken:10min
# Tier: ___not sure
# Time complexity: O(n)
# Space complexity: O(1)
# LC status:Not submitted
# Pattern: Two pointers Maximun varient
# Variant: Maximize/minimize between ends
# mistakes/confusion: No

"""
### T1-2. Continuous Subarray Sum — LC 523
Medium | Prefix Sum — Modulo variant

Your previous attempt used sliding window — wrong approach.
Now you have the correct concept. Solve using the template above.

Given an integer array nums and integer k, return true if nums has a
"good subarray": length >= 2 AND sum is a multiple of k.

Examples:
```
nums = [23,2,4,6,7], k = 6   →  True  ([2,4] sums to 6)
nums = [23,2,6,4,7], k = 6   →  True  (entire array sums to 42 = 7×6)
nums = [23,2,6,4,7], k = 13  →  False
nums = [5,0,0,0], k = 3      →  True  ([0,0] sums to 0, 0 is multiple of 3)
```

Constraints: 1 <= nums.length <= 10^5. 0 <= nums[i] <= 10^9. 1 <= k <= 2^31-1.

Edge case to check: sum = 0 (0 is always a multiple of k).

"""

#Brute Force

def continuessubarraysumk(nums,k):


    for i in range(len(nums)):

        prefix=0

        for j in range(len(nums)):

            prefix+=nums[j]

            if prefix%k==0 and j-i+1>1:
                return True
    return False

print(continuessubarraysumk(nums = [23,2,4,6,7], k = 6))
print(continuessubarraysumk(nums = [23,2,6,4,7], k = 6))
print(continuessubarraysumk(nums = [5,0,0,0], k = 3))
print(continuessubarraysumk(nums = [23,2,6,4,7], k = 13 ))

# Status: Independent
# Time taken: 8 min
# Tier: T1
# Time complexity: O(n^2)
# Space complexity: O(1)
# LC status:Not submitted
# Pattern: Prefix Sum using nested loop
# Variant: Modulo
# mistakes/confusion:NA


#optimal solution using the prefix sum module varient.


def continuessubarraysumk(nums,k):

    prefix=0
    seen={0:-1}

    for i,num in enumerate(nums):

        prefix+=num

        remainder=prefix%k

        if remainder in seen:

            if i-seen[remainder]>1:
                return True
        else:
            seen[remainder]=i

    return False

print(continuessubarraysumk(nums = [23,2,4,6,7], k = 6))

# Status: Independent
# Time taken: 15 min
# Tier: T1
# Time complexity: O(n)
# Space complexity: O(1)
# LC status:Not submitted
# Pattern: Prefix Sum u
# Variant: Modulo
# mistakes/confusion:NA



"""
### T1-3. Guess Number Higher or Lower — LC 374
Easy | Binary Search — Standard

This failed on Day 22 and was never retried. Today close it out.

We play a game. I pick a number from 1 to n.
You call guess(num) API: returns -1 (too high), 1 (too low), 0 (correct).
Find the number I picked.

```python
# The guess API is already defined:
# def guess(num: int) -> int:

Examples:
n=10, pick=6  →  6
n=1,  pick=1  →  1
n=2,  pick=2  →  2
```

Constraints: 1 <= n <= 2^31-1. 1 <= pick <= n.

Use left <= right loop. Adjust based on guess() return value.

"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):


def guess(n,pick):


    if n==pick:
        return 0
    elif n>pick:
        return -1
    else:
        return 1


def guessNumber(n):
        """
        :type n: int
        :rtype: int
        """
        left=0
        right=n

        while left<=right:

            mid=(right+left)//2

            res=guess(mid)

            if res==0:
                return mid
            elif res==-1:
                right=mid-1
            elif res==1:
                left=mid+1

# Status:Hint
# Time taken:20 min
# Tier: T1
# Time complexity: O(N)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Binary Search
# Variant: Standard
# mistakes/confusion:NA

"""
### T1-4. Subarray Sum Equals K — LC 560
Medium | Prefix Sum — Prefix + Hash Map

Flagged shaky multiple times. Solve from scratch today — no looking at old code.

Given array nums and integer k, return count of subarrays whose sum equals k.

```
[1,1,1], k=2     →  2
[1,2,3], k=3     →  2
[1,-1,0], k=0    →  3
[0,0,0,0], k=0   →  5
```

Constraints: 1 <= nums.length <= 2×10^4. -1000 <= nums[i] <= 1000.

Mental trigger before coding: seen={0:1}, needed = prefix - k

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: Prefix Sum
# Variant: Prefix + Hash Map
# mistakes/confusion:
```

"""

#Brute Force: Here we can count prefix for each subarray using nested loop and with counter we can count the number of subarrays sum eaqul to k.

#optimal solution using prefix+Hash Map


def subarraysumequalsk(nums,k):

    count=0
    prefix=0
    seen={0:1}

    for i in range(len(nums)):

        prefix+=nums[i]
        needed=prefix-k

        
        if needed in seen:
            count+=seen[needed]
        
        seen[prefix]=seen.get(prefix,0)+1
    return count

print(subarraysumequalsk([1,1,1], k=2 ))
print(subarraysumequalsk([1,2,3], k=3  ))
print(subarraysumequalsk([0,0,0,0],k=0))
print(subarraysumequalsk([1,-1,0],0))

# Status: Independent
# Time taken:20m
# Tier: Not sure.
# Time complexity: O(n)
# Space complexity: O(n)
# LC status: Accepted
# Pattern: Prefix Sum
# Variant: Prefix + Hash Map
# mistakes/confusion:initally thougt to save seen[needed]=seen.get(needed,0)+1 but i was wrong got to know while Dry run.


## TIER 2 — Revision (3 problems — no pattern label, identify yourself)

"""
### T2-1. LC 1207
Easy

Given an array of integers arr, return true if the number of occurrences
of each value in the array is unique, or false otherwise.

```
[1,2,2,1,1,3]   →  True   (1 appears 3 times, 2 appears 2 times, 3 appears 1 time — all unique)
[1,2]            →  False  (both appear 1 time)
[−3,0,1,−3,1,1,1,−3,10,0]  →  True
```

Constraints: 1 <= arr.length <= 1000. -1000 <= arr[i] <= 1000.

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern:
# Variant:
# mistakes/confusion:

"""

def numberofoccurances(nums):

    seen={}

    for i in nums:
        seen[i]=seen.get(i,0)+1
    seen2=set()
    
    for key,value in seen.items():

        if value in seen2:
            return False
        
        seen2.add(value)
    return True

print(numberofoccurances([1,2,2,1,1,3]))
print(numberofoccurances([1,2]))
print(numberofoccurances([-3,0,1,-3,1,1,1,-3,10,0]))


# Status: Independent.
# Time taken:15 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(n)
# LC status: NA
# Pattern: Frequncy Hashing 
# Variant: 
# mistakes/confusion: Na

"""
### T2-2. LC 205
Easy

Given two strings s and t, return true if s is isomorphic to t.
Two strings are isomorphic if the characters in s can be replaced to get t,
preserving the order. No two characters may map to the same character.
A character may map to itself.

```
"egg", "add"    →  True
"foo", "bar"    →  False
"paper","title" →  True
"badc","baba"   →  False
```

Constraints: 1 <= s.length <= 5×10^4. t.length == s.length.

"""

def isomorphicstring(s,t):

    if len(s)!=len(t):
        return False

    seens={}

    seent={}


    for i in range(len(s)):


        if s[i] in seens and seens[s[i]]!=t[i]:
            return False
        else:
            seens[s[i]]=t[i]
        
        if t[i] in seent and seent[t[i]]!=s[i]:
            return False
        else:
            seent[t[i]]=s[i]
    
    return True


print(isomorphicstring("egg", "add" ))
print(isomorphicstring("foo", "bar"  ))
print(isomorphicstring("paper","title" ))
print(isomorphicstring("badc","baba"  ))

# Status: Independent.
# Time taken: 20 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(n)
# LC status: NA
# Pattern: Hash Map 
# Variant:
# mistakes/confusion:


"""
### T2-3. LC 852
Medium

You may treat this as a sorted-then-unsorted structure.
Given a mountain array arr (values increase to a peak then decrease),
return the index of the peak element.

Solve in O(log n) time this time. Not O(n).

```
arr = [0,1,0]      →  1
arr = [0,2,1,0]    →  1
arr = [0,10,5,2]   →  1
arr = [3,4,5,1]    →  2
```

Constraints: 3 <= arr.length <= 10^5. 0 <= arr[i] <= 10^6. Guaranteed mountain.

Hint trigger: if arr[mid] > arr[mid+1] → peak is at mid or left → right = mid
              if arr[mid] < arr[mid+1] → peak is right of mid → left = mid+1
              when left == right → that is the peak

"""

def mountainarray(nums):

    left=0
    right=len(nums)-1


    while left<right:

        mid=(left+right)//2
     

        if nums[mid]>nums[mid+1]:
            right=mid
        if nums[mid]<nums[mid+1]:
            left=mid+1   
    return left


print(mountainarray([0,1,0]))
print(mountainarray([0,2,1,0] ))
print(mountainarray([0,10,5,2]))
        


# Status: hint
# Time taken: 40 min
# Tier: ___
# Time complexity: O(log n)
# Space complexity: O(1)
# LC status: NA
# Pattern: binary search
# Variant:
# mistakes/confusion:I was stuck bcz i was returning the mid instaed of left.


## TIER 3 — Revision (2 problems)


"""
### T3-1. LC 27
Easy

Given integer array nums and integer val, remove all occurrences of val in-place.
Return the number of elements that are not equal to val.
The order of remaining elements does not matter.

```
[3,2,2,3], val=3   →  2  (first 2 elements are [2,2])
[0,1,2,2,3,0,4,2], val=2  →  5 (first 5 elements are [0,1,3,0,4])
```

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern:
# Variant:
# mistakes/confusion:

"""

def removealloccurances(nums,val):

    write=0

    for i in range(len(nums)):

        if nums[i]!=val:
            nums[write]=nums[i]
            write+=1
        
    
    return write,nums

print("removealloccurances")

print(removealloccurances([3,2,2,3], val=3 ))
print(removealloccurances([0,1,2,2,3,0,4,2], val=3 ))
print(removealloccurances([3,2,2,3], val=3 ))


# Status: Independent.
# Time taken: 25 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: NA
# Pattern: Write pointer
# Variant:
# mistakes/confusion: the second edge case showing output as 5 and i was confusd for more than 15min bcz its wrong its 5 instaed 7 here the question asking the return the number of non val elements.

"""
### T3-2. LC 167
Medium

Given a 1-indexed array of integers numbers sorted in non-decreasing order,
find two numbers that add up to a specific target.
Return their indices as [index1, index2] (1-indexed).
Use only constant extra space.

```
[2,7,11,15], target=9   →  [1,2]
[2,3,4], target=6       →  [1,3]
[-1,0], target=-1       →  [1,2]
```

Constraints: 2 <= numbers.length <= 3×10^4. Exactly one solution exists.

"""

def twosum(nums,target):

    left=0
    
    right=len(nums)-1

    while left<right:

        sumlr=nums[left]+nums[right]

        if sumlr==target:
            return [left+1,right+1]
        elif sumlr>target:
            right-=1
        else:
            left+=1
print(twosum([2,7,11,15], target=9 ))
print(twosum([2,3,4], target=6))
print(twosum([-1,0], target=-1))


# Status: Independent
# Time taken: 10 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: NA
# Pattern: Two pointer 
# Variant: 
# mistakes/confusion: NA

## NEW PROBLEM — Second problem for today's new concept (1 problem)


"""
### N1. Subarray Sums Divisible by K — LC 974
Medium | Same concept as LC 523 — practice the modulo variant again

Given integer array nums and integer k, return the number of non-empty subarrays
that have a sum divisible by k.

```
nums=[4,5,0,-2,-3,1], k=5   →  7
nums=[5], k=9                →  0
```

Constraints: 1 <= nums.length <= 3×10^4. -10^4 <= nums[i] <= 10^4. 2 <= k <= 10^4.

Difference from LC 523: return COUNT of subarrays, not just True/False.
Same core idea: remainder = prefix % k. But now use frequency map, not just existence check.

Mental trigger:
```

"""

#brute force.

def subarraysumdivide(nums,k):

    count=0

    for i in range(len(nums)):

        prefix=0

        for j in range(i,len(nums)):

            prefix+=nums[j]

            if prefix < 0:
                prefix+=k
            
            if prefix % k ==0:
                count+=1
    return count


print(subarraysumdivide([4,5,0,-2,-3,1], k=5 ))
print(subarraysumdivide(nums=[5], k=9  ))


#optimal solution using the prefixsum+ modulo varienet


def subarraysumdivide(nums,k):

    seen={0:1}

    count=0

    prefix=0


    for i , num in enumerate(nums):

        prefix+=num

        reminder=prefix % k

        if reminder < 0:
            reminder+=k

      
        count+=seen.get(reminder,0)
        
        seen[reminder]=seen.get(reminder,0)+1

    return count


print(subarraysumdivide([4,5,0,-2,-3,1], k=5 ))
print(subarraysumdivide(nums=[5], k=9  ))


# Status:Hint (as you have given the template itslef in the probelms so i seen that and solved.)
# Time taken: 15 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(n)
# LC status: Na
# Pattern: Prefix Sum
# Variant: Modulo
# mistakes/confusion: 




#Final concultion of the the Tier model in not ingerite like for each solution how can i assing the tier i dont know.  


#The modulo varinet is little bit undrstand the entire Seen={0:1} or seen={0:-1} these intutions and not inherited conceptually i can solve but that is from memory not from the intution.



        


                


            









        

        



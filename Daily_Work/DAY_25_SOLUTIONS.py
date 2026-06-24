## Session 1 — Prefix Sum + All Subarray Problems

"""
These are the highest priority because they contain the most concept-heavy logic.

### 1. Running Sum of 1D Array — LC 1480

**Pattern:** Prefix Sum
**Recall trigger:** `prefix[i] = prefix[i-1] + nums[i]`

Tests:

```python
[1,2,3,4]          # [1,3,6,10]
[3,1,2,10,1]       # [3,4,6,16,17]
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---  """
def runningsum(nums):
    
   output=[nums[0]]
   for i in range(1,len(nums)):
       output.append(nums[i]+output[i-1])
   

   return output

print(runningsum([1,2,3,4]))

#Status: independent.
#LC: Accepted.

"""
### 2. Find Pivot Index — LC 724

**Pattern:** Prefix Sum
**Recall trigger:** `right_sum = total - left_sum - current`

Tests:

```python
[1,7,3,6,5,6]      # 3
[1,2,3]             # -1
[2,1,-1]            # 0
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""

#Brute Force.
class Solution(object):
    def pivotIndex(self, nums):
        leftsum=0
        total_sum=sum(nums)

        for i in range(len(nums)):

            rightsum=total_sum-leftsum-nums[i]

            if leftsum==rightsum:
                return i
            leftsum+=nums[i]
        return -1
    
#Status: independent.

#LC:accepted.

"""
### 3. Find Highest Altitude — LC 1732

**Pattern:** Running Prefix Sum

Tests:

```python
[-5,1,5,0,-7]       # 1
[-4,-3,-2,-1,4,3,2] # 0
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt_gain=0
        high_alt=0

        for i in gain:
            alt_gain+=i

            if alt_gain>high_alt:
                high_alt=alt_gain
        return high_alt
    

#Status: independent.

#LC:accepted.

"""
### 4. Range Sum Query — Immutable — LC 303

**Pattern:** Prefix Sum
**Priority:** Concept not understood earlier.

Tests:

```python
nums = [-2,0,3,-5,2,-1]

sumRange(0,2)       # 1
sumRange(2,5)       # -1
sumRange(0,5)       # -3
```

[ ] Independent  [ ] Hint  [ ] Old code seen

"""













"""
### 5. Product of Array Except Self — LC 238

**Pattern:** Prefix Product + Suffix Product
**Recall trigger:** Left product does **not** include current item; right product does **not** include current item.

Tests:

```python
[1,2,3,4]           # [24,12,8,6]
[-1,1,0,-3,3]       # [0,0,9,0,0]
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""

def prodarrayexceptself(nums):

    left=[1]

    for i in range(1,len(nums)):

        left.append(nums[i-1]*left[i-1])
    
    right=[None]*len(nums)
    right[-1]=1

    for j in range(len(nums)-2,-1,-1):
        right[j]=(nums[j+1]*right[j+1])

    output=[]

    for k in range(len(nums)):

        output.append(left[k]*right[k])
    
    return output
    

print(prodarrayexceptself([1,2,3,4]))

#Status: independent.

#LC:accepted.


"""

### 6. Subarray Sum Equals K — LC 560

**Pattern:** Prefix Sum + Frequency Hash Map
**Priority:** Previously hint-needed and flagged shaky.

Mental trigger:

```text
needed_prefix = current_prefix - k
seen = {0: 1}
```

Tests:

```python
[1,1,1], 2          # 2
[1,2,3], 3          # 2
[1,-1,0], 0         # 3
```

[ ] Independent  [ ] Hint  [ ] Old code seen
"""

def subarraySum(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0

        for i in range(len(nums)):

            prefix=0
           

            for j in range(i,len(nums)):
             

                prefix+=nums[j]

                if prefix==k:
                    count+=1
        return count

print(subarraySum([1,2,1,2,1],3))

def subarraySum(nums, k):

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


print(subarraySum([1,2,1,2,1],3))

#status: solved independednt but still feels not deppend Properly.

#LC: Accepted.

"""
### 7. Contiguous Array — LC 525

**Pattern:** Prefix Balance + Hash Map
**Priority:** Concept not understood earlier.

Mental trigger:

```text
0 -> -1
1 -> +1

same balance seen again
= equal number of 0 and 1 between indices
```

Tests:

```python
[0,1]                       # 2
[0,1,0]                     # 2
[0,1,1,0,1,1,1,0]           # 4
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""

def findMaxLength(nums):
    seen = {0: -1}
    balance = 0
    best = 0

    for i in range(len(nums)):
        
        if nums[i]==0:
            balance-=1
        else:
            balance+=1
        
        if balance in seen:
            best=max(best,i-seen[balance])
        else:
            seen[balance]=i


    return best


#status: Seen old solution need deep understanding on this.

#LC: Accepted.


"""
### 8. Maximum Subarray — LC 53

**Pattern:** Running-State Tracking / Kadane’s Algorithm
**Subarray problem — mandatory.**

Tests:

```python
[-2,1,-3,4,-1,2,1,-5,4]     # 6
[1]                          # 1
[5,4,-1,7,8]                # 23
```

[ ] Independent  [ ] Hint  [ ] Old code seen

"""

def maxsubarray(nums):

    max_array=nums[0]
    prefix=nums[0]

    for i in range(1,   len(nums)):

        prefix=max(nums[i],prefix+nums[i])

        max_array=max(max_array,prefix)
    
    return max_array

print(maxsubarray([-2,1,-3,4,-1,2,1,-5,4] ))
print(maxsubarray([5,4,-1,7,8]   ))

#Status: Independent after guided concept learning

#LC: Accepted.

"""
### 9. Maximum Product Subarray — LC 152

**Pattern:** Running-State Tracking
**Subarray problem — mandatory.**

Mental trigger:

```text
Negative number can swap maximum and minimum.
Track both current_max and current_min.
```

Tests:

```python
[2,3,-2,4]                  # 6
[-2,0,-1]                   # 0
[-2,3,-4]                   # 24
```

[ ] Independent  [ ] Hint  [ ] Old code seen

"""

def maxprodsubarray(nums):

    max_subarray=nums[0]
    min_subarray=nums[0]
    
    max_prod=nums[0]
    

    for i in range(1,len(nums)):
        n=nums[i]

        temp_min=min_subarray
        temp_max=max_subarray

        max_subarray=max(n,temp_max*n,temp_min*n)
        min_subarray=min(n,temp_max*n,temp_min*n)

        max_prod=max(max_prod,max_subarray)

    return max_prod


print(maxprodsubarray([2,3,-2,4] ))

#status: Independent after guided concept learning

#LC=Accepted.

"""
### 10. Maximum Average Subarray I — LC 643

**Pattern:** Fixed-Size Sliding Window
**Subarray problem — mandatory.**

Tests:

```python
[1,12,-5,-6,50,3], 4        # 12.75
[5], 1                       # 5.0
```

[ ] Independent  [ ] Hint  [ ] Old code seen

"""

def maxaverage(nums,k):

    left=0
    best=0
    prefix=0

    for right in range(len(nums)):

        prefix+=nums[right]

        while right-left+1>k:

            prefix-=nums[left]
            left+=1
            
        if right-left+1==k:
            best=max(best,prefix)
    
    return best/float(k)

print(maxaverage([1,12,-5,-6,50,3], 4 ))
print(maxaverage([5], 1 ))

#status: independent.

#LC=Accepted.
        


"""
 ### 4. Range Sum Query — Immutable — LC 303

**Pattern:** Prefix Sum
**Priority:** Concept not understood earlier.

Tests:

```python
nums = [-2,0,3,-5,2,-1]

sumRange(0,2)       # 1
sumRange(2,5)       # -1
sumRange(0,5)       # -3
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---
 
 
"""       

class NumArray(object):

    def __init__(self, nums):
        self.prefix=[0]

        for i in nums:
            self.prefix.append(self.prefix[-1]+i)
       

    def sumRange(self, left, right):
        return self.prefix[right+1]-self.prefix[left]


obj = NumArray([-2, 0, 3, -5, 2, -1])

print(obj.sumRange(0, 2))  # 1
print(obj.sumRange(2, 5))  # -1
print(obj.sumRange(0, 5))  # -3

#status:solved with hints.

#LC:NA

    
"""
### 7. Contiguous Array — LC 525

**Pattern:** Prefix Balance + Hash Map
**Priority:** Concept not understood earlier.

Mental trigger:

```text
0 -> -1
1 -> +1

same balance seen again
= equal number of 0 and 1 between indices
```

Tests:

```python
[0,1]                       # 2
[0,1,0]                     # 2
[0,1,1,0,1,1,1,0]           # 4
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""

def findMaxLength(nums):

    balance=0
    best=0
    seen={0:-1}

    for i in range(len(nums)):

        if nums[i]==1:
            balance+=1
        else:
            balance-=1
        
        if balance in seen:
            best=max(best,i-seen[balance])
        else:
            seen[balance]=i
    return best


print(findMaxLength([0, 1]))                    # 2
print(findMaxLength([0, 1, 0]))                 # 2
print(findMaxLength([0, 1, 1, 0]))              # 4

#status: solved after guided concept learning
#Pattern: Prefix Balance + Hash Map


def maxSubArray(nums):

    currentsum=nums[0]
    best=nums[0]

    for i in range(1,len(nums)):

        currentsum=max(nums[i],currentsum+nums[i])

        best=max(best,currentsum)

    return best

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
print(maxSubArray([1]))                       # 1
print(maxSubArray([-3,-2,-5]))                # -2

"""
### 11. Longest Substring Without Repeating Characters — LC 3

**Pattern:** Variable-Size Sliding Window + Set

Tests:

```python
"abcabcbb"                  # 3
"bbbbb"                     # 1
"pwwkew"                    # 3
"baca"                      # 3
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""

def longsubstring(s):

    left=0
    seen=set()
    best=0

    for i in range(len(s)):

        while s[i] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[i])

        best=max(best,i-left+1)
    return best    

print(longsubstring("abcabcbb"))
print(longsubstring("bbbbb"))
print(longsubstring("pwwkew"))
print(longsubstring("baca"))

#Status : Independent
#LC: Accepted

"""
### 12. Minimum Size Subarray Sum — LC 209

**Pattern:** Variable-Size Sliding Window
**Subarray problem — mandatory.**

Mental trigger:

```text
Expand until sum >= target.
While valid, update answer and shrink.
```

Tests:

```python
7, [2,3,1,2,4,3]            # 2
4, [1,4,4]                  # 1
11, [1,1,1,1,1]             # 0
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""

def minSubArrayLen(target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left=0
        minarray=float('inf')
        prefix=0

        for right in range(len(nums)):

            prefix+=nums[right]

            while prefix>=target:
                minarray=min(minarray,right-left+1)
                prefix-=nums[left]
                left+=1
        if minarray==float('inf'):
            return 0
        else:
            return minarray

#Status : Independent
#LC: Accepted


"""
### 13. Longest Repeating Character Replacement — LC 424

**Pattern:** Sliding Window + Frequency Map
**Priority:** Previously hint-needed.

Mental trigger:

```text
window_length - max_frequency <= k
```

Tests:

```python
"ABAB", 2                   # 4
"AABABBA", 1                # 4
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""

def characterReplacement(s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        seen={}
        max_freq=0
        left=0
        best=0

        for right in range(len(s)):

            seen[s[right]]=seen.get(s[right],0)+1

            max_freq=max(seen.values())

            while (right-left+1)-max_freq > k:

                seen[s[left]]-=1
                left+=1
            best=max(best,right-left+1)
        return best


#Status : Independent
#LC: Accepted

"""
### 14. Permutation in String — LC 567

**Pattern:** Fixed-Size Sliding Window + Frequency Map

Tests:

```python
"ab", "eidbaooo"            # True
"ab", "eidboaoo"            # False
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""

def checkInclusion(s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        seen_s1={}
        for i in s1:
            seen_s1[i]=seen_s1.get(i,0)+1
        
        left=0
        seen2={}

        for right in range(len(s2)):

            seen2[s2[right]]=seen2.get(s2[right],0)+1

            while right-left+1 > len(s1):
                seen2[s2[left]]-=1
                if seen2[s2[left]]==0:
                    del seen2[s2[left]]
                left+=1
            if seen_s1==seen2:
                return True
        return False

#Status : Independent
#LC: Accepted


"""
### 15. Find All Anagrams in a String — LC 438

**Pattern:** Fixed-Size Sliding Window + Frequency Map

Tests:

```python
"cbaebabacd", "abc"         # [0,6]
"abab", "ab"                # [0,1,2]
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""

def findAnagrams(s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        seen1={}
        for i in p:
            seen1[i]=seen1.get(i,0)+1
        
        seen2={}
        out=[]
        left=0

        for right in range(len(s)):

            seen2[s[right]]=seen2.get(s[right],0)+1

            while right-left+1 > len(p):
                seen2[s[left]]-=1

                if seen2[s[left]]==0:
                    del seen2[s[left]]
                left+=1
            
            if seen1==seen2:
                out.append(left)
        return out

#Status : Independent
#LC: Accepted

"""
### 16. Fruits Into Baskets — LC 904

**Pattern:** Variable-Size Sliding Window + Frequency Map
**Subarray problem — mandatory.**

Tests:

```python
[1,2,1]                     # 3
[0,1,2,2]                   # 3
[1,2,3,2,2]                 # 4
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""

def totalFruit(fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        seen={}
        left=0
        fruit=0

        for right in range(len(fruits)):

            seen[fruits[right]]=seen.get(fruits[right],0)+1

            while len(seen)>2:
                seen[fruits[left]]-=1

                if seen[fruits[left]]==0:
                    del seen[fruits[left]]
                left+=1

            fruit=max(fruit,right-left+1)
            
        return fruit

#Status : Independent
#LC: Accepted

"""

### 17. Max Consecutive Ones III — LC 1004

**Pattern:** Variable-Size Sliding Window
**Subarray problem — mandatory.**

Tests:

```python
[1,1,1,0,0,0,1,1,1,1,0], 2     # 6
[0,0,1,1,1,0,0], 0             # 3
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""

def longestOnes(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left=0
        best=0
        zeros=0


        for right in range(len(nums)):

            if nums[right]==0:
                zeros+=1

            while zeros>k:

                if nums[left]==0:
                    zeros-=1
                left+=1
            
            best=max(best,right-left+1)
        return best

#Status : solved by seen old solution
#LC: Accepted

"""
### 18. Contains Duplicate II — LC 219

**Pattern:** Sliding Window + Set
**Important order:** Check → add → shrink.

Tests:

```python
[1,2,3,1], 3                # True
[1,0,1,1], 1                # True
[1,2,3,1,2,3], 2            # False
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""

def containsNearbyDuplicate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        left=0
        seen=set()

        for right in range(len(nums)):

            if nums[right] in seen:
                return True
            else:
                seen.add(nums[right])
            
            while right-left+1>k:
                seen.remove(nums[left])
                left+=1
        return False


#Status : Independent
#LC: Accepted



"""
## Session 3 — Hash Maps, Sorting, Two Pointers, Strings

### 19. Top K Frequent Words — LC 692

**Pattern:** Frequency Sorting
**Priority:** Previously hint-needed.

Required sort order:

```text
frequency descending
word ascending
```

Tests:

```python
["i","love","leetcode","i","love","coding"], 2
# ["i","love"]

["aaa","aa","a"], 1
# ["a"]
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""

def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        seen={}

        for i in words:
            seen[i]=seen.get(i,0)+1
        
        sorted_seen=sorted(seen.items(),key=lambda x:(-x[1],x[0]))
        out=[]

        for key,value in sorted_seen:

            out.append(key)

            if len(out)==k:
                return out
        

#Status : Independent
#LC: Accepted


"""
### 20. Two Sum — LC 1

**Pattern:** Complement Lookup
**Recall trigger:** Store `number -> index`, not `needed -> index`.

Tests:

```python
[2,7,11,15], 9             # [0,1]
[3,2,4], 6                 # [1,2]
[3,3], 6                   # [0,1]
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""

def twosum(nums,target):

    seen={}

    for i in range(len(nums)):
        needed=target-nums[i]

        if needed in seen:
            return [seen[needed],i]
        
        seen[nums[i]]=i
print(twosum([2,7,11,15], 9    ))
print(twosum([3,2,4], 6    ))
print(twosum([3,3], 6    ))


#Status : Independent
#LC: Accepted


"""
### 21. Two Sum II — Input Array Is Sorted — LC 167

**Pattern:** Two Pointers
**Use sorted property; do not use a dictionary.**

Tests:

```python
[2,7,11,15], 9             # [1,2]
[2,3,4], 6                 # [1,3]
[-1,0], -1                 # [1,2]
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---
"""
def twosum2(nums,target):

    left=0
    right=len(nums)-1

    while left<right:

        sum_of=nums[right]+nums[left]

        if sum_of==target:
            return [left+1,right+1]
        elif sum_of>target:
            right-=1
        else:
            left+=1
    
print(twosum2([2,7,11,15], 9  ))
print(twosum2([2,3,4], 6  ))
print(twosum2([-1,0], -1    ))

#Status : Independent
#LC: Accepted

"""
### 22. Isomorphic Strings — LC 205

**Pattern:** Two-Way Hash Map
**Priority:** Old solution was peeked during recall.

Tests:

```python
"egg", "add"               # True
"foo", "bar"               # False
"badc", "baba"             # False
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""
def isomorphicstring(s,t):

    if len(s)!=len(t):
        return False

    seen_s={}
    seen_t={}

    for i in range(len(s)):

        if s[i] in seen_s and seen_s[s[i]]!=t[i]:
            return False
        else:
            seen_s[s[i]]=t[i]
        
        if t[i] in seen_t and seen_t[t[i]]!=s[i]:
            return False
        else:
            seen_t[t[i]]=s[i]
    return True

print(isomorphicstring("egg", "add"  ))
print(isomorphicstring("foo", "bar"   ))
print(isomorphicstring("badc", "baba"  ))

#Status : Independent
#LC: Accepted


"""
### 23. Remove Duplicates from Sorted Array — LC 26

**Pattern:** Two Pointers + In-Place Overwrite
**Priority:** Write-pointer initialization was confusing earlier.

Tests:

```python
[1,1,2]                    # return 2; first values [1,2]
[0,0,1,1,1,2,2,3,3,4]     # return 5; first values [0,1,2,3,4]
[]                          # return 0
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---
"""
def removeduplicate(nums):

    if not nums:
        return 0

    write=1
    
    for i in range(1,len(nums)):

        if nums[i]!=nums[write-1]:
            nums[write]=nums[i]
            write+=1
    return write

print(removeduplicate([1,1,2] ))
print(removeduplicate([0,0,1,1,1,2,2,3,3,4]))
print(removeduplicate([]))

#Status : Independent
#LC: Accepted

"""
### 24. Remove Element — LC 27

**Pattern:** Two Pointers + In-Place Overwrite

Tests:

```python
[3,2,2,3], 3               # return 2
[0,1,2,2,3,0,4,2], 2      # return 5
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""
def removeelement(nums,val):

    write=0

    for i in range(len(nums)):

        if nums[i]!=val:
            nums[write]=nums[i]
            write+=1
    return write

print(removeelement([3,2,2,3], 3)  )
print(removeelement([0,1,2,2,3,0,4,2], 2  )  )


#Status : Independent
#LC: Accepted

"""
### 25. Length of Last Word — LC 58

**Pattern:** String Traversal
**Priority:** Earlier marked as not solved.

Tests:

```python
"Hello World"                      # 5
"   fly me   to   the moon  "      # 4
"a"                                # 1
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""

def lenoflastword(s):

    lastwordlen=0
    count=0

    for i in s:

        if i==" ":
            count=0
        else:
            count+=1
        
        if count!=0:
            lastwordlen=count
    return lastwordlen

print(lenoflastword("Hello World"  ))
print(lenoflastword("   fly me   to   the moon  "   ))
print(lenoflastword("a"  ))

#Status : Independent
#LC: Accepted

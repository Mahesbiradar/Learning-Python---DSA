# Session 2 — 24-Hour Recall: Yesterday’s New / Hint Problems

"""
## 4. Unique Number of Occurrences (LC 1207)


Pattern: Frequency Hashing

```python
[1,2,2,1,1,3]             # True
[1,2]                     # False
```

[ ] Independent  [ ] Hint


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

print(uniqueOccurrences([1,2,2,1,1,3]))
print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
print(uniqueOccurrences([1,2]))

# Status: independent

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:Na

# Pattern: Frqunecy Hashing.

"""
## 5. Top K Frequent Words (LC 692)

Pattern: Frequency Sorting

Required sort order:

```text
frequency descending
word ascending
```

Test:

```python
["i","love","leetcode","i","love","coding"], 2
# ["i","love"]

["aaa","aa","a"], 1
# ["a"]
```

[ ] Independent  [ ] Hint

"""

def topKFrequent(words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        seen={}

        for i in words:
            seen[i]=seen.get(i,0)+1
        
        sorted_seen=sorted(seen.items(),key=lambda x:(-x[1],x[0]))

        result=[]

        for key,value in sorted_seen:
            result.append(key)

            if len(result)==k:
                return result

print(topKFrequent(["i","love","leetcode","i","love","coding"],2))
print(topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"],4))

# Status: independent

# Time complexity: O(n+mlogm)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:i seen the sotred syntax from web (x:(-x[1],x[0])) still need clarity

# Pattern: Frqunecy sorting

"""
## 6. Two Sum (LC 1)

Pattern: Complement Lookup

Mental trigger:

```text
Store current number -> index
Search for target - current number
```

Test:

```python
[2,7,11,15], 9            # [0,1]
[3,2,4], 6                # [1,2]
[3,3], 6                  # [0,1]
```

[ ] Independent  [ ] Hint

---
"""

def twosum(nums,target):
     
     seen={}

     for i in range(len(nums)):
        needed=target-nums[i]

        if needed in seen:
            return [seen[needed],i]
        
        seen[nums[i]]=i
    

print(twosum([2,7,11,15],9))
print(twosum([3,2,4],6))
          

# Status: independent

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:

# Pattern: Complement Lookup

"""
## 7. Two Sum II — Sorted Array (LC 167)

Pattern: Two Pointers / Complement Lookup

Use the sorted property this time: left and right pointers.

Test:

```python
[2,7,11,15], 9            # [1,2]
[2,3,4], 6                # [1,3]
[-1,0], -1                # [1,2]
```

[ ] Independent  [ ] Hint

"""
def two_sum(nums,target):
     
    right=len(nums)-1
    left=0

    while left < right:
     

        sum=nums[left]+nums[right]
         
        if sum==target:
            return [left+1,right+1]
        elif sum>target:
            right-=1
        else:
             left+=1

print(two_sum([2,7,11,15], 9))
print(two_sum([2,3,4], 6 ))
print(two_sum([-1,0], -1 ))


# Status: independent

# Time complexity: O(n)

# Space complexity: O(1)

# LC status: Accepted

# mistakes/confusion:

# Pattern: Complement Lookup + Two pointers


"""
## 8. Contains Duplicate II (LC 219)

Pattern: Sliding Window + Set

Important order:

```text
check duplicate first
add current item
shrink if window is too large
```

Test:

```python
[1,2,3,1], 3              # True
[1,0,1,1], 1              # True
[1,2,3,1,2,3], 2          # False
```

[ ] Independent  [ ] Hint

--
"""
def containsduplicate(nums,val):
     
    left=0
    seen=set()

    for right in range(len(nums)):
         
        if nums[right] in seen:
            return True
        seen.add(nums[right])

        while right - left + 1 > val:
            seen.remove(nums[left])
            left+=1
    return False

print(containsduplicate([1,2,3,1], 3 ))
print(containsduplicate([1,0,1,1], 1))
print(containsduplicate([1,2,3,1,2,3], 2 ))

# Status: independent

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:

# Pattern: sliding window + set


"""
## 9. Remove Duplicates from Sorted Array (LC 26)

Pattern: Two Pointers + In-place Overwrite

Test:

```python
[1,1,2]                   # return 2; first values become [1,2]
[0,0,1,1,1,2,2,3,3,4]    # return 5; first values become [0,1,2,3,4]
[]                        # return 0
```

[ ] Independent  [ ] Hint

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

print(removeduplicate([1,1,2]  ))
print(removeduplicate([0,0,1,1,1,2,2,3,3,4]  ))


# Status: independent

# Time complexity: O(n)

# Space complexity: O(1)

# LC status: Accepted

# mistakes/confusion:

# Pattern: Two pointers

"""
## 10. Remove Element (LC 27)

Pattern: Two Pointers + In-place Overwrite

Test:

```python
[3,2,2,3], 3             # return 2
[0,1,2,2,3,0,4,2], 2    # return 5
```

[ ] Independent  [ ] Hint

---


"""

def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        write=0

        for i in range(len(nums)):

            if nums[i]!=val:
                nums[write]=nums[i]
                write+=1
        return write

# Status: seen old solution bcz im confused about initilization of write pointer.

# Time complexity: O(n)

# Space complexity: O(1)

# LC status: Accepted

# mistakes/confusion:

# Pattern: Two pointers + inplace Overwrite


# Session 3 — Sliding Window Recall

"""
## 11. Longest Substring Without Repeating Characters (LC 3)

Pattern: Sliding Window + Set

```python
"abcabcbb"                # 3
"bbbbb"                   # 1
"pwwkew"                  # 3
```

[ ] Independent  [ ] Hint

---

"""

def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        seen=set()
        best=0
        left=0

        for i in range(len(s)):

            while s[i] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[i])

            best=max(best,i-left+1)
        return best

print(lengthOfLongestSubstring("abcabcbb"))


# Status: independent

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:

# Pattern:Sliding Window.

"""

## 12. Minimum Size Subarray Sum (LC 209)

Pattern: Sliding Window

```python
target = 7, nums = [2,3,1,2,4,3]  # 2
target = 4, nums = [1,4,4]        # 1
target = 11, nums = [1,1,1,1,1]   # 0
```

[ ] Independent  [ ] Hint

---

"""

def minsizeofsubarraysum(nums,target):
     
    left=0
    minsize=float('inf')
    subarraysum=0


    for right in range(len(nums)):
         
        subarraysum+=nums[right]

        while subarraysum>=target:
            minsize=min(minsize,right-left+1)
            subarraysum-=nums[left]
            left+=1
       
    
    if minsize==float('inf'):
        return 0
    else:
        return minsize

print(minsizeofsubarraysum([2,3,1,2,4,3],7))

# Status: Solved with Hint / correction

# Time complexity: O(n)

# Space complexity: O(1)

# LC status: Accepted

# mistakes/confusion:

# Pattern:Sliding Window.

"""
## 13. Longest Repeating Character Replacement (LC 424)

Pattern: Sliding Window + Frequency Map

```python
s = "ABAB", k = 2         # 4
s = "AABABBA", k = 1      # 4
```

[ ] Independent  [ ] Hint

---

"""
def longreatingchar(s,k):
     
    left=0
    seen={}
    best=0
    max_freq=0

    for right in range(len(s)):

        seen[s[right]]=seen.get(s[right],0)+1

        max_freq=max(max_freq,seen[s[right]])

        while (right-left+1)-max_freq>k:
            seen[s[left]]-=1
            left+=1
        
        best=max(best,right-left+1)
    return best

print(longreatingchar("ABAB",2))
print(longreatingchar("AABABBA",1))


# Status: Solved with Hint

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:

# Pattern:Sliding Window.

         
"""
## 14. Permutation in String (LC 567)

Pattern: Fixed-Size Sliding Window + Frequency Map

```python
s1 = "ab", s2 = "eidbaooo"      # True
s1 = "ab", s2 = "eidboaoo"      # False
```

[ ] Independent  [ ] Hint

"""
def permutationinstring(s1,s2):

    seen_s1={}

    for i in s1:
        seen_s1[i]=seen_s1.get(i,0)+1

    left=0
    seen_s2={}

    for right in range(len(s2)):

        seen_s2[s2[right]]=seen_s2.get(s2[right],0)+1

        while right-left+1>len(s1):
            seen_s2[s2[left]]-=1
            if seen_s2[s2[left]]==0:
                del seen_s2[s2[left]]
            left+=1
        
        if seen_s1==seen_s2:
            return True
    return False


print(permutationinstring(s1 = "ab", s2 = "eidbaooo"))
print(permutationinstring(s1 = "ab", s2 = "eidboaoo"))

     
# Status: independent

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:

# Pattern:Sliding Window.

"""
## 15. Find All Anagrams in a String (LC 438)

Pattern: Fixed-Size Sliding Window + Frequency Map

```python
s = "cbaebabacd", p = "abc"     # [0,6]
s = "abab", p = "ab"            # [0,1,2]
```

[ ] Independent  [ ] Hint

---

"""

def findanagrams(s,p):

    seen_p={}

    for i in p:
        seen_p[i]=seen_p.get(i,0)+1
    
    result=[]

    seen_s={}

    left=0

    for right in range(len(s)):

        seen_s[s[right]]=seen_s.get(s[right],0)+1

        while right-left+1>len(p):
            seen_s[s[left]]-=1

            if seen_s[s[left]]==0:
                del seen_s[s[left]]
            left+=1
        if seen_p==seen_s:
            result.append(left)
    return result

print(findanagrams(s = "cbaebabacd", p = "abc"))
print(findanagrams(s = "abab", p = "ab"))

# Status: independent

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:

# Pattern:Sliding Window.

"""
# Session 4 — Other Shaky Recall

## 16. Subarray Sum Equals K (LC 560)

Pattern: Prefix Sum + Hash Map

Mental trigger:

```text
needed prefix = current_sum - k
```

Test:

```python
[1,1,1], 2                # 2
[1,2,3], 3                # 2
[1,-1,0], 0               # 3
```

[ ] Independent  [ ] Hint

---

"""
#Brute Force.

def subarraysumequalsk(nums,k):

    count=0
  

    for i in range(len(nums)):
        prefix=0

        for j in range(i,len(nums)):
            prefix+=nums[j]

            if prefix==k:
                count+=1
    return count

print(subarraysumequalsk([1,1,1], 2))
print(subarraysumequalsk([1,2,3], 3))
print(subarraysumequalsk([1,-1,0], 0))


#optimal solution:

def subarraysumequalsk(nums,k):

    count=0
    seen={0:1}
    prefix=0
    

    for i in range(len(nums)):

        prefix+=nums[i]
        needed=prefix-k

        if needed in seen:
            count+=seen[needed]
        
        seen[prefix]=seen.get(prefix,0)+1

    return count

print(subarraysumequalsk([1,1,1], 2))
print(subarraysumequalsk([1,2,3], 3))
print(subarraysumequalsk([1,-1,0], 0))

# Status: solved with hints

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:

# Pattern:Prefix sum + frequncy Hashing

"""
## 17. Isomorphic Strings (LC 205)

Pattern: Two-Way Hash Map

```python
"egg", "add"              # True
"foo", "bar"              # False
"badc", "baba"            # False
```

[ ] Independent  [ ] Hint

---

"""

def isomorphicstrings(s,t):

    if len(s)!=len(t):
        return False

    seen1={}
    seen2={}

    for i in range(len(s)):

        if s[i] in seen1 and seen1[s[i]]!=t[i]:
            return False
        else:
            seen1[s[i]]=t[i]
        
        if t[i] in seen2 and seen2[t[i]]!=s[i]:
            return False
        else:
            seen2[t[i]]=s[i]
    return True

print(isomorphicstrings(s = "egg", t = "add"))
print(isomorphicstrings(s = "f11", t = "b23"))
print(isomorphicstrings(s="paper", t = "title"))

# Status: solved with hints(old solution seen)

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:

# Pattern:Frequncy Hashing 

"""

## 18. Maximum Product Subarray (LC 152)

Pattern: Running-State Tracking

Remember: a negative number can swap the role of current maximum and current minimum.

```python
[2,3,-2,4]                # 6
[-2,0,-1]                 # 0
[-2,3,-4]                 # 24
```

[ ] Independent  [ ] Hint

---

"""
def maxprodsubarray(nums):

    currentmin=nums[0]
    currentmax=nums[0]
    maxprod=nums[0]

    for i in range(1,len(nums)):

        n=nums[i]

        tem_max=currentmax
        tem_min=currentmin

        currentmax=max(n,tem_max*n,tem_min*n)
        currentmin=min(n,tem_max*n,tem_min*n)

        maxprod=max(maxprod,currentmax,currentmin)

    return maxprod

print(maxprodsubarray([2,3,-2,4]))
print(maxprodsubarray([-2,0,-1]  ))
print(maxprodsubarray([-2,3,-4]   ))


# Status: solved with hints(old solution seen)

# Time complexity: O(n)

# Space complexity: O(1)

# LC status: Accepted

# mistakes/confusion:

# Pattern:Running state Tracking.


"""
# Session 1 — Finish Yesterday’s Gaps

## 1. Length of Last Word (LC 58)

Pattern: String Traversal

Edge cases:

```python
"Hello World"                       # 5
"   fly me   to   the moon  "       # 4
"a"                                 # 1
```

[ ] Independent  [ ] Hint  [ ] Submitted

---

"""


def lastwordlenght(s):

    count=0
    last_word_len=0

    for i in range(len(s)):

        if s[i]==" ":
            count=0
        else:
            count+=1
        
        if count!=0:
            last_word_len=count

    return last_word_len

print(lastwordlenght("Hello World" ))
print(lastwordlenght("   fly me   to   the moon  "))
print(lastwordlenght("a"))

# Status: independent

# Time complexity: O(n)

# Space complexity: O(1)

# LC status: Accepted

# mistakes/confusion:

# Pattern:string Traversal

"""
## 2. Range Sum Query — Immutable (LC 303)

Pattern: Prefix Sum

Test:

```python
nums = [-2, 0, 3, -5, 2, -1]
sumRange(0, 2)  # 1
sumRange(2, 5)  # -1
sumRange(0, 5)  # -3
```

[ ] Independent  [ ] Hint  [ ] Submitted

---

"""

#Status: Pending
"""
## 3. Contiguous Array (LC 525)

Pattern: Prefix Sum + Hash Map

Key conversion:

```python
0 -> -1
1 -> +1
```

Test:

```python
[0, 1]                    # 2
[0, 1, 0]                 # 2
[0, 1, 1, 0, 1, 1, 1, 0] # 4

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

#Concept Not understtod ill retry Later.


#Just seen the solution and paster here.


#Status: Hint / not understood — retry tomorrow
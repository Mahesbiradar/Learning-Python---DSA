## Concept Warm-Up (5 min)

# Write both Sliding Window templates from memory. No notes.

# Fixed-Size Sliding Window

nums=[8,5,-6,4,7,2] 

k=4

subarraysum=0
max_subarray=float('-inf')

for right in range(len(nums)):

    subarraysum+=nums[right]

    if right>=k:
        subarraysum-=nums[right-k]
    
    if right>=k-1:
        max_subarray=max(max_subarray,subarraysum)

print(max_subarray)

## Variable-Size Sliding Window
nums=[8,5,-6,4,7,2]
target=10

left=0
sumarray_prod=1
max_subarray=float('-inf')

for right in range(len(nums)):

    subarraysum+=nums[right]

    while subarraysum>=target:
        subarraysum-=nums[left]
        left+=1
    
    
    max_subarray=max(max_subarray,subarraysum)

print(max_subarray)
    

## Revision Problems (5 problems)

"""
### Maximum Average Subarray I (LC 643)

Pattern: Sliding Window (Fixed Window)
Due: 24h recall
Constraint: 1 <= k <= nums.length <= 10^5; -10^4 <= nums[i] <= 10^4.
Goal: Solve independently. Focus on:

* when window becomes valid,
* why `right >= k-1`,
* why subtraction maintains window size.
  [ ] Solved independently
  [ ] Needed hint (note what)
  [ ] Submitted to LC — Result: ___

"""
#Brute Force:

def findMaxAverage(nums,k):

    subarraysum=0
    
    for i in range(0,k):
        subarraysum+=nums[i]
    max_sum=subarraysum

    print(max_sum)

    for j in range(k,len(nums)):

        subarraysum+=nums[j]-nums[j-k]

        if subarraysum>max_sum:
            max_sum=subarraysum
    
    return max_sum/k

print(findMaxAverage([1,12,-5,-6,50,3],4))



#optimal solution using sliding window.
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        subarraysum=0
        max_subarray=float('-inf')

        for right in range(len(nums)):
            #add elemenets to window or expand window
            subarraysum+=nums[right]

            #if window is invalid remove left element

            if right>=k:
                subarraysum-=nums[right-k]
            
            #Take maxsubarray when window is valid.
            if right>=k-1:
               max_subarray=max(max_subarray,subarraysum)
        
        return max_subarray/float(k)

# Status: Solved independednt
# Time complexity: O(n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:Sliding window

# Core invariant:
# Optimization jump:
# Key decision:
# Recognition trigger:
# Wrong assumption:
# One-line explanation:

"""
### Longest Substring Without Repeating Characters (LC 3)

Pattern: Sliding Window (Variable Window)
Due: 24h recall
Constraint: 0 <= s.length <= 5 * 10^4; English letters, digits, symbols, spaces.
Goal: Solve independently. Focus on:

* shrinking while duplicate exists,
* why `while` is required,
* maintaining validity.
  [ ] Solved independently
  [ ] Needed hint (note what)
  [ ] Submitted to LC — Result: ___

"""

def lengthOfLongestSubstring(s):

    left=0
    lenght=0
    seen=set()

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        
        seen.add(s[right])

        lenght=max(lenght,right-left+1)
    return lenght

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))

# Status: Solved with hints
# Time complexity: O(n)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:Sliding window

"""
### Minimum Size Subarray Sum (LC 209)

Pattern: Sliding Window (Variable Window)
Due: 24h recall
Constraint: 1 <= target <= 10^9; 1 <= nums.length <= 10^5.
Goal: Solve independently. Focus on:

* `sum >= target`,
* why shrinking happens repeatedly,
* why total complexity is O(n).
  [ ] Solved independently
  [ ] Needed hint (note what)
  [ ] Submitted to LC — Result: ___

"""

def minSubArrayLen(nums,target):

    left=0
    min_len=float('inf')
    subarray_sum=0

    for right in range(len(nums)):
        
        subarray_sum+=nums[right]

        while subarray_sum>=target:

            min_len=min(min_len,right-left+1)

            subarray_sum-=nums[left]

            left+=1
    if min_len==float('inf'):
        return 0
    return min_len

print(minSubArrayLen([2,3,1,2,4,3],7))
print(minSubArrayLen([1,4,4],4))
print(minSubArrayLen([1,1,1,1,1,1,1,1],11))

# Status: Solved with hints
# Time complexity: O(n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:Sliding window

"""
### Two Sum (LC 1)

Pattern: Complement Lookup
Due: 7d final recall
Constraint: exactly one valid answer exists.
Goal: One-pass hash map from memory. No tracing needed.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___


"""

#brute Force:

def twoSum(nums,target):

    for i in range(len(nums)):

        for j in range(i+1,len(nums)):

            if nums[i]+nums[j]==target:
                return [i,j]

print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))    

# Status: Solved independent
# Time complexity: O(n^2)
# Space complexity:O(1)
# LC status:NA
# mistakes/confusion:NA
# Pattern:Nested loop

def twoSum(nums,target):

    seen={}

    for i in range(len(nums)):

        needed=target-nums[i]

        if needed in seen:
            return [seen[needed],i]
        
        seen[nums[i]]=i

print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))    

# Status: Solved independent
# Time complexity: O(n)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:Complement Lookup

"""
### Valid Anagram (LC 242)

Pattern: Frequency Hashing
Due: 7d final recall
Constraint: lowercase English letters only.
Goal: Solve in under 5 minutes from memory.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

#Brute Force:

def isAnagram(s,t):

    if len(s)!=len(t):
        return False
    
    for i in range(len(s)):

        count1=0
        count2=0

        for j in range(len(s)):

            if s[i]==s[j]:
                count1+=1
        for k in  range(len(t)):

            if s[i]==t[k]:
                 count2+=1
        
        if count1!=count2:
            return False
    return True

print(isAnagram("anagram","nagaram"))
print(isAnagram("rat","car"))

# Status: Solved independent
# Time complexity: O(n^2)
# Space complexity:O(1)
# LC status:NA
# mistakes/confusion:NA
# Pattern:

def isAnagram(s,t):
    if len(s)!=len(t):
        return False
    
    s_f={}

    for i in s:
        s_f[i]=s_f.get(i,0)+1

    t_f={}

    for j in t:
        t_f[j]=t_f.get(j,0)+1
    
    for k in range(len(s)):

        if s[k] not in t_f:
            return False
        
        if s_f[s[k]]!=t_f[s[k]]:
            return False

    return True

print(isAnagram("anagram","nagaram"))
print(isAnagram("rat","car"))

# Status: Solved independent
# Time complexity: O(n)
# Space complexity:O(n)
# LC status:NA
# mistakes/confusion:NA
# Pattern:Frequency hashing

### New Problems (3 problems, local only)


"""
### Longest Repeating Character Replacement (LC 424)

Pattern: Sliding Window (Variable Window)
Difficulty: Medium

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing at most `k` replacements.

Example 1:
Input: s = "ABAB", k = 2
Output: 4

Example 2:
Input: s = "AABABBA", k = 1
Output: 4

Constraints:

* 1 <= s.length <= 10^5
* s consists of only uppercase English letters.
* 0 <= k <= s.length

Key insight:
Window is valid if:

```python
window_size - max_frequency <= k
```
"""
def characterReplacement(s,k):

    left=0
    seen={}
    best_len=0
    max_freq=0

    for right in range(len(s)):
        seen[s[right]]=seen.get(s[right],0)+1

        max_freq=max(max_freq,max(seen.values()))

        while (right-left+1)-max_freq>k:
            seen[s[left]]-=1
            left+=1

        
        best_len=max(best_len,right-left+1)
    
    return best_len
        

print(characterReplacement("ABAB",2))

# Status: Solved with hints
# Time complexity: O(n)
# Space complexity:O(n)
# LC status:NA
# mistakes/confusion:NA
# Pattern:sliding window + Frequency Hashing.

"""
### Permutation in String (LC 567)

Pattern: Sliding Window + Frequency Hashing
Difficulty: Medium

Given two strings `s1` and `s2`, return `True` if `s2` contains a permutation of `s1`, or `False` otherwise.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: True

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: False

Constraints:

* 1 <= s1.length, s2.length <= 10^4
* s1 and s2 consist of lowercase English letters.

Key insight:
Fixed-size window of length `len(s1)`.


"""

def Permutationinstring(s1,s2):


    left=0
    seen_a={}
    for i in s1:
        seen_a[i]=seen_a.get(i,0)+1
    window_freq={}
    for right in range(len(s2)):

        window_freq[s2[right]]=window_freq.get(s2[right],0)+1

        if right-left+1>len(s1):
            window_freq[s2[left]]-=1
            if window_freq[s2[left]]==0:
                del window_freq[s2[left]]
            left+=1
        
        if seen_a==window_freq:
            return True
    return False

print(Permutationinstring("ab","eidbaooo"))
print(Permutationinstring("ab","eidboaoo"))
        
# Status: Solved with hints
# Time complexity: O(n)
# Space complexity:O(n)
# LC status:NA
# mistakes/confusion:NA
# Pattern:fixed size sliding window + Frequency Matching.

"""
### Fruits Into Baskets (LC 904)

Pattern: Sliding Window (Variable Window)
Difficulty: Medium

You are visiting a farm with a row of fruit trees represented by an integer array `fruits`.

You have two baskets, and each basket can hold only one type of fruit. You may start at any tree, but must pick exactly one fruit from every tree while moving right.

Return the maximum number of fruits you can collect.

Example 1:
Input: fruits = [1,2,1]
Output: 3

Example 2:
Input: fruits = [0,1,2,2]
Output: 3

Example 3:
Input: fruits = [1,2,3,2,2]
Output: 4

Constraints:

* 1 <= fruits.length <= 10^5
* 0 <= fruits[i] < fruits.length

Key insight:
Window valid only while unique fruit types <= 2.


"""
    
def Fruits_Baskets(fruits):

    fruits_freq={}
    left=0
    max_fruits=0

    for right in range(len(fruits)):

        fruits_freq[fruits[right]]=fruits_freq.get(fruits[right],0)+1

        while len(fruits_freq)>2:
            fruits_freq[fruits[left]]-=1
            if fruits_freq[fruits[left]]==0:
                del fruits_freq[fruits[left]]
            left+=1
        max_fruits=max(max_fruits,right-left+1)
    
    return max_fruits

print(Fruits_Baskets([1,2,1]))
print(Fruits_Baskets([0,1,2,2]))
print(Fruits_Baskets([1,2,3,2,2]))

# Status: Solved with hints
# Time complexity: O(n)
# Space complexity:O(n)
# LC status:NA
# mistakes/confusion:NA
# Pattern:sliding window














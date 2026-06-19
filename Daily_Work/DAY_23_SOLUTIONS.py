## Concept Warm-Up (10 min)

# Write these templates from memory. No notes.

### Frequency Hashing

# Frequency Hashing Template

def freq_hashing(nums):

    seen={}

    for i in nums:
        
        seen[i]=seen.get(i,0)+1
        
    return seen

print(freq_hashing([1,3,4,5,2,3,2,1,4]))



# Revision Problems — Frequency Hashing

"""
### Contains Duplicate (LC 217)

Pattern: Frequency Hashing
Goal: Detect duplicate using hash set.

[ ] Solved independently
[ ] Needed hint
[ ] Submitted to LC

"""
def containsDuplicate(nums):

    seen={}

    for i in nums:
        seen[i]=seen.get(i,0)+1
    
    for key,value in seen.items():

        if value>1:
            return True
    return False

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

# Status: Independent 

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:No

# Pattern: Frequncy Hashing


"""
### Valid Anagram (LC 242)

Pattern: Frequency Hashing
Goal: Compare frequency counts.

[ ] Solved independently
[ ] Needed hint
[ ] Submitted to LC


"""

def isAnagram(s, t):
       
        seen_1={}
        
        for i in s:
            seen_1[i]=seen_1.get(i,0)+1
        
        seen_2={}

        for j in t:
            seen_2[j]=seen_2.get(j,0)+1

        if seen_1==seen_2:
            return True
        return False

    

print(isAnagram( s = "anagram", t = "nagaram"))
print(isAnagram("rat","car"))

# Status: Independent 

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:No

# Pattern: Frequncy Hashing

"""
### First Unique Character in a String (LC 387)

Pattern: Frequency Hashing
Goal: Count frequencies and locate first unique character.

[ ] Solved independently
[ ] Needed hint
[ ] Submitted to LC

"""

def firstUniqChar(s):
        """
        :type s: str
        :rtype: int
        """
        seen={}

        for i in s:
            seen[i]=seen.get(i,0)+1

        for i in range(len(s)):

            if seen[s[i]]==1:
                return i
        return -1

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))

# Status: Independent 

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:No

# Pattern: Frequncy Hashing

"""
### Intersection of Two Arrays II (LC 350)

Pattern: Frequency Hashing
Goal: Frequency map + decrement counts.

[ ] Solved independently
[ ] Needed hint
[ ] Submitted to LC

"""

def intersect(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        seen={}
        result=[]

        for i in nums1:
            seen[i]=seen.get(i,0)+1
        
        for j in nums2:
            if j in seen and seen[j]>0:
                result.append(j)
                seen[j]-=1
        return result

print(intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
print(intersect( [4,9,5], nums2 = [9,4,9,8,4]))

# Status: Independent 

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:No

# Pattern: Frequncy Hashing

"""
### Majority Element (LC 169)

Pattern: Frequency Hashing
Goal: Hash map solution first.

[ ] Solved independently
[ ] Needed hint
[ ] Submitted to LC

"""
def majorityElement( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen={}
        major_count=0
        major_element=None

        for i in nums:
            seen[i]=seen.get(i,0)+1
        
        for key,value in seen.items():

            if value>major_count:
                major_count=value
                major_element=key
        return major_element
print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))

# Status: Independent 

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:No

# Pattern: Frequncy Hashing

"""
## New Problem

### Unique Number of Occurrences (LC 1207)

Pattern: Frequency Hashing

Edge Case 1:
arr = [1,2]
Expected: False

Edge Case 2:
arr = [-3,0,1,-3,1,1,1,-3,10,0]
Expected: True

[ ] Solved independently
[ ] Needed hint
[ ] Submitted to LC

"""

def uniqueOccurrences( arr):
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
            else:
                seen_set.add(value)
        return True

print(uniqueOccurrences([1,2,2,1,1,3]))
print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
print(uniqueOccurrences([1,2]))

# Status: Independent 

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:No

# Pattern: Frequncy Hashing



## New Problem

### Unique Number of Occurrences (LC 1207)
"""
Pattern: Frequency Hashing

Edge Case 1:
arr = [1,2]
Expected: False

Edge Case 2:
arr = [-3,0,1,-3,1,1,1,-3,10,0]
Expected: True

[ ] Solved independently
[ ] Needed hint
[ ] Submitted to LC

"""









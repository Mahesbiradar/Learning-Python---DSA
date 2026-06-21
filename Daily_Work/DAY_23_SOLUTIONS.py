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



# Revision Problems — Frequency Sorting

"""
#  Top K Frequent Elements (LC 347)

Pattern: Frequency Sorting

[ ] Solved independently
[ ] Needed hint
[ ] Submitted to LC

---
"""

def topKFrequent(nums,k):
     
     seen={}

     for i in nums:
          seen[i]=seen.get(i,0)+1
     
     sorted_seen=sorted(seen.items(),key=lambda x:x[1],reverse=True)

     result=[]

     for key,value in sorted_seen:
        
        result.append(key)

        if len(result)==k:
             return result
    

          

print(topKFrequent([1,2,1,2,1,2,3,1,3,2],2))
print(topKFrequent([1],1))
print(topKFrequent([1,2,1,2,1,2,3,1,3,2],2))

# Status: Independent 

# Time complexity: O(n+mlogm)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:No

# Pattern: Frequncy sorting 

"""
### Sort Characters By Frequency (LC 451)

Pattern: Frequency Sorting

[ ] Solved independently
[ ] Needed hint
[ ] Submitted to LC

"""

def frequencySort(s):
     
     seen={}

     for i in s:
          seen[i]=seen.get(i,0)+1
        
     sorted_seen=sorted(seen.items(),key=lambda x:x[1],reverse=True)

     output_str=""


     for key ,value in sorted_seen:
          
          output_str+=key*value
     
     return output_str

print(frequencySort("Aabb"))
print(frequencySort("tree"))
print(frequencySort("cccaaa"))


# Status: Independent 

# Time complexity: O(n+mlogm)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:No

# Pattern: Frequncy sorting 

## New Problem

""" Top K Frequent Words (LC 692)

Pattern: Frequency Sorting

Edge Case 1:
words = ["i","love","leetcode","i","love","coding"]
k = 2

Expected:
["i","love"]

Edge Case 2:
words = ["aaa","aa","a"]
k = 1

Expected:
["a"]

[ ] Solved independently
[ ] Needed hint
[ ] Submitted to LC

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
print(topKFrequent(["aaa","aa","a"],1))


# Status: solved with Hints

# Time complexity: O(n+mlogm)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:No

# Pattern: Frequncy sorting 

"""
# Revision Problems — Complement Lookup

### Two Sum (LC 1)

Pattern: Complement Lookup

[ ] Solved independently
[ ] Needed hint
[ ] Submitted to LC


"""

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}

        for i in range(len(nums)):
            needed=target-nums[i]

            if needed in seen:
                return [seen[needed],i]
            seen[nums[i]]=i

print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))

# Status: solved with Hints

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:seen[nums[i]]=i  intially i was mapping seen[needed]=i

# Pattern: Complemenet Lookup

def twoSum(nums, target):
     
     for i in range(len(nums)):
          

        for j in range(len(nums)):
             
            if i!=j:
                if nums[i]+nums[j]==target:
                    return [i,j]


print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))
         

# Status: independent

# Time complexity: O(n*2)

# Space complexity: O(1)

# LC status: NA

# mistakes/confusion:Na

# Pattern: Nested Loop+Compliment lookup

"""
## New Problem

### Two Sum II — Input Array Is Sorted (LC 167)

Pattern: Complement Lookup / Two Pointers

Edge Case 1:
numbers = [2,7,11,15]
target = 9

Expected:
[1,2]

Edge Case 2:
numbers = [-1,0]
target = -1

Expected:
[1,2]

[ ] Solved independently
[ ] Needed hint
[ ] Submitted to LC


"""

def twoSum(numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}

        for i in range(len(numbers)):

            needed=target-numbers[i]

            if needed in seen:
                return [seen[needed]+1,i+1]
            seen[numbers[i]]=i


print(twoSum([2,7,11,15],9))
print(twoSum([2,3,4],6))
print(twoSum([-1,0],-1))

# Status: independent

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:NA

# Pattern: Complemenet Lookup

"""
### Contains Duplicate II (LC 219)

Pattern: Complement Lookup / Sliding Window

Edge Case 1:
nums = [1,2,3,1]
k = 3

Expected:
True

Edge Case 2:
nums = [1,2,3,1,2,3]
k = 2

Expected:
False

[ ] Solved independently
[ ] Needed hint
[ ] Submitted to LC

"""

# def containsNearbyDuplicate(nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         left=0
#         seen=set()
        
#         for right in range(len(nums)):

#             seen.add(nums[right])

#             while (right-left+1)>k:
               
#                 seen.remove(nums[left])
#                 left+=1
              
#             if nums[right] in seen:
#                 return False
            

            
#         return True

#Above Solution was wrong then seen the old solution and just fipped the true amd False conditions and sequnce of the condtions.

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
            
            seen.add(nums[right])

            while (right-left+1)>k:
                seen.remove(nums[left])
                left+=1

            
        return False

print(containsNearbyDuplicate([1,2,3,1],3))
print(containsNearbyDuplicate([1,0,1,1],1))
print(containsNearbyDuplicate([1,2,3,1,2,3],2))

# Status: solved by seen old solution.

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:NA

# Pattern: Complemenet Lookup+sliding window.


# Revision Problems — Prefix Sum

"""
# Running Sum of 1D Array (LC 1480)


Pattern: Prefix Sum

[ ] Solved independently
[ ] Needed hint
[ ] Submitted to LC

"""

def runningSum(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        running_sum=[nums[0]]
       

        for i in range(1,len(nums)):
            running_sum.append(running_sum[i-1]+nums[i])
        
        return running_sum

print(runningSum([1,2,3,4]))
print(runningSum([1,1,1,1,1]))
print(runningSum([3,1,2,10,1]))


# Status: independent

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:NA

# Pattern: prefix sum

"""

### Find Pivot Index (LC 724)

Pattern: Prefix Sum

[ ] Solved independently
[ ] Needed hint
[ ] Submitted to LC

"""

def pivotIndex(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum=0
        totalsum=sum(nums)

        for i in range(len(nums)):

            right_sum=totalsum - left_sum -nums[i]

            if left_sum==right_sum:
                return i
            left_sum+=nums[i]
        return -1
print(pivotIndex([1,7,3,6,5,6]))
print(pivotIndex([1,2,3]))
print(pivotIndex([2,1,-1]))

# Status: independent

# Time complexity: O(n)

# Space complexity: O(1)

# LC status: Accepted

# mistakes/confusion:NA

# Pattern: prefix sum

"""
### Find Highest Altitude (LC 1732)

Pattern: Prefix Sum

[ ] Solved independently
[ ] Needed hint
[ ] Submitted to LC

"""

def largestAltitude(gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt=0
        best=0

        for i in range(len(gain)):
            alt+=gain[i]
            best=max(best,alt)
        return best
        
print(largestAltitude([-5,1,5,0,-7]))
print(largestAltitude([-4,-3,-2,-1,4,3,2]))

# Status: independent

# Time complexity: O(n)

# Space complexity: O(1)

# LC status: Accepted

# mistakes/confusion:NA

# Pattern: prefix sum


"""
### Product of Array Except Self (LC 238)

Pattern: Prefix Sum

[ ] Solved independently
[ ] Needed hint
[ ] Submitted to LC

"""

def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left=[1]

        for i in range(1,len(nums)):
            left.append(left[i-1]*nums[i-1])
        
        right=[None]*len(nums)

        right[-1]=1

        for j in range(len(nums)-2,-1,-1):

            right[j]=right[j+1]*nums[j+1]
        
        output=[]

        for k in range(len(nums)):

            output.append(left[k]*right[k])
        return output

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))



# Status: independent

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:intially i have assigned left[0]=nums[0] and right[-1]=nums[-1]

# Pattern: prefix sum

"""
## New Problem

### Range Sum Query — Immutable (LC 303)

Pattern: Prefix Sum

Edge Case 1:

nums = [-2,0,3,-5,2,-1]

sumRange(0,2)

Expected:
1

Edge Case 2:

sumRange(2,5)

Expected:
-1

[ ] Solved independently
[ ] Needed hint
[ ] Submitted to LC

-

"""

#The problem Not understood.

"""
## New Problem

### Contiguous Array (LC 525)

Pattern: Prefix Sum + Hash Map

Edge Case 1:

nums = [0,1]

Expected:
2

Edge Case 2:

nums = [0,1,0]

Expected:
2

[ ] Solved independently
[ ] Needed hint
[ ] Submitted to LC

"""


#Not Solved

"""
### Remove Duplicates from Sorted Array (LC 26)

Edge Case 1:
nums = [1,1,2]

Expected Length:
2

Edge Case 2:
nums = [0,0,1,1,1,2,2,3,3,4]

Expected Length:
5

[ ] Solved independently
[ ] Needed hint
[ ] Submitted to LC

"""

def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        write=1
        
        for read in range(1,len(nums)):

            if nums[write-1]!=nums[read]:
                nums[write]=nums[read]
                write+=1
        return write

print(removeDuplicates([1,1,2]))


# Status: Solved with hints

# Time complexity: O(n)

# Space complexity: O(1)

# LC status: Accepted

# mistakes/confusion:NA

# Pattern: Two pointers+Inplace swap


"""
### Remove Element (LC 27)

Edge Case 1:
nums = [3,2,2,3]
val = 3

Expected Length:
2

Edge Case 2:
nums = [0,1,2,2,3,0,4,2]
val = 2

Expected Length:
5

[ ] Solved independently
[ ] Needed hint
[ ] Submitted to LC

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
print(removeElement([3,2,2,3],3))
print(removeElement([0,1,2,2,3,0,4,2],2))


# Status: Solved independent

# Time complexity: O(n)

# Space complexity: O(1)

# LC status: Accepted

# mistakes/confusion:NA

# Pattern: Two pointers+Inplace swap


"""
### Length of Last Word (LC 58)

Edge Case 1:
s = "Hello World"

Expected:
5

Edge Case 2:
s = "   fly me   to   the moon  "

Expected:
4

[ ] Solved independently
[ ] Needed hint
[ ] Submitted to LC


"""

#Not Solved

     
     











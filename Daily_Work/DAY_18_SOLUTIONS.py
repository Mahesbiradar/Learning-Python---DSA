## Revision Problems (5 problems)

"""
### Max Consecutive Ones III (LC 1004)
Pattern: Sliding Window
Due: 24h revision — independent D17 — ready to submit
Constraint: 1 <= nums.length <= 10^5; nums[i] is 0 or 1; 0 <= k <= nums.length.
Goal: Reproduce independently. Two valid approaches — zero-counter integer OR frequency map. Aim for the O(1) space version.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""


def longestOnes(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        Zero_p=0
        left=0
        best=0

        for right in range(len(nums)):

            if nums[right]==0:
                Zero_p+=1
            
            if Zero_p>k:
                if nums[left]==0:
                    Zero_p-=1
                left+=1
            best=max(best,right-left+1)
        return best

print(longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))
print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))



# Status:independent solve
# Time complexity:O(n)
# Space complexity:O(1)
# LC status:Accepted
# Core invariant: Zero_p>k
# What caused invalidity: if zero count is greter than k the window is invalid.
# Key mistake:NA
# Recognition trigger:consecative ones.
# Pattern:variable size Slidinig Window

"""
### Find All Anagrams in a String (LC 438)
Pattern: Sliding Window + Frequency Hashing
Due: 24h revision — hint-needed D17 — must solve independently this time
Constraint: 1 <= s.length, p.length <= 3 * 10^4; both lowercase English letters.
Goal: Solve fully independently. Focus on: fixed window of `len(p)`, when to delete a key (count == 0), appending `left` (not `right`) to result.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___
"""

def findAnagrams(s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        seen_p={}
        for i in p:
            seen_p[i]=seen_p.get(i,0)+1
        seen_s={}
        left=0
        result=[]

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

print(findAnagrams("cbaebabacd","abc"))
print(findAnagrams("abab","ab"))


# Status:independent solve
# Time complexity:O(n)
# Space complexity:O(n)
# LC status:Accepted
# Core invariant: window size > len(p)
# What caused invalidity: if window size is greter than the len of the string 'p' the window is invalid.
# Key mistake:NA
# Recognition trigger:All anagrams.
# Pattern:fixed size Slidinig Window

"""
### Group Anagrams (LC 49)
Pattern: Grouping Hash Maps
Due: 7d final recall
Constraint: 1 <= strs.length <= 10^4; strs[i] consists of lowercase English letters.
Goal: Sorted-key grouping from memory in under 5 minutes. This is the final scheduled recall.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""


def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        seen={}

        for strings in strs:

            sorted_s=sorted(strings)
            stri="".join(sorted_s)

            if stri in seen:
                seen[stri]+=[strings]
            else:
                seen[stri]=[strings]
        return seen.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams(["a"]))
# Status:independent solve
# Time complexity:O(n)
# Space complexity:O(n)
# LC status:Accepted
# Key mistake:NA
# Recognition trigger:group anagrams
# Pattern:Frequncy Hashing.

"""
### Find Pivot Index (LC 724)
Pattern: Prefix Sum
Due: 7d final recall
Constraint: 1 <= nums.length <= 10^4; -1000 <= nums[i] <= 1000; return -1 if no pivot exists.
Goal: One-pass O(n) solution from memory. Recall: `right = total - left - nums[i]`. Final scheduled recall.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

def pivotIndex(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        totalsum=sum(nums)

        for i in range (len(nums)):
            right=totalsum-left-nums[i]

            if left==right:
                return i
            left+=nums[i]
        return -1
print(pivotIndex([1,7,3,6,5,6]))
print(pivotIndex([1,2,3]))
print(pivotIndex([2,1,-1]))

# Status: solved independent 
# Time complexity: O(n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:prefix sum 

"""
451. Sort Characters By Frequency

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.


Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
 
"""
def sortchars(s):
     
    seen={}

    for i in s:
          seen[i]=seen.get(i,0)+1
    
    bucket=[]

    for j in range(len(s)+1):
         bucket.append([])
    
    for key,Value in seen.items():
         
         bucket[Value].append(key)
        

    string=""

    for char_freq in range(len(bucket)-1,-1,-1):
         
         for char in bucket[char_freq]:
              string+=char*char_freq


    return string

print(sortchars("cccaaa"))
print(sortchars("tree"))
print(sortchars("Aabb"))

# Status: solved independent 
# Time complexity: O(n)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:Frequency Hahing/Bucket sorting.


"""
350. Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

"""

def intersection_arrays(nums1,nums2):
     
    seen_nums2={}

    for i in nums2:
          seen_nums2[i]=seen_nums2.get(i,0)+1
    
    result=[]

    for j in range(len(nums1)):
         
         if nums1[j] in seen_nums2 and seen_nums2[nums1[j]]>0:
              
              result.append(nums1[j])

              seen_nums2[nums1[j]]-=1
    return result

print(intersection_arrays([1,2,2,1],[2,2]))
print(intersection_arrays([4,9,5],[9,4,9,8,4]))

# Status: solved independent 
# Time complexity: O(n)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:Frequency hashing.

"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

"""

def productExceptSelf(nums):
     
     left=[1]

     for i in range(1,len(nums)):
          
        left.append(left[i-1]*nums[i-1])
     
     right=[None]*len(nums)
     right[-1]=1

     for j in range(len(right)-2,-1,-1):
          
        right[j]=right[j+1]*nums[j+1]
     
     result=[]

     for k in range(len(nums)):
        
        result.append(left[k]*right[k])



     return result

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))

"""
### Contains Duplicate II (LC 219)
Pattern: Sliding Window
Due: 24h revision — independent D17 — ready to submit
Constraint: 1 <= nums.length <= 10^5; -10^9 <= nums[i] <= 10^9; 0 <= k <= 10^5.
Goal: Reproduce the set-based fixed window independently. Focus on: check before add, shrink when set size exceeds k.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___


"""

def containsNearbyDuplicate(nums,k):
     
     seen=set()

     left=0

     for i in range(len(nums)):
          
          if nums[i] in seen:
               return True
          seen.add(nums[i])
          
          if i-left+1>k:
               seen.remove(nums[left])
               left+=1
     return False

print(containsNearbyDuplicate([1,2,3,1],3))
print(containsNearbyDuplicate([1,0,1,1],1))
print(containsNearbyDuplicate([1,2,3,1,2,3],2))

# Status:independent solve
# Time complexity:O(n)
# Space complexity:O(n)
# LC status:Accepted
# Core invariant: window size > k
# What caused invalidity: if window size is greter than the k the window is invalid.
# Key mistake:NA
# Recognition trigger:containsNearbyDuplicate
# Pattern:fixed size Slidinig Window
               
          

def numberOfSpecialChars(word):
     
    seen={}
    for char in word:
          seen[char.lower()]=seen.get(char.lower(),0)+1
    
    return seen

print(numberOfSpecialChars("aaAbcBC"))

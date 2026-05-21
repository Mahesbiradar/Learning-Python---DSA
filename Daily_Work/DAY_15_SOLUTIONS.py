
## Revision Problems (5 problems)


"""
### Product of Array Except Self (LC 238)
Pattern: Prefix Sum
Due: 3d recall
Constraint: 2 <= nums.length <= 10^5; answer fits in 32-bit integer; solve without division in O(n).
Goal: Solve independently. If confident -> submit to LC after.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC - Result: ___

"""
#Brute Force:Using Nested Loop

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]

        for i in range(len(nums)):

            product=1
            
            for j in range(len(nums)):

                if i!=j:
                    product*=nums[j]
            
            result.append(product)
        return result

# Status:solved independent
# Time complexity:O(n^2)
# Space complexity:O(1)
# LC status:NA
# mistakes/confusion:NA
# Pattern:Prefix sum

# Core invariant:product*=nums[j] except the self index.
# Optimization jump:NA
# Key decision:Skipping the current elemeny while calculating product
# Recognition trigger:Product of Array
# Wrong assumption:
# One-line explanation:we colaculates the product of array with each iteration except self.


#optimla solution:using left and right arrays.

class Solution(object):
    def productExceptSelf(self, nums):
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
        
        result=[]

        for k in range(len(nums)):
            result.append(left[k]*right[k])
        return result
    
# Status:solved independently
# Time complexity:O(n)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:Prefix sum

# Core invariant:
# Optimization jump:intead of calculating prefix for each iteration will calculate with right and left arrays
# Key decision:
# Recognition trigger:product of array
# Wrong assumption:NA
# One-line explanation:calc right and left array except selt and then multiply both arrays.

"""
### Find Highest Altitude (LC 1732)
Pattern: Prefix Sum
Due: 3d recall
Constraint: 1 <= gain.length <= 100; altitude starts at 0.
Goal: Solve independently. If confident -> submit to LC after.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC - Result: ___

"""

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max_alt=0
        prefix=0

        for i in range(len(gain)):
            prefix+=gain[i]

            if prefix>max_alt:
                max_alt=prefix
        return max_alt

# Status: solved independent
# Time complexity:O(n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:na
# Pattern:prefix sum 

# Core invariant:
# Optimization jump:NA
# Key decision:Storing the Max altitude if the bike gains at any point
# Recognition trigger:max altitude point.
# Wrong assumption:NA
# One-line explanation:running the prefix with each iteration and storing the max altitute gain.

"""
### Isomorphic Strings (LC 205)
Pattern: Grouping Hash Maps
Due: 3d recall
Constraint: 1 <= s.length <= 5 * 10^4; s and t have equal length and contain valid ASCII characters.
Goal: Solve independently. If confident -> submit to LC after.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC - Result: ___

"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        s_t={}
        t_s={}


        for i in range(len(s)):

            if s[i] in s_t and s_t[s[i]]!=t[i]:
                return False 
            else:
                s_t[s[i]]=t[i]
            
            if t[i] in t_s and t_s[t[i]]!=s[i]:
                return False
            else:
                t_s[t[i]]=s[i]
        
        return True
    

# Status: solved independent
# Time complexity:O(n)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:
# Pattern:Grouping Hasmap

# Core invariant:
# Optimization jump:
# Key decision: mapping key value pair for both stirng in vice-versa
# Recognition trigger:isomorphic 
# Wrong assumption:
# One-line explanation: map both string each other in hashing and then check all are mapped uniquly or not.


"""
### Two Sum (LC 1)
Pattern: Complement Lookup
Due: 7d final recall
Constraint: 2 <= nums.length <= 10^4; exactly one valid answer exists; do not use the same element twice.
Goal: Solve independently. If confident -> submit to LC after.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC - Result: ___

"""

#Brute Force:

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):

            for j in range(i+1,len(nums)):

                if nums[i]+nums[j]==target:
                    return [i,j]

# Status: solved independently
# Time complexity:O(n^2)
# Space complexity:O(1)
# LC status:Na
# mistakes/confusion:Na
# Pattern:Complement Check

# Core invariant:
# Optimization jump:
# Key decision:
# Recognition trigger:
# Wrong assumption:
# One-line explanation:


#optimal solution: complement Lookup

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}

        for i in range(len(nums)):

            current=nums[i]
            needed=target - current

            if needed in seen:
                return [seen[needed],i]
            
            seen[current]=i
        
# Status: solved independent
# Time complexity:O(n)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:Na
# Pattern:Coplement Lookup

# Core invariant:
# Optimization jump:
# Key decision:
# Recognition trigger:
# Wrong assumption:
# One-line explanation:

"""
### Valid Anagram (LC 242)
Pattern: Frequency Hashing
Due: 7d final recall
Constraint: 1 <= s.length, t.length <= 5 * 10^4; strings contain lowercase English letters.
Goal: Solve independently. If confident -> submit to LC after.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC - Result: ___

"""

#Brute Force:


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        
        for i in range(len(s)):

            count1=0
            count2=0

            for j in range(len(s)):
                if s[i]==s[j]:
                    count1+=1
            for k in range(len(t)):
                if s[i]==t[k]:
                    count2+=1
            if count1!=count2:
                return False
        return True

# Status: solved independent
# Time complexity: O(n^2)
# Space complexity:O(1)
# LC status:Na
# mistakes/confusion:Na
# Pattern:Frequncy Check of elements.

# Core invariant:
# Optimization jump:
# Key decision:
# Recognition trigger:
# Wrong assumption:
# One-line explanation:

#optimal Solution using Frequncy Hashing.


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        seen1={}

        for i in s:
            seen1[i]=seen1.get(i,0)+1
        
        seen2={}

        for j in t:
            seen2[j]=seen2.get(j,0)+1
        
        for k in range (len(s)):

            if s[k] not in seen2:
                return False
            
            if seen1[s[k]]!=seen2[s[k]]:
                return False

        return True

# Status: solved independent
# Time complexity: O(n)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:Na
# Pattern:Frequncy Hashing

# Core invariant:
# Optimization jump:
# Key decision:
# Recognition trigger:
# Wrong assumption:
# One-line explanation:

## New Problems (3 problems, local only)

"""
### Maximum Average Subarray I (LC 643)
Pattern: Sliding Window
Difficulty: Easy
Given an integer array `nums` and an integer `k`, find the contiguous subarray of length `k` with the maximum average value. Return that maximum average.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: The best window is [12,-5,-6,50], whose average is 51 / 4 = 12.75.

Example 2:
Input: nums = [5], k = 1
Output: 5.0

Constraints:
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4


"""

def findMaxAverage(nums,k):

    subarraysum=0
    max_subarray=float('-inf')
    best_start = 0
    
    for right in range(len(nums)):
        subarraysum+=nums[right]

        if right>=k:
            subarraysum-=nums[right-k]
        
        if right>=k-1:
            if subarraysum>max_subarray:
                max_subarray=subarraysum
                best_start=right-k+1

    return max_subarray/k,best_start

print(findMaxAverage([1,12,-5,-6,50,3],4))
print(findMaxAverage([5],1))
print(findMaxAverage([5],1))

# Status:understood the Concept and solved with hints.
# Time complexity:O(n)
# Space complexity:O(1)
# LC status:NA
# mistakes/confusion:NA
# Pattern:Sliding window

# Core invariant: subarraysum-=nums[right-k]
# Optimization jump:NA
# Key decision:store maxvalue only when the valid window.
# Recognition trigger:Maxsubarry average.
# Wrong assumption:To store max from before valid window size.
# One-line explanation:

"""
### Longest Substring Without Repeating Characters (LC 3)
Pattern: Sliding Window
Difficulty: Medium
Given a string `s`, return the length of the longest substring that contains no repeated characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: "abc" is a longest substring without repeated characters.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: "b" is the longest valid substring.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: "wke" is a longest valid substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s may contain letters, digits, symbols, and spaces.

"""

def lengthOfLongestSubstring(s):

    left=0
    best=0
    seen=set()

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[right])

        best=max(best,right-left+1)
    return best

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))

# Status:solved but seen the hints during the topic exploration
# Time complexity: O(n)
# Space complexity:O(1)
# LC status:NA
# mistakes/confusion:Na
# Pattern:sliding Window

# Core invariant:
# Optimization jump:
# Key decision:
# Recognition trigger:
# Wrong assumption:
# One-line explanation:


"""
### Minimum Size Subarray Sum (LC 209)
Pattern: Sliding Window
Difficulty: Medium
Given an array of positive integers `nums` and a positive integer `target`, return the length of the smallest contiguous subarray whose sum is at least `target`. Return 0 if no such subarray exists.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: [4,3] is the shortest valid subarray.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4

"""

def minSubArrayLen(nums,target):


    left=0
    subarraysum=0
    min_lenght=float('inf')

    for i in range(len(nums)):

        subarraysum+=nums[i]

        # if subarraysum>=target:
        #     min_lenght=min(min_lenght,i-left+1)

        while subarraysum>=target:
            min_lenght=min(min_lenght,i-left+1)
            subarraysum-=nums[left]
            left+=1
    if min_lenght==float('inf'):
        return 0
    
    return min_lenght
        
        
    
print(minSubArrayLen([2,3,1,2,4,3],7))
print(minSubArrayLen([1,4,4],4))
print(minSubArrayLen([1,1,1,1,1,1,1,1],11))

# Status: solved with hints
# Time complexity: O(n)
# Space complexity:O(1)
# LC status:Na
# mistakes/confusion:Na
# Pattern:Sliding window

# Core invariant:
# Optimization jump:
# Key decision:Expanding and shrinking
# Recognition trigger:Subarray
# Wrong assumption:
# One-line explanation:
# Day 22 — May 28, 2026 — Consolidation
## Concept Warm-Up (5 min)
# Write the Sliding Window template from memory. No notes.
# Include both fixed-size and variable-size variants.

#fixed Size 

nums=[1,3,5,2,7,9,3]
left=0
k=2
subarraysum=0
best=0

for right in range(len(nums)):
    subarraysum+=nums[right]

    if right-left+1>k:
        subarraysum-=nums[left]
        left+=1
    
    best=max(best,subarraysum)

print(best)

# varoable Size
s = "abcabcbb"
seen={}
left=0
best=0

for right in range(len(s)):

    if s[right] in seen:
        seen[s[left]]-=1
        
        if seen[s[left]]==0:
            del seen[s[left]]
        left+=1
    
    seen[s[right]]=seen.get(s[right],0)+1

    print(seen)

    best=max(best,right-left+1)

print(best)
    

## Revision Problems — OVERDUE (9 problems)

"""
### Find Pivot Index (LC 724)
Pattern: Prefix Sum
Due: 14d recall — OVERDUE 4 days (was due May 24)
Constraint: 1 <= nums.length <= 10^4; -1000 <= nums[i] <= 1000
Goal: Running prefix sum. At each index, left sum equals total sum minus left sum minus current element. Reproduce independently.
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

        for i in range(len(nums)):

            right=totalsum-left-nums[i]

            if left==right:
                return i
            left+=nums[i]
        return -1
print(pivotIndex([1,7,3,6,5,6]))
print(pivotIndex([1,2,3]))

# Status:solved independent 
# Time complexity:O(n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:Na
# Pattern:Two pointers along with total sum.

"""
### Sort Characters By Frequency (LC 451)
Pattern: Frequency Sorting
Due: 14d recall — OVERDUE 4 days (was due May 24)
Constraint: 1 <= s.length <= 5 * 10^5; s consists of uppercase and lowercase English letters and digits
Goal: Count frequencies, sort by frequency descending, reconstruct string. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

def frequencySort(s):
        """
        :type s: str
        :rtype: str
        """
        seen={}

        for i in s:
            seen[i]=seen.get(i,0)+1
        
        bucket=[]

        for buk in range(len(s)+1):
            bucket.append([])
        
        for key,value in seen.items():
            bucket[value].append(key)
        
        op_str=""

        for index in range(len(bucket)-1,-1,-1):

            for char in bucket[index]:
                op_str+=char*index

        return op_str

print(frequencySort("tree"))
print(frequencySort("cccaaa"))
print(frequencySort("Aabb"))

    
# Status:solved independent 
# Time complexity:O(n)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:Na
# Pattern:Frequncy Hashing and bucket sorting.

"""
### Intersection of Two Arrays II (LC 350)
Pattern: Frequency Hashing
Due: 14d recall — OVERDUE 4 days (was due May 24)
Constraint: 1 <= nums1.length, nums2.length <= 1000; 0 <= nums1[i], nums2[i] <= 1000
Goal: Hash map frequency count of smaller array, iterate larger array and decrement. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

def intersect( nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        seen={}

        for i in nums2:
            seen[i]=seen.get(i,0)+1
        
        result=[]

        for j in nums1:

            if j in seen and seen[j]>0:
                result.append(j)
                seen[j]-=1
        
        return result

print(intersect([1,2,2,1],[2,2]))
print(intersect([4,9,5],[9,4,9,8,4]))

# Status:solved independent 
# Time complexity:O(n)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:Na
# Pattern:Frequency hashing.


"""

### Isomorphic Strings (LC 205)
Pattern: Grouping Hash Maps
Due: 7d final recall — OVERDUE 3 days (was due May 25)
Constraint: 1 <= s.length <= 5 * 10^4; t.length == s.length; s and t consist of any valid ascii character
Goal: Two hash maps — s→t mapping and t→s mapping. Verify bijection at each character. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""
def isIsomorphic(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
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
print(isIsomorphic("egg","add"))
print(isIsomorphic("paper","title"))
print(isIsomorphic("f11","b23"))

# Status:solved by seen old solution for hint.
# Time complexity:O(n)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:Na
# Pattern:Frequency hashing.

"""
### Longest Substring Without Repeating Characters (LC 3)
Pattern: Sliding Window
Due: 3d recall — OVERDUE 3 days (was due May 25)
Constraint: 0 <= s.length <= 5 * 10^4
Goal: Variable window with hash set for uniqueness. Expand right, shrink left until duplicate removed. Track max length. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

def lengthOfLongestSubstring( s):
        """
        :type s: str
        :rtype: int
        """
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


# Status:solved independent
# Time complexity:O(n)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:Here initially to remove seen chars in set i used if instead of while loop which remove only 1 item not left substring.
# Pattern:variable size sliding window.

"""
### Minimum Size Subarray Sum (LC 209)
Pattern: Sliding Window
Due: 3d recall — OVERDUE 3 days (was due May 25)
Constraint: 1 <= target <= 10^9; 1 <= nums.length <= 10^5; 1 <= nums[i] <= 10^4
Goal: Variable window — expand right, shrink left while sum >= target. Track min length. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___


"""
def minSubArrayLen(target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left=0
        subarraysum=0
        best=float('inf')

        for right in range(len(nums)):

            subarraysum+=nums[right]

            while subarraysum>=target:
                best=min(best,right-left+1)
                subarraysum-=nums[left]
                left+=1
        
        if best==float('inf'):
            return 0
        return best
print(minSubArrayLen(7,[2,3,1,2,4,3]))
print(minSubArrayLen(4,[1,4,4]))
print(minSubArrayLen(11,[1,1,1,1,1,1,1,1]))


# Status:solved independent
# Time complexity:O(n)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:initialy i have not read the problems correctly which stating min lenght of equal or greater Than target so i made solution for just equal to target.
# Pattern:variable size sliding window.

"""
### Fruits Into Baskets (LC 904)
Pattern: Sliding Window
Due: 3d recall — OVERDUE 2 days (was due May 26)
Constraint: 1 <= fruits.length <= 10^5; 0 <= fruits[i] < fruits.length
Goal: Variable window — at most 2 distinct fruit types. Hash map count, shrink when > 2 types. Track max length. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

def totalFruit(fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left=0
        seen={}
        best=0

        for right in range(len(fruits)):

            seen[fruits[right]]=seen.get(fruits[right],0)+1

            if len(seen)>2:
                seen[fruits[left]]-=1

                if seen[fruits[left]]==0:
                    del seen[fruits[left]]
                left+=1
            
            best=max(best,right-left+1)
            
        return best

print(totalFruit([1,2,1]))
print(totalFruit([0,1,2,2]))
print(totalFruit([1,2,3,2,2]))



# Status:solved independent
# Time complexity:O(n)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:Na
# Pattern:Frequency hashing.

"""
### Subarray Sum Equals K (LC 560)
Pattern: Prefix Sum
Due: 7d final recall — OVERDUE 2 days (was due May 26)
Constraint: 1 <= nums.length <= 2 * 10^4; -1000 <= nums[i] <= 1000; -10^7 <= k <= 10^7
Goal: Hash map of prefix sum frequencies. At each step, check if current_sum - k exists in map. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""
#This is initial approch but some of the hidden testcaes Failed.

def subarraySum(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left=0
        subarraysum=0
        count=0

        for right in range(len(nums)):

            subarraysum+=nums[right]

            while subarraysum>k:
                subarraysum-=nums[left]
                left+=1
            
            if subarraysum==k:
                count+=1
            

        return count

# 
def subarraySum(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix=0
        count=0
        seen={0:1}

        for right in range(len(nums)):

            prefix+=nums[right]
            count+=seen.get(prefix-k,0)
            seen[prefix]=seen.get(prefix,0)+1
        return count

print(subarraySum([1,1,1],2))
print(subarraySum([1,2,3],3))


# Status:solved by seen the old solution as the prv code i tried failed with some hidden test cases.
# Time complexity:O(n)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:Make this problem as shaky as ill try to solve once again.
# Pattern:Frequency hashing.

"""
### Maximum Subarray (LC 53)
Pattern: Running-State Tracking
Due: 7d final recall — OVERDUE 2 days (was due May 26)
Constraint: 1 <= nums.length <= 10^5; -10^4 <= nums[i] <= 10^4
Goal: Kadane's algorithm — at each step, max_ending_here = max(nums[i], max_ending_here + nums[i]). Track global max. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum=nums[0]
        max_sum=nums[0]

        for i in range(1,len(nums)):

            current_sum=max(nums[i],current_sum+nums[i])
            max_sum=max(max_sum,current_sum)
        return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1]))
print(maxSubArray([5,4,-1,7,8]))


# Status:solved independent
# Time complexity:O(n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:Na
# Pattern:Running state Tracking

## Revision Problems — DUE TODAY (12 problems)

"""
### Valid Palindrome (LC 125)
Pattern: Two Pointers
Due: 14d recall — May 28
Constraint: 1 <= s.length <= 2 * 10^5; s consists only of printable ASCII characters
Goal: Two pointers from ends, skip non-alphanumeric, compare lowercase chars. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        left=0
        right=len(s)-1

        while left<right:

            while left<right and not s[left].isalnum():
                left+=1
       
            
            while left<right and not s[right].isalnum():
                right-=1
         
        

            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))

# Status:solved independent
# Time complexity:O(n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:Na
# Pattern:two pointers.

"""
### Reverse String (LC 344)
Pattern: Two Pointers
Due: 14d recall — May 28
Constraint: 1 <= s.length <= 10^5; s[i] is a printable ascii character
Goal: In-place swap with two pointers from ends moving inward. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___


"""
print("The Program")

def reverseString(s):
    left=0
    right=len(s)-1


    while left<right:

        s[left],s[right]=s[right],s[left]

        left+=1
        right-=1
    return s

print(reverseString(["h","e","l","l","o"]))
print(reverseString(["H","a","n","n","a","h"]))
        
# Status:solved independent
# Time complexity:O(n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:Intially i used for loop later realized the mistake.
# Pattern:two pointers.

"""
### Is Subsequence (LC 392)
Pattern: Two Pointers
Due: 14d recall — May 28
Constraint: 0 <= s.length <= 100; 0 <= t.length <= 10^4; s and t consist only of lowercase English letters
Goal: Two pointers — advance t pointer always, advance s pointer only on match. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

def isSubsequence(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        if not t:
            return False
        pointer=0

        for i in range(len(t)):

            if t[i]==s[pointer]:
                pointer+=1
            
            if len(s)==pointer:
                return True
        return False

print(isSubsequence("abc","ahbgdc"))
print(isSubsequence("axc","ahbgdc"))


# Status:solved independent
# Time complexity:O(n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:
# Pattern:two pointers.

"""
### Top K Frequent Elements (LC 347)
Pattern: Frequency Sorting
Due: 14d recall — May 28
Constraint: 1 <= nums.length <= 10^5; -10^4 <= nums[i] <= 10^4; k is in range [1, number of unique elements]
Goal: Frequency map + heap/sort to get top k. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

def topkelements(nums,k):
     
     seen={}

     for i in nums:
          seen[i]=seen.get(i,0)+1
    
     sorted_seen=sorted(seen.items(),key=lambda x:x[1],reverse=True)

     result=[]

     for key,values in sorted_seen:
          result.append(key)

          if len(result)==k:
               return result

print(topkelements([1,1,1,2,2,3,4,],2))
          



        








        


## Concept Warm-Up (5 min)
# Fixed-size sliding window (size k)
nums=[0,1,2,4,6,3,4]
k=3
current_subarray=0
max_res=0

for right in range(len(nums)):
    current_subarray+=nums[right]

    if right>=k:
        current_subarray-=nums[right-k]
    
    if right>=k-1:
        max_res=max(max_res,current_subarray)
print(max_res)

# Variable-size sliding window

s = "abcabcbb"

seen=set()
left=0
best=0

for right in range(len(s)):


    while s[right] in seen:
        seen.remove(s[left])
        left+=1
    
    seen.add(s[right])

    best=max(best,right-left+1)

print(best)

### Revision Problems (5 problems)

"""
### Longest Repeating Character Replacement (LC 424)
Pattern: Sliding Window
Due: 24h revision — hint-needed D16
Constraint: 1 <= s.length <= 10^5; s consists of only uppercase English letters; 0 <= k <= s.length.
Goal: Recall the key invariant from memory: `window_size - max_frequency <= k`. Solve fully independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left=0
        seen={}
        best_len=0
        max_freq=0

        for right in range(len(s)):

            seen[s[right]]=seen.get(s[right],0)+1
            max_freq=max(max_freq,max(seen.values()))

            while (right-left+1)-max_freq>k:

                seen[s[left]]-=1
                
                if seen[s[left]]==0:
                    del seen[s[left]]
                left+=1
            
            best_len=max(best_len,right-left+1)
        return best_len
    
# Status: Solved independent but for debug seen old solution.
# Time complexity: O(n)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:sliding window + Frequency Hashing.

"""
### Permutation in String (LC 567)
Pattern: Sliding Window + Frequency Hashing
Due: 24h revision — hint-needed D16
Constraint: 1 <= s1.length, s2.length <= 10^4; both strings consist of lowercase English letters.
Goal: Recall the fixed-window frequency-matching approach independently. Focus on: when to delete a key vs set to 0.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

def checkInclusion(s1, s2):
    
    seen1={}
    for i in s1:
        seen1[i]=seen1.get(i,0)+1
    seen2={}
    left=0

    for right in range(len(s2)):
            
        seen2[s2[right]]=seen2.get(s2[right],0)+1

        while right-left+1>len(s1):
            seen2[s2[left]]-=1

            if seen2[s2[left]]==0:
                del seen2[s2[left]]
            left+=1
        print("seen2",seen2,"S2[right]",s2[right])
        if seen1==seen2:
                return True
    return False

print(checkInclusion("ab","eidbaooo"))
print(checkInclusion("ab","eidboaoo"))

# Status: Solved independent
# Time complexity: O(n)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:fixed size sliding window + Frequency Hashing.

"""
### Fruits Into Baskets (LC 904)
Pattern: Sliding Window
Due: 24h revision — hint-needed D16
Constraint: 1 <= fruits.length <= 10^5; 0 <= fruits[i] < fruits.length.
Goal: Recall the "at most 2 distinct" shrink condition independently. Focus on: when to delete a key from the map.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___


"""

def totalFruit(fruits):

    seen={}
    left=0
    best=0

    for right in range(len(fruits)):
        seen[fruits[right]]=seen.get(fruits[right],0)+1

        while len(seen)>2:
            seen[fruits[left]]-=1

            if seen[fruits[left]]==0:
                del seen[fruits[left]]
            left+=1
        best=max(best,right-left+1)
    return best

print(totalFruit([1,2,1]))
print(totalFruit([0,1,2,2]))
print(totalFruit([1,2,3,2,2]))


# Status: Solved independent
# Time complexity: O(n)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:fixed size sliding window.

"""
### Group Anagrams (LC 49)
Pattern: Grouping Hash Maps
Due: 7d final recall (due May 24 — pull early)
Constraint: 1 <= strs.length <= 10^4; 0 <= strs[i].length <= 100; strs[i] consists of lowercase English letters.
Goal: Reproduce the sorted-key grouping approach independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

"""
def groupAnagrams(strs):

    seen={}
    for i in range(len(strs)):

        sorted_i=sorted(strs[i])
        str_i="".join(sorted_i)
        
        if str_i in seen:
            seen[str_i]+=[strs[i]]
        else:
            seen[str_i]=[strs[i]]
    
    return seen.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# Status: Solved independent
# Time complexity: O(n+m log m)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:Frequncy Hashing + sorting.

"""
### Find Pivot Index (LC 724)
Pattern: Prefix Sum
Due: 7d final recall (due May 24 — pull early)
Constraint: 1 <= nums.length <= 10^4; -1000 <= nums[i] <= 1000.
Goal: Recall the `left_sum == total - left_sum - nums[i]` invariant independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

"""
#Brute Force:

def pivotindex(nums):
    
    for i in range(len(nums)):

        left=0
        right=0

        for j in range(0,i):
            left+=nums[j]
        for k in range(i+1,len(nums)):
            right+=nums[k]
        if left==right:
            return i
    return -1

print(pivotindex([1,7,3,6,5,6]))
print(pivotindex([2,1,-1]))
print(pivotindex([1,2,3]))

# Status: Solved independent
# Time complexity: O(n^2)
# Space complexity:O(1)
# LC status:NA
# mistakes/confusion:NA
# Pattern:Prefix sum

#optimal solution:


def pivotindex(nums):

    left=0
    totalsum=sum(nums)

    for i in range(len(nums)):

        right=totalsum-left-nums[i]

        if left==right:
            return i
        left+=nums[i]

    return -1

print(pivotindex([1,7,3,6,5,6]))
print(pivotindex([2,1,-1]))
print(pivotindex([1,2,3]))

# Status: Solved independent
# Time complexity: O(n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:Prefix sum + total sum

"""
### Max Consecutive Ones III (LC 1004)
Pattern: Sliding Window
Difficulty: Medium
Given a binary array `nums` and an integer `k`, return the maximum number of consecutive 1s in the array if you can flip at most `k` 0s.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: Flip the two 0s at index 5 and 10. The longest run of 1s is [1,1,1,0,0,1,1,1,1,1] with length 6 (indices 0–5 after flipping index 5).

Wait — correct explanation: flip positions 4 and 5 → [1,1,1,0,1,1,1,1,1,1,0]. Longest = 6. Actually the answer is bold: `[1,1,1,0,0,**1,1,1,1,1**]` — flip indices 4,10 → run of 6. Just trust the output: 6.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
- 0 <= k <= nums.length

Hint if stuck: Variable-size window. Track the count of zeros inside the window. Window is valid while `zeros_in_window <= k`. Shrink from left when zeros exceed k.

"""
#solution using hashmap

def Consecutive_Ones(nums,k):
    left=0
    seen={}
    best=0

    for right in range(len(nums)):

        seen[nums[right]]=seen.get(nums[right],0)+1

        while seen.get(0,0)>k:
            seen[nums[left]]-=1
            left+=1
        best=max(best,right-left+1)
    return best

print(Consecutive_Ones([1,1,1,0,0,0,1,1,1,1,0],2))
print(Consecutive_Ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))

# Status: Solved independent
# Time complexity: O(n)
# Space complexity:O(n)
# LC status:NA
# mistakes/confusion:NA
# Pattern:sliding window 

#optimal solution

def Consecutive_Ones(nums,k):
    left=0
    zero_count=0
    best=0

    for right in range(len(nums)):

        if nums[right]==0:
            zero_count+=1

        while zero_count>k:
            if nums[left]==0:
                zero_count-=1
            left+=1
        best=max(best,right-left+1)
    return best

print(Consecutive_Ones([1,1,1,0,0,0,1,1,1,1,0],2))
print(Consecutive_Ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))

# Status: Solved independent
# Time complexity: O(n)
# Space complexity:O(1)
# LC status:NA
# mistakes/confusion:NA
# Pattern:sliding window 

"""
### Find All Anagrams in a String (LC 438)
Pattern: Sliding Window + Frequency Hashing
Difficulty: Medium
Given two strings `s` and `p`, return a list of all the start indices of `p`'s anagrams in `s`. You may return the answer in any order.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0, 6]
Explanation: The substring starting at index 0 is "cba" which is an anagram of "abc". The substring starting at index 6 is "bac" which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0, 1, 2]

Constraints:
- 1 <= s.length, p.length <= 3 * 10^4
- s and p consist of lowercase English letters.

Hint if stuck: Fixed-size window of length `len(p)` over `s`. Maintain a frequency map of the current window. When window size exceeds `len(p)`, remove the leftmost character (delete key if count reaches 0). Compare window map to `p` map — if equal, append `left` to result.


"""

def findAnagrams(s,p):

    seen_p={}

    for i in p:
        seen_p[i]=seen_p.get(i,0)+1
    
    left=0
    result=[]

    seen_s={}

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

# Status: Solved independent with one hint
# Time complexity: O(n)
# Space complexity:O(n)
# LC status:NA
# mistakes/confusion:NA
# Pattern:sliding window 


"""
### Contains Duplicate II (LC 219)
Pattern: Sliding Window
Difficulty: Easy
Given an integer array `nums` and an integer `k`, return `True` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: True

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: True

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: False

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 0 <= k <= 10^5

Hint if stuck: Fixed-size sliding window using a set of size at most k+1. For each new element: check if it's already in the set (duplicate within k distance) → return True. Add it, then if set size exceeds k, remove the oldest element (`nums[right - k]`).


"""

def containsNearbyDuplicate(nums,k):

    left=0
    seen=set()

    for right in range(len(nums)):

        if nums[right] in seen:
            return True
        seen.add(nums[right])
        
        while right-left+1>k:
            seen.remove(nums[left])
            left+=1
    return False

print(containsNearbyDuplicate([1,2,3,1],3))
print(containsNearbyDuplicate([1,0,1,1],1))
print(containsNearbyDuplicate([1,2,3,1,2,3],2))

# Status: Solved independent
# Time complexity: O(n)
# Space complexity:O(n)
# LC status:NA
# mistakes/confusion:NA
# Pattern:sliding window 







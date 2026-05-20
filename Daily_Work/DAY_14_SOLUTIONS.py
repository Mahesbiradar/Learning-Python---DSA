"""
## Concept Warm-Up (5 min)
Write the Running-State Tracking template from memory. No notes.

```python
# Running-State Tracking / Kadane

```
```python
# Running min/max state for product-style problems


"""

# Running-State Tracking / Kadane

# nums=[7,1,4,5,6,2]

# min_price=nums[0]
# max_profit=0

# for i in range(len(nums)):
#     if nums[i]<min_price:
#         min_price=nums[i]
#     else:
#         profit=nums[i]-min_price
#         if profit>max_profit:
#             max_profit=profit
# print(max_profit)

# #Kadane
# nums=[-2,1,-3,4,-1,2,1,-5,4]

# current_sum=nums[0]
# max_sum=float('-inf')

# for i in range(1,len(nums)):

#     current_sum=max(nums[i],current_sum+nums[i])

#     if current_sum>max_sum:
#         max_sum=current_sum
# print(max_sum)

# Running min/max state for product-style problems

def maxprod(nums):

   current_max=nums[0]
   current_min=nums[0]
   max_prod=nums[0]

   for i in range(1,len(nums)):
       
       temp_max=current_max
       temp_min=current_min

       current_max=max(nums[i],temp_max*nums[i],temp_min*nums[i])
       current_min=min(nums[i],temp_max*nums[i],temp_min*nums[i])

       max_prod=max(max_prod,current_max)

       print("i:-",nums[i],"current_max:-",current_max,"current_min:-",current_min,"max_prod:-",max_prod)
    
   return max_prod

print(maxprod([-2, 6, -3, -10, 0, 2]))
print(maxprod([-1, -3, -10, 0, 6]))


"""
### Valid Palindrome (LC 125)
Pattern: Two Pointers
Due: 3d recall
Constraint: 1 <= s.length <= 2 * 10^5; ignore non-alphanumeric characters and case.
Goal: Solve independently. If confident → submit to LC after.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

def isPalindrome(s):

    left=0
    right=len(s)-1

    while left<right:

        while left<right and not s[left].isalnum():
            left+=1
        while left<right and not s[right].isalnum():
            right-=1
        
        if s[left].upper()!=s[right].upper():
            return False
        left+=1
        right-=1
    return True
print(isPalindrome("A man, a plan, a canal: Panama"))

# Status: Solved independently
# Time complexity:O(n)
# Space complexity:O(1)
# LC status:Accepted
# Pattern:Two pointers

# Core invariant:
# Optimization jump:
# Key decision: 1>skipping the non alpha characters from both end. 
# Recognition trigger:Palindrome and two pointers
# Wrong assumption:NA
# One-line explanation:#Comparing Two pointers and moving towards center while skipping the non alpha chars.
        
"""
### Reverse String (LC 344)
Pattern: Two Pointers
Due: 3d recall
Constraint: 1 <= s.length <= 10^5; modify the input array in-place with O(1) extra memory.
Goal: Solve independently. If confident → submit to LC after.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

def reverseString(s):

    left=0
    right=len(s)-1

    while left<right:

        s[left],s[right] = s[right],s[left]

        left+=1
        right-=1
    return s
print(reverseString(["h","e","l","l","o"]))
print(reverseString(["H","a","n","n","a","h"]))

# Status:solved independently
# Time complexity: O(n)
# Space complexity:O(1)
# LC status:Accepted
# Pattern:two pointers

# Core invariant:
# Optimization jump:Since the problem stated to do revers in-Place.
# Key decision:assignment values to both pointer at a time
# Recognition trigger:two pointers and reverse string.
# Wrong assumption:
# One-line explanation:use two pointers and run a while loop and then swap the values of pointers and move towards the center.

"""
### Is Subsequence (LC 392)
Pattern: Two Pointers
Due: 3d recall
Constraint: 0 <= s.length <= 100; 0 <= t.length <= 10^4; strings contain only lowercase English letters.
Goal: Solve independently. If confident → submit to LC after.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___
"""
def isSubsequence(s,t):

    if not s:
        return True
    if not t:
        return False
    
    pointer_s=0

    for i in range(len(t)):

        if t[i]==s[pointer_s]:
            pointer_s+=1
        
        if len(s)==pointer_s:
            return True
    return False

print(isSubsequence("abc","ahbgdc"))
print(isSubsequence("axc","ahbgdc"))

# Status:solved independently
# Time complexity:O(n)
# Space complexity:O(1)
# LC status:Accepted
# Pattern:two pointers

# Core invariant:
# Optimization jump:
# Key decision:initializing the two pointers and the Second pass where the len(s)==S pointer
# Recognition trigger:Two pointer and subsequnce
# Wrong assumption:
# One-line explanation:intialize two pointers and iterate over the t if we match the elements of both sting increment s pointer and check if len(s) matches with s pointer.

"""
### Top K Frequent Elements (LC 347)
Pattern: Frequency Sorting
Due: 3d recall
Constraint: 1 <= nums.length <= 10^5; k is in range [1, number of unique elements]; answer is unique.
Goal: Solve independently. If confident → submit to LC after.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""




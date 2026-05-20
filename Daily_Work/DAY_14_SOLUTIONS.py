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
def topKFrequent(nums,k):

    seen={}

    for num in nums:
        seen[num]=seen.get(num,0)+1
    sorted_seen=sorted(seen.items(),key=lambda x:x[1],reverse=True)

    result=[]

    for key,value in sorted_seen:
        result.append(key)

        if len(result)==k:
            return result
print(topKFrequent([1,1,1,2,2,3],2))
print(topKFrequent([1],1))
print(topKFrequent([1,2,1,2,1,2,3,1,3,2],2))

# Status:solved independently
# Time complexity:O(n+m log m)
# Space complexity:O(n)
# LC status:Accepted
# Pattern:Frequncy Hashing/Second Pass

# Core invariant:sorted(seen.items(),key=lambda x:x[1],reverse=True) and len(result)==k
# Optimization jump:NA
# Key decision:Frequncy Hashing/Sorting and then Second pass to append till k elements.
# Recognition trigger:Frequent Elements
# Wrong assumption:
# One-line explanation:Map Frequency of all element then sort in decring order then append required elements in result list.

"""
### Majority Element (LC 169)
Pattern: Frequency Hashing
Due: 3d recall
Constraint: 1 <= nums.length <= 5 * 10^4; majority element always exists and appears more than n // 2 times.
Goal: Solve independently. If confident → submit to LC after.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___
"""
#Brute Force:

def majorityElement(nums):

    major_element=None
    max_count=0

    for i in nums:
        count=0

        for j in nums:

            if i==j:
                count+=1
        
        if count>max_count:
            max_count=count
            major_element=i
    return major_element
print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))

# Status:solved independently
# Time complexity:O(n^2)
# Space complexity:O(1)
# LC status:Na
# Pattern:Running state Tracking

# Core invariant:
# Optimization jump:since iterating over nums again and again for counting the Frquency we can optimize using hashing 
# Key decision:Capturing the max frequncy elements.
# Recognition trigger: Majority elements
# Wrong assumption:Na
# One-line explanation:will use two Global varible to store Max_count and element and will run a nested loop to capture the Frequncy of each element.


#optimize solution:

def majorityElement(nums):

    seen={}
    
    for num in nums:
        seen[num]=seen.get(num,0)+1
    
    major_element=None
    max_count=0

    for key, value in seen.items():

        if value>max_count:
            max_count=value
            major_element=key
    return major_element

print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))

# Status:solved independently
# Time complexity:O(n)
# Space complexity:O(n)
# LC status:Accepted
# Pattern:Frequncy Hashing + running state Tracking

# Core invariant:
# Optimization jump:
# Key decision:Frequncy of all elements and then Tracking the Running state.
# Recognition trigger:Majority element.
# Wrong assumption:Na
# One-line explanation:map all elemets frequncy using hashing the run a loop over dict and then Track max_frequncy and element associated with.

"""
53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.


Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104


"""

def maxSubArray(nums):

    max_sum=float('-inf')
   
   
    for i in range(len(nums)):

        prefix=0

        for j in range(i,len(nums)):

            prefix+=nums[j]

            if prefix>max_sum:
                max_sum=prefix
                
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([5,4,-1,7,8]))
print(maxSubArray([1]))

# Status:Solved independently 
# Time complexity:O(n^2)
# Space complexity:O(1)
# LC status:NA
# mistakes/confusion:NA
# Pattern:Running state Tracking

# Core invariant:
# Optimization jump:Repeating the prefix sum each time. so we can optimize By kadanes algo(restart/Continue Approch)
# Key decision:Tracking running state
# Recognition trigger:max_subarry
# Wrong assumption:
# One-line explanation:Here will calculate the prefix of each subarry exist and track max subarry using the nested loop.

#optimal solution

def maxsubarray(nums):

    max_sum=nums[0]
    current_max=nums[0]

    for i in range(1,len(nums)):

        current_max=max(nums[i],current_max+nums[i])

        if current_max>max_sum:
            max_sum=current_max
    return max_sum

print(maxsubarray([4,-1,2,1]))
print(maxSubArray([5,4,-1,7,8]))
print(maxSubArray([1]))

# Status:solved independently
# Time complexity:O(n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:Tracking running state/Kadane

# Core invariant: current_max=max(nums[i],current_max+nums[i])
# Optimization jump:    
# Key decision:Tracking the running state
# Recognition trigger:
# Wrong assumption:
# One-line explanation:Here with each iteration using kadanes algo we can continue with subarry or restart with current element based on max value.

"""
152. Maximum Product Subarray

Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.


"""
#brute force:using nested loop

def maxProduct(nums):

    max_prod=float('-inf')

    for i in range(len(nums)):

        prefix_prod=1

        for j in range(i,len(nums)):

            prefix_prod*=nums[j]

            if prefix_prod>max_prod:
                max_prod=prefix_prod
    return max_prod

print(maxProduct([2,3,-2,4]))
print(maxProduct([-2,0,-1]))

# Status:solved independent
# Time complexity:O(n^2)
# Space complexity:O(1)
# LC status:Na
# mistakes/confusion:NA
# Pattern:Running state tracking using Nested loop

# Core invariant:
# Optimization jump:since we are calculating prefix_prod again and again so we can optimize using min and max.
# Key decision:running state
# Recognition trigger:
# Wrong assumption:
# One-line explanation:Using nested loop we can calculate prefix of each subarray and will track max_prod of subrary in global variable.

#Optimal solution using the min and max

def maxProduct(nums):

    current_max=nums[0]
    current_min=nums[0]
    max_prod=nums[0]

    for i in range(1,len(nums)):
        n=nums[i]

        temp_max=current_max
        temp_min=current_min


        current_max=max(n,temp_max*n,temp_min*n)
        current_min=min(n,temp_max*n,temp_min*n)
        max_prod=max(max_prod,current_max)

    return max_prod

print(maxProduct([2,3,-2,4]))
print(maxProduct([-2,0,-1]))

# Status: solved independently
# Time complexity:O(n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:Running state Tracking/Min max

# Core invariant:min and max
# Optimization jump:
# Key decision:Tracking both min and max
# Recognition trigger:Product of subarray
# Wrong assumption:
# One-line explanation:While iteration we shoud use both min and max values bcz the negatives becomes max in next iteration.


"""
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

"""

#Brute Force:

def subarraySum(nums,k):

    count=0

    for i in range(len(nums)):

        prifix=0

        for j in range(i,len(nums)):

            prifix+=nums[j]

            if prifix==k:
                count+=1
    return count

print(subarraySum([1,1,1],2))
print(subarraySum([1,2,3],3))


# Status:solved independently
# Time complexity:O(n^2)
# Space complexity:O(1)
# LC status:Na
# mistakes/confusion:
# Pattern:prefix sum + second pass.

# Core invariant:
# Optimization jump:since we are calculating prefix again and again we can store it in hasmap to optimize
# Key decision:
# Recognition trigger: Subarry sum and given the value of subarray
# Wrong assumption:
# One-line explanation:


#optimal solution using the hashmap


def subarraySum(nums,k):

    seen={0:1}
    count=0
    prefix=0

    for i in range(len(nums)):

        prefix+=nums[i]
        count+=seen.get(prefix-k,0)
        seen[prefix]=seen.get(prefix,0)+1

    return count

print(subarraySum([1,1,1],2))
print(subarraySum([1,2,3],3))

# Status:solved independently
# Time complexity:O(n)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:Na
# Pattern:Prefix sum + Hash map

# Core invariant: count+=seen.get(prefix-k,0)
# Optimization jump: keeping prefix in dict
# Key decision: count+=seen.get(prefix-k,0)
# Recognition trigger: 
# Wrong assumption:
# One-line explanation: with each iteration checking the old prefix exist then incrementing the Count with frequeny of old prefix.

"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

"""

def maxProfit(nums):

    min_price=nums[0]
    max_profit=0

    for i in range(1,len(nums)):


        if nums[i]<min_price:
            min_price=nums[i]
        else:
            profit=nums[i]-min_price

            if profit>max_profit:
                max_profit=profit
    return max_profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))

# Status:Solved independent 
# Time complexity:O(n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:Na
# Pattern:Running state tracking

# Core invariant:min price(buy) before selling
# Optimization jump:NA
# Key decision:Buy stock before seeling
# Recognition trigger:
# Wrong assumption:
# One-line explanation:

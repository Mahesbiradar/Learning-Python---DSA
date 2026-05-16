#Day_10 Solutions:

## Concept Warm-Up (5 min)
# Write the Prefix Sum template from memory. No notes.
# Prefix Sum — build array where prefix[i] = sum of nums[0..i-1]

nums=[1,2,3,4,5]

left_sum=[nums[0]]

for i in range(1,len(nums)):
    left_sum.append(left_sum[i-1]+nums[i])

print(left_sum)


## Revision Problems (5 problems)

"""
### Valid Palindrome (LC 125)
Pattern: Two Pointers
Due: overdue (May 15)
Constraint: Only alphanumeric chars count. Case-insensitive. Empty string → True.
Examples: "A man, a plan, a canal: Panama" → True | "race a car" → False | " " → True
Goal: Two-pointer from both ends, skip non-alphanumeric, compare lowercased.
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
        
        if s[left].lower()!=s[right].lower():
            return False
        left+=1
        right-=1

    return True

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))

# Status: Solved with Hint
# Time complexicity: O(n)
# Space complaxicity: O(1)
# LC status: Accepted.
# mistakes/confusion: intially i was stuck for the syntax for moving pointer when char is nonalpa So taken hind for This line (while left<right and not s[left].isalnum():)
# Pattern: Two pointers.

"""
### Reverse String (LC 344)
Pattern: Two Pointers
Due: overdue (May 15)
Constraint: In-place. O(1) extra memory. Modify input array directly.
Examples: ["h","e","l","l","o"] → ["o","l","l","e","h"] | ["H","a","n","n","a","h"] → ["h","a","n","n","a","H"]
Goal: Two-pointer swap from both ends moving inward.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

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

# Status: Solved independently
# Time complexicity: O(n)
# Space complaxicity: O(1)
# LC status: Accepted.
# mistakes/confusion: NA
# Pattern: Two pointers.

"""
### Is Subsequence (LC 392)
Pattern: Two Pointers
Due: overdue (May 15)
Constraint: 0 <= s.length <= 100, 0 <= t.length <= 10^4. All lowercase.
Examples: s="abc", t="ahbgdc" → True | s="axc", t="ahbgdc" → False | s="", t="anything" → True
Goal: Two pointers — crawl t with one pointer, advance s-pointer only on match. Return s-pointer == len(s).
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

def isSubsequence(s,t):

    if not s:
        return True

    s_pointer=0

    for i in range(len(t)):

        if t[i]==s[s_pointer]:
            s_pointer+=1
        if s_pointer==len(s):
            return True
    return False

print(isSubsequence("abc","ahbgdc"))
print(isSubsequence("axc","ahbgdc"))
print(isSubsequence("","ahbgdc"))

# Status: Solved independently
# Time complexicity: O(n)
# Space complaxicity: O(1)
# LC status: Accepted.
# mistakes/confusion: NA
# Pattern: Two pointers.

"""
### Top K Frequent Elements (LC 347)
Pattern: Frequency Sorting
Due: May 16 (24h recall)
Constraint: 1 <= nums.length <= 10^5. k is always valid. Answer is unique.
Examples: [1,1,1,2,2,3], k=2 → [1,2] | [1], k=1 → [1]
Goal: Build freq dict with .get(), sort by frequency descending with lambda, return first k keys.
Write complexity: Time = O(n + m log m), Space = O(n) where m = unique values.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

"""

def topKFrequent(nums,k):

    seen={}

    for i in nums:
        seen[i]=seen.get(i,0)+1
    sorted_seen=sorted(seen.items(),key=lambda x:x[1],reverse=True)

    result=[]

    for element,count in sorted_seen:
        result.append(element)

        if len(result)==k:
            return result
    
print(topKFrequent([1,1,1,2,2,3],2))
print(topKFrequent([1],1))

# Status: Solved independently
# Time complexicity: O(n+m log m)
# Space complaxicity: O(n)
# LC status: Accepted.
# mistakes/confusion: NA
# Pattern: Frequncy Hashing/Sorting

"""
### Majority Element (LC 169)
Pattern: Frequency Hashing
Due: May 16 (24h recall)
Constraint: n >= 1. Majority element always exists (appears > n//2 times).
Examples: [3,2,3] → 3 | [2,2,1,1,1,2,2] → 2 | [1] → 1
Goal: Dict frequency version. Second pass over dict to find max. Do NOT use Counter or max() with key.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

#Brute Force Solution:

def majorityElement(nums):

    max_count=0
    majorelement=None
    for i in nums:
        count=0
        for j in nums:
            if i==j:
                count+=1
        if count>max_count:
            max_count=count
            majorelement=i
    return majorelement
print(majorityElement([2,2,1,1,1,2,2]))
print(majorityElement([3,2,3]))

# Status: Solved independently
# Time complexicity: O(n^2)
# Space complaxicity: O(1)
# LC status: Time Limit Exceeded  42 / 53 testcases passed
# mistakes/confusion: NA
# Pattern: Linear Traversal / Elements Counting.

#optimal Solution:Using Frequncy Hashing

def majorityElement(nums):

    seen={}
    for i in nums:
        seen[i]=seen.get(i,0)+1
    
    max_frequency=0
    majorelement=None

    for key,value in seen.items():

        if value>max_frequency:
            max_frequency=value
            majorelement=key
    return majorelement

print(majorityElement([2,2,1,1,1,2,2]))
print(majorityElement([3,2,3]))

# Status: Solved independently
# Time complexicity: O(n)
# Space complaxicity: O(n)
# LC status: Accepted
# mistakes/confusion: NA
# Pattern: Frequncy Hashing  / Major Element Tracking.



## New Problems (3 problems — local only, do NOT submit to LC)


"""
### Product of Array Except Self (LC 238)
Pattern: Prefix Sum (prefix × suffix products)
Difficulty: Medium
Constraints: 2 <= nums.length <= 10^5. -30 <= nums[i] <= 30. Product fits in 32-bit int. No division allowed.

Description: Given an integer array nums, return an array answer such that answer[i] equals the product of all elements of nums except nums[i].

Examples:
- [1,2,3,4] → [24,12,8,6]
- [-1,1,0,-3,3] → [0,0,9,0,0]

Hint (read only if stuck): Two passes. Left pass builds prefix products. Right pass multiplies in suffix products in-place.

"""

#Using Brute Force:Nested loop

def productExceptSelf(nums):

    result=[]

    for i in range(len(nums)):

        prod=1
        for j in range(len(nums)):

            if i!=j:
                prod*=nums[j]
        result.append(prod)

    return result

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))

# Status: Solved independently
# Time complexicity: O(n^2)
# Space complaxicity: O(n)
# LC status: NA
# mistakes/confusion: NA
# Pattern: Linera Traversal

#Using prefix and suffix prod.

def productExceptSelf(nums):
    #left pass to buid the left arry prefix
    left=[1]
    for i in range(1,len(nums)):
        left.append(left[i-1]*nums[i-1])

    #Right pass to build the right array suffix
    right=[None]*len(nums)
    right[-1]=1
    for j in range(len(nums)-2,-1,-1):
        right[j]=right[j+1]*nums[j+1]
    #Multiply both array to get a product excep self
    result=[]
    for k in range(len(nums)):
        result.append(left[k]*right[k])

    return result

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))

# Status: Solved independently
# Time complexicity: O(n)
# Space complaxicity: O(n)
# LC status: NA
# mistakes/confusion: NA
# Pattern: prefix and suffix product.


"""
### Subarray Sum Equals K (LC 560)
Pattern: Prefix Sum + Hash Map
Difficulty: Medium
Constraints: 1 <= nums.length <= 2×10^4. -1000 <= nums[i] <= 1000. -10^7 <= k <= 10^7.

Description: Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals k.

Examples:
- [1,1,1], k=2 → 2
- [1,2,3], k=3 → 2
- [3,4,7,2,-3,1,4,2], k=7 → 4

Key insight: For each prefix_sum, check if (prefix_sum - k) exists in your seen dict. Count occurrences.
Template hint:
```
prefix_sum = 0
seen = {0: 1}
count = 0
for num in nums:
    prefix_sum += num
    count += seen.get(prefix_sum - k, 0)
    seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
```

"""

def subarraySum(nums,k):
    count=0
    prefix=0
    seen={0:1}

    for num in nums:
        prefix+=num
        count+=seen.get(prefix-k,0)
        seen[prefix]=seen.get(prefix,0)+1
        print("Num:=",num, "Prefix=", prefix , "count=",count, "seen=",seen)
    
    return count

print(subarraySum([1,1,1],2))
print(subarraySum([1,2,3],3))
print(subarraySum([3,4,7,2,-3,1,4,2],7))

# Status: Solved with given Hint
# Time complexicity: O(n)
# Space complaxicity: O(m)
# LC status: NA
# mistakes/confusion: I have solved as per given hind the not understood the Concept
# Pattern: prefixsum and Frequency Map

"""
### Maximum Subarray (LC 53)
Pattern: Running-State Tracking (Kadane's algorithm)
Difficulty: Medium
Constraints: 1 <= nums.length <= 10^5. -10^4 <= nums[i] <= 10^4.

Description: Given an integer array nums, find the subarray with the largest sum and return its sum.

Examples:
- [-2,1,-3,4,-1,2,1,-5,4] → 6  (subarray [4,-1,2,1])
- [1] → 1
- [5,4,-1,7,8] → 23
- [-1,-2,-3] → -1

Key decision at each element: extend the current subarray OR start fresh from this element.
Running state: current_sum = max(nums[i], current_sum + nums[i])



"""

def maxSubArray(nums):

    current_sum=0
    max_sum=float('-inf')

    for i in range(len(nums)):

        current_sum = max(nums[i],current_sum+nums[i])

        if current_sum>max_sum:
            max_sum=current_sum
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([5,4,-1,7,8]))
print(maxSubArray([-1,-2,-3]))
print(maxSubArray([1]))

# Status: Solved with given Hint
# Time complexicity: O(n*m)
# Space complaxicity: O(1)
# LC status: NA
# mistakes/confusion: I have solved as per given hind initailly the problem state ment not understtod.
# Pattern: running state 


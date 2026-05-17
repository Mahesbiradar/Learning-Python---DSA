"""# Concept Warm-Up (5 min)
Write both templates from memory. No notes.

```python
# Prefix Sum — build array where prefix[i] = sum of nums[0..i-1]


```

```python
# Running-State Tracking (Kadane's) — extend or restart at each element



"""
# Prefix Sum — build array where prefix[i] = sum of nums[0..i-1]

def prefixsum(nums):

    prefix_sum=[0]*len(nums)
    prefix_sum[0]=nums[0]

    for i in range(1,len(nums)):
        prefix_sum[i]=prefix_sum[i-1]+nums[i]
          
    return prefix_sum

print(prefixsum([2,4,5,6,1]))


"""
## Revision Problems (5 problems — all due May 17)

### Product of Array Except Self (LC 238)
Pattern: Prefix Sum (prefix × suffix products)
Due: May 17 (24h recall)
Constraint: No division allowed. 2 <= nums.length <= 10^5.
Examples: [1,2,3,4] → [24,12,8,6] | [-1,1,0,-3,3] → [0,0,9,0,0]
Goal: Solve without hints this time. Left pass builds prefix products, right pass multiplies suffix in-place.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

"""
#Brute Force:using inner Loop

def productExceptSelf(nums):

    result=[]

    for i in range(len(nums)):
        prefix_prod=1
        for j in range(len(nums)):

            if i!=j:
                prefix_prod*=nums[j]
        result.append(prefix_prod)
    
    return result

print(productExceptSelf([1,2,3,4]))


# Status: Solved independently
# Time complexicity: O(n^2)
# Space complaxicity: O(n)
# LC status: NA
# mistakes/confusion: NA
# Pattern: Prefixproduct.

#Using optimal Solution

def productExceptSelf(nums):

    #left array
    left=[1]

    for i in range(1,len(nums)):
        left.append(left[i-1]*nums[i-1])
    #Right array
    right=[None]*len(nums)
    right[-1]=1


    for j in range(len(nums)-2,-1,-1):
        right[j]=(right[j+1]*nums[j+1])
    
    #result array left*right
    result=[]

    for k in range(len(nums)):
        result.append(left[k]*right[k])
    return result
                
print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))

# Status: Solved independently
# Time complexicity: O(n)
# Space complaxicity: O(n)
# LC status: Accepted
# mistakes/confusion: NA
# Pattern: Prefix and suffix Product

"""
### Subarray Sum Equals K (LC 560)
Pattern: Prefix Sum + Hash Map
Due: May 17 (24h recall)
Constraint: 1 <= nums.length <= 2×10^4. -10^7 <= k <= 10^7. Negative numbers allowed.
Examples: [1,1,1], k=2 → 2 | [1,2,3], k=3 → 2 | [3,4,7,2,-3,1,4,2], k=7 → 4
Goal: Reconstruct from scratch. seen = {0:1}. At each step: count += seen.get(prefix - k, 0).
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___
---
"""
#Brute Force:using nested loop

def subarraySum(nums,k):

    count=0

    for i in range(len(nums)):

        prefix_sum=0
        print("i:",i)

        for j in range(i,len(nums)):
            prefix_sum+=nums[j]

            print(prefix_sum)
            if prefix_sum==k:
                count+=1
    
    return count

# Status: Solved independently
# Time complexicity: O(n^2)
# Space complaxicity: O(1)
# LC status:
# mistakes/confusion: NA
# Pattern: Prefix sum and counter

#Using the optimal solution

print(subarraySum([3,4,7,2,-3,1,4,2],7))

def subarraySum(nums,k):

    count=0
    seen={0:1}
    prefix=0

    for num in nums:
        prefix+=num
        # print(prefix)
        count+=seen.get(prefix-k,0)
        seen[prefix]=seen.get(prefix,0)+1
        print(seen)
    return count

print(subarraySum([1,1,1],2))
print(subarraySum([1,1,1],2))
print(subarraySum([1,1,1],2))

# Status: Solved independently
# Time complexicity: O(n)
# Space complaxicity: O(n)
# LC status:NA
# mistakes/confusion: The concept Not fully Understood the code written here is from yesterdays memory recall
# Pattern: Prefix sum + hash Map

"""
### Maximum Subarray (LC 53)
Pattern: Running-State Tracking (Kadane's)
Due: May 17 (24h recall)
Constraint: 1 <= nums.length <= 10^5. -10^4 <= nums[i] <= 10^4.
Examples: [-2,1,-3,4,-1,2,1,-5,4] → 6 | [5,4,-1,7,8] → 23 | [-1,-2,-3] → -1
Goal: Two running variables: current_sum and max_sum. Decision: extend or start fresh.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""
#Brute Force:

def maxSubArray(nums):

    max_sum=float('-inf')

    for i in range(len(nums)):
        prefix_sum=0
        for j in range(i,len(nums)):
            prefix_sum+=nums[j]
            if prefix_sum>max_sum:
                max_sum=prefix_sum
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# Status: Solved independently
# Time complexicity: O(n^2)
# Space complaxicity: O(1)
# LC status:NA
# mistakes/confusion: Keep this concept in loop for one or two more days with simlar concept with diffrent Problems.
# Pattern: Counter + runnung state


def maxSubArray(nums):

    max_sum=float('-inf')
    current_sum=0

    for num in nums:

        current_sum=max(num,current_sum+num)

        if current_sum>max_sum:
            max_sum=current_sum
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([5,4,-1,7,8]))
print(maxSubArray([-1,-2,-3]))
print(maxSubArray([1]))

# Status: Solved using yesterdays solution 
# Time complexicity: O(n)
# Space complaxicity: O(1)
# LC status:NA
# mistakes/confusion: still not understood the Concept fully.
# Pattern:runnung state

"""
### Group Anagrams (LC 49)
Pattern: Grouping Hash Maps
Due: May 17 (3d recall)
Constraint: 1 <= strs.length <= 10^4. All lowercase. 0 <= strs[i].length <= 100.
Examples: ["eat","tea","tan","ate","nat","bat"] → [["bat"],["nat","tan"],["ate","eat","tea"]] | [""] → [[""]]
Goal: sorted(word) as key, append to defaultdict list. Return list of values.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___


"""
def groupAnagram(strs):

    seen={}

    for word in strs:

        sorted_word=sorted(word)

        key="".join(sorted_word)

        if key in seen:
            seen[key]+=[word]
        else:
            seen[key]=[word]


    return seen.values()

print(groupAnagram(["eat","tea","tan","ate","nat","bat"]))

# Status: solved with hints for the hashing maps syntax for appeding things in list
# Time complexicity: O(n)
# Space complaxicity: O(n)
# LC status:Accepted
# mistakes/confusion: 
# Pattern:Frequnecy map


"""
### Find Pivot Index (LC 724)
Pattern: Prefix Sum
Due: May 17 (3d recall)
Constraint: 1 <= nums.length <= 10^4. -1000 <= nums[i] <= 1000.
Examples: [1,7,3,6,5,6] → 3 | [1,2,3] → -1 | [2,1,-1] → 0
Goal: left_sum starts at 0. At each index: if left_sum == total - left_sum - nums[i] → return i. Then add nums[i] to left_sum.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

#using Brute Force:Nested Loop 

def pivotIndex(nums):

    for i in range(len(nums)):

        left_prefix=0

        for j in range(0,i):
            left_prefix+=nums[j]
        
        right=0
        for k in range(i+1,len(nums)):
            right+=nums[k]
        if left_prefix==right:
            return i
    return -1

print(pivotIndex([1,7,3,6,5,6]))

    
# Status: independent solve 
# Time complexicity: O(n^2)
# Space complaxicity: O(1)
# LC status:NA
# mistakes/confusion: 
# Pattern:Prifix and suffix sum

#optimal solution: using total sum 

def pivotIndex(nums):

    totalsum=sum(nums)
    left=0

    for i in range(len(nums)):

        right=totalsum-left-nums[i]

        if left==right:
            return i
        
        left+=nums[i]

    return -1

print(pivotIndex([1,7,3,6,5,6]))

# Status: independent solve 
# Time complexicity: O(n)
# Space complaxicity: O(1)
# LC status:Accepted
# mistakes/confusion: 
# Pattern:Prifix and suffix sum



"""
### Find the Highest Altitude (LC 1732)
Pattern: Prefix Sum (running prefix max)
Difficulty: Easy
Constraints: n == gain.length, 1 <= n <= 100, -100 <= gain[i] <= 100

Description: A biker starts at altitude 0. Given an array gain where gain[i] is the net altitude change between point i and i+1, return the highest altitude reached at any point (including the start at 0).

Examples:
- [-5,1,5,0,-7] → 1
- [-4,-3,-2,-1,4,3,2] → 0

Key insight: Build the running altitude prefix (cumulative sum), track the max. Start max at 0 (the starting altitude).

"""

def largestAltitude(gain):

    max_alt=0
    prefix_gain=0

    for i in range(len(gain)):

        prefix_gain+=gain[i]

        if prefix_gain>max_alt:
            max_alt=prefix_gain
    
    return max_alt

print("Largest alt")
print(largestAltitude([-5,1,5,0,-7]))
print(largestAltitude([-4,-3,-2,-1,4,3,2]))

# Status: independent solve 
# Time complexicity: O(n)
# Space complaxicity: O(1)
# LC status:NA
# mistakes/confusion: NA
# Pattern:Prifix sum and running state

"""
### Maximum Product Subarray (LC 152)
Pattern: Running-State Tracking (track both max and min)
Difficulty: Medium
Constraints: 1 <= nums.length <= 2×10^4, -10 <= nums[i] <= 10

Description: Given an integer array nums, find the subarray with the largest product and return the product.

Examples:
- [2,3,-2,4] → 6
- [-2,0,-1] → 0
- [-2,3,-4] → 24

Key insight: Unlike Kadane's, track both max_prod and min_prod at every step. A negative number flips min↔max. At each element: new_max = max(num, num*max_prod, num*min_prod).

"""

#Brute Force Solution:

def maxProduct(nums):

    maxSubarray_prod=float('-inf')
    

    for i in range(len(nums)):
        
        prefix_prod=1

        for j in range(i,len(nums)):

            prefix_prod*=nums[j]

            if prefix_prod>maxSubarray_prod:
                maxSubarray_prod=prefix_prod
    return maxSubarray_prod
                     

print(maxProduct([2,3,-2,4]))
print(maxProduct([-2,0,-1]))
print(maxProduct([-2,3,-4]))

# Status: independent solve 
# Time complexicity: O(n^2)
# Space complaxicity: O(1)
# LC status:NA
# mistakes/confusion: But keep optimization problem for next Revision or new Problem once again.
# Pattern:Prifix prod and running state

"""
### Isomorphic Strings (LC 205)
Pattern: Grouping Hash Maps (bijection mapping)
Difficulty: Easy
Constraints: 1 <= s.length <= 5×10^4, t.length == s.length, valid ASCII characters

Description: Two strings s and t are isomorphic if characters in s can be replaced one-to-one to get t. No two characters may map to the same character, but a character may map to itself. Return True if isomorphic.

Examples:
- s="egg", t="add" → True
- s="foo", t="bar" → False
- s="paper", t="title" → True

Key insight: Two dicts — s_to_t and t_to_s. At each position, check both directions are consistent: if s[i] already mapped, it must map to t[i]; if t[i] already mapped-to, it must come from s[i].


"""

def isIsomorphic(s,t):
    
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

print(isIsomorphic("egg","add"))
print(isIsomorphic("foo","bar"))
print(isIsomorphic("ab","aa"))
print(isIsomorphic("ab","xx"))
    
# Status: independent solve with hints for the two checks
# Time complexicity: O(n)
# Space complaxicity: O(1)
# LC status:NA
# mistakes/confusion: NA
# Pattern:Hashing Map with two passes



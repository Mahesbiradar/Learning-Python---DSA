"""
## Revision Problems (5 problems)

### First Unique Character in a String (LC 387)
Pattern: Frequency Hashing
Due: 3d recall
Constraint: 1 <= s.length <= 10^5; s contains only lowercase English letters.
Goal: Solve independently. If confident → submit to LC after.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""
#usning the Brute Force:Nested loop 

def firstUniqChar(s):

    for i in range(len(s)):
        count=0

        for j in  range(len(s)):

            if s[i]==s[j]:
                count+=1
        if count==1:
            return i
    return -1

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))

# Status: independent solve 
# Time complexicity: O(n^2)
# Space complaxicity: O(1)
# LC status:NA
# mistakes/confusion: 
# Pattern:Frequncy count /Nested loop

#optimal solution using the Frequency Hashing.

def firstUniqChar(s):

    seen={}

    for i in s:
        seen[i]=seen.get(i,0)+1
    
    for i in range(len(s)):

        if seen[s[i]]==1:
            return i

    return -1

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))

# Status: independent solve 
# Time complexicity: O(n)
# Space complaxicity: O(n)
# LC status:Accepted
# mistakes/confusion: NA
# Pattern:Frequncy Hashing


"""
### Best Time to Buy and Sell Stock (LC 121)
Pattern: Running-State Tracking
Due: 3d recall
Constraint: 1 <= prices.length <= 10^5; 0 <= prices[i] <= 10^4.
Goal: Solve independently. If confident → submit to LC after.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""
#Brute Force approch: i will use outer loop buy stock and inner loop to sell stock and see the profit.

def maxProfit(nums):

    max_profit=0

    for i in range(len(nums)):

        current_price=nums[i]

        for j in range(i+1,len(nums)):

            profit=nums[j]-current_price

            if profit>max_profit:
                max_profit=profit
    return max_profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))

# Status: independent solve 
# Time complexicity: O(n^2)
# Space complaxicity: O(1)
# LC status:NA
# mistakes/confusion: NA
# Pattern:Linear Traversal/Running state

#optimal solution: Tracking min Price

def maxProfit(nums):

    min_price=nums[0]
    max_profit=0

    for i in range(len(nums)):

        if nums[i]<min_price:
            min_price=nums[i]
        else:
            profit=nums[i]-min_price

            if profit>max_profit:
                max_profit=profit
    return max_profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))

# Status: independent solve 
# Time complexicity: O(n)
# Space complaxicity: O(1)
# LC status:Accepetd
# mistakes/confusion: NA
# Pattern:Linear Traversal/Running state tracking


"""
### Running Sum of 1d Array (LC 1480)
Pattern: Prefix Sum
Due: 3d recall
Constraint: 1 <= nums.length <= 1000; -10^6 <= nums[i] <= 10^6.
Goal: Solve independently. If confident → submit to LC after.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___


"""

def runningSum(nums):

    result=[]

    running_sum=0

    for num in nums:
        running_sum+=num
        result.append(running_sum)
    return result

print(runningSum([1,2,3,4]))
print(runningSum([1,1,1,1,1]))
print(runningSum([3,1,2,10,1]))

# Status: independent solve 
# Time complexicity: O(n)
# Space complaxicity: O(n)
# LC status:Accepetd
# mistakes/confusion: NA
# Pattern:Running state tracking

nums = [3,4,7,2,-3,1,4,2]


"""
### Subarray Sum Equals K (LC 560)
Pattern: Prefix Sum + Hash Map
Due: 3d recall
Constraint: 1 <= nums.length <= 2 * 10^4; -1000 <= nums[i] <= 1000; -10^7 <= k <= 10^7.
Goal: Solve independently. If confident → submit to LC after.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

#unding Brute Force:

def subarraySum(nums,k):

    count=0

    for i in range(len(nums)):

        prefix=0

        for j in range(i,len(nums)):

            prefix+=nums[j]

            if prefix==k:
                count+=1
    return count

print(subarraySum([1,1,1],2))
print(subarraySum([1,2,3],3))

# Status: independent solve
# Time complexicity: O(n^2)
# Space complaxicity: O(1)
# LC status:NA
# mistakes/confusion: NA
# Pattern:Prefix sum

#optimal solution: using prefix sum and Hashmap 

def subarraySum(nums,k):

    count=0
    seen={0:1}
    prefixSum=0

    for i in range(len(nums)):
        prefixSum+=nums[i]
        print("Current index:-",i,"prefixSum:-",prefixSum)
        needed=prefixSum-k
        print("needed:-",needed)
        count+=seen.get(needed,0)
        print("count:-",count)
        seen[prefixSum]=seen.get(prefixSum,0)+1
        print("seen:-",seen)
    
    return count
    
print(subarraySum([1,1,1],2))
print(subarraySum([1,2,3],3))

# Status: solved with hints and seen old solution now some portion is understood.But need revision
# Time complexicity: O(n)
# Space complaxicity: O(n)
# LC status:Accepted
# mistakes/confusion: NA
# Pattern:Prefix sum / frequency hashing.

"""
### Maximum Subarray (LC 53)
Pattern: Running-State Tracking
Due: 3d recall
Constraint: 1 <= nums.length <= 10^5; -10^4 <= nums[i] <= 10^4.
Goal: Solve independently. If confident → submit to LC after.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___


"""

#using brute Force

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
print(maxSubArray([1]))
print(maxSubArray([5,4,-1,7,8]))

# Status: Solved independently
# Time complexicity: O(n^2)
# Space complaxicity: O(1)
# LC status:NA
# mistakes/confusion: NA
# Pattern:Prefix sum /Running state.

#using kadane algo:

def maxSubArray(nums):

    max_sum=float('-inf')
    currentsum=0

    for i in range(len(nums)):
        currentsum=max(nums[i],currentsum+nums[i])

        if currentsum>max_sum:
            max_sum=currentsum
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1]))
print(maxSubArray([5,4,-1,7,8]))

# Status: Solved with hints and understood the concept need revision
# Time complexicity: O(n)
# Space complaxicity: O(1)
# LC status:Accepted
# mistakes/confusion: NA
# Pattern:Running-State Tracking


"""
152. Maximum Product Subarray
Medium
Topics
premium lock icon
Companies
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element

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

#Brute Force:

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


# Status: independent solve
# Time complexicity: O(n^2)
# Space complaxicity: O(1)
# LC status:Na  
# mistakes/confusion: NA
# Pattern:prefix prod/Running state Tracking



#optimal solution: using max and min

def maxProduct(nums):

    current_max=nums[0]
    current_min=nums[0]
    answer=nums[0]

    for i in range(1,len(nums)):

        n=nums[i]
        temp_max=current_max
        temp_min=current_min

        current_max=max(n,temp_max*n,temp_min*n)
        current_min=min(n,temp_max*n,temp_min*n)

        answer=max(answer,current_max)
    return answer
   
print(maxProduct([2,3,-2,4]))
print(maxProduct([-2,0,-1]))

# Status: sloved with hints and seen the solution
# Time complexicity: O(n)
# Space complaxicity: O(1)
# LC status:Accepted
# mistakes/confusion:
# PatternRunning state Tracking

"""
## Concept Warm-Up (5 min)
Write the Prefix Sum + Running-State Tracking templates from memory. No notes.

```python
# Prefix Sum + Hash Map


```

```python
# Kadane's / Running-State Tracking


"""

# Kadane's / Running-State Tracking

nums=[-2,1,-3,4,-1,2,1,-5,4]

max_sum=float('-inf')
current_max=0

for i in range(len(nums)):

    current_max=max(nums[i],current_max+nums[i])

    if current_max>max_sum:
        max_sum=current_max
print(max_sum)
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



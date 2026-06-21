## Session 1 — Prefix Sum + All Subarray Problems

"""
These are the highest priority because they contain the most concept-heavy logic.

### 1. Running Sum of 1D Array — LC 1480

**Pattern:** Prefix Sum
**Recall trigger:** `prefix[i] = prefix[i-1] + nums[i]`

Tests:

```python
[1,2,3,4]          # [1,3,6,10]
[3,1,2,10,1]       # [3,4,6,16,17]
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---  """
def runningsum(nums):
    
   output=[nums[0]]
   for i in range(1,len(nums)):
       output.append(nums[i]+output[i-1])
   

   return output

print(runningsum([1,2,3,4]))

#Status: independent.
#LC: Accepted.

"""
### 2. Find Pivot Index — LC 724

**Pattern:** Prefix Sum
**Recall trigger:** `right_sum = total - left_sum - current`

Tests:

```python
[1,7,3,6,5,6]      # 3
[1,2,3]             # -1
[2,1,-1]            # 0
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""

#Brute Force.
class Solution(object):
    def pivotIndex(self, nums):
        leftsum=0
        total_sum=sum(nums)

        for i in range(len(nums)):

            rightsum=total_sum-leftsum-nums[i]

            if leftsum==rightsum:
                return i
            leftsum+=nums[i]
        return -1
    
#Status: independent.

#LC:accepted.

"""
### 3. Find Highest Altitude — LC 1732

**Pattern:** Running Prefix Sum

Tests:

```python
[-5,1,5,0,-7]       # 1
[-4,-3,-2,-1,4,3,2] # 0
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt_gain=0
        high_alt=0

        for i in gain:
            alt_gain+=i

            if alt_gain>high_alt:
                high_alt=alt_gain
        return high_alt
    

#Status: independent.

#LC:accepted.

"""
### 4. Range Sum Query — Immutable — LC 303

**Pattern:** Prefix Sum
**Priority:** Concept not understood earlier.

Tests:

```python
nums = [-2,0,3,-5,2,-1]

sumRange(0,2)       # 1
sumRange(2,5)       # -1
sumRange(0,5)       # -3
```

[ ] Independent  [ ] Hint  [ ] Old code seen

"""













"""
### 5. Product of Array Except Self — LC 238

**Pattern:** Prefix Product + Suffix Product
**Recall trigger:** Left product does **not** include current item; right product does **not** include current item.

Tests:

```python
[1,2,3,4]           # [24,12,8,6]
[-1,1,0,-3,3]       # [0,0,9,0,0]
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""

def prodarrayexceptself(nums):

    left=[1]

    for i in range(1,len(nums)):

        left.append(nums[i-1]*left[i-1])
    
    right=[None]*len(nums)
    right[-1]=1

    for j in range(len(nums)-2,-1,-1):
        right[j]=(nums[j+1]*right[j+1])

    output=[]

    for k in range(len(nums)):

        output.append(left[k]*right[k])
    
    return output
    

print(prodarrayexceptself([1,2,3,4]))

#Status: independent.

#LC:accepted.


"""

### 6. Subarray Sum Equals K — LC 560

**Pattern:** Prefix Sum + Frequency Hash Map
**Priority:** Previously hint-needed and flagged shaky.

Mental trigger:

```text
needed_prefix = current_prefix - k
seen = {0: 1}
```

Tests:

```python
[1,1,1], 2          # 2
[1,2,3], 3          # 2
[1,-1,0], 0         # 3
```

[ ] Independent  [ ] Hint  [ ] Old code seen
"""

def subarraySum(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0

        for i in range(len(nums)):

            prefix=0
           

            for j in range(i,len(nums)):
             

                prefix+=nums[j]

                if prefix==k:
                    count+=1
        return count

print(subarraySum([1,2,1,2,1],3))

def subarraySum(nums, k):

    count=0
    prefix=0
    seen={0:1}

    for i in range(len(nums)):
        prefix+=nums[i]

        needed=prefix-k

        if needed in seen:
            count+=seen[needed]
        
        seen[prefix]=seen.get(prefix,0)+1
    
    return count


print(subarraySum([1,2,1,2,1],3))

#status: solved independednt but still feels not deppend Properly.

#LC: Accepted.

"""
### 7. Contiguous Array — LC 525

**Pattern:** Prefix Balance + Hash Map
**Priority:** Concept not understood earlier.

Mental trigger:

```text
0 -> -1
1 -> +1

same balance seen again
= equal number of 0 and 1 between indices
```

Tests:

```python
[0,1]                       # 2
[0,1,0]                     # 2
[0,1,1,0,1,1,1,0]           # 4
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""

def findMaxLength(nums):
    seen = {0: -1}
    balance = 0
    best = 0

    for i in range(len(nums)):
        
        if nums[i]==0:
            balance-=1
        else:
            balance+=1
        
        if balance in seen:
            best=max(best,i-seen[balance])
        else:
            seen[balance]=i


    return best


#status: Seen old solution need deep understanding on this.

#LC: Accepted.


"""
### 8. Maximum Subarray — LC 53

**Pattern:** Running-State Tracking / Kadane’s Algorithm
**Subarray problem — mandatory.**

Tests:

```python
[-2,1,-3,4,-1,2,1,-5,4]     # 6
[1]                          # 1
[5,4,-1,7,8]                # 23
```

[ ] Independent  [ ] Hint  [ ] Old code seen

"""

def maxsubarray(nums):

    max_array=nums[0]
    prefix=nums[0]

    for i in range(len(nums)):

        prefix=max(nums[i],prefix+nums[i])

        max_array=max(max_array,prefix)
    
    return max_array

print(maxsubarray([-2,1,-3,4,-1,2,1,-5,4] ))
print(maxsubarray([5,4,-1,7,8]   ))

#Status: Independent after guided concept learning

#LC: Accepted.

"""
### 9. Maximum Product Subarray — LC 152

**Pattern:** Running-State Tracking
**Subarray problem — mandatory.**

Mental trigger:

```text
Negative number can swap maximum and minimum.
Track both current_max and current_min.
```

Tests:

```python
[2,3,-2,4]                  # 6
[-2,0,-1]                   # 0
[-2,3,-4]                   # 24
```

[ ] Independent  [ ] Hint  [ ] Old code seen

"""

def maxprodsubarray(nums):

    max_subarray=nums[0]
    min_subarray=nums[0]
    
    max_prod=nums[0]
    

    for i in range(1,len(nums)):
        n=nums[i]

        temp_min=min_subarray
        temp_max=max_subarray

        max_subarray=max(n,temp_max*n,temp_min*n)
        min_subarray=min(n,temp_max*n,temp_min*n)

        max_prod=max(max_prod,max_subarray)

    return max_prod


print(maxprodsubarray([2,3,-2,4] ))

#status: Independent after guided concept learning

#LC=Accepted.

"""
### 10. Maximum Average Subarray I — LC 643

**Pattern:** Fixed-Size Sliding Window
**Subarray problem — mandatory.**

Tests:

```python
[1,12,-5,-6,50,3], 4        # 12.75
[5], 1                       # 5.0
```

[ ] Independent  [ ] Hint  [ ] Old code seen

"""

def maxaverage(nums,k):

    left=0
    best=0
    prefix=0

    for right in range(len(nums)):

        prefix+=nums[right]

        while right-left+1>k:

            prefix-=nums[left]
            left+=1
            
        if right-left+1==k:
            best=max(best,prefix)
    
    return best/float(k)

print(maxaverage([1,12,-5,-6,50,3], 4 ))
print(maxaverage([5], 1 ))

#status: independent.

#LC=Accepted.
        


"""
 ### 4. Range Sum Query — Immutable — LC 303

**Pattern:** Prefix Sum
**Priority:** Concept not understood earlier.

Tests:

```python
nums = [-2,0,3,-5,2,-1]

sumRange(0,2)       # 1
sumRange(2,5)       # -1
sumRange(0,5)       # -3
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---
 
 
"""       

class NumArray(object):

    def __init__(self, nums):
        self.prefix=[0]

        for i in nums:
            self.prefix.append(self.prefix[-1]+i)
       

    def sumRange(self, left, right):
        return self.prefix[right+1]-self.prefix[left]


obj = NumArray([-2, 0, 3, -5, 2, -1])

print(obj.sumRange(0, 2))  # 1
print(obj.sumRange(2, 5))  # -1
print(obj.sumRange(0, 5))  # -3

#status:solved with hints.

#LC:NA

    
"""
### 7. Contiguous Array — LC 525

**Pattern:** Prefix Balance + Hash Map
**Priority:** Concept not understood earlier.

Mental trigger:

```text
0 -> -1
1 -> +1

same balance seen again
= equal number of 0 and 1 between indices
```

Tests:

```python
[0,1]                       # 2
[0,1,0]                     # 2
[0,1,1,0,1,1,1,0]           # 4
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

"""

def findMaxLength(nums):

    balance=0
    best=0
    seen={0:-1}

    for i in range(len(nums)):

        if nums[i]==1:
            balance+=1
        else:
            balance-=1
        
        if balance in seen:
            best=max(best,i-seen[balance])
        else:
            seen[balance]=i
    return best


print(findMaxLength([0, 1]))                    # 2
print(findMaxLength([0, 1, 0]))                 # 2
print(findMaxLength([0, 1, 1, 0]))              # 4

#status: solved after guided concept learning
#Pattern: Prefix Balance + Hash Map


def maxSubArray(nums):

    currentsum=nums[0]
    best=nums[0]

    for i in range(1,len(nums)):

        currentsum=max(nums[i],currentsum+nums[i])

        best=max(best,currentsum)

    return best

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
print(maxSubArray([1]))                       # 1
print(maxSubArray([-3,-2,-5]))                # -2



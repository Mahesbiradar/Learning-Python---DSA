## TIER 4 Recalls (5 min each, no full solve)

# Write the template from memory. If you can't in 3 min → flag as Tier 2. (Both skipped Jul 6 — repeating today.)

# 1. Frequency Hashing

def freqhashing(nums):

    seen = {}

    for i in nums:
        seen[i]=seen.get(i,0)+1
    
    for key, value in seen.items():
        
        if value == 1:
            return key
    return -1

# 2. Sliding Window (Fixed size)

def silidingwindow(nums,k):

    left = 0

    best = 0

    countofovels = 0

    for right in range(len(nums)):

        if nums[right] in 'aeiou':
            countofovels += 1
        
        while right-left+1 > k:

            if nums[left] in 'aeiou':
                countofovels -= 1
            left += 1
        
        if right-left+1 == k:
            best = max(best,countofovels)
    return countofovels

# Pattern 1 recalled correctly (Y/N): Yes
# Pattern 2 recalled correctly (Y/N): Yes

## TIER 1 — Priority Revision (solve all 3, no hints — this is a 2nd attempt on all three same-day)

"""
### 1. Search in Rotated Sorted Array — Medium
There is an integer array `nums` sorted in ascending order (distinct values), rotated at an unknown pivot. Given the rotated array and an integer `target`, return the index of `target` if found, or `-1`. Must run in O(log n).

Example 1: `nums = [4,5,6,7,0,1,2], target = 0` → Output: `4`
Example 2: `nums = [4,5,6,7,0,1,2], target = 3` → Output: `-1`
Example 3: `nums = [1], target = 0` → Output: `-1`

Constraints: `1 <= nums.length <= 5000`, `-10^4 <= nums[i] <= 10^4`, all values unique, array is rotated at some pivot, `-10^4 <= target <= 10^4`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        while left <= right :

            mid = (right+left)//2

            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:

                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid]<= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1 

# Status: independent
# Time taken: 25 min
# Tier:
# Time complexity: O(logn) With each iteration search space becomes half
# Space complexity: O(1)
# LC status:Accepted
# Pattern:Binary search
# Variant: Fixed search
# mistakes/confusion:Na

"""
### 2. Find Minimum in Rotated Sorted Array — Medium
Suppose an array of length `n` sorted in ascending order is rotated between 1 and `n` times. Given the rotated sorted array `nums` of unique elements, return the minimum element. Must run in O(log n).

Example 1: `nums = [3,4,5,1,2]` → Output: `1`
Example 2: `nums = [4,5,6,7,0,1,2]` → Output: `0`
Example 3: `nums = [11,13,15,17]` → Output: `11`

Constraints: `n == nums.length`, `1 <= n <= 5000`, `-5000 <= nums[i] <= 5000`, all unique, rotated between 1 and n times.

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:

"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        while left < right:

            mid = (right+left)//2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
    
# Status: Independent
# Time taken: 20 min
# Tier:
# Time complexity: O(logn) search space reduces to half with each iteration
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Binary search
# Variant: Boundry search
# mistakes/confusion: Na

"""
### 3. Koko Eating Bananas — Medium
There are `n` piles of bananas, `piles[i]` bananas in the `i`th pile. Koko eats at a speed of `k` bananas per hour: each hour she picks one pile and eats `k` bananas from it (or all of it if fewer than `k` remain), and does not eat from another pile that hour. Koko wants to finish all bananas within `h` hours. Return the minimum integer `k` such that she can finish within `h` hours.

Example 1: `piles = [3,6,7,11], h = 8` → Output: `4`
Example 2: `piles = [30,11,23,4,20], h = 5` → Output: `30`
Example 3: `piles = [30,11,23,4,20], h = 6` → Output: `23`

Constraints: `1 <= piles.length <= 10^4`, `piles.length <= h <= 10^9`, `1 <= piles[i] <= 10^9`

"""

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def feasible(speed):

            totalshours = 0

            for i in piles:

                qouationt = i // speed
                remainder = 0
                if i % speed ==0:
                    remainder = 0
                else:
                    remainder = 1
                totalshours += qouationt + remainder
            return totalshours <= h
        
        lo = 1
        hi = max(piles)

        while lo < hi:

            mid = (hi+lo)//2

            work = feasible(mid)

            if work:
                hi = mid
            else :
                lo = mid + 1
        return lo
    
# Status:independent
# Time taken: 30 min
# Tier:
# Time complexity: O(n(log(max(piles))))
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Binary search
# Variant:Boundry search
# mistakes/confusion:Na

"""
## TIER 2 — Revision (2 problems — only 2 due, both taken)

### 1. Total Appeal of A String — Hard
The appeal of a string is the number of distinct characters found in the string. Given a string `s`, return the total appeal of all of its substrings.
Note: last 2 attempts were brute force O(n²) only — this attempt, try to derive the O(n) contribution-per-character approach before coding.

Example 1: `s = "abbca"` → Output: `28`
Example 2: `s = "code"` → Output: `20`

Constraints: `1 <= s.length <= 10^5`, lowercase English letters.

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```
"""
class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0

        for i in range(len(s)):

            seen = set()

            for j in range(i,len(s)):

                seen.add(s[j])

                count += len(seen)
        return count


# Status: Hint 
# Time taken: 20 min
# Tier:
# Time complexity: O(n^2)
# Space complexity: O(n)
# LC status: na
# Pattern: NA
# Variant:na
# mistakes/confusion: Since i have not solved optimized solution i have to work on this.

"""
### 2. Make Sum Divisible by P — Hard
Given an array of positive integers `nums`, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by `p`. It is not allowed to remove the whole array. Return the length of the smallest subarray you need to remove, or `-1` if it's impossible.
Note: this is the USO close-out attempt — solve cold, no notes, to confirm the standalone session from Jul 5 stuck.

Example 1: `nums = [3,1,4,2], p = 6` → Output: `1`
Example 2: `nums = [6,3,5,2], p = 9` → Output: `2`
Example 3: `nums = [1,2,3], p = 3` → Output: `0`

Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^9`, `1 <= p <= 10^9`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
"""
class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        totalsum = sum(nums)

        target = totalsum % p

        if target == 0:
            return 0
        
        best = len(nums)

        seen = {0:-1}
        
        prefix = 0

        for i in range(len(nums)):

            prefix += nums[i]

            current = prefix % p

            needed = (current-target+p) % p

            if needed in seen:
                best = min (best,i-seen[needed])
            
            seen[current]=i
        if best == len(nums):
            return -1
        else :
            return best
        
# Status: independent 
# Time taken: 25 min
# Tier:
# Time complexity: O(n)
# Space complexity: O(n)
# LC status:Accepted
# Pattern:Prefix sum 
# Variant:modulo 
# mistakes/confusion:Na

"""
## TIER 3 — Revision (2 problems, both overdue since Jul 5 — priority pick)

### 1. Subarray Sum Equals K — Medium
Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals `k`.

Example 1: `nums = [1,1,1], k = 2` → Output: `2`
Example 2: `nums = [1,2,3], k = 3` → Output: `2`

Constraints: `1 <= nums.length <= 2*10^4`, `-1000 <= nums[i] <= 1000`, `-10^7 <= k <= 10^7`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```
"""

def subarrayequalk(nums,k):

    prefix = 0

    count = 0

    seen = {0:1}


    for i in range(len(nums)):

        prefix += nums[i]

        needed = prefix - k 

        if needed in seen:
            count += seen[needed]
        
        seen[prefix] = seen.get(prefix,0)+1
    return count

print(subarrayequalk([1,1,1], k = 2))
print(subarrayequalk([1,2,3], k = 3))

# Status: independent
# Time taken: 20 min
# Tier:
# Time complexity: O(n)
# Space complexity: O(n)
# LC status: Accepted
# Pattern: Prefix sum + Hashing
# Variant:
# mistakes/confusion:Na

"""
### 2. Binary Subarrays With Sum — Medium
Given a binary array `nums` and an integer `goal`, return the number of non-empty subarrays with a sum equal to `goal`.

Example 1: `nums = [1,0,1,0,1], goal = 2` → Output: `4`
Example 2: `nums = [0,0,0,0,0], goal = 0` → Output: `15`

Constraints: `1 <= nums.length <= 3*10^4`, `nums[i]` is `0` or `1`, `0 <= goal <= nums.length`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:

"""

class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """

        seen = {0:1}

        prefix = 0

        count = 0


        for i in range(len(nums)):

            prefix += nums[i]

            needed = prefix - goal

            if needed in seen:
                count += seen[needed]
            
            seen[prefix] = seen.get(prefix,0)+1

        return count 


# Status: Independent
# Time taken: 20 min
# Tier:
# Time complexity: O(n)
# Space complexity: O(n)
# LC status: Accepted
# Pattern: Prifix sum + Hash map
# Variant:
# mistakes/confusion:   nA


## New Problems (3 problems) — identify the pattern yourself, do not skip Step 3 of the SOP
"""
### 1. Reverse a Singly Linked List — Easy
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1: `head = [1,2,3,4,5]` → Output: `[5,4,3,2,1]`
Example 2: `head = [1,2]` → Output: `[2,1]`
Example 3: `head = []` → Output: `[]`

Constraints: number of nodes is `0` to `5000`, `-5000 <= Node.val <= 5000`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        current = head

        while current is not None:

            next_node = current.next

            current.next = prev

            prev = current

            current = next_node

        return prev

# Status: Hint
# Time taken: 30 min
# Tier:
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Linked list
# Variant:
# mistakes/confusion:Na

"""
### 2. Reverse a Linked List Between Two Positions — Medium
Given the head of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right` (1-indexed), and return the reversed list.

Example 1: `head = [1,2,3,4,5], left = 2, right = 4` → Output: `[1,4,3,2,5]`
Example 2: `head = [5], left = 1, right = 1` → Output: `[5]`

Constraints: number of nodes `n`, `1 <= n <= 500`, `-500 <= Node.val <= 500`, `1 <= left <= right <= n`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)

        current = head

        prev = dummy

        dummy.next = head

        position = 1

        #Phase-1 traverse to left postion.
        while position < left :

            prev = current

            current = current.next

            position +=1
        
        #Phase-2 reverse the list
        
        before_left = prev
        left_node = current
        prev = None

        count = right - left + 1

        while count > 0:

            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            count -= 1
        
         #Phase-3 reconnect
        
        before_left.next = prev
        left_node.next = current

        return dummy.next


# Status: hint
# Time taken: 40 min
# Tier:
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: linked list reversal b/w two postions
# Variant:
# mistakes/confusion: Na











## Tier 4 Recalls (5 min each)

# 1. Grouping Hash Maps

def grouphashmap(strng):

    seen ={}

    for i in strng:

        sorted_i = sorted(i)
        key = "".join(sorted_i)

        if key in seen:
            seen[key] += [i]
        else:
            seen[key] = [i]
    return seen.values()

# 2. Frequency Sorting

def frequncysorting(nums,k):

    seen ={}

    for i in nums:
        seen[i] = seen.get(i,0)+1
    
    sorted_seen = sorted(seen.items(), key=lambda x:x[1], reverse=True)

    out = []

    for key,value in sorted_seen:

        out.append(key)

        if len(out) == k:
            return out

## Tier 1 — Priority Revision

"""

### Merge k Sorted Lists (LC 23)

You have an array of `k` linked-lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

**Example 1:**
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

**Example 2:**
Input: lists = []
Output: []

**Example 3:**
Input: lists = [[]]
Output: []

**Constraints:**
- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- `lists[i]` is sorted in ascending order.
- The sum of all `lists[i].length` will not exceed `10^4`

"""

    # Definition for singly-linked list.
class ListNode(object):
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
class Solution(object):
        def mergeKLists(self, lists):
            """
            :type lists: List[Optional[ListNode]]
            :rtype: Optional[ListNode]
            """
            if not lists:
                return None 
            

            def mergetwolist(list1,list2):

                dummy = ListNode(0)
                
                current = dummy

                while list1 and list2:

                    if list1.val <= list2.val:
                        current.next = list1
                        list1 = list1.next
                    else:
                        current.next = list2
                        list2 = list2.next

                    current = current.next
                
                current.next = list1 if list1 else list2

                return dummy.next
            
            while len(lists)>1:

                mergedlist = []

                for i in range(0,len(lists),2):

                    first = lists[i]

                    if i+1 < len(lists):
                        second = lists[i+1]
                    else:
                        second = None
                    
                    merged = mergetwolist(first,second)

                    mergedlist.append(merged)
                
                lists = mergedlist
            
            return lists[0]

# Status: Hint
# Time taken: 25 min
# Time complexity: O(n*logm)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Linked List — Dummy Node / Merge k Sorted
# Variant: Merge k sorted lists (min-heap or divide-and-conquer)
# mistakes/confusion: Na

## Tier 2 — Revision

"""
### Search in Rotated Sorted Array (LC 33) — Standalone Confirmation

There is an integer array `nums` sorted in ascending order (with distinct values).

Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

**Example 2:**
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

**Example 3:**
Input: nums = [1], target = 0
Output: -1

**Constraints:**
- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are unique.
- `nums` is guaranteed to be rotated at some pivot.
- `-10^4 <= target <= 10^4`

"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right =len(nums)-1

        while left <= right:

            mid = (right+left)//2

            if nums[mid]== target:
                return mid
            elif nums[left] <= nums[mid]:

                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:

                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
    

# Status: independent
# Time taken: 15 min
# Time complexity: O(logn)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Binary Search — Applied (rotated array)
# Variant: Exact search in rotated sorted array
# mistakes/confusion: Na


## Tier 3 — Revision

"""

### Find Minimum in Rotated Sorted Array (LC 153) — Standalone Confirmation

Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated `4` times.
- `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.

You must write an algorithm that runs in `O(log n)` time.

**Example 1:**
Input: nums = [3,4,5,1,2]
Output: 1

**Example 2:**
Input: nums = [4,5,6,7,0,1,2]
Output: 0

**Example 3:**
Input: nums = [11,13,15,17]
Output: 11

**Constraints:**
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are unique.
- `nums` is sorted and rotated between `1` and `n` times.


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

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
    
# Status: independent
# Time taken: 20 min
# Time complexity: O(logn)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Binary Search — Applied (boundary search in rotated array)
# Variant: Find minimum in rotated sorted array
# mistakes/confusion: Na

"""
### Koko Eating Bananas (LC 875) — Standalone Confirmation

Koko loves to eat bananas. There are `n` piles of bananas, the `i`-th pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses a pile and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

**Example 1:**
Input: piles = [3,6,7,11], h = 8
Output: 4

**Example 2:**
Input: piles = [30,11,23,4,20], h = 5
Output: 30

**Example 3:**
Input: piles = [30,11,23,4,20], h = 6
Output: 23

**Constraints:**
- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

"""

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        def feasible(speed):

            count = 0

            for i in piles:
                diviser = i // speed
                remainder = 1 if i % speed != 0 else 0
                count += diviser + remainder
            
            return False if count > h else True
        
        
        left = 1

        right = max(piles)

        while left < right:

            mid = (right+left)//2

            isfeasible = feasible(mid)

            if isfeasible:
                right = mid
            else:
                left = mid + 1
                
        return left 

# Status: independent
# Time taken: 15 min
# Time complexity: O(n*logm)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted 
# Pattern: Binary Search — Applied (feasibility / monotonic predicate on answer space)
# Variant: Search on answer — minimum feasible speed
# mistakes/confusion: Na

"""
### Subarray Sum Equals K (LC 560) — OVERDUE

Given an array of integers `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals `k`.

**Example 1:**
Input: nums = [1,1,1], k = 2
Output: 2

**Example 2:**
Input: nums = [1,2,3], k = 3
Output: 2

**Constraints:**
- `1 <= nums.length <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`

"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen ={0:1}

        prefix = 0

        count = 0

        for i in range(len(nums)):

            prefix += nums[i]

            needed = prefix - k

            if needed in seen:
                count += seen[needed]
            
            seen[prefix] =seen.get(prefix,0)+1
        return count 


# Status: independent
# Time taken: 15 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Prefix Sum + Hash Map
# Variant: Count subarrays with sum equal to k
# mistakes/confusion: Na

"""
### Binary Subarrays With Sum (LC 930) — OVERDUE

Given a binary array `nums` and an integer `goal`, return the number of non-empty subarrays with a sum `goal`.

A subarray is a contiguous part of the array.

**Example 1:**
Input: nums = [1,0,1,0,1], goal = 2
Output: 4

**Example 2:**
Input: nums = [0,0,0,0,0], goal = 0
Output: 15

**Constraints:**
- `1 <= nums.length <= 3 * 10^4`
- `nums[i]` is either `0` or `1`.
- `0 <= goal <= nums.length`

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
    
# Status: independent
# Time taken: 10 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Prefix Sum + Hash Map
# Variant: Count subarrays with sum equal to goal (binary array)
# mistakes/confusion: 

"""
### Length of Last Word (LC 58) — OVERDUE

Given a string `s` consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

**Example 1:**
Input: s = "Hello World"
Output: 5

**Example 2:**
Input: s = "   fly me   to   the moon  "
Output: 4

**Example 3:**
Input: s = "luffy is still joyboy"
Output: 6

**Constraints:**
- `1 <= s.length <= 10^4`
- `s` consists of only English letters and spaces `' '`.
- There will be at least one word in `s`.

"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lenght = 0
        count = 0

        for i in range(len(s)):

            if s[i] != " ":
                count +=1
            else:
                count = 0
            
            if count != 0:
                lenght = count 
        return lenght 

# Status: independent
# Time taken: 10 min
# Time complexity: O(n)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: String Traversal
# Variant: Find length of last word
# mistakes/confusion: Na

"""
### First Bad Version (LC 278) — OVERDUE

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

**Example 1:**
Input: n = 5, bad = 4
Output: 4

**Example 2:**
Input: n = 1, bad = 1
Output: 1

**Constraints:**
- `1 <= bad <= n <= 2^31 - 1`

```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n 

        while left < right:

            mid = (right + left)//2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left 


# Status: independent
# Time taken: 10 min
# Time complexity: O(logn)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Binary Search — Standard
# Variant: Lower bound / first true in monotonic boolean array
# mistakes/confusion: Na










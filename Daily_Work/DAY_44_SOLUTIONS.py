## Tier 4 Recalls (5 min each)

# 1. Running State / Kadane — max subarray tracking

def runningstate(nums):


    currentsub = 0

    max_subarray = float('-inf')

    for i in range(len(nums)):

        currentsub = max(nums[i],currentsub+nums[i])

        max_subarray = max(max_subarray,currentsub)

    return max_subarray


# 2. Running State / Kadane — min-max product tracking

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_profit = 0

        for i in range(1,len(prices)):

            if prices[i] < min_price:
                min_price = prices[i]
            else:
                profit = prices[i] - min_price

                if profit > max_profit:
                    max_profit = profit
        return max_profit

## Tier 1 — Priority Revision

### 1. Merge k Sorted Lists (LC 23)

"""
### 1. Merge k Sorted Lists (LC 23)

You are given an array of `k` linked-lists, each sorted in ascending order.

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
- The sum of `lists[i].length` will not exceed `10^4`.

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

        def mergetwolists(list1,list2):

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



        while len(lists) > 1:

                mergedlist = []

                for i in range(0,len(lists),2):

                    first = lists[i]

                    if i+1 < len(lists):
                        second = lists[i+1]
                    else:
                        second = None
                    
                    merge = mergetwolists(first,second)

                    mergedlist.append(merge)
                
                lists = mergedlist
            
        return lists[0]


# Status: independent
# Time taken: 20 min
# Time complexity: O(n * log k)
# Space complexity: O(k)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Linked List
# Variant: Dummy node — merge k sorted lists
# mistakes/confusion: Na


## Tier 3 — Revision (7 Problems)


"""
### 2. Find Minimum in Rotated Sorted Array (LC 153)

Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated `4` times.
- `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return the minimum element of this array.

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
- All the integers of `nums` are **unique**.
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

            if nums[mid]>nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
    
# Status: independent
# Time taken: 15 min
# Time complexity: O(logn)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Binary Search
# Variant: Applied — boundary search in rotated array
# mistakes/confusion: Na


"""
### 3. Find Peak Element (LC 162)

A peak element is an element that is strictly greater than its neighbors.

Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in `O(log n)` time.

**Example 1:**
Input: nums = [1,2,3,1]
Output: 2

**Example 2:**
Input: nums = [1,2,1,3,5,6,4]
Output: 5

**Constraints:**
- `1 <= nums.length <= 1000`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `nums[i] != nums[i + 1]` for all 

"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (right+left)//2

            if nums[mid]>nums[mid+1]:
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
# Pattern: Binary Search
# Variant: Lower bound — first peak position
# mistakes/confusion: Na


"""
### 4. Range Sum Query - Immutable (LC 303)

Given an integer array `nums`, handle multiple queries of the following type:

1. Calculate the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** where `left <= right`.

Implement the `NumArray` class:

- `NumArray(int[] nums)` Initializes the object with the integer array `nums`.
- `int sumRange(int left, int right)` Returns the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** (i.e. `nums[left] + nums[left + 1] + ... + nums[right]`).

**Example 1:**
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

**Constraints:**
- `1 <= nums.length <= 10^4`
- `-10^5 <= nums[i] <= 10^5`
- `0 <= left <= right < nums.length`
- At most `10^4` calls will be made to `sumRange`.

"""

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        prefix = [0]

        for i in range(len(nums)):
            prefix.append(prefix[i]+nums[i])
        
        self.prefix = prefix
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix[right+1]-self.prefix[left]

# Status: independent
# Time taken: 15 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Prefix Sum
# Variant: Prefix array
# mistakes/confusion: Na

"""
### 5. Two Sum (LC 1)

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have **exactly one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

**Example 1:**
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

**Example 2:**
Input: nums = [3,2,4], target = 6
Output: [1,2]

**Example 3:**
Input: nums = [3,3], target = 6
Output: [0,1]

**Constraints:**
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- **Only one valid answer exists.**

"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen ={}

        for i in range(len(nums)):

            needed = target - nums[i]

            if needed in seen:
                return [seen[needed],i]
            
            seen[nums[i]] = i
        
# Status: independent
# Time taken: 10 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted 
# Pattern: Complement Lookup
# Variant: Two Sum style
# mistakes/confusion: Na

"""
### 6. Valid Perfect Square (LC 367)

Given a positive integer `num`, return `true` *if* `num` *is a perfect square or* `false` *otherwise*.

A **perfect square** is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as `sqrt`.

**Example 1:**
Input: num = 16
Output: true

**Example 2:**
Input: num = 14
Output: false

**Constraints:**
- `1 <= num <= 2^31 - 1`

"""
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 0
        right = num

        while left <= right:

            mid = (right+left)//2

            n = mid*mid

            if n == num:
                return True
            elif n > num:
                right = mid -1
            else:
                left = mid + 1
        return False

# Status: Independent
# Time taken: 10 min
# Time complexity: O(logn)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted 
# Pattern: Binary Search
# Variant: Lower bound — exact square check
# mistakes/confusion: Na

"""
### 7. Ransom Note (LC 383)

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

**Example 1:**
Input: ransomNote = "a", magazine = "b"
Output: false

**Example 2:**
Input: ransomNote = "aa", magazine = "ab"
Output: false

**Example 3:**
Input: ransomNote = "aa", magazine = "aab"
Output: true

**Constraints:**
- `1 <= ransomNote.length, magazine.length <= 10^5`
- `ransomNote` and `magazine` consist of lowercase English letters.

# Status: ___
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Frequency Hashing
# Variant: Count + query
# mistakes/confusion: ___

"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
       
        seenr = {}

        for i in ransomNote:
            seenr[i] = seenr.get(i,0)+1
        seenm = {}
        for j in magazine:
            seenm[j] = seenm.get(j,0)+1
        
        for k in ransomNote:
            
            if k not in seenm or seenm[k]<seenr[k]:
                return False

        return True

# Status: independent
# Time taken: 20 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Frequency Hashing
# Variant: Count + query
# mistakes/confusion:Na

"""
### 8. Koko Eating Bananas (LC 875)

Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return *the minimum integer* `k` *such that she can eat all the bananas within* `h` *hours*.

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
        def isfeasible(speed):

            count = 0

            for i in piles:
                divisor = i // speed
                remainder = 0 if i % speed == 0 else 1

                count += divisor + remainder
            
            return False if count > h else True
        
        left = 1
        right = max(piles)

        while left < right:

            mid = (right+left)//2

            if isfeasible(mid):
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
# Pattern: Binary Search
# Variant: Applied — boundary / feasibility on answer space
# mistakes/confusion: Na




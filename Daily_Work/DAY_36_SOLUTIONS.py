## TIER 4 Recalls (5 min each, no full solve)

"""
Write the pattern template from memory. If you can't in 3 min → flag as Tier 2.

"""
# 1. Prefix Sum

def prefix_sum(nums):

    totalsum = sum(nums)

    left = 0


    for i in range(len(nums)):

        right = totalsum-nums[left]-nums[i]

        if right == left:
            return i
        left += nums[i]
    return -1

#2. Two Pointers

def two_pointers(nums,target):

    left = 0
    right = len(nums)-1

    while left < right:

        num = nums[left] + nums[right]

        if num == target:
            return [left,right]

# Pattern 1 recalled correctly (Y/N): Yes But evaluate the template
# Pattern 2 recalled correctly (Y/N): Yes But evaluate the template

## TIER 1 — Priority Revision (solve these first, all of them)

"""
### 1. Total Appeal of A String — Hard
The appeal of a string is the number of distinct characters inside that string. Given a lowercase string `s`, return the sum of the appeal values of every non-empty substring of `s`.

Before coding, do a standalone derivation:
- For each index `i`, decide how many substrings use `s[i]` as the newest contribution for that character.
- Track the previous position of each character.
- Write why the contribution is based on the gap since the previous occurrence and the number of possible right endpoints.
- Only then code the O(n) version.

Example 1: `s = "abbca"` → Output: `28`
Example 2: `s = "code"` → Output: `20`

Constraints: `1 <= s.length <= 10^5`, `s` contains only lowercase English letters.

```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

"""

#Brute Force:

def totalappead(s):

    count = 0

    for i in range(len(s)):

        seen = set()

        for j in range(i,len(s)):

            seen.add(s[j])

            count += len(seen)
    return count

print(totalappead("abbca"))
print(totalappead("code"))

# Status: Independent
# Time taken: 15 min
# Tier: ___
# Time complexity: O(n^2) double pass over string
# Space complexity: O(n) set is used to keep all unique elemetes in substring. 
# LC status: Not submitted
# Pattern: Nested loop 
# Variant: ___
# mistakes/confusion: Na

# Note: Keep this optimal solution on hold untill my all core patterns doesnt finish like: Linked Lists,Trees,Graphs,Dynamic Programming

"""
### 2. Reverse Linked List II LC-92 — Medium
Given the head of a singly linked list and two integers `left` and `right`, reverse the nodes from position `left` to position `right` using 1-indexing. Return the head of the modified list.

Example 1: `head = [1,2,3,4,5], left = 2, right = 4` → Output: `[1,4,3,2,5]`
Example 2: `head = [5], left = 1, right = 1` → Output: `[5]`

Constraints: number of nodes `n`, `1 <= n <= 500`, `-500 <= Node.val <= 500`, `1 <= left <= right <= n`.

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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

        while position < left:

            prev = current

            current = current.next

            position +=1
        
        before_node = prev
        left_node = current
        prev = None

        num = right - left+1

        while num > 0:

            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            num -=1
        
        before_node.next = prev
        left_node.next = current

        return dummy.next


# Status: Independent
# Time taken: 30 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted 
# Pattern: Revarsal between two points
# Variant: ___
# mistakes/confusion: Na

"""
### 3. Merge Two Sorted Lists — Easy
You are given the heads of two sorted linked lists, `list1` and `list2`. Merge their nodes into one sorted linked list and return the head of the merged list.

Example 1: `list1 = [1,2,4], list2 = [1,3,4]` → Output: `[1,1,2,3,4,4]`
Example 2: `list1 = [], list2 = []` → Output: `[]`
Example 3: `list1 = [], list2 = [0]` → Output: `[0]`

Constraints: both lists contain `0` to `50` nodes, `-100 <= Node.val <= 100`, and both input lists are sorted in non-decreasing order.

```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
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

# Status: Independent
# Time taken: 20 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Merge two sorted list
# Variant: ___
# mistakes/confusion: Na

"""
### 4. Remove Nth Node From End of List — Medium
Given the head of a linked list and an integer `n`, remove the `n`th node from the end of the list and return the updated head.

Example 1: `head = [1,2,3,4,5], n = 2` → Output: `[1,2,3,5]`
Example 2: `head = [1], n = 1` → Output: `[]`
Example 3: `head = [1,2], n = 1` → Output: `[1]`

Constraints: list size `sz`, `1 <= sz <= 30`, `0 <= Node.val <= 100`, `1 <= n <= sz`.

```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___
```

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)

        fast = dummy
        slow = dummy

        dummy.next = head

        while n+1 > 0:

            fast = fast.next
            n -= 1
        
        while fast:

            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next

# Status: Hint
# Time taken: 25 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted 
# Pattern: Fast and slow pointers 
# Variant: 
# mistakes/confusion: Na

"""
### 5. Maximum Twin Sum of a Linked List — Medium
In a linked list with even length `n`, node `i` is paired with node `n - 1 - i`. The twin sum is the sum of the values in a paired set of nodes. Return the maximum twin sum in the linked list.

Example 1: `head = [5,4,2,1]` → Output: `6`
Example 2: `head =  ` → Output: `7`
Example 3: `head = [1,100000]` → Output: `100001`

Constraints: number of nodes `n`, `2 <= n <= 10^5`, `n` is even, `1 <= Node.val <= 10^5`.

```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow = head
        fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        current = slow
        prev = None

        while current :
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        right = prev
        left = head 

        twin_sum = 0

        while right:
            sum_of_two_nodes = right.val + left.val

            right = right.next
            left = left .next
            twin_sum = max(twin_sum,sum_of_two_nodes)
        
        return twin_sum
    

# Status:Hint
# Time taken: 25 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted 
# Pattern: Fast and slow + Reversal + Traversal
# Variant: ___
# mistakes/confusion: one mistake i made in th first loop i kept just only While Fast:

## TIER 2 — Revision (1 problem due)

"""
### 1. Koko Eating Bananas — Medium
You are given `piles`, where `piles[i]` is the number of bananas in the `i`th pile, and an integer `h`. Koko chooses an integer speed `k`. Each hour, she chooses one pile and eats up to `k` bananas from it. Return the minimum `k` that allows her to finish all piles within `h` hours.

Example 1: `piles = [3,6,7,11], h = 8` → Output: `4`
Example 2: `piles = [30,11,23,4,20], h = 5` → Output: `30`
Example 3: `piles = [30,11,23,4,20], h = 6` → Output: `23`

Constraints: `1 <= piles.length <= 10^4`, `piles.length <= h <= 10^9`, `1 <= piles[i] <= 10^9`.

```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___
```
"""

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def fesible(hrs):

            counthrs = 0

            for i in piles:

                if i <= hrs:
                    counthrs +=1
                else:
                    division = i // hrs
                    remainder = i % hrs

                    counthrs += division +1 if remainder !=0 else division
            if counthrs > h:
                return False
            else:
                return True
        
        left = 1

        right = max(piles )

        while left < right:

            mid = (right+left)//2

            isfeasible = fesible(mid)

            if isfeasible:
                right = mid
            else:
                left = mid +1
        return left

# Status: Independent
# Tier: ___
# Time complexity: O(nlogm)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Binary search
# Variant: Boundry search
# mistakes/confusion: Na

## TIER 3 — Revision (2 problems)

"""
### 1. Longest Consecutive Sequence — Medium
Given an unsorted integer array `nums`, return the length of the longest run of consecutive integer values. The algorithm should run in O(n) time.

Example 1: `nums = [100,4,200,1,3,2]` → Output: `4`
Example 2: `nums = [0,3,7,2,5,8,4,6,0,1]` → Output: `9`
Example 3: `nums = []` → Output: `0`

Constraints: `0 <= nums.length <= 10^5`, `-10^9 <= nums[i] <= 10^9`.

```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()

        for i in nums:
            seen.add(i)
        
        
        maxlen = 0

        for j in seen:

            if j-1 not in seen:
                startnum = j
                count =1

                while startnum + 1 in seen:
                    startnum += 1
                    count += 1
                maxlen = max(maxlen,count)
        return maxlen
    
# Status: Independent
# Time taken: 25 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(n)
# LC status: Accepted 
# Pattern: Consecutive Sequence
# Variant: ___
# mistakes/confusion: NA

"""
### 2. Maximum Number of Vowels in a Substring of Given Length — Medium
Given a string `s` and an integer `k`, return the maximum number of vowel characters in any substring of length `k`. The vowel characters are `a`, `e`, `i`, `o`, and `u`.

Example 1: `s = "abciiidef", k = 3` → Output: `3`
Example 2: `s = "aeiou", k = 2` → Output: `2`
Example 3: `s = "leetcode", k = 3` → Output: `2`

Constraints: `1 <= s.length <= 10^5`, `s` contains lowercase English letters, `1 <= k <= s.length`.

```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

"""

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        countofowel = 0

        best = 0

        left = 0

        for right in range(len(s)):

            if s[right] in 'aeiou':
                countofowel += 1
            
            while right-left+1 > k:

                if s[left] in 'aeiou':
                    countofowel -= 1
                left +=1
            
            if right-left+1 == k:
                best = max(best,countofowel)
        return best


# Status: Independent
# Time taken: 15 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted 
# Pattern: Sliding window
# Variant: Fixed size
# mistakes/confusion:na




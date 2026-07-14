## TIER 4 Recalls (5 min each, no full solve)

#1. Prefix Sum

def prefixsum(nums):

    totalsum = sum(nums)

    left = 0

    for i in range(len(nums)):

        right = totalsum - left - nums[i]

        if right == left:
            return i
        
        left += nums[i]
    return -1

#2. Two Pointers

def twopointers(nums):

    left = 0
    right = len(nums)-1

    maxwater = 0

    while left < right:

        water = min(nums[left],nums[right]) * (right - left)

        if nums[right] < nums[left]:
            right -=1
        else:
            left +=1
        
        maxwater = max(maxwater,water)
    
    return maxwater

## TIER 1 — Priority Revision (solve these first, all of them)


def totalappeal(s):

    count = 0

    for i in range(len(s)):

        seen = set()

        for j in range(i,len(s)):

            seen.add(s[j])

            count += len(seen)
    return count

print(totalappeal("abbca"))
print(totalappeal("code"))

# Status: Independent
# Time taken: 15 min
# Tier: ___
# Time complexity: O(n^2)
# Space complexity: O(n)
# LC status:Not submitted
# Pattern: Nested loop
# Variant: ___
# mistakes/confusion: Keep this problem on hold for next 5 weeks untill i finish the linked list.

"""
### 2. Remove Nth Node From End of List — Medium
Given the head of a linked list and an integer `n`, remove the `n`th node from the end of the list and return the updated head.

Example 1:  
Input: `head = [1,2,3,4,5], n = 2` → Output: `[1,2,3,5]`

Example 2:  
Input: `head = [1], n = 1` → Output: `[]`

Example 3:  
Input: `head = [1,2], n = 1` → Output: `[1]`

Constraints:
- The number of nodes in the list is `sz`
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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

        num = n + 1

        while num > 0:
            
            fast = fast.next
            num -= 1
        
        while fast:

            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next


    
# Status: Independent
# Time taken: 15 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Slow and fast pointer.
# Variant: ___
# mistakes/confusion: Na

"""
### 3. Maximum Twin Sum of a Linked List — Medium
In a linked list with even length `n`, node `i` is paired with node `n - 1 - i`. The twin sum is the sum of the values in a paired set of nodes. Return the maximum twin sum in the linked list.

Example 1:  
Input: `head = [5,4,2,1]` → Output: `6`

Example 2:  
Input: `head = [4,2,2,3]` → Output: `7`

Example 3:  
Input: `head = [1,100000]` → Output: `100001`

Constraints:
- `2 <= n <= 10^5`
- `n` is even
- `1 <= Node.val <= 10^5`

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

        fast = head
        slow = head

        while fast and fast.next:

            fast = fast.next.next
            slow = slow.next
        
        prev = None
        current = slow

        while current:

            next_node = current.next

            current.next = prev

            prev = current

            current = next_node
        
        right = prev
        left = head
        twin_sum = 0

        while right:

            twonodessum = right.val + left.val
            right = right.next
            left = left.next
            twin_sum = max(twin_sum,twonodessum)
        
        return twin_sum

# Status: Independent
# Time taken: 15 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted 
# Pattern: Fast and slow + revarsal
# Variant: ___
# mistakes/confusion: Na

## TIER 2 — Revision (3 problems)

"""
### 1. Koko Eating Bananas — Medium
You are given `piles`, where `piles[i]` is the number of bananas in the `i`th pile, and an integer `h`. Koko chooses an integer speed `k`. Each hour, she chooses one pile and eats up to `k` bananas from it. Return the minimum integer `k` such that she can finish all the bananas within `h` hours.

Example 1:
- Input: `piles = [3,6,7,11], h = 8`
- Output: `4`

Example 2:
- Input: `piles = [30,11,23,4,20], h = 5`
- Output: `30`

Example 3:
- Input: `piles = [30,11,23,4,20], h = 6`
- Output: `23`

Constraints:
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
        
        def feasible(num):

            countofhrs = 0

            for i in piles:

                if i <= num:
                    countofhrs += 1
                else:

                    division = i // num
                    remainder = 1 if i % num != 0 else 0
                    countofhrs += division + remainder

                    
            if countofhrs > h:
                return False
            else:
                return True
        
        
        left = 1
        right = max(piles)

        while left < right:

            mid = (right + left) // 2

            isfeasible = feasible(mid)

            minspeed = float('inf')

            if isfeasible:
                right = mid
            else :
                left = mid + 1
        return left
    

# Status: Independent
# Time taken: 25 min
# Tier: ___
# Time complexity: O(n log m)
# Space complexity: O(1)
# LC status: Accepted 
# # Pattern: Binary search
# Variant: ___
# mistakes/confusion: Na


"""
### 2. Reverse Linked List II — Medium
Given the head of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right` (1-indexed). Return the reversed list.

Example 1:
- Input: `head = [1,2,3,4,5], left = 2, right = 4`
- Output: `[1,4,3,2,5]`

Example 2:
- Input: `head = [5], left = 1, right = 1`
- Output: `[5]`

Constraints:
- `n` is number of nodes.
- `1 <= n <= 500`
- `-500 <= Node.val <= 500`
- `1 <= left <= right <= n`

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

        dummy.next =  head 

        postion = 1
        
        while postion < left:

            prev = current

            current = current.next

            postion += 1
        
        
        before_left = prev
        left_node = current

        prev = None

        num = right-left+1

        while num > 0:

            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            num -= 1
        
        before_left.next = prev
        left_node.next = current

        return dummy.next

# Status: Independent
# Time taken: 20 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Traversal + Revarsal.
# Variant: ___
# mistakes/confusion: Na

"""
### 3. Merge Two Sorted Lists — Easy
You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted list and return the head of the merged list.

Example 1:
- Input: `list1 = [1,2,4], list2 = [1,3,4]`
- Output: `[1,1,2,3,4,4]`

Example 2:
- Input: `list1 = [], list2 = []`
- Output: `[]`

Example 3:
- Input: `list1 = [], list2 = [0]`
- Output: `[0]`

Constraints:
- `0 <= number of nodes <= 50` for each list
- `-100 <= Node.val <= 100`
- Both lists are sorted in non-decreasing order.

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
# Time taken: 15 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Traversal + linking nodes in assendng order
# Variant: ___
# mistakes/confusion: na

## TIER 3 — Revision (2 problems)

"""
### 1. Longest Consecutive Sequence — Medium
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

A consecutive sequence is a sequence of elements such that each element's value is exactly `1` greater than the previous element.

Example 1:
- Input: `nums = [100,4,200,1,3,2]`
- Output: `4`  
(Explanation: The longest consecutive sequence is `[1,2,3,4]`.)

Example 2:
- Input: `nums = [0,3,7,2,5,8,4,6,0,1]`
- Output: `9`

Example 3:
- Input: `nums = []`
- Output: `0`

Constraints:
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

```python
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

        max_len = 0
        
        for num in seen:

            if num-1 not in seen:
                sequncenum= num
                length = 1

                while sequncenum + 1 in seen:
                    sequncenum += 1
                    length += 1
                max_len = max(max_len,length)
        return max_len
    
# Status: Independent
# Time taken: 20 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: consecutive sequence
# Variant: ___
# mistakes/confusion: Na

"""
### 2. Maximum Number of Vowels in a Substring of Given Length — Medium
Given a string `s` and an integer `k`, return the maximum number of vowel letters in any substring of `s` with length `k`.

The vowel letters are: `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

Example 1:
- Input: `s = "abciiidef", k = 3`
- Output: `3`

Example 2:
- Input: `s = "aeiou", k = 2`
- Output: `2`

Example 3:
- Input: `s = "leetcode", k = 3`
- Output: `2`

Constraints:
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters
- `1 <= k <= s.length`

"""

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0

        max_vowels = 0

        count = 0

        for right in range(len(s)):

            if s[right] in 'aeiou':
                count += 1
            
            while right-left+1 > k:

                if s[left] in 'aeiou':
                    count -= 1
                left += 1
            
            if right-left+1 == k:
                max_vowels = max(max_vowels,count)
        return max_vowels
    

# Status: Independent
# Time taken: 10 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted 
# Pattern: Sliding wondow
# Variant: Fixed size
# mistakes/confusion:Na

## New Problems (2 problems)

# (Linked Lists variants — choose new concept variants after doing TIER 1)

"""
### 1. Reverse Linked List — Medium
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
- Input: `head = [1,2,3,4,5]`
- Output: `[5,4,3,2,1]`

Example 2:
- Input: `head = [null]`
- Output: `[]`

Example 3:
- Input: `head = [1]`
- Output: `[1]`

Constraints:
- `0 <= The number of nodes in the list <= 5000`
- `-5000 <= Node.val <= 5000`

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___

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

        while current:

            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev

# Status: Independent
# Time taken: 15 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Revarsal
# Variant: 
# mistakes/confusion: Na

"""
### 2. Linked List Cycle — Medium
Given head, the head of a linked list, determine if the linked list has a cycle.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.

Return `true` if there is a cycle, otherwise return `false`.

Example 1:
- Input: head = [3,2,0,-4], pos = 1
- Output: true

Example 2:
- Input: head = [1,2], pos = 0
- Output: true

Example 3:
- Input: head = [1], pos = -1
- Output: false

Constraints:
- The number of the nodes in the list is in the range `[0, 10^4]`
- `-10^4 <= Node.val <= 10^4`
- `pos` is `-1` or a valid index in the linked list.

```python
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
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = set()

        current = head

        while current:

            if current in seen:
                return True
            
            seen.add(current)
            current = current.next
        return False  
        
# Status: Hint
# Time taken: 25 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(n)
# LC status: Accepted.
# Pattern:Traversal+Mebmbeship check
# Variant: ___
# mistakes/confusion: Na


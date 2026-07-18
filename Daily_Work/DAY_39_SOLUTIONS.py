## TIER 4 Recalls (5 min each, no full solve)

# Write the [pattern] template from memory. If you can't in 3 min → flag as Tier 2.

# 1. Prefix Sum + Modulo

def prefixsum(nums,k):

    pefix = 0

    seen = {0:1}

    count = 0

    for i in range(len(nums)):

        pefix += nums[i]

        needed = pefix % k

        if needed in seen:
            count += seen[needed]
        
        seen[needed]= seen.get(needed,0)+1

    return count

# 2. Linked List Fast/Slow + Reversal

def linkedlist(head):

    fast = head
    slow = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next
    
    current = slow 

    prev = None 

    while current:

        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return head

# Pattern 1 recalled correctly (Y/N):No

# Pattern 2 recalled correctly (Y/N):Yes

## TIER 1 — Priority Revision (solve these first, all of them)


"""
### 1. Linked List Cycle — Easy
Given the head of a linked list, determine whether the linked list contains a cycle. A cycle exists if following `next` pointers can bring you back to a previously visited node.

Return `true` if there is a cycle, otherwise return `false`.

Example 1:
- Input: `head = [3,2,0,-4], pos = 1`
- Output: `true`
- Explanation: the tail connects back to the node at index `1`.

Example 2:
- Input: `head = [1,2], pos = 0`
- Output: `true`

Example 3:
- Input: `head = [1], pos = -1`
- Output: `false`

Constraints:
- The number of nodes is in the range `[0, 10^4]`
- `-10^4 <= Node.val <= 10^4`
- `pos` is `-1` or a valid index in the linked list

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

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

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

# Status: Independent
# Time taken: 15 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(n)
# LC status: Accepted
# Pattern: Hashmap + Traversal
# Variant: ___
# mistakes/confusion: Na

"""
### 2. Find the Divisibility Array of a String — Medium
Given a 0-indexed string `word` of digits and a positive integer `m`, return an integer array `div` of the same length as `word`.

For each index `i`, `div[i] = 1` if the numeric value of `word[0...i]` is divisible by `m`; otherwise `div[i] = 0`.

Example 1:
- Input: `word = "998244353", m = 3`
- Output: `[1,1,0,0,0,1,1,0,0]`

Example 2:
- Input: `word = "1010", m = 10`
- Output: `[0,1,0,1]`

Constraints:
- `1 <= word.length <= 10^5`
- `word` consists of digits only
- `word` does not contain leading zeros
- `1 <= m <= 10^9`

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
    def divisibilityArray(self, word, m):
        """
        :type word: str
        :type m: int
        :rtype: List[int]
        """

        out = []

        remainder = 0

        for i in range(len(word)):

            remainder = (remainder * 10 + int(word[i])) % m

            if remainder == 0:
                out.append(1)
            else:
                out.append(0)
        return out

# Status: Independent
# Time taken: 20 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(n)
# LC status: Accepted
# Pattern: prefix sum + modulo
# Variant: ___
# mistakes/confusion:NA

"""
### 3. Reorder List — Medium
Given the head of a singly linked list ordered as `L0 → L1 → ... → Ln`, reorder it in-place to `L0 → Ln → L1 → Ln-1 → L2 → Ln-2 ...`.

Do not change node values; only rearrange node links.

Example 1:
- Input: `head = [1,2,3,4]`
- Output: `[1,4,2,3]`

Example 2:
- Input: `head = [1,2,3,4,5]`
- Output: `[1,5,2,4,3]`

Constraints:
- The number of nodes is in the range `[1, 5 * 10^4]`
- `1 <= Node.val <= 1000`

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

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        #Phase 1(find mid+1)

        slow = head
        fast = head

        while fast and fast.next:

            slow= slow.next
            fast = fast.next.next
        
        current = slow.next
        slow.next = None

        prev = None

        while current:

            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        left = head
        right = prev

        while right:

            left_next = left.next
            right_next = right.next

            left.next = right
            right.next = left_next

            left = left_next
            right = right_next
        
        return head
    
 # Status: Independent
# Time taken: 25 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Slow and Fast + Reversal + reorder
# Variant: ___
# mistakes/confusion: Na


## TIER 2 — Revision (3 problems)

"""
### 1. Middle of the Linked List — Easy
Given the head of a singly linked list, return the middle node. If there are two middle nodes, return the second middle node.

Example 1:
- Input: `head = [1,2,3,4,5]`
- Output: `[3,4,5]`

Example 2:
- Input: `head = [1,2,3,4,5,6]`
- Output: `[4,5,6]`

Constraints:
- The number of nodes is in the range `[1, 100]`
- `1 <= Node.val <= 100`

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
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
        
        return slow
        
# Status: Independent
# Time taken: 10 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Slow and fast pointers
# Variant: ___
# mistakes/confusion: Na

"""
### 2. Linked List Cycle II — Medium
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return `None`.

The input uses `pos` to describe where the tail connects, but `pos` is not passed to your function.

Example 1:
- Input: `head = [3,2,0,-4], pos = 1`
- Output: node with value `2`

Example 2:
- Input: `head = [1,2], pos = 0`
- Output: node with value `1`

Example 3:
- Input: `head = [1], pos = -1`
- Output: `None`

Constraints:
- The number of nodes is in the range `[0, 10^4]`
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked list

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
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head

        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None
        
        left = head
        right = fast

        while left != right:

            left = left.next
            right = right.next
        return left
    

# Status:Hint
# Time taken: 30 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Slow and Fast pointer and Floyed algo
# Variant: ___
# mistakes/confusion: Na

"""
### 3. Palindrome Linked List — Easy
Given the head of a singly linked list, return `true` if the node values form a palindrome; otherwise return `false`.

Example 1:
- Input: `head = [1,2,2,1]`
- Output: `true`

Example 2:
- Input: `head = [1,2]`
- Output: `false`

Constraints:
- The number of nodes is in the range `[1, 10^5]`
- `0 <= Node.val <= 9`

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
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        current = slow
        prev = None

        while current:

            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        left = head
        right = prev

        while right:

            if left.val != right.val:
                return False

            left = left.next
            right = right.next
        return True 

# Status: Independent
# Time taken: 15 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: slow and Fast + Reversal
# Variant: ___
# mistakes/confusion: Na


## TIER 3 — Revision (2 problems)

"""
### 1. Max Number of K-Sum Pairs — Medium
Given an integer array `nums` and an integer `k`, in one operation you can pick two numbers from the array whose sum equals `k` and remove them.

Return the maximum number of operations you can perform.

Example 1:
- Input: `nums = [1,2,3,4], k = 5`
- Output: `2`
- Explanation: remove pairs `(1,4)` and `(2,3)`.

Example 2:
- Input: `nums = [3,1,3,4,3], k = 6`
- Output: `1`
- Explanation: remove one pair `(3,3)`.

Constraints:
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= 10^9`

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
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left  = 0
        right = len(nums)-1
        count = 0
        sorted_nums = sorted(nums)

        while left < right:
            
            num = sorted_nums[left]+sorted_nums[right]

            if num == k:
                count += 1
                left += 1
                right -= 1
            elif num > k:
                right -= 1
            else:
                left += 1
        return count
    
# Status: Independent
# Time taken: 15 min
# Tier: ___
# Time complexity: O(n + logm)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Two pointers + Sorting
# Variant: Na
# mistakes/confusion: Na

"""
### 2. Minimize Maximum Pair Sum in Array — Medium
Given an array `nums` of even length, pair every number with exactly one other number. The pair sum is the sum of a pair. Return the minimized maximum pair sum among all pairs.

Example 1:
- Input: `nums = [3,5,2,3]`
- Output: `7`
- Explanation: pair `(3,3)` and `(5,2)`, maximum pair sum is `7`.

Example 2:
- Input: `nums = [3,5,4,2,4,6]`
- Output: `8`

Constraints:
- `2 <= nums.length <= 10^5`
- `nums.length` is even
- `1 <= nums[i] <= 10^5`

"""
class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sorted_nums = sorted(nums)

        left = 0
        right = len(sorted_nums)-1
        maxpair = 0

        while left < right:

            num = sorted_nums[left] + sorted_nums[right]

            maxpair = max(maxpair, num)

            left += 1
            right -= 1
        return maxpair

# Status: Independent 
# Time taken: 10 min
# Tier: ___
# Time complexity: O(n + log m)
# Space complexity: O(1)
# Pattern: Two pointers + sorting
# LC status: Accepted
# Variant: 
# mistakes/confusion:Na

## New Problems (2 problems)


"""

### 1. Odd Even Linked List — Medium
Given the head of a singly linked list, group all nodes with odd indices together followed by all nodes with even indices, and return the reordered list.

The first node is considered odd, the second node is even, and so on. Keep the relative order inside the odd group and inside the even group.

Example 1:
- Input: `head = [1,2,3,4,5]`
- Output: `[1,3,5,2,4]`

Example 2:
- Input: `head = [2,1,3,5,6,4,7]`
- Output: `[2,3,6,7,1,5,4]`

Constraints:
- The number of nodes is in the range `[0, 10^4]`
- `-10^6 <= Node.val <= 10^6`

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
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:

            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next
        
        odd.next = even_head

        return head
    
# Status: Hint
# Time taken: 35 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Linked List Pointer Manipulation(In-Place List Partitioning)
# Variant: Odd-Even Index Partition
# mistakes/confusion: Na

"""
### 2. Swap Nodes in Pairs — Medium
Given the head of a linked list, swap every two adjacent nodes and return the head of the modified list.

You must solve the problem without modifying node values; only node links may be changed.

Example 1:
- Input: `head = [1,2,3,4]`
- Output: `[2,1,4,3]`

Example 2:
- Input: `head = []`
- Output: `[]`

Example 3:
- Input: `head = [1]`
- Output: `[1]`

Constraints:
- The number of nodes is in the range `[0, 100]`
- `0 <= Node.val <= 100`

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

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:

            first = prev.next
            second = first.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = first
        
        return dummy.next

# Status:Hint
# Time taken: 35 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Local Pointer Rewiring
# Variant: ___
# mistakes/confusion: Na

## TIER 4 Recalls (5 min each, no full solve)

# Write the pattern template from memory. If you can't in 3 min → flag as Tier 2.

# 1. Sliding Window (Fixed size)

def silidingwindow(nums,k):

    left = 0

    best = 0

    prefix = 0

    for right in range(len(nums)):

        prefix += nums[right]

        while right-left+1 > k:

            prefix -=nums[left]

            left+=1
        
        if right-left+1 == k:
            best = max(best,prefix)
    return best

# 2. Binary Search (Standard)


def search(nums, target):
       
        left = 0
        right = len(nums)-1

        while left <= right:

            mid = (right+left)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

## TIER 1 — Priority Revision (solve all 3, no hints)

"""
### 1. Total Appeal of A String — Hard
The appeal of a string is the number of distinct characters found in the string. Given a string `s`, return the total appeal of all of its substrings.
Note: 3 consecutive attempts have been brute force O(n²) only. This time, before coding, write out: for each character at index `i`, how many substrings is it the LAST occurrence contributing to? (Hint: compare to the previous index that character appeared at.)

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

                count +=len(seen)
                
        return count

# Status: independent 
# Time taken: 15 min
# Tier:
# Time complexity: O(n^2)
# Space complexity: O(1)
# LC status: Not submitted
# Pattern:Nested loop brute force
# Variant:
# mistakes/confusion: ill finish optimal today eod with special session.


"""
### 2. Reverse a Singly Linked List — Easy
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
        current = head
        prev = None

        while current != None:

            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        return prev

# Status: independent
# Time taken: 15 min
# Tier:
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern:Link reversal 
# Variant:
# mistakes/confusion:Na

"""
### 3. Reverse a Linked List Between Two Positions — Medium
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
```
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

        #Step-1 reach untill left node.

        position = 1

        while position < left:

            prev = current

            current = current.next

            position +=1

        

        #Step -2 reversal b/w two nodes

        before_left = prev
        left_node = current
        prev = None

        while right-left+1 > 0:

            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

            right -= 1
        
        before_left.next = prev
        left_node.next = current

        return dummy.next

# Status: hints (before_left.next left_node.next instead of using pinters i used nodes to reconnection)
# Time taken: 30 min
# Tier:
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Linked list reversal b/w two nodes
# Variant:
# mistakes/confusion: Na

## TIER 3 — Revision (2 problems — one overdue pick + one due today)

"""
### 1. Length of Last Word — Easy
Given a string `s` consisting of words and spaces, return the length of the last word in the string. A word is a maximal substring consisting of non-space characters only.

Example 1: `s = "Hello World"` → Output: `5`
Example 2: `s = "   fly me   to   the moon  "` → Output: `4`
Example 3: `s = "luffy is still joyboy"` → Output: `6`

Constraints: `1 <= s.length <= 10^4`, `s` consists of only English letters and spaces `' '`. There will be at least one word in `s`.

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
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0
        lenoflastword = 0

        for i in range(len(s)):

            if s[i] == " ":
                count = 0
            else:
                count += 1
            
            if count != 0:

                lenoflastword = count

        return lenoflastword


# Status: independent
# Time taken: 10 min
# Tier:
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: String Traversal
# Variant:
# mistakes/confusion:Na

"""
### 2. First Bad Version — Easy
You are a product manager leading a team to develop a new product. Since each version is developed based on the previous version, all the versions after a bad version are also bad. Suppose you have `n` versions `[1, 2, ..., n]` and you want to find the first bad one, which causes all the following ones to be bad. You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version, minimizing calls to the API.

Example 1: `n = 5, bad = 4` → Output: `4`
Example 2: `n = 1, bad = 1` → Output: `1`

Constraints: `1 <= bad <= n <= 2^31 - 1`

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

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(num):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left = 0

        right = n

        firstbad = 0


        while left <= right:

            mid = (right+left)//2

            num = isBadVersion(mid)

            if num:
                firstbad = mid
                right = mid - 1
            else:
                left = mid + 1

        return firstbad
    
# Status: independent
# Time taken: 15 min
# Tier:
# Time complexity: O(log n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: binary search 
# Variant: boundry search
# mistakes/confusion:Na

"""
### 1. Merge Two Sorted Lists — Easy
You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted list by splicing together the nodes of the first two lists. Return the head of the merged linked list.

Example 1: `list1 = [1,2,4], list2 = [1,3,4]` → Output: `[1,1,2,3,4,4]`
Example 2: `list1 = [], list2 = []` → Output: `[]`
Example 3: `list1 = [], list2 = [0]` → Output: `[0]`

Constraints: number of nodes in both lists is in the range `[0, 50]`, `-100 <= Node.val <= 100`, both `list1` and `list2` are sorted in non-decreasing order.

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

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode(0)

        current = dummy

        while list1 and list2:

            if list1.val <= list2.val:
                current.next= list1
                list1 = list1.next
            else:
                current.next= list2
                list2= list2.next
            
            current= current.next
        
        current.next = list1 if list1 else list2

        return dummy.next
    

# Status: hint
# Time taken: 35 min
# Tier:
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Two Pointer Merge
# Variant:
# mistakes/confusion:Na

"""
### 2. Remove Nth Node From End of List — Medium
Given the head of a linked list, remove the `n`th node from the end of the list and return its head.

Example 1: `head = [1,2,3,4,5], n = 2` → Output: `[1,2,3,5]`
Example 2: `head = [1], n = 1` → Output: `[]`
Example 3: `head = [1,2], n = 1` → Output: `[1]`

Constraints: number of nodes `sz`, `1 <= sz <= 30`, `0 <= Node.val <= 100`, `1 <= n <= sz`

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
            n -=1
        
        while fast:

            fast= fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next
    
 # Status: hint
# Time taken: 35 min
# Tier:
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Fast and slow pointers
# Variant:
# mistakes/confusion:   

"""
### 3. Maximum Twin Sum of a Linked List — Medium
*(Carried over from Day 34 — planned but not attempted.)*
In a linked list of size `n`, where `n` is even, the `i`th node (0-indexed) is the twin of the `(n-1-i)`th node, for `0 <= i <= (n/2)-1`. The twin sum is defined as the sum of a node and its twin. Given the head of a linked list of even length, return the maximum twin sum.

Example 1: `head = [5,4,2,1]` → Output: `6`
Example 2: `head = [4,2,2,3]` → Output: `7`
Example 3: `head = [1,100000]` → Output: `100001`

Constraints: number of nodes `n`, `2 <= n <= 10^5`, `n` is even, `1 <= Node.val <= 10^5`

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
            
     
        prv = None
        current = slow

        while current:

            next_node = current.next
            current.next = prv
            prv = current
            current = next_node
        
        # beforeleft.next = prv
        # leftnode.next = None

        
        left = head
        right = prv

        twinsum = 0

        while right:

            sumofapair = left.val + right.val

            left=left.next
            right = right.next
            twinsum = max(twinsum,sumofapair)
        
        return twinsum

# Status: hints
# Time taken: 35 min
# Tier:
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: slow and fast pointers & reversal.
# Variant:
# mistakes/confusion:Na



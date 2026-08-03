## Tier 4 Recalls (5 min each)

# Write the template from memory.

# 1. Frequency Hashing

def frequencyhashing(nums):

    seen ={}

    for i in nums:
        seen[i]=seen.get(i,0)+1

    return seen

# 2. Grouping Hash Maps


def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        seen = {}

        for word in strs:

            sorted_word = "".join(sorted(word))

            if sorted_word in seen:
                seen[sorted_word] += [word]
            else:
                seen[sorted_word] = [word]
        
        return seen.values()

## Tier 2 — Revision

"""
### Remove All Adjacent Duplicates in String (LC 1047)
You are given a string `s` consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on `s` until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

**Example 1:**
Input: s = "abbaca"
Output: "ca"

**Example 2:**
Input: s = "azxxzy"
Output: "ay"

"""

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []

        for i in s:

            if stack:
                if stack[-1] == i:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        
        answer = "".join(stack)

        return answer


# Status: Independent
# Time taken: 20 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Stack
# Variant: Remove adjacent duplicates
# mistakes/confusion: Na



## Tier 3 — Revision (8 Problems)

"""

### Peak Index in Mountain Array (LC 852)
An array `arr` is a mountain if the following properties hold:
- `arr.length >= 3`
- There exists some `i` with `0 < i < arr.length - 1` such that:
  - `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`
  - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

Given a mountain array `arr`, return the index `i` such that the above properties hold. You may assume that a valid answer always exists.

**Example 1:**
Input: arr = [0,1,0]
Output: 1

**Example 2:**
Input: arr = [0,2,1,0]
Output: 1

"""

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left = 0
        right = len(arr)-1

        while left < right:

            mid = (right+left)//2

            if arr[mid]>arr[mid+1]:
                right = mid
            else:
                left = mid+1 
        return left

# Status: Independent
# Time taken: 7 min
# Time complexity: O(logn)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Binary search
# Variant: applied boundry search
# mistakes/confusion: Na

"""
### Remove Duplicates from Sorted Array (LC 26)
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:
- Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially.
- Return `k`.

**Example 1:**
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

**Example 2:**
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        write = 1

        for i in range(1,len(nums)):

            if nums[i] != nums[write-1]:
                nums[write] = nums[i]
                write += 1
        
        return write

# Time taken: 10 min
# Time complexity: O(n)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Two pointers
# Variant: write pointer
# mistakes/confusion: Na

"""
### Max Number of K-Sum Pairs (LC 1679)
You are given an integer array `nums` and an integer `k`.

In one operation, you can pick two numbers from the array whose sum equals `k` and remove them from the array.

Return the maximum number of such operations you can perform on the array.

**Example 1:**
Input: nums = [1,2,3,4], k = 5
Output: 2

**Example 2:**
Input: nums = [3,1,3,4,3], k = 6
Output: 1

"""

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        sorted_nums = sorted(nums)

        count_operations = 0

        while left < right:

            num = sorted_nums[left] + sorted_nums[right]

            if num == k:
                count_operations += 1
                left += 1
                right -= 1
            elif num > k:
                right -= 1
            else:
                left += 1 

        return count_operations

# Time taken: 20 min
# Time complexity: O(nlogn)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Two pointers
# Variant: Maximize sorted
# mistakes/confusion: Na

"""
### Minimize Maximum Pair Sum in Array (LC 1877)
The pair sum of a pair `(a,b)` is equal to `a + b`. The maximum pair sum is the largest pair sum in a list of pairs.

For example, if we have pairs `(1,5)`, `(2,3)`, and `(4,4)`, the maximum pair sum would be `max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8`.

Given an array `nums` of even length `n`, pair up the elements of `nums` into `n / 2` pairs such that:
- Each element of `nums` is in exactly one pair, and
- The maximum pair sum is minimized.

Return the minimized maximum pair sum after optimally pairing up the elements.

**Example 1:**
Input: nums = [3,5,2,3]
Output: 7

**Example 2:**
Input: nums = [3,5,4,2,4,6]
Output: 8

"""

class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)

        left = 0
        right = len(nums)-1

        maximum_pair_sum = 0

        while left < right:

            pair_sum = sorted_nums[left] + sorted_nums[right]

            maximum_pair_sum = max(maximum_pair_sum,pair_sum)

            left += 1
            right -= 1
        
        return maximum_pair_sum

# Time taken: 7 min
# Time complexity: O(nlogn)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Two pointers
# Variant: Maximize sorted
# mistakes/confusion: Na

"""
### Linked List Cycle II (LC 142)
Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to (0-indexed). It is `-1` if there is no cycle.

**Example 1:**
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1

**Example 2:**
Input: head = [1,2], pos = 0
Output: tail connects to node index 0

**Example 3:**
Input: head = [1], pos = -1
Output: no cycle

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
        if not head or not head.next:
            return None

        slow = head

        fast = head

        while fast and fast.next:

            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                break
        else:
            return None
        
        
        slow = head 

        while slow != fast:

            slow = slow.next
            fast = fast.next
        
        return slow


# Time taken: 15 min
# Time complexity: O(n)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Linked List
# Variant: slow and Fast pointers + cycle entry
# mistakes/confusion: 

"""
### Odd Even Linked List (LC 328)
Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

**Example 1:**
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

**Example 2:**
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

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

            odd =  odd.next
            even = even.next

        odd.next = even_head

        return head

# Time taken: 20 min
# Time complexity: O(n)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Linked List
# Variant: In-place manipulation — odd-even index partition
# mistakes/confusion: Na

"""
### Linked List Cycle (LC 141)
Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

**Example 1:**
Input: head = [3,2,0,-4], pos = 1
Output: true

**Example 2:**
Input: head = [1,2], pos = 0
Output: true

**Example 3:**
Input: head = [1], pos = -1
Output: false

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

        slow = head 
        fast = head 

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False 
        

# Time taken: 10 min
# Time complexity: O(n)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Linked List
# Variant: slow and fast pointers 
# mistakes/confusion: Na

"""
### Swap Nodes in Pairs (LC 24)
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

**Example 1:**
Input: head = [1,2,3,4]
Output: [2,1,4,3]

**Example 2:**
Input: head = []
Output: []

**Example 3:**
Input: head = [1]
Output: [1]

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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
            second = prev.next.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = first
        
        return dummy.next

# Time taken: 15 min
# Time complexity: O(n)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Linked List
# Variant: In place pointers manipulation
# mistakes/confusion: Na

## New Problems


## Learning Block — Monotonic Stack (Next Greater Element Family)

"""
## Problem 1 — Next Greater Element I (LC 496)

You are given two distinct integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

For each element in `nums1`, find the first greater element to its right in `nums2`.

If none exists, return `-1`.

---

### Example 1

```text
Input:
nums1 = [4,1,2]
nums2 = [1,3,4,2]

Output:
[-1,3,-1]
```

---

### Example 2

```text
Input:
nums1=[2,4]
nums2=[1,2,3,4]

Output:
[3,-1]
```
"""

#Brute Force Solution

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        out = []
        for num in nums1:
            index = None
            for j in range(len(nums2)):

                if num == nums2[j]:
                    index =  j
                    break

            for k in range(index+1,len(nums2)):

                if nums2[k] > num:
                    out.append(nums2[k])
                    break
            else:
                out.append(-1)
        return out

# Status: Independent 
# Time taken: 30 min
# Time complexity: O(n^2)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Brute Force
# Variant: Next Greater Element
# mistakes/confusion: OPTIMAL APPROCH ALSO comes with same complexity if we use dict to store the elements of nums2 with ites indexes.

#Using Stack optimal approach.

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack =[]

        next_greater = {}

        for i in nums2:

            while stack and i > stack[-1]:

                next_greater[stack[-1]] = i

                stack.pop()

            stack.append(i)
        
        answer =[]
        for num in nums1:

            if num in next_greater:
                answer.append(next_greater[num])
            else:
                answer.append(-1)
        return answer

# Status: hint
# Time taken: 20 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Monotonic Stack
# Variant: Next Greater Element
# mistakes/confusion: Na


"""
## Problem 2 — Next Greater Element II (LC 503)

A circular array means the last element's next element is the first element.

Return the next greater element for every position.

---

### Example

```text
Input:
nums=[1,2,1]

Output:
[2,-1,2]
```

"""

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [-1]*len(nums)
        stack =[]

        n = len(nums)

        for i in range(n*2):

            while stack and nums[i%n] > nums[stack[-1]]:

                answer[stack[-1]] = nums[i%n]

                stack.pop()
            
            if i < n:
                stack.append(i)
        return answer

# Status: Independent
# Time taken: 20 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Monotonic Stack
# Variant: Stock Span
# mistakes/confusion: Na


# rest two Problems plan for the next day 

#I have mannually added the workload of 3 new problems.















    




## Tier 4 Recalls (5 min each)

# Write the template from memory.

# 1. Frequency Hashing — Count + query

def frequncyhashing(words,k):

    seen ={}

    for i in words:
        seen[i] = seen.get(i,0)+1

    sorted_seen = sorted(seen.items(),key=lambda x:(-x[1],x[0]))

    out  = []

    for key,value in sorted_seen:

        out.append(key)

        if len(out) == k:
            return out

#Status: Completed in 5m

# 2. Valid Anagram — Count + query

def validanagram(string1,string2):

    seen1={}

    seen2={}

    for i in string1:
        seen1[i]=seen1.get(i,0)+1
    for j in string2:
        seen2[j]=seen2.get(j,0)+1


    for k in string1:

        if k not in seen2:
            return False
        elif seen2[k] < seen1[k]:
            return False
    return True

#Status: Completed in 5m

## Tier 1 — Priority Revision

"""
### 1. Daily Temperatures (LC 739)

Given an array of integers `temperatures` represents the daily temperatures, return *an array* `answer` *such that* `answer[i]` *is the number of days you have to wait after the* `ith` *day to get a warmer temperature*. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

**Example 1:**
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

**Example 2:**
```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

**Example 3:**
```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

**Constraints:**
- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0]*len(temperatures)

        stack = []

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
 
                answer[stack[-1]] = i - stack[-1]

                stack.pop()
            
            stack.append(i)

        return answer

# Status: independent
# Time taken: 30 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted 
# Pattern: Monolethic stack
# Variant: ___
# mistakes/confusion: Na

## Tier 3 — Revision (7 Problems)

"""
### 2. Longest Consecutive Sequence (LC 128)

Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence*.

You must write an algorithm that runs in `O(n)` time.

**Example 1:**
```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

**Example 2:**
```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

**Constraints:**
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

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
        maxsequnce = 0
        
        for j in seen:

            if j-1 not in seen:
                num = j
                lenght = 1

                while num + 1 in seen:

                    num += 1
                    lenght +=1
            
                maxsequnce = max(maxsequnce,lenght)
        
        return maxsequnce

# Status: independent
# Time taken: 20 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Hashmap + sequence
# Variant: consecutive sequence
# mistakes/confusion: Na

"""
### 3. Maximum Number of Vowels in a Substring of Given Length (LC 1456)

Given a string `s` and an integer `k`, return *the maximum number of vowel letters in any substring of* `s` *with length* `k`.

Vowel letters in English are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

**Example 1:**
```
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
```

**Example 2:**
```
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
```

**Example 3:**
```
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
```

**Constraints:**
- `1 <= s.length <= 10^5`
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
        lenght = 0
        maxlen = 0

        for right in range(len(s)):
      
            if s[right] in ['a','e','i','o','u']:
                lenght += 1
            
            while right-left+1 > k:

                if s[left] in ['a','e','i','o','u']:
                    lenght -= 1
                left += 1
            
            if right-left+1 == k:
                maxlen = max(maxlen,lenght)
        return maxlen

# Status: independent
# Time taken: 15 min
# Time complexity: O(n)
# Space complexity: O(k)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Sliding window
# Variant: fixed size
# mistakes/confusion: Na

"""
### 4. Reverse Linked List (LC 206)

Given the `head` of a singly linked list, reverse the list, and return *the reversed list*.

**Example 1:**
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

**Example 2:**
```
Input: head = [1,2]
Output: [2,1]
```

**Example 3:**
```
Input: head = []
Output: []
```

**Constraints:**
- The number of nodes in the list is the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

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

        while current:

            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev

# Status: independent
# Time taken: 10 min
# Time complexity: O(n)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Linked list reversal
# Variant: reversal
# mistakes/confusion: Na

"""
### 5. Merge Two Sorted Lists (LC 21)

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return *the head of the merged linked list*.

**Example 1:**
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Example 2:**
```
Input: list1 = [], list2 = []
Output: []
```

**Example 3:**
```
Input: list1 = [], list2 = [0]
Output: [0]
```

**Constraints:**
- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in **non-decreasing** order.

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

# Status: independent
# Time taken: 15 min
# Time complexity: O(n)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Two Linked list pointer manupulation
# Variant:  tWO LINKED LIST MERGE
# mistakes/confusion: nA

"""
### 6. Reverse Linked List II (LC 92)

Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return *the reversed list*.

**Example 1:**
```
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
```

**Example 2:**
```
Input: head = [5], left = 1, right = 1
Output: [5]
```

**Constraints:**
- The number of nodes in the list is `n`.
- `1 <= n <= 500`
- `-500 <= Node.val <= 500`
- `1 <= left <= right <= n`

**Follow up:** Could you do it in one pass?

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

        dummy.next = head


        prev = dummy

        position = 1

        current = head
        
        while position < left:

            prev = current
            
            current =  current.next

            position += 1
        
        before_left = prev
        left_node = current

        prev = None

        n = right-left+1

        while n > 0:

            next_node =  current.next
            current.next = prev
            prev = current
            current = next_node
            n -= 1
        
        before_left.next = prev
        left_node.next = current

        return dummy.next


# Status: independent
# Time taken: 15 min
# Time complexity: O(n)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Traversal + revarsal
# Variant: Reverse b/w two Nodes
# mistakes/confusion: Na

"""
### 7. Remove Nth Node From End of List (LC 19)

Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

**Example 1:**
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

**Example 2:**
```
Input: head = [1], n = 1
Output: []
```

**Example 3:**
```
Input: head = [1,2], n = 1
Output: [1]
```

**Constraints:**
- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

**Follow up:** Could you do this in one pass?

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

        dummy.next = head

        right = dummy
        left = dummy

        position = 1

        while position <= n:

            right =  right.next
            position += 1
        
        prev = None

        while right:
            prev = left
            right = right.next
            left = left.next

        prev.next = prev.next.next

        return dummy.next

# Status: independent
# Time taken: 20 min
# Time complexity: O(n)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: SLow and Fast pointers
# Variant: remove nth Node
# mistakes/confusion: Na

"""
### 8. Maximum Twin Sum of a Linked List (LC 2130)

In a linked list of size `n`, where `n` is **even**, the `ith` node (**0-indexed**) of the linked list is known as the **twin** of the `(n-1-i)th` node, if `0 <= i <= (n / 2) - 1`.

* For example, if `n = 4`, then node `0` is the twin of node `3`, and node `1` is the twin of node `2`. These are the only nodes with twins for `n = 4`.

The **twin sum** is defined as the sum of a node and its twin.

Given the `head` of a linked list with even length, return *the **maximum twin sum** of the linked list*.

**Example 1:**
```
Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6.
```

**Example 2:**
```
Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in the linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7.
```

**Example 3:**
```
Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
```

**Constraints:**
- The number of nodes in the list is an **even** integer in the range `[2, 10^5]`.
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
        prev = None

        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None

        current = slow

        prev = None

        while current:

            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        right = prev
        left = head
        maxTwinsum = 0

        while right:

            sumoftwonodes =  left.val + right.val
            
            left = left.next
            right = right.next
            maxTwinsum = max(maxTwinsum,sumoftwonodes)
        
        return maxTwinsum

# Status: independent
# Time taken: 15 min
# Time complexity: O(n)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: slow and Fast pointer + Reversal
# Variant: Twin sum
# mistakes/confusion:Na







    
    




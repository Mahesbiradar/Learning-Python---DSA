## Tier 4 Recalls (5 min each)


# 1. Valid Palindrome (Two Pointers — Opposite Ends)


def validpalindrom(s):

    left = 0
    right = len(s)-1

    while left < right:

        if s[left] != s[right]:
            return False

        left += 1
        right -=1
    return True

def validpalindrom(s):

    left = 0
    right = len(s)-1

    while left < right:

        while not s[left].isalnum():
            left += 1

        while not s[right].isalnum():
            right -=1

        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True

# 2. Reverse String (Two Pointers — Opposite Ends)

def reversestring(s):

    left = 0
    right = len(s)-1

    while left < right:

        s[left], s[right] = s[right], s[left]

        left += 1
        right -=1

    return s

## Tier 3 — Revision (2 Problems)


"""

### 1. Contiguous Array (LC 525)

Given a binary array `nums`, return the maximum length of a contiguous subarray with an equal number of `0` and `1`.

**Example 1:**
```
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
```

**Example 2:**
```
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
```

**Constraints:**
- `1 <= nums.length <= 105`
- `nums[i]` is either `0` or `1`

"""

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_len = 0

        prefix = 0

        seen = {0:-1}

        for i in range(len(nums)):

            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1
            
            if prefix in seen:
                max_len = max(max_len, i-seen[prefix])
            else:
                seen[prefix] = i
        return max_len


# Status: Independent
# Time taken: 20 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Prefix sum
# Variant: Modulo
# mistakes/confusion:Na

"""
### 2. Top K Frequent Words (LC 692)

Given an array of strings `words` and an integer `k`, return the `k` most frequent strings.

Return the answer sorted by frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

**Example 1:**
```
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
```

**Example 2:**
```
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
```

**Constraints:**
- `1 <= words.length <= 500`
- `1 <= words[i].length <= 10`
- `words[i]` consists of lowercase English letters.
- `1 <= k <= number of unique words`

"""

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        seen = {}

        for i in words:

            seen[i] = seen.get(i,0)+1
        
        sorted_seen = sorted(seen.items(),key=lambda x:(-x[1],x[0]))

        out = []

        for key,value in sorted_seen:

            out.append(key)

            if len(out) == k:
                return out

# Status: Independent
# Time taken: 15 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Frequncy sorting
# Variant: 
# mistakes/confusion:Na

## Tier 3 — Revision Fillers (3 Problems)
"""
### 3. Find the Divisibility Array of a String (LC 2575)

You are given a 0-indexed string `word`, consisting of lowercase English letters. You need to select one index and remove the letter at that index from `word`.

The divisibility array `div` of `word` is an integer array of length `n` such that:
- `div[i] = 1` if the numeric value of `word[0,...,i]` is divisible by `m`, or
- `div[i] = 0` otherwise.

Return the divisibility array of `word`.

**Example 1:**
```
Input: word = "998244353", m = 3
Output: [1,1,0,0,0,1,1,0,0]
Explanation: There are only 4 prefixes that are divisible by 3: "9", "99", "998244", and "9982443".
```

**Example 2:**
```
Input: word = "1010", m = 10
Output: [0,1,0,1]
Explanation: There are only 2 prefixes that are divisible by 10: "10", and "1010".
```

**Constraints:**
- `1 <= n <= 105`
- `word.length == n`
- `word` consists of digits from `0` to `9`
- `1 <= m <= 109`

"""

class Solution(object):
    def divisibilityArray(self, word, m):
        """
        :type word: str
        :type m: int
        :rtype: List[int]
        """
        prefix = 0

        out = []

        for i in range(len(word)):

            prefix = (prefix * 10 + int(word[i])) % m

            if prefix == 0:
                out.append(1)
            else:
                out.append(0)
        return out

# Status: Independent
# Time taken: 15 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Prefix sum
# Variant: Modulo
# mistakes/confusion:Na

"""
### 4. Middle of the Linked List (LC 876)

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

**Example 1:**
```
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
```

**Example 2:**
```
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
```

**Constraints:**
- The number of nodes in the list is in the range `[1, 100]`.
- `1 <= Node.val <= 100`

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
# Time taken: 20 min
# Time complexity: O(n)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Fats and Slow pointers
# Variant: Middle
# mistakes/confusion:Na

"""
### 5. Reorder List (LC 143)

You are given the head of a singly linked-list. The list can be represented as:

```
L0 → L1 → … → Ln - 1 → Ln
```

Reorder the list to be on the following form:

```
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
```

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

**Example 1:**
```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

**Example 2:**
```
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

**Constraints:**
- The number of nodes in the list is in the range `[1, 5 * 104]`.
- `1 <= Node.val <= 1000`

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
        slow = head 
        fast = head
     
        while fast and fast.next:
  
            slow = slow.next
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
# Time complexity: O(n)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Fats and Slow pointers + revrersal + pointers manupulation
# Variant: Reorder List
# mistakes/confusion:Na


## New Problems — Stack: Basic Stack (3 Problems)

### Learning Block — Basic Stack Pattern

"""
### 6. Valid Parentheses (LC 20) — Easy

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1:**
```
Input: s = "()"
Output: true
```

**Example 2:**
```
Input: s = "()[]{}"
Output: true
```

**Example 3:**
```
Input: s = "(]"
Output: false
```

**Constraints:**
- `1 <= s.length <= 10^4`
- `s[i]` is a parenthesis `'('`, `')'`, `'{'`, `'}'`, `'['` or `']'`.

"""



class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs ={")":"(", "}":"{", "]":"["}

        for ch in s:

            if ch in ["(","{","["]:
                stack.append(ch)
            elif ch in pairs:
                if not stack or pairs[ch] != stack[-1]:
                    return False
                else:
                    stack.pop()

        
        return True if not stack else False

# Status: Hint
# Time taken: 25 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: stack
# Variant: valid parenthesis
# mistakes/confusion: na

"""
### 7. Min Stack (LC 155) — Medium

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

**Example 1:**
```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

**Constraints:**
- `-2^31 <= val <= 2^31 - 1`
- Methods `pop`, `top` and `getMin` operations will always be called on non-empty stacks.
- At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`.

"""

class MinStack(object):

    def __init__(self):

        self.stack = []
        self.minstack = []
        

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)

        if self.minstack:

            self.minstack.append(min(self.minstack[-1],value))
        else:
            self.minstack.append(value)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minstack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Status: hint
# Time taken: 30 min
# Time complexity: O(1)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: stack
# Variant: Min Stack
# mistakes/confusion: na


"""
### 8. Remove All Adjacent Duplicates In String (LC 1047) — Easy

You are given a string `s` consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on `s` until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

**Example 1:**
```
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
```

**Example 2:**
```
Input: s = "azxxzy"
Output: "ay"
```

**Constraints:**
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.

# Status: Independent / Hint / Failed
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

"""


class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for i in s:

            if not stack:
                stack.append(i)
            elif i != stack[-1]:
                stack.append(i)
            else:
                stack.pop()
        
        string = "".join(stack)

        return string

# Status: Independent
# Time taken: 10 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: stack
# Variant: Remove All Adjacent Duplicates
# mistakes/confusion: Na
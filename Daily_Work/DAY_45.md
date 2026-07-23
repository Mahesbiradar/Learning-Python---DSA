
---

# Day 45 — 2026-07-23 — Learning Day

Focus: Stack — Basic Stack (Valid Parentheses, Min Stack, Remove Adjacent Duplicates)

Phase: Stack + Queue — Volume Building

Daily Target: 10 Problems

---

## SOP Reminder (2 min before every problem)

Read → Restate → Identify Pattern → Plan in Words → Dry Run → Code → Test → Submit

---

## Tier 4 Recalls (5 min each)

Write the template from memory.

1. Valid Palindrome (Two Pointers — Opposite Ends)
2. Reverse String (Two Pointers — Opposite Ends)

---

## Tier 3 — Revision (2 Problems)

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

---

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

---

## Tier 3 — Revision Fillers (3 Problems)

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

---

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

---

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

---

## New Problems — Stack: Basic Stack (3 Problems)

### Learning Block — Basic Stack Pattern

**Where to learn:** NeetCode → Stack section → "Valid Parentheses" concept video (first 10 min)

**Trigger words:** matching brackets, next greater element, previous smaller, valid parentheses, remove adjacent duplicates, min stack

**Mental model:** A stack is a LIFO (Last-In-First-Out) structure. Think of a stack of plates — you can only add or remove from the top. In code problems, use a stack when you need to match the most recent element with the current one, or when you need to undo the last action.

**Why this pattern exists:** Brute force for matching problems is O(n²) because you repeatedly scan for pairs. A stack collapses this to O(n) by handling each element exactly once — every push has a corresponding pop, and the top of the stack always represents the most recent unmatched element.

**Blank template:**
```python
stack = []
for element in sequence:
    if matches_condition(element, stack):
        stack.pop()  # or stack.append(transformed)
    else:
        stack.append(element)
return build_result_from(stack)
```

**Dry run — Valid Parentheses on `"([{}])"`:**
- `'('` → push → stack: `['(']`
- `'['` → push → stack: `['(', '[']`
- `'{'` → push → stack: `['(', '[', '{']`
- `'}'` → matches `{` on top → pop → stack: `['(', '[']`
- `']'` → matches `[` on top → pop → stack: `['(']`
- `')'` → matches `(` on top → pop → stack: `[]`
- Stack empty → valid → `True`

**Common mistakes from PATTERNS.md:**
- Forgetting to check `if stack` before accessing `stack[-1]` (IndexError on empty stack)
- Pushing closing brackets instead of opening ones (map closing → opening, not the reverse)
- Returning `True` immediately when stack empties mid-string (must process entire string)
- Using a queue instead of a stack (breaks LIFO matching order)

---

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

# Status: Independent / Hint / Failed
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

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

# Status: Independent / Hint / Failed
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

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

---

## Daily Summary

New: 3 | Tier1: 0 | Tier2: 0 | Tier3: 5 | Tier4: 2 | Total: 10
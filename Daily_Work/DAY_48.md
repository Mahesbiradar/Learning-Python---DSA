---

# Day 48 — 2026-07-27 — Learning Day

Focus: Deque / Sliding Window Maximum

Phase: Stack + Queue — Volume Building

Daily Target: 12 Problems

---

## SOP Reminder (2 min before every problem)

Read → Restate → Identify Pattern → Plan in Words → Dry Run → Code → Test → Submit

---

## Tier 4 Recalls (5 min each)

Write the template from memory.

1. Frequency Hashing
2. Grouping Hash Maps

---

## Tier 1 — Priority Revision

None.

---

## Tier 2 — Revision

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

# Status: Independent / Hint / Failed
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Stack
# Variant: Remove adjacent duplicates
# mistakes/confusion: ___

---

## Tier 3 — Revision (8 Problems)

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

# Status: Independent / Hint / Failed
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Binary Search
# Variant: Applied — boundary search
# mistakes/confusion: ___

---

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

# Status: Independent / Hint / Failed
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Two Pointers
# Variant: Write pointer — compact/remove
# mistakes/confusion: ___

---

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

# Status: Independent / Hint / Failed
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Two Pointers
# Variant: Maximize sorted
# mistakes/confusion: ___

---

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

# Status: Independent / Hint / Failed
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Two Pointers
# Variant: Maximize sorted
# mistakes/confusion: ___

---

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

# Status: Independent / Hint / Failed
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Linked List
# Variant: Fast + slow pointer — cycle entry
# mistakes/confusion: ___

---

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

# Status: Independent / Hint / Failed
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Linked List
# Variant: In-place manipulation — odd-even index partition
# mistakes/confusion: ___

---

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

# Status: Independent / Hint / Failed
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Linked List
# Variant: Fast + slow pointer — cycle detection
# mistakes/confusion: ___

---

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

# Status: Independent / Hint / Failed
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Linked List
# Variant: In-place manipulation — local pointer rewiring
# mistakes/confusion: ___

---


# New Problems

## Learning Block — Monotonic Stack (Next Greater Element Family)

**Where to learn:** NeetCode Stack Playlist — Next Greater Element + Monotonic Stack

**Trigger words:**

* next greater
* next larger
* first greater element on right
* nearest greater
* stock span
* greater to left/right

**Mental model:**

Maintain a stack that stores indices (or values) in **monotonic decreasing order**.

Whenever a larger element arrives:

* Pop all smaller elements.
* The current element becomes their "Next Greater Element."
* Push the current index afterward.

Every element is pushed once and popped once.

---

**Why this pattern exists:**

Brute force checks every element against everything on its right.

```text
O(n²)
```

A monotonic stack keeps only useful candidates.

```text
O(n)
```

---

**State**

```python
stack = []
```

The stack stores indices whose next greater element hasn't been found yet.

---

**Common mistakes**

1. Storing values instead of indices when indices are needed.
2. Forgetting to pop all smaller elements.
3. Using `<` instead of `<=` when duplicates matter.
4. Forgetting to push the current index after popping.

---

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

---

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Monotonic Stack
# Variant: Next Greater Element
# mistakes/confusion: ___
```

---

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

---

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Monotonic Stack
# Variant: Circular Next Greater
# mistakes/confusion: ___
```

---

## Problem 3 — Online Stock Span (LC 901)

Design a class that collects daily stock prices and returns the stock span.

The span is the number of consecutive previous days whose price is **less than or equal** to today's price.

---

### Example

```text
Input

["StockSpanner","next","next","next","next","next","next","next"]

[[],[100],[80],[60],[70],[60],[75],[85]]

Output

[null,1,1,1,2,1,4,6]
```

---

```python
# Status: Independent / Hint /Failed
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Monotonic Stack
# Variant: Stock Span
# mistakes/confusion: ___
```

---

## Problem 4 — Asteroid Collision (LC 735)

We are given asteroids moving along a line.

Positive numbers move right.

Negative numbers move left.

When two asteroids moving toward each other collide:

* Smaller one explodes.
* If equal, both explode.

Return the final state.

---

### Example 1

```text
Input:
[5,10,-5]

Output:
[5,10]
```

---

### Example 2

```text
Input:
[8,-8]

Output:
[]
```

---

### Example 3

```text
Input:
[10,2,-5]

Output:
[10]
```

---

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Stack
# Variant: Simulation + Collision
# mistakes/confusion: ___
```



## Daily Summary

New: 4 | Tier1: 0 | Tier2: 1 | Tier3: 8 | Tier4: 2 | Total: 15
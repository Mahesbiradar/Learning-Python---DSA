---
# Day 40 — 2026-07-19 — Consolidation Day
Focus: Linked Lists — Floyd cycle + local pointer rewiring; Two Pointers complexity cleanup
Phase: New DS — Linked Lists (in progress)
Daily target: 10 problems/recalls

Consolidation trigger: Tier 1 backlog = 6, so new problems = 0 today.

---
## SOP Reminder (2 min before every problem)
Read fully → Restate in one line → Identify pattern → Plan in words → Dry run → Code → Test

Before code, write `# Pattern: ___ | Variant: ___`.
Complexity fields must be real answers with a one-sentence reason. Never leave `O(?)`.
Do not schedule Total Appeal O(n) before Aug 11.

---
## TIER 4 Recalls (5 min each, no full solve)
Write the [pattern] template from memory. If you can't in 3 min → flag as Tier 2.
1. Prefix Sum + Modulo
2. Linked List Fast/Slow + Reversal

```
# Pattern 1 recalled correctly (Y/N): ___
# Pattern 2 recalled correctly (Y/N): ___
```

---
## TIER 1 — Priority Revision (solve these first, all of them)

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
```

### 2. Linked List Cycle II — Medium
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return `None`.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that the tail's `next` pointer is connected to. `pos` is not passed as a parameter.

Do not modify the linked list.

Example 1:
- Input: `head = [3,2,0,-4], pos = 1`
- Output: tail connects to node index `1`
- Explanation: there is a cycle in the linked list, where tail connects to the second node.

Example 2:
- Input: `head = [1,2], pos = 0`
- Output: tail connects to node index `0`
- Explanation: there is a cycle in the linked list, where tail connects to the first node.

Example 3:
- Input: `head = [1], pos = -1`
- Output: no cycle
- Explanation: there is no cycle in the linked list.

Constraints:
- The number of nodes in the list is in the range `[0, 10^4]`
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
```

### 3. Max Number of K-Sum Pairs — Medium
Given an integer array `nums` and an integer `k`, in one operation you can pick two numbers from the array whose sum equals `k` and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:
- Input: `nums = [1,2,3,4], k = 5`
- Output: `2`
- Explanation: starting with `nums = [1,2,3,4]`:
  - Remove numbers `1` and `4`, then `nums = [2,3]`
  - Remove numbers `2` and `3`, then `nums = []`
  There are no more pairs that sum up to `5`, so a total of `2` operations.

Example 2:
- Input: `nums = [3,1,3,4,3], k = 6`
- Output: `1`
- Explanation: starting with `nums = [3,1,3,4,3]`:
  - Remove the first two `3`s, then `nums = [1,4,3]`
  There are no more pairs that sum up to `6`, so a total of `1` operation.

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
```

### 4. Minimize Maximum Pair Sum in Array — Medium
The pair sum of a pair `(a,b)` is equal to `a + b`. The maximum pair sum is the largest pair sum in a list of pairs.

Given an array `nums` of even length `n`, pair up the elements of `nums` into `n / 2` pairs such that each element of `nums` is in exactly one pair.

Return the minimized maximum pair sum after optimally pairing up the elements.

Example 1:
- Input: `nums = [3,5,2,3]`
- Output: `7`
- Explanation: pair the elements into `(3,3)` and `(5,2)`.
  The maximum pair sum is `max(6,7) = 7`.

Example 2:
- Input: `nums = [3,5,4,2,4,6]`
- Output: `8`
- Explanation: pair the elements into `(3,5)`, `(4,4)`, and `(6,2)`.
  The maximum pair sum is `max(8,8,8) = 8`.

Constraints:
- `n == nums.length`
- `2 <= n <= 10^5`
- `n` is even
- `1 <= nums[i] <= 10^5`

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

### 5. Odd Even Linked List — Medium
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

The relative order inside both the odd and even groups should remain as it was in the input.

Example 1:
- Input: `head = [1,2,3,4,5]`
- Output: `[1,3,5,2,4]`

Example 2:
- Input: `head = [2,1,3,5,6,4,7]`
- Output: `[2,3,6,7,1,5,4]`

Constraints:
- The number of nodes in the linked list is in the range `[0, 10^4]`
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
```

### 6. Swap Nodes in Pairs — Medium
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes. Only nodes themselves may be changed.

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
- The number of nodes in the list is in the range `[0, 100]`
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
```

---
## TIER 2 — Revision (3 problems)

No active Tier 2 problems due today.

---
## TIER 3 — Revision (2 problems)

### 1. Peak Index in a Mountain Array — Medium
An array `arr` is a mountain if:
- `arr.length >= 3`
- There exists some `i` with `0 < i < arr.length - 1` such that:
  - `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`
  - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

Given a mountain array `arr`, return the index `i` such that `arr[i]` is the peak.

Example 1:
- Input: `arr = [0,1,0]`
- Output: `1`

Example 2:
- Input: `arr = [0,2,1,0]`
- Output: `1`

Example 3:
- Input: `arr = [0,10,5,2]`
- Output: `1`

Constraints:
- `3 <= arr.length <= 10^5`
- `0 <= arr[i] <= 10^6`
- `arr` is guaranteed to be a mountain array

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

### 2. Remove Duplicates from Sorted Array — Easy
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Return `k`, the number of unique elements in `nums`.

The judge will test your solution by calling your function, then checking that the first `k` elements of `nums` contain the unique elements in their original order.

Example 1:
- Input: `nums = [1,1,2]`
- Output: `2, nums = [1,2,_]`
- Explanation: your function should return `k = 2`, with the first two elements of `nums` being `1` and `2`.

Example 2:
- Input: `nums = [0,0,1,1,1,2,2,3,3,4]`
- Output: `5, nums = [0,1,2,3,4,_,_,_,_,_]`
- Explanation: your function should return `k = 5`, with the first five elements of `nums` being `0,1,2,3,4`.

Constraints:
- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order

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

---
## New Problems (0 problems)

None today — Consolidation Day because Tier 1 backlog is 6.

---
## Daily Summary
New: 0 | Tier1: 6 | Tier2: 0 | Tier3: 2 | Tier4: 2 | Total: 10

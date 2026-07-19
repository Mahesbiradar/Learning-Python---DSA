```markdown
---
# Day 41 — 2026-07-20 — Consolidation Day
Focus: Linked Lists — Floyd O(1) cycle detection, local pointer rewiring; overdue Tier 3 catch-up
Phase: New DS — Linked Lists (in progress)
Daily target: 10 problems/recalls

Consolidation trigger: Tier 1 backlog = 2, but 5 overdue Tier 3 problems (Jul 15) require immediate attention. New problems = 0 today.

---

## SOP Reminder (2 min before every problem)

Read → Restate → Identify Pattern → Plan in Words → Dry Run → Code → Test → Submit

---

## Tier 4 Recalls (5 min each)

Write the template from memory.

1. Prefix Sum + Modulo
2. Linked List Fast/Slow + Reversal

---

## Tier 1 — Priority Revision (solve these first, all of them)

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
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___
```

### 2. Swap Nodes in Pairs — Medium
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
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___
```

---

## Tier 2 — Revision

No active Tier 2 problems due today.

---

## Tier 3 — Revision (2 Problems)

### 1. Search in Rotated Sorted Array — Medium
There is an integer array `nums` sorted in ascending order (with distinct values).

Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

Example 1:
- Input: `nums = [4,5,6,7,0,1,2], target = 0`
- Output: `4`

Example 2:
- Input: `nums = [4,5,6,7,0,1,2], target = 3`
- Output: `-1`

Example 3:
- Input: `nums = [1], target = 0`
- Output: `-1`

Constraints:
- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are unique.
- `nums` is guaranteed to be rotated at some pivot.
- `-10^4 <= target <= 10^4`

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___
```

### 2. Find Minimum in Rotated Sorted Array — Medium
Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated `4` times.
- `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.

You must write an algorithm that runs in `O(log n)` time.

Example 1:
- Input: `nums = [3,4,5,1,2]`
- Output: `1`
- Explanation: The original array was `[1,2,3,4,5]` rotated 3 times.

Example 2:
- Input: `nums = [4,5,6,7,0,1,2]`
- Output: `0`
- Explanation: The original array was `[0,1,2,4,5,6,7]` and it was rotated 4 times.

Example 3:
- Input: `nums = [11,13,15,17]`
- Output: `11`
- Explanation: The original array was `[11,13,15,17]` and it was rotated 4 times.

Constraints:
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are unique.
- `nums` is sorted and rotated between `1` and `n` times.

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___
```

---

## New Problems

None today — Consolidation Day because Tier 1 backlog + 5 overdue Tier 3 problems require full attention.

---

## Daily Summary

New: 0 | Tier1: 2 | Tier2: 0 | Tier3: 2 | Tier4: 2 | Total: 6
```


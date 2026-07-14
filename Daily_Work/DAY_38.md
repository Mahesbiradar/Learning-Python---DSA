---
# Day 38 — 2026-07-15 — Reinforcement Day
Focus: Linked Lists — cycle recovery + fast/slow follow-up, with overdue Tier 3 cleanup
Phase: New DS — Linked Lists (in progress)
Daily target: 10 problems/recalls
---

## SOP Reminder (2 min before every problem)
Read → Restate → Pattern Check → Brute Force (words) → Optimal Plan (words) → Dry Run → Code → Test → Submit

Full SOP: problem_solving.md. Before code, write `# Pattern: ___ | Variant: ___`.
Complexity fields must be real answers with a one-sentence reason. Never leave `O(?)`.

---
## TIER 4 Recalls (5 min each, no full solve)
Write the pattern template from memory. If you can't in 3 min → flag as Tier 2.
1. Prefix Sum
2. Binary Search

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

---
## TIER 2 — Revision (0 problems due)

No active Tier 2 problems are due today. Use the extra slot for overdue Tier 3 cleanup below.

---
## TIER 3 — Revision (3 problems)

Extra note: 2 Tier 3 problems were required; 1 extra overdue Tier 3 problem is included because the Tier 2 pool is empty.

### 1. Contiguous Array — Medium
Given a binary array `nums`, return the maximum length of a contiguous subarray with an equal number of `0`s and `1`s.

Example 1:
- Input: `nums = [0,1]`
- Output: `2`

Example 2:
- Input: `nums = [0,1,0]`
- Output: `2`

Constraints:
- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`

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

### 2. Find the Divisibility Array of a String — Medium
Given a numeric string `word` and an integer `m`, build an array `div` where `div[i] = 1` if the integer represented by `word[0..i]` is divisible by `m`; otherwise `div[i] = 0`.

Example 1:
- Input: `word = "998244353", m = 3`
- Output: `[1,1,0,0,0,1,1,0,0]`

Example 2:
- Input: `word = "1010", m = 10`
- Output: `[0,1,0,1]`

Constraints:
- `1 <= word.length <= 10^5`
- `word` contains digits only and does not start with `0`
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
```

### 3. Top K Frequent Words — Medium
Given a list of strings `words` and an integer `k`, return the `k` most frequent words. Sort by frequency from highest to lowest. If two words have the same frequency, sort them lexicographically.

Example 1:
- Input: `words = ["i","love","leetcode","i","love","coding"], k = 2`
- Output: `["i","love"]`

Example 2:
- Input: `words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4`
- Output: `["the","is","sunny","day"]`

Constraints:
- `1 <= words.length <= 500`
- `1 <= words[i].length <= 10`
- `words[i]` contains lowercase English letters
- `1 <= k <= number of unique words`

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
## New Problems (4 problems)

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
```

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
```

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

### 4. Reorder List — Medium
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
```

---
## Daily Summary
New: 4 | Tier1: 1 | Tier2: 0 | Tier3: 3 | Tier4: 2 | Total: 10

## Mandatory Closing Check
# Prompt 1 (End of Day agent) run: Yes / No
# STATUS.md updated: Yes / No

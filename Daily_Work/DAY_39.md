---
# Day 39 — 2026-07-16 — Reinforcement Day
Focus: Linked Lists — Floyd cycle cleanup + reorder cleanup; Prefix Sum modulo cold retry
Phase: New DS — Linked Lists (in progress) + Prefix Sum Modulo regression cleanup
Daily target: 12 problems/recalls

---
## SOP Reminder (2 min before every problem)
Read fully → Restate in one line → Identify pattern → Plan in words → Dry run → Code → Test

Before code, write `# Pattern: ___ | Variant: ___`.
Complexity fields must be real answers with a one-sentence reason. Never leave `O(?)`.
Do not schedule Total Appeal O(n) before Aug 11.

---
## Reinforcement Warm-Up
1. Write the core template from memory.
2. The invariant this template maintains is: ___
3. If I changed ___ to ___, it would fail because: ___

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
```

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
```

---
## TIER 2 — Revision (3 problems)

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

---
## TIER 3 — Revision (2 problems)

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
```

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
## New Problems (2 problems)
New problem count is capped at 2 today because Tier 1 + Tier 2 backlog already fills the 12-slot target.

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
```

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
```

---
## Daily Summary
New: 2 | Tier1: 3 | Tier2: 3 | Tier3: 2 | Tier4: 2 | Total: 12

## Mandatory Closing Check
# Prompt 1 (End of Day agent) run: Yes / No
# STATUS.md updated: Yes / No

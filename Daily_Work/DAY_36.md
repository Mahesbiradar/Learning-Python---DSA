---
# Day 36 — 2026-07-14 — Consolidation Day
Focus: Linked Lists catch-up + Total Appeal O(n) derivation
Phase: New DS — Linked Lists (in progress) + Contribution Counting consolidation
Daily target: 10 problems/recalls

Consolidation trigger: Tier 1 backlog = 5, so new problems = 0 today.

---
## SOP Reminder (2 min before every problem)
Read → Restate → Pattern Check → Brute Force (words) → Optimal Plan (words) → Dry Run → Code → Test → Submit

Full SOP: problem_solving.md. Before code, write `# Pattern: ___ | Variant: ___`.
Complexity fields must be real answers with a one-sentence reason. Never leave `O(?)`.

---
## TIER 4 Recalls (5 min each, no full solve)
Write the pattern template from memory. If you can't in 3 min → flag as Tier 2.
1. Prefix Sum
2. Two Pointers

```
# Pattern 1 recalled correctly (Y/N): ___
# Pattern 2 recalled correctly (Y/N): ___
```

---
## TIER 1 — Priority Revision (solve these first, all of them)

### 1. Total Appeal of A String — Hard
The appeal of a string is the number of distinct characters inside that string. Given a lowercase string `s`, return the sum of the appeal values of every non-empty substring of `s`.

Before coding, do a standalone derivation:
- For each index `i`, decide how many substrings use `s[i]` as the newest contribution for that character.
- Track the previous position of each character.
- Write why the contribution is based on the gap since the previous occurrence and the number of possible right endpoints.
- Only then code the O(n) version.

Example 1: `s = "abbca"` → Output: `28`
Example 2: `s = "code"` → Output: `20`

Constraints: `1 <= s.length <= 10^5`, `s` contains only lowercase English letters.

```
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

### 2. Reverse Linked List II — Medium
Given the head of a singly linked list and two integers `left` and `right`, reverse the nodes from position `left` to position `right` using 1-indexing. Return the head of the modified list.

Example 1: `head = [1,2,3,4,5], left = 2, right = 4` → Output: `[1,4,3,2,5]`
Example 2: `head = [5], left = 1, right = 1` → Output: `[5]`

Constraints: number of nodes `n`, `1 <= n <= 500`, `-500 <= Node.val <= 500`, `1 <= left <= right <= n`.

```
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

### 3. Merge Two Sorted Lists — Easy
You are given the heads of two sorted linked lists, `list1` and `list2`. Merge their nodes into one sorted linked list and return the head of the merged list.

Example 1: `list1 = [1,2,4], list2 = [1,3,4]` → Output: `[1,1,2,3,4,4]`
Example 2: `list1 = [], list2 = []` → Output: `[]`
Example 3: `list1 = [], list2 = [0]` → Output: `[0]`

Constraints: both lists contain `0` to `50` nodes, `-100 <= Node.val <= 100`, and both input lists are sorted in non-decreasing order.

```
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

### 4. Remove Nth Node From End of List — Medium
Given the head of a linked list and an integer `n`, remove the `n`th node from the end of the list and return the updated head.

Example 1: `head = [1,2,3,4,5], n = 2` → Output: `[1,2,3,5]`
Example 2: `head = [1], n = 1` → Output: `[]`
Example 3: `head = [1,2], n = 1` → Output: `[1]`

Constraints: list size `sz`, `1 <= sz <= 30`, `0 <= Node.val <= 100`, `1 <= n <= sz`.

```
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

### 5. Maximum Twin Sum of a Linked List — Medium
In a linked list with even length `n`, node `i` is paired with node `n - 1 - i`. The twin sum is the sum of the values in a paired set of nodes. Return the maximum twin sum in the linked list.

Example 1: `head = [5,4,2,1]` → Output: `6`
Example 2: `head = [4,2,2,3]` → Output: `7`
Example 3: `head = [1,100000]` → Output: `100001`

Constraints: number of nodes `n`, `2 <= n <= 10^5`, `n` is even, `1 <= Node.val <= 10^5`.

```
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
## TIER 2 — Revision (1 problem due)

### 1. Koko Eating Bananas — Medium
You are given `piles`, where `piles[i]` is the number of bananas in the `i`th pile, and an integer `h`. Koko chooses an integer speed `k`. Each hour, she chooses one pile and eats up to `k` bananas from it. Return the minimum `k` that allows her to finish all piles within `h` hours.

Example 1: `piles = [3,6,7,11], h = 8` → Output: `4`
Example 2: `piles = [30,11,23,4,20], h = 5` → Output: `30`
Example 3: `piles = [30,11,23,4,20], h = 6` → Output: `23`

Constraints: `1 <= piles.length <= 10^4`, `piles.length <= h <= 10^9`, `1 <= piles[i] <= 10^9`.

```
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

### 1. Longest Consecutive Sequence — Medium
Given an unsorted integer array `nums`, return the length of the longest run of consecutive integer values. The algorithm should run in O(n) time.

Example 1: `nums = [100,4,200,1,3,2]` → Output: `4`
Example 2: `nums = [0,3,7,2,5,8,4,6,0,1]` → Output: `9`
Example 3: `nums = []` → Output: `0`

Constraints: `0 <= nums.length <= 10^5`, `-10^9 <= nums[i] <= 10^9`.

```
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

### 2. Maximum Number of Vowels in a Substring of Given Length — Medium
Given a string `s` and an integer `k`, return the maximum number of vowel characters in any substring of length `k`. The vowel characters are `a`, `e`, `i`, `o`, and `u`.

Example 1: `s = "abciiidef", k = 3` → Output: `3`
Example 2: `s = "aeiou", k = 2` → Output: `2`
Example 3: `s = "leetcode", k = 3` → Output: `2`

Constraints: `1 <= s.length <= 10^5`, `s` contains lowercase English letters, `1 <= k <= s.length`.

```
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
Skipped today because Tier 1 backlog is 5. Do not introduce a new linked-list variant until the current Tier 1 linked-list problems are solved cold.

---
## Daily Summary
New: 0 | Tier1: 5 | Tier2: 1 | Tier3: 2 | Tier4: 2 | Total: 10

## Mandatory Closing Check
# Prompt 1 (End of Day agent) run: Yes / No
# STATUS.md updated: Yes / No

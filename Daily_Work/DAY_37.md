---
# Day 37 — 2026-07-15 — Learning Day
Focus: Linked Lists catch-up — Dummy node (Remove Nth) + Twin Sum (reverse second half) + add 2 new linked-list variants
Phase: New DS — Linked Lists (in progress)
Daily target: 12 problems (new + revision combined)
---

## SOP Reminder (2 min before every problem)
Read fully → Restate in one line → Identify pattern → Plan in words → Dry run → Code → Test

---

## TIER 4 Recalls (5 min each, no full solve)
Write the [pattern] template from memory. If you can't in 3 min → flag as Tier 2.
1. Prefix Sum
2. Two Pointers (maximize/minimize between ends)

---

## TIER 1 — Priority Revision (solve these first, all of them)

### 1. Total Appeal of A String — Hard
The appeal of a string is the number of distinct characters inside that string. Given a lowercase string `s`, return the sum of the appeal values of every non-empty substring of `s`.

Example 1: `s = "abbca"` → Output: `28`  
Example 2: `s = "code"` → Output: `20`

Constraints:
- `1 <= s.length <= 10^5`
- `s` contains only lowercase English letters.

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

### 2. Remove Nth Node From End of List — Medium
Given the head of a linked list and an integer `n`, remove the `n`th node from the end of the list and return the updated head.

Example 1:  
Input: `head = [1,2,3,4,5], n = 2` → Output: `[1,2,3,5]`

Example 2:  
Input: `head = [1], n = 1` → Output: `[]`

Example 3:  
Input: `head = [1,2], n = 1` → Output: `[1]`

Constraints:
- The number of nodes in the list is `sz`
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

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

### 3. Maximum Twin Sum of a Linked List — Medium
In a linked list with even length `n`, node `i` is paired with node `n - 1 - i`. The twin sum is the sum of the values in a paired set of nodes. Return the maximum twin sum in the linked list.

Example 1:  
Input: `head = [5,4,2,1]` → Output: `6`

Example 2:  
Input: `head = [4,2,2,3]` → Output: `7`

Example 3:  
Input: `head = [1,100000]` → Output: `100001`

Constraints:
- `2 <= n <= 10^5`
- `n` is even
- `1 <= Node.val <= 10^5`

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

### 1. Koko Eating Bananas — Medium
You are given `piles`, where `piles[i]` is the number of bananas in the `i`th pile, and an integer `h`. Koko chooses an integer speed `k`. Each hour, she chooses one pile and eats up to `k` bananas from it. Return the minimum integer `k` such that she can finish all the bananas within `h` hours.

Example 1:
- Input: `piles = [3,6,7,11], h = 8`
- Output: `4`

Example 2:
- Input: `piles = [30,11,23,4,20], h = 5`
- Output: `30`

Example 3:
- Input: `piles = [30,11,23,4,20], h = 6`
- Output: `23`

Constraints:
- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

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

### 2. Reverse Linked List II — Medium
Given the head of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right` (1-indexed). Return the reversed list.

Example 1:
- Input: `head = [1,2,3,4,5], left = 2, right = 4`
- Output: `[1,4,3,2,5]`

Example 2:
- Input: `head = [5], left = 1, right = 1`
- Output: `[5]`

Constraints:
- `n` is number of nodes.
- `1 <= n <= 500`
- `-500 <= Node.val <= 500`
- `1 <= left <= right <= n`

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

### 3. Merge Two Sorted Lists — Easy
You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted list and return the head of the merged list.

Example 1:
- Input: `list1 = [1,2,4], list2 = [1,3,4]`
- Output: `[1,1,2,3,4,4]`

Example 2:
- Input: `list1 = [], list2 = []`
- Output: `[]`

Example 3:
- Input: `list1 = [], list2 = [0]`
- Output: `[0]`

Constraints:
- `0 <= number of nodes <= 50` for each list
- `-100 <= Node.val <= 100`
- Both lists are sorted in non-decreasing order.

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

### 1. Longest Consecutive Sequence — Medium
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

A consecutive sequence is a sequence of elements such that each element's value is exactly `1` greater than the previous element.

Example 1:
- Input: `nums = [100,4,200,1,3,2]`
- Output: `4`  
(Explanation: The longest consecutive sequence is `[1,2,3,4]`.)

Example 2:
- Input: `nums = [0,3,7,2,5,8,4,6,0,1]`
- Output: `9`

Example 3:
- Input: `nums = []`
- Output: `0`

Constraints:
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

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

### 2. Maximum Number of Vowels in a Substring of Given Length — Medium
Given a string `s` and an integer `k`, return the maximum number of vowel letters in any substring of `s` with length `k`.

The vowel letters are: `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

Example 1:
- Input: `s = "abciiidef", k = 3`
- Output: `3`

Example 2:
- Input: `s = "aeiou", k = 2`
- Output: `2`

Example 3:
- Input: `s = "leetcode", k = 3`
- Output: `2`

Constraints:
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters
- `1 <= k <= s.length`

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
(Linked Lists variants — choose new concept variants after doing TIER 1)

### 1. Reverse Linked List — Medium
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
- Input: `head = [1,2,3,4,5]`
- Output: `[5,4,3,2,1]`

Example 2:
- Input: `head = [null]`
- Output: `[]`

Example 3:
- Input: `head = [1]`
- Output: `[1]`

Constraints:
- `0 <= The number of nodes in the list <= 5000`
- `-5000 <= Node.val <= 5000`

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

### 2. Linked List Cycle — Medium
Given head, the head of a linked list, determine if the linked list has a cycle.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.

Return `true` if there is a cycle, otherwise return `false`.

Example 1:
- Input: head = [3,2,0,-4], pos = 1
- Output: true

Example 2:
- Input: head = [1,2], pos = 0
- Output: true

Example 3:
- Input: head = [1], pos = -1
- Output: false

Constraints:
- The number of the nodes in the list is in the range `[0, 10^4]`
- `-10^4 <= Node.val <= 10^4`
- `pos` is `-1` or a valid index in the linked list.

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
New: 2 problems | Tier 1 revision: 3 | Tier 2: 3 | Tier 3: 2 | Tier 4 recalls: 2 | Total: 12

# Day 34 — 2026-07-07 — Learning Day
Focus: Linked Lists — Traversal + Basic Ops (Reverse a list) | Revision: Binary Search Applied (33, 153, 875), Prefix Sum Modulo, Prefix+Hash Map
Phase: New DS — Linked Lists (Jul 7 – Jul 21), started today
Daily target: 12 problems (3 Tier1 + 2 Tier2 + 2 Tier3 + 2 Tier4 recalls + 3 new)

---
## SOP Reminder (2 min before every problem)
Read fully → Restate in one line → Identify pattern → Plan in words → Dry run → Code → Test

Full SOP: problem_solving.md. Do not skip Step 3 (write `# Pattern: ... | Variant: ...` before coding).
RULE: complexity fields must be real answers with justification, never `O(?)`. Wrong complexity = automatic Tier 1.

---
## NEW PATTERN CONCEPT BLOCK — Linked Lists: Reversal (Traversal + Basic Ops)

**Where to learn:** Neetcode.io → search "Reverse Linked List" → watch the concept part only (15 min). Do not watch the coded solution before attempting LC 206 yourself.

**Trigger words:** reverse a list, next/prev pointer, in-place reversal, singly linked list, reverse between positions, reverse in groups

**Mental model:** Walk the list once. At each node, flip its `next` pointer to point backward instead of forward, carrying three references (prev, curr, next) forward as you go.

**Why it exists:** Copying nodes into an array, reversing the array, and rebuilding the list costs O(n) extra space. Flipping pointers in place processes each node exactly once with O(1) extra space.

**Template (fill in from memory after watching — do not copy from a solution):**
```python
def reverseList(head):
    prev = None
    curr = head
    while curr:
        # ___ (save curr.next before you overwrite it)
        # ___ (flip curr.next to point at prev)
        # ___ (advance prev to curr)
        # ___ (advance curr to the saved next)
    return prev
```

**Dry run — head = 1 -> 2 -> 3 -> None:**
```
prev=None, curr=1
step1: nxt=2, curr.next=None (curr.next=prev), prev=1, curr=2
step2: nxt=3, curr.next=1,    prev=2, curr=3
step3: nxt=None, curr.next=2, prev=3, curr=None
loop ends (curr is None) → return prev = 3 -> 2 -> 1 -> None
```

**Common mistakes:** No block exists yet in PATTERNS.md for Linked Lists — this is the first exposure. After solving today's 3 problems, write the derived template + your own common-mistakes list into PATTERNS.md so Day 35's reinforcement warm-up has a reference block to recall against.

---
## TIER 4 Recalls (5 min each, no full solve)
Write the template from memory. If you can't in 3 min → flag as Tier 2. (Both skipped Jul 6 — repeating today.)
1. Frequency Hashing
2. Sliding Window (Fixed size)

```
# Pattern 1 recalled correctly (Y/N): ___
# Pattern 2 recalled correctly (Y/N): ___
```

---
## TIER 1 — Priority Revision (solve all 3, no hints — this is a 2nd attempt on all three same-day)

### 1. Search in Rotated Sorted Array — Medium
There is an integer array `nums` sorted in ascending order (distinct values), rotated at an unknown pivot. Given the rotated array and an integer `target`, return the index of `target` if found, or `-1`. Must run in O(log n).

Example 1: `nums = [4,5,6,7,0,1,2], target = 0` → Output: `4`
Example 2: `nums = [4,5,6,7,0,1,2], target = 3` → Output: `-1`
Example 3: `nums = [1], target = 0` → Output: `-1`

Constraints: `1 <= nums.length <= 5000`, `-10^4 <= nums[i] <= 10^4`, all values unique, array is rotated at some pivot, `-10^4 <= target <= 10^4`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```

### 2. Find Minimum in Rotated Sorted Array — Medium
Suppose an array of length `n` sorted in ascending order is rotated between 1 and `n` times. Given the rotated sorted array `nums` of unique elements, return the minimum element. Must run in O(log n).

Example 1: `nums = [3,4,5,1,2]` → Output: `1`
Example 2: `nums = [4,5,6,7,0,1,2]` → Output: `0`
Example 3: `nums = [11,13,15,17]` → Output: `11`

Constraints: `n == nums.length`, `1 <= n <= 5000`, `-5000 <= nums[i] <= 5000`, all unique, rotated between 1 and n times.

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```

### 3. Koko Eating Bananas — Medium
There are `n` piles of bananas, `piles[i]` bananas in the `i`th pile. Koko eats at a speed of `k` bananas per hour: each hour she picks one pile and eats `k` bananas from it (or all of it if fewer than `k` remain), and does not eat from another pile that hour. Koko wants to finish all bananas within `h` hours. Return the minimum integer `k` such that she can finish within `h` hours.

Example 1: `piles = [3,6,7,11], h = 8` → Output: `4`
Example 2: `piles = [30,11,23,4,20], h = 5` → Output: `30`
Example 3: `piles = [30,11,23,4,20], h = 6` → Output: `23`

Constraints: `1 <= piles.length <= 10^4`, `piles.length <= h <= 10^9`, `1 <= piles[i] <= 10^9`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```

---
## TIER 2 — Revision (2 problems — only 2 due, both taken)

### 1. Total Appeal of A String — Hard
The appeal of a string is the number of distinct characters found in the string. Given a string `s`, return the total appeal of all of its substrings.
Note: last 2 attempts were brute force O(n²) only — this attempt, try to derive the O(n) contribution-per-character approach before coding.

Example 1: `s = "abbca"` → Output: `28`
Example 2: `s = "code"` → Output: `20`

Constraints: `1 <= s.length <= 10^5`, lowercase English letters.

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```

### 2. Make Sum Divisible by P — Hard
Given an array of positive integers `nums`, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by `p`. It is not allowed to remove the whole array. Return the length of the smallest subarray you need to remove, or `-1` if it's impossible.
Note: this is the USO close-out attempt — solve cold, no notes, to confirm the standalone session from Jul 5 stuck.

Example 1: `nums = [3,1,4,2], p = 6` → Output: `1`
Example 2: `nums = [6,3,5,2], p = 9` → Output: `2`
Example 3: `nums = [1,2,3], p = 3` → Output: `0`

Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^9`, `1 <= p <= 10^9`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```

---
## TIER 3 — Revision (2 problems, both overdue since Jul 5 — priority pick)

### 1. Subarray Sum Equals K — Medium
Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals `k`.

Example 1: `nums = [1,1,1], k = 2` → Output: `2`
Example 2: `nums = [1,2,3], k = 3` → Output: `2`

Constraints: `1 <= nums.length <= 2*10^4`, `-1000 <= nums[i] <= 1000`, `-10^7 <= k <= 10^7`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```

### 2. Binary Subarrays With Sum — Medium
Given a binary array `nums` and an integer `goal`, return the number of non-empty subarrays with a sum equal to `goal`.

Example 1: `nums = [1,0,1,0,1], goal = 2` → Output: `4`
Example 2: `nums = [0,0,0,0,0], goal = 0` → Output: `15`

Constraints: `1 <= nums.length <= 3*10^4`, `nums[i]` is `0` or `1`, `0 <= goal <= nums.length`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```

---
## New Problems (3 problems) — identify the pattern yourself, do not skip Step 3 of the SOP

### 1. Reverse a Singly Linked List — Easy
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1: `head = [1,2,3,4,5]` → Output: `[5,4,3,2,1]`
Example 2: `head = [1,2]` → Output: `[2,1]`
Example 3: `head = []` → Output: `[]`

Constraints: number of nodes is `0` to `5000`, `-5000 <= Node.val <= 5000`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```

### 2. Reverse a Linked List Between Two Positions — Medium
Given the head of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right` (1-indexed), and return the reversed list.

Example 1: `head = [1,2,3,4,5], left = 2, right = 4` → Output: `[1,4,3,2,5]`
Example 2: `head = [5], left = 1, right = 1` → Output: `[5]`

Constraints: number of nodes `n`, `1 <= n <= 500`, `-500 <= Node.val <= 500`, `1 <= left <= right <= n`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```

### 3. Maximum Twin Sum of a Linked List — Medium
In a linked list of size `n` where `n` is even, the `i`th node (0-indexed) is the twin of the `(n-1-i)`th node, for `0 <= i <= (n/2)-1`. The twin sum is the sum of a node and its twin. Given the head of a linked list of even length, return the maximum twin sum.

Example 1: `head = [5,4,2,1]` → Output: `6`
Example 2: `head = [4,2,2,3]` → Output: `7`
Example 3: `head = [1,100000]` → Output: `100001`

Constraints: number of nodes `n`, `2 <= n <= 10^5`, `n` is even, `1 <= Node.val <= 10^5`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```

---
## Daily Summary
New: 3 | Tier1: 3 | Tier2: 2 | Tier3: 2 | Tier4: 2 | Total: 12

## Mandatory Closing Check
# Prompt 1 (End of Day agent) run: Yes
# STATUS.md updated: Yes

---
# Day 32 — 2026-07-05 (Sunday) — Recovery Day
Focus: Prefix Sum + Modulo (Standalone Derivation Session) + Backlog clearance for missed Jul 3 & Jul 4
Phase: Gap Fill — Prefix Sum Modulo standalone session (USO, flagged Day 26) | Binary Search Lower-bound close-out pushed to next study day
Daily target: 11 full solves + 2 template recalls (compressed catch-up — no new problems today)

**Why this shape:** No session ran Jul 3 or Jul 4. Per the Regression/USO rules in STATUS.md, "Make Sum Divisible by P" (LC 1590) is flagged UNRESOLVED-SINCE-ORIGIN for Prefix Sum + Modulo and must NOT be folded into a normal timed Tier 1 slot again — it needs its own 60–90 min derivation-first session. Today (day off) is the first day with enough time to run that properly, so it gets its own block below instead of sitting in the Tier 1 list. Everything else today is backlog revision only — this is a Recovery Day, so no new patterns or new problems are introduced.

---
## SOP Reminder (2 min before every problem)
Read fully → Restate in one line → Identify pattern → Plan in words → Dry run → Code → Test

---
## STANDALONE SESSION — Prefix Sum + Modulo (60–90 min, not timeboxed to 25/40 min)

This overrides the normal Tier 1 clock for LC 1590 only. Follow all 4 steps in order — do not skip to code.

**Step 1 — Write the derivation by hand, from memory, before opening PATTERNS.md:**
```
If prefix[j] % k = prefix[i] % k
Then (prefix[j] - prefix[i]) % k = ...
And  prefix[j] - prefix[i] = ...
Therefore ...
```
Then check it against the DERIVATION block in PATTERNS.md → PATTERN: Prefix Sum + Modulo. Log result (Y/N).

**Step 2 — Write the LC 1590 extension by hand, from memory, before coding:**
```
total_sum % p = target        (what does this represent?)
We need: subarray_sum % p = target
prefix[j] - prefix[i] = subarray_sum
→ prefix[i] % p = needed = ...
```
Check against PATTERNS.md extension block. Log result (Y/N).

**Step 3 — Solve these 3 problems back-to-back, in this order, cold (no peeking at old solutions):**

### A. Continuous Subarray Sum (LC 523) — Medium [revision — already Tier 3, solve cold as reinforcement]

Given an integer array `nums` and an integer `k`, return `true` if `nums` has a continuous subarray
of size **at least two** whose elements sum up to a multiple of `k`, or `false` otherwise.

An integer `x` is a multiple of `k` if there exists an integer `n` such that `x = n * k`. `0` is
always a multiple of `k`.

**Example 1:**
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2,4] is a continuous subarray of size 2 whose elements sum up to 6.

**Example 2:**
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23,2,6,4,7] is a continuous subarray of size 5 whose elements sum up to 42, and 42 is
a multiple of 6.

**Example 3:**
Input: nums = [23,2,6,4,7], k = 13
Output: false

**Constraints:**
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
- 0 <= sum(nums[i]) <= 2^31 - 1
- 1 <= k <= 2^31 - 1

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

### B. Subarray Sums Divisible by K (LC 974) — Medium [revision — already Tier 3, solve cold as reinforcement]

Given an integer array `nums` and an integer `k`, return the number of non-empty **subarrays**
that have a sum divisible by `k`.

A subarray is a contiguous part of an array.

**Example 1:**
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4,5,0,-2,-3,1], [5], [5,0], [5,0,-2,-3], [0], [0,-2,-3], [-2,-3]

**Example 2:**
Input: nums = [5], k = 9
Output: 0

**Constraints:**
- 1 <= nums.length <= 3 * 10^4
- -10^4 <= nums[i] <= 10^4
- 2 <= k <= 10^4

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

### C. Make Sum Divisible by P (LC 1590) — Medium ⚠️ USO STANDALONE TARGET — up to 90 min

Given an array of positive integers `nums`, remove the **smallest** subarray (possibly empty) such
that the **sum** of the remaining elements is divisible by `p`. It is **not** allowed to remove
the whole array. Return the length of the smallest subarray to remove, or **-1** if impossible.

A **subarray** is a contiguous block of elements in the array.

**Example 1:**
Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: Sum is 10. Remove [4] → remaining sum = 6, divisible by 6.

**Example 2:**
Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: Remove [5,2] → remaining sum = 9, divisible by 9.

**Example 3:**
Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Sum = 6 is already divisible by 3. Remove nothing (return 0).

**Constraints:**
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= p <= 10^9

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

**Step 4 — Only mark the USO row "Standalone Session Done: Yes" if tomorrow (next study day) you can
solve LC 1590 cold, independently, with no hint. One session is never enough by itself — this is
evidence-gathering, not resolution.**

---

## TIER 4 Recalls (5 min each, no full solve)
Write the template from memory. If you can't in 3 min → write "FAILED" and flag as Tier 2 for tomorrow.
Complete all 3 steps: (1) template from memory, (2) the invariant it maintains, (3) what breaks if you change one specific line.

1. Frequency Hashing
2. Two Pointers (Opposite ends — palindrome/reverse)

---

## TIER 1 — Priority Revision (solve first, all of them)

### 1. Longest Consecutive Sequence (LC 128) — Medium ⚠️ Hint D31 — solve cold today, no video/notes

Given an unsorted array of integers `nums`, return the length of the **longest consecutive
elements sequence**.

You must write an algorithm that runs in **O(n)** time.

**Example 1:**
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4]. Its length is 4.

**Example 2:**
Input: nums = [0,3,7,2,5,8,1,9,6,4]
Output: 10

**Example 3:**
Input: nums = []
Output: 0

**Constraints:**
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

## TIER 2 — Revision (3 problems — all Tier 2 pool items, all overdue)

### 2. Arranging Coins (LC 441) — Easy [OVERDUE since Jun 27]

You have `n` coins and you want to build a staircase with these coins. The staircase consists of
`k` rows where the `i`th row has exactly `i` coins. The last row of the staircase may be
incomplete.

Given the integer `n`, return the number of **complete rows** of the staircase you will build.

**Example 1:**
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

**Example 2:**
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.

**Constraints:**
- 1 <= n <= 2^31 - 1

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

### 3. Remove Element (LC 27) — Easy [OVERDUE since Jun 28]

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums`
**in-place**. The order of the elements may be changed. Then return the number of elements in
`nums` which are not equal to `val`.

**Example 1:**
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

**Example 2:**
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]

**Constraints:**
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

### 4. Total Appeal of A String (LC 2262) — Hard [OVERDUE since Jul 2 — optimal not yet submitted]

The **appeal** of a string is the number of **distinct** characters found in the string.
Given a string `s`, return the **total appeal** of all of its **substrings**.
A substring is a contiguous sequence of characters within a string.

**Example 1:**
Input: s = "abbca"
Output: 28
Explanation: The following are the substrings of "abbca":
- Substrings of length 1: "a", "b", "b", "c", "a" have an appeal of 1, 1, 1, 1, and 1 respectively.
- Substrings of length 2: "ab", "bb", "bc", "ca" have an appeal of 2, 1, 2, and 2 respectively.
- Substrings of length 3: "abb", "bbc", "bca" have an appeal of 2, 2, and 3 respectively.
- Substrings of length 4: "abbc", "bbca" have an appeal of 3 and 3 respectively.
- Substrings of length 5: "abbca" has an appeal of 3.
The total appeal is 1+1+1+1+1 + 2+1+2+2 + 2+2+3 + 3+3 + 3 = 28.

**Example 2:**
Input: s = "code"
Output: 20

**Constraints:**
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.

```python
# Your solution here (attempt the optimal this time — last-index-of-char + contribution counting)
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

## TIER 3 — Revision (4 problems — doubled today to cover the 2-day gap)

### 5. Two Sum II — Input Array Is Sorted (LC 167) — Medium [Due Jul 4]

Given a **1-indexed** array of integers `numbers` that is already sorted in **non-decreasing
order**, find two numbers such that they add up to a specific `target` number. Return the indices
of the two numbers, `index1` and `index2`, **added by one**, as an integer array
`[index1, index2]` of length 2.

**Example 1:**
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

**Example 2:**
Input: numbers = [2,3,4], target = 6
Output: [1,3]

**Example 3:**
Input: numbers = [-1,0], target = -1
Output: [1,2]

**Constraints:**
- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order
- -1000 <= target <= 1000
- Exactly one solution exists.

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

### 6. Unique Number of Occurrences (LC 1207) — Easy [Due Jul 4]

Given an array of integers `arr`, return `true` if the number of occurrences of each value in the
array is **unique**, or `false` otherwise.

**Example 1:**
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: 1 occurs 3 times, 2 occurs 2 times, 3 occurs 1 time. No two values have the same
number of occurrences.

**Example 2:**
Input: arr = [1,2]
Output: false

**Example 3:**
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

**Constraints:**
- 1 <= arr.length <= 1000
- -1000 <= arr[i] <= 1000

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

### 7. Isomorphic Strings (LC 205) — Easy [Due Jul 5 — regression risk, appeared in Regression Log twice before]

Given two strings `s` and `t`, determine if they are **isomorphic**.
Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.
All occurrences of a character must be replaced with another character while preserving the order
of characters. No two characters may map to the same character, but a character may map to itself.

**Example 1:**
Input: s = "egg", t = "add"
Output: true

**Example 2:**
Input: s = "foo", t = "bar"
Output: false

**Example 3:**
Input: s = "paper", t = "title"
Output: true

**Constraints:**
- 1 <= s.length <= 5 * 10^4
- t.length == s.length
- s and t consist of any valid ASCII character.

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

### 8. Container With Most Water (LC 11) — Medium [Due Jul 5]

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such
that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains
the most water. Return the maximum amount of water a container can store.

Notice that you may not slant the container.

**Example 1:**
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

**Example 2:**
Input: height = [1,1]
Output: 1

**Constraints:**
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

## New Problems (0 — Recovery Day, revision only)

No new problems today. This is a compressed catch-up session for the missed Jul 3 and Jul 4
sessions plus the Prefix Sum + Modulo standalone derivation. Binary Search Applied and Binary
Search Lower-bound close-out (queued for Jun 30 – Jul 5 in the Learning Phase Tracker) resume on
the next normal study day.

---

## Mandatory Closing Check

  # Prompt 1 (End of Day agent) run: Yes / No
  # STATUS.md updated: Yes / No

---

## Daily Summary
Standalone session: 3 (523, 974, 1590) | Tier1: 1 | Tier2: 3 | Tier3: 4 | Tier4 recalls: 2 | New: 0 | Total full solves: 11

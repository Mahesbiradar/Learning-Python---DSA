---
# Day 31 — 2026-07-02 — Reinforcement Day (Prefix Sum Modulo Standalone + Phase 1 Gap-Fill)
Focus: Prefix Sum + Modulo (USO standalone session on LC 1590) | New: Longest Consecutive Sequence (LC 128)
Phase: Gap-Fill — Phase 1 close-out
Daily target: 11 problems

---
## SOP Reminder (2 min before every problem)
Read fully → Restate in one line → Write `# Pattern: [name] | Variant: [name]` BEFORE any code → Plan brute force (words only) → Plan optimal (words only) → Dry run → Code → Test → Submit

Complexity rule: Never write O(?). Always write the real answer with a one-sentence justification.
Example: "O(n) — one pass through array" or "O(log n) — search space halves each iteration."

---
## ⚠️ PRE-SESSION: Prefix Sum + Modulo Derivation (5 min — do this before Tier 1)

UNRESOLVED-SINCE-ORIGIN flag is active for Prefix Sum + Modulo.
Before attempting LC 1590, write the 4-line algebraic proof from memory below.
Do NOT open PATTERNS.md until you have tried. After writing, verify against PATTERNS.md.

```
[ Write proof here ]
If prefix[j] % k = ...
Then ...
And ...
Therefore ...
```

Only proceed to LC 1590 once you can write this proof correctly without looking.
Time for LC 1590 today is NOT capped at 40 min — give it up to 90 min.

---
## TIER 4 Recalls — Warm-Up Templates (5 min each)
Complete all 3 steps for each template. A recall is only complete when all 3 are answered.
  Step 1: Write the template from memory.
  Step 2: "The invariant this template maintains is: ___"
  Step 3: "If I changed [specific line] to [wrong version], it would fail because: ___"

If you cannot write the template in 3 min → write "FAILED" and flag as Tier 2 for tomorrow.

### Recall 1: Sliding Window (Variable size)

```python
# Write template from memory here
```

Invariant: ___
If I changed ___ to ___, it would fail because: ___

---

### Recall 2: Prefix Sum + Hash Map (560 style)

```python
# Write template from memory here
```

Invariant: ___
If I changed ___ to ___, it would fail because: ___

---
## TIER 1 — Priority Revision (solve ALL 3 first — no skipping)

### 1. Make Sum Divisible by P (LC 
) — Medium ⚠️ USO STANDALONE — Write derivation proof above first

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

**Recovery questions (answer in comments before coding):**
1. What is `target = total % p` telling you?
2. What does `needed = (current - target) % p` find?
3. Why is `seen` initialized as `{0: -1}` and stores index, not count?

```python
# Answer the 3 recovery questions here as comments first:
# 1.
# 2.
# 3.

# Then write your solution:
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) — [one-sentence justification]
# Space complexity: O(?) — [one-sentence justification]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

### 2. Range Sum Query - Immutable (LC 303) — Easy ⚠️ D30 UNVERIFIED — solve fresh, fill ALL fields

Day 30 had code written (brute + optimal both) but comment fields were blank.
Solve independently today from scratch. Do not look at D30 code first.
If you cannot solve it independently, mark Status: Hint.

Given an integer array `nums`, handle multiple queries of the following type:
Calculate the sum of elements of `nums` between indices `left` and `right` **inclusive**.

Implement the `NumArray` class:
- `NumArray(int[] nums)` — Initializes the object with the integer array `nums`.
- `int sumRange(int left, int right)` — Returns the sum of elements between `left` and `right`
  inclusive. Must be **O(1)** per query.

**Example 1:**
Input:
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output: [null, 1, -1, -3]
Explanation:
numArray = NumArray([-2, 0, 3, -5, 2, -1])
numArray.sumRange(0, 2) → (-2) + 0 + 3 = 1
numArray.sumRange(2, 5) → 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5) → (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

**Constraints:**
- 1 <= nums.length <= 10^4
- -10^5 <= nums[i] <= 10^5
- 0 <= left <= right < nums.length
- At most 10^4 calls will be made to sumRange.

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) __init__ | O(?) sumRange — [justify each]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

### 3. K Divisible Elements Subarrays (LC 2261) — Medium ⚠️ Overdue since Jun 30

Given a **0-indexed** integer array `nums` and two positive integers `k` and `p`.

Return the number of **distinct** subarrays of `nums` which have **at most** `k` elements
that are divisible by `p`.

Two arrays are distinct if there exists some index `i` where `a[i] != b[i]`.

**Example 1:**
Input: nums = [2,3,3,2,2], k = 2, p = 2
Output: 6

**Example 2:**
Input: nums = [1,2,3,4], k = 4, p = 1
Output: 10
Explanation: All subarrays qualify (all elements divisible by 1). 4 elements → 10 distinct subarrays total.

**Constraints:**
- 1 <= nums.length <= 200
- 1 <= p, k <= nums.length
- 1 <= nums[i] <= 200

**Recovery note:** D29 — brute force was independent, optimal was hint-based.
Attempt brute force first independently. Then attempt optimal if you recall it.

```python
# Brute force solution (attempt independently first):
```

```python
# Optimal solution (only if recalled from D29 — mark Hint if needed reference):
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) brute | O(?) optimal — [justify]
# Space complexity: O(?) — [justify]
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---
## TIER 2 — Revision (3 problems — most overdue picked)

### 4. Two Sum (LC 1) — Easy [OVERDUE since Jun 27]

Given an array of integers `nums` and an integer `target`, return the **indices** of the two
numbers that add up to `target`. You may assume that exactly one solution exists. You may not
use the same element twice. Return the answer in any order.

**Example 1:**
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

**Example 2:**
Input: nums = [3,2,4], target = 6
Output: [1,2]

**Example 3:**
Input: nums = [3,3], target = 6
Output: [0,1]

**Constraints:**
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

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

### 5. Valid Perfect Square (LC 367) — Easy [OVERDUE since Jun 27]

Given a positive integer `num`, return `true` if `num` is a perfect square, or `false` otherwise.
Do **not** use any built-in library function such as `sqrt`.

**Example 1:**
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16, and 4 is an integer.

**Example 2:**
Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14, and 3.742 is not an integer.

**Constraints:**
- 1 <= num <= 2^31 - 1

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

### 6. Ransom Note (LC 383) — Easy [OVERDUE since Jul 1]

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed
by using the letters from `magazine` and `false` otherwise. Each letter in `magazine` can only
be used **once**.

**Example 1:**
Input: ransomNote = "a", magazine = "b"
Output: false

**Example 2:**
Input: ransomNote = "aa", magazine = "ab"
Output: false

**Example 3:**
Input: ransomNote = "aa", magazine = "aab"
Output: true

**Constraints:**
- 1 <= ransomNote.length, magazine.length <= 10^5
- ransomNote and magazine consist of lowercase English letters.

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
## TIER 3 — Revision (2 problems — due Jul 4, pulling 2 days early)

### 7. First Bad Version (LC 278) — Easy [Due Jul 4]

You are a product manager and currently leading a team to develop a new product. Unfortunately,
the latest version of your product fails the quality check. Since each version is developed based
on the previous version, all the versions after a bad version are also bad.

You are given `n` versions `[1, 2, ..., n]` and a provided API `isBadVersion(version)` which
returns whether version is bad. Find the **first bad version** while minimizing API calls.

**Example 1:**
Input: n = 5, bad = 4
Output: 4
Explanation: isBadVersion(3) → false, isBadVersion(4) → true. First bad version is 4.

**Example 2:**
Input: n = 1, bad = 1
Output: 1

**Constraints:**
- 1 <= bad <= n <= 2^31 - 1

```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

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

### 8. Find Peak Element (LC 162) — Medium [Due Jul 4]

A peak element is an element that is **strictly greater** than its neighbors.

Given a **0-indexed** integer array `nums`, find a peak element and return its index. If the array
contains multiple peaks, return the index of **any** of the peaks.

You may imagine that `nums[-1] = nums[n] = -∞`. An element is always greater than a neighbor
outside the array boundary.

You must write an algorithm that runs in **O(log n)** time.

**Example 1:**
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and the function should return index 2.

**Example 2:**
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Either index 1 (value 2) or index 5 (value 6) is acceptable.

**Constraints:**
- 1 <= nums.length <= 1000
- -2^31 <= nums[i] <= 2^31 - 1
- nums[i] != nums[i + 1] for all valid i.

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
## New Problems (1 problem — Phase 1 must-solve gap-fill)

### 9. Longest Consecutive Sequence (LC 128) — Medium [Phase 1 must-solve — FIRST ATTEMPT]

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
- O(n) time required — sorting-based solutions do not meet the constraint.

```python
# Brute force first (words only — do not code the brute force, just state the approach):
# Brute force: ___
# Why brute force fails: ___

# Optimal solution:
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
## Mandatory Closing Check (do not skip)

# Prompt 1 (End of Day agent) run: Yes / No
# STATUS.md updated: Yes / No

---
## Daily Summary

| Section | Problems | Count |
|---------|----------|-------|
| Tier 4 Recalls | Sliding Window Variable, Prefix Sum + Hash Map | 2 |
| Tier 1 | LC 1590 (USO), LC 303 (unverified), LC 2261 (overdue) | 3 |
| Tier 2 | LC 1 (overdue), LC 367 (overdue), LC 383 (overdue) | 3 |
| Tier 3 | LC 278, LC 162 | 2 |
| New | LC 128 | 1 |
| **Total** | | **11** |

Execution order:
1. Write Prefix Modulo derivation proof cold (5 min — no shortcuts, no PATTERNS.md yet)
2. Tier 4 recalls: Sliding Window Variable → Prefix Sum + Hash Map (3-step protocol each)
3. Tier 1: LC 303 first (quick, clears a fast Tier 1) → LC 1590 (USO, up to 90 min) → LC 2261
4. Tier 2: LC 1 → LC 367 → LC 383
5. Tier 3: LC 278 → LC 162
6. New: LC 128 (cold solve — identify the pattern yourself)
7. Run Prompt 1 before closing the file.

Remaining Tier 2 overdue (defer to Day 32): Arranging Coins (441 — Jun 27), Remove Element (27 — Jun 28), Total Appeal (2262 — Jul 2).

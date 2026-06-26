# Day 27 — June 27, 2026 — Reinforcement Day
Focus: Two Pointers (Maximize variant) + Prefix Sum (Modulo variant) — Day 2 solidification
Phase: Gap Fill — closing Two Pointers maximize before Prefix Sum Modulo reinforcement
Daily target: 12 problems

---

## SOP Reminder (2 min before every problem)
Read fully → Restate in one line → Identify pattern → Brute force in words →
Optimal plan in words → Dry run on paper → Code → Test edge cases → Submit

Time targets: Easy = 15-20 min | Medium = 25-35 min
Exceed the target → Tier 1 regardless of correctness.

---

## TIER 4 Recalls (5 min each — write from memory, no notes)

### Recall 1 — Frequency Hashing
Write the full Frequency Hashing template from memory.
Include: dict setup, count pass, answer pass.

```python
# Write here from memory


```
Time taken: ___ min | Result: Recalled clean / Struggled (→ Tier 2)

---

### Recall 2 — Complement Lookup
Write the Complement Lookup template from memory.
Include: seen dict, check-then-store order, what gets stored as key vs value.

```python
# Write here from memory


```
Time taken: ___ min | Result: Recalled clean / Struggled (→ Tier 2)

---

## PATTERN WARM-UP — Two Pointers: Maximize/Minimize (5 min, before Tier 1)

This was introduced yesterday. Write the template from memory before touching any problems.

```python
def two_pointer_maximize(height):
    # Write from memory


```

Key rules (recite before writing):
- Start: left = 0, right = len - 1
- Value = ________________
- Move the ________ side inward
- Stop when ________________

If you cannot write it in 3 min → re-read yesterday's concept block in DAY_26.md, then continue.

---

## PATTERN WARM-UP — Prefix Sum Modulo (3 min, before LC 974)

Two versions exist — pick the right one:

| Version | Seen init | What it answers |
|---------|-----------|----------------|
| EXISTS (LC 523) | `{0: -1}` | Is there a subarray with sum divisible by k? (True/False) |
| COUNT (LC 974) | `{0: 1}` | How many subarrays have sum divisible by k? (int) |

The sign of `remainder` matters — if negative, add k before using:
`if remainder < 0: remainder += k`

---

## TIER 1 — Priority Revision (solve ALL 3 before anything else)

---

### T1-1. Guess Number Higher or Lower — LC 374
Easy | Binary Search

Solve completely blind — no looking at yesterday's code, no template.

We play a guessing game. I pick a number from 1 to n.
Each call to `guess(num)` returns:
  -1  → your guess is higher than the answer
   1  → your guess is lower than the answer
   0  → you guessed correctly

Find the number I picked.

```
# The guess API is already defined:
# def guess(num: int) -> int:

n=10, pick=6  →  6
n=1,  pick=1  →  1
n=2,  pick=2  →  2
```

Constraints: 1 <= n <= 2^31-1. 1 <= pick <= n.

What to fix from yesterday:
- Loop condition: `left <= right`
- Adjust correctly: if guess(mid)==-1 → high, if ==1 → low, if ==0 → return

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

### T1-2. Peak Index in a Mountain Array — LC 852
Medium | Binary Search

Solve in O(log n) this time. Not O(n). The O(n) version is wrong for this problem.

A mountain array increases to a peak then strictly decreases.
Return the index of the peak element.

```
arr = [0,1,0]      →  1
arr = [0,2,1,0]    →  1
arr = [0,10,5,2]   →  1
arr = [3,4,5,1]    →  2
arr = [24,69,100,99,79,78,67,36,26,19]  →  2
```

Constraints: 3 <= arr.length <= 10^5. 0 <= arr[i] <= 10^6. Guaranteed mountain.

What to fix from yesterday:
- Loop: `while left < right` (NOT `<=`)
- If arr[mid] > arr[mid+1] → peak is AT or LEFT of mid → `right = mid`
- If arr[mid] < arr[mid+1] → peak is RIGHT of mid → `left = mid + 1`
- Return: `return left` (NOT `return mid`)

Write the full O(log n) solution cold. No hints.

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

### T1-3. Subarray Sums Divisible by K — LC 974
Medium | Prefix Sum

Retry completely blind — no looking at yesterday's template. Use the warm-up above.

Given integer array nums and integer k, return the number of non-empty subarrays
that have a sum divisible by k.

```
nums=[4,5,0,-2,-3,1], k=5   →  7
nums=[5], k=9                →  0
nums=[7,3,-5,6,-9], k=3     →  4
```

Constraints: 1 <= nums.length <= 3×10^4. -10^4 <= nums[i] <= 10^4. 2 <= k <= 10^4.

Edge cases to test:
- Negative numbers in array (remainder goes negative → add k)
- Single element divisible by k
- All elements 0

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

## TIER 2 — Revision (3 problems — identify the pattern yourself)

---

### T2-1. LC 26
Easy

Given an integer array nums sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once.
Return the number of unique elements.

The first k elements of nums must contain the unique elements in the original order.
It does not matter what you leave beyond the first k elements.

```
[1,1,2]             →  2  (nums becomes [1,2,_])
[0,0,1,1,1,2,2,3,3,4]  →  5  (nums becomes [0,1,2,3,4,_,_,_,_,_])
```

Constraints: 1 <= nums.length <= 3×10^4. -100 <= nums[i] <= 100. Sorted.

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

### T2-2. LC 278
Easy

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions
after a bad version are also bad.

You have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether version is bad.
Implement a function to find the first bad version. Minimize the number of API calls.

```
# The isBadVersion API is defined:
# def isBadVersion(version: int) -> bool:

n=5, bad=4  →  4  (versions: [good, good, good, bad, bad])
n=1, bad=1  →  1
```

Constraints: 1 <= bad <= n <= 2^31-1.

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

### T2-3. LC 162
Medium

A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index of any of them.

You may imagine that nums[-1] = nums[n] = -∞ (elements outside are minus infinity).
Solve in O(log n) time.

```
nums=[1,2,3,1]   →  2  (nums[2]=3 is a peak)
nums=[1,2,1,3,5,6,4]  →  1 or 5 (both valid peaks)
nums=[1]          →  0
```

Constraints: 1 <= nums.length <= 1000. -2^31 <= nums[i] <= 2^31-1. nums[i] ≠ nums[i+1].

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

## TIER 3 — Revision (2 problems — identify the pattern yourself)

---

### T3-1. LC 167
Medium

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Return the indices of the two numbers [index1, index2] (1-indexed).

The tests are generated such that there is exactly one solution.
You may not use the same element twice.
Use only constant extra space.

```
[2,7,11,15], target=9    →  [1,2]
[2,3,4], target=6        →  [1,3]
[-1,0], target=-1        →  [1,2]
[1,3,4,5,7,11], target=9 →  [3,5]
```

Constraints: 2 <= numbers.length <= 3×10^4. Exactly one solution.

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

### T3-2. LC 1207
Easy

Given an array of integers arr, return true if the number of occurrences of each value
in the array is unique (no two values have the same occurrence count), or false otherwise.

```
[1,2,2,1,1,3]               →  True   (1→3, 2→2, 3→1 — all unique counts)
[1,2]                        →  False  (both appear once)
[-3,0,1,-3,1,1,1,-3,10,0]   →  True
[3,3,3,3,3,3]               →  True   (only one value)
```

Constraints: 1 <= arr.length <= 1000. -1000 <= arr[i] <= 1000.

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

## New Problems (2 problems — identify the pattern yourself)

Both problems are Medium difficulty. Apply full SOP — dry run before coding.

---

### N1. Max Number of K-Sum Pairs — LC 1679
Medium

You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k
and remove them from the array.

Return the maximum number of operations you can perform on the array.

```
nums=[1,2,3,4], k=5          →  2   (remove [1,4] first, then [2,3])
nums=[3,1,3,4,3], k=6        →  1   (remove [3,3])
nums=[1,1,1,1], k=2          →  2
nums=[2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2], k=3  →  5
```

Constraints: 1 <= nums.length <= 10^5. 1 <= nums[i] <= 10^9. 1 <= k <= 10^9.

Brute force hint (words only, don't code): check every pair → O(n²). Too slow for 10^5.
Think: can you sort and then use two ends?

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

### N2. Minimize Maximum Pair Sum in Array — LC 1877
Medium

The pair sum of a pair (a, b) is equal to a + b.
The maximum pair sum is the largest pair sum in a list of pairs.
Given an array nums of even length n, pair up the elements such that:
- Each element belongs to exactly one pair
- The maximum pair sum is minimized

Return the minimized maximum pair sum after optimally pairing up the elements.

```
nums=[3,5,2,3]       →  7    (pairs: [3,3] and [2,5] → max pair sum is max(6,7)=7)
nums=[3,5,4,2,4,6]   →  8    (pairs: [2,6],[3,5],[4,4] → max is 8)
nums=[1,2]           →  3
nums=[1,1,1,1]       →  2
```

Constraints: n is even. 2 <= nums.length <= 10^5. 1 <= nums[i] <= 10^5.

Brute force hint (words only): try every possible pairing → exponential. Too slow.
Think: what if you sorted the array? What would the optimal pairing look like?

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

## Priority Order for Today

1. Tier 4 recalls first (10 min total)
2. Pattern warm-up: Two Pointers maximize template from memory (3 min)
3. Pattern warm-up: Prefix Sum Modulo version table (2 min)
4. Tier 1 in order: LC 374 → LC 852 → LC 974 (hardest first)
5. Tier 2: LC 26 → LC 278 → LC 162
6. Tier 3: LC 167 → LC 1207
7. New problems last: LC 1679 → LC 1877

If you run out of time after Tier 1 + Tier 2: skip new problems, do Tier 3. Never skip Tier 1.

---

## Daily Summary

| Slot | Problems | Count |
|------|----------|-------|
| Tier 4 Recalls | Frequency Hashing, Complement Lookup | 2 |
| Tier 1 | LC 374, LC 852, LC 974 | 3 |
| Tier 2 | LC 26, LC 278, LC 162 | 3 |
| Tier 3 | LC 167, LC 1207 | 2 |
| New | LC 1679, LC 1877 | 2 |
| **Total** | | **12** |

---

## What Success Looks Like Today

- LC 374: solved clean, independent, no hints → Tier 2 or 3
- LC 852: O(log n) correct, `return left`, no hint → Tier 2 (first clean O(log n) solve)
- LC 974: written from scratch, no template visible, handles negative numbers → Tier 2
- LC 1679 and LC 1877: recognize the pattern from trigger words and dry run independently

If 374 + 852 + 974 are all independent today → Binary Search and Prefix Modulo are building.
If any of these needs a hint again → they stay Tier 1 and appear again tomorrow. That is fine.

---

## End of Day

Run PROMPT 1 to evaluate, assign tiers, and update STATUS.md.

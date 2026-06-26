# Day 28 — June 28, 2026 — Reinforcement Day
Focus: Prefix Sum (Modulo variant) — Day 3 | Prefix+HashMap — close shaky gap
Phase: Gap Fill — Prefix Sum Modulo (target end Jun 30) + overdue Binary Search Lower bound cleanup
Daily target: 10 problems

---

## SOP Reminder (2 min before every problem)
Read fully → Restate in one line → Identify pattern → Brute force in words →
Optimal plan in words → Dry run on paper → Code → Test edge cases → Submit

Time targets: Easy = 15-20 min | Medium = 25-35 min
Exceed the target → Tier 1 regardless of correctness.

---

## TIER 4 Recalls (5 min each — write from memory, no notes)

### Recall 1 — Running State (Kadane / min-max tracking)
Write the Best Time to Buy and Sell Stock template from memory.
Include: initial state, loop body, update order (check BEFORE updating min).

```python
# Write here from memory


```
Time taken: ___ min | Result: Recalled clean / Struggled (→ Tier 2)

---

### Recall 2 — Prefix Sum (Pivot / equilibrium)
Write the Find Pivot Index template from memory.
Include: total sum, left_sum, update-after-compare rule.

```python
# Write here from memory


```
Time taken: ___ min | Result: Recalled clean / Struggled (→ Tier 2)

---

## PATTERN WARM-UP — Prefix Sum Modulo (3 min before LC 974)

Fill this from memory before touching any problem. No notes.

**Two versions — which do you use when?**

| Version | `seen` init | Loop body: `seen` update | Use when |
|---------|------------|--------------------------|----------|
| EXISTS (LC 523) | `{0: ___}` | Only if NOT in seen | True/False |
| COUNT (LC 974, 560) | `{0: ___}` | Always add/increment | Count |

**The key mistake from D27:** you wrote `seen[prefix]` instead of `seen[remainder]`.
The KEY is always the **remainder**, not the prefix. Prefix changes every step. Remainder is what you store and look up.

**Fix LC 523 WA:** Your approach was correct. Check these 3 exact lines:
```python
seen = {0: -1}            # ← -1 (index before array starts)
if remainder in seen:
    if i - seen[remainder] >= 2:   # ← gap of at least 2 (length ≥ 2)
        return True
else:
    seen[remainder] = i            # ← ONLY update if NOT already in seen (keep earliest)
```
The WA is likely from updating `seen[remainder]` every time (overwriting earliest index).
Verify: if `remainder in seen`, do NOT update — keep the earliest occurrence.

---

## TIER 1 — Priority Revision (solve before anything else)

---

### T1-1. Subarray Sums Divisible by K — LC 974
Medium | Prefix Sum

Third attempt. Solve completely from scratch — no notes, no warm-up visible.
Close this out today.

Given integer array nums and integer k, return the number of non-empty subarrays
that have a sum divisible by k.

```
nums=[4,5,0,-2,-3,1], k=5   →  7
nums=[5], k=9                →  0
nums=[7,3,-5,6,-9], k=3     →  4
nums=[0,0,0,0,0], k=3       →  15
```

Constraints: 1 <= nums.length <= 3×10^4. -10^4 <= nums[i] <= 10^4. 2 <= k <= 10^4.

Before coding — say aloud:
1. I use `seen = {0: 1}` because I'm COUNTING
2. I store and look up `remainder = prefix % k`
3. Negative remainder → add k
4. I always update `seen[remainder]` after checking

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

### T2-1. LC 523
Medium

Given an integer array nums and integer k, return true if nums has a good subarray:
a contiguous subarray of length at least 2 whose sum is a multiple of k.

```
nums=[23,2,4,6,7], k=6    →  True   ([2,4] sums to 6)
nums=[23,2,6,4,7], k=6    →  True   (entire array sums to 42 = 7×6)
nums=[23,2,6,4,7], k=13   →  False
nums=[5,0,0,0], k=3       →  True   ([0,0] sums to 0)
nums=[0,1,0], k=2         →  False
```

Constraints: 1 <= nums.length <= 10^5. 0 <= nums[i] <= 10^9. 1 <= k <= 2^31-1.

This had a Wrong Answer on LC. Resubmit after fixing — see warm-up block above.
Key difference from LC 974: you return True/False, not count. Use `seen = {0: -1}`.

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

### T2-2. LC 744
Easy

You are given a characters array letters that is sorted in non-decreasing order,
and a character target.
Return the smallest character in letters that is strictly greater than target.
If such a character does not exist, return the first character in letters.

```
letters=["c","f","j"], target="a"   →  "c"
letters=["c","f","j"], target="c"   →  "f"
letters=["c","f","j"], target="d"   →  "f"
letters=["c","f","j"], target="j"   →  "c"  (wraps around)
letters=["x","x","y","y"], target="z"  →  "x"
```

Constraints: 2 <= letters.length <= 10^4. letters[i] is a lowercase English letter.
letters is sorted. letters has at least two different characters.

Solve in O(log n).

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

### T2-3. LC 11
Medium

You are given an integer array height of length n. There are n vertical lines drawn
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container that holds the most water.
Return the maximum amount of water the container can store.

```
height=[1,8,6,2,5,4,8,3,7]   →  49
height=[1,1]                   →  1
height=[4,3,2,1,4]            →  16
height=[1,2,1]                 →  2
```

Constraints: n >= 2. 0 <= height[i] <= 10^4.

Submit to LC after solving — this is still marked NA in STATUS.

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

### T3-1. LC 560
Medium

Given an array of integers nums and an integer k, return the total number of
subarrays whose sum equals to k.

```
nums=[1,1,1], k=2       →  2
nums=[1,2,3], k=3       →  2
nums=[1,-1,0], k=0      →  3
nums=[0,0,0,0], k=0     →  10
```

Constraints: 1 <= nums.length <= 2×10^4. -1000 <= nums[i] <= 1000.

This is Tier 3 — should be fast. If it takes >15 min, it drops to Tier 2.

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

### T3-2. LC 205
Easy

Given two strings s and t, return true if s is isomorphic to t.
Two strings are isomorphic if the characters in s can be replaced to get t,
preserving order. No two characters may map to the same character.
A character may map to itself.

```
s="egg", t="add"      →  True
s="foo", t="bar"      →  False
s="paper", t="title"  →  True
s="badc", t="baba"    →  False
```

Constraints: 1 <= s.length <= 5×10^4. t.length == s.length.

This is Tier 3 — should be fast. If it takes >15 min, it drops to Tier 2.

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

---

### N1. Binary Subarrays With Sum — LC 930
Medium

Given a binary array nums and an integer goal, return the number of non-empty
subarrays with a sum equal to goal.

A subarray is a contiguous part of the array.

```
nums=[1,0,1,0,1], goal=2   →  4
nums=[0,0,0,0,0], goal=0   →  15
nums=[1,0,1], goal=1       →  4
nums=[0,1,0,1,0], goal=2   →  4
```

Constraints: 1 <= nums.length <= 3×10^4. nums[i] is 0 or 1. 0 <= goal <= nums.length.

Note: This looks similar to LC 560 but the array is binary and contains many zeros.
Brute force: O(n²) nested loops. There is an O(n) solution.

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

### N2. Make Sum Divisible by P — LC 1590
Medium

Given an array of positive integers nums, remove the smallest subarray (possibly empty)
such that the sum of the remaining elements is divisible by p.
It is not allowed to remove the whole array.
Return the length of the smallest subarray that you need to remove, or -1 if impossible.

```
nums=[3,1,4,2], p=6     →  1   (remove [4], remaining sum = 6)
nums=[6,3,5,2], p=9     →  2   (remove [5,2], remaining sum = 9)
nums=[1,2,3], p=3       →  0   (sum = 6, already divisible)
nums=[1,2,3], p=7       →  -1  (impossible)
nums=[1000000000,1000000000,1000000000], p=3  →  0
```

Constraints: 1 <= nums.length <= 10^5. 1 <= nums[i] <= 10^9. 1 <= p <= 10^9.

Harder variant — think step by step:
Step 1: total_remainder = sum(nums) % p. If 0 → return 0.
Step 2: You need to find the shortest subarray whose sum ≡ total_remainder (mod p).
Step 3: Use prefix sum + hash map to find shortest such subarray.

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

1. Tier 4 recalls (10 min)
2. Pattern warm-up — Prefix Sum Modulo table (3 min, from memory)
3. **T1: LC 974 first** — solve blind, no warm-up visible
4. T2: LC 523 → fix WA and resubmit
5. T2: LC 744 → Binary Search, should be fast
6. T3: LC 560 → should be Tier 3 speed (<15 min)
7. T3: LC 205 → should be Tier 3 speed (<15 min)
8. T2: LC 11 → Two Pointers Maximize
9. New: LC 930 → should recognize same as LC 560
10. New: LC 1590 → hardest today, attempt last

If time is short: stop after LC 11. Skip 1590 for tomorrow.

---

## Note on Overdue Tier 2 (not in today's plan)

These 5 Tier 2 problems were due Jun 27 but not scheduled today (10+ competing problems):
LC 692, LC 1, LC 1456, LC 367, LC 441

They carry over to Day 29. None are pattern-critical right now (Freq Sorting, Complement Lookup, Binary Search Lower bound extras).

---

## Daily Summary

| Slot | Problems | Count |
|------|----------|-------|
| Tier 4 Recalls | Running State, Prefix Sum Pivot | 2 |
| Tier 1 | LC 974 | 1 |
| Tier 2 | LC 523, LC 744, LC 11 | 3 |
| Tier 3 | LC 560, LC 205 | 2 |
| New | LC 930, LC 1590 | 2 |
| **Total** | | **10** |

---

## What Success Looks Like Today

- **LC 974**: solved independently from scratch, <30 min → Tier 2 or 3
- **LC 523**: WA fixed, resubmitted, Accepted → Tier 2 or 3
- **LC 560, 205**: both done in <15 min each → confirm Tier 3
- **LC 930**: identified as same pattern as LC 560, solved independently
- **LC 1590**: attempt made (Tier 2 is fine for this difficulty)

If LC 974 is still Hint → the Modulo variant is genuinely shaky. Add an extra day.
If LC 974 is Independent + <25 min → Prefix Modulo is building, proceed to Binary Search Applied on Day 29.

---

## End of Day

Run PROMPT 1 to evaluate, assign tiers, and update STATUS.md.

# Day 33 — 2026-07-06 — Reinforcement Day
Focus: Binary Search (Applied + Lower-bound close-out) + Hash Set (Sequence Expansion) consolidation
Phase: Gap Fill (final day before Linked Lists starts Jul 7)
Daily target: 10 problems (2 Tier1 + 0 Tier2 + 3 Tier3 + 2 Tier4 recalls + 3 new)

---
## SOP Reminder (2 min before every problem)
Read fully → Restate in one line → Identify pattern → Plan in words → Dry run → Code → Test

Full SOP: problem_solving.md. Do not skip Step 3 (write `# Pattern: ... | Variant: ...` before coding).
RULE: complexity fields must be real answers with justification, never `O(?)`. Wrong complexity = automatic Tier 1.

---
## Concept Refresher — PATTERNS.md gap (no block exists yet for these two patterns)

Both problems that have chronically needed hints (128, 441) belong to patterns with **no written block in PATTERNS.md**. Do the 3-step warm-up below for each before touching the Tier 1 problems. If either warm-up fails, that IS the signal these need a standalone session — don't just push through to the answer.

**Warm-up protocol (answer all 3 before coding):**
1. Write the template from memory.
2. "The invariant this template maintains is: ___"
3. "If I changed [specific line] to [wrong version], it would fail because: ___"

### Binary Search — Applied (answer-space search, not array search)
**Trigger words:** rotated sorted array, minimum in rotated array, minimize the maximum, minimum speed/days to finish, capacity to ship
**Mental model:** The search space is often the ANSWER, not the array — binary search works on any monotonic true/false predicate.
**Why it exists:** Linear scan over the answer range is O(range); binary search over a monotonic feasibility check collapses it to O(log(range) × check_cost).
**Template (feasibility form):**
```python
lo, hi = min_possible, max_possible
while lo < hi:
    mid = (lo + hi) // 2
    if feasible(mid):
        hi = mid
    else:
        lo = mid + 1
return lo
```
**Common mistakes:**
1. Loop bound mismatch — `lo < hi` with `hi = mid` must never pair with `lo <= hi`, causes infinite loop
2. LC 33: must first determine which half is sorted before deciding which side target could be on
3. Koko-style: hours per pile = ceil(pile / k), not floor — off-by-one drops valid answers

### Hash Set — Sequence Expansion
**Trigger words:** longest consecutive sequence, longest run of consecutive integers
**Mental model:** Only start counting a run from a number whose `num - 1` is NOT in the set — guarantees each run is counted exactly once, from its true start.
**Why it exists:** Sorting is O(n log n). The "only start from sequence heads" check makes the total work O(n) — every number is ever extended into at most once across the whole run.
**Template:**
```python
num_set = set(nums)
longest = 0
for num in num_set:
    if num - 1 not in num_set:      # only start counting from sequence starts
        length = 1
        while num + length in num_set:
            length += 1
        longest = max(longest, length)
return longest
```
**Common mistakes:**
1. Skipping the `num - 1 not in num_set` check → re-walks every sequence from every element → O(n²) worst case (often still "passes" on small inputs, which is why this keeps sneaking through as a false-independent solve)
2. Starting `length` at 0 instead of 1
3. Iterating the raw list instead of the set (not wrong, just redundant work — dedupe first)

---
## TIER 4 Recalls (5 min each, no full solve)
Write the template from memory. If you can't in 3 min → flag as Tier 2.
1. Frequency Hashing
2. Sliding Window (Fixed size)

---
## TIER 1 — Priority Revision (solve both, no hints — 2nd/3rd consecutive attempt on both)

### 1. Longest Consecutive Sequence (LC 128) — Medium
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence. Your algorithm must run in O(n) time.

Example 1: `nums = [100,4,200,1,3,2]` → Output: `4` (the sequence is 1,2,3,4)
Example 2: `nums = [0,3,7,2,5,8,4,6,0,1]` → Output: `9`

Constraints: `0 <= nums.length <= 10^5`, `-10^9 <= nums[i] <= 10^9`

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

### 2. Arranging Coins (LC 441) — Easy
You have `n` coins and want to build a staircase with `k` rows where the `i`th row has exactly `i` coins. The last row may be incomplete. Given `n`, return the number of complete rows.

Example 1: `n = 5` → Output: `2`
Example 2: `n = 8` → Output: `3`

Constraints: `1 <= n <= 2^31 - 1`

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
## TIER 2 — Revision (0 due today)
No Tier 2 problems due Jul 6. Skip this slot — compensated with an extra Tier 3 pick below.

---
## TIER 3 — Revision (3 problems)

### 1. Find Smallest Letter Greater Than Target (LC 744) — Easy
Given a characters array `letters` sorted in non-decreasing order and a character `target`, return the smallest character in the array that is larger than `target`. If no such character exists, return the first character in `letters` (wrap around).

Example 1: `letters = ["c","f","j"], target = "a"` → `"c"`
Example 2: `letters = ["c","f","j"], target = "c"` → `"f"`
Example 3: `letters = ["c","f","j"], target = "d"` → `"f"`

Constraints: `2 <= letters.length <= 10^4`, letters are lowercase, sorted, contain at least 2 distinct characters.

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

### 2. Guess Number Higher or Lower (LC 374) — Easy
Pick a number from 1 to `n`. A pre-built API `guess(num)` returns `-1` (pick is lower), `1` (pick is higher), or `0` (correct). Return the number.

Example 1: `n = 10, pick = 6` → Output: `6`

Constraints: `1 <= n <= 2^31 - 1`, `1 <= pick <= n`

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

### 3. Maximum Number of Vowels in a Substring of Given Length (LC 1456) — Medium
Given a string `s` and an integer `k`, return the maximum number of vowel letters in any substring of `s` with length `k`.

Example 1: `s = "abciiidef", k = 3` → Output: `3`
Example 2: `s = "aeiou", k = 2` → Output: `2`
Example 3: `s = "leetcode", k = 3` → Output: `2`

Constraints: `1 <= s.length <= 10^5`, lowercase letters, `1 <= k <= s.length`

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
## New Problems (3 problems)

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
## Daily Summary
New: 3 | Tier1: 2 | Tier2: 0 | Tier3: 3 | Tier4: 2 | Total: 10

## Mandatory Closing Check
# Prompt 1 (End of Day agent) run: Yes
# STATUS.md updated: Yes

# Day 26 — June 25, 2026 — Learning Day
Focus: Two Pointers (Maximize variant) + Prefix Sum (Modulo variant) — NEW CONCEPTS
Phase: Gap Fill — closing 2 critical missing variants before Linked Lists
Daily target: 12 problems (2 recalls + 4 tier1 + 3 tier2 + 2 tier3 + 1 new)

---

## SOP Reminder (read before every problem — 2 min)

Read fully → Restate in one line → Identify pattern → Brute force in words →
Optimal plan in words → Dry run on paper → Code → Test edge cases → Submit

Time targets: Easy = 15-20 min | Medium = 25-35 min
Exceed the target → Tier 1 regardless of correctness.

---

## TIER 4 Template Recalls (5 min each — write from memory, no notes)

### Recall 1 — Sliding Window (Variable size)
Write the full variable-size sliding window template from memory.
Include: state setup, loop structure, shrink condition, answer update.
If you cannot write it in 3 min → mark as Tier 2 and add to revision pool.

```python
# Write here from memory



```
Time taken: ___ min | Result: Recalled clean / Struggled (→ Tier 2)

---

### Recall 2 — Prefix Sum + Hash Map (560 style)
Write the template from memory.
Include: seen dict initialization, prefix accumulation, needed calculation, count update.

```python
# Write here from memory



```
Time taken: ___ min | Result: Recalled clean / Struggled (→ Tier 2)

---

## NEW CONCEPT 1 — Two Pointers: Maximize/Minimize Between Two Ends

This variant did not fire for you on LC 11. Learn it now before attempting.

### Where to learn
Neetcode.io → search "Container With Most Water" → watch concept explanation only (first 5 min).
Stop before he codes. Then fill the template below from your understanding.

### Trigger words
"maximum area", "container", "most water", "maximize value between two indices",
"two walls", "height and distance", "minimize cost between endpoints"

### Mental model
Start with the widest possible window (left=0, right=end).
At each step, the value = min(height[left], height[right]) × distance.
The bottleneck is always the SHORTER side.
Move the shorter side inward — moving the taller side can never increase the value.

### Why it exists
Brute force: check every pair of indices → O(n²).
Two pointers: one scan from both ends → O(n).
Key insight: you never need to check pairs where moving the taller side,
because min() is already limited by the shorter — only moving shorter can help.

### Template (fill after watching — write from memory)

```python
def two_pointer_maximize(arr):
    left = 0
    right = len(arr) - 1
    best = 0

    while left < right:
        # calculate current value
        value = _______________

        best = max(best, value)

        # move the side that limits the value
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1

    return best
```

### Dry run — height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

Trace the first 4 steps manually before coding LC 11:

| left | right | h[l] | h[r] | area | best | move |
|------|-------|------|------|------|------|------|
| 0 | 8 | 1 | 7 | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

Expected final answer: 49

### Common mistakes
1. Moving the TALLER side instead of shorter — this never helps
2. Using area = height[left] × (right - left) without min() — wrong when heights differ
3. Missing the while left < right condition — left == right means no container

---

## NEW CONCEPT 2 — Prefix Sum: Modulo Variant

This is what LC 523 needed. Your sliding window approach cannot solve this.

### Where to learn
Neetcode.io → search "Continuous Subarray Sum" → watch concept explanation only.
Stop before he codes. Then fill below.

### Trigger words
"multiple of k", "divisible by k", "subarray sum divisible",
"contiguous subarray sum is a multiple", "sum % k == 0"

### Mental model
If prefix[i] % k == prefix[j] % k,
then the subarray between j+1 and i has sum divisible by k.

Why? prefix[i] - prefix[j] = sum(j+1..i)
If both have same remainder when divided by k → their difference is divisible by k.

Store the EARLIEST index where each remainder was seen.
Check if gap between current index and stored index >= 2 (length at least 2).

### Why it exists
Sliding window cannot handle "divisible by k" — shrinking the window
doesn't give you control over divisibility.
Prefix + modulo converts the divisibility check into an equality check on remainders.

### Template

```python
def prefix_modulo(nums, k):
    seen = {0: -1}   # remainder 0 seen before index 0
    prefix = 0

    for i, num in enumerate(nums):
        prefix += num
        remainder = prefix % k

        if remainder in seen:
            if i - seen[remainder] >= 2:   # length must be at least 2
                return True
        else:
            seen[remainder] = i   # store EARLIEST index only — never update

    return False
```

### Dry run — nums = [23, 2, 4, 6, 7], k = 6

| i | num | prefix | prefix%6 | seen | in seen? | gap>=2? |
|---|-----|--------|----------|------|----------|---------|
| — | — | 0 | 0 | {0:-1} | — | — |
| 0 | 23 | 23 | 5 | | | |
| 1 | 2 | 25 | 1 | | | |
| 2 | 4 | 29 | 5 | | | |
| 3 | 6 | 35 | 5 | | | |

Expected: True (subarray [2,4] sums to 6, which is 1×6)

### Common mistakes
1. Updating seen[remainder] every time — only store EARLIEST index
2. Forgetting the gap >= 2 check — subarray must have length >= 2
3. Using sliding window — this problem cannot be solved with sliding window
4. Not initializing seen = {0: -1} — misses subarrays starting from index 0

---

## TIER 1 — Priority Revision (solve all 4 before moving to anything else)

---

### T1-1. Container With Most Water — LC 11
Medium | Two Pointers — Maximize variant

You attempted this before and did not recognize the pattern.
Now you have the concept. Solve it using the template above.

Given n vertical lines where the ith line has height height[i].
Find two lines that form a container holding the most water.
Return the maximum amount of water the container can store.

Examples:
```
height = [1,8,6,2,5,4,8,3,7]  →  49
height = [1,1]                 →  1
height = [4,3,2,1,4]          →  16
height = [1,2,1]               →  2
```

Constraints: n >= 2. 0 <= height[i] <= 10^4.

Dry run before coding. Fill the table in the concept block above.
Submit to LC after local solve.

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: Two Pointers
# Variant: Maximize/minimize between ends
# mistakes/confusion:
```

---

### T1-2. Continuous Subarray Sum — LC 523
Medium | Prefix Sum — Modulo variant

Your previous attempt used sliding window — wrong approach.
Now you have the correct concept. Solve using the template above.

Given an integer array nums and integer k, return true if nums has a
"good subarray": length >= 2 AND sum is a multiple of k.

Examples:
```
nums = [23,2,4,6,7], k = 6   →  True  ([2,4] sums to 6)
nums = [23,2,6,4,7], k = 6   →  True  (entire array sums to 42 = 7×6)
nums = [23,2,6,4,7], k = 13  →  False
nums = [5,0,0,0], k = 3      →  True  ([0,0] sums to 0, 0 is multiple of 3)
```

Constraints: 1 <= nums.length <= 10^5. 0 <= nums[i] <= 10^9. 1 <= k <= 2^31-1.

Edge case to check: sum = 0 (0 is always a multiple of k).

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: Prefix Sum
# Variant: Modulo
# mistakes/confusion:
```

---

### T1-3. Guess Number Higher or Lower — LC 374
Easy | Binary Search — Standard

This failed on Day 22 and was never retried. Today close it out.

We play a game. I pick a number from 1 to n.
You call guess(num) API: returns -1 (too high), 1 (too low), 0 (correct).
Find the number I picked.

```python
# The guess API is already defined:
# def guess(num: int) -> int:

Examples:
n=10, pick=6  →  6
n=1,  pick=1  →  1
n=2,  pick=2  →  2
```

Constraints: 1 <= n <= 2^31-1. 1 <= pick <= n.

Use left <= right loop. Adjust based on guess() return value.

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: Binary Search
# Variant: Standard
# mistakes/confusion:
```

---

### T1-4. Subarray Sum Equals K — LC 560
Medium | Prefix Sum — Prefix + Hash Map

Flagged shaky multiple times. Solve from scratch today — no looking at old code.

Given array nums and integer k, return count of subarrays whose sum equals k.

```
[1,1,1], k=2     →  2
[1,2,3], k=3     →  2
[1,-1,0], k=0    →  3
[0,0,0,0], k=0   →  5
```

Constraints: 1 <= nums.length <= 2×10^4. -1000 <= nums[i] <= 1000.

Mental trigger before coding: seen={0:1}, needed = prefix - k

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: Prefix Sum
# Variant: Prefix + Hash Map
# mistakes/confusion:
```

---

## TIER 2 — Revision (3 problems — no pattern label, identify yourself)

---

### T2-1. LC 1207
Easy

Given an array of integers arr, return true if the number of occurrences
of each value in the array is unique, or false otherwise.

```
[1,2,2,1,1,3]   →  True   (1 appears 3 times, 2 appears 2 times, 3 appears 1 time — all unique)
[1,2]            →  False  (both appear 1 time)
[−3,0,1,−3,1,1,1,−3,10,0]  →  True
```

Constraints: 1 <= arr.length <= 1000. -1000 <= arr[i] <= 1000.

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern:
# Variant:
# mistakes/confusion:
```

---

### T2-2. LC 205
Easy

Given two strings s and t, return true if s is isomorphic to t.
Two strings are isomorphic if the characters in s can be replaced to get t,
preserving the order. No two characters may map to the same character.
A character may map to itself.

```
"egg", "add"    →  True
"foo", "bar"    →  False
"paper","title" →  True
"badc","baba"   →  False
```

Constraints: 1 <= s.length <= 5×10^4. t.length == s.length.

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern:
# Variant:
# mistakes/confusion:
```

---

### T2-3. LC 852
Medium

You may treat this as a sorted-then-unsorted structure.
Given a mountain array arr (values increase to a peak then decrease),
return the index of the peak element.

Solve in O(log n) time this time. Not O(n).

```
arr = [0,1,0]      →  1
arr = [0,2,1,0]    →  1
arr = [0,10,5,2]   →  1
arr = [3,4,5,1]    →  2
```

Constraints: 3 <= arr.length <= 10^5. 0 <= arr[i] <= 10^6. Guaranteed mountain.

Hint trigger: if arr[mid] > arr[mid+1] → peak is at mid or left → right = mid
              if arr[mid] < arr[mid+1] → peak is right of mid → left = mid+1
              when left == right → that is the peak

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern:
# Variant:
# mistakes/confusion:
```

---

## TIER 3 — Revision (2 problems)

---

### T3-1. LC 27
Easy

Given integer array nums and integer val, remove all occurrences of val in-place.
Return the number of elements that are not equal to val.
The order of remaining elements does not matter.

```
[3,2,2,3], val=3   →  2  (first 2 elements are [2,2])
[0,1,2,2,3,0,4,2], val=2  →  5 (first 5 elements are [0,1,3,0,4])
```

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern:
# Variant:
# mistakes/confusion:
```

---

### T3-2. LC 167
Medium

Given a 1-indexed array of integers numbers sorted in non-decreasing order,
find two numbers that add up to a specific target.
Return their indices as [index1, index2] (1-indexed).
Use only constant extra space.

```
[2,7,11,15], target=9   →  [1,2]
[2,3,4], target=6       →  [1,3]
[-1,0], target=-1       →  [1,2]
```

Constraints: 2 <= numbers.length <= 3×10^4. Exactly one solution exists.

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern:
# Variant:
# mistakes/confusion:
```

---

## NEW PROBLEM — Second problem for today's new concept (1 problem)

---

### N1. Subarray Sums Divisible by K — LC 974
Medium | Same concept as LC 523 — practice the modulo variant again

Given integer array nums and integer k, return the number of non-empty subarrays
that have a sum divisible by k.

```
nums=[4,5,0,-2,-3,1], k=5   →  7
nums=[5], k=9                →  0
```

Constraints: 1 <= nums.length <= 3×10^4. -10^4 <= nums[i] <= 10^4. 2 <= k <= 10^4.

Difference from LC 523: return COUNT of subarrays, not just True/False.
Same core idea: remainder = prefix % k. But now use frequency map, not just existence check.

Mental trigger:
```
seen = {0: 1}       ← remainder 0 seen once (before array)
for each element:
    prefix += num
    remainder = prefix % k
    if remainder < 0: remainder += k   ← handle negative numbers
    count += seen.get(remainder, 0)
    seen[remainder] = seen.get(remainder, 0) + 1
```

Note: This is the COUNT version. LC 523 was the EXISTS version.
Use the frequency map (like LC 560) combined with the modulo idea.

```python
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: Prefix Sum
# Variant: Modulo
# mistakes/confusion:
```

---

## Daily Summary

| Slot | Problems | Count |
|------|----------|-------|
| Tier 4 Recalls | Sliding Window template, Prefix+HashMap template | 2 |
| Tier 1 | LC 11, LC 523, LC 374, LC 560 | 4 |
| Tier 2 | LC 1207, LC 205, LC 852 | 3 |
| Tier 3 | LC 27, LC 167 | 2 |
| New | LC 974 | 1 |
| **Total** | | **12** |

---

## Priority Order for Today

1. Tier 4 recalls first (10 min total)
2. Read BOTH new concept blocks completely
3. Dry run both concept examples on paper
4. Tier 1 in order: LC 11 → LC 523 → LC 374 → LC 560
5. Tier 2 and Tier 3 after all Tier 1 done
6. LC 974 last

---

## End of Day

Run PROMPT 1 to update STATUS.md and get tomorrow's plan ready.

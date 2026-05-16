# Day 11 — May 17, 2026 — Retrieval
Focus: Prefix Sum + Running-State Tracking
LC target today: Running Sum (1480) — ready to submit, due May 18 (3d recall)

---

## Concept Warm-Up (5 min)
Write both templates from memory. No notes.

```python
# Prefix Sum — build array where prefix[i] = sum of nums[0..i-1]


```

```python
# Running-State Tracking (Kadane's) — extend or restart at each element


```

---

## Revision Problems (5 problems — all due May 17)

### Product of Array Except Self (LC 238)
Pattern: Prefix Sum (prefix × suffix products)
Due: May 17 (24h recall)
Constraint: No division allowed. 2 <= nums.length <= 10^5.
Examples: [1,2,3,4] → [24,12,8,6] | [-1,1,0,-3,3] → [0,0,9,0,0]
Goal: Solve without hints this time. Left pass builds prefix products, right pass multiplies suffix in-place.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

### Subarray Sum Equals K (LC 560)
Pattern: Prefix Sum + Hash Map
Due: May 17 (24h recall)
Constraint: 1 <= nums.length <= 2×10^4. -10^7 <= k <= 10^7. Negative numbers allowed.
Examples: [1,1,1], k=2 → 2 | [1,2,3], k=3 → 2 | [3,4,7,2,-3,1,4,2], k=7 → 4
Goal: Reconstruct from scratch. seen = {0:1}. At each step: count += seen.get(prefix - k, 0).
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

### Maximum Subarray (LC 53)
Pattern: Running-State Tracking (Kadane's)
Due: May 17 (24h recall)
Constraint: 1 <= nums.length <= 10^5. -10^4 <= nums[i] <= 10^4.
Examples: [-2,1,-3,4,-1,2,1,-5,4] → 6 | [5,4,-1,7,8] → 23 | [-1,-2,-3] → -1
Goal: Two running variables: current_sum and max_sum. Decision: extend or start fresh.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

### Group Anagrams (LC 49)
Pattern: Grouping Hash Maps
Due: May 17 (3d recall)
Constraint: 1 <= strs.length <= 10^4. All lowercase. 0 <= strs[i].length <= 100.
Examples: ["eat","tea","tan","ate","nat","bat"] → [["bat"],["nat","tan"],["ate","eat","tea"]] | [""] → [[""]]
Goal: sorted(word) as key, append to defaultdict list. Return list of values.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

### Find Pivot Index (LC 724)
Pattern: Prefix Sum
Due: May 17 (3d recall)
Constraint: 1 <= nums.length <= 10^4. -1000 <= nums[i] <= 1000.
Examples: [1,7,3,6,5,6] → 3 | [1,2,3] → -1 | [2,1,-1] → 0
Goal: left_sum starts at 0. At each index: if left_sum == total - left_sum - nums[i] → return i. Then add nums[i] to left_sum.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

## New Problems (3 problems — local only, do NOT submit to LC)

### Find the Highest Altitude (LC 1732)
Pattern: Prefix Sum (running prefix max)
Difficulty: Easy
Constraints: n == gain.length, 1 <= n <= 100, -100 <= gain[i] <= 100

Description: A biker starts at altitude 0. Given an array gain where gain[i] is the net altitude change between point i and i+1, return the highest altitude reached at any point (including the start at 0).

Examples:
- [-5,1,5,0,-7] → 1
- [-4,-3,-2,-1,4,3,2] → 0

Key insight: Build the running altitude prefix (cumulative sum), track the max. Start max at 0 (the starting altitude).

---

### Maximum Product Subarray (LC 152)
Pattern: Running-State Tracking (track both max and min)
Difficulty: Medium
Constraints: 1 <= nums.length <= 2×10^4, -10 <= nums[i] <= 10

Description: Given an integer array nums, find the subarray with the largest product and return the product.

Examples:
- [2,3,-2,4] → 6
- [-2,0,-1] → 0
- [-2,3,-4] → 24

Key insight: Unlike Kadane's, track both max_prod and min_prod at every step. A negative number flips min↔max. At each element: new_max = max(num, num*max_prod, num*min_prod).

---

### Isomorphic Strings (LC 205)
Pattern: Grouping Hash Maps (bijection mapping)
Difficulty: Easy
Constraints: 1 <= s.length <= 5×10^4, t.length == s.length, valid ASCII characters

Description: Two strings s and t are isomorphic if characters in s can be replaced one-to-one to get t. No two characters may map to the same character, but a character may map to itself. Return True if isomorphic.

Examples:
- s="egg", t="add" → True
- s="foo", t="bar" → False
- s="paper", t="title" → True

Key insight: Two dicts — s_to_t and t_to_s. At each position, check both directions are consistent: if s[i] already mapped, it must map to t[i]; if t[i] already mapped-to, it must come from s[i].

---

## After Solving — log in your .py file

```python
# Status: Independent / Hint / Failed
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# mistakes/confusion: [note or NA]
# Pattern: [pattern name]
```

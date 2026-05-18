# Day 12 — May 18 — Recovery
Focus: Clear overdue revisions + 24h recalls | Week 2 wrap-up
LC target today: Running Sum (1480) + Find Highest Altitude (1732) — both independent, quick submits

---

## Concept Warm-Up (5 min)
Write both Building-family templates from memory. No notes.

```python
# Prefix Sum — build prefix array where prefix[i] = sum of nums[0..i-1]


```

```python
# Kadane's (Running-State Tracking) — extend or restart at each element


```

---

## Revision Problems (5 problems — overdue first)

### Sort Characters by Frequency (LC 451)
Pattern: Frequency Sorting
Due: May 17 — 3d recall (OVERDUE)
Constraint: 1 <= s.length <= 5×10^5. Uppercase, lowercase, and digits.
Examples: "tree" → "eert" | "cccaaa" → "cccaaa" | "Aabb" → "bbAa"
Goal: Count character frequencies → sort by frequency descending → build result string.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

### Intersection of Two Arrays II (LC 350)
Pattern: Frequency Hashing
Due: May 17 — 3d recall (OVERDUE)
Constraint: 1 <= nums1.length, nums2.length <= 1000. 0 <= nums1[i], nums2[i] <= 1000.
Examples: [1,2,2,1], [2,2] → [2,2] | [4,9,5], [9,4,9,8,4] → [4,9]
Goal: Count frequencies for both arrays → for each key take min(count1, count2) → expand to result list.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

### Find the Highest Altitude (LC 1732)
Pattern: Prefix Sum (running prefix max)
Due: May 18 — 24h recall
Constraint: n == gain.length, 1 <= n <= 100, -100 <= gain[i] <= 100.
Examples: [-5,1,5,0,-7] → 1 | [-4,-3,-2,-1,4,3,2] → 0
Goal: Running cumulative altitude from 0 → track max. Start max_alt at 0 (the starting altitude counts).
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

### Isomorphic Strings (LC 205)
Pattern: Grouping Hash Maps (bijection mapping)
Due: May 18 — 24h recall
Constraint: 1 <= s.length <= 5×10^4. t.length == s.length. Valid ASCII characters.
Examples: "egg", "add" → True | "foo", "bar" → False | "paper", "title" → True | "ab", "aa" → False
Goal: Two dicts — s_to_t and t_to_s. At each position check BOTH directions: if already mapped it must match; if already mapped-to it must come from same source.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

### Maximum Product Subarray (LC 152)
Pattern: Running-State Tracking (track both max and min)
Due: May 18 — 24h recall
Constraint: 1 <= nums.length <= 2×10^4. -10 <= nums[i] <= 10.
Examples: [2,3,-2,4] → 6 | [-2,0,-1] → 0 | [-2,3,-4] → 24
Goal: Unlike Kadane's, track both max_prod AND min_prod at every step. A negative number flips min↔max. At each element: new_max = max(num, num*max_prod, num*min_prod). Same for min.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

## New Problems
Recovery Day — no new problems today.
Use this time to: submit Running Sum + Find Highest Altitude to LC, and review the Week 3 plan.

---

Note: After solving each problem in your .py file, log these comment fields:
  # Status: Independent / Hint / Failed
  # Time complexity: O(?)
  # Space complexity: O(?)
  # LC status: Accepted / NA / Not submitted
  # mistakes/confusion: [note or NA]
  # Pattern: [pattern name]

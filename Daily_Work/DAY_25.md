# Intensive Revision Sprint — Non-Binary-Search Patterns

**Goal:** Rebuild confidence across Arrays, Strings, Hashing, Prefix Sum, Two Pointers, Sliding Window, and Running-State Tracking.

**Rule:**

* Do not see old code for the first 15–20 minutes.
* If stuck, write the pattern and invariant before taking a hint.
* After solving, write: `Independent / Hint / Old code seen`.
* Binary Search is intentionally excluded from this sprint.

---

## Session 1 — Prefix Sum + All Subarray Problems

These are the highest priority because they contain the most concept-heavy logic.

### 1. Running Sum of 1D Array — LC 1480

**Pattern:** Prefix Sum
**Recall trigger:** `prefix[i] = prefix[i-1] + nums[i]`

Tests:

```python
[1,2,3,4]          # [1,3,6,10]
[3,1,2,10,1]       # [3,4,6,16,17]
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

### 2. Find Pivot Index — LC 724

**Pattern:** Prefix Sum
**Recall trigger:** `right_sum = total - left_sum - current`

Tests:

```python
[1,7,3,6,5,6]      # 3
[1,2,3]             # -1
[2,1,-1]            # 0
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

### 3. Find Highest Altitude — LC 1732

**Pattern:** Running Prefix Sum

Tests:

```python
[-5,1,5,0,-7]       # 1
[-4,-3,-2,-1,4,3,2] # 0
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

### 4. Range Sum Query — Immutable — LC 303

**Pattern:** Prefix Sum
**Priority:** Concept not understood earlier.

Tests:

```python
nums = [-2,0,3,-5,2,-1]

sumRange(0,2)       # 1
sumRange(2,5)       # -1
sumRange(0,5)       # -3
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

### 5. Product of Array Except Self — LC 238

**Pattern:** Prefix Product + Suffix Product
**Recall trigger:** Left product does **not** include current item; right product does **not** include current item.

Tests:

```python
[1,2,3,4]           # [24,12,8,6]
[-1,1,0,-3,3]       # [0,0,9,0,0]
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

### 6. Subarray Sum Equals K — LC 560

**Pattern:** Prefix Sum + Frequency Hash Map
**Priority:** Previously hint-needed and flagged shaky.

Mental trigger:

```text
needed_prefix = current_prefix - k
seen = {0: 1}
```

Tests:

```python
[1,1,1], 2          # 2
[1,2,3], 3          # 2
[1,-1,0], 0         # 3
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

### 7. Contiguous Array — LC 525

**Pattern:** Prefix Balance + Hash Map
**Priority:** Concept not understood earlier.

Mental trigger:

```text
0 -> -1
1 -> +1

same balance seen again
= equal number of 0 and 1 between indices
```

Tests:

```python
[0,1]                       # 2
[0,1,0]                     # 2
[0,1,1,0,1,1,1,0]           # 4
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

### 8. Maximum Subarray — LC 53

**Pattern:** Running-State Tracking / Kadane’s Algorithm
**Subarray problem — mandatory.**

Tests:

```python
[-2,1,-3,4,-1,2,1,-5,4]     # 6
[1]                          # 1
[5,4,-1,7,8]                # 23
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

### 9. Maximum Product Subarray — LC 152

**Pattern:** Running-State Tracking
**Subarray problem — mandatory.**

Mental trigger:

```text
Negative number can swap maximum and minimum.
Track both current_max and current_min.
```

Tests:

```python
[2,3,-2,4]                  # 6
[-2,0,-1]                   # 0
[-2,3,-4]                   # 24
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

### 10. Maximum Average Subarray I — LC 643

**Pattern:** Fixed-Size Sliding Window
**Subarray problem — mandatory.**

Tests:

```python
[1,12,-5,-6,50,3], 4        # 12.75
[5], 1                       # 5.0
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

## Session 2 — Sliding Window + String Subarray Patterns

### 11. Longest Substring Without Repeating Characters — LC 3

**Pattern:** Variable-Size Sliding Window + Set

Tests:

```python
"abcabcbb"                  # 3
"bbbbb"                     # 1
"pwwkew"                    # 3
"baca"                      # 3
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

### 12. Minimum Size Subarray Sum — LC 209

**Pattern:** Variable-Size Sliding Window
**Subarray problem — mandatory.**

Mental trigger:

```text
Expand until sum >= target.
While valid, update answer and shrink.
```

Tests:

```python
7, [2,3,1,2,4,3]            # 2
4, [1,4,4]                  # 1
11, [1,1,1,1,1]             # 0
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

### 13. Longest Repeating Character Replacement — LC 424

**Pattern:** Sliding Window + Frequency Map
**Priority:** Previously hint-needed.

Mental trigger:

```text
window_length - max_frequency <= k
```

Tests:

```python
"ABAB", 2                   # 4
"AABABBA", 1                # 4
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

### 14. Permutation in String — LC 567

**Pattern:** Fixed-Size Sliding Window + Frequency Map

Tests:

```python
"ab", "eidbaooo"            # True
"ab", "eidboaoo"            # False
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

### 15. Find All Anagrams in a String — LC 438

**Pattern:** Fixed-Size Sliding Window + Frequency Map

Tests:

```python
"cbaebabacd", "abc"         # [0,6]
"abab", "ab"                # [0,1,2]
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

### 16. Fruits Into Baskets — LC 904

**Pattern:** Variable-Size Sliding Window + Frequency Map
**Subarray problem — mandatory.**

Tests:

```python
[1,2,1]                     # 3
[0,1,2,2]                   # 3
[1,2,3,2,2]                 # 4
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

### 17. Max Consecutive Ones III — LC 1004

**Pattern:** Variable-Size Sliding Window
**Subarray problem — mandatory.**

Tests:

```python
[1,1,1,0,0,0,1,1,1,1,0], 2     # 6
[0,0,1,1,1,0,0], 0             # 3
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

### 18. Contains Duplicate II — LC 219

**Pattern:** Sliding Window + Set
**Important order:** Check → add → shrink.

Tests:

```python
[1,2,3,1], 3                # True
[1,0,1,1], 1                # True
[1,2,3,1,2,3], 2            # False
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

## Session 3 — Hash Maps, Sorting, Two Pointers, Strings

### 19. Top K Frequent Words — LC 692

**Pattern:** Frequency Sorting
**Priority:** Previously hint-needed.

Required sort order:

```text
frequency descending
word ascending
```

Tests:

```python
["i","love","leetcode","i","love","coding"], 2
# ["i","love"]

["aaa","aa","a"], 1
# ["a"]
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

### 20. Two Sum — LC 1

**Pattern:** Complement Lookup
**Recall trigger:** Store `number -> index`, not `needed -> index`.

Tests:

```python
[2,7,11,15], 9             # [0,1]
[3,2,4], 6                 # [1,2]
[3,3], 6                   # [0,1]
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

### 21. Two Sum II — Input Array Is Sorted — LC 167

**Pattern:** Two Pointers
**Use sorted property; do not use a dictionary.**

Tests:

```python
[2,7,11,15], 9             # [1,2]
[2,3,4], 6                 # [1,3]
[-1,0], -1                 # [1,2]
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

### 22. Isomorphic Strings — LC 205

**Pattern:** Two-Way Hash Map
**Priority:** Old solution was peeked during recall.

Tests:

```python
"egg", "add"               # True
"foo", "bar"               # False
"badc", "baba"             # False
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

### 23. Remove Duplicates from Sorted Array — LC 26

**Pattern:** Two Pointers + In-Place Overwrite
**Priority:** Write-pointer initialization was confusing earlier.

Tests:

```python
[1,1,2]                    # return 2; first values [1,2]
[0,0,1,1,1,2,2,3,3,4]     # return 5; first values [0,1,2,3,4]
[]                          # return 0
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

### 24. Remove Element — LC 27

**Pattern:** Two Pointers + In-Place Overwrite

Tests:

```python
[3,2,2,3], 3               # return 2
[0,1,2,2,3,0,4,2], 2      # return 5
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

### 25. Length of Last Word — LC 58

**Pattern:** String Traversal
**Priority:** Earlier marked as not solved.

Tests:

```python
"Hello World"                      # 5
"   fly me   to   the moon  "      # 4
"a"                                # 1
```

[ ] Independent  [ ] Hint  [ ] Old code seen

---

# Completion Standard

| Result        | Meaning                                                  |
| ------------- | -------------------------------------------------------- |
| Independent   | You wrote correct logic without seeing old code or hints |
| Hint          | You needed a small conceptual prompt                     |
| Old code seen | You looked at a previous solution or copied structure    |

## Final Assessment

After all 25 problems:

* **20+ independent:** ready to start Binary Search intensive revision.
* **15–19 independent:** repeat only the hint-needed problems once more.
* **Below 15 independent:** do not start Binary Search yet; first repair the weak non-binary patterns.

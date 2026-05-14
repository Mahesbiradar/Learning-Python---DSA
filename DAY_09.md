# DAY 09
Date: 2026-05-15
Week 2 / Day 9
Day Type: Reinforcement
Pattern Focus: Frequency Sorting + Complement Lookup

---

## Concept Warm-Up (write from memory, no notes, 10 min)

Write Frequency Sorting template from memory:
```python
# Your code here — sorting version only
```

Write Complement Lookup template from memory:
```python
# Your code here
```

Complexity check before continuing:
- Frequency Sorting: Time = ___, Space = ___
- Complement Lookup: Time = ___, Space = ___

---

## Revision Problems → Submit to LeetCode after independent local solve

### R1. Valid Anagram (LC 242) — Frequency Hashing
3-day recall. No notes. Must use `freq_s == freq_t` comparison. No `char in string` in any loop.

Constraints: 1 <= s.length, t.length <= 5×10⁴. Lowercase letters only.

Examples:
- s="anagram", t="nagaram" → True
- s="rat", t="car" → False
- s="", t="" → True
- s="a", t="ab" → False

Solve locally → If independent → Submit LC 242
Status: [ ] Independent  [ ] Hint  [ ] Failed
LC Result: [ ] Accepted  [ ] Wrong Answer  [ ] Not submitted
Time taken: ___

---

### R2. Two Sum (LC 1) — Complement Lookup
3-day recall. No notes. Check complement first, store after.

Constraints: 2 <= nums.length <= 10⁴. Exactly one valid answer.

Examples:
- [2,7,11,15], target=9 → [0,1]
- [3,2,4], target=6 → [1,2]
- [3,3], target=6 → [0,1]

Solve locally → If independent → Submit LC 1
Status: [ ] Independent  [ ] Hint  [ ] Failed
LC Result: [ ] Accepted  [ ] Wrong Answer  [ ] Not submitted
Time taken: ___

---

### R3. First Unique Character in a String (LC 387) — Frequency Hashing
24h recall. Count first, second pass over original string (not dict).

Constraints: 1 <= s.length <= 10⁵. Lowercase letters only.

Examples:
- "leetcode" → 0
- "loveleetcode" → 2
- "aabb" → -1
- "" → -1

Edge case before submitting: empty string, all same chars.

Solve locally → If independent → Submit LC 387
Status: [ ] Independent  [ ] Hint  [ ] Failed
LC Result: [ ] Accepted  [ ] Wrong Answer  [ ] Not submitted
Time taken: ___

---

### R4. Best Time to Buy and Sell Stock (LC 121) — Running State
Due for LC submission. Initialize min_price from nums[0], not 0.

Constraints: 1 <= prices.length <= 10⁵. 0 <= prices[i] <= 10⁴.

Examples:
- [7,1,5,3,6,4] → 5
- [7,6,4,3,1] → 0
- [1,2] → 1
- [3] → 0

Edge case before submitting: decreasing prices → 0.

Solve locally → If independent → Submit LC 121
Status: [ ] Independent  [ ] Hint  [ ] Failed
LC Result: [ ] Accepted  [ ] Wrong Answer  [ ] Not submitted
Time taken: ___

---

## New Problems → Solve locally only, DO NOT submit to LC

### N1. Top K Frequent Elements (LC 347) — Frequency Sorting
Last attempt needed syntax help. Today: sorting version only, no bucket. Lambda must fire from memory.

Constraints: 1 <= nums.length <= 10⁵. k is valid. Answer is unique.

Examples:
- [1,1,1,2,2,3], k=2 → [1,2]
- [1], k=1 → [1]
- [-1,-1,2,2,2,3], k=2 → [2,-1]
- [5,3,5,3,2], k=2 → [5,3] any order

Requirements:
- Build freq dict using .get()
- Sort by frequency descending with lambda
- Return first k keys
- Write complexity as O(n + m log m) where m = unique values

Status: [ ] Independent  [ ] Hint  [ ] Failed
Time taken: ___
Complexity written: Time = ___ Space = ___

---

### N2. Majority Element (LC 169) — Frequency Hashing
Due for LC. Today solve locally from scratch. Then move to LC submission queue for Day 10.

Constraints: n >= 1. Majority element always exists (appears > n//2 times).

Examples:
- [3,2,3] → 3
- [2,2,1,1,1,2,2] → 2
- [1] → 1
- [-1,-1,-1,2,3] → -1

Requirements:
- Dictionary frequency version only
- Second pass to find max frequency
- Do NOT use Counter or max() with key

Status: [ ] Independent  [ ] Hint  [ ] Failed
Time taken: ___

---

### N3. Running Sum of 1d Array (LC 1480) — Prefix Sum
Due for LC. Today: in-place version, O(1) space. Then move to LC queue for Day 10.

Constraints: 1 <= nums.length <= 1000. -10⁶ <= nums[i] <= 10⁶.

Examples:
- [1,2,3,4] → [1,3,6,10]
- [1,1,1,1,1] → [1,2,3,4,5]
- [-1,2,-3,4] → [-1,1,-2,2]
- [] → []

Requirements:
- In-place version (modify nums directly)
- O(1) extra space

Status: [ ] Independent  [ ] Hint  [ ] Failed
Time taken: ___

---

## Reflection (fill before closing — 6 fields)

```
Day Type: Reinforcement
Pattern Focus: Frequency Sorting / Complement Lookup

Revision results (R1-R4):
  Valid Anagram: Independent/Hint/Failed — LC: Accepted/Wrong/Not submitted
  Two Sum: Independent/Hint/Failed — LC: Accepted/Wrong/Not submitted
  First Unique: Independent/Hint/Failed — LC: Accepted/Wrong/Not submitted
  Best Stock: Independent/Hint/Failed — LC: Accepted/Wrong/Not submitted

New problem results (N1-N3):
  Top K: Independent/Hint/Failed
  Majority Element: Independent/Hint/Failed
  Running Sum: Independent/Hint/Failed

Concept warm-up recalled without notes: Frequency Sorting yes/no | Complement Lookup yes/no

Main mistake today:

Family stability update:
  Frequency Sorting: Shaky/Building (Top K sorting lambda recalled independently? yes/no)
  Complement Lookup: Building/Stable (Two Sum clean? yes/no)

Continue/Repeat/Slow down:
Reason:
```

---

## LC Submission Log for Today

| Problem | LC# | Local Result | LC Result |
|---------|-----|--------------|-----------|
| Valid Anagram | 242 | | |
| Two Sum | 1 | | |
| First Unique Character | 387 | | |
| Best Time Stock | 121 | | |

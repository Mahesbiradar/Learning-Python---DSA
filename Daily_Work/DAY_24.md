# Day 24 — June 21, 2026 — Full Revision + Gap Recovery

Focus: Complete Day 23 gaps, revise Sliding Window, and reinforce weak recall patterns.
Target: 18 questions
Rule: Attempt every question without notes first. If stuck for 15 minutes, mark `Hint`, learn the missing idea, then code it.

---

## Concept Warm-Up (15 min)

Write these from memory.

### 1. Prefix Sum + Hash Map

```python
# What does prefix_sum represent?
# What do we store in the map?
# When do we update the answer?
```

### 2. Sliding Window

```python
# left = 0
# for right in range(len(nums)):
#     add current item
#     while window is invalid:
#         remove nums[left]
#         left += 1
#     update answer
```

### 3. Two Pointers — In-place Write

```python
# write = 0 or 1?
# for read in range(?):
#     if current item is valid/new:
#         nums[write] = nums[read]
#         write += 1
# return write
```

---

# Session 1 — Finish Yesterday’s Gaps

## 1. Length of Last Word (LC 58)

Pattern: String Traversal

Edge cases:

```python
"Hello World"                       # 5
"   fly me   to   the moon  "       # 4
"a"                                 # 1
```

[ ] Independent  [ ] Hint  [ ] Submitted

---

## 2. Range Sum Query — Immutable (LC 303)

Pattern: Prefix Sum

Test:

```python
nums = [-2, 0, 3, -5, 2, -1]
sumRange(0, 2)  # 1
sumRange(2, 5)  # -1
sumRange(0, 5)  # -3
```

[ ] Independent  [ ] Hint  [ ] Submitted

---

## 3. Contiguous Array (LC 525)

Pattern: Prefix Sum + Hash Map

Key conversion:

```python
0 -> -1
1 -> +1
```

Test:

```python
[0, 1]                    # 2
[0, 1, 0]                 # 2
[0, 1, 1, 0, 1, 1, 1, 0] # 4
```

[ ] Independent  [ ] Hint  [ ] Submitted

---

# Session 2 — 24-Hour Recall: Yesterday’s New / Hint Problems

## 4. Unique Number of Occurrences (LC 1207)

Pattern: Frequency Hashing

```python
[1,2,2,1,1,3]             # True
[1,2]                     # False
```

[ ] Independent  [ ] Hint

---

## 5. Top K Frequent Words (LC 692)

Pattern: Frequency Sorting

Required sort order:

```text
frequency descending
word ascending
```

Test:

```python
["i","love","leetcode","i","love","coding"], 2
# ["i","love"]

["aaa","aa","a"], 1
# ["a"]
```

[ ] Independent  [ ] Hint

---

## 6. Two Sum (LC 1)

Pattern: Complement Lookup

Mental trigger:

```text
Store current number -> index
Search for target - current number
```

Test:

```python
[2,7,11,15], 9            # [0,1]
[3,2,4], 6                # [1,2]
[3,3], 6                  # [0,1]
```

[ ] Independent  [ ] Hint

---

## 7. Two Sum II — Sorted Array (LC 167)

Pattern: Two Pointers / Complement Lookup

Use the sorted property this time: left and right pointers.

Test:

```python
[2,7,11,15], 9            # [1,2]
[2,3,4], 6                # [1,3]
[-1,0], -1                # [1,2]
```

[ ] Independent  [ ] Hint

---

## 8. Contains Duplicate II (LC 219)

Pattern: Sliding Window + Set

Important order:

```text
check duplicate first
add current item
shrink if window is too large
```

Test:

```python
[1,2,3,1], 3              # True
[1,0,1,1], 1              # True
[1,2,3,1,2,3], 2          # False
```

[ ] Independent  [ ] Hint

---

## 9. Remove Duplicates from Sorted Array (LC 26)

Pattern: Two Pointers + In-place Overwrite

Test:

```python
[1,1,2]                   # return 2; first values become [1,2]
[0,0,1,1,1,2,2,3,3,4]    # return 5; first values become [0,1,2,3,4]
[]                        # return 0
```

[ ] Independent  [ ] Hint

---

## 10. Remove Element (LC 27)

Pattern: Two Pointers + In-place Overwrite

Test:

```python
[3,2,2,3], 3             # return 2
[0,1,2,2,3,0,4,2], 2    # return 5
```

[ ] Independent  [ ] Hint

---

# Session 3 — Sliding Window Recall

## 11. Longest Substring Without Repeating Characters (LC 3)

Pattern: Sliding Window + Set

```python
"abcabcbb"                # 3
"bbbbb"                   # 1
"pwwkew"                  # 3
```

[ ] Independent  [ ] Hint

---

## 12. Minimum Size Subarray Sum (LC 209)

Pattern: Sliding Window

```python
target = 7, nums = [2,3,1,2,4,3]  # 2
target = 4, nums = [1,4,4]        # 1
target = 11, nums = [1,1,1,1,1]   # 0
```

[ ] Independent  [ ] Hint

---

## 13. Longest Repeating Character Replacement (LC 424)

Pattern: Sliding Window + Frequency Map

```python
s = "ABAB", k = 2         # 4
s = "AABABBA", k = 1      # 4
```

[ ] Independent  [ ] Hint

---

## 14. Permutation in String (LC 567)

Pattern: Fixed-Size Sliding Window + Frequency Map

```python
s1 = "ab", s2 = "eidbaooo"      # True
s1 = "ab", s2 = "eidboaoo"      # False
```

[ ] Independent  [ ] Hint

---

## 15. Find All Anagrams in a String (LC 438)

Pattern: Fixed-Size Sliding Window + Frequency Map

```python
s = "cbaebabacd", p = "abc"     # [0,6]
s = "abab", p = "ab"            # [0,1,2]
```

[ ] Independent  [ ] Hint

---

# Session 4 — Other Shaky Recall

## 16. Subarray Sum Equals K (LC 560)

Pattern: Prefix Sum + Hash Map

Mental trigger:

```text
needed prefix = current_sum - k
```

Test:

```python
[1,1,1], 2                # 2
[1,2,3], 3                # 2
[1,-1,0], 0               # 3
```

[ ] Independent  [ ] Hint

---

## 17. Isomorphic Strings (LC 205)

Pattern: Two-Way Hash Map

```python
"egg", "add"              # True
"foo", "bar"              # False
"badc", "baba"            # False
```

[ ] Independent  [ ] Hint

---

## 18. Maximum Product Subarray (LC 152)

Pattern: Running-State Tracking

Remember: a negative number can swap the role of current maximum and current minimum.

```python
[2,3,-2,4]                # 6
[-2,0,-1]                 # 0
[-2,3,-4]                 # 24
```

[ ] Independent  [ ] Hint

---

# Daily Summary

```text
Finish gaps:
58, 303, 525

24-hour recall:
1207, 692, 1, 167, 219, 26, 27

Sliding Window:
3, 209, 424, 567, 438

Shaky recall:
560, 205, 152

Total: 18 questions
```

---

# Scoring

```text
15–18 independent = Excellent revision day
12–14 independent = Good; one focused recall block tomorrow
Below 12 independent = repeat weak families before new topics
```

---

After each solution, add:

```text
# Status: Independent / Hint / Failed
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# mistakes/confusion: [note or NA]
# Pattern: [pattern name]
```

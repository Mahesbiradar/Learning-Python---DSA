# Day 16 — May 22, 2026 — Reinforcement

Focus: Sliding Window + 7d Recall Blitz
LC target today: Running Sum (1480) + Maximum Average Subarray I (643) if both feel effortless

---

## Concept Warm-Up (5 min)

Write both Sliding Window templates from memory. No notes.

```python
# Fixed-Size Sliding Window


```

```python
# Variable-Size Sliding Window


```

---

## Revision Problems (5 problems)

### Maximum Average Subarray I (LC 643)

Pattern: Sliding Window (Fixed Window)
Due: 24h recall
Constraint: 1 <= k <= nums.length <= 10^5; -10^4 <= nums[i] <= 10^4.
Goal: Solve independently. Focus on:

* when window becomes valid,
* why `right >= k-1`,
* why subtraction maintains window size.
  [ ] Solved independently
  [ ] Needed hint (note what)
  [ ] Submitted to LC — Result: ___

---

### Longest Substring Without Repeating Characters (LC 3)

Pattern: Sliding Window (Variable Window)
Due: 24h recall
Constraint: 0 <= s.length <= 5 * 10^4; English letters, digits, symbols, spaces.
Goal: Solve independently. Focus on:

* shrinking while duplicate exists,
* why `while` is required,
* maintaining validity.
  [ ] Solved independently
  [ ] Needed hint (note what)
  [ ] Submitted to LC — Result: ___

---

### Minimum Size Subarray Sum (LC 209)

Pattern: Sliding Window (Variable Window)
Due: 24h recall
Constraint: 1 <= target <= 10^9; 1 <= nums.length <= 10^5.
Goal: Solve independently. Focus on:

* `sum >= target`,
* why shrinking happens repeatedly,
* why total complexity is O(n).
  [ ] Solved independently
  [ ] Needed hint (note what)
  [ ] Submitted to LC — Result: ___

---

### Two Sum (LC 1)

Pattern: Complement Lookup
Due: 7d final recall
Constraint: exactly one valid answer exists.
Goal: One-pass hash map from memory. No tracing needed.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

### Valid Anagram (LC 242)

Pattern: Frequency Hashing
Due: 7d final recall
Constraint: lowercase English letters only.
Goal: Solve in under 5 minutes from memory.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

## New Problems (3 problems, local only)

### Longest Repeating Character Replacement (LC 424)

Pattern: Sliding Window (Variable Window)
Difficulty: Medium

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing at most `k` replacements.

Example 1:
Input: s = "ABAB", k = 2
Output: 4

Example 2:
Input: s = "AABABBA", k = 1
Output: 4

Constraints:

* 1 <= s.length <= 10^5
* s consists of only uppercase English letters.
* 0 <= k <= s.length

Key insight:
Window is valid if:

```python
window_size - max_frequency <= k
```

---

### Permutation in String (LC 567)

Pattern: Sliding Window + Frequency Hashing
Difficulty: Medium

Given two strings `s1` and `s2`, return `True` if `s2` contains a permutation of `s1`, or `False` otherwise.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: True

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: False

Constraints:

* 1 <= s1.length, s2.length <= 10^4
* s1 and s2 consist of lowercase English letters.

Key insight:
Fixed-size window of length `len(s1)`.

---

### Fruits Into Baskets (LC 904)

Pattern: Sliding Window (Variable Window)
Difficulty: Medium

You are visiting a farm with a row of fruit trees represented by an integer array `fruits`.

You have two baskets, and each basket can hold only one type of fruit. You may start at any tree, but must pick exactly one fruit from every tree while moving right.

Return the maximum number of fruits you can collect.

Example 1:
Input: fruits = [1,2,1]
Output: 3

Example 2:
Input: fruits = [0,1,2,2]
Output: 3

Example 3:
Input: fruits = [1,2,3,2,2]
Output: 4

Constraints:

* 1 <= fruits.length <= 10^5
* 0 <= fruits[i] < fruits.length

Key insight:
Window valid only while unique fruit types <= 2.

---

Note: After solving each problem in your .py file, log these comment fields:

```python
# Status: Independent / Hint / Failed
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# mistakes/confusion: [note or NA]
# Pattern: [pattern name]
```

Prompt 1 reads these directly — no separate reflection needed.

Based on your current STATUS tracker, Sliding Window is still in Building stage and needs repeated recall before introducing Binary Search. 

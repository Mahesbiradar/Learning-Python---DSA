# Day 17 — May 23, 2026 — Reinforcement
Focus: Sliding Window (24h recall — 424, 567, 904) + Sliding Window depth extension
LC target today: Submit 424, 567, 904 only if today's recall is fully independent — no pressure otherwise

---

## Concept Warm-Up (5 min)
Write both Sliding Window templates from memory. No notes. No peeking at yesterday.

```python
# Fixed-size sliding window (size k)




```

```python
# Variable-size sliding window




```

---

## Revision Problems (5 problems)

### Longest Repeating Character Replacement (LC 424)
Pattern: Sliding Window
Due: 24h revision — hint-needed D16
Constraint: 1 <= s.length <= 10^5; s consists of only uppercase English letters; 0 <= k <= s.length.
Goal: Recall the key invariant from memory: `window_size - max_frequency <= k`. Solve fully independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Permutation in String (LC 567)
Pattern: Sliding Window + Frequency Hashing
Due: 24h revision — hint-needed D16
Constraint: 1 <= s1.length, s2.length <= 10^4; both strings consist of lowercase English letters.
Goal: Recall the fixed-window frequency-matching approach independently. Focus on: when to delete a key vs set to 0.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Fruits Into Baskets (LC 904)
Pattern: Sliding Window
Due: 24h revision — hint-needed D16
Constraint: 1 <= fruits.length <= 10^5; 0 <= fruits[i] < fruits.length.
Goal: Recall the "at most 2 distinct" shrink condition independently. Focus on: when to delete a key from the map.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Group Anagrams (LC 49)
Pattern: Grouping Hash Maps
Due: 7d final recall (due May 24 — pull early)
Constraint: 1 <= strs.length <= 10^4; 0 <= strs[i].length <= 100; strs[i] consists of lowercase English letters.
Goal: Reproduce the sorted-key grouping approach independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Find Pivot Index (LC 724)
Pattern: Prefix Sum
Due: 7d final recall (due May 24 — pull early)
Constraint: 1 <= nums.length <= 10^4; -1000 <= nums[i] <= 1000.
Goal: Recall the `left_sum == total - left_sum - nums[i]` invariant independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

## New Problems (3 problems, local only)
Do NOT submit to LC. Solve locally first.
All three extend Sliding Window into new constraint shapes.

### Max Consecutive Ones III (LC 1004)
Pattern: Sliding Window
Difficulty: Medium
Given a binary array `nums` and an integer `k`, return the maximum number of consecutive 1s in the array if you can flip at most `k` 0s.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: Flip the two 0s at index 5 and 10. The longest run of 1s is [1,1,1,0,0,1,1,1,1,1] with length 6 (indices 0–5 after flipping index 5).

Wait — correct explanation: flip positions 4 and 5 → [1,1,1,0,1,1,1,1,1,1,0]. Longest = 6. Actually the answer is bold: `[1,1,1,0,0,**1,1,1,1,1**]` — flip indices 4,10 → run of 6. Just trust the output: 6.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
- 0 <= k <= nums.length

Hint if stuck: Variable-size window. Track the count of zeros inside the window. Window is valid while `zeros_in_window <= k`. Shrink from left when zeros exceed k.

### Find All Anagrams in a String (LC 438)
Pattern: Sliding Window + Frequency Hashing
Difficulty: Medium
Given two strings `s` and `p`, return a list of all the start indices of `p`'s anagrams in `s`. You may return the answer in any order.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0, 6]
Explanation: The substring starting at index 0 is "cba" which is an anagram of "abc". The substring starting at index 6 is "bac" which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0, 1, 2]

Constraints:
- 1 <= s.length, p.length <= 3 * 10^4
- s and p consist of lowercase English letters.

Hint if stuck: Fixed-size window of length `len(p)` over `s`. Maintain a frequency map of the current window. When window size exceeds `len(p)`, remove the leftmost character (delete key if count reaches 0). Compare window map to `p` map — if equal, append `left` to result.

### Contains Duplicate II (LC 219)
Pattern: Sliding Window
Difficulty: Easy
Given an integer array `nums` and an integer `k`, return `True` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: True

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: True

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: False

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 0 <= k <= 10^5

Hint if stuck: Fixed-size sliding window using a set of size at most k+1. For each new element: check if it's already in the set (duplicate within k distance) → return True. Add it, then if set size exceeds k, remove the oldest element (`nums[right - k]`).

---

Note: After solving each problem in your .py file, log these comment fields:
  # Status: Independent / Hint / Failed
  # Time complexity: O(?)
  # Space complexity: O(?)
  # LC status: Accepted / NA / Not submitted
  # mistakes/confusion: [note or NA]
  # Pattern: [pattern name]
Prompt 1 reads these directly — no separate reflection needed.

# Day 21 — May 27, 2026 — Reinforcement
Focus: Binary Search (24h recall + depth) + overdue recall blitz
LC target today: Sqrt(x) (69), Find Smallest Letter Greater Than Target (744), Find Peak Element (162) — only if 24h recall passes independently

---

## Concept Warm-Up (5 min)
Write the Binary Search lower-bound template from memory. No notes.
Focus on `left < right` loop condition and when to use `right = mid` vs `left = mid + 1`.

```python
# Lower-bound Binary Search (left < right)






```

---

## Revision Problems (5 problems)

### Group Anagrams (LC 49)
Pattern: Grouping Hash Maps
Due: 14d recall — OVERDUE 2 days (was due May 24)
Constraint: 1 <= strs.length <= 10^4; 0 <= strs[i].length <= 100
Goal: Hash map with sorted tuple key. Group strings by character frequency signature. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Find Highest Altitude (LC 1732)
Pattern: Prefix Sum
Due: 7d final recall — OVERDUE 1 day (was due May 25)
Constraint: n == gain.length; 1 <= n <= 100; -100 <= gain[i] <= 100
Goal: Running prefix sum starting at 0, track max altitude encountered. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Sqrt(x) (LC 69)
Pattern: Binary Search
Due: 24h revision — May 27
Constraint: 0 <= x <= 2^31 - 1
Goal: Lower-bound binary search. Predicate: mid*mid <= x. Track best valid mid. Use `left <= right` or `left < right` with best tracker. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Find Smallest Letter Greater Than Target (LC 744)
Pattern: Binary Search
Due: 24h revision — May 27
Constraint: 2 <= letters.length <= 10^4; sorted non-decreasing; at least two different characters
Goal: Lower-bound variant — find first element > target. If none found, wrap to letters[0]. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Find Peak Element (LC 162)
Pattern: Binary Search
Due: 24h revision — May 27
Constraint: 1 <= nums.length <= 1000; nums[i] != nums[i+1]
Goal: Compare mid with mid+1. If ascending, peak is right; else peak is left (including mid). `left < right`, return left. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

## New Problems (3 problems, local only)

### Valid Perfect Square (LC 367)
Pattern: Binary Search
Difficulty: Easy

Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in exponent function or operator.

Example 1:
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:
Input: num = 14
Output: false
Explanation: We return false because 3.741 * 3.741 = 14 and 3.741 is not an integer.

Constraints:
- 1 <= num <= 2^31 - 1

---

### Arranging Coins (LC 441)
Pattern: Binary Search
Difficulty: Easy

You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Example 1:
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

Example 2:
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.

Constraints:
- 1 <= n <= 2^31 - 1

---

### Guess Number Higher or Lower (LC 374)
Pattern: Binary Search
Difficulty: Easy

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:
- -1: Your guess is higher than the number I picked (i.e. num > pick).
- 1: Your guess is lower than the number I picked (i.e. num < pick).
- 0: Your guess is equal to the number I picked (i.e. num == pick).

Return the number that I picked.

Example 1:
Input: n = 10, pick = 6
Output: 6

Example 2:
Input: n = 1, pick = 1
Output: 1

Example 3:
Input: n = 2, pick = 1
Output: 1

Constraints:
- 1 <= n <= 2^31 - 1
- 1 <= pick <= n

---

Note: After solving each problem in your .py file, log these comment fields:
  # Status: Independent / Hint / Failed
  # Time complexity: O(?)
  # Space complexity: O(?)
  # LC status: Accepted / NA / Not submitted
  # mistakes/confusion: [note or NA]
  # Pattern: [pattern name]
Prompt 1 reads these directly — no separate reflection needed.

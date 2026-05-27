# Day 20 — May 26, 2026 — Reinforcement
Focus: Binary Search (24h recall) + Overdue Recall Blitz
LC target today: Binary Search (704), Search Insert Position (35) — optional, only if 24h recall passes independently

---

## Concept Warm-Up (5 min)
Write the Binary Search template from memory. No notes.
Focus specifically on the loop condition (`left <= right` vs `left < right`) and the mid-calculation overflow guard.

```python
# Binary Search — standard template






```

---

## Revision Problems (5 problems)

### Product of Array Except Self (LC 238)
Pattern: Prefix Sum
Due: 7d final recall — overdue May 24
Constraint: 2 <= nums.length <= 10^5; -30 <= nums[i] <= 30; product of any prefix or suffix fits in 32-bit int.
Goal: Two-pass approach — left products + right products. No division allowed. Reproduce in under 3 minutes.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Maximum Average Subarray I (LC 643)
Pattern: Sliding Window
Due: 3d recall — overdue May 25
Constraint: 1 <= k <= n <= 10^5.
Goal: Fixed window of size k. Track window sum, update max average. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Binary Search (LC 704)
Pattern: Binary Search
Due: 24h revision — May 26
Constraint: 1 <= nums.length <= 10^4; nums sorted ascending; all unique.
Goal: Standard template — `left <= right`, `mid = left + (right - left) // 2`, return -1 if not found.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Search Insert Position (LC 35)
Pattern: Binary Search
Due: 24h revision — May 26
Constraint: 1 <= nums.length <= 10^4; distinct values sorted ascending.
Goal: Lower-bound variant — `left < right`, post-loop return `left`. Handle insert-at-end case.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### First Bad Version (LC 278)
Pattern: Binary Search
Due: 24h revision — May 26
Constraint: 1 <= bad <= n <= 2^31 - 1.
Goal: Lower-bound on predicate — `left < right`, `right = mid` when bad, `left = mid + 1` when good. Minimize API calls.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

## New Problems (3 problems, local only)

### Sqrt(x) (LC 69)
Pattern: Binary Search
Difficulty: Easy

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Constraints:
- 0 <= x <= 2^31 - 1

---

### Find Smallest Letter Greater Than Target (LC 744)
Pattern: Binary Search
Difficulty: Easy

You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

Example 1:
Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

Example 2:
Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

Example 3:
Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that are lexicographically greater than 'z', so we return letters[0].

Constraints:
- 2 <= letters.length <= 10^4
- letters[i] is a lowercase English letter
- letters is sorted in non-decreasing order
- letters contains at least two different characters

---

### Find Peak Element (LC 162)
Pattern: Binary Search
Difficulty: Easy

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

Constraints:
- 1 <= nums.length <= 1000
- -2^31 <= nums[i] <= 2^31 - 1
- nums[i] != nums[i + 1] for all valid i

---

Note: After solving each problem in your .py file, log these comment fields:
  # Status: Independent / Hint / Failed
  # Time complexity: O(?)
  # Space complexity: O(?)
  # LC status: Accepted / NA / Not submitted
  # mistakes/confusion: [note or NA]
  # Pattern: [pattern name]
Prompt 1 reads these directly — no separate reflection needed.

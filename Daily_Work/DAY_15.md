# Day 15 - May 21, 2026 - Learning
Focus: Sliding Window + recall cleanup
LC target today: None mandatory - all listed LC problems are already accepted; use LC only if a revision feels effortless

---

## Concept Warm-Up (5 min)
Write the Sliding Window template from memory. No notes.

```python
# Fixed-size sliding window



```

```python
# Variable-size sliding window



```

## Sliding Window Concept Block

### Trigger words
- Contiguous subarray or substring
- Longest / shortest / maximum / minimum window
- At most / at least / exactly K
- Repeated characters, distinct characters, target sum, average over length K

### Mental model
Maintain a window between `left` and `right`.
Expand with `right` to include new elements.
Shrink with `left` when the window becomes invalid or too large.
Update the answer only when the window is valid for the problem.

### Fixed-size template

```python
window_sum = 0
best = float("-inf")

for right in range(len(nums)):
    window_sum += nums[right]

    if right >= k:
        window_sum -= nums[right - k]

    if right >= k - 1:
        best = max(best, window_sum)
```

Time complexity: O(n)
Space complexity: O(1)

### Variable-size template

```python
left = 0
best = 0
state = {}

for right in range(len(items)):
    # add items[right] to state

    while window_is_invalid:
        # remove items[left] from state
        left += 1

    best = max(best, right - left + 1)
```

Time complexity: O(n), because each pointer moves forward at most n times.
Space complexity: O(k) or O(n), depending on what the window stores.

## Revision Problems (5 problems)

### Product of Array Except Self (LC 238)
Pattern: Prefix Sum
Due: 3d recall
Constraint: 2 <= nums.length <= 10^5; answer fits in 32-bit integer; solve without division in O(n).
Goal: Solve independently. If confident -> submit to LC after.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC - Result: ___

### Find Highest Altitude (LC 1732)
Pattern: Prefix Sum
Due: 3d recall
Constraint: 1 <= gain.length <= 100; altitude starts at 0.
Goal: Solve independently. If confident -> submit to LC after.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC - Result: ___

### Isomorphic Strings (LC 205)
Pattern: Grouping Hash Maps
Due: 3d recall
Constraint: 1 <= s.length <= 5 * 10^4; s and t have equal length and contain valid ASCII characters.
Goal: Solve independently. If confident -> submit to LC after.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC - Result: ___

### Two Sum (LC 1)
Pattern: Complement Lookup
Due: 7d final recall
Constraint: 2 <= nums.length <= 10^4; exactly one valid answer exists; do not use the same element twice.
Goal: Solve independently. If confident -> submit to LC after.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC - Result: ___

### Valid Anagram (LC 242)
Pattern: Frequency Hashing
Due: 7d final recall
Constraint: 1 <= s.length, t.length <= 5 * 10^4; strings contain lowercase English letters.
Goal: Solve independently. If confident -> submit to LC after.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC - Result: ___

## New Problems (3 problems, local only)
Do NOT submit to LC. Solve locally first.

### Maximum Average Subarray I (LC 643)
Pattern: Sliding Window
Difficulty: Easy
Given an integer array `nums` and an integer `k`, find the contiguous subarray of length `k` with the maximum average value. Return that maximum average.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: The best window is [12,-5,-6,50], whose average is 51 / 4 = 12.75.

Example 2:
Input: nums = [5], k = 1
Output: 5.0

Constraints:
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

### Longest Substring Without Repeating Characters (LC 3)
Pattern: Sliding Window
Difficulty: Medium
Given a string `s`, return the length of the longest substring that contains no repeated characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: "abc" is a longest substring without repeated characters.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: "b" is the longest valid substring.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: "wke" is a longest valid substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s may contain letters, digits, symbols, and spaces.

### Minimum Size Subarray Sum (LC 209)
Pattern: Sliding Window
Difficulty: Medium
Given an array of positive integers `nums` and a positive integer `target`, return the length of the smallest contiguous subarray whose sum is at least `target`. Return 0 if no such subarray exists.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: [4,3] is the shortest valid subarray.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4

---

Note: After solving each problem in your .py file, log these comment fields:
  # Status: Independent / Hint / Failed
  # Time complexity: O(?)
  # Space complexity: O(?)
  # LC status: Accepted / NA / Not submitted
  # mistakes/confusion: [note or NA]
  # Pattern: [pattern name]
Prompt 1 reads these directly - no separate reflection needed.
---

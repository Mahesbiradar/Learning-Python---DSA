# Day 19 — May 27, 2026 — Learning
Focus: Binary Search (new pattern) + Retrieval (overdue 7d/3d recalls)
LC target today: Optional — re-submit any previously Accepted problem for speed practice

---

## Concept Warm-Up (5 min)
Write the Binary Search template from memory. No notes.
Focus specifically on the loop condition (`left <= right` vs `left < right`) and the mid-calculation overflow guard.

```python
# Binary Search — standard template





```

---

## New Pattern — Binary Search

### Mental Model
Binary search halves the search space every iteration. The invariant: the target (if it exists) is always within the current `[left, right]` bounds.

### Trigger Words
- "sorted array"
- "find position / index"
- "first occurrence / last occurrence"
- "minimum maximum" or "maximum minimum"
- "search in O(log n)"

### Template
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2   # overflow-safe
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1   # not found
```

### Key Decisions
| Decision | Standard search | Lower bound | Upper bound |
|----------|----------------|-------------|-------------|
| Loop condition | `left <= right` | `left < right` | `left < right` |
| Return on match | `return mid` | `right = mid` | `left = mid + 1` |
| Pointer move (mid < target) | `left = mid + 1` | `left = mid + 1` | `left = mid + 1` |
| Pointer move (mid > target) | `right = mid - 1` | `right = mid` | `right = mid - 1` |
| Post-loop return | `-1` | `left` (insert position) | `right` |

### Time/Space Complexity
- Time: O(log n)
- Space: O(1) iterative, O(log n) recursive

---

## Revision Problems (5 problems)

### First Unique Character in a String (LC 387)
Pattern: Frequency Hashing
Due: 7d final recall — overdue May 25
Constraint: 1 <= s.length <= 10^5; s consists of only lowercase English letters.
Goal: One-pass frequency dict + second-pass index check. Reproduce in under 3 minutes.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Best Time to Buy and Sell Stock (LC 121)
Pattern: Running-State Tracking
Due: 7d final recall — overdue May 25
Constraint: 1 <= prices.length <= 10^5; 0 <= prices[i] <= 10^4.
Goal: Track min_price and max_profit in one pass. Kadane-style state transition.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Running Sum of 1d Array (LC 1480)
Pattern: Prefix Sum
Due: 7d final recall — overdue May 25
Constraint: 1 <= nums.length <= 1000; -10^6 <= nums[i] <= 10^6.
Goal: In-place or new array — both O(n). Verify edge case: length 1.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Longest Repeating Character Replacement (LC 424)
Pattern: Sliding Window
Due: 3d recall — due May 26
Constraint: 1 <= s.length <= 10^5; 0 <= k <= s.length; s consists of only uppercase English letters.
Goal: Variable window — `max_freq` tracks dominant char, `window_len - max_freq <= k` is the invariant. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Permutation in String (LC 567)
Pattern: Sliding Window
Due: 3d recall — due May 26
Constraint: 1 <= s1.length, s2.length <= 10^4; both lowercase English letters.
Goal: Fixed window of `len(s1)`, frequency map comparison. Focus: delete key when count hits 0.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

## New Problems (3 problems, local only)

### Binary Search (LC 704)
Pattern: Binary Search
Difficulty: Easy

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in `nums` are unique.
- `nums` is sorted in ascending order.

---

### Search Insert Position (LC 35)
Pattern: Binary Search
Difficulty: Easy

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- `nums` contains distinct values sorted in ascending order.
- -10^4 <= target <= 10^4

---

### First Bad Version (LC 278)
Pattern: Binary Search
Difficulty: Easy

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1

Constraints:
- 1 <= bad <= n <= 2^31 - 1

---

Note: After solving each problem in your .py file, log these comment fields:
  # Status: Independent / Hint / Failed
  # Time complexity: O(?)
  # Space complexity: O(?)
  # LC status: Accepted / NA / Not submitted
  # mistakes/confusion: [note or NA]
  # Pattern: [pattern name]
Prompt 1 reads these directly — no separate reflection needed.

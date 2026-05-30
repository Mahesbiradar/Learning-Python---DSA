# Day 22 — May 28, 2026 — Consolidation
Focus: Overdue blitz + due-today clear — ALL backlog problems
LC target today: None — pure backlog clearance day

---

## Concept Warm-Up (5 min)
Write the Sliding Window template from memory. No notes.
Include both fixed-size and variable-size variants.

```python
# Fixed-size Sliding Window






# Variable-size Sliding Window






```

---

## Revision Problems — OVERDUE (9 problems)

### Find Pivot Index (LC 724)
Pattern: Prefix Sum
Due: 14d recall — OVERDUE 4 days (was due May 24)
Constraint: 1 <= nums.length <= 10^4; -1000 <= nums[i] <= 1000
Goal: Running prefix sum. At each index, left sum equals total sum minus left sum minus current element. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Sort Characters By Frequency (LC 451)
Pattern: Frequency Sorting
Due: 14d recall — OVERDUE 4 days (was due May 24)
Constraint: 1 <= s.length <= 5 * 10^5; s consists of uppercase and lowercase English letters and digits
Goal: Count frequencies, sort by frequency descending, reconstruct string. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Intersection of Two Arrays II (LC 350)
Pattern: Frequency Hashing
Due: 14d recall — OVERDUE 4 days (was due May 24)
Constraint: 1 <= nums1.length, nums2.length <= 1000; 0 <= nums1[i], nums2[i] <= 1000
Goal: Hash map frequency count of smaller array, iterate larger array and decrement. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Isomorphic Strings (LC 205)
Pattern: Grouping Hash Maps
Due: 7d final recall — OVERDUE 3 days (was due May 25)
Constraint: 1 <= s.length <= 5 * 10^4; t.length == s.length; s and t consist of any valid ascii character
Goal: Two hash maps — s→t mapping and t→s mapping. Verify bijection at each character. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Longest Substring Without Repeating Characters (LC 3)
Pattern: Sliding Window
Due: 3d recall — OVERDUE 3 days (was due May 25)
Constraint: 0 <= s.length <= 5 * 10^4
Goal: Variable window with hash set for uniqueness. Expand right, shrink left until duplicate removed. Track max length. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Minimum Size Subarray Sum (LC 209)
Pattern: Sliding Window
Due: 3d recall — OVERDUE 3 days (was due May 25)
Constraint: 1 <= target <= 10^9; 1 <= nums.length <= 10^5; 1 <= nums[i] <= 10^4
Goal: Variable window — expand right, shrink left while sum >= target. Track min length. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Fruits Into Baskets (LC 904)
Pattern: Sliding Window
Due: 3d recall — OVERDUE 2 days (was due May 26)
Constraint: 1 <= fruits.length <= 10^5; 0 <= fruits[i] < fruits.length
Goal: Variable window — at most 2 distinct fruit types. Hash map count, shrink when > 2 types. Track max length. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Subarray Sum Equals K (LC 560)
Pattern: Prefix Sum
Due: 7d final recall — OVERDUE 2 days (was due May 26)
Constraint: 1 <= nums.length <= 2 * 10^4; -1000 <= nums[i] <= 1000; -10^7 <= k <= 10^7
Goal: Hash map of prefix sum frequencies. At each step, check if current_sum - k exists in map. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Maximum Subarray (LC 53)
Pattern: Running-State Tracking
Due: 7d final recall — OVERDUE 2 days (was due May 26)
Constraint: 1 <= nums.length <= 10^5; -10^4 <= nums[i] <= 10^4
Goal: Kadane's algorithm — at each step, max_ending_here = max(nums[i], max_ending_here + nums[i]). Track global max. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

## Revision Problems — DUE TODAY (12 problems)

### Valid Palindrome (LC 125)
Pattern: Two Pointers
Due: 14d recall — May 28
Constraint: 1 <= s.length <= 2 * 10^5; s consists only of printable ASCII characters
Goal: Two pointers from ends, skip non-alphanumeric, compare lowercase chars. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Reverse String (LC 344)
Pattern: Two Pointers
Due: 14d recall — May 28
Constraint: 1 <= s.length <= 10^5; s[i] is a printable ascii character
Goal: In-place swap with two pointers from ends moving inward. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Is Subsequence (LC 392)
Pattern: Two Pointers
Due: 14d recall — May 28
Constraint: 0 <= s.length <= 100; 0 <= t.length <= 10^4; s and t consist only of lowercase English letters
Goal: Two pointers — advance t pointer always, advance s pointer only on match. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Top K Frequent Elements (LC 347)
Pattern: Frequency Sorting
Due: 14d recall — May 28
Constraint: 1 <= nums.length <= 10^5; -10^4 <= nums[i] <= 10^4; k is in range [1, number of unique elements]
Goal: Frequency map + heap/sort to get top k. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Majority Element (LC 169)
Pattern: Frequency Hashing
Due: 14d recall — May 28
Constraint: n == nums.length; 1 <= n <= 5 * 10^4; -10^9 <= nums[i] <= 10^9
Goal: Boyer-Moore voting or hash map. Majority appears > n/2 times. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Max Consecutive Ones III (LC 1004)
Pattern: Sliding Window
Due: 3d recall — May 28
Constraint: 1 <= nums.length <= 10^5; nums[i] is either 0 or 1; 0 <= k <= nums.length
Goal: Variable window — at most k zeros flipped. Track max window length. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Find All Anagrams in a String (LC 438)
Pattern: Sliding Window
Due: 3d recall — May 28
Constraint: 1 <= s.length, p.length <= 3 * 10^4; s and p consist of lowercase English letters
Goal: Fixed window of len(p). Hash map frequency match for anagram. Slide and update counts. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Contains Duplicate II (LC 219)
Pattern: Sliding Window
Due: 3d recall — May 28
Constraint: 1 <= nums.length <= 10^5; -10^9 <= nums[i] <= 10^9; 0 <= k <= 10^5
Goal: Hash set of last k elements. Check if current element exists in set. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Maximum Product Subarray (LC 152)
Pattern: Running-State Tracking
Due: 7d final recall — May 28
Constraint: 1 <= nums.length <= 2 * 10^4; -10 <= nums[i] <= 10
Goal: Track both max and min ending at each position (negative flips). Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Valid Perfect Square (LC 367)
Pattern: Binary Search
Due: 24h revision — May 28
Constraint: 1 <= num <= 2^31 - 1
Goal: Binary search — mid*mid == num. Use `left <= right` loop. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Arranging Coins (LC 441)
Pattern: Binary Search
Due: 24h revision — May 28
Constraint: 1 <= n <= 2^31 - 1
Goal: Binary search on k — sum of 1..k = k(k+1)/2 <= n. Find max k. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Guess Number Higher or Lower (LC 374)
Pattern: Binary Search
Due: 24h revision — May 28
Constraint: 1 <= n <= 2^31 - 1; 1 <= pick <= n
Goal: Standard binary search using guess() API. `left <= right`, adjust based on -1/1/0. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

## New Problems (0 problems)
Consolidation day — zero new problems. 21 revision slots total. Solve as many as you can. Prioritize overdue items first.
Sliding Window family has been flagged Shaky for 6+ consecutive days. Backlog clearance is the only priority today.

---

Note: After solving each problem in your .py file, log these comment fields:
  # Status: Independent / Hint / Failed
  # Time complexity: O(?)
  # Space complexity: O(?)
  # LC status: Accepted / NA / Not submitted
  # mistakes/confusion: [note or NA]
  # Pattern: [pattern name]
Prompt 1 reads these directly — no separate reflection needed.

# Day 10 — May 16, 2026 — Reinforcement
Focus: Prefix Sum + Running-State Tracking
LC target today: Valid Palindrome (125), Reverse String (344), Majority Element (169), Top K Frequent (347) — only if independent ✓

---

## Concept Warm-Up (5 min)
Write the Prefix Sum template from memory. No notes.

```python
# Prefix Sum — build array where prefix[i] = sum of nums[0..i-1]


```

---

## Revision Problems (5 problems)

### Valid Palindrome (LC 125)
Pattern: Two Pointers
Due: overdue (May 15)
Constraint: Only alphanumeric chars count. Case-insensitive. Empty string → True.
Examples: "A man, a plan, a canal: Panama" → True | "race a car" → False | " " → True
Goal: Two-pointer from both ends, skip non-alphanumeric, compare lowercased.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

### Reverse String (LC 344)
Pattern: Two Pointers
Due: overdue (May 15)
Constraint: In-place. O(1) extra memory. Modify input array directly.
Examples: ["h","e","l","l","o"] → ["o","l","l","e","h"] | ["H","a","n","n","a","h"] → ["h","a","n","n","a","H"]
Goal: Two-pointer swap from both ends moving inward.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

### Is Subsequence (LC 392)
Pattern: Two Pointers
Due: overdue (May 15)
Constraint: 0 <= s.length <= 100, 0 <= t.length <= 10^4. All lowercase.
Examples: s="abc", t="ahbgdc" → True | s="axc", t="ahbgdc" → False | s="", t="anything" → True
Goal: Two pointers — crawl t with one pointer, advance s-pointer only on match. Return s-pointer == len(s).
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

### Top K Frequent Elements (LC 347)
Pattern: Frequency Sorting
Due: May 16 (24h recall)
Constraint: 1 <= nums.length <= 10^5. k is always valid. Answer is unique.
Examples: [1,1,1,2,2,3], k=2 → [1,2] | [1], k=1 → [1]
Goal: Build freq dict with .get(), sort by frequency descending with lambda, return first k keys.
Write complexity: Time = O(n + m log m), Space = O(n) where m = unique values.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

### Majority Element (LC 169)
Pattern: Frequency Hashing
Due: May 16 (24h recall)
Constraint: n >= 1. Majority element always exists (appears > n//2 times).
Examples: [3,2,3] → 3 | [2,2,1,1,1,2,2] → 2 | [1] → 1
Goal: Dict frequency version. Second pass over dict to find max. Do NOT use Counter or max() with key.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

## New Problems (3 problems — local only, do NOT submit to LC)

### Product of Array Except Self (LC 238)
Pattern: Prefix Sum (prefix × suffix products)
Difficulty: Medium
Constraints: 2 <= nums.length <= 10^5. -30 <= nums[i] <= 30. Product fits in 32-bit int. No division allowed.

Description: Given an integer array nums, return an array answer such that answer[i] equals the product of all elements of nums except nums[i].

Examples:
- [1,2,3,4] → [24,12,8,6]
- [-1,1,0,-3,3] → [0,0,9,0,0]

Hint (read only if stuck): Two passes. Left pass builds prefix products. Right pass multiplies in suffix products in-place.

---

### Subarray Sum Equals K (LC 560)
Pattern: Prefix Sum + Hash Map
Difficulty: Medium
Constraints: 1 <= nums.length <= 2×10^4. -1000 <= nums[i] <= 1000. -10^7 <= k <= 10^7.

Description: Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals k.

Examples:
- [1,1,1], k=2 → 2
- [1,2,3], k=3 → 2
- [3,4,7,2,-3,1,4,2], k=7 → 4

Key insight: For each prefix_sum, check if (prefix_sum - k) exists in your seen dict. Count occurrences.
Template hint:
```
prefix_sum = 0
seen = {0: 1}
count = 0
for num in nums:
    prefix_sum += num
    count += seen.get(prefix_sum - k, 0)
    seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
```

---

### Maximum Subarray (LC 53)
Pattern: Running-State Tracking (Kadane's algorithm)
Difficulty: Medium
Constraints: 1 <= nums.length <= 10^5. -10^4 <= nums[i] <= 10^4.

Description: Given an integer array nums, find the subarray with the largest sum and return its sum.

Examples:
- [-2,1,-3,4,-1,2,1,-5,4] → 6  (subarray [4,-1,2,1])
- [1] → 1
- [5,4,-1,7,8] → 23
- [-1,-2,-3] → -1

Key decision at each element: extend the current subarray OR start fresh from this element.
Running state: current_sum = max(nums[i], current_sum + nums[i])

---

## After Solving — log in your .py file

```python
# Status: Independent / Hint / Failed
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# mistakes/confusion: [note or NA]
# Pattern: [pattern name]
```

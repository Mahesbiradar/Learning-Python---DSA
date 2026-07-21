---

# Day 42 — 2026-07-21 — Reinforcement Day

Focus: Binary Search Applied (standalone session) + Linked List Dummy Node

Phase: Linked Lists (Volume Building)

Daily Target: 11 Problems

---

&gt; **Standalone Session Note — Day 1 of 2 (Jul 21–22):**
&gt; LC 33, LC 153, and LC 875 are the mandatory Binary Search Applied standalone session set.
&gt; Do NOT time-box to 25/40 min targets — give each 60–90 min.
&gt; Before touching code for any of these three, write the monotonic predicate / rotation-handling logic by hand on paper.
&gt; Solve them back-to-back in the same block. Only mark the standalone session "done" if you can solve the hardest variant cold with no hint on the next day.

---

## SOP Reminder (2 min before every problem)

Read → Restate → Identify Pattern → Plan in Words → Dry Run → Code → Test → Submit

---

## Tier 4 Recalls (5 min each)

Write the template from memory.

1. Frequency Hashing
2. Prefix Sum — Pivot / Equilibrium

---

## Tier 1 — Priority Revision

### 1. Search in Rotated Sorted Array (LC 33)

There is an integer array `nums` sorted in ascending order (with **distinct values**).

Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` (`1 &lt;= k &lt; nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed).

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

**Example 2:**
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

**Example 3:**
Input: nums = [1], target = 0
Output: -1

# Status: 
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Binary Search
# Variant: Applied — exact search in rotated sorted array
# mistakes/confusion: ___

---

### 2. Find Minimum in Rotated Sorted Array (LC 153)

Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times.

Given the sorted rotated array `nums` of **unique** elements, return the **minimum** element of this array.

You must write an algorithm that runs in `O(log n)` time.

**Example 1:**
Input: nums = [3,4,5,1,2]
Output: 1

**Example 2:**
Input: nums = [4,5,6,7,0,1,2]
Output: 0

**Example 3:**
Input: nums = [11,13,15,17]
Output: 11

# Status: 
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Binary Search
# Variant: Applied — boundary search in rotated sorted array
# mistakes/confusion: ___

---

## Tier 3 — Revision (6 Problems)

### 3. Find Peak Element (LC 162)

A peak element is an element that is strictly greater than its neighbors.

Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.

You may imagine that `nums[-1] = nums[n] = -∞`.

You must write an algorithm that runs in `O(log n)` time.

**Example 1:**
Input: nums = [1,2,3,1]
Output: 2

**Example 2:**
Input: nums = [1,2,1,3,5,6,4]
Output: 5

# Status: 
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Binary Search
# Variant: Lower bound — first position
# mistakes/confusion: ___

---

### 4. Range Sum Query - Immutable (LC 303)

Given an integer array `nums`, handle multiple queries of the following type:

1. Calculate the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** where `left &lt;= right`.

Implement the `NumArray` class:
- `NumArray(int[] nums)` initializes the object with the integer array `nums`.
- `int sumRange(int left, int right)` returns the **sum** of the elements of `nums` between indices `left` and `right` **inclusive**.

**Example 1:**
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

# Status: 
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Prefix Sum
# Variant: Prefix array
# mistakes/confusion: ___

---

### 5. Two Sum (LC 1)

Given an array of integers `nums` and an integer `target`, return **indices** of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

**Example 1:**
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

**Example 2:**
Input: nums = [3,2,4], target = 6
Output: [1,2]

**Example 3:**
Input: nums = [3,3], target = 6
Output: [0,1]

# Status: 
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Complement Lookup
# Variant: Two Sum style
# mistakes/confusion: ___

---

### 6. Valid Perfect Square (LC 367)

Given a positive integer `num`, return `true` if `num` is a perfect square or `false` otherwise.

**Do not** use any built-in library function, such as `sqrt`.

**Example 1:**
Input: num = 16
Output: true

**Example 2:**
Input: num = 14
Output: false

# Status: 
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Binary Search
# Variant: Lower bound — first position
# mistakes/confusion: ___

---

### 7. Ransom Note (LC 383)

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

**Example 1:**
Input: ransomNote = "a", magazine = "b"
Output: false

**Example 2:**
Input: ransomNote = "aa", magazine = "ab"
Output: false

**Example 3:**
Input: ransomNote = "aa", magazine = "aab"
Output: true

# Status: 
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Frequency Hashing
# Variant: Count + query
# mistakes/confusion: ___

---

### 8. Koko Eating Bananas (LC 875)

Koko loves to eat bananas. There are `n` piles of bananas, the `i`th pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the **minimum integer** `k` such that she can eat all the bananas within `h` hours.

**Example 1:**
Input: piles = [3,6,7,11], h = 8
Output: 4

**Example 2:**
Input: piles = [30,11,23,4,20], h = 5
Output: 30

**Example 3:**
Input: piles = [30,11,23,4,20], h = 6
Output: 23

&gt; **Standalone session problem.** Before coding, write out the monotonic predicate in plain English: "If Koko can finish at speed k, then she can also finish at any speed &gt; k." Use this to justify why binary search on the answer space works.

# Status: 
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Binary Search
# Variant: Applied — boundary / feasibility (search on answer)
# mistakes/confusion: ___

---

## New Problems

### 9. Merge k Sorted Lists (LC 23)

You are given an array of `k` linked-lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

**Example 1:**
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

**Example 2:**
Input: lists = []
Output: []

**Example 3:**
Input: lists = [[]]
Output: []

**Constraints:**
- `k == lists.length`
- `0 &lt;= k &lt;= 10^4`
- `0 &lt;= lists[i].length &lt;= 500`
- `-10^4 &lt;= lists[i][j] &lt;= 10^4`
- `lists[i]` is sorted in ascending order.
- The sum of `lists[i].length` will not exceed `10^4`.

# Status: 
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Linked List
# Variant: Dummy node — merge k sorted lists
# mistakes/confusion: ___

---

## Daily Summary

New: 1 | Tier1: 2 | Tier2: 0 | Tier3: 6 | Tier4: 2 | Total: 11

---
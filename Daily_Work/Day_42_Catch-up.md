---

# Day 42 Catch-up — 2026-07-21 — Backlog Clearance

Focus: Overdue Tier 3 Revision (Arrays + Hash Maps phase)

Phase: Linked Lists (Volume Building) — on hold for 1 day

Daily Target: 12 Problems

---

## SOP Reminder (2 min before every problem)

Read → Restate → Identify Pattern → Plan in Words → Dry Run → Code → Test → Submit

---

## Tier 3 — Revision (Backlog Clearance)

Solve in order. Do not skip ahead.

### 1. K Divisible Elements Subarrays (LC 2261)

Given an integer array `nums` and two integers `k` and `p`, return the number of **distinct subarrays** which have **at most** `k` elements divisible by `p`.

Two subarrays are **distinct** if they have different elements or different lengths.

**Example 1:**
Input: nums = [2,3,3,2,2], k = 2, p = 2
Output: 11

**Example 2:**
Input: nums = [1,2,3,4], k = 4, p = 1
Output: 10

# Status: 
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Brute Force
# Variant: Subarray enumeration
# mistakes/confusion: ___

---

### 2. Two Sum II — Input Array Is Sorted (LC 167)

Given a **1-indexed** array of integers `numbers` that is already sorted in **non-decreasing order**, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 &lt;= index1 &lt; index2 &lt;= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, **added by one** as an integer array `[index1, index2]` of length 2.

**Example 1:**
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

**Example 2:**
Input: numbers = [2,3,4], target = 6
Output: [1,3]

**Example 3:**
Input: numbers = [-1,0], target = -1
Output: [1,2]

# Status: 
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Two Pointers
# Variant: Opposite ends
# mistakes/confusion: ___

---

### 3. Unique Number of Occurrences (LC 1207)

Given an array of integers `arr`, return `true` if the number of occurrences of each value in the array is **unique**, or `false` otherwise.

**Example 1:**
Input: arr = [1,2,2,1,1,3]
Output: true

**Example 2:**
Input: arr = [1,2]
Output: false

**Example 3:**
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
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

### 4. Subarray Sums Divisible by K (LC 974)

Given an integer array `nums` and an integer `k`, return the number of non-empty subarrays that have a sum divisible by `k`.

**Example 1:**
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7

**Example 2:**
Input: nums = [5], k = 9
Output: 0

# Status: 
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Prefix Sum
# Variant: Modulo
# mistakes/confusion: ___

---

### 5. Continuous Subarray Sum (LC 523)

Given an integer array `nums` and an integer `k`, return `true` if `nums` has a **good subarray** or `false` otherwise.

A **good subarray** is a subarray where:
- its length is **at least two**, and
- the sum of the elements of the subarray is a multiple of `k`.

**Example 1:**
Input: nums = [23,2,4,6,7], k = 6
Output: true

**Example 2:**
Input: nums = [23,2,6,4,7], k = 6
Output: true

**Example 3:**
Input: nums = [23,2,6,4,7], k = 13
Output: false

# Status: 
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Prefix Sum
# Variant: Modulo
# mistakes/confusion: ___

---

### 6. Container With Most Water (LC 11)

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Example 1:**
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

**Example 2:**
Input: height = [1,1]
Output: 1

# Status: 
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Two Pointers
# Variant: Maximize/minimize between ends
# mistakes/confusion: ___

---

### 7. Isomorphic Strings (LC 205)

Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

**Example 1:**
Input: s = "egg", t = "add"
Output: true

**Example 2:**
Input: s = "foo", t = "bar"
Output: false

**Example 3:**
Input: s = "paper", t = "title"
Output: true

# Status: 
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Grouping Hash Map
# Variant: Canonical key
# mistakes/confusion: ___

---

### 8. Remove Element (LC 27)

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place**. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

**Example 1:**
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

**Example 2:**
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]

# Status: 
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Two Pointers
# Variant: Write pointer — compact/remove
# mistakes/confusion: ___

---

### 9. Arranging Coins (LC 441)

You have `n` coins and you want to build a staircase with these coins. The staircase consists of `k` rows where the `ith` row has exactly `i` coins. The last row of the staircase **may be** incomplete.

Given the integer `n`, return the number of **complete rows** of the staircase you will build.

**Example 1:**
Input: n = 5
Output: 2

**Example 2:**
Input: n = 8
Output: 3

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

### 10. Find Smallest Letter Greater Than Target (LC 744)

You are given an array of characters `letters` that is sorted in **non-decreasing order**, and a character `target`. There are **at least two different characters** in `letters`.

Return the **smallest** character in `letters` that is lexicographically **greater than** `target`. If such a character does not exist, return the first character in `letters`.

**Example 1:**
Input: letters = ["c","f","j"], target = "a"
Output: "c"

**Example 2:**
Input: letters = ["c","f","j"], target = "c"
Output: "f"

**Example 3:**
Input: letters = ["x","x","y","y"], target = "z"
Output: "x"

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

### 11. Guess Number Higher or Lower (LC 374)

We are playing the Guess Game. The game is as follows:

I pick a number from `1` to `n`. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API `int guess(int num)`, which returns 3 possible results:
- `-1`: Your guess is higher than the number I picked (i.e. `num &gt; pick`).
- `1`: Your guess is lower than the number I picked (i.e. `num &lt; pick`).
- `0`: your guess is equal to the number I picked (i.e. `num == pick`).

Return the number that I picked.

**Example 1:**
Input: n = 10, pick = 6
Output: 6

**Example 2:**
Input: n = 1, pick = 1
Output: 1

**Example 3:**
Input: n = 2, pick = 1
Output: 1

# Status: 
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Binary Search
# Variant: Standard — find target
# mistakes/confusion: ___

---

### 12. Make Sum Divisible by P (LC 1590)

Given an array of positive integers `nums`, remove the **smallest** subarray (possibly **empty**) such that the **sum** of the remaining elements is divisible by `p`. It is **not** allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or `-1` if it's impossible.

**Example 1:**
Input: nums = [3,1,4,2], p = 6
Output: 1

**Example 2:**
Input: nums = [6,3,5,2], p = 9
Output: 2

**Example 3:**
Input: nums = [1,2,3], p = 3
Output: 0

# Status: 
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: Prefix Sum
# Variant: Modulo
# mistakes/confusion: ___

---

## Daily Summary

New: 0 | Tier1: 0 | Tier2: 0 | Tier3: 12 | Tier4: 0 | Total: 12

---
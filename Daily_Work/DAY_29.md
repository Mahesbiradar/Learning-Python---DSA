---
# Day 29 — 2026-06-29 — Reinforcement Day
Focus: Prefix Sum — Modulo Variant (Session 2)
Phase: Gap-Fill (DS 1: Arrays + Hash Maps)
Daily target: 12 problems

---
## SOP Reminder (2 min before every problem)
Read fully → Restate in one line → Identify pattern → Plan in words → Dry run → Code → Test

---
## Warm-Up — Modulo Variant Template (5 min, write from memory)
Before any problems, write the Prefix Sum Modulo core template from memory.
Key question to answer: why does `prefix[j] % k == prefix[i] % k` mean the subarray is divisible by k?

[ Write template here ]

---
## TIER 4 Recalls (5 min each, no full solve)
Write the template from memory. If you can't in 3 min → flag as Tier 2 and add to next day.

1. Prefix Sum (Pivot / Equilibrium)
2. Sliding Window (Variable size)

---
## TIER 1 — Priority Revision (solve these first, all of them)

### 1. Find Smallest Letter Greater Than Target (LC 744) — Easy
Given a characters array `letters` that is sorted in non-decreasing order, and a character `target`,
return the smallest character in the array that is strictly greater than `target`.

Note that letters wrap around: if every character in `letters` is smaller than or equal to `target`,
then return `letters[0]`.

**Example 1:**
Input: letters = ["c","f","j"], target = "a"
Output: "c"

**Example 2:**
Input: letters = ["c","f","j"], target = "c"
Output: "f"

**Example 3:**
Input: letters = ["c","f","j"], target = "j"
Output: "c"

**Constraints:**
- 2 <= letters.length <= 10^4
- letters[i] is a lowercase English letter
- letters is sorted in non-decreasing order
- letters contains at least two different characters
- target is a lowercase English letter

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

### 2. Make Sum Divisible by P (LC 1590) — Medium
Given an array of positive integers `nums`, remove the **smallest** subarray (possibly empty) such
that the **sum** of the remaining elements is divisible by `p`. It is **not** allowed to remove
the whole array. Return the length of the smallest subarray that you need to remove, or `-1` if
it is impossible.

A **subarray** is defined as a contiguous block of elements in the array.

**Example 1:**
Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum is 10. Remove [4] → remaining sum = 6, which is divisible by 6.

**Example 2:**
Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: Remove [5,2] → remaining sum = 9, divisible by 9.

**Example 3:**
Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Sum = 6 is already divisible by 3. Remove nothing.

**Constraints:**
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= p <= 10^9

**Self-hint (read only after 20 min of no progress):**
total_remainder = sum(nums) % p. You need to find the shortest subarray
whose sum ≡ total_remainder (mod p). Then use prefix sum + hash map to
find the shortest such subarray in O(n).

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

## TIER 2 — Revision (3 problems)

### 3. 
 — Medium
Given a binary array `nums`, return the maximum length of a contiguous subarray with an equal
number of `0` and `1`.

**Example 1:**
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

**Example 2:**
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is the longest contiguous subarray with equal number of 0 and 1.

**Constraints:**
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

### 4. Range Sum Query - Immutable (LC 303) — Easy
Given an integer array `nums`, handle multiple queries of the following type:
Calculate the sum of the elements of `nums` between indices `left` and `right` **inclusive**
where `left <= right`.

Implement the `NumArray` class:
- `NumArray(int[] nums)` — Initializes the object with the integer array `nums`.
- `int sumRange(int left, int right)` — Returns the sum of elements between indices `left` and
  `right` inclusive (O(1) per query is expected).

**Example 1:**
Input:
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output: [null, 1, -1, -3]
Explanation:
numArray = NumArray([-2, 0, 3, -5, 2, -1])
numArray.sumRange(0, 2) → (-2) + 0 + 3 = 1
numArray.sumRange(2, 5) → 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5) → (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

**Constraints:**
- 1 <= nums.length <= 10^4
- -10^5 <= nums[i] <= 10^5
- 0 <= left <= right < nums.length
- At most 10^4 calls will be made to sumRange

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?) init | O(?) query
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

### 5. Maximum Number of Vowels in a Substring of Given Length (LC 1456) — Medium
Given a string `s` and an integer `k`, return the **maximum number of vowel letters** in any
substring of `s` with length `k`.

Vowel letters in English are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

**Example 1:**
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

**Example 2:**
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

**Example 3:**
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" all contain 2 vowels.

**Constraints:**
- 1 <= s.length <= 10^5
- s consists of lowercase English letters
- 1 <= k <= s.length

**Time target: under 20 min (last attempt was 45 min — focus on recognising the window structure immediately)**

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

## TIER 3 — Revision (2 problems)

### 6. Length of Last Word (LC 58) — Easy
Given a string `s` consisting of words and spaces, return the length of the **last** word in
the string. A **word** is a maximal substring consisting of non-space characters only.

**Example 1:**
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

**Example 2:**
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

**Example 3:**
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

**Constraints:**
- 1 <= s.length <= 10^4
- s consists of only English letters and spaces ' '
- There will be at least one word in s

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

### 7. Guess Number Higher or Lower (LC 374) — Easy
We are playing the Guess Game. I pick a number from `1` to `n`. You have to guess which number
I picked. Every time you guess wrong, I will tell you whether the number I picked is higher or
lower than your guess.

You call a pre-defined API `int guess(int num)`, which returns three possible results:
- `-1`: Your guess is higher than the number I picked (i.e. `num > pick`).
- `1`: Your guess is lower than the number I picked (i.e. `num < pick`).
- `0`: Your guess is equal to the number I picked.

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

**Constraints:**
- 1 <= n <= 2^31 - 1
- 1 <= pick <= n

**Note from last attempt:** Pattern was misidentified as Two Pointers in file — it is Binary Search.
Recall: left, right = 1, n. mid = (left + right) // 2. Check guess(mid), adjust bounds.

```python
# The guess API is already defined for you.
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          0 if num is equal to the picked number
# def guess(num: int) -> int:

# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

## New Problems (3 problems)

### 8. Find the Divisibility Array of a String (LC 2575) — Medium
You are given a **0-indexed** string `word` of length `n` consisting of digits, and a positive
integer `m`.

The **divisibility array** `div` of `word` is an integer array of length `n` such that:
- `div[i] = 1` if the numeric value of `word[0,...,i]` is divisible by `m`, or
- `div[i] = 0` otherwise.

Return the divisibility array of `word`.

**Example 1:**
Input: word = "998244353", m = 3
Output: [1,1,0,0,0,1,1,0,0]
Explanation:
word[0..0] = "9"      → 9 % 3 = 0      → div[0] = 1
word[0..1] = "99"     → 99 % 3 = 0     → div[1] = 1
word[0..2] = "998"    → 998 % 3 = 2    → div[2] = 0
word[0..5] = "998244" → 998244 % 3 = 0 → div[5] = 1

**Example 2:**
Input: word = "1010", m = 10
Output: [0,1,0,1]
Explanation:
"1"    → 1 % 10 = 1  → div[0] = 0
"10"   → 10 % 10 = 0 → div[1] = 1
"101"  → 101 % 10 = 1→ div[2] = 0
"1010" → 1010 % 10=0 → div[3] = 1

**Constraints:**
- 1 <= n <= 10^5
- word consists of digits from '0' to '9'
- 1 <= m <= 10^9

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

### 9. K Divisible Elements Subarrays (LC 2261) — Medium
Given an integer array `nums` and two integers `k` and `p`, return the **number of distinct
subarrays** which have **at most** `k` elements divisible by `p`.

Note that two subarrays are **distinct** if they differ at any index.

**Example 1:**
Input: nums = [2,3,3,2,2], k = 2, p = 2
Output: 6
Explanation: The distinct subarrays with at most 2 elements divisible by 2 are:
[2], [2,3], [2,3,3], [3], [3,3], [2]
The subarrays [2] and [3] appear more than once in the array but count as one distinct each.
Other subarrays have more than 2 elements divisible by 2 and are not counted.

**Example 2:**
Input: nums = [1,2,3,4], k = 4, p = 1
Output: 10
Explanation: All elements of nums are divisible by 1. Every subarray has at most 4 elements
divisible by 1. Since all subarrays are distinct, total count = 10 (total subarrays of length 4).

**Constraints:**
- 1 <= nums.length <= 200
- 1 <= nums[i], p <= 200
- 1 <= k <= nums.length

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

### 10. Total Appeal of A String (LC 2262) — Hard
The **appeal** of a string is the number of **distinct** characters found in the string.
For example, the appeal of `"abbca"` is 3 because it has 3 distinct characters: 'a', 'b', 'c'.

Given a string `s`, return the **total appeal of all of its substrings**.

**Example 1:**
Input: s = "abbca"
Output: 28
Explanation:
Substrings of length 1: "a"(1), "b"(1), "b"(1), "c"(1), "a"(1) → sum = 5
Substrings of length 2: "ab"(2), "bb"(1), "bc"(2), "ca"(2)     → sum = 7
Substrings of length 3: "abb"(2), "bbc"(2), "bca"(3)            → sum = 7
Substrings of length 4: "abbc"(3), "bbca"(3)                    → sum = 6
Substrings of length 5: "abbca"(3)                              → sum = 3
Total = 5 + 7 + 7 + 6 + 3 = 28

**Example 2:**
Input: s = "code"
Output: 20
Explanation:
Length 1: "c"(1), "o"(1), "d"(1), "e"(1)          → sum = 4
Length 2: "co"(2), "od"(2), "de"(2)                → sum = 6
Length 3: "cod"(3), "ode"(3)                        → sum = 6
Length 4: "code"(4)                                 → sum = 4
Total = 4 + 6 + 6 + 4 = 20

**Constraints:**
- 1 <= s.length <= 10^5
- s consists of lowercase English letters

**Note:** This is a Hard. Brute force O(n³) is too slow. Think: instead of counting per substring,
count the **contribution** of each character across all substrings it appears in.

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

## Daily Summary
New: 3 | Tier1: 2 | Tier2: 3 | Tier3: 2 | Tier4: 2 recalls | Total: 12

# Day 2 Problems: Arrays + Duplicates + In-Place Updates

Date: 2026-05-02  
Phase: 1 - Arrays + Hashing + Strings  
Topic: duplicate detection, set lookup, in-place writes, missing values, prefix/suffix thinking  
Target: 10 problems  
Expected time: 8-10 hours

## Before You Start

Revision status: passed, with one note.

- `second_maximum(nums)` should check `len(nums) < 2` before reading `nums[0]`. Your current visible tests pass, but `[]` would crash.
- `move_zeros(nums)` is correct and in-place.
- `major_element(nums)` using dictionary is correct.
- `boyer_moore(nums)` candidate logic is correct, and your validation pass is a good extra safety step.

## How To Submit For Evaluation

After solving all problems, come back with:

```text
Day 2 completed.

Attempted:
Solved independently:
Solved after hint:
Stuck:

My answers are in:
- file name or pasted below

Problems I want reviewed first:
1.
2.
3.
```

For each problem, write:

```text
Problem:

Understanding:

Brute Force:

Optimized:

Dry Run:

Code:

Time Complexity:

Space Complexity:

Status: Solved independently / Solved after hint / Stuck

Mistake or confusion:
```

## Day 2 Rules

- Do not use built-in shortcuts that hide the learning pattern.
- You may use `set()` and `dict()` where the pattern asks for hashing.
- For in-place problems, do not create a second result list unless the brute-force version asks for it.
- Dry run the write-pointer problems carefully.
- If stuck, spend 30-45 minutes before taking a hint.

---

## Problem 1: Contains Duplicate

Given a list of integers, return `True` if any value appears at least twice. Return `False` if every element is distinct.

Example:

```python
nums = [1, 2, 3, 1]
```

Expected output:

```python
True
```

Requirements:
- First write the brute-force nested-loop idea.
- Then solve using a set.

Test cases:

```python
[1, 2, 3, 1] -> True
[1, 2, 3, 4] -> False
[1, 1, 1, 3, 3, 4, 3, 2, 4, 2] -> True
[] -> False
```

---

## Problem 2: Remove Duplicates From Sorted Array

Given a sorted list of integers, remove duplicates in-place so each unique element appears only once. Return the number of unique elements.

Example:

```python
nums = [1, 1, 2]
```

Expected output:

```python
2
```

After the function runs, the first `2` positions should be:

```python
[1, 2]
```

Requirements:
- Solve in-place.
- Use a write pointer.
- Do not create a second list for the optimized solution.

Test cases:

```python
[1, 1, 2] -> 2, first part [1, 2]
[0, 0, 1, 1, 1, 2, 2, 3, 3, 4] -> 5, first part [0, 1, 2, 3, 4]
[1] -> 1, first part [1]
[] -> 0, first part []
```

---

## Problem 3: Remove Element

Given a list `nums` and an integer `val`, remove all occurrences of `val` in-place. Return the new length.

Example:

```python
nums = [3, 2, 2, 3]
val = 3
```

Expected output:

```python
2
```

After the function runs, the first `2` positions should contain:

```python
[2, 2]
```

Requirements:
- Solve in-place.
- The order of remaining elements can stay the same.
- Do not create a second list for the optimized solution.

Test cases:

```python
[3, 2, 2, 3], val = 3 -> 2, first part [2, 2]
[0, 1, 2, 2, 3, 0, 4, 2], val = 2 -> 5, first part [0, 1, 3, 0, 4]
[], val = 1 -> 0, first part []
[1, 1, 1], val = 1 -> 0, first part []
```

---

## Problem 4: Missing Number

Given a list containing `n` distinct numbers from the range `0` to `n`, return the only number missing from the list.

Example:

```python
nums = [3, 0, 1]
```

Expected output:

```python
2
```

Requirements:
- First solve using a set.
- Then try the sum formula approach.

Test cases:

```python
[3, 0, 1] -> 2
[0, 1] -> 2
[9, 6, 4, 2, 3, 5, 7, 0, 1] -> 8
[0] -> 1
```

---

## Problem 5: Intersection Of Two Arrays

Given two lists, return a list of unique values that appear in both lists.

Example:

```python
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
```

Expected output:

```python
[2]
```

Requirements:
- Output may be in any order.
- Return unique intersection values only.
- Use sets for the optimized solution.

Test cases:

```python
[1, 2, 2, 1], [2, 2] -> [2]
[4, 9, 5], [9, 4, 9, 8, 4] -> [9, 4]
[], [1, 2] -> []
[1, 2], [3, 4] -> []
```

---

## Problem 6: Best Time To Buy And Sell Stock

Given a list where `prices[i]` is the stock price on day `i`, return the maximum profit from buying once and selling once later. If no profit is possible, return `0`.

Example:

```python
prices = [7, 1, 5, 3, 6, 4]
```

Expected output:

```python
5
```

Requirements:
- First write the brute-force pair-check idea.
- Then solve in one pass by tracking the minimum price so far.

Test cases:

```python
[7, 1, 5, 3, 6, 4] -> 5
[7, 6, 4, 3, 1] -> 0
[1, 2] -> 1
[2, 4, 1] -> 2
```

---

## Problem 7: Plus One

Given a list of digits representing a non-negative integer, add one and return the resulting digits.

Example:

```python
digits = [1, 2, 3]
```

Expected output:

```python
[1, 2, 4]
```

Requirements:
- Traverse from right to left.
- Handle carry.
- Do not convert the whole list to an integer.

Test cases:

```python
[1, 2, 3] -> [1, 2, 4]
[4, 3, 2, 1] -> [4, 3, 2, 2]
[9] -> [1, 0]
[9, 9, 9] -> [1, 0, 0, 0]
```

---

## Problem 8: Rotate Array

Given a list `nums`, rotate it to the right by `k` steps.

Example:

```python
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
```

Expected output:

```python
[5, 6, 7, 1, 2, 3, 4]
```

Requirements:
- First solve using an extra list.
- Then try the in-place reverse method.
- Handle `k > len(nums)`.

Test cases:

```python
[1, 2, 3, 4, 5, 6, 7], k = 3 -> [5, 6, 7, 1, 2, 3, 4]
[-1, -100, 3, 99], k = 2 -> [3, 99, -1, -100]
[1, 2], k = 3 -> [2, 1]
[], k = 3 -> []
```

---

## Problem 9: Product Of Array Except Self

Given a list of integers, return a list where each index contains the product of all numbers except the number at that index.

Example:

```python
nums = [1, 2, 3, 4]
```

Expected output:

```python
[24, 12, 8, 6]
```

Requirements:
- Do not use division.
- First solve using left and right product arrays.
- Then try optimizing to output array plus one running suffix variable.

Test cases:

```python
[1, 2, 3, 4] -> [24, 12, 8, 6]
[-1, 1, 0, -3, 3] -> [0, 0, 9, 0, 0]
[2, 3] -> [3, 2]
[0, 0] -> [0, 0]
```

---

## Problem 10: First Missing Positive

Given an unsorted list of integers, return the smallest missing positive integer.

Example:

```python
nums = [1, 2, 0]
```

Expected output:

```python
3
```

Requirements:
- First solve using a set.
- Then read about the in-place cyclic placement approach and attempt it if you have time.
- This is the hard/stretch problem for Day 2.

Test cases:

```python
[1, 2, 0] -> 3
[3, 4, -1, 1] -> 2
[7, 8, 9, 11, 12] -> 1
[1] -> 2
```

## End Of Day Checklist

```text
[ ] I attempted all 10 problems.
[ ] I wrote brute force for every problem.
[ ] I dry ran every problem.
[ ] I wrote time complexity for every problem.
[ ] I wrote space complexity for every problem.
[ ] I marked each problem status honestly.
[ ] I listed mistakes/confusions.
```

## Day 2 Success Criteria

Day 2 is successful if:

- You solve at least 7/10 problems.
- You can explain when to use a set for duplicate lookup.
- You can explain the write-pointer pattern.
- You can solve `Contains Duplicate` and `Best Time To Buy And Sell Stock` without hints.
- You attempt `Product Of Array Except Self`, even if it needs a hint.

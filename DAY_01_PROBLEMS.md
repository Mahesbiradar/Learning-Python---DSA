# Day 1 Problems: Array Traversal + Tracking

Date: 2026-05-01  
Phase: 1 - Arrays + Hashing + Strings  
Topic: Array traversal, indexing, tracking, adjacent comparison, in-place updates  
Target: 10 problems  
Expected time: 8-10 hours

## How To Submit For Evaluation

After solving all problems, come back with:

```text
Day 1 completed.

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

For each problem, write your answer in this format:

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

Do not submit only code. I need your thinking, dry run, and complexity.

## Day 1 Rules

- Try each problem independently first.
- If stuck, spend 30-45 minutes before seeing a hint.
- Write brute force even if the solution feels obvious.
- Dry run before coding.
- Write time and space complexity for every problem.
- Mark status honestly.

---

## Problem 1: Print All Elements

Given a list, print every element one by one.

Example:

```python
nums = [10, 20, 30, 40]
```

Expected output:

```text
10
20
30
40
```

Requirements:
- Visit every element.
- Do not use built-in shortcuts for learning purposes.

---

## Problem 2: Sum Of List

Given a list of integers, return the sum of all elements.

Example:

```python
nums = [10, 20, 30]
```

Expected output:

```python
60
```

Requirements:
- Use a loop.
- Do not use Python's built-in `sum()` for this practice.

Test cases:

```python
[10, 20, 30] -> 60
[5] -> 5
[] -> 0
[-1, 2, -3] -> -2
```

---

## Problem 3: Count Even Numbers

Given a list of integers, count how many numbers are even.

Example:

```python
nums = [1, 2, 3, 4, 6]
```

Expected output:

```python
3
```

Requirements:
- Use modulo `%`.
- Return the count.

Test cases:

```python
[1, 2, 3, 4, 6] -> 3
[1, 3, 5] -> 0
[2, 4, 6] -> 3
[] -> 0
```

---

## Problem 4: Find Maximum Element

Given a non-empty list of integers, return the maximum element.

Example:

```python
nums = [10, 5, 20, 8]
```

Expected output:

```python
20
```

Requirements:
- Do not use `max()`.
- Track the maximum manually.

Test cases:

```python
[10, 5, 20, 8] -> 20
[5] -> 5
[-10, -3, -20] -> -3
[7, 7, 7] -> 7
```

---

## Problem 5: Find Minimum Element

Given a non-empty list of integers, return the minimum element.

Example:

```python
nums = [10, 5, 20, 8]
```

Expected output:

```python
5
```

Requirements:
- Do not use `min()`.
- Track the minimum manually.

Test cases:

```python
[10, 5, 20, 8] -> 5
[5] -> 5
[-10, -3, -20] -> -20
[7, 7, 7] -> 7
```

---

## Problem 6: Reverse Array

Given a list, reverse it.

Example:

```python
nums = [1, 2, 3, 4]
```

Expected output:

```python
[4, 3, 2, 1]
```

Requirements:
- First solve using a new list.
- Then try in-place using two pointers.
- Do not use `reverse()` or slicing `[::-1]` for this practice.

Test cases:

```python
[1, 2, 3, 4] -> [4, 3, 2, 1]
[1, 2, 3] -> [3, 2, 1]
[5] -> [5]
[] -> []
```

---

## Problem 7: Check If Array Is Sorted

Given a list of integers, return `True` if it is sorted in non-decreasing order, otherwise return `False`.

Example:

```python
nums = [1, 2, 2, 4]
```

Expected output:

```python
True
```

Requirements:
- Compare adjacent elements.
- Duplicates are allowed.

Test cases:

```python
[1, 2, 2, 4] -> True
[1, 3, 2, 4] -> False
[5] -> True
[] -> True
[-3, -2, -2, 0] -> True
```

---

## Problem 8: Find Second Largest Distinct Element

Given a list of integers, return the second largest distinct element.

Example:

```python
nums = [10, 5, 8, 20, 15]
```

Expected output:

```python
15
```

Requirements:
- Do not sort the list.
- Handle duplicate largest values.
- Handle negative numbers.
- If no second largest distinct value exists, return `None`.

Test cases:

```python
[10, 5, 8, 20, 15] -> 15
[20, 20, 10] -> 10
[5, 5, 5] -> None
[1] -> None
[-10, -5, -20] -> -10
```

---

## Problem 9: Move Zeroes To End

Given a list of integers, move all zeroes to the end while keeping the order of non-zero elements.

Example:

```python
nums = [0, 1, 0, 3, 12]
```

Expected output:

```python
[1, 3, 12, 0, 0]
```

Requirements:
- Solve in-place.
- Do not create a second list.
- Keep the order of non-zero elements.

Test cases:

```python
[0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
[0, 0, 1] -> [1, 0, 0]
[1, 2, 3] -> [1, 2, 3]
[0, 0, 0] -> [0, 0, 0]
[] -> []
```

---

## Problem 10: Majority Element

Given a list of integers where one element appears more than `n // 2` times, return that majority element.

Example:

```python
nums = [3, 2, 3]
```

Expected output:

```python
3
```

Requirements:
- First solve using a dictionary frequency map.
- Then try the Boyer-Moore voting approach if you can.
- You may assume a majority element always exists.

Test cases:

```python
[3, 2, 3] -> 3
[2, 2, 1, 1, 1, 2, 2] -> 2
[1] -> 1
[5, 5, 5, 2, 2] -> 5
```

---

## End Of Day Checklist

Before coming back for evaluation, confirm:

```text
[ ] I attempted all 10 problems.
[ ] I wrote brute force for every problem.
[ ] I dry ran every problem.
[ ] I wrote time complexity for every problem.
[ ] I wrote space complexity for every problem.
[ ] I marked each problem status honestly.
[ ] I listed mistakes/confusions.
```

## Day 1 Success Criteria

Day 1 is successful if:

- You attempted all 10 problems.
- You solved at least 7 independently.
- You correctly explained traversal, tracking, adjacent comparison, and in-place updates.
- You wrote correct complexity for all 10 problems.
- You know exactly which problems need revision tomorrow.

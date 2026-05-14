# Day 1 Evaluation

Date reviewed: 2026-05-02  
Solution file: `Daily_Work/DAY_01_SOLUTIONS.py`  
Result: Pass  
Decision: Continue to Day 2 after fixing notes

## Score

Problems attempted: 10/10  
Correct outputs on visible tests: 10/10  
Solved independently: 9/10  
Solved after hint: 1/10  
Unsolved: 0/10  
Day 1 accuracy: 90%

## Problem Review

| # | Problem | Result | Notes |
| ---: | --- | --- | --- |
| 1 | Print All Elements | Pass | Good correction: avoid `print(function_that_prints())` because it prints `None`. |
| 2 | Sum Of List | Pass | Correct loop and edge case for empty list. |
| 3 | Count Even Numbers | Pass | Correct modulo usage and count tracking. |
| 4 | Find Maximum Element | Pass | Correct. Prefer initializing with `nums[0]` when input is guaranteed non-empty. |
| 5 | Find Minimum Element | Pass | Correct. Prefer initializing with `nums[0]` when input is guaranteed non-empty. |
| 6 | Reverse Array | Pass | Both approaches are correct. Rename functions so one does not overwrite the other. Extra-list space is `O(n)`, not `O(2)`. |
| 7 | Check If Array Is Sorted | Pass | Correct adjacent comparison. Dry run wording should say failure happens when `nums[i] > nums[i + 1]`. |
| 8 | Second Largest Distinct Element | Pass | Correct final logic. Edge cases came after hint, so revisit tomorrow. |
| 9 | Move Zeroes To End | Pass | Correct in-place position tracking. Good recovery from missing `pos += 1`. |
| 10 | Majority Element | Pass | Dictionary solution is correct. Space complexity is `O(n)`, not `O(1)`. Boyer-Moore remains pending. |

## Corrections To Make In Your Notes

- Reverse with extra list:
  - Time: `O(n)`
  - Space: `O(n)`
- Reverse in-place:
  - Time: `O(n)`
  - Space: `O(1)`
- Majority element using dictionary:
  - Time: `O(n)`
  - Space: `O(n)`
- Majority element using Boyer-Moore:
  - Time: `O(n)`
  - Space: `O(1)`
- If a function prints output and returns nothing, calling `print(function(...))` prints an extra `None`.
- Avoid reusing the same function name for two different solutions in the same file.

## Mentor Notes

Your thinking is moving in the right direction. You are writing the approach before code, testing edge cases, and catching mistakes while debugging. That is exactly the Day 1 habit.

The main upgrade now is precision:
- Write exact comparisons in dry runs.
- Keep complexity notes mathematically correct.
- Separate "works" from "optimal".
- Name functions clearly when writing multiple versions.

## Required Revision Before Day 2

Re-solve these without notes:

1. Second Largest Distinct Element
2. Move Zeroes To End
3. Majority Element with dictionary

Then learn and code:

1. Majority Element using Boyer-Moore voting

## Day 2 Recommendation

Continue to Day 2: Arrays + Duplicates + In-Place Updates.

Day 2 focus:
- Contains Duplicate
- Remove Duplicates from Sorted Array
- Missing Number
- Intersection of Two Arrays
- Best Time to Buy and Sell Stock
- Product of Array Except Self

Do not skip the revision items above. They should take 60-90 minutes before starting new Day 2 problems.

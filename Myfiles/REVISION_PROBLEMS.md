# Revision Problems

Solve these without looking at `PROBLEMS.md` first. After solving, compare your approach, edge cases, and complexity.

## Current Priority Queue

Use this queue before the full archive when the day plan asks for targeted revision.

| ID | Problem | Pattern | Why revisit | Next target |
| --- | --- | --- | --- | --- |
| REV-LC-001 | Valid Palindrome | Two pointers with skip loops | Day 05 still needed hints for inner skip-loop flow | Re-solve without hints |
| REV-LC-002 | Find Pivot Index | Prefix sum / check-before-update | Optimal solution worked, but update order was confusing | Dry run, then code |
| REV-LC-003 | Product Of Array Except Self | Prefix/suffix products | Day 05 used left/right arrays; target is output array + suffix variable | O(n), O(1) extra beyond output |
| REV-LC-004 | Is Subsequence | Match pointer scan | Day 05 improved, but avoid membership/frequency thinking | One scan over `t` |
| REV-LC-005 | Best Time To Buy And Sell Stock | One-pass min tracking | Day 05 improved from help-needed to independent | Timed 15-minute re-solve |
| REV-LC-006 | Group Anagrams | Sorted-key dictionary grouping | Day 06 solution viewed; Day 07 has no verified completion | Re-solve without notes; return `list(groups.values())` |
| REV-LC-007 | Valid Anagram | Character frequency comparison | Clean O(n) hash version still needs verified solve and LeetCode proof | Count/decrement; avoid string membership loop |
| REV-LC-008 | Sort Characters By Frequency | Frequency sorting | Day 07 planned but no completion evidence | Count, sort by count, build repeated chars |
| REV-LC-009 | Intersection of Two Arrays II | Frequency consume | Day 07 planned but no completion evidence | Count one list, consume from the other |
| REV-LC-010 | Daily completion tracking | Process discipline | Day 07 reflection was blank, so progress could not be verified | Record independent/hint/solution/unsolved before ending day |

## Arrays / Lists

## [REV-ARR-001] Move Zeros to End

Topic: Arrays / Lists  
Pattern: Two Pointer / Position Tracking  
Difficulty: Medium

### Problem

Move all zeros to the end while keeping the order of non-zero elements.

### Input

```python
nums = [0, 1, 0, 3, 12]
```

### Expected Output

```python
[1, 3, 12, 0, 0]
```

### Requirements

- Solve in-place.
- Do not create a second list.
- Time: O(n)
- Space: O(1)

## [REV-ARR-002] Find Second Largest Distinct Element

Topic: Arrays / Lists  
Pattern: Tracking  
Difficulty: Medium

### Problem

Find the second largest distinct number in a list.

### Input

```python
nums = [10, 5, 8, 20, 15]
```

### Expected Output

```python
15
```

### Requirements

- Do not sort the list.
- Handle duplicate largest values.
- Handle negative numbers.

## [REV-ARR-003] Check if List is Sorted

Topic: Arrays / Lists  
Pattern: Adjacent Comparison  
Difficulty: Medium

### Problem

Check whether a list is sorted in non-decreasing order.

### Input

```python
nums = [1, 3, 2, 5]
```

### Expected Output

```python
False
```

### Requirements

- Use index traversal.
- Stop early when unsorted order is found.

## [REV-ARR-004] Remove Duplicates Without Set

Topic: Arrays / Lists  
Pattern: Existence Check  
Difficulty: Medium

### Problem

Remove duplicate values while preserving original order.

### Input

```python
nums = [1, 2, 2, 3, 4, 4, 5]
```

### Expected Output

```python
[1, 2, 3, 4, 5]
```

### Requirements

- Do not use `set`.
- Preserve order.

## [REV-ARR-005] Find Missing Number

Topic: Arrays / Lists  
Pattern: Existence Check  
Difficulty: Medium

### Problem

Numbers from `1` to `n` are given with one number missing. Find the missing number.

### Input

```python
nums = [1, 2, 4, 5]
```

### Expected Output

```python
3
```

### Requirements

- First solve with nested loops.
- Then try an optimized version.

## [REV-ARR-006] Two Sum

Topic: Arrays / Lists  
Pattern: Hashing  
Difficulty: Medium

### Problem

Return the indexes of two numbers whose sum equals the target.

### Input

```python
nums = [2, 7, 11, 15]
target = 9
```

### Expected Output

```python
[0, 1]
```

### Requirements

- Solve in one pass.
- Use a dictionary.
- Do not use the same element twice.

## [REV-ARR-007] Duplicate Detection With Nested Loops

Topic: Arrays / Lists  
Pattern: Nested Loops  
Difficulty: Medium

### Problem

Find and print the first duplicate found using nested loops.

### Input

```python
nums = [1, 2, 3, 2]
```

### Expected Output

```python
2
```

### Requirements

- Do not use set or dictionary.
- Avoid comparing an element with itself.

## [REV-ARR-008] Matrix Row Sum

Topic: Arrays / Lists  
Pattern: Nested Traversal  
Difficulty: Medium

### Problem

Return a list containing the sum of every row in a matrix.

### Input

```python
matrix = [[1, 2], [3, 4], [5, 6]]
```

### Expected Output

```python
[3, 7, 11]
```

### Requirements

- Use nested loops.
- Do not use built-in `sum()`.

## Strings

## [REV-STR-001] Check Palindrome Without Slicing

Topic: Strings  
Pattern: Two Pointer  
Difficulty: Medium

### Problem

Check whether a string is a palindrome without using slicing.

### Input

```python
text = "madam"
```

### Expected Output

```python
True
```

### Requirements

- Use two pointers.
- Stop early on mismatch.

## [REV-STR-002] Count Words Robust

Topic: Strings  
Pattern: Linear Traversal  
Difficulty: Medium

### Problem

Count words in a string that may contain leading, trailing, and multiple spaces.

### Input

```python
text = "  I   love   Python  "
```

### Expected Output

```python
3
```

### Requirements

- Do not use `split()`.
- Count only word starts.

## [REV-STR-003] Remove Consecutive Duplicates

Topic: Strings  
Pattern: Adjacent Comparison  
Difficulty: Medium

### Problem

Remove only consecutive duplicate characters.

### Input

```python
text = "aaabbccdaa"
```

### Expected Output

```python
"abcda"
```

### Requirements

- Do not remove non-consecutive repeats.
- Handle empty string.

## [REV-STR-004] First Repeating Character

Topic: Strings  
Pattern: Hashing  
Difficulty: Medium

### Problem

Find the first character that repeats while scanning left to right.

### Input

```python
text = "abcaed"
```

### Expected Output

```python
"a"
```

### Requirements

- Use `seen` logic.
- Stop immediately after the first repeat.

## [REV-STR-005] First Non-Repeating Character

Topic: Strings  
Pattern: Frequency Dictionary  
Difficulty: Medium

### Problem

Find the first character that appears exactly once.

### Input

```python
text = "aabbcde"
```

### Expected Output

```python
"c"
```

### Requirements

- Use a frequency dictionary.
- Preserve original order.

## [REV-STR-006] Check Anagram

Topic: Strings  
Pattern: Frequency Counting  
Difficulty: Medium

### Problem

Check whether two strings are anagrams.

### Input

```python
s1 = "listen"
s2 = "silent"
```

### Expected Output

```python
"Anagram"
```

### Requirements

- Do not sort.
- Character counts must match.

## [REV-STR-007] Check Substring Manually

Topic: Strings  
Pattern: Nested Loops  
Difficulty: Medium

### Problem

Check whether `sub` exists inside `text` without using `in`, `find`, or `index`.

### Input

```python
text = "hello world"
sub = "world"
```

### Expected Output

```python
"Found"
```

### Requirements

- Try every valid starting index.
- Compare characters manually.

## [REV-STR-008] Find Longest Word

Topic: Strings  
Pattern: String Building  
Difficulty: Medium

### Problem

Find the longest word in a sentence without using `split()`.

### Input

```python
text = "I love Python programming"
```

### Expected Output

```python
"programming"
```

### Requirements

- Build words manually.
- Compare the last word after the loop.

## [REV-STR-009] String Compression

Topic: Strings  
Pattern: String Building / Counting  
Difficulty: Medium

### Problem

Compress consecutive characters with their counts.

### Input

```python
text = "aaabbc"
```

### Expected Output

```python
"a3b2c1"
```

### Requirements

- Count consecutive groups.
- Handle the final group correctly.

## [REV-STR-010] Check Rotation

Topic: Strings  
Pattern: String Matching  
Difficulty: Medium

### Problem

Check whether `s2` is a rotation of `s1`.

### Input

```python
s1 = "abcde"
s2 = "cdeab"
```

### Expected Output

```python
"Yes"
```

### Requirements

- Lengths must match.
- Try both the standard concatenation method and a manual rotation method.

## Sets / Hashing

## [REV-HASH-001] Check Duplicate Exists

Topic: Sets / Hashing  
Pattern: Hashing  
Difficulty: Medium

### Problem

Return whether any duplicate exists in a list.

### Input

```python
nums = [1, 2, 3, 4, 1]
```

### Expected Output

```python
True
```

### Requirements

- Use a set.
- Stop early when duplicate is found.

## [REV-HASH-002] Find Common Elements Optimized

Topic: Sets / Hashing  
Pattern: Hashing  
Difficulty: Medium

### Problem

Find common elements between two lists.

### Input

```python
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
```

### Expected Output

```python
[3, 4]
```

### Requirements

- Use a set for fast lookup.
- Preserve the order from list `a`.

## [REV-HASH-003] Find Missing Number Optimized

Topic: Sets / Hashing  
Pattern: Hashing  
Difficulty: Medium

### Problem

Find the missing number from `1` to `n` using sets.

### Input

```python
nums = [1, 2, 4, 5]
```

### Expected Output

```python
3
```

### Requirements

- Use set difference.
- Convert the result into a single number.

## [REV-HASH-004] Count Frequencies

Topic: Sets / Hashing  
Pattern: Frequency Dictionary  
Difficulty: Medium

### Problem

Count the frequency of every number in a list.

### Input

```python
nums = [1, 2, 2, 3, 1, 4]
```

### Expected Output

```python
{1: 2, 2: 2, 3: 1, 4: 1}
```

### Requirements

- Use a dictionary.
- Do not use `count()`.

## [REV-HASH-005] First Non-Repeating Element

Topic: Sets / Hashing  
Pattern: Frequency Dictionary  
Difficulty: Medium

### Problem

Find the first number that appears only once.

### Input

```python
nums = [1, 2, 2, 3, 1, 4]
```

### Expected Output

```python
3
```

### Requirements

- Count frequencies first.
- Then scan the original list again.

## Tuples

## [REV-TUP-001] Reverse Tuple Without Slicing

Topic: Tuples  
Pattern: Reverse Traversal  
Difficulty: Medium

### Problem

Reverse a tuple without using slicing.

### Input

```python
values = (1, 2, 3, 4)
```

### Expected Output

```python
(4, 3, 2, 1)
```

### Requirements

- Remember that tuples are immutable.
- Build a new tuple.

## [REV-TUP-002] Remove Duplicates From Tuple

Topic: Tuples  
Pattern: Existence Check  
Difficulty: Medium

### Problem

Remove duplicates from a tuple while preserving order.

### Input

```python
values = (1, 2, 2, 3, 1)
```

### Expected Output

```python
(1, 2, 3)
```

### Requirements

- Do not use a set.
- Build a new tuple.

## [REV-TUP-003] Second Largest in Tuple

Topic: Tuples  
Pattern: Tracking  
Difficulty: Medium

### Problem

Find the second largest distinct number in a tuple.

### Input

```python
values = (5, 1, 8, 3, 8)
```

### Expected Output

```python
5
```

### Requirements

- Do not sort.
- Ignore duplicate largest values.

## [REV-TUP-004] Find Minimum Sum Pair

Topic: Tuples  
Pattern: Linear Traversal  
Difficulty: Medium

### Problem

Find the pair with the smallest sum.

### Input

```python
pairs = [(1, 5), (2, 3), (4, 7)]
```

### Expected Output

```python
(2, 3)
```

### Requirements

- Use loop unpacking.
- Track both the minimum sum and the result pair.

## [REV-TUP-005] Count Frequency Using Tuples

Topic: Tuples  
Pattern: Nested Loops  
Difficulty: Medium

### Problem

Return `(value, count)` pairs for every unique number.

### Input

```python
nums = [1, 2, 2, 3]
```

### Expected Output

```python
[(1, 1), (2, 2), (3, 1)]
```

### Requirements

- Use nested loops.
- Avoid duplicate `(value, count)` pairs.

## Revision Order

1. Solve all Arrays / Lists problems.
2. Solve all Strings problems.
3. Solve all Sets / Hashing problems.
4. Solve all Tuples problems.
5. Re-solve the problems you missed without checking notes.

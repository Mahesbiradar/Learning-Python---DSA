# Day 08 Work

Date: 2026-05-14  
Phase: Month 1 - Arrays + Hashing + Strings  
Current week focus: repeat Day 07 consolidation because Day 07 has no verified completion record.

## Today's Realistic Goals

- Complete 3 new problems maximum.
- Complete 2 revision problems.
- Get at least 1 accepted LeetCode submission before optional work.
- Record solved independently / after hints / after solution for every problem.
- Keep completion target at 70-80%, not perfection.

## Today's Continuation

Continue Day 07's unfinished consolidation:
- Clean hash-map anagram logic.
- Frequency counting with duplicates.
- Frequency sorting with correct `m = unique count` complexity.
- Group Anagrams sorted-key recall.
- Pivot Index no-answer return case.

Do not start a heavy Week 2 topic until this is logged cleanly.

## Prerequisites Revision

Write these from memory before coding:

```python
freq[x] = freq.get(x, 0) + 1
key = "".join(sorted(word))
right_sum = total_sum - left_sum - nums[i]
sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)
```

Explain:
- Why dictionary lookup is average `O(1)`.
- Why sorting one word of length `k` costs `O(k log k)`.
- Why frequency sorting is `O(n + m log m)`, where `m` is the number of unique values.
- Why Pivot Index must return `-1` if no valid index exists.

Time target: 15 minutes.

## Fundamentals Revision

Write from memory:

```python
def frequency_map(items):
    pass

def first_unique(items):
    pass
```

Expected behavior:

```python
frequency_map([1, 1, 2, 3, 3, 3]) -> {1: 2, 2: 1, 3: 3}
first_unique([1, 2, 2, 3, 1, 4]) -> 3
```

Complexity:
- `frequency_map`: Time = , Space =
- `first_unique`: Time = , Space =

Time target: 15 minutes.

## Today's New Problems

### 1. Valid Anagram - Clean Hash Version

Topic: Hashing / Strings  
Pattern: Character frequency comparison  
Difficulty: Easy  
LeetCode: Required

Requirements:
- Return early if lengths differ.
- Use count/decrement or two frequency dictionaries.
- Do not use `char in t` inside a loop.
- Write exact time and space complexity.

Test cases:

```python
"anagram", "nagaram" -> True
"rat", "car" -> False
"aa", "a" -> False
"", "" -> True
"aacc", "ccac" -> False
```

Time target: 25 minutes.

### 2. Intersection of Two Arrays II

Topic: Hashing / Frequency  
Pattern: Count one list, consume from the other  
Difficulty: Easy  
LeetCode: Recommended

Requirements:
- Count frequencies from one list.
- Traverse the other list.
- Append only when remaining count is positive.
- Decrease count after using a value.

Test cases:

```python
[1, 2, 2, 1], [2, 2] -> [2, 2]
[4, 9, 5], [9, 4, 9, 8, 4] -> [4, 9] in any order
[1, 1, 1], [1, 1] -> [1, 1]
[], [1, 2] -> []
[3], [3] -> [3]
```

Time target: 25-30 minutes.

### 3. Sort Characters By Frequency

Topic: Hashing / Frequency Sorting  
Pattern: Count characters, sort by count  
Difficulty: Medium  
LeetCode: Recommended

Requirements:
- Build a character frequency dictionary.
- Sort dictionary items by frequency descending.
- Build the answer by repeating each character `count` times.
- Do sorting version only; bucket version is optional later.

Test cases:

```python
"tree" -> "eert" or "eetr"
"cccaaa" -> "cccaaa" or "aaaccc"
"Aabb" -> "bbAa" or "bbaA"
"a" -> "a"
"" -> ""
```

Time target: 35-40 minutes.

## Revision Problems

### Revision 1. Group Anagrams

Why revisit: Day 06 was solution viewed and Day 07 has no verified completion.  
Pattern: Sorted string key to dictionary list  
Difficulty: Medium  
LeetCode: Required if clean locally

Rules:
- Do not read old code first.
- Use `key = "".join(sorted(word))`.
- Append each word to the correct dictionary list.
- Return `list(groups.values())`.

Time target: 30-35 minutes.

### Revision 2. Find Pivot Index

Why revisit: Day 06 had a no-answer return bug and Day 07 has no verified fix.  
Pattern: Prefix sum with check-before-update  
Difficulty: Easy

Rules:
- Compute `right_sum`.
- Compare `left_sum == right_sum`.
- Then add current number to `left_sum`.
- Return `-1` after the loop.

Must-pass tests:

```python
[1, 7, 3, 6, 5, 6] -> 3
[1, 2, 3] -> -1
[2, 1, -1] -> 0
[0, 0, 0] -> 0
[-1, -1, 0, 1, 1, 0] -> 5
```

Time target: 15-20 minutes.

## Weak-Pattern Reinforcement

| Weak pattern | Tomorrow's rule |
| --- | --- |
| Completion tracking | Fill reflection immediately after solving. |
| Medium hashing | Count/group first; only then sort or collect output. |
| Group Anagrams | Dictionary value is a list; return `list(groups.values())`. |
| Frequency sorting | Use `sorted(freq.items(), key=lambda item: item[1], reverse=True)`. |
| Pivot Index | If no pivot is found, return `-1`, never default `0`. |
| Complexity | Use `m = unique count` for sorted frequency items. |
| LeetCode proof | Submit one clean easy before optional medium work. |

## LeetCode Workflow

1. Solve locally first.
2. Run every listed example and one custom edge case.
3. Submit `Valid Anagram` first if clean; otherwise submit `Find Pivot Index`.
4. If accepted, record pattern trigger and complexity.
5. If rejected, fix locally and submit once more.
6. If rejected twice, stop and add the failed case to the revisit queue.

## Completion Target

70-80% completion is enough if:
- 2 of 3 new problems are solved or seriously attempted,
- both revision problems are attempted,
- Pivot Index no-pivot case passes,
- at least 1 LeetCode accepted submission is recorded,
- the daily reflection is filled.

## Optional Only If Required Work Is Clean

### Top K Frequent Elements - Sorting Version Re-solve

Target:
- No bucket sort.
- Count frequencies.
- Sort `freq.items()` by count.
- Return first `k` keys.

Time target: 25-30 minutes.

## Daily Reflection

Problems solved independently:

Problems solved after hints:

Problems solved after solution:

Unsolved problems:

What improved today:

Biggest blocker:

Biggest conceptual gap:

What needs repetition tomorrow:

Was today's pace sustainable?

Should tomorrow continue, repeat, or slow down?

Reason:

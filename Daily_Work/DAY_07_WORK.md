# Day 07 Work

Date: 2026-05-13  
Phase: Month 1 - Arrays + Hashing + Strings  
Current week focus: consolidate Day 06 hashing and finally get LeetCode proof before adding more medium volume.

## Today's Realistic Goals

- Complete 3 new problems maximum.
- Complete 2 revision problems.
- Get at least 1 accepted LeetCode submission before optional work.
- Fix Day 06 Pivot Index no-answer bug.
- Keep completion target at 70-80%, not perfection.

## Today's Topic

Clean hash-map implementation, frequency sorting, dictionary grouping recall, and prefix-sum correctness.

## Why This Topic Now

Day 06 showed real improvement:
- Valid Palindrome optimized skip loops were solved independently.
- Majority Element dictionary version was solved independently.
- Pivot Index check-before-add ordering was recalled.

But these remain unstable:
- Group Anagrams was marked solution viewed.
- Top K Frequent Elements needed syntax help, and bucket sort was solution viewed.
- Pivot Index returned `0` instead of `-1` when no pivot exists.
- No LeetCode accepted submission is recorded yet.

## Prerequisites Revision

Write these from memory before coding:

```python
freq[x] = freq.get(x, 0) + 1
key = "".join(sorted(word))
right_sum = total_sum - left_sum - nums[i]
```

Explain:
- Why dictionary lookup is average `O(1)`.
- Why sorting one word of length `k` costs `O(k log k)`.
- Why Top K sorting is `O(n + m log m)`, where `m` is unique values.
- Why Pivot Index must return `-1` if no valid index exists.

## Fundamentals Revision

Write from memory:

```python
def frequency_map(items):
    pass

def sort_items_by_frequency(items):
    pass
```

Expected behavior:

```python
frequency_map([1, 1, 2, 3, 3, 3]) -> {1: 2, 2: 1, 3: 3}
sort_items_by_frequency([1, 1, 2, 3, 3, 3]) -> [3, 1, 2]
```

Complexity:
- `frequency_map`: Time = , Space =
- `sort_items_by_frequency`: Time = , Space =

## Today's New Problems

### 1. Valid Anagram - Clean Hash Version

Topic: Hashing / Strings  
Pattern: Character frequency comparison  
Difficulty: Easy  
LeetCode: Required

Problem:

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

Requirements:
- Do not use `char in t` inside a loop.
- Use dictionary counts or count/decrement.
- Return early if lengths differ.
- Write exact time and space complexity.

Test cases:

```python
s = "anagram", t = "nagaram" -> True
s = "rat", t = "car" -> False
s = "aa", t = "a" -> False
s = "", t = "" -> True
s = "aacc", t = "ccac" -> False
```

Time target: 25-30 minutes.

### 2. Intersection of Two Arrays II

Topic: Hashing / Frequency  
Pattern: Count one list, consume from the other  
Difficulty: Easy  
LeetCode: Recommended

Problem:

Given two integer lists `nums1` and `nums2`, return their intersection including duplicate occurrences.

Example:

```python
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
```

Expected output:

```python
[2, 2]
```

Requirements:
- Count frequencies from one list.
- Traverse the other list.
- Append only when remaining count is positive.
- Decrease the count after using a value.

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

Problem:

Given a string `s`, return a string with characters sorted by decreasing frequency.

Example:

```python
s = "tree"
```

Expected output:

```python
"eert" or "eetr"
```

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

Time target: 35-45 minutes.

## Revision Problems

### Revision 1. Group Anagrams

Why revisit: Day 06 implementation was marked solution viewed.  
Pattern: Sorted string key to dictionary list  
Difficulty: Medium  
LeetCode: Required if clean locally

Rules:
- Do not read Day 06 code first.
- Use `key = "".join(sorted(word))`.
- Append each word to the correct dictionary list.
- Return `list(groups.values())`, not raw `dict_values`.

Test cases:

```python
["eat", "tea", "tan", "ate", "nat", "bat"] -> grouped anagrams
[""] -> [[""]]
["a"] -> [["a"]]
["abc", "bca", "cab", "xyz", "zyx"] -> two groups
```

Time target: 30-35 minutes.

### Revision 2. Find Pivot Index

Why revisit: Day 06 returned `0` instead of `-1` when no pivot exists.  
Pattern: Prefix sum with check-before-update  
Difficulty: Easy

Rules:
- Compute `right_sum`.
- Compare `left_sum == right_sum`.
- Then add current number to `left_sum`.
- Return `-1` after the loop.

Test cases:

```python
[1, 7, 3, 6, 5, 6] -> 3
[1, 2, 3] -> -1
[2, 1, -1] -> 0
[0, 0, 0] -> 0
[-1, -1, 0, 1, 1, 0] -> 5
```

Time target: 15-20 minutes.

## Weak-Pattern Reinforcement

| Weak pattern | Today's rule |
| --- | --- |
| Medium hashing | Count/group first; only then sort or collect output. |
| Group Anagrams | Dictionary value is a list; return `list(groups.values())`. |
| Top K / frequency sorting | Sorting syntax: `sorted(freq.items(), key=lambda item: item[1], reverse=True)`. |
| Pivot Index | If no pivot is found, return `-1`, never default `0`. |
| Complexity | Write `m = unique count` when sorting dictionary items. |
| LeetCode proof | Submit one clean easy before optional medium work. |

## LeetCode Workflow

1. Solve locally first.
2. Run every listed example and one custom edge case.
3. Submit one of: `Valid Anagram`, `Find Pivot Index`, `Valid Palindrome`, or `Group Anagrams`.
4. If accepted, record pattern trigger and complexity.
5. If rejected, fix locally and submit once more.
6. If rejected twice, stop and add the failed case to the revisit queue.

## Completion Target

70-80% completion is enough if:
- 2 of 3 new problems are solved or seriously attempted,
- both revision problems are attempted,
- Pivot Index no-pivot case is fixed,
- at least 1 LeetCode accepted submission is recorded.

## Optional Only If Required Work Is Clean

### Top K Frequent Elements - Sorting Version Re-solve

Why optional today: it needs repetition, but Group Anagrams and Pivot Index are higher-priority fixes.

Target:
- No bucket sort.
- Count frequencies.
- Sort `freq.items()` by count.
- Return first `k` keys.

Time target: 25-30 minutes.

## Daily Reflection

What improved today:

Biggest blocker:

Biggest conceptual gap:

What needs repetition tomorrow:

Was today's pace sustainable?

Should tomorrow continue, repeat, or slow down?

Reason:

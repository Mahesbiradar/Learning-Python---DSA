# Day 04 Work

Date: 2026-05-10  
Phase: Month 1 - Arrays + Hashing + Strings  
Current week focus: stabilize Day 3 hash-map weaknesses, then continue into string traversal and two pointers.

## Today's Realistic Goals

- Complete 3 new problems.
- Complete 2 revision problems.
- Complete prerequisites and fundamentals revision.
- Submit at least 1 clean problem on LeetCode after local solving.
- Target 70-80% completion, not overload.

## Today's Topic

String traversal with two pointers, plus revision of hash-map patterns from Day 03.

## Why This Topic Now

Day 03 showed strong effort and better revision discipline, but the must-cover hashing problems are not mastered yet. Day 04 should continue into strings while reinforcing:
- dictionary complement lookup,
- frequency-map comparison,
- frequency map plus second pass,
- complexity precision,
- LeetCode submission discipline.

## Required Prerequisites

- Python string indexing.
- Python string methods: `.isalnum()` and `.lower()`.
- Left/right two-pointer traversal.
- In-place list swapping.
- Dictionary lookup with `in`.
- `dict.get(key, default)`.
- Frequency-map construction.
- Time and space complexity for string/list traversal.

## Quick Prerequisite Revision Checklist

- [ ] Re-write a frequency counter using `dict.get`.
- [ ] Explain why dictionary lookup is usually O(1).
- [ ] Explain why a frequency dictionary is O(n) space.
- [ ] Write the Two Sum template from memory: check complement first, then store current value/index.
- [ ] Write `sorted(s)` complexity: O(n log n) time, O(n) space in Python.
- [ ] Dry run two pointers on a palindrome string.
- [ ] Practice `.isalnum()` and `.lower()` on at least 5 characters.

## Fundamentals Revision

Task: Write these from memory before starting LeetCode-style problems.

```python
def count_frequency(items):
    pass

def is_plain_palindrome(s):
    pass
```

Checklist:
- [ ] Frequency counter works for list, string, and empty input.
- [ ] Palindrome works for odd length, even length, and empty string.
- [ ] Time and space complexity written for both.

Expected behavior:

```python
count_frequency([1, 2, 1, 3]) -> {1: 2, 2: 1, 3: 1}
count_frequency("apple") -> {"a": 1, "p": 2, "l": 1, "e": 1}
count_frequency([]) -> {}

is_plain_palindrome("madam") -> True
is_plain_palindrome("racecar") -> True
is_plain_palindrome("hello") -> False
is_plain_palindrome("") -> True
```

Solutions:

```python

```

Complexity:
- `count_frequency`: Time = , Space =
- `is_plain_palindrome`: Time = , Space =

## Today's New Problems

### 1. Valid Palindrome

Topic: Strings / Two Pointers  
Pattern: Clean input + left/right pointer  
Difficulty: Easy  
LeetCode: Required

Problem:

Given a string `s`, return `True` if it is a palindrome after converting uppercase letters into lowercase letters and removing all non-alphanumeric characters. Otherwise, return `False`.

A palindrome reads the same forward and backward.

Example:

```python
s = "A man, a plan, a canal: Panama"
```

Expected output:

```python
True
```

Why:

```text
After ignoring spaces, punctuation, and case:
"amanaplanacanalpanama"
This reads the same forward and backward.
```

Example:

```python
s = "race a car"
```

Expected output:

```python
False
```

Why:

```text
After cleaning:
"raceacar"
This does not read the same forward and backward.
```

Input details:
- Input is a string `s`.
- `s` can contain letters, digits, spaces, punctuation, and symbols.
- Uppercase and lowercase versions of the same letter should be treated as equal.

Output details:
- Return `True` if the cleaned string is a palindrome.
- Return `False` otherwise.

Requirements:
- Ignore non-alphanumeric characters.
- Compare lowercase characters.
- Use two pointers.
- Do not build a fully cleaned string for the optimized version.
- Move `left` forward while `s[left]` is not alphanumeric.
- Move `right` backward while `s[right]` is not alphanumeric.

Test cases:

```python
"A man, a plan, a canal: Panama" -> True
"race a car" -> False
" " -> True
"0P" -> False
"Madam" -> True
"No lemon, no melon" -> True
"ab@a" -> True
"abc" -> False
```

Edge cases to remember:
- Empty string or only spaces/punctuation should return `True`.
- Digits count as alphanumeric characters.
- Case must be ignored.
- Pointer movement must not cross incorrectly when skipping symbols.

Time target: 30-40 minutes.

Status:
- [ ] Independent solve
- [ ] Hint used
- [ ] Solution viewed
- [ ] Unsolved

Problem-solving notes:

Dry run:

Brute-force idea:

Optimized idea:

Solution:

```python

```

Time complexity:

Space complexity:

Mistakes/confusions:

Pattern trigger:

LeetCode submission status:
- [ ] Not submitted
- [ ] Accepted
- [ ] Wrong answer
- [ ] Time limit exceeded
- [ ] Revisit required

Revisit requirement:

---

### 2. Reverse String

Topic: Strings / Two Pointers  
Pattern: In-place swap  
Difficulty: Easy  
LeetCode: Recommended

Problem:

Given a list of characters `s`, reverse the list in-place.

You must modify the input list directly and use O(1) extra memory.

Example:

```python
s = ["h", "e", "l", "l", "o"]
```

Expected output:

```python
["o", "l", "l", "e", "h"]
```

Why:

```text
The first and last characters are swapped, then the two pointers move inward.
```

Example:

```python
s = ["H", "a", "n", "n", "a", "h"]
```

Expected output:

```python
["h", "a", "n", "n", "a", "H"]
```

Input details:
- Input is a list of single-character strings.
- The function usually returns nothing on LeetCode.
- The list itself must be changed.

Output details:
- Do not return a new list.
- After the function runs, `s` should be reversed.

Requirements:
- Reverse a list of characters in-place.
- Use left and right pointers.
- Swap `s[left]` and `s[right]`.
- Do not use slicing for the optimized version.
- Do not create another list.

Test cases:

```python
["h", "e", "l", "l", "o"] -> ["o", "l", "l", "e", "h"]
["H", "a", "n", "n", "a", "h"] -> ["h", "a", "n", "n", "a", "H"]
["a"] -> ["a"]
[] -> []
["a", "b"] -> ["b", "a"]
["1", "2", "3"] -> ["3", "2", "1"]
```

Edge cases to remember:
- Empty list should remain empty.
- One-character list should remain unchanged.
- Even and odd lengths both work with `while left < right`.
- The problem wants mutation, not a returned new object.

Time target: 15-20 minutes.

Status:
- [ ] Independent solve
- [ ] Hint used
- [ ] Solution viewed
- [ ] Unsolved

Problem-solving notes:

Dry run:

Brute-force idea:

Optimized idea:

Solution:

```python

```

Time complexity:

Space complexity:

Mistakes/confusions:

Pattern trigger:

LeetCode submission status:
- [ ] Not submitted
- [ ] Accepted
- [ ] Wrong answer
- [ ] Time limit exceeded
- [ ] Revisit required

Revisit requirement:

---

### 3. Is Subsequence

Topic: Strings / Two Pointers  
Pattern: Scan target while matching source pointer  
Difficulty: Easy  
LeetCode: Recommended

Problem:

Given two strings `s` and `t`, return `True` if `s` is a subsequence of `t`, and `False` otherwise.

A subsequence is formed by deleting zero or more characters from another string without changing the order of the remaining characters.

Example:

```python
s = "abc"
t = "ahbgdc"
```

Expected output:

```python
True
```

Why:

```text
"a", "b", and "c" appear in `t` in the same order.
```

Example:

```python
s = "axc"
t = "ahbgdc"
```

Expected output:

```python
False
```

Why:

```text
"a" and "c" appear, but "x" does not appear between them in order.
```

Input details:
- Input `s` is the string you are trying to match.
- Input `t` is the string you are scanning.
- Both strings may be empty.

Output details:
- Return `True` if all characters of `s` are found in `t` in order.
- Return `False` otherwise.

Requirements:
- Use two pointers.
- One pointer tracks the current character in `s`.
- One pointer scans through `t`.
- Move the `s` pointer only when there is a match.
- Handle empty `s`.

Test cases:

```python
s = "abc", t = "ahbgdc" -> True
s = "axc", t = "ahbgdc" -> False
s = "", t = "ahbgdc" -> True
s = "abc", t = "" -> False
s = "ace", t = "abcde" -> True
s = "aec", t = "abcde" -> False
s = "aaaaaa", t = "bbaaaa" -> False
```

Edge cases to remember:
- Empty `s` is always a subsequence.
- Non-empty `s` cannot be a subsequence of empty `t`.
- Matching must preserve order.
- Repeated characters require enough repeated matches in `t`.

Time target: 30-40 minutes.

Status:
- [ ] Independent solve
- [ ] Hint used
- [ ] Solution viewed
- [ ] Unsolved

Problem-solving notes:

Dry run:

Brute-force idea:

Optimized idea:

Solution:

```python

```

Time complexity:

Space complexity:

Mistakes/confusions:

Pattern trigger:

LeetCode submission status:
- [ ] Not submitted
- [ ] Accepted
- [ ] Wrong answer
- [ ] Time limit exceeded
- [ ] Revisit required

Revisit requirement:

## Revision Problems

### Revision 1. Two Sum

Why revisit: Day 03 optimized solution required solution help for `seen[nums[i]] = i`.  
Pattern: Dictionary complement lookup  
Difficulty: Easy  
LeetCode: Required

Problem:

Given a list of integers `nums` and an integer `target`, return the indexes of the two numbers such that they add up to `target`.

You may assume that each input has exactly one valid answer, and you may not use the same element twice.

Example:

```python
nums = [2, 7, 11, 15]
target = 9
```

Expected output:

```python
[0, 1]
```

Why:

```text
nums[0] + nums[1] = 2 + 7 = 9
```

Input details:
- `nums` is a list of integers.
- `target` is an integer.
- Values may be positive, negative, or zero.
- The same value may appear more than once.

Output details:
- Return a list of two indexes.
- Index order usually does not matter unless the platform expects a specific answer.

Rules:
- First write brute force in words only.
- Then write optimized code from memory.
- Store numbers you have already seen with their index.
- For each number, check whether `target - current_number` already exists.
- Check complement before storing current value.
- Do not use the same index twice.
- Submit on LeetCode if local tests pass.

Test cases:

```python
[2, 7, 11, 15], target = 9 -> [0, 1]
[3, 2, 4], target = 6 -> [1, 2]
[3, 3], target = 6 -> [0, 1]
[-1, -2, -3, -4, -5], target = -8 -> [2, 4]
[0, 4, 3, 0], target = 0 -> [0, 3]
```

Edge cases to remember:
- Duplicate values can be the correct answer.
- Negative values work the same way.
- Zero plus zero requires two separate indexes.
- Store index, not just value.

Time target: 25 minutes.

Status:
- [ ] Independent re-solve
- [ ] Hint used
- [ ] Solution viewed
- [ ] Unsolved

Dry run:

Brute-force idea:

Optimized idea:

Solution:

```python

```

Time complexity:

Space complexity:

Mistakes/confusions:

Pattern trigger:

LeetCode submission status:
- [ ] Not submitted
- [ ] Accepted
- [ ] Wrong answer
- [ ] Time limit exceeded
- [ ] Revisit required

Revisit again?
- [ ] No
- [ ] 3 days
- [ ] 7 days

---

### Revision 2. First Unique Character OR Valid Anagram

Choose the one that feels weaker after warm-up.

## Option A: First Unique Character

Why revisit: Day 03 optimized second pass needed a hint.  
Pattern: Frequency map + second pass  
Difficulty: Easy  
LeetCode: Required

Problem:

Given a string `s`, return the index of the first non-repeating character.

If every character repeats, return `-1`.

Example:

```python
s = "leetcode"
```

Expected output:

```python
0
```

Why:

```text
"l" appears only once and is the first unique character.
```

Input details:
- Input is a string `s`.
- The string may be empty.
- Characters can repeat.

Output details:
- Return the index of the first character whose count is `1`.
- Return `-1` if no unique character exists.

Requirements:
- First write the brute-force nested-loop idea.
- Then solve using a frequency dictionary.
- First pass: count every character.
- Second pass: scan the original string by index.
- Return the first index whose character count is `1`.

Test cases:

```python
"leetcode" -> 0
"loveleetcode" -> 2
"aabb" -> -1
"z" -> 0
"" -> -1
"dddccdbba" -> 8
```

Edge cases to remember:
- Empty string returns `-1`.
- One-character string returns `0`.
- Do not return the first key in the dictionary; scan original order.
- Character count must be exactly `1`.

Dry run:

Brute-force idea:

Optimized idea:

Solution:

```python

```

Time complexity:

Space complexity:

Mistakes/confusions:

## Option B: Valid Anagram

Why revisit: Day 03 hash-map comparison needed a hint and sorting complexity was unclear.  
Pattern: Character frequency comparison  
Difficulty: Easy  
LeetCode: Required

Problem:

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

An anagram means both strings contain the same characters with the same frequency, but possibly in a different order.

Example:

```python
s = "anagram"
t = "nagaram"
```

Expected output:

```python
True
```

Example:

```python
s = "rat"
t = "car"
```

Expected output:

```python
False
```

Input details:
- Inputs are two strings, `s` and `t`.
- Lengths may be different.
- Characters may repeat.

Output details:
- Return `True` only if both strings have exactly the same character counts.
- Return `False` otherwise.

Requirements:
- First write the brute-force/sorting idea.
- Then solve using a dictionary frequency map.
- If lengths are different, return `False` immediately.
- Count characters in `s`.
- Decrease counts using characters from `t`.
- If any needed character is missing or count becomes negative, return `False`.

Test cases:

```python
"anagram", "nagaram" -> True
"rat", "car" -> False
"a", "a" -> True
"a", "ab" -> False
"listen", "silent" -> True
"aa", "a" -> False
```

Edge cases to remember:
- Different lengths cannot be anagrams.
- Same letters with different counts are not anagrams.
- Sorting approach is simpler but costs O(n log n).
- Hash-map approach is O(n) time with O(n) space.

Dry run:

Brute-force idea:

Optimized idea:

Solution:

```python

```

Time target: 20-25 minutes.

Status:
- [ ] Independent re-solve
- [ ] Hint used
- [ ] Solution viewed
- [ ] Unsolved

Time complexity:

Space complexity:

Mistakes/confusions:

Pattern trigger:

LeetCode submission status:
- [ ] Not submitted
- [ ] Accepted
- [ ] Wrong answer
- [ ] Time limit exceeded
- [ ] Revisit required

Revisit again?
- [ ] No
- [ ] 3 days
- [ ] 7 days

## Revision Reminders

- Re-solve without reading old code first.
- Write the pattern trigger before writing code.
- If stuck, take only one hint, then close it and reattempt.
- Do not mark a revision problem mastered unless solved independently today.

## Re-Solving Reminders

- Start with a tiny example.
- Dry run variables manually.
- Code after the dry run, not before.
- Compare with old solution only after finishing.

## Problem-Solving Notes

General notes for today:

## Dry Runs

Use this space for manual traces:

```text

```

## Brute-Force Ideas

Use this space to compare brute-force approaches:

```text

```

## Optimized Ideas

Use this space to compare optimized approaches:

```text

```

## Mistakes / Confusions

- 

## Pattern-Recognition Notes

| Trigger in problem | Pattern to try | Example |
| --- | --- | --- |
| Need compare from both ends | Two pointers | Valid Palindrome |
| Need reverse in-place | Two pointers + swap | Reverse String |
| Need preserve order while matching | Two pointers / subsequence scan | Is Subsequence |
| Need pair that sums to target | Dictionary complement lookup | Two Sum |
| Need first item with count 1 | Frequency map + second pass | First Unique Character |
| Need compare character counts | Frequency map | Valid Anagram |

## Time And Space Complexity

| Problem | Time | Space | Correct? |
| --- | --- | --- | --- |
| Fundamentals frequency counter |  |  |  |
| Plain palindrome |  |  |  |
| Valid Palindrome |  |  |  |
| Reverse String |  |  |  |
| Is Subsequence |  |  |  |
| Two Sum revision |  |  |  |
| First Unique OR Valid Anagram revision |  |  |  |

## LeetCode Submission Status

| Problem | Submitted? | Result | Notes |
| --- | --- | --- | --- |
| Valid Palindrome |  |  |  |
| Reverse String |  |  |  |
| Is Subsequence |  |  |  |
| Two Sum |  |  | Revision problem |
| First Unique Character OR Valid Anagram |  |  | Revision problem |

## Revisit-Required Problems

Move any problem here if:
- hint was used,
- solution was viewed,
- complexity was wrong,
- implementation was unstable,
- pattern trigger was unclear.

| Problem | Reason | Next revisit |
| --- | --- | --- |
|  |  |  |

## Weak-Pattern Reinforcement

| Weak pattern | Today's rule |
| --- | --- |
| Complement lookup | Store current value/index after checking needed value. |
| Frequency + first index | Count first, then scan the original string by index. |
| Frequency comparison | Compare counts, not just membership. |
| Complexity precision | Write time/space before checking notes. |
| String skipping | Move pointers carefully while skipping invalid characters. |

## LeetCode Workflow

1. Solve locally first.
2. Run all examples and one custom edge case.
3. Submit once.
4. If accepted, write the trigger and complexity.
5. If rejected, fix locally and submit once more.
6. If rejected twice, stop and add the exact issue to the revisit queue.

## Completion Target

70-80% completion is enough if:
- 3 new problems are attempted,
- 2 revision problems are attempted,
- at least 1 problem is accepted on LeetCode,
- no full solution is viewed unless truly stuck after a real attempt.

## Daily Reflection

What went well:

What felt weak:

Which pattern became clearer:

Which problem needs another re-solve:

Should tomorrow continue, repeat, or slow down?

Reason:

## Time Spent

| Activity | Time spent |
| --- | ---: |
| Prerequisites revision |  |
| Fundamentals revision |  |
| New problem 1 |  |
| New problem 2 |  |
| New problem 3 |  |
| Revision problem 1 |  |
| Revision problem 2 |  |
| LeetCode submissions |  |
| Notes and tracker update |  |
| Total |  |

## What Needs Repetition Tomorrow

- Two Sum dictionary storage.
- First Unique second pass over original order.
- Valid Anagram complexity and dictionary comparison.
- String two-pointer mechanics.
- Clean complexity notes.

## What Should Be Updated After Finishing Today?

Update only the existing system files:

- `DSA_PROGRESS_TRACKER.md`
  - daily log,
  - independent/hint/solution counts,
  - weak patterns,
  - revision completion,
  - next-day decision.

- `PROBLEMS.md`
  - revisit queue,
  - problem status,
  - mastery status.

- `WEEK_01_EXECUTION_PLAN.md` if needed
  - adjust tomorrow's focus only if today's result changes pacing.

Also update:
- Revisit queue.
- Mastery status.
- Weak-pattern notes.
- LeetCode status.

# Day 06 Work

Date: 2026-05-12  
Phase: Month 1 - Arrays + Hashing + Strings  
Current week focus: keep placement roadmap moving while stabilizing Day 05 prefix/running-state and Day 04 two-pointer weaknesses.

## Today's Realistic Goals

- Complete 3 new problems maximum.
- Complete 2 revision problems.
- Get at least 1 accepted LeetCode submission before optional work.
- Keep completion target at 70-80%, not perfection.
- Stop optional work if Valid Palindrome or Pivot Index is still unstable.

## Today's Topic

Dictionary grouping, frequency ranking, and controlled revision of prefix-sum and string two-pointer patterns.

## Why This Topic Now

Day 05 improved running-sum and stock-profit confidence, but these areas still need proof:
- LeetCode submissions are behind.
- Pivot Index check-before-update ordering is fragile.
- Valid Palindrome skip loops still required hints.
- Product Except Self is not yet at the target output-array + suffix form.

Day 06 should move into Week 2-style hashing carefully, without abandoning revision.

## Prerequisites Revision

- Re-write `freq[x] = freq.get(x, 0) + 1`.
- Explain why dictionary key lookup is average `O(1)`.
- Explain why `sorted(word)` costs `O(k log k)` for a word of length `k`.
- Dry run Pivot Index using:

```python
[2, 1, -1] -> 0
[0, 0, 0] -> 0
```

- Re-write the Valid Palindrome skip-loop template:

```python
while left < right and not s[left].isalnum():
    left += 1
while left < right and not s[right].isalnum():
    right -= 1
```

## Fundamentals Revision

Write from memory before new problems:

```python
def count_frequency(nums):
    pass

def group_words_by_sorted_key(words):
    pass
```

Expected behavior:

```python
count_frequency([1, 2, 2, 3, 1]) -> {1: 2, 2: 2, 3: 1}
group_words_by_sorted_key(["eat", "tea", "tan", "ate"]) -> {"aet": ["eat", "tea", "ate"], "ant": ["tan"]}
```

Complexity:
- `count_frequency`: Time = , Space =
- `group_words_by_sorted_key`: Time = , Space =

## Today's New Problems

### 1. Group Anagrams

Topic: Hashing / Grouping  
Pattern: Sorted string key or character-count key  
Difficulty: Medium  
LeetCode: Required

Problem:

Given a list of strings `strs`, group words that are anagrams of each other. Return the groups in any order.

Two words are anagrams if they contain the same characters with the same frequencies, but possibly in a different order.

Example:

```python
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

Expected output:

```python
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

Why:

```text
"eat", "tea", and "ate" all become "aet" when sorted.
"tan" and "nat" both become "ant" when sorted.
"bat" becomes "abt" and has no matching word.
```

Requirements:
- Use a dictionary where each key maps to a list of words.
- First use sorted-string key.
- Write time complexity carefully.
- Submit on LeetCode after local examples pass.

Test cases:

```python
["eat", "tea", "tan", "ate", "nat", "bat"] -> groups of ["eat","tea","ate"], ["tan","nat"], ["bat"]
[""] -> [[""]]
["a"] -> [["a"]]
["abc", "bca", "cab", "xyz", "zyx"] -> groups of ["abc","bca","cab"], ["xyz","zyx"]
["bob", "obb", "boo"] -> groups of ["bob","obb"], ["boo"]
```

Edge cases:
- Empty string is a valid word.
- A single word returns one group.
- Output group order does not matter.
- Word order inside each group usually does not matter for LeetCode.
- Sorting each word costs extra time.

Time target: 40-50 minutes.

Status:
- [ ] Independent solve
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

---

### 2. Top K Frequent Elements

Topic: Hashing / Frequency  
Pattern: Count frequencies, then select top `k`  
Difficulty: Medium  
LeetCode: Required

Problem:

Given an integer list `nums` and an integer `k`, return the `k` most frequent elements. The answer can be returned in any order.

Example:

```python
nums = [1, 1, 1, 2, 2, 3]
k = 2
```

Expected output:

```python
[1, 2]
```

Why:

```text
1 appears 3 times.
2 appears 2 times.
3 appears 1 time.
The top 2 most frequent values are 1 and 2.
```

Requirements:
- Build a frequency dictionary.
- First solve using sorting by frequency.
- If time remains, read bucket-sort idea only after your own version works.

Test cases:

```python
nums = [1, 1, 1, 2, 2, 3], k = 2 -> [1, 2]
nums = [1], k = 1 -> [1]
nums = [4, 4, 4, 6, 6, 7], k = 1 -> [4]
nums = [-1, -1, 2, 2, 2, 3], k = 2 -> [2, -1]
nums = [5, 3, 5, 3, 2], k = 2 -> [5, 3] in any order
```

Edge cases:
- `k` can be `1`.
- Negative numbers are allowed.
- Multiple answers may be valid when frequencies tie.
- Return elements, not frequencies.
- Sorting dictionary items by count is acceptable for the first solution.

Time target: 45-55 minutes.

Status:
- [ ] Independent solve
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

---

### 3. Majority Element

Topic: Arrays / Frequency or Voting  
Pattern: Frequency count first, Boyer-Moore optional  
Difficulty: Easy  
LeetCode: Recommended

Problem:

Given a non-empty integer list `nums`, return the element that appears more than `n // 2` times. You may assume the majority element always exists.

Example:

```python
nums = [3, 2, 3]
```

Expected output:

```python
3
```

Why:

```text
n = 3
n // 2 = 1
3 appears 2 times, and 2 > 1.
```

Requirements:
- Solve with dictionary count.
- Explain why majority means count `> n // 2`.
- Try Boyer-Moore only if time/energy remains.

Test cases:

```python
[3, 2, 3] -> 3
[2, 2, 1, 1, 1, 2, 2] -> 2
[1] -> 1
[-1, -1, -1, 2, 3] -> -1
[6, 6, 6, 6, 7, 7, 7] -> 6
```

Edge cases:
- One-element list.
- Negative numbers.
- Majority count must be strictly greater than `n // 2`.
- The problem guarantees a majority exists, so no special "not found" return is needed on LeetCode.

Time target: 25-35 minutes.

Status:
- [ ] Independent solve
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

## Revision Problems

### Revision 1. Find Pivot Index

Why revisit: Day 05 optimal version worked, but compare-before-add placement was confusing.  
Pattern: Prefix sum with derived right sum  
Difficulty: Easy

Rules:
- Do not use old code.
- Dry run first.
- At each index: compute right sum, compare, then add current value to left sum.

Problem:

Given a list `nums`, return the leftmost index where the sum of all values to the left equals the sum of all values to the right. If no such index exists, return `-1`.

Example:

```python
nums = [1, 7, 3, 6, 5, 6]
```

Expected output:

```python
3
```

Why:

```text
Left of index 3: 1 + 7 + 3 = 11
Right of index 3: 5 + 6 = 11
```

Test cases:

```python
[1, 7, 3, 6, 5, 6] -> 3
[1, 2, 3] -> -1
[2, 1, -1] -> 0
[0, 0, 0] -> 0
[-1, -1, 0, 1, 1, 0] -> 5
```

Edge cases:
- Pivot can be index `0`.
- Pivot can be the last index.
- Zeroes can create many valid pivots; return the leftmost one.
- Negative numbers are allowed.

Time target: 20 minutes.

Status:
- [ ] Independent re-solve
- [ ] Hint used
- [ ] Solution viewed
- [ ] Unsolved

Solution:

```python

```

Time complexity:

Space complexity:

Revisit again?
- [ ] No
- [ ] 3 days
- [ ] 7 days

---

### Revision 2. Valid Palindrome

Why revisit: Day 05 still used hints for optimized skip loops.  
Pattern: Two pointers with skip loops  
Difficulty: Easy  
LeetCode: Required if clean locally

Rules:
- No cleaned-string extra-list version first.
- Skip invalid characters before comparing.
- Compare lowercase characters.

Problem:

Given a string `s`, return `True` if it is a palindrome after converting uppercase letters to lowercase and removing all non-alphanumeric characters. Otherwise, return `False`.

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
After ignoring spaces, punctuation, and capitalization:
"amanaplanacanalpanama"

This reads the same forward and backward.
```

Test cases:

```python
"A man, a plan, a canal: Panama" -> True
"race a car" -> False
" " -> True
"0P" -> False
"No lemon, no melon" -> True
".,," -> True
```

Edge cases:
- Empty or punctuation-only string should return `True`.
- Digits count as alphanumeric.
- Case should not matter.
- Do not compare characters until both pointers are on valid alphanumeric characters.

Time target: 25 minutes.

Status:
- [ ] Independent re-solve
- [ ] Hint used
- [ ] Solution viewed
- [ ] Unsolved

Solution:

```python

```

Time complexity:

Space complexity:

Revisit again?
- [ ] No
- [ ] 3 days
- [ ] 7 days

## Weak-Pattern Reinforcement

| Weak pattern | Today's rule |
| --- | --- |
| Pivot Index | Compare before adding current value to `left_sum`. |
| Valid Palindrome | Skip invalid characters before comparison. |
| Grouping | Dictionary value can be a list; append words into the right group. |
| Frequency ranking | Count first; selection/ranking is a separate step. |
| Complexity | Sorting each word is not free; include it in total complexity. |
| LeetCode proof | Submit one clean problem before optional tasks. |

## LeetCode Workflow

1. Solve locally first.
2. Run all listed examples and one custom edge case.
3. Submit one of: `Best Time To Buy And Sell Stock`, `Group Anagrams`, `Top K Frequent Elements`, or `Valid Palindrome`.
4. If accepted, record pattern trigger and complexity.
5. If rejected, fix locally and submit once more.
6. If rejected twice, stop and add the exact failed case to the revisit queue.

## Completion Target

70-80% completion is enough if:
- 2 of 3 new problems are solved or seriously attempted,
- both revision problems are attempted,
- at least 1 LeetCode accepted submission is recorded,
- no optional problem is attempted before LeetCode proof.

## Daily Reflection

What improved today:

Biggest blocker:

Biggest conceptual gap:

What needs repetition tomorrow:

Was today's pace sustainable?

Should tomorrow continue, repeat, or slow down?

Reason:

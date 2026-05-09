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

## Why This Plan

Day 03 showed strong effort and better revision discipline, but the must-cover hashing problems are not mastered yet. The next day should continue strings while reinforcing:
- dictionary complement lookup,
- frequency-map comparison,
- frequency map plus second pass,
- complexity precision,
- LeetCode submission discipline.

## Prerequisites Revision

Time target: 30 minutes total.

- [ ] Re-write a frequency counter using `dict.get`.
- [ ] Explain why dictionary lookup is usually O(1).
- [ ] Explain why a frequency dictionary is O(n) space.
- [ ] Write the Two Sum template from memory: check complement first, then store current value/index.
- [ ] Write `sorted(s)` complexity: O(n log n) time, O(n) space in Python.
- [ ] Dry run two pointers on a palindrome string.

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

## New Problems

### 1. Valid Palindrome

Topic: Strings / Two Pointers  
Pattern: Clean input + left/right pointer  
LeetCode: Required

Requirements:
- Ignore non-alphanumeric characters.
- Compare lowercase characters.
- Use two pointers.
- Do not build a fully cleaned string for the optimized version.

Time target: 30-40 minutes.

Status:
- [ ] Independent solve
- [ ] Hint used
- [ ] Solution viewed
- [ ] Unsolved

Complexity:

Mistakes/confusions:

LeetCode:
- [ ] Not submitted
- [ ] Accepted
- [ ] Revisit required

---

### 2. Reverse String

Topic: Strings / Two Pointers  
Pattern: In-place swap  
LeetCode: Recommended

Requirements:
- Reverse a list of characters in-place.
- Use left and right pointers.
- Do not return a new list.

Time target: 15-20 minutes.

Status:
- [ ] Independent solve
- [ ] Hint used
- [ ] Solution viewed
- [ ] Unsolved

Complexity:

Mistakes/confusions:

---

### 3. Is Subsequence

Topic: Strings / Two Pointers  
Pattern: Scan target while matching source pointer  
LeetCode: Recommended

Requirements:
- Determine whether `s` is a subsequence of `t`.
- Use two pointers.
- Handle empty `s`.

Time target: 30-40 minutes.

Status:
- [ ] Independent solve
- [ ] Hint used
- [ ] Solution viewed
- [ ] Unsolved

Complexity:

Mistakes/confusions:

## Revision Problems

### Revision 1. Two Sum

Why revisit: Day 03 optimized solution required solution help for `seen[nums[i]] = i`.

Time target: 25 minutes.

Rules:
- First write brute force in words only.
- Then write optimized code from memory.
- Check complement before storing current value.
- Submit on LeetCode if local tests pass.

Status:
- [ ] Independent re-solve
- [ ] Hint used
- [ ] Solution viewed
- [ ] Unsolved

Revisit again?
- [ ] No
- [ ] 3 days
- [ ] 7 days

---

### Revision 2. First Unique Character OR Valid Anagram

Choose the one that feels weaker after warm-up.

Option A: First Unique Character  
Why revisit: Day 03 optimized second pass needed a hint.

Option B: Valid Anagram  
Why revisit: Day 03 hash-map comparison needed a hint and sorting complexity was unclear.

Time target: 20-25 minutes.

Status:
- [ ] Independent re-solve
- [ ] Hint used
- [ ] Solution viewed
- [ ] Unsolved

Revisit again?
- [ ] No
- [ ] 3 days
- [ ] 7 days

## Weak-Pattern Reinforcement

| Weak pattern | Tomorrow's rule |
| --- | --- |
| Complement lookup | Store current value/index after checking needed value. |
| Frequency + first index | Count first, then scan the original string by index. |
| Frequency comparison | Compare counts, not just membership. |
| Complexity precision | Write time/space before checking notes. |
| Prefix/suffix | No new prefix/suffix problem tomorrow; only light recall if time remains. |

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

## What Needs Repetition Tomorrow

- Two Sum dictionary storage.
- First Unique second pass over original order.
- Valid Anagram complexity and dictionary comparison.
- String two-pointer mechanics.
- Clean complexity notes.


# Day 05 Work

Date: 2026-05-11  
Phase: Month 1 - Arrays + Hashing + Strings  
Current week focus: stabilize Day 04 string two-pointer weaknesses while rebuilding prefix/suffix and running-state confidence.

## Today's Realistic Goals

- Complete 3 new problems.
- Complete 2 revision problems.
- Submit at least 1 clean solution on LeetCode.
- Keep completion target at 70-80%, not perfection.
- Skip optional medium work unless required items are clean.

## Today's Topic

Prefix basics, pivot reasoning, one-pass running minimum, and 24-hour string two-pointer recall.

## Why This Topic Now

Day 04 improved several Day 03 weak areas, especially Two Sum and First Unique Character. The biggest blockers now are:
- Valid Palindrome optimized skip loops,
- Is Subsequence match-pointer movement,
- Valid Anagram optimized complexity discipline,
- missing LeetCode submission proof,
- older Day 02 instability around prefix/suffix and running-state problems.

Day 05 should continue forward, but gently. The priority is clean recall and one accepted submission.

## Required Prerequisites

- Forward traversal with a running total.
- Reverse traversal with a running value.
- Prefix sum meaning: value accumulated before/current index.
- Suffix meaning: value accumulated after/current index.
- One-pass minimum tracking.
- String `.isalnum()` and `.lower()`.
- Two-pointer skip loops.
- Subsequence scan with one match pointer.

## Quick Prerequisite Revision Checklist

- [ ] Write prefix sums for `[1, 2, 3, 4]`.
- [ ] Write left sum and right sum around index `2` for `[1, 7, 3, 6, 5, 6]`.
- [ ] Explain `min_price` and `max_profit` in Best Time to Buy/Sell Stock.
- [ ] Dry run Valid Palindrome on `"A man, a plan, a canal: Panama"`.
- [ ] Dry run Is Subsequence on `s = "abc"`, `t = "ahbgdc"`.
- [ ] Write why `char in dictionary` is O(1) average, but `char in string` is O(n).

## Fundamentals Revision

Task: Write these from memory before LeetCode-style problems.

```python
def running_sum(nums):
    pass

def clean_hash_anagram(s, t):
    pass
```

Checklist:
- [ ] Running sum handles empty list.
- [ ] Running sum does not overwrite needed values incorrectly.
- [ ] Anagram version uses dictionary membership/comparison, not string membership inside a loop.
- [ ] Time and space complexity written for both.

Expected behavior:

```python
running_sum([1, 2, 3, 4]) -> [1, 3, 6, 10]
running_sum([]) -> []

clean_hash_anagram("anagram", "nagaram") -> True
clean_hash_anagram("rat", "car") -> False
clean_hash_anagram("aa", "a") -> False
```

Solutions:

```python

```

Complexity:
- `running_sum`: Time = , Space =
- `clean_hash_anagram`: Time = , Space =

## Today's New Problems

### 1. Running Sum of 1d Array

Topic: Arrays / Prefix Sum  
Pattern: Running total  
Difficulty: Easy  
LeetCode: Recommended

Problem:

Given a list `nums`, return a list where each index contains the sum of all values from index `0` to that index.

Example:

```python
nums = [1, 2, 3, 4]
```

Expected output:

```python
[1, 3, 6, 10]
```

Why:

```text
1
1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 4 = 10
```

Requirements:
- Use a running total.
- Return a new list first.
- Then try the in-place version if time remains.
- Write time and space complexity for both versions.

Test cases:

```python
[1, 2, 3, 4] -> [1, 3, 6, 10]
[1, 1, 1, 1, 1] -> [1, 2, 3, 4, 5]
[3, 1, 2, 10, 1] -> [3, 4, 6, 16, 17]
[] -> []
[-1, 2, -3, 4] -> [-1, 1, -2, 2]
```

Edge cases:
- Empty list.
- Negative values.
- One-element list.

Time target: 15-20 minutes.

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

### 2. Find Pivot Index

Topic: Arrays / Prefix Sum  
Pattern: Left sum equals right sum  
Difficulty: Easy  
LeetCode: Recommended

Problem:

Given a list `nums`, return the leftmost index where the sum of values to the left equals the sum of values to the right. If no such index exists, return `-1`.

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

Requirements:
- First write the brute-force idea.
- Then solve using `total_sum` and `left_sum`.
- At each index, compute `right_sum = total_sum - left_sum - nums[i]`.
- Check before adding current value to `left_sum`.

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
- Zeroes and negative numbers are allowed.
- Return the leftmost valid pivot.

Time target: 30-40 minutes.

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

### 3. Best Time To Buy And Sell Stock

Topic: Arrays / Running State  
Pattern: One-pass minimum tracking  
Difficulty: Easy  
LeetCode: Required

Problem:

Given a list `prices`, where `prices[i]` is the stock price on day `i`, return the maximum profit from buying once and selling once later. If no profit is possible, return `0`.

Example:

```python
prices = [7, 1, 5, 3, 6, 4]
```

Expected output:

```python
5
```

Why:

```text
Buy at 1 and sell at 6.
Profit = 6 - 1 = 5
```

Requirements:
- First write the brute-force nested-loop idea.
- Then solve in one pass.
- Track the lowest price seen so far.
- Track the best profit seen so far.
- Never sell before buying.

Test cases:

```python
[7, 1, 5, 3, 6, 4] -> 5
[7, 6, 4, 3, 1] -> 0
[1, 2] -> 1
[2, 1, 2, 1, 0, 1, 2] -> 2
[3] -> 0
```

Edge cases:
- Prices always decreasing.
- One price only.
- Best buy can appear after several high values.
- Later lower price should update `min_price`.

Time target: 30-40 minutes.

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

### Revision 1. Valid Palindrome

Why revisit: Day 04 optimized version needed hint/solution exposure for inner skip loops.  
Pattern: Two pointers with skip loops  
Difficulty: Easy  
LeetCode: Required

Rules:
- Do not read yesterday's code first.
- Dry run before coding.
- Use `while left < right and not s[left].isalnum()` for skipping.
- Compare lowercase characters.
- Submit on LeetCode only after local examples pass.

Test cases:

```python
"A man, a plan, a canal: Panama" -> True
"race a car" -> False
" " -> True
"0P" -> False
"No lemon, no melon" -> True
```

Time target: 25-30 minutes.

Status:
- [ ] Independent re-solve
- [ ] Hint used
- [ ] Solution viewed
- [ ] Unsolved

Solution:

```python

```

Revisit again?
- [ ] No
- [ ] 3 days
- [ ] 7 days

---

### Revision 2. Is Subsequence

Why revisit: Day 04 required repeated hints for match-pointer placement.  
Pattern: Scan `t`, advance `s` pointer only on match  
Difficulty: Easy  
LeetCode: Recommended

Rules:
- Do not use nested loops.
- Use one pointer for `s`.
- Loop through characters of `t`.
- Check completion inside the loop and after the loop.

Test cases:

```python
s = "abc", t = "ahbgdc" -> True
s = "axc", t = "ahbgdc" -> False
s = "", t = "ahbgdc" -> True
s = "abc", t = "" -> False
s = "aaaaaa", t = "bbaaaa" -> False
```

Time target: 20-25 minutes.

Status:
- [ ] Independent re-solve
- [ ] Hint used
- [ ] Solution viewed
- [ ] Unsolved

Solution:

```python

```

Revisit again?
- [ ] No
- [ ] 3 days
- [ ] 7 days

## Optional Only If Required Work Is Clean

### Product Of Array Except Self

Why optional: This remains important, but Day 05 should not overload before LeetCode proof and Day 04 recall.

Target version:
- Output array for prefix products.
- One running suffix variable.
- No division.
- O(n) time.
- O(1) extra space beyond output.

Time target: 35-45 minutes only if all required tasks are finished.

## Weak-Pattern Reinforcement

| Weak pattern | Today's rule |
| --- | --- |
| Valid Palindrome skip loops | Skip invalid characters before comparing. |
| Subsequence scan | Scan `t`; advance `s` pointer only on match. |
| Prefix/pivot reasoning | Check current index using left sum before adding current value. |
| Running minimum | Update `min_price`; profit is current price minus previous minimum. |
| Complexity discipline | Dictionary membership is average O(1); string/list membership is O(n). |
| LeetCode proof | One accepted submission is required before optional work. |

## LeetCode Workflow

1. Solve locally first.
2. Run every listed example and one custom edge case.
3. Submit once after local tests pass.
4. If accepted, write the pattern trigger and complexity.
5. If rejected, fix locally and submit once more.
6. If rejected twice, stop and add the exact issue to the revisit queue.

## Completion Target

70-80% completion is enough if:
- 3 new problems are attempted,
- 2 revision problems are attempted,
- at least 1 problem is accepted on LeetCode,
- Product Except Self is skipped if the required work is not clean.

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
| "running sum", "sum so far" | Prefix sum | Running Sum |
| "left sum equals right sum" | Total sum minus left/current | Pivot Index |
| "buy before sell", "max profit" | One-pass min tracking | Best Time to Buy/Sell Stock |
| "ignore punctuation", "palindrome" | Two pointers with skip loops | Valid Palindrome |
| "subsequence", "same order" | One scan with match pointer | Is Subsequence |

## Time And Space Complexity

| Problem | Time | Space | Correct? |
| --- | --- | --- | --- |
| Fundamentals running sum |  |  |  |
| Fundamentals clean hash anagram |  |  |  |
| Running Sum |  |  |  |
| Pivot Index |  |  |  |
| Best Time To Buy/Sell Stock |  |  |  |
| Valid Palindrome revision |  |  |  |
| Is Subsequence revision |  |  |  |

## LeetCode Submission Status

| Problem | Submitted? | Result | Notes |
| --- | --- | --- | --- |
| Running Sum |  |  |  |
| Pivot Index |  |  |  |
| Best Time To Buy/Sell Stock |  |  | Required |
| Valid Palindrome |  |  | Required if clean locally |
| Is Subsequence |  |  | Revision |

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

## Daily Reflection

What improved today:

Biggest blocker:

Biggest conceptual gap:

Which problem needs repetition tomorrow:

Was today's pace sustainable?

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

- `WEEK_01_EXECUTION_PLAN.md` if today's result changes pacing.

Also update:
- Revisit queue.
- Mastery status.
- Weak-pattern notes.
- LeetCode status.

## End-Of-Day Analysis

### Completion Summary

Problems attempted: 7 total  
Independent solves: Running Sum fundamentals, clean hash anagram after self-debug, Running Sum new-list and in-place, Pivot Index brute force and optimal, Best Time To Buy/Sell Stock brute force and optimal, Is Subsequence revision, Product Except Self two-array version  
Solved after hints: Valid Palindrome revision  
Solved after solution: None visible today  
Unsolved: None locally, but Product Except Self target optimized-space version remains incomplete

LeetCode status: no accepted submission recorded.

### What Improved Today

- Running total / prefix basics improved strongly.
- Best Time To Buy/Sell Stock improved from earlier help-needed status to independent one-pass implementation.
- Brute-force-first discipline stayed consistent.
- Edge cases were tested more carefully than earlier days: empty lists, negative values, decreasing stock prices, zero arrays, and one-element stock prices.

### Biggest Blockers

- Valid Palindrome optimized skip-loop flow still needed hints.
- LeetCode submission discipline is still behind the roadmap.
- Product Except Self still has not reached the expected output-array + one suffix variable implementation.

### Biggest Conceptual Gaps

- Check-before-update ordering in Pivot Index.
- Difference between dictionary membership and string/list membership for complexity.
- Knowing when a two-pointer/subsequence problem should avoid membership/frequency checks.
- Counting output array as allowed space in Product Except Self, while extra left/right arrays are not optimal.

### Revisit Required

| Problem | Reason | Next revisit |
| --- | --- | --- |
| Valid Palindrome | Hint still needed for skip loops | Day 06 |
| Find Pivot Index | Optimal update order was confusing | Day 06 |
| Product Of Array Except Self | Used two extra arrays, not target optimized form | Day 06 or Day 07 |
| Is Subsequence | Improved, but unnecessary membership-check instinct remains | 3 days |
| Best Time To Buy/Sell Stock | Improved, but needs proof and spaced recall | 3 days |

### Mastery Decision

Can move toward mastered:
- Running Sum of 1d Array, after LeetCode/timed proof and 3-day recall.
- Best Time To Buy/Sell Stock, after accepted submission and 3-day recall.

Cannot mark fully mastered yet:
- Pivot Index, because the core optimal ordering still felt unstable.
- Valid Palindrome, because hints were still needed.
- Product Except Self, because the target optimized version is not done.
- Is Subsequence, because the solution improved but the pattern trigger is not fully automatic.

### Pace And Revision

Current pace is slightly overloaded. The required work was completed, but optional Product Except Self was added before LeetCode proof. Revision is helping, but it is not sufficient until at least one accepted submission and one no-hint palindrome re-solve are recorded.

Tomorrow should continue, but with stricter limits: 3 new problems maximum, 2 revision problems, and no optional work before LeetCode acceptance.

# Current Week Execution Plan

Phase: Month 1 - Arrays + Hashing + Strings  
Current position: Day 1 complete, Day 2 attempted, Day 3 completed with revisit required, Day 4 completed locally, Day 5 completed locally  
Goal for this week: stabilize array/write-pointer/hash basics before increasing medium volume.

## Week Targets

- New problems: 18-24 maximum.
- Revision problems: 12-18.
- LeetCode submissions: 8-12.
- Must-cover progress: finish `Contains Duplicate`, `Two Sum`, `Valid Anagram`, `First Unique Character`, `Valid Palindrome`, and reattempt `Product of Array Except Self`.
- Weekly mock: 4 timed problems, not 6+.
- Success target: 70-80% completion, not perfection.

## Day 1: Completed - Array Traversal + Tracking

Today's topic: traversal, count, max/min, reverse, sorted check, second largest, move zeroes, majority.  
Why this topic now: these are the base mechanics for all later arrays.  
Prerequisites: loops, indexing, `range`, list mutation, dictionaries.  
Status: complete and passed.

Revision required:
- Second Largest Distinct Element.
- Move Zeroes.
- Majority Element dictionary and Boyer-Moore.

## Day 2: Completed/Reviewed - Duplicates + In-Place Updates

Today's topic: set lookup, write pointer, missing values, carry, rotation, prefix/suffix.  
Why this topic now: these are the first real placement patterns after basic traversal.  
Prerequisites: sets, dictionaries, modulo, right-to-left loops, list assignment.

Weak prerequisites:
- Write-pointer confidence.
- Prefix/suffix mental model.
- Carry handling from right to left.
- Complexity of extra containers.

Exact prerequisite revision before continuing:
- Revise `set.add`, `x in seen`, `dict.get`.
- Re-write the write-pointer template:

```python
write = 0
for read in range(len(nums)):
    if keep_condition(nums[read]):
        nums[write] = nums[read]
        write += 1
return write
```

Required revision:
- Remove Duplicates From Sorted Array.
- Remove Element.
- Best Time To Buy And Sell Stock.
- Plus One.
- Product Of Array Except Self.

## Day 3: Completed/Reviewed - Hash Map Frequency + Two Sum

Today's topic: hash map lookup and frequency counting.  
Why this topic now: Day 2 introduced sets; the next placement step is using dictionaries for indexes and counts.  
Required prerequisite concepts: dictionary insertion, membership check, `dict.get`, complements.

If prerequisites are weak:
- Revise `CONCEPTS.md` sections: Dictionaries, Hashing, Time Complexity, Space Complexity.
- Write a 5-line frequency counter before solving.

Completed:
1. Two Sum - brute force correct; optimized complement dictionary required solution help.
2. Valid Anagram - sorting/hash approaches attempted; hash comparison needed hint.
3. First Unique Character in a String - brute force independent; optimized second pass needed hint.
4. Remove Element revision - independent re-solve succeeded.
5. Product Of Array Except Self revision - two-array prefix/suffix version improved; target output-array + suffix version still pending.

LeetCode:
- No Day 3 submission proof yet. Day 4 must include at least one accepted submission from the Day 3 revisit set.

Decision:
- Do not add optional mediums yet.
- Continue to Day 4, but keep Day 3 hashing revision mandatory.

## Day 4: Completed/Reviewed - Strings + Palindrome + Character Counting

Today's topic: string traversal, normalization, palindrome, character frequency.  
Why this topic now: strings use the same traversal/hash patterns but require careful immutability handling.  
Required prerequisite concepts: string indexing, `.lower()`, `.isalnum()`, list building + `"".join`.

If prerequisites are weak:
- Revise `CONCEPTS.md` sections: Strings, String Building, Dictionaries.
- Practice reversing a string and counting characters locally.
- Re-write from memory: `freq[x] = freq.get(x, 0) + 1`.
- Re-write from memory: check complement first, then store current value/index.

Problems:
1. Valid Palindrome - must-cover, LeetCode, 30-40 minutes.
2. Reverse String - fundamentals, 15-20 minutes.
3. Is Subsequence - two-pointer string scan, 30-40 minutes.

Revision:
- Two Sum - 24-hour revisit, 25 minutes, must submit if clean locally.
- First Unique Character in a String or Valid Anagram - 24-hour revisit, 20-25 minutes.

Prerequisite/fundamentals revision:
- 10 minutes: dictionary frequency counter and `dict.get`.
- 10 minutes: `sorted()` complexity and string immutability.
- 10 minutes: two-pointer palindrome dry run.

Weak-pattern reinforcement:
- Complement lookup: never store `needed` as the seen value for standard Two Sum; store current number to its index after checking.
- Frequency + order: build counts first, then scan the original string/list when the answer depends on first position.
- Complexity: write time/space before checking old notes.

LeetCode workflow:
1. Solve locally first with all listed examples.
2. Submit only after local tests pass.
3. Target one accepted submission minimum; two accepted is a bonus.
4. If rejected twice, stop and write the failed case into the revisit queue.

Realistic completion target:
- 70-80% success means 3 new problems attempted, 2 revision problems attempted, and at least 1 LeetCode accepted.
- Skip Longest Common Prefix tomorrow unless all required items finish cleanly.

Expected difficulty:
- Mostly easy; focus on clean explanations and 24-hour recall, not volume.

Completed:
1. Valid Palindrome - completed locally, but optimized skip-loop version needed hint/solution exposure.
2. Reverse String - independent local solve; in-place swap pattern is strong.
3. Is Subsequence - completed locally after repeated hints; needs 24-hour re-solve.
4. Two Sum revision - independent brute force and optimized complement lookup.
5. First Unique Character revision - independent brute force and optimized frequency + second pass.
6. Valid Anagram extra revision - completed locally, but optimized complexity needs correction because of string membership inside the comparison loop.

LeetCode:
- No Day 4 submission proof yet. Day 5 must include at least one accepted submission before optional work.

Decision:
- Continue to Day 5, but reduce overload. Keep 3 new problems max, 2 revision problems max, and make LeetCode submission proof mandatory.

## Day 5: Prefix/Suffix + Running State + Day 4 String Revisit

Today's topic: running values from left/right, prefix/suffix products, one-pass min/max, and 24-hour string two-pointer recall.  
Why this topic now: Day 2 showed prefix/suffix and running-state are unstable, while Day 4 showed Valid Palindrome and Is Subsequence need immediate recall before moving on.  
Required prerequisite concepts: forward loop, reverse loop, output array, accumulated product, `min_price`, string skip loops, subsequence match pointer.

If prerequisites are weak:
- Write prefix sum for `[1,2,3,4]`.
- Write suffix product manually for `[1,2,3,4]`.
- Re-read Product Except Self notes before coding.
- Dry run Valid Palindrome on `"A man, a plan, a canal: Panama"`.
- Dry run Is Subsequence on `s = "abc", t = "ahbgdc"`.

Problems:
1. Running Sum of 1d Array - prefix basics, 15-20 minutes.
2. Find Pivot Index - prefix/suffix reasoning, 30-40 minutes.
3. Best Time To Buy And Sell Stock - one-pass running minimum, 30-40 minutes, LeetCode.

Revision:
- Valid Palindrome - 24-hour re-solve, 25-30 minutes, LeetCode if clean locally.
- Is Subsequence - 24-hour re-solve, 20-25 minutes.

Optional only if all required work is clean:
- Product of Array Except Self output-array + suffix version, 35-45 minutes.

Expected difficulty:
- 3 easy/new, 2 revision. Product Except Self is optional because Day 4 already exceeded revision volume and LeetCode proof is behind.

Completed:
1. Running Sum of 1d Array - independent new-list and in-place versions.
2. Find Pivot Index - independent brute force and optimal versions; optimal check-before-add ordering needs revisit.
3. Best Time To Buy And Sell Stock - independent brute force and one-pass versions; strong improvement from Day 2.
4. Valid Palindrome revision - solved with hints; skip-loop flow remains unstable.
5. Is Subsequence revision - independent, but avoid unnecessary membership/frequency checks.
6. Product Of Array Except Self optional - solved with left/right arrays, but not the target output-array + one suffix variable form.

LeetCode:
- No Day 5 accepted submission is recorded. Day 6 must submit before optional work.

Decision:
- Continue to Day 6 only as a controlled consolidation day. Do not increase volume. Keep 3 new problems, 2 revision problems, and a hard LeetCode-first rule.

## Day 6: Grouping + Frequency Mediums + LeetCode Proof

Today's topic: grouping with dictionary keys, frequency buckets, and cleanup of Day 5 prefix/pointer weaknesses.  
Why this topic now: after basic dictionary count, grouping is the next interview pattern, but Day 5 also left LeetCode proof and prefix/skip-loop revision behind.  
Required prerequisite concepts: tuple/list as key rules, sorting string characters, dictionary of lists, pivot check-before-update, palindrome skip loops.

If prerequisites are weak:
- Revise tuples as dictionary keys.
- Write `''.join(sorted(word))` and explain its cost.
- Dry run Pivot Index on `[2, 1, -1]` and `[0, 0, 0]`.
- Re-write the Valid Palindrome skip-loop template once from memory.

Problems:
1. Group Anagrams - must-cover, LeetCode, 40-50 minutes.
2. Top K Frequent Elements - must-cover, LeetCode, 45-55 minutes.
3. Majority Element or Sort Characters By Frequency - choose one based on energy, 25-35 minutes.

Revision:
- Find Pivot Index - 20 minutes, no notes.
- Valid Palindrome - 25 minutes, no hints if possible.

Expected difficulty:
- 2 mediums, 1 easy/medium, 2 revisions. Realistic 70-80% completion means at least 2 new problems, both revisions attempted, and 1 accepted LeetCode submission. Skip optional extras.

## Day 7: Weekly Mock + Review

Today's topic: mixed arrays/hash/strings under time.  
Why this topic now: interview readiness comes from retrieval, not just fresh solving.  
Required prerequisite concepts: all Week 1 pattern triggers.

Mock set:
1. Contains Duplicate - 10 minutes.
2. Valid Anagram - 15 minutes.
3. Two Sum - 25 minutes.
4. Product of Array Except Self - 40 minutes.

Review:
- Write why each slow/fail problem was difficult.
- Update failed queue.
- Mark only truly independent re-solves as mastered.

Decision rule:
- Continue to Week 2 if 3/4 mock problems are solved without full solution help.
- Repeat weak patterns for 2-3 days if Product Except Self, Two Sum, or Valid Anagram fail.

## LeetCode Practice Structure

For each must-cover problem:
1. Solve locally first.
2. Submit once locally tested.
3. If accepted, write pattern trigger.
4. If rejected, fix locally and submit once more.
5. If rejected twice, stop and analyze; do not spam submissions.

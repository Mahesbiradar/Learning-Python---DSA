# DSA STATUS
Last updated: 2026-06-20 (Day 23 — Restart Day 1 after 3-week gap)
Current: Month 2 | Week 1 | Day 23 (Stable Family Recall + Stress Testing)
Restart Phase: 3-day revision blitz before new topics

---

## Pattern Family Stability

| Family | Level | Primary Blocker | LC Accepted |
|--------|-------|-----------------|-------------|
| Frequency Hashing | Stable | — | 5 |
| Grouping Hash Maps | Stable | ✓ upgraded Week 3 — 7d recall passed | 2 |
| Frequency Sorting | Stable | ✓ upgraded D10 — 2 LC accepted + independent | 2 |
| Complement Lookup | Stable | ✓ Two Sum independent + LC | 2 |
| Prefix Sum | Stable | ✓ upgraded D13 — 5 LC accepted + 70%+ independent | 5 |
| Two Pointers | Stable | ✓ upgraded D10 — 3 LC accepted + independent | 3 |
| Running-State Tracking | Stable | upgraded D14 — Kadane + Max Product min/max solved independently and verified | 3 |
| Sliding Window | Stable | upgraded D22 — 11/15 independent (73%), 9 LC accepted | 9 |
| Binary Search | Building | 6 LC accepted; 6/10 independent (~60%) — needs 70%+; lower-bound template still shaky (744, 441, 374 hint-needed) | 6 |

Upgrade rule: 70%+ independent solve rate + 2 LC accepted in family → Stable
LC batch session: when a family reaches Stable, do one LC session for remaining pending in that family

---

## Problem Tracker

LC Status: ✓ = accepted | pending = not submitted yet | skipped = won't submit

| Problem | LC# | Family | LC Status | Notes |
|---------|-----|--------|-----------|-------|
| Contains Duplicate | 217 | Freq Hashing | ✓ | independent D23 recall — passed |
| Two Sum | 1 | Complement Lookup | ✓ | hint-needed D23 (initial mapping error), then corrected — passed |
| Valid Anagram | 242 | Freq Hashing | ✓ | independent D23 recall — passed |
| First Unique Character | 387 | Freq Hashing | ✓ | independent D23 recall — passed |
| Valid Palindrome | 125 | Two Pointers | ✓ | independent D22 recall; 14d recall passed |
| Reverse String | 344 | Two Pointers | ✓ | independent D22 recall; 14d recall passed |
| Is Subsequence | 392 | Two Pointers | ✓ | independent D22 recall; 14d recall passed |
| Running Sum | 1480 | Prefix Sum | ✓ | independent D23 recall — passed |
| Find Pivot Index | 724 | Prefix Sum | ✓ | independent D23 recall — passed |
| Best Time Stock | 121 | Running State | ✓ | independent D14 recall |
| Group Anagrams | 49 | Grouping Hash Maps | ✓ | independent D21 recall; 14d recall passed |
| Top K Frequent | 347 | Freq Sorting | ✓ | independent D23 recall — passed |
| Sort Chars by Freq | 451 | Freq Sorting | ✓ | independent D23 recall — passed |
| Intersection Arrays II | 350 | Freq Hashing | ✓ | independent D23 recall — passed |
| Majority Element | 169 | Freq Hashing | ✓ | independent D23 recall — passed |
| Product of Array Except Self | 238 | Prefix Sum | ✓ | independent D23 recall — passed |
| Subarray Sum Equals K | 560 | Prefix Sum | ✓ | hint-needed D22 recall; 7d final recall passed — FLAGGED shaky |
| Maximum Subarray | 53 | Running-State Tracking | ✓ | independent D22 recall; 7d final recall passed |
| Find Highest Altitude | 1732 | Prefix Sum | ✓ | independent D23 recall — passed |
| Maximum Product Subarray | 152 | Running-State Tracking | ✓ | independent D22 recall; 7d final recall passed |
| Isomorphic Strings | 205 | Grouping Hash Maps | ✓ | hint-needed D22 recall (peeked old solution); 7d final recall passed |
| Maximum Average Subarray I | 643 | Sliding Window | ✓ | hint-needed D15; 24h recall D16 — Accepted |
| Longest Substring Without Repeating | 3 | Sliding Window | ✓ | independent D22 recall; 3d recall passed |
| Minimum Size Subarray Sum | 209 | Sliding Window | ✓ | independent D22 recall; 3d recall passed |
| Longest Repeating Char Replacement | 424 | Sliding Window | ✓ | hint D16; quasi-independent D17 (peeked) — Accepted |
| Permutation in String | 567 | Sliding Window | ✓ | hint D16; independent D17 — Accepted |
| Fruits Into Baskets | 904 | Sliding Window | ✓ | independent D22 recall; 3d recall passed |
| Max Consecutive Ones III | 1004 | Sliding Window | ✓ | independent D22 recall; 3d recall passed |
| Find All Anagrams in a String | 438 | Sliding Window | ✓ | independent D22 recall; 3d recall passed |
| Contains Duplicate II | 219 | Sliding Window | ✓ | independent D23 recall — passed |
| Binary Search | 704 | Binary Search | ✓ | independent D19; 24h recall D20 — LC Accepted May 26 |
| Search Insert Position | 35 | Binary Search | ✓ | independent D19; 24h recall D20 — LC Accepted May 26 |
| First Bad Version | 278 | Binary Search | ✓ | hint-needed D19; independent D20 recall — LC Accepted May 26 |
| Sqrt(x) | 69 | Binary Search | ✓ | independent D20; 24h recall D21 — LC Accepted May 27 |
| Find Smallest Letter Greater Than Target | 744 | Binary Search | ✓ | hint-needed D20; 24h recall D21 still hint-needed — LC Accepted May 27 |
| Find Peak Element | 162 | Binary Search | ✓ | hint-needed D20; 24h recall D21 still hint-needed — LC Accepted May 27 |
| Valid Perfect Square | 367 | Binary Search | ✓ | hint-needed D22; LC Accepted May 28 |
| Arranging Coins | 441 | Binary Search | ✓ | hint-needed D22; LC Accepted May 28 |
| Guess Number Higher or Lower | 374 | Binary Search | NA | Failed D22 — not solved; retry pending |
| Unique Number of Occurrences | 1207 | Freq Hashing | ✓ | independent D23 — new problem, LC Accepted Jun 20 |
| Top K Frequent Words | 692 | Freq Sorting | ✓ | hint-needed D23 — new problem, LC Accepted Jun 20 |
| Two Sum II | 167 | Complement Lookup | ✓ | independent D23 — new problem, LC Accepted Jun 20 |
| Remove Duplicates | 26 | Two Pointers | ✓ | hint-needed D23 — new problem, LC Accepted Jun 20 |
| Remove Element | 27 | Two Pointers | ✓ | independent D23 — new problem, LC Accepted Jun 20 |
| Range Sum Query | 303 | Prefix Sum | NA | Not understood D23 — needs retry |
| Contiguous Array | 525 | Prefix Sum | NA | Not solved D23 — needs retry |
| Length of Last Word | 58 | String | NA | Not solved D23 — needs retry |

---

## Revision Queue

Agent: pull top 4-5 into daily revision slots by due date.
Rule: 24h after first solve → first revision. 3d after that → recall check. 7d → final recall.

| Problem | LC# | Due | Notes |
|---------|-----|-----|-------|
| Longest Repeating Char Replacement | 424 | Jun 1 (passed) | 7d final recall — passed D22 |
| Permutation in String | 567 | Jun 1 (passed) | 7d final recall — passed D22 |
| Sqrt(x) | 69 | May 30 (passed) | 3d recall — passed D21 |
| Find Smallest Letter Greater Than Target | 744 | May 30 (passed) | 3d recall — hint-needed D21 |
| Find Peak Element | 162 | May 30 (passed) | 3d recall — hint-needed D21 |
| Maximum Average Subarray I | 643 | May 29 (passed) | 7d final recall — passed D20 |
| Binary Search | 704 | May 29 (passed) | 3d recall — passed D20 |
| Search Insert Position | 35 | May 29 (passed) | 3d recall — passed D20 |
| First Bad Version | 278 | May 29 (passed) | 3d recall — passed D20 |
| Valid Perfect Square | 367 | May 29 (passed) | 3d recall — hint-needed D22 |
| Arranging Coins | 441 | May 29 (passed) | 3d recall — hint-needed D22 |
| Guess Number Higher or Lower | 374 | Jun 21 | Retry — Failed D22, not addressed in D23 |
| Range Sum Query | 303 | Jun 21 | Retry — Not understood D23 |
| Contiguous Array | 525 | Jun 21 | Retry — Not solved D23 |
| Length of Last Word | 58 | Jun 21 | Retry — Not solved D23 |
| Subarray Sum Equals K | 560 | Jun 21 | 3d recall — hint-needed D22, FLAGGED shaky |
| Isomorphic Strings | 205 | Jun 21 | 3d recall — hint-needed D22 (peeked old solution) |
| Sliding Window warm-up | — | Jun 21 | warm-up had stale variable bug D22 (non-graded) |
| Unique Number of Occurrences | 1207 | Jun 21 | 24h revision — new problem D23 |
| Top K Frequent Words | 692 | Jun 21 | 24h revision — hint-needed D23 |
| Two Sum II | 167 | Jun 21 | 24h revision — independent D23 |
| Remove Duplicates | 26 | Jun 21 | 24h revision — hint-needed D23 |
| Remove Element | 27 | Jun 21 | 24h revision — independent D23 |

---

## LC Submission Log

| Date | Problem | LC# | Result |
|------|---------|-----|--------|
| May 13 | Valid Anagram | 242 | Accepted |
| May 13 | Sort Chars by Freq | 451 | Accepted |
| May 13 | Intersection Arrays II | 350 | Accepted |
| May 13 | Group Anagrams | 49 | Accepted |
| May 13 | Find Pivot Index | 724 | Accepted |
| May 14 | Valid Anagram | 242 | Accepted |
| May 14 | Find Pivot Index | 724 | Accepted |
| May 15 | Valid Anagram | 242 | Accepted |
| May 15 | Two Sum | 1 | Accepted |
| May 15 | First Unique Character | 387 | Accepted |
| May 15 | Best Time to Buy and Sell Stock | 121 | Accepted |
| May 16 | Valid Palindrome | 125 | Accepted |
| May 16 | Reverse String | 344 | Accepted |
| May 16 | Is Subsequence | 392 | Accepted |
| May 16 | Top K Frequent | 347 | Accepted |
| May 16 | Majority Element | 169 | Accepted |
| May 17 | Product of Array Except Self | 238 | Accepted |
| May 18 | Find Highest Altitude | 1732 | Accepted |
| May 18 | Isomorphic Strings | 205 | Accepted |
| May 19 | Running Sum | 1480 | Accepted |
| May 19 | Subarray Sum Equals K | 560 | Accepted |
| May 19 | Maximum Subarray | 53 | Accepted |
| May 19 | Maximum Product Subarray | 152 | Accepted |
| May 22 | Maximum Average Subarray I | 643 | Accepted |
| May 22 | Longest Substring Without Repeating | 3 | Accepted |
| May 22 | Minimum Size Subarray Sum | 209 | Accepted |
| May 23 | Longest Repeating Char Replacement | 424 | Accepted |
| May 23 | Permutation in String | 567 | Accepted |
| May 23 | Fruits Into Baskets | 904 | Accepted |
| May 24 | Max Consecutive Ones III | 1004 | Accepted |
| May 24 | Find All Anagrams in a String | 438 | Accepted |
| May 24 | Contains Duplicate II | 219 | Accepted |
| May 26 | Binary Search | 704 | Accepted |
| May 26 | Search Insert Position | 35 | Accepted |
| May 26 | First Bad Version | 278 | Accepted |
| May 27 | Sqrt(x) | 69 | Accepted |
| May 27 | Find Smallest Letter Greater Than Target | 744 | Accepted |
| May 27 | Find Peak Element | 162 | Accepted |
| May 28 | Valid Perfect Square | 367 | Accepted |
| May 28 | Arranging Coins | 441 | Accepted |
| Jun 20 | Unique Number of Occurrences | 1207 | Accepted |
| Jun 20 | Top K Frequent Words | 692 | Accepted |
| Jun 20 | Two Sum II | 167 | Accepted |
| Jun 20 | Remove Duplicates | 26 | Accepted |
| Jun 20 | Remove Element | 27 | Accepted |

Unique problems LC accepted: 41
Weekly LC slot: 45 min, clear pending problems you feel confident on

---

## Restart Phase Tracker (3-day blitz)

### Day 23 — Jun 20 (Yesterday) — Stable Family Recall

Focus: All Stable families (Freq Hashing, Freq Sorting, Complement Lookup, Prefix Sum, Two Pointers, Running-State, Sliding Window)

Results:
- Total problems attempted: 20
- Solved independently: 14/20 (70%)
- Solved with hints: 3/20 (Two Sum initial mapping error, Top K Frequent Words sorting tuple, Remove Duplicates write pointer logic)
- Not solved: 3/20 (Range Sum Query 303 — not understood, Contiguous Array 525 — not solved, Length of Last Word 58 — not solved)
- LC submitted: 5 new problems (1207, 692, 167, 26, 27) — all Accepted
- Family stability after recall: All Stable families confirmed intact after 3-week gap

Verdict: **Good Restart** (17/20 = 85% solved, 70% independent)

### Day 24 — Jun 21 (Today) — Recovery + Retry

Focus: Retry failed/unsolved problems from D23 + Binary Search depth
- Guess Number Higher or Lower (374) — retry
- Range Sum Query (303) — retry after understanding
- Contiguous Array (525) — retry
- Length of Last Word (58) — retry
- Subarray Sum Equals K (560) — 3d recall, shaky
- Isomorphic Strings (205) — 3d recall
- Binary Search new problems: 3 easy variants to push family to Stable

### Day 25 — Jun 22 (Tomorrow) — Final Confirmation

Focus: 24h recall of D24 problems + any remaining gaps
- If 70%+ independent on D24 → confirm restart complete, introduce Linked List
- If <70% independent → one more consolidation day before new topics

---

## Week 4 Review (Historical — May 26-28)

### Week Summary

- Total new problems solved: 6
- Total revisions done: 31 (D20: 5, D21: 5, D22: 21)
- LC accepted this week (unique): 8 (D20: 3, D21: 3, D22: 2)
- Average independent solve rate: 73% (D22 boost: 16/18 independent on backlog blitz)
- Families that reached Stable: Sliding Window — upgraded to Stable (11/15 independent = 73%, 9 LC accepted)
- Families still Shaky: Binary Search (Building, 60% independent)
- Biggest pattern gap: Binary Search lower-bound template (`left < right`) still shaky — 4/10 problems hint-needed (744, 162, 441, 374); Subarray Sum Equals K and Isomorphic Strings needed hints on recall
- Overall verdict: On Track — major backlog clearance achieved

---

## Weekly Scores

| Week | New Problems | Revisions | LC Accepted | Independent% |
|------|-------------|-----------|-------------|--------------|
| 1 | 29 | 14 | 0 | 67% |
| 2 | 17 | 28 | 15 | 73% |
| 3 | 12 | 43 | 13 | 67% |
| 4 | 6 | 31 | 8 | 73% |
| 5 (Restart) | 5 | 15 | 5 | 70% |

---

## Mastered (light recall only)

Contains Duplicate, Reverse String (in-place), Move Zeroes,
Majority Element (dict version), Intersection of Two Arrays (unique),
Print/Sum/Count/Max/Min basics, Check Sorted Array,
First Unique Character (387), Best Time to Buy and Sell Stock (121), Running Sum of 1d Array (1480),
Group Anagrams (49), Find Pivot Index (724), Sort Chars by Freq (451),
Intersection Arrays II (350), Product of Array Except Self (238),
Valid Palindrome (125), Is Subsequence (392), Top K Frequent (347),
Longest Substring Without Repeating (3), Minimum Size Subarray Sum (209),
Fruits Into Baskets (904), Max Consecutive Ones III (1004),
Find All Anagrams in a String (438), Contains Duplicate II (219),
Maximum Subarray (53), Maximum Product Subarray (152),
Valid Anagram (242), Contains Duplicate (217), First Unique Character (387),
Unique Number of Occurrences (1207), Two Sum II (167), Remove Element (27)

Day 13 tracker note (2026-05-19): verified with `C:\Users\dell\AppData\Local\Python\bin\python.exe` outside sandbox after default Python commands failed; all visible test outputs matched expected values.
Day 14 tracker note (2026-05-20): default `python` / path `python` / `python3` commands failed; verified with `C:\Users\dell\AppData\Local\Python\pythoncore-3.14-64\python.exe`; all visible test outputs matched expected values.
Day 15 tracker note (2026-05-21): verified in Claude sandbox (python3); all 9 test case outputs matched expected values.
Day 16 tracker note (2026-05-22): verified in Claude sandbox (python3); all graded test case outputs matched expected values; warm-up variable window had a stale variable bug (non-graded).
Day 17 tracker note (2026-05-23): verified in Claude sandbox (python3); all graded test case outputs matched expected values; debug prints in checkInclusion (567) are non-graded noise — final True/False correct.
Day 18 tracker note (2026-05-24): verified in sandbox (python); all 8 graded test case outputs matched expected values; 1004/438/219 promoted to LC Accepted.
Day 19 tracker note (2026-05-25): verified in sandbox (python3); all 24 test case outputs matched expected values; 704/35 ready to submit; 278 hint-needed (lower-bound template not internalized); 387/121/1480 final recall passed → Mastered.
Day 20 tracker note (2026-05-26): verified in sandbox (python3); all 14 graded test case outputs matched expected values; 704/35/278 promoted to LC Accepted; 69/744/162 hint-needed (lower-bound template not internalized on new variants); 8 overdue items remain unaddressed.
Day 21 tracker note (2026-05-27): verified in sandbox (python3); all 19 graded test case outputs matched expected values; 69/744/162 promoted to LC Accepted; 367 independent (ready to submit); 441/374 hint-needed; 9 overdue items remain unaddressed; Group Anagrams + Find Highest Altitude 7d/14d recall passed independently.
Day 22 tracker note (2026-05-28): verified in sandbox (python3); 18/20 graded test case outputs matched expected values; Valid Perfect Square + Arranging Coins promoted to LC Accepted; Guess Number Higher or Lower Failed (not solved); Subarray Sum Equals K hint-needed (peeked old solution); Isomorphic Strings hint-needed (peeked old solution); Sliding Window backlog CLEARED — 11/15 independent (73%) → upgraded to Stable; Binary Search backlog: 6/10 independent (60%) still Building; ALL May 24-28 overdue items addressed.
Day 23 tracker note (2026-06-20): verified in sandbox (python3); 17/20 problems solved (14 independent, 3 hint-needed); 5 new problems LC Accepted (1207, 692, 167, 26, 27); 3 not solved (303, 525, 58); All Stable families confirmed intact after 3-week gap; Two Sum had initial mapping error (seen[needed]=i instead of seen[nums[i]]=i) — corrected; Restart verdict: Good (85% solved, 70% independent).

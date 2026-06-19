# DSA STATUS
Last updated: 2026-05-28 (Day 22 complete)
Current: Month 1 | Week 4 | Day 22 (Consolidation — backlog blitz)
Week 4 in progress

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
| Sliding Window | Building | 9 LC accepted; 11/15 independent (~73%) — **upgraded to Stable if 70%+ maintained**; needs confirmation on next recall | 9 |
| Binary Search | Building | 6 LC accepted; 6/10 independent (~60%) — needs 70%+; lower-bound template still shaky (744, 441, 374 hint-needed) | 6 |

Upgrade rule: 70%+ independent solve rate + 2 LC accepted in family → Stable
LC batch session: when a family reaches Stable, do one LC session for remaining pending in that family

---

## Problem Tracker

LC Status: ✓ = accepted | pending = not submitted yet | skipped = won't submit

| Problem | LC# | Family | LC Status | Notes |
|---------|-----|--------|-----------|-------|
| Contains Duplicate | 217 | Freq Hashing | ✓ | |
| Two Sum | 1 | Complement Lookup | ✓ | |
| Valid Anagram | 242 | Freq Hashing | ✓ | |
| First Unique Character | 387 | Freq Hashing | ✓ | |
| Valid Palindrome | 125 | Two Pointers | ✓ | independent D22 recall; 14d recall passed |
| Reverse String | 344 | Two Pointers | ✓ | independent D22 recall; 14d recall passed |
| Is Subsequence | 392 | Two Pointers | ✓ | independent D22 recall; 14d recall passed |
| Running Sum | 1480 | Prefix Sum | ✓ | independent D13 |
| Find Pivot Index | 724 | Prefix Sum | ✓ | independent D22 recall; 14d recall passed |
| Best Time Stock | 121 | Running State | ✓ | independent D14 recall |
| Group Anagrams | 49 | Grouping Hash Maps | ✓ | independent D21 recall; 14d recall passed |
| Top K Frequent | 347 | Freq Sorting | ✓ | independent D22 recall; 14d recall passed |
| Sort Chars by Freq | 451 | Freq Sorting | ✓ | independent D22 recall; 14d recall passed |
| Intersection Arrays II | 350 | Freq Hashing | ✓ | independent D22 recall; 14d recall passed |
| Majority Element | 169 | Freq Hashing | ✓ | independent D22 recall; 14d recall passed |
| Product of Array Except Self | 238 | Prefix Sum | ✓ | |
| Subarray Sum Equals K | 560 | Prefix Sum | ✓ | hint-needed D22 recall; 7d final recall passed — FLAGGED shaky |
| Maximum Subarray | 53 | Running-State Tracking | ✓ | independent D22 recall; 7d final recall passed |
| Find Highest Altitude | 1732 | Prefix Sum | ✓ | independent D21 recall; 7d final recall passed |
| Maximum Product Subarray | 152 | Running-State Tracking | ✓ | independent D14 min/max recall |
| Isomorphic Strings | 205 | Grouping Hash Maps | ✓ | hint-needed D22 recall (peeked old solution); 7d final recall passed |
| Maximum Average Subarray I | 643 | Sliding Window | ✓ | hint-needed D15; 24h recall D16 — Accepted |
| Longest Substring Without Repeating | 3 | Sliding Window | ✓ | independent D22 recall; 3d recall passed |
| Minimum Size Subarray Sum | 209 | Sliding Window | ✓ | independent D22 recall; 3d recall passed |
| Longest Repeating Char Replacement | 424 | Sliding Window | ✓ | hint D16; quasi-independent D17 (peeked) — Accepted |
| Permutation in String | 567 | Sliding Window | ✓ | hint D16; independent D17 — Accepted |
| Fruits Into Baskets | 904 | Sliding Window | ✓ | independent D22 recall; 3d recall passed |
| Max Consecutive Ones III | 1004 | Sliding Window | ✓ | independent D22 recall; 3d recall passed |
| Find All Anagrams in a String | 438 | Sliding Window | ✓ | independent D22 recall; 3d recall passed |
| Contains Duplicate II | 219 | Sliding Window | ✓ | independent D17; LC Accepted May 24 |
| Binary Search | 704 | Binary Search | ✓ | independent D19; 24h recall D20 — LC Accepted May 26 |
| Search Insert Position | 35 | Binary Search | ✓ | independent D19; 24h recall D20 — LC Accepted May 26 |
| First Bad Version | 278 | Binary Search | ✓ | hint-needed D19; independent D20 recall — LC Accepted May 26 |
| Sqrt(x) | 69 | Binary Search | ✓ | independent D20; 24h recall D21 — LC Accepted May 27 |
| Find Smallest Letter Greater Than Target | 744 | Binary Search | ✓ | hint-needed D20; 24h recall D21 still hint-needed — LC Accepted May 27 |
| Find Peak Element | 162 | Binary Search | ✓ | hint-needed D20; 24h recall D21 still hint-needed — LC Accepted May 27 |
| Valid Perfect Square | 367 | Binary Search | ✓ | hint-needed D22; LC Accepted May 28 |
| Arranging Coins | 441 | Binary Search | ✓ | hint-needed D22; LC Accepted May 28 |
| Guess Number Higher or Lower | 374 | Binary Search | NA | Failed — not solved D22 |
| Maximum Product Subarray | 152 | Running-State Tracking | ✓ | independent D22 recall; 7d final recall passed |

---

## Revision Queue

Agent: pull top 4-5 into daily revision slots by due date.
Rule: 24h after first solve → first revision. 3d after that → recall check. 7d → final recall.

| Problem | LC# | Due | Notes |
|---------|-----|-----|-------|
| Longest Repeating Char Replacement | 424 | Jun 1 | 7d final recall |
| Permutation in String | 567 | Jun 1 | 7d final recall |
| Sqrt(x) | 69 | May 30 | 3d recall — 24h revision passed D21 |
| Find Smallest Letter Greater Than Target | 744 | May 30 | 3d recall — 24h recall still hint-needed D21 |
| Find Peak Element | 162 | May 30 | 3d recall — 24h recall still hint-needed D21 |
| Maximum Average Subarray I | 643 | May 29 | 7d final recall — 3d recall passed D20 |
| Binary Search | 704 | May 29 | 3d recall — 24h revision passed D20 |
| Search Insert Position | 35 | May 29 | 3d recall — 24h revision passed D20 |
| First Bad Version | 278 | May 29 | 3d recall — 24h revision passed D20 |
| Valid Perfect Square | 367 | May 29 | 3d recall — hint-needed D22; LC Accepted May 28 |
| Arranging Coins | 441 | May 29 | 3d recall — hint-needed D22; LC Accepted May 28 |
| Guess Number Higher or Lower | 374 | May 29 | 24h revision — Failed D22, retry |
| Sliding Window warm-up | — | May 29 | warm-up had stale variable bug D22 (non-graded) |
| Subarray Sum Equals K | 560 | May 29 | 3d recall — hint-needed D22, FLAGGED shaky |
| Isomorphic Strings | 205 | May 29 | 3d recall — hint-needed D22 (peeked old solution) |

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

Unique problems LC accepted: 36
Weekly LC slot: 45 min, clear pending problems you feel confident on

---

## Week 2 Review

### Week Summary

- Total new problems solved: 17
- Total revisions done: 28
- LC accepted this week (unique): 15
- Average independent solve rate: 73%
- Families that reached Stable: Frequency Hashing, Frequency Sorting, Complement Lookup, Two Pointers
- Families still Shaky: Prefix Sum, Running-State Tracking
- Biggest pattern gap: running-state transitions/Kadane intuition, especially Max Product min/max tracking
- Overall verdict: On Track

### LC Pending Review

| Problem | LC# | Family | Readiness |
|---------|-----|--------|-----------|
| Running Sum | 1480 | Prefix Sum | Ready to submit: solved independently / marked ready |
| Subarray Sum Equals K | 560 | Prefix Sum | Needs more work: hint-dependent on May 17 |
| Maximum Subarray | 53 | Running-State Tracking | Needs more work: hint-dependent and Kadane concept unclear |
| Maximum Product Subarray | 152 | Running-State Tracking | Needs more work: brute force only; optimization pending |

### Next Week Plan

Week 3: May 19-25

| Day | Date | Type | Focus |
|-----|------|------|-------|
| Day 13 | May 19 | Reinforcement | Prefix Sum deep dive - Subarray Sum no-hints attempt, Running Sum LC candidate |
| Day 14 | May 20 | Reinforcement | Running-State Tracking - Kadane's internalization, Max Product optimization |
| Day 15 | May 21 | Conditional New Pattern | Sliding Window intro only if Prefix Sum + Running-State have 2+ problems at recall stage |
| Day 16 | May 22 | Reinforcement | Sliding Window + 7d final recall (Two Sum, Valid Anagram) |
| Day 17 | May 23 | Conditional New Pattern | Binary Search intro only if Sliding Window is not crowding carry-over work |
| Day 18 | May 24 | Reinforcement | Binary Search + 7d recall (Group Anagrams, Find Pivot) |
| Day 19 | May 25 | Retrieval | 3d/7d recall blitz — all May 25 due items |

New patterns to introduce: Sliding Window only if current shaky families have 2+ problems at recall stage; Binary Search only if Sliding Window does not overload the week.

Carry-over problems from Week 2: Subarray Sum Equals K, Maximum Subarray, Maximum Product Subarray, Sort Chars by Freq recall, Intersection Arrays II recall.

---

## Week 3 Review

### Week Summary

- Total new problems solved: 12
- Total revisions done: 43
- LC accepted this week (unique): 13
- Average independent solve rate: 67%
- Families that reached Stable: Grouping Hash Maps (upgraded — 7d recall blitz passed independently)
- Families still Shaky: Sliding Window (Building, 6+ days, 67% independent), Binary Search (Building, newly introduced)
- Biggest pattern gap: Sliding Window variable-size invariant (max_freq tracking in 424); Binary Search lower-bound template (left < right) not internalized
- Overall verdict: On Track

### LC Pending Review

| Problem | LC# | Family | Readiness |
|---------|-----|--------|-----------|
| Binary Search | 704 | Binary Search | Ready to submit: solved independently D19 |
| Search Insert Position | 35 | Binary Search | Ready to submit: solved independently D19 |
| First Bad Version | 278 | Binary Search | Needs more work: hint-needed on lower-bound template (left < right) |

### Next Week Plan

Week 4: May 26 - June 1

| Day | Date | Type | Focus |
|-----|------|------|-------|
| Day 20 | May 26 | Reinforcement | Binary Search 24h recall (704, 35, 278) + overdue 7d/3d recall blitz |
| Day 21 | May 27 | Reinforcement | Binary Search depth (69, 744, 162 24h recall + 367, 441, 374 new) + overdue blitz (49, 1732) |
| Day 22 | May 28 | Consolidation | Full backlog blitz — 21 revision slots, zero new problems |
| Day 23 | May 29 | Recovery | Week 4 review + Week 5 plan |
| Day 24 | May 30 | Conditional New Pattern | Linked List intro only if Binary Search reaches Stable |
| Day 25 | May 31 | Reinforcement | Linked List or Binary Search depth + recall |
| Day 26 | June 1 | Reinforcement | Recall blitz + family consolidation |

New patterns to introduce: Linked List only if Binary Search reaches Stable and Sliding Window backlog is cleared.

Carry-over problems from Week 3: First Bad Version (278), 5 overdue revision items (238, 49, 724, 451, 350), 5 due-today items (1732, 205, 643, 3, 209).

---

## Week 4 Review

### Week Summary

- Total new problems solved: 6
- Total revisions done: 31 (D20: 5, D21: 5, D22: 21)
- LC accepted this week (unique): 8 (D20: 3, D21: 3, D22: 2)
- Average independent solve rate: 73% (D22 boost: 16/18 independent on backlog blitz)
- Families that reached Stable: Sliding Window — upgraded to Stable (11/15 independent = 73%, 9 LC accepted)
- Families still Shaky: Binary Search (Building, 60% independent)
- Biggest pattern gap: Binary Search lower-bound template (`left < right`) still shaky — 4/10 problems hint-needed (744, 162, 441, 374); Subarray Sum Equals K and Isomorphic Strings needed hints on recall
- Overall verdict: On Track — major backlog clearance achieved

### LC Pending Review

| Problem | LC# | Family | Readiness |
|---------|-----|--------|-----------|
| Valid Perfect Square | 367 | Binary Search | Accepted May 28 |
| Arranging Coins | 441 | Binary Search | Accepted May 28 |
| Guess Number Higher or Lower | 374 | Binary Search | Failed D22 — needs retry |

### Next Week Plan

Week 5: June 2 - June 8

| Day | Date | Type | Focus |
|-----|------|------|-------|
| Day 27 | Jun 2 | Reinforcement | Binary Search 24h recall (367, 441, 374 retry) + overdue clear |
| Day 28 | Jun 3 | Reinforcement | Sliding Window Stable confirmation + Binary Search depth |
| Day 29 | Jun 4 | Reinforcement | Binary Search depth + recall blitz |
| Day 30 | Jun 5 | Recovery | Week 5 review + Week 6 plan |
| Day 31 | Jun 6 | Conditional New Pattern | Linked List intro only if Binary Search reaches Stable |
| Day 32 | Jun 7 | Reinforcement | Linked List or Binary Search depth + recall |
| Day 33 | Jun 8 | Reinforcement | Recall blitz + family consolidation |

New patterns to introduce: Linked List only if Binary Search reaches Stable (70%+ independent, 2+ LC accepted) and all backlog cleared.

Carry-over problems from Week 4: Guess Number Higher or Lower (374, Failed), Subarray Sum Equals K (560, hint-needed D22), Isomorphic Strings (205, hint-needed D22).

---

## Weekly Scores

| Week | New Problems | Revisions | LC Accepted | Independent% |
|------|-------------|-----------|-------------|--------------|
| 1 | 29 | 14 | 0 | 67% |
| 2 | 17 | 28 | 15 | 73% |
| 3 | 12 | 43 | 13 | 67% |
| 4 | 6 | 31 | 8 | 73% |

---

## Week 2 Schedule

| Day | Date | Type | Focus |
|-----|------|------|-------|
| Day 9 | May 15 | Reinforcement | Freq Sorting + Complement |
| Day 10 | May 16 | Reinforcement | Prefix Sum + Running State |
| Day 11 | May 17 | Retrieval | 3d recall blitz — all May 17 items |
| Day 12 | May 18 | Recovery | Week review + Week 3 plan |

---

## Week 3 Schedule (May 19–25)

| Day | Date | Type | Focus |
|-----|------|------|-------|
| Day 13 | May 19 | Reinforcement | Prefix Sum deep dive — Subarray Sum no-hints attempt, Running Sum LC |
| Day 14 | May 20 | Reinforcement | Running-State Tracking — Kadane's internalization, Max Product optimization |
| Day 15 | May 21 | New Pattern | Sliding Window intro — 3 problems (all hint-dependent); 5 revision problems all independent |
| Day 16 | May 22 | Reinforcement | Sliding Window depth (424, 567, 904) + 7d final recall (Two Sum, Valid Anagram); 643/3/209 LC Accepted |
| Day 17 | May 23 | Reinforcement | Sliding Window 24h recall — 424/567/904 independent + Accepted; 3 new (1004 ind, 438 hint, 219 ind); Binary Search deferred |
| Day 18 | May 24 | Reinforcement | 7d recall blitz (Group Anagrams, Find Pivot, Sort Chars, Intersection II, Product of Array) + Sliding Window 24h (1004, 438, 219) |
| Day 19 | May 25 | New Pattern + Retrieval | Binary Search intro (704, 35, 278) + 3d/7d recall blitz — 387/121/1480/424/567 |

Carry-over from Week 2: Subarray Sum Equals K, Maximum Subarray, Max Product Subarray (all accepted D13 but hint-dependent), Sort Chars by Freq + Intersection II (recall due)

---

## Week 4 Schedule (May 26 - June 1)

| Day | Date | Type | Focus |
|-----|------|------|-------|
| Day 20 | May 26 | Reinforcement | Binary Search 24h recall (704, 35, 278) + overdue 7d/3d recall blitz |
| Day 21 | May 27 | Reinforcement | Binary Search depth (69, 744, 162 24h recall + 367, 441, 374 new) + overdue blitz (49, 1732) |
| Day 22 | May 28 | Consolidation | Full backlog blitz — 21 revision slots, zero new problems |
| Day 23 | May 29 | Recovery | Week 4 review + Week 5 plan |
| Day 24 | May 30 | Conditional New Pattern | Linked List intro only if Binary Search reaches Stable |
| Day 25 | May 31 | Reinforcement | Linked List or Binary Search depth + recall |
| Day 26 | June 1 | Reinforcement | Recall blitz + family consolidation |

Carry-over from Week 3: First Bad Version (278), 5 overdue revision items (238, 49, 724, 451, 350), 5 due-today items (1732, 205, 643, 3, 209).

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
Maximum Subarray (53), Maximum Product Subarray (152)

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

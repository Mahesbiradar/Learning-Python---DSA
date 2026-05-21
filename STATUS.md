# DSA STATUS
Last updated: 2026-05-21 (Day 15)
Current: Month 1 | Week 3 | Day 15 (Sliding Window intro + Revision)
Week 2 complete

---

## Pattern Family Stability

| Family | Level | Primary Blocker | LC Accepted |
|--------|-------|-----------------|-------------|
| Frequency Hashing | Stable | — | 5 |
| Grouping Hash Maps | Building | Group Anagrams hint-needed in recall | 2 |
| Frequency Sorting | Stable | ✓ upgraded D10 — 2 LC accepted + independent | 2 |
| Complement Lookup | Stable | ✓ Two Sum independent + LC | 2 |
| Prefix Sum | Stable | ✓ upgraded D13 — 5 LC accepted + 70%+ independent; keep Subarray Sum on recall | 5 |
| Two Pointers | Stable | ✓ upgraded D10 — 3 LC accepted + independent | 3 |
| Running-State Tracking | Stable | upgraded D14 - Kadane + Max Product min/max solved independently and verified | 3 |
| Sliding Window | Building | All 3 intro problems hint-dependent D15 — needs independent recall before upgrade | 0 |

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
| Valid Palindrome | 125 | Two Pointers | ✓ | independent D14 recall; alphanumeric syntax fixed |
| Reverse String | 344 | Two Pointers | ✓ | independent D14 recall |
| Is Subsequence | 392 | Two Pointers | ✓ | independent D14 recall |
| Running Sum | 1480 | Prefix Sum | ✓ | independent D13 |
| Find Pivot Index | 724 | Prefix Sum | ✓ | |
| Best Time Stock | 121 | Running State | ✓ | independent D14 recall |
| Group Anagrams | 49 | Grouping Hash Maps | ✓ | |
| Top K Frequent | 347 | Freq Sorting | ✓ | independent D14 recall |
| Sort Chars by Freq | 451 | Freq Sorting | ✓ | |
| Intersection Arrays II | 350 | Freq Hashing | ✓ | |
| Majority Element | 169 | Freq Hashing | ✓ | independent D14 recall; optimal Accepted |
| Product of Array Except Self | 238 | Prefix Sum | ✓ | |
| Subarray Sum Equals K | 560 | Prefix Sum | ✓ | independent D14 recall |
| Maximum Subarray | 53 | Running-State Tracking | ✓ | independent D14 Kadane recall |
| Find Highest Altitude | 1732 | Prefix Sum | ✓ | |
| Maximum Product Subarray | 152 | Running-State Tracking | ✓ | independent D14 min/max recall |
| Isomorphic Strings | 205 | Grouping Hash Maps | ✓ | independent solve D12 |
| Maximum Average Subarray I | 643 | Sliding Window | pending | hint-needed D15 — submit after independent recall |
| Longest Substring Without Repeating | 3 | Sliding Window | pending | hint-needed D15 — submit after independent recall |
| Minimum Size Subarray Sum | 209 | Sliding Window | pending | hint-needed D15 — submit after independent recall |

---

## Revision Queue

Agent: pull top 4-5 into daily revision slots by due date.
Rule: 24h after first solve → first revision. 3d after that → recall check. 7d → final recall.

| Problem | LC# | Due | Notes |
|---------|-----|-----|-------|
| Maximum Average Subarray I | 643 | May 22 | 24h revision — hint-needed D15 |
| Longest Substring Without Repeating | 3 | May 22 | 24h revision — hint-needed D15 |
| Minimum Size Subarray Sum | 209 | May 22 | 24h revision — hint-needed D15 |
| Two Sum | 1 | May 22 | 7d final recall |
| Valid Anagram | 242 | May 22 | 7d final recall |
| Group Anagrams | 49 | May 24 | 7d final recall |
| Find Pivot Index | 724 | May 24 | 7d final recall |
| Sort Chars by Freq | 451 | May 24 | 7d final recall |
| Intersection II | 350 | May 24 | 7d final recall |
| First Unique Character | 387 | May 25 | 7d final recall |
| Best Time Stock | 121 | May 25 | 7d final recall |
| Running Sum | 1480 | May 25 | 7d final recall |
| Find Highest Altitude | 1732 | May 25 | 7d final recall |
| Isomorphic Strings | 205 | May 25 | 7d final recall |
| Product of Array Except Self | 238 | May 24 | 7d final recall |
| Maximum Average Subarray I | 643 | May 25 | 3d recall |
| Longest Substring Without Repeating | 3 | May 25 | 3d recall |
| Minimum Size Subarray Sum | 209 | May 25 | 3d recall |
| Subarray Sum Equals K | 560 | May 27 | 7d final recall |
| Valid Palindrome | 125 | May 27 | 7d final recall |
| Reverse String | 344 | May 27 | 7d final recall |
| Is Subsequence | 392 | May 27 | 7d final recall |
| Top K Frequent | 347 | May 27 | 7d final recall |
| Majority Element | 169 | May 27 | 7d final recall |
| Maximum Subarray | 53 | May 27 | 7d final recall |
| Maximum Product Subarray | 152 | May 28 | 7d final recall |

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

Unique problems LC accepted: 19
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
| Day 15 | May 21 | Conditional New Pattern | Sliding Window intro only if Prefix Sum + Running-State have 2+ recall-stage problems under control |
| Day 16 | May 22 | Reinforcement | Sliding Window + 7d recall blitz (Two Sum, Valid Anagram) |
| Day 17 | May 23 | Conditional New Pattern | Binary Search intro only if Sliding Window is not crowding carry-over work |
| Day 18 | May 24 | Reinforcement | Binary Search + 7d recall (Group Anagrams, Find Pivot) |
| Day 19 | May 25 | Retrieval | 3d/7d recall blitz — all May 25 due items |

New patterns to introduce: Sliding Window only if current shaky families have 2+ problems at recall stage; Binary Search only if Sliding Window does not overload the week.

Carry-over problems from Week 2: Subarray Sum Equals K, Maximum Subarray, Maximum Product Subarray, Sort Chars by Freq recall, Intersection Arrays II recall.

---

## Weekly Scores

| Week | New Problems | Revisions | LC Accepted | Independent% |
|------|-------------|-----------|-------------|--------------|
| 1 | 29 | 14 | 0 | 67% |
| 2 | 17 | 28 | 15 | 73% |
| 3 | 3 | 20 | 4 | 75% |

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
| Day 16 | May 22 | Reinforcement | Sliding Window 24h recall + 7d final recall (Two Sum, Valid Anagram) |
| Day 17 | May 23 | Conditional New Pattern | Binary Search intro only if Sliding Window is not crowding carry-over work |
| Day 18 | May 24 | Reinforcement | Binary Search + 7d recall (Group Anagrams, Find Pivot, Product of Array, Intersection II) |
| Day 19 | May 25 | Retrieval | 3d/7d recall blitz — all May 25 due items (heavy day: 8 problems) |

Carry-over from Week 2: Subarray Sum, Maximum Subarray, Max Product Subarray (all accepted D13 but hint-dependent), Sort Chars by Freq + Intersection II (recall due)

Day 13 tracker note (2026-05-19): verified with `C:\Users\dell\AppData\Local\Python\bin\python.exe` outside sandbox after default Python commands failed; all visible test outputs matched expected values.
Day 14 tracker note (2026-05-20): default `python` / path `python` / `python3` commands failed; verified with `C:\Users\dell\AppData\Local\Python\pythoncore-3.14-64\python.exe`; all visible test outputs matched expected values.
Day 15 tracker note (2026-05-21): verified in Claude sandbox (python3); all 9 test case outputs matched expected values.

---

## Mastered (light recall only)

Contains Duplicate, Reverse String (in-place), Move Zeroes,
Majority Element (dict version), Intersection of Two Arrays (unique),
Print/Sum/Count/Max/Min basics, Check Sorted Array
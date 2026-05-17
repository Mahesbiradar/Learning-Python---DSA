# DSA STATUS
Last updated: 2026-05-17 (Day 11)
Current: Month 1 | Week 2 | Day 11
Week 2 days remaining: 0 (Recovery Day 12 tomorrow)

---

## Pattern Family Stability

| Family | Level | Primary Blocker | LC Accepted |
|--------|-------|-----------------|-------------|
| Frequency Hashing | Stable | — | 5 |
| Grouping Hash Maps | Building | Group Anagrams hint-needed in recall | 1 |
| Frequency Sorting | Stable | ✓ upgraded D10 — 2 LC accepted + independent | 2 |
| Complement Lookup | Stable | ✓ Two Sum independent + LC | 2 |
| Prefix Sum | Building | Subarray Sum hint-dependent | 2 |
| Two Pointers | Stable | ✓ upgraded D10 — 3 LC accepted + independent | 3 |
| Running-State Tracking | Building | Kadane's concept still unclear after D11 | 1 |

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
| Valid Palindrome | 125 | Two Pointers | ✓ | hint: alphanumeric check syntax |
| Reverse String | 344 | Two Pointers | ✓ | |
| Is Subsequence | 392 | Two Pointers | ✓ | independent D10 (was hint-dependent) |
| Running Sum | 1480 | Prefix Sum | pending | ready to submit |
| Find Pivot Index | 724 | Prefix Sum | ✓ | |
| Best Time Stock | 121 | Running State | ✓ | |
| Group Anagrams | 49 | Grouping Hash Maps | ✓ | |
| Top K Frequent | 347 | Freq Sorting | ✓ | |
| Sort Chars by Freq | 451 | Freq Sorting | ✓ | |
| Intersection Arrays II | 350 | Freq Hashing | ✓ | |
| Majority Element | 169 | Freq Hashing | ✓ | brute: TLE; optimal: Accepted |
| Product of Array Except Self | 238 | Prefix Sum | ✓ | |
| Subarray Sum Equals K | 560 | Prefix Sum | pending | hint needed 2026-05-17 |
| Maximum Subarray | 53 | Running-State Tracking | pending | hint needed 2026-05-17 |
| Find Highest Altitude | 1732 | Prefix Sum | pending | ready to submit |
| Maximum Product Subarray | 152 | Running-State Tracking | pending | brute only, optimization pending |
| Isomorphic Strings | 205 | Grouping Hash Maps | pending | hint needed 2026-05-17 |

---

## Revision Queue

Agent: pull top 4-5 into daily revision slots by due date.
Rule: 24h after first solve → first revision. 3d after that → recall check. 7d → final recall.

| Problem | LC# | Due | Notes |
|---------|-----|-----|-------|
| Sort Chars by Freq | 451 | May 17 | 3d recall (OVERDUE) |
| Intersection II | 350 | May 17 | 3d recall (OVERDUE) |
| First Unique Character | 387 | May 18 | 3d recall |
| Best Time Stock | 121 | May 18 | 3d recall |
| Running Sum | 1480 | May 18 | 3d recall |
| Find Highest Altitude | 1732 | May 18 | 24h recall |
| Maximum Product Subarray | 152 | May 18 | 24h recall |
| Isomorphic Strings | 205 | May 18 | 24h recall |
| Valid Palindrome | 125 | May 19 | 3d recall |
| Reverse String | 344 | May 19 | 3d recall |
| Is Subsequence | 392 | May 19 | 3d recall |
| Top K Frequent | 347 | May 19 | 3d recall |
| Majority Element | 169 | May 19 | 3d recall |
| Product of Array Except Self | 238 | May 20 | 3d recall |
| Subarray Sum Equals K | 560 | May 20 | 3d recall |
| Maximum Subarray | 53 | May 20 | 3d recall |
| Two Sum | 1 | May 22 | 7d final recall |
| Valid Anagram | 242 | May 22 | 7d final recall |
| Group Anagrams | 49 | May 24 | 7d final recall |
| Find Pivot Index | 724 | May 24 | 7d final recall |

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

Unique problems LC accepted: 13
Weekly LC slot: 45 min, clear pending problems you feel confident on

---

## Weekly Scores

| Week | New Problems | Revisions | LC Accepted | Independent% |
|------|-------------|-----------|-------------|--------------|
| 1 | 29 | 14 | 0 | 67% |
| 2 (partial) | 17 | 23 | 17 | 73% |

---

## Week 2 Schedule

| Day | Date | Type | Focus |
|-----|------|------|-------|
| Day 9 | May 15 | Reinforcement | Freq Sorting + Complement |
| Day 10 | May 16 | Reinforcement | Prefix Sum + Running State |
| Day 11 | May 17 | Retrieval | 3d recall blitz — all May 17 items |
| Day 12 | May 18 | Recovery | Week review + Week 3 plan |

---

## Mastered (light recall only)

Contains Duplicate, Reverse String (in-place), Move Zeroes,
Majority Element (dict version), Intersection of Two Arrays (unique),
Print/Sum/Count/Max/Min basics, Check Sorted Array

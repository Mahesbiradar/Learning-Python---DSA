# DSA STATUS
Last updated: 2026-05-15 (Day 9)
Current: Month 1 | Week 2 | Day 9
Week 2 days remaining: 2 (Days 10, 11 then Recovery Day 12)

---

## Pattern Family Stability

| Family | Level | Primary Blocker | LC Accepted |
|--------|-------|-----------------|-------------|
| Frequency Hashing | Stable | — | 4 |
| Grouping Hash Maps | Building | Group Anagrams 3d recall due May 17 | 1 |
| Frequency Sorting | Building | Top K lambda recalled D9, pending LC | 0 |
| Complement Lookup | Stable | ✓ Two Sum independent + LC | 2 |
| Prefix Sum | Building | Product output+suffix unsolved | 2 |
| Two Pointers | Building | Subsequence membership instinct | 0 |
| Running-State Tracking | Building | — | 1 |

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
| Valid Palindrome | 125 | Two Pointers | pending | solved D4 |
| Reverse String | 344 | Two Pointers | pending | solved D4 |
| Is Subsequence | 392 | Two Pointers | pending | hint-dependent still |
| Running Sum | 1480 | Prefix Sum | pending | ready to submit |
| Find Pivot Index | 724 | Prefix Sum | ✓ | |
| Best Time Stock | 121 | Running State | ✓ | |
| Group Anagrams | 49 | Grouping Hash Maps | ✓ | |
| Top K Frequent | 347 | Freq Sorting | pending | ready to submit |
| Sort Chars by Freq | 451 | Freq Sorting | ✓ | |
| Intersection Arrays II | 350 | Freq Hashing | ✓ | |
| Majority Element | 169 | Freq Hashing | pending | ready to submit |

---

## Revision Queue

Agent: pull top 4-5 into daily revision slots by due date.
Rule: 24h after first solve → first revision. 3d after that → recall check. 7d → final recall.

| Problem | LC# | Due | Notes |
|---------|-----|-----|-------|
| Valid Palindrome | 125 | May 15 | overdue |
| Is Subsequence | 392 | May 15 | overdue |
| Reverse String | 344 | May 15 | overdue |
| Top K Frequent | 347 | May 16 | |
| Majority Element | 169 | May 16 | |
| Group Anagrams | 49 | May 17 | 3d recall |
| Find Pivot Index | 724 | May 17 | 3d recall |
| Sort Chars by Freq | 451 | May 17 | 3d recall |
| Intersection II | 350 | May 17 | 3d recall |
| First Unique Character | 387 | May 18 | 3d recall |
| Best Time Stock | 121 | May 18 | 3d recall |
| Running Sum | 1480 | May 18 | 3d recall |
| Two Sum | 1 | May 22 | 7d final recall |
| Valid Anagram | 242 | May 22 | 7d final recall |

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

Unique problems LC accepted: 7
Weekly LC slot: 45 min, clear pending problems you feel confident on

---

## Weekly Scores

| Week | New Problems | Revisions | LC Accepted | Independent% |
|------|-------------|-----------|-------------|--------------|
| 1 | 29 | 14 | 0 | 67% |
| 2 (partial) | 11 | 13 | 11 | 78% |

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

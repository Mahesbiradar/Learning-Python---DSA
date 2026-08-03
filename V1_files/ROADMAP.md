# DSA Roadmap — 4 Months to Job Ready

Start: 2026-05-01 | Target: 2026-10-01 (updated from Sep 1 — matches STATUS.md timeline)
Daily: 6+ hours | Problems/day: 3-4 new + 3-4 revision
LC Strategy: Submit revision problems (after independent local solve)
Last updated: 2026-07-01 (Day 30 audit — phase status corrected from solution file evidence)

---

## Phase 1 — Arrays + Hashing + Strings (Weeks 1–9)
**Status: NEARING COMPLETION — Week 9 (as of 2026-07-01)**
**Actual duration: Extended from planned 6 weeks to 9 weeks due to gap-fill sessions on Prefix Modulo and Binary Search applied variants.**

Progress as of Day 30:
- 10/12 must-solve problems complete (LC accepted)
- 59 unique LC problems accepted total across Phase 1 scope
- 30 problems at Tier 4 (mastered)
- Remaining gaps: LC 128 (Longest Consecutive Sequence), LC 443 (String Compression)
- Unresolved concept: Prefix Sum + Modulo derivation (standalone session required — see STATUS.md)

Patterns to master:
- Linear traversal, tracking, adjacent comparison ✓
- Write pointer (remove, compact, move) ✓
- Set lookup, complement lookup (Two Sum) ✓
- Frequency hashing, grouping hash maps, frequency sorting ✓
- Prefix sum (pivot, running, range query, hash map combo) ✓
- Prefix sum + modulo (LC 523, 974 stable; LC 1590 still shaky)
- Running state (stock profit, Kadane's, max product) ✓
- Two pointers: opposite direction, skip loops, subsequence scan, maximize/minimize ✓
- Sliding window: fixed size ✓, variable size ✓
- Binary search: standard ✓, lower-bound ✓, applied (partially)

Must-solve problems (LeetCode accepted required):
1. Contains Duplicate ✓ Tier 4
2. Two Sum ✓ Tier 2
3. Valid Anagram ✓ Tier 4
4. First Unique Character in a String ✓ Tier 4
5. Valid Palindrome ✓ Tier 4
6. Best Time to Buy and Sell Stock ✓ Tier 4
7. Product of Array Except Self ✓ Tier 4
8. Group Anagrams ✓ Tier 4
9. Top K Frequent Elements ✓ Tier 4
10. Longest Consecutive Sequence — NOT YET ATTEMPTED (add Day 31–33)
11. Subarray Sum Equals K ✓ Tier 3
12. String Compression or Encode/Decode — NOT YET ATTEMPTED (add Day 33–35)

Phase 1 close-out target: Week 10 (approx. 2026-07-10)

Weekly problem target: 20-25 total (new + revision)
LC accepted target: 4-5 per week

---

### Weekly Unseen Problem Quota (effective Week 7, i.e. 2026-06-15 onward)

Starting Week 7, every week must include at least 3 unseen Medium problems solved cold:
- No pattern hint provided on the problem card
- No "Trigger words" section shown in advance
- Solve independently, time-boxed to 35 min
- If failed → Tier 1. If hint needed → Tier 1. Only independent solves within 35 min count.
- Purpose: verify that pattern recognition has generalized beyond memorization

Track in Weekly Scores column as "Unseen Mediums: X/3"

---

## Phase 2 — Two Pointers (advanced) + Stack + Queue (Weeks 10–13)
**Status: NOT STARTED — target start approx. 2026-07-10**
**Note: Sliding Window and Two Pointers (sorted/maximize) were completed ahead of schedule during Phase 1 gap-fill sessions (Days 26–30). Phase 2 therefore skips those and focuses on Stack, Queue, and harder Two Pointer variants.**

Patterns to master:
- Sorted array two pointers: 3Sum, Trapping Rain Water (not yet attempted)
- Stack: basic operations (Valid Parentheses, Min Stack), monotonic stack (Daily Temperatures)
- Queue/deque: basics, sliding window maximum
- Binary Search applied: rotated array (LC 33), search on answer (LC 875, LC 1011)

Must-solve problems:
Two pointers (remaining): 3Sum (LC 15), Trapping Rain Water (LC 42)
Stack: Valid Parentheses (LC 20), Min Stack (LC 155), Daily Temperatures (LC 739)
Queue: Sliding Window Maximum (LC 239)
Binary Search applied: Search in Rotated Array (LC 33), Koko Eating Bananas (LC 875)
Sliding window (remaining gap): Min Window Substring (LC 76)

Weekly target: 22-28 total
LC accepted target: 5-6 per week

---

## Phase 3 — Linked List + Trees + BST (Weeks 13–17)
**Status: NOT STARTED — target start approx. 2026-08-01**

Patterns to master:
- Linked list: traversal, reversal, dummy node, fast/slow pointer
- Tree DFS: recursion, preorder/inorder/postorder, path sum
- Tree BFS: level order
- BST: validation, search, LCA

Must-solve: 18 problems (see full list in STATUS.md)
Weekly target: 22-28 total
LC accepted target: 5-6 per week

---

## Phase 4 — Graphs + DP + Greedy + Mocks (Weeks 17–21)
**Status: NOT STARTED — target start approx. 2026-09-01**

Patterns to master:
- Graph BFS/DFS, grid traversal
- 1D DP: state + transition (Fibonacci-style, subsequence-style)
- Greedy: intervals, reachability

Must-solve: 18 problems (see full list in STATUS.md)
Weekly target: 18-22 total (heavy mock focus)
LC accepted target: 4-5 per week + 3 full mock sessions/week

Mock interview schedule (Phase 4):
- Weeks 17–18: 1 mock per week (60 min, 2 Medium problems, no hints)
- Weeks 19–20: 2 mocks per week
- Week 21: 3 mocks per week, unseen Hard exposure begins

---

## Total Targets
Problems solved: 350-400
LC accepted: 100-120 (revised up from 80-100 given actual pace of 59 by Day 30)
Full mocks: 12-15
Timeline: ~21 weeks from May 1 (target interview: October 2026)

Progress as of Day 30 (2026-07-01):
- 59 unique LC accepted (target pace: on track)
- Phase 1: 83% complete (10/12 must-solve done)
- Phase 2–4: not started
- Biggest risk: Prefix Modulo derivation gap, time complexity annotation errors

---

## Mastery Criteria (problem is done when ALL are true)
1. Solved from scratch without hints on a fresh day
2. LeetCode accepted
3. Can explain brute force and optimized approach aloud
4. Time and space complexity correct with named variables
5. Re-solved once after 3+ days without reading previous solution

## Revision Schedule
- Independent first solve: revisit at 3d, 7d, 14d
- Hint used: revisit at 1d, 3d, 7d
- Solution viewed: revisit at 1d, 3d, 7d, 14d
- Failed on revision: restart clock from 1d

## Unseen Problem Quota (mandatory from Week 7 onward)
Every week: 3 unseen Medium problems, solved cold with no pattern hint.
These must be tracked in the Weekly Scores table as "Unseen: X/3".
Independent cold solve within 35 min = Tier 2 minimum. Anything else = Tier 1.

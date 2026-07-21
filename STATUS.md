# DSA STATUS
Current Study Day: 42
Last updated: 2026-07-21 (D42 Catch-up completed)
Current: Month 2 | Week 12 | 12 overdue Tier 3 problems cleared. 4 overdue Tier 3 remain.
Next focus: Jul 22 — LC23 (Tier 1) + remaining 4 overdue Tier 3 Arrays (LC560, LC930, LC58, LC278). Binary Search Applied standalone confirmation pending Day 43.
Target: Junior SDE 6-8 LPA | Timeline: Oct 2026

---

## RULE PRECEDENCE (highest → lowest)

1. Recovery Day
2. Assessment Day
3. Mandatory Standalone Session (from STATUS)
4. Consolidation Day
5. Tier 1 revisions
6. Tier 2 revisions
7. Tier 3 revisions
8. Tier 4 recalls
9. New problems from Learning Phase

If two rules conflict, always obey the higher-priority rule.


## DATA PRECEDENCE

When multiple uploaded files contain overlapping information, use:

1. STATUS.md
2. DAY_N_SOLUTIONS.py
3. DAY_N.md

Never reconcile conflicting values manually.

If STATUS.md already contains an aggregated value,
use it instead of recalculating.

## MANDATORY STANDALONE SESSION

If STATUS declares a mandatory standalone session:

- It overrides the normal Learning Phase for that day only.
- All standalone problems are mandatory.
- Do not replace them with older overdue revisions.
- Generate the standalone note exactly once at the top of the DAY file.

## SYSTEM RULES (agent must read before generating any plan)

Daily target: 10-12 problems total (new + revision combined)
Weekly assessment: Every Friday — 4 unseen problems, no hints, 30 min each
Problem total target: 200-250 solved | LC accepted target: 115-120

Tier definitions:
  TIER 1 (SHAKY): hint-needed OR wrong approach OR &gt;40 min OR failed → revisit next day
  TIER 2 (BUILDING): independent but &gt;25 min OR first time solving variant → revisit in 3 days
  TIER 3 (STABLE): independent + &lt;25 min + LC accepted → revisit in 7 days
  TIER 4 (MASTERED): stable + 14-day recall passed + &lt;10 min → revisit in 30 days (template only)

Tier movement:
  Independent + fast → move UP one tier
  Hint needed or failed → drop to TIER 1 (restart clock)
  New unseen problem → start at TIER 2
  TIER 4 fails 30-day recall → drop to TIER 2

Pattern stability upgrade rule: 70%+ independent on variant + 5 LC accepted in family → Stable
Pattern assessment trigger: all variants of a DS complete → Friday assessment with 4 unseen problems

Daily revision slots:
  TIER 1: all due today (priority, no cap)
  TIER 2: 3 problems
  TIER 3: 2 problems
  TIER 4: 2 template recalls (write template from memory, no full solve)
  New problems: 3-4

SOP reference: problem_solving.md
Solution comment fields required: Status / Time taken / Tier / Time complexity / Space complexity / LC status / Pattern / Variant / mistakes

---

## PATTERN COVERAGE MAP

Format: Pattern | Variant | Solved | Target | Status | Next problems needed

### DS 1: Arrays + Hash Maps + Strings (Phase: Gap-Fill)

| Pattern | Variant | Solved | Target | Status | Pending problems |
|---------|---------|--------|--------|--------|-----------------|
| Frequency Hashing | Count + query | 7 | 12 | Stable | LC 290, 1512, 884, 748, 771 |
| Grouping Hash Map | Canonical key grouping | 2 | 8 | Stable | LC 249, 1002, 2273, 1657, 2135, 49-v2 |
| Frequency Sorting | Sort by count | 3 | 8 | Stable | LC 1636, 2206, 1051, 791, 2418 |
| Complement Lookup | Two Sum style | 3 | 8 | Stable | LC 653, 2006, 1010, 2351, 1512 |
| Prefix Sum | Running prefix | 3 | 8 | Stable | LC 2485, 1413, 2574, 1854 |
| Prefix Sum | Pivot / equilibrium | 2 | 6 | Stable | LC 2270, 1991, 1744 |
| Prefix Sum | Prefix + Hash Map (560 style) | 3 | 8 | Building | LC 930, 1124, 974, 1477 |
| Prefix Sum | Modulo variant (523 style) | 4 | 8 | Building | LC 2262 (not submitted) |
| Two Pointers | Opposite ends — palindrome/reverse | 3 | 8 | Stable | LC 680, 977, 283, 1768 |
| Two Pointers | Write pointer — compact/remove | 2 | 8 | Stable | LC 283, 905, 2460, 75, 1089 |
| Two Pointers | Maximize/minimize between ends | 3 | 10 | Building | LC 42, 633, 11584, 2824 |
| Sliding Window | Fixed size | 5 | 10 | Stable | LC 2090, 1343, 1052, 2269 |
| Sliding Window | Variable size | 5 | 12 | Stable | LC 159, 340, 487, 1493, 2024 |
| Running State | Kadane / min-max tracking | 3 | 8 | Stable | LC 918, 2401, 1749, 1186 |
| Binary Search | Standard — find target | 3 | 8 | Stable | LC 374, 540, 1346, 2300 |
| Binary Search | Lower bound — first position | 4 | 10 | Building | LC 34, 2529, 1385, 1064 |
| Binary Search | Applied — non-obvious structure | 5 | 10 | Building (D42 standalone Day 1: LC33 independent 30min, LC153 independent 15min, LC875 independent 25min. All Accepted. Awaiting Day 43 cold confirmation before marking chronic pattern broken.) | LC 1095, 1011 |
| Hash Set | Sequence expansion | 1 | 6 | Building | LC 128 accepted D37 independent in 20 min; space-complexity comment was a minor metadata miss, held Tier 3 |

### DS 2: Linked Lists (Phase: Volume Building)

| Pattern | Variant | Solved | Target | Status | Problems |
|---------|---------|--------|--------|--------|---------|
| Traversal + basic ops | Reverse a list | 1 | 6 | Building | LC 206 independent again D37 (15 min) after D35 recovery; needs volume beyond one variant |
| Dummy node | Remove Nth / merge | 3 | 6 | Building | LC 21 reconfirmed; LC 19 recovered independent D37; LC 23 attempted D42 (hints, 45min, Tier 1) |
| Fast + slow pointer | Middle / cycle detection | 3 | 6 | Building | LC876 independent D38; LC141 Floyd O(1) solved cold D41; LC142 Floyd entry Tier 3 |
| In-place manipulation | Reorder / reverse groups | 6 | 6 | Building | LC92/2130/234 independent; LC143 recovered independent D39; LC328 cold Tier 3; LC24 cold Tier 3 D41 |

### DS 3: Stack + Queue (Phase: NOT STARTED)

| Pattern | Variant | Solved | Target | Status | Problems |
|---------|---------|--------|--------|--------|---------|
| Basic Stack | Valid parens / min stack | 0 | 6 | NOT STARTED | LC 20, 155, 1047, 2390 |
| Monotonic Stack | Next greater element | 0 | 6 | NOT STARTED | LC 739, 496, 503, 901 |
| Deque / Sliding Window Max | Window max | 0 | 6 | NOT STARTED | LC 239, 1438, 862 |

### DS 4: Trees (Phase: NOT STARTED)

| Pattern | Variant | Solved | Target | Status | Problems |
|---------|---------|--------|--------|--------|---------|
| Tree DFS | Depth / height | 0 | 6 | NOT STARTED | LC 104, 111, 543, 1026 |
| Tree DFS | Path sum / structure | 0 | 6 | NOT STARTED | LC 112, 113, 226, 100 |
| Tree DFS | Traversal (pre/in/post) | 0 | 6 | NOT STARTED | LC 144, 94, 145, 105 |
| Tree BFS | Level order | 0 | 6 | NOT STARTED | LC 102, 107, 103, 637 |
| BST | Search / validate | 0 | 6 | NOT STARTED | LC 700, 98, 530, 701 |
| BST | LCA / operations | 0 | 6 | NOT STARTED | LC 235, 236, 450 |

### DS 5: Graphs (Phase: NOT STARTED)

| Pattern | Variant | Solved | Target | Status | Problems |
|---------|---------|--------|--------|--------|---------|
| Graph DFS | Components / flood fill | 0 | 6 | NOT STARTED | LC 200, 695, 547, 1020 |
| Graph BFS | Shortest path | 0 | 6 | NOT STARTED | LC 542, 994, 1162, 1926 |
| Grid traversal | Islands / surrounded | 0 | 6 | NOT STARTED | LC 130, 417, 286, 1254 |

### DS 6: Heap (Phase: NOT STARTED)

| Pattern | Variant | Solved | Target | Status | Problems |
|---------|---------|--------|--------|--------|---------|
| Min/Max Heap | Top K / Kth largest | 0 | 6 | NOT STARTED | LC 215, 703, 347-heap, 1046 |
| Two Heaps | Median stream | 0 | 4 | NOT STARTED | LC 295, 480 |

### DS 7: Dynamic Programming 1D (Phase: NOT STARTED)

| Pattern | Variant | Solved | Target | Status | Problems |
|---------|---------|--------|--------|--------|---------|
| 1D DP | Fibonacci style | 0 | 6 | NOT STARTED | LC 70, 198, 213, 746 |
| 1D DP | Subsequence style | 0 | 6 | NOT STARTED | LC 300, 322, 139, 416 |

---

## PROBLEM TRACKER

| Problem | LC# | Pattern | Variant | Tier | Last Solved | Next Due | LC | Notes |
|---------|-----|---------|---------|------|------------|----------|-----|-------|
| Contains Duplicate | 217 | Freq Hashing | Count+query | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed D23 |
| Valid Anagram | 242 | Freq Hashing | Count+query | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed D23 |
| First Unique Character | 387 | Freq Hashing | Count+query | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed D23 |
| Intersection Arrays II | 350 | Freq Hashing | Count+query | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed D23 |
| Majority Element | 169 | Freq Hashing | Count+query | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed D23 |
| Unique Number of Occurrences | 1207 | Freq Hashing | Count+query | 3 | Jul 21 | Jul 28 | ✓ | D42 catch-up independent 15 min, accepted — reconfirmed Tier 3 |
| Ransom Note | 383 | Freq Hashing | Count+query | 3 | Jul 21 | Jul 28 | ✓ | D42 independent 25 min, accepted — reconfirmed Tier 3 |
| Group Anagrams | 49 | Grouping Hash Map | Canonical key | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D23 passed |
| Isomorphic Strings | 205 | Grouping Hash Map | Canonical key | 3 | Jul 21 | Jul 28 | ✓ | D42 catch-up independent 20 min, accepted — reconfirmed Tier 3, regression risk cleared |
| Top K Frequent Elements | 347 | Freq Sorting | Sort by count | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D23 passed |
| Sort Chars by Frequency | 451 | Freq Sorting | Sort by count | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D23 passed |
| Top K Frequent Words | 692 | Freq Sorting | Sort by count | 3 | Jul 16 | Jul 23 | ✓ | independent D38, 20 min, accepted — reconfirmed Tier 3 |
| Two Sum | 1 | Complement Lookup | Two Sum style | 3 | Jul 21 | Jul 28 | ✓ | D42 independent 10 min, accepted — reconfirmed Tier 3 |
| Two Sum II | 167 | Two Pointers | Opposite ends | 3 | Jul 21 | Jul 28 | ✓ | D42 catch-up independent 10 min, accepted — reconfirmed Tier 3 |
| Running Sum | 1480 | Prefix Sum | Running prefix | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| Find Highest Altitude | 1732 | Prefix Sum | Running prefix | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| Find Pivot Index | 724 | Prefix Sum | Pivot | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| Product of Array Except Self | 238 | Prefix Sum | Pivot | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| Subarray Sum Equals K | 560 | Prefix Sum | Prefix+Hash Map | 3 | Jul 8 | Jul 15 | ✓ | reconfirmed independent D34, 20 min, clean — STILL OVERDUE |
| Range Sum Query | 303 | Prefix Sum | Prefix array | 3 | Jul 21 | Jul 28 | ✓ | D42 independent 20 min, accepted — reconfirmed Tier 3 |
| Contiguous Array | 525 | Prefix Sum | Prefix+Hash Map | 3 | Jul 16 | Jul 23 | ✓ | independent D38, 15 min, accepted — reconfirmed Tier 3 |
| Continuous Subarray Sum | 523 | Prefix Sum | Modulo | 3 | Jul 21 | Jul 28 | ✓ | D42 catch-up independent 25 min, accepted — reconfirmed Tier 3 |
| Valid Palindrome | 125 | Two Pointers | Opposite ends | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D22 passed |
| Reverse String | 344 | Two Pointers | Opposite ends | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D22 passed |
| Is Subsequence | 392 | Two Pointers | Opposite ends | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D22 passed |
| Remove Duplicates | 26 | Two Pointers | Write pointer | 3 | Jul 19 | Jul 26 | ✓ | independent D40, 15 min, accepted — reconfirmed Tier 3 |
| Remove Element | 27 | Two Pointers | Write pointer | 3 | Jul 21 | Jul 28 | ✓ | D42 catch-up independent 15 min, accepted — reconfirmed Tier 3 |
| Container With Most Water | 11 | Two Pointers | Maximize/minimize | 3 | Jul 21 | Jul 28 | ✓ | D42 catch-up independent 15 min, accepted — reconfirmed Tier 3 |
| Maximum Average Subarray I | 643 | Sliding Window | Fixed size | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| Permutation in String | 567 | Sliding Window | Fixed size | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| Find All Anagrams | 438 | Sliding Window | Fixed size | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| Contains Duplicate II | 219 | Sliding Window | Fixed size | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| Maximum Number of Vowels | 1456 | Sliding Window | Fixed size | 3 | Jul 15 | Jul 22 | ✓ | independent D37, 10 min, accepted — reconfirmed Tier 3 |
| Longest Substring Without Repeating | 3 | Sliding Window | Variable size | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| Minimum Size Subarray Sum | 209 | Sliding Window | Variable size | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| Fruits Into Baskets | 904 | Sliding Window | Variable size | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| Max Consecutive Ones III | 1004 | Sliding Window | Variable size | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| Longest Repeating Char Replacement | 424 | Sliding Window | Variable size | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| Best Time to Buy and Sell Stock | 121 | Running State | Kadane/min-max | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D23 passed |
| Maximum Subarray | 53 | Running State | Kadane/min-max | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D22 passed |
| Maximum Product Subarray | 152 | Running State | Kadane/min-max | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D22 passed |
| Binary Search | 704 | Binary Search | Standard | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| Search Insert Position | 35 | Binary Search | Standard | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| First Bad Version | 278 | Binary Search | Standard | 3 | Jul 12 | Jul 19 | ✓ | independent D35, 15 min, output verified — STILL OVERDUE |
| Sqrt(x) | 69 | Binary Search | Lower bound | 4 | Jun 20 | Jul 20 | ✓ | independent, accepted |
| Find Smallest Letter Greater | 744 | Binary Search | Lower bound | 3 | Jul 21 | Jul 28 | ✓ | D42 catch-up independent 10 min, accepted — reconfirmed Tier 3 |
| Find Peak Element | 162 | Binary Search | Lower bound | 3 | Jul 21 | Jul 28 | ✓ | D42 independent 20 min, accepted — reconfirmed Tier 3 |
| Valid Perfect Square | 367 | Binary Search | Lower bound | 3 | Jul 21 | Jul 28 | ✓ | D42 independent 15 min, accepted — reconfirmed Tier 3 |
| Arranging Coins | 441 | Binary Search | Lower bound | 3 | Jul 21 | Jul 28 | ✓ | D42 catch-up independent 20 min, accepted — reconfirmed Tier 3 |
| Guess Number Higher or Lower | 374 | Binary Search | Standard | 3 | Jul 21 | Jul 28 | ✓ | D42 catch-up independent 15 min, accepted — reconfirmed Tier 3 |
| Peak Index in Mountain Array | 852 | Binary Search | Applied | 3 | Jul 19 | Jul 26 | ✓ | independent D40, 15 min, accepted — reconfirmed Tier 3 |
| Length of Last Word | 58 | String Traversal | — | 3 | Jul 12 | Jul 19 | ✓ | independent D35, 10 min, output verified — STILL OVERDUE |
| Search in Rotated Sorted Array | 33 | Binary Search | Applied — exact search | 2 | Jul 21 | Jul 24 | ✓ | D42 standalone session, independent 30 min, accepted — recovered from Tier 1 regression |
| Find Minimum in Rotated Sorted Array | 153 | Binary Search | Applied — boundary search | 3 | Jul 21 | Jul 28 | ✓ | D42 standalone session, independent 15 min, accepted — recovered from Tier 1 regression |
| Koko Eating Bananas | 875 | Binary Search | Applied — boundary/feasibility | 3 | Jul 21 | Jul 29 | ✓ | D42 standalone session, independent 25 min, accepted — reconfirmed Tier 3 |
| Binary Subarrays With Sum | 930 | Prefix Sum | Prefix+Hash Map | 3 | Jul 8 | Jul 15 | ✓ | reconfirmed independent D34, 20 min, clean — STILL OVERDUE |
| Max Number of K-Sum Pairs | 1679 | Two Pointers | Maximize sorted | 3 | Jul 19 | Jul 26 | ✓ | D40 independent 25 min, accepted; complexity corrected to O(n log n) time, O(n) space — promoted Tier 3 |
| Minimize Maximum Pair Sum | 1877 | Two Pointers | Maximize sorted | 3 | Jul 19 | Jul 26 | ✓ | D40 independent 20 min, accepted; complexity corrected to O(n log n) time, O(n) space — promoted Tier 3 |
| Subarray Sums Divisible by K | 974 | Prefix Sum | Modulo | 3 | Jul 21 | Jul 28 | ✓ | D42 catch-up independent 25 min, accepted — reconfirmed Tier 3 |
| Find the Divisibility Array | 2575 | Prefix Sum | Running modulo | 3 | Jul 16 | Jul 23 | ✓ | independent D39, 20 min, accepted; reconfirmed Tier 3 |
| K Divisible Elements Subarrays | 2261 | Brute Force | Subarray enum | 3 | Jul 21 | Jul 28 | ✓ | D42 catch-up independent 25 min, accepted — brute force reconfirmed, optimal still not recalled cold |
| Total Appeal of A String | 2262 | Brute Force | Subarray enum | 1 | Jul 14 | Aug 11 | — | independent brute-force D37 (15 min), printed 28/20 matches examples but O(n²) wrong for constraints and LC not submitted — USER HOLD until Aug 11 / after key patterns finish |
| Longest Consecutive Sequence | 128 | Hash Set | Sequence expansion | 3 | Jul 15 | Jul 22 | ✓ | independent D37, 20 min, accepted — corrected to Tier 3; note: set-based solution uses O(n) space |
| Make Sum Divisible by P | 1590 | Prefix Sum | Modulo | 3 | Jul 21 | Jul 28 | ✓ | D42 catch-up independent 25 min, accepted — reconfirmed Tier 3, USO remains closed |
| Reverse Linked List | 206 | Traversal + basic ops | Reverse a list | 3 | Jul 15 | Jul 22 | ✓ | independent D37, 15 min, accepted — second cold solve after D34 hint |
| Reverse Linked List II | 92 | In-place manipulation | Reverse between positions | 3 | Jul 15 | Jul 22 | ✓ | independent D37, 20 min, accepted — timed cleanup confirms Tier 3 |
| Merge Two Sorted Lists | 21 | Dummy node | Merge sorted lists | 3 | Jul 15 | Jul 22 | ✓ | independent D37, 15 min, accepted — dummy merge reconfirmed |
| Remove Nth Node From End | 19 | Dummy node | Remove nth from end | 3 | Jul 15 | Jul 22 | ✓ | independent D37, 15 min, accepted — recovered from D36 hint |
| Maximum Twin Sum of a Linked List | 2130 | In-place manipulation | Twin sum / reverse second half | 3 | Jul 15 | Jul 22 | ✓ | independent D37, 15 min, accepted — recovered from D36 hint |
| Linked List Cycle | 141 | Fast + slow pointer | Cycle detection | 3 | Jul 20 | Jul 27 | ✓ | D41 independent 15 min, accepted; Floyd O(1) solved COLD — major breakthrough, promoted Tier 3 |
| Middle of the Linked List | 876 | Fast + slow pointer | Middle node | 3 | Jul 16 | Jul 23 | ✓ | independent D38, 10 min, accepted |
| Linked List Cycle II | 142 | Fast + slow pointer | Cycle entry | 3 | Jul 19 | Jul 26 | ✓ | D40 independent 20 min, accepted; Floyd entry solved COLD — major recovery, promoted Tier 3 |
| Palindrome Linked List | 234 | In-place manipulation | Palindrome check / reverse second half | 3 | Jul 16 | Jul 23 | ✓ | independent D38, 15 min, accepted |
| Reorder List | 143 | In-place manipulation | Reorder by reversing second half | 3 | Jul 16 | Jul 23 | ✓ | independent D39, 25 min, accepted; recovered from D38 hint |
| Odd Even Linked List | 328 | In-place manipulation | Odd-even index partition | 3 | Jul 19 | Jul 26 | ✓ | D40 independent 20 min, accepted; pointer partition solved cold — promoted Tier 3 |
| Swap Nodes in Pairs | 24 | In-place manipulation | Local pointer rewiring | 3 | Jul 20 | Jul 27 | ✓ | D41 independent 20 min, accepted; local rewiring solved COLD — promoted Tier 3 |
| Merge k Sorted Lists | 23 | Linked List | Dummy node — merge k sorted lists | 1 | Jul 21 | Jul 23 | ✓ | D42 new problem, hints needed, 45 min, accepted — Tier 1 |

---

## REVISION POOL — CURRENT

### TIER 1 — Due ASAP (solve before anything else)

| Problem | LC# | Due | Why TIER 1 |
|---------|-----|-----|-----------|
| Merge k Sorted Lists | 23 | Jul 23 | D42 new problem, hints needed, 45 min |

### ON HOLD — Do not schedule before Aug 11

| Problem | LC# | Resume Date | Reason |
|---------|-----|-------------|--------|
| Total Appeal of A String | 2262 | Aug 11 | User-deferred optimized O(n) derivation for 4 weeks; finish key patterns first |

### TIER 2 — Due in 3 days

| Problem | LC# | Due | Notes |
|---------|-----|-----|-------|
| Search in Rotated Sorted Array | 33 | Jul 24 | D42 standalone session, independent 30 min — monitor for Tier 3 promotion on next cycle |

### TIER 3 — Due in 7 days

| Problem | LC# | Due |
|---------|-----|-----|
| Find Minimum in Rotated Sorted Array | 153 | Jul 28 |
| Find Peak Element | 162 | Jul 28 |
| Range Sum Query | 303 | Jul 28 |
| Two Sum | 1 | Jul 28 |
| Valid Perfect Square | 367 | Jul 28 |
| Ransom Note | 383 | Jul 28 |
| Koko Eating Bananas | 875 | Jul 29 |
| Unique Number of Occurrences | 1207 | Jul 28 |
| Two Sum II | 167 | Jul 28 |
| Subarray Sums Divisible by K | 974 | Jul 28 |
| Continuous Subarray Sum | 523 | Jul 28 |
| Container With Most Water | 11 | Jul 28 |
| Isomorphic Strings | 205 | Jul 28 |
| Remove Element | 27 | Jul 28 |
| Arranging Coins | 441 | Jul 28 |
| Find Smallest Letter Greater | 744 | Jul 28 |
| Guess Number Higher or Lower | 374 | Jul 28 |
| Make Sum Divisible by P | 1590 | Jul 28 |
| K Divisible Elements Subarrays | 2261 | Jul 28 |
| Longest Consecutive Sequence | 128 | Jul 22 |
| Maximum Number of Vowels | 1456 | Jul 22 |
| Contiguous Array | 525 | Jul 23 |
| Top K Frequent Words | 692 | Jul 23 |
| Find the Divisibility Array | 2575 | Jul 23 |
| Middle of the Linked List | 876 | Jul 23 |
| Palindrome Linked List | 234 | Jul 23 |
| Reorder List | 143 | Jul 23 |
| Peak Index in Mountain Array | 852 | Jul 26 |
| Remove Duplicates | 26 | Jul 26 |
| Max Number of K-Sum Pairs | 1679 | Jul 26 |
| Minimize Maximum Pair Sum | 1877 | Jul 26 |
| Linked List Cycle II | 142 | Jul 26 |
| Odd Even Linked List | 328 | Jul 26 |
| Linked List Cycle | 141 | Jul 27 |
| Swap Nodes in Pairs | 24 | Jul 27 |
| Reverse Linked List | 206 | Jul 22 |
| Merge Two Sorted Lists | 21 | Jul 22 |
| Reverse Linked List II | 92 | Jul 22 |
| Remove Nth Node From End | 19 | Jul 22 |
| Maximum Twin Sum of a Linked List | 2130 | Jul 22 |

### TIER 3 — OVERDUE (must schedule immediately)

| Problem | LC# | Original Due |
|---------|-----|-------------|
| Subarray Sum Equals K | 560 | Jul 15 |
| Binary Subarrays With Sum | 930 | Jul 15 |
| Length of Last Word | 58 | Jul 19 |
| First Bad Version | 278 | Jul 19 |

### TIER 4 — Due in 30 days (template recall only)

All problems in Mastered section below. 
- Frequency Hashing recall completed D42 → next due Aug 20
- Prefix Sum Pivot recall completed D42 → next due Aug 20
- Remainder overdue since Jul 20

Template recall = write the pattern template from memory in 3 min. No full solve needed.

---

## PATTERN FAMILY STABILITY

| Family | Status | Independent% | LC Accepted | Blocker |
|--------|--------|-------------|-------------|---------|
| Frequency Hashing | Stable | 90%+ | 7 | — |
| Grouping Hash Maps | Stable | 85% | 2 | — (Isomorphic Strings reconfirmed D42 catch-up, blocker cleared) |
| Frequency Sorting | Stable | 80% | 3 | Top K Words reconfirmed D38 in 20 min |
| Complement Lookup | Stable | 85% | 3 | Two Sum had mapping error D23 |
| Prefix Sum (running/pivot) | Stable | 90% | 8 | — |
| Prefix Sum (Hash Map combo) | Building | 100% | 3 | 525 reconfirmed D38; need 5 LC ✓ for Stable (2 more) |
| Prefix Sum (Modulo) | Building | improving after regression | 4 | LC1590 reconfirmed independent D42 catch-up; keep one more cold cycle before calling stable |
| Contribution Counting / Substring Appeal | On hold until Aug 11 | 0% optimal on LC 2262 | 0 | 6 consecutive attempts stayed brute force through D37; user-deferred until key patterns are finished |
| Two Pointers (opposite/write) | Stable | 85% | 5 | — |
| Two Pointers (maximize) | Building | 100% | 5 | 4 problems, all independent, LC ✓ — needs 4+ more |
| Sliding Window | Stable | 85% | 9 | LC1456 reconfirmed D37 in 10 min |
| Running State | Stable | 90% | 3 | — |
| Binary Search (standard) | Stable | 90% | 3 | 374 failed |
| Binary Search (lower bound) | Building | 70% | 5 | 441 recovered independent D33 (was hint D32) — improving, monitor next cycle |
| Binary Search (applied) | Building | ~55% (7/12 recent) | 5 | D42 standalone Day 1: all 3 independent. Awaiting Day 43 cold confirmation before marking chronic pattern broken. LC33 still slow at 30 min. |
| Hash Set (Sequence Expansion) | Building | improving | 1 | LC128 accepted D37 independent in 20 min; keep Tier 3, but remember set solution is O(n) space |
| Linked Lists | Building — Volume Phase | ~82% recent | 11 | D42: LC23 (Merge k) required hints + 45 min. All other linked list revisions independent. Dummy node variant now at 3/6. |

---

## PATTERN ASSESSMENT LOG

| Pattern/DS | Date | Score | Result | Notes |
|-----------|------|-------|--------|-------|
| Arrays+Hashing (partial) | Jun 24 | 3/5 | See notes | 383✓ 11✗ 523✗ 1456✓ 852✓(wrong complexity) |

Full pattern assessment pending: complete gap fills first (Two Pointers maximize, Prefix Modulo, Binary Search Applied).

---

## LEARNING PHASE TRACKER

| Phase | Focus | Status | Start | Target End |
|-------|-------|--------|-------|-----------|
| Gap Fill | Two Pointers maximize (LC 11, 42) | Done — 100% independent, needs volume (4/10) | Jun 25 | Jun 28 |
| Gap Fill | Prefix Sum Modulo (LC 523, 974, 1590) | Standalone session done D32 — 523/974 solved cold, 1590 independent first time, USO pending 1 more cold confirm | Jun 27 | Jul 5 |
| Gap Fill | Binary Search Applied (LC 33, 153, 875) | D42 standalone Day 1 completed: LC33 independent 30min, LC153 independent 15min, LC875 independent 25min. All Accepted. Awaiting Day 43 cold confirmation before marking chronic pattern broken. | Jun 30 | Jul 3 (missed) → Jul 21–22 |
| Gap Fill | Binary Search Lower bound (close out) | Recovered — 441 independent D33 (was hint D32) | Jul 3 | Jul 6 (closed) |
| New DS | Linked Lists | Volume Building — D42: LC23 (Merge k) added but Tier 1. Dummy node 3/6. ALL prior blockers cleared D41. | Jul 7 | Jul 23 |
| New DS | Stack + Queue | Not started | Jul 23 | Aug 6 |
| New DS | Trees | Not started | Aug 6 | Aug 27 |
| New DS | Graphs | Not started | Aug 27 | Sep 10 |
| New DS | Heap + 1D DP | Not started | Sep 10 | Sep 24 |
| Mock Phase | Mixed assessments only | Not started | Sep 24 | Oct 15 |

---

## LC SUBMISSION LOG

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
| Jun 24 | Maximum Number of Vowels | 1456 | Accepted |
| Jun 24 | Peak Index in Mountain Array | 852 | Accepted |
| Jun 24 | Ransom Note | 383 | Accepted |
| Jun 25 | Guess Number Higher or Lower | 374 | Accepted |
| Jun 27 | Subarray Sums Divisible by K | 974 | Accepted |
| Jun 27 | Max Number of K-Sum Pairs | 1679 | Accepted |
| Jun 27 | Minimize Maximum Pair Sum | 1877 | Accepted |
| Jun 28 | Container With Most Water | 11 | Accepted |
| Jun 28 | Continuous Subarray Sum | 523 | Accepted |
| Jun 28 | Binary Subarrays With Sum | 930 | Accepted |
| Jun 29 | Range Sum Query - Immutable | 303 | Accepted |
| Jun 29 | Make Sum Divisible by P | 1590 | Accepted |
| Jun 29 | Find the Divisibility Array of a String | 2575 | Accepted |
| Jun 29 | K Divisible Elements Subarrays | 2261 | Accepted |
| Jul 1 | Contiguous Array | 525 | Accepted |
| Jul 2 | Longest Consecutive Sequence | 128 | Accepted |
| Jul 6 | Search in Rotated Sorted Array | 33 | Accepted |
| Jul 6 | Find Minimum in Rotated Sorted Array | 153 | Accepted |
| Jul 6 | Koko Eating Bananas | 875 | Accepted |
| Jul 8 | Reverse Linked List | 206 | Accepted |
| Jul 8 | Reverse Linked List II | 92 | Accepted |
| Jul 12 | Merge Two Sorted Lists | 21 | Accepted |
| Jul 12 | Remove Nth Node From End | 19 | Accepted |
| Jul 12 | Maximum Twin Sum of a Linked List | 2130 | Accepted |
| Jul 14 | Linked List Cycle | 141 | Accepted |
| Jul 16 | Middle of the Linked List | 876 | Accepted |
| Jul 16 | Linked List Cycle II | 142 | Accepted |
| Jul 16 | Palindrome Linked List | 234 | Accepted |
| Jul 16 | Reorder List | 143 | Accepted |
| Jul 21 | Merge k Sorted Lists | 23 | Accepted |

Unique problems LC accepted: 75

---

## WEEKLY SCORES

| Week | New Problems | Revisions | LC Accepted | Independent% | Notes |
|------|-------------|-----------|-------------|--------------|-------|
| 1 | 29 | 14 | 0 | 67% | |
| 2 | 17 | 28 | 15 | 73% | |
| 3 | 12 | 43 | 13 | 67% | |
| 4 | 6 | 31 | 8 | 73% | |
| 5 (Restart) | 5 | 15 | 5 | 70% | |
| 6 (Gap Fill) | 5 | 0 | 3 | 60% | |
| 7 (Gap Fill D26-28) | 7 | 21 | 6 | ~79% (independent) | |
| 8 (Jun 29 - Jul 5, D29-D32) | 4 | 35 | 6 | ~72% | avg 20 min/problem — Fri Jul 3 assessment missed, Recovery Day used Jul 5 |
| 9 (Jul 6, D33) | 3 | 5 | 3 | 63% (5/8) | Reinforcement Day — 128/441 recovered to Tier 3; Binary Search Applied (33,153,875) all hint-needed despite template given directly; Tier 4 recalls skipped |
| 10 (Jul 7-12, D34-D35 processed; Jul 10-11 backlog) | 5 | 12 | 5 unique new (15 accepted attempts) | ~59% (10/17), avg ~25 min | Verdict: Slightly Behind — 2-day backlog + 5 Tier 1 carry-over; no variants moved Stable; LC206 recovered but Linked List dummy/in-place variants remain shaky |
| 11 (Jul 14-20, D36-D41) | 8 | 52 | 5 unique new | ~77% (37/48), avg ~21 min | Linked Lists surged — 8 new variants, all blockers cleared D41. Binary Search Applied collapsed — LC33/153 regressed to hint-needed. 12 overdue Tier 3 problems from Arrays phase need immediate cleanup. |
| 12 (Jul 21, D42+D42-Catch-up) | 1 | 20 | 21 | 95% (20/21) | Standalone session Day 1 + catch-up: 20 revisions total, 100% independent on catch-up block. 4 overdue Tier 3 remain. |

---

## REGRESSION LOG

Tracks problems that were solved independently, then regressed. Use this to identify unstable memory patterns.
Source: Cross-referenced from Day 08–30 solution files.

| Problem | LC# | First Independent | Regression | Cause | Recovered |
|---------|-----|------------------|------------|-------|-----------|
| Subarray Sum Equals K | 560 | Day 14 | Day 22 | Seen old solution — high-volume session fatigue | Day 25 |
| Isomorphic Strings | 205 | Day 12 | Days 22–25 (multiple) | Template recalled without understanding dual-map constraint | Day 25 |
| Max Product Subarray | 152 | Day 14 | Day 24 | Not attempted in full; hint needed on high-volume day | Day 25+ |
| Contains Duplicate II | 219 | Days 16–18 | Days 22–23 | Wrong update order: check → add → shrink confused | Day 25 |
| Find the Divisibility Array | 2575 | Day 30 | Day 38 | Hint needed on rolling modulo despite prior Tier 3 | D39 |
| Search in Rotated Sorted Array | 33 | Day 34 | Day 41 | Hint needed on rotated array binary search after 12 days | D42 — standalone session recovered |
| Find Minimum in Rotated Sorted Array | 153 | Day 34 | Day 41 | Hint needed on boundary search after 12 days | D42 — standalone session recovered |

Rule: if any problem appears in this log twice, it requires a dedicated first-principles session, not another revision cycle.

---

## UNRESOLVED-SINCE-ORIGIN — Standalone Session Required

These concepts have been flagged (by comment fields or explicit notes in solution files) as needing a dedicated session separate from the normal Tier 1 revision queue. They must NOT be folded back into daily revision until the standalone session is complete and the concept is understood from first principles.

| Concept | First Flagged | Evidence | Standalone Session Done? | Date |
|---------|--------------|----------|--------------------------|------|
| Prefix Sum + Modulo derivation | Day 26 (LC 1590 first failure) | Day 32: ran dedicated 60-90 min standalone session. Solved 523, 974 cold+independent, LC 1590 independent first time (30 min, Tier 1→2). Day 34: LC 1590 solved independently AGAIN, cold, no notes (25 min, Accepted) — 2nd consecutive cold independent solve confirms derivation stuck. | Yes | Jul 8 |
| OOP / Class Mechanics (self.prefix in Python) | Day 23 (LC 303 first failure) | Day 31: solved independently (20 min) but comment: "still not internalized why we initialized the list with 0". D42: solved again independent 20 min. | No — monitor next cycle | — |
| Binary Search Applied (feasibility/monotonic predicate on answer space) | Jun 24 assessment (523✗, later flagged Jun 30) | D33: all 3 hint-needed. D34: all 3 independent — chronic pattern broken. D41: LC33/153 BOTH regressed to hint-needed after 12 days. Chronic pattern NOT broken. D42: Standalone Day 1 completed — all 3 independent (LC33 30min, LC153 15min, LC875 25min). Awaiting Day 43 cold confirmation. | In Progress | Jul 21–22 |
| Contribution counting / Total Appeal O(n) derivation | Day 34 (LC 2262 3rd brute-force-only attempt) | Day 37 processed Jul 14: 6th consecutive attempt still O(n²) brute force; user explicitly deferred optimized derivation for 4 weeks to finish key patterns first. Do not schedule before Aug 11. | Deferred | Aug 11 |

Protocol for Standalone Session:
1. Do NOT time-box to 25/40 min targets — give it 60–90 min
2. Write the algebraic derivation or conceptual model by hand before touching code
3. Solve 2–3 problems of the same concept back-to-back in the same session
4. Only mark "Done" if you can solve the hardest variant cold, with no hint, on the NEXT day

---

## MASTERED (Tier 4 — 30-day template recall only)

Contains Duplicate (217), Valid Anagram (242), First Unique Character (387),
Intersection Arrays II (350), Majority Element (169), Group Anagrams (49),
Find Pivot Index (724), Sort Chars by Freq (451), Running Sum (1480),
Find Highest Altitude (1732), Product of Array Except Self (238),
Best Time to Buy and Sell Stock (121), Maximum Subarray (53),
Maximum Product Subarray (152), Valid Palindrome (125), Reverse String (344),
Is Subsequence (392), Top K Frequent Elements (347),
Maximum Average Subarray I (643), Permutation in String (567),
Find All Anagrams (438), Contains Duplicate II (219),
Longest Substring Without Repeating (3), Minimum Size Subarray Sum (209),
Fruits Into Baskets (904), Max Consecutive Ones III (1004),
Longest Repeating Char Replacement (424), Binary Search (704),
Search Insert Position (35), Sqrt(x) (69)

Next Tier 4 recall due: Jul 20, 2026 (overdue — 2 recalls completed D42: Frequency Hashing, Prefix Sum Pivot; remainder pending)
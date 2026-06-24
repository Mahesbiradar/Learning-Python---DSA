# DSA STATUS
Last updated: 2026-06-24 (Day 25 — System Restructure)
Current: Month 2 | Week 6 | Gap-Fill Phase
Next focus: Two Pointers (maximize variant) → Prefix Sum Modulo → Binary Search Applied
Target: Junior SDE 6-8 LPA | Timeline: Oct 2026

---

## SYSTEM RULES (agent must read before generating any plan)

Daily target: 10-12 problems total (new + revision combined)
Weekly assessment: Every Friday — 4 unseen problems, no hints, 30 min each
Problem total target: 200-250 solved | LC accepted target: 115-120

Tier definitions:
  TIER 1 (SHAKY): hint-needed OR wrong approach OR >40 min OR failed → revisit next day
  TIER 2 (BUILDING): independent but >25 min OR first time solving variant → revisit in 3 days
  TIER 3 (STABLE): independent + <25 min + LC accepted → revisit in 7 days
  TIER 4 (MASTERED): stable + 14-day recall passed + <10 min → revisit in 30 days (template only)

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
| Prefix Sum | Prefix + Hash Map (560 style) | 3 | 8 | Shaky | LC 930, 1124, 974, 1477 |
| Prefix Sum | Modulo variant (523 style) | 0 | 8 | NOT STARTED | LC 523, 974, 1590, 2575, 2261 |
| Two Pointers | Opposite ends — palindrome/reverse | 3 | 8 | Stable | LC 680, 977, 283, 1768 |
| Two Pointers | Write pointer — compact/remove | 2 | 8 | Stable | LC 283, 905, 2460, 75, 1089 |
| Two Pointers | Maximize/minimize between ends | 0 | 10 | NOT STARTED | LC 11, 42, 1679, 1877, 633 |
| Sliding Window | Fixed size | 5 | 10 | Stable | LC 2090, 1343, 1052, 2269 |
| Sliding Window | Variable size | 5 | 12 | Stable | LC 159, 340, 487, 1493, 2024 |
| Running State | Kadane / min-max tracking | 3 | 8 | Stable | LC 918, 2401, 1749, 1186 |
| Binary Search | Standard — find target | 3 | 8 | Stable | LC 374, 540, 1346, 2300 |
| Binary Search | Lower bound — first position | 4 | 10 | Building | LC 34, 2529, 1385, 1064 |
| Binary Search | Applied — non-obvious structure | 2 | 10 | Shaky | LC 33, 153, 1095, 875, 1011 |

### DS 2: Linked Lists (Phase: NOT STARTED)

| Pattern | Variant | Solved | Target | Status | Problems |
|---------|---------|--------|--------|--------|---------|
| Traversal + basic ops | Reverse a list | 0 | 6 | NOT STARTED | LC 206, 92, 2130 |
| Dummy node | Remove Nth / merge | 0 | 6 | NOT STARTED | LC 21, 19, 23 |
| Fast + slow pointer | Middle / cycle detection | 0 | 6 | NOT STARTED | LC 876, 141, 142 |
| In-place manipulation | Reorder / reverse groups | 0 | 6 | NOT STARTED | LC 143, 25, 2095 |

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
| Unique Number of Occurrences | 1207 | Freq Hashing | Count+query | 3 | Jun 20 | Jun 27 | ✓ | new D23, independent |
| Ransom Note | 383 | Freq Hashing | Count+query | 3 | Jun 24 | Jul 1 | ✓ | 2 attempts locally, accepted |
| Group Anagrams | 49 | Grouping Hash Map | Canonical key | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D23 passed |
| Isomorphic Strings | 205 | Grouping Hash Map | Canonical key | 2 | Jun 24 | Jun 27 | ✓ | hint-needed D22, D25 independent |
| Top K Frequent Elements | 347 | Freq Sorting | Sort by count | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D23 passed |
| Sort Chars by Frequency | 451 | Freq Sorting | Sort by count | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D23 passed |
| Top K Frequent Words | 692 | Freq Sorting | Sort by count | 2 | Jun 24 | Jun 27 | ✓ | hint D23, independent D25 |
| Two Sum | 1 | Complement Lookup | Two Sum style | 2 | Jun 24 | Jun 27 | ✓ | hint D23 (mapping error), independent D25 |
| Two Sum II | 167 | Complement Lookup | Two Sum style | 3 | Jun 20 | Jun 27 | ✓ | independent D23 |
| Running Sum | 1480 | Prefix Sum | Running prefix | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D23 passed |
| Find Highest Altitude | 1732 | Prefix Sum | Running prefix | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D23 passed |
| Find Pivot Index | 724 | Prefix Sum | Pivot | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D23 passed |
| Product of Array Except Self | 238 | Prefix Sum | Pivot | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D23 passed |
| Subarray Sum Equals K | 560 | Prefix Sum | Prefix+Hash Map | 1 | Jun 25 | Jun 26 | ✓ | shaky - hint D22+D25, needs daily retry |
| Range Sum Query | 303 | Prefix Sum | Prefix+Hash Map | 2 | Jun 25 | Jun 28 | NA | hint-needed D25 |
| Contiguous Array | 525 | Prefix Sum | Prefix+Hash Map | 2 | Jun 25 | Jun 28 | ✓ | hint-needed D25 |
| Continuous Subarray Sum | 523 | Prefix Sum | Modulo | 1 | Jun 24 | Jun 25 | ✗ | failed - concept not known |
| Valid Palindrome | 125 | Two Pointers | Opposite ends | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D22 passed |
| Reverse String | 344 | Two Pointers | Opposite ends | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D22 passed |
| Is Subsequence | 392 | Two Pointers | Opposite ends | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D22 passed |
| Remove Duplicates | 26 | Two Pointers | Write pointer | 2 | Jun 20 | Jun 27 | ✓ | hint D23, independent D25 |
| Remove Element | 27 | Two Pointers | Write pointer | 3 | Jun 20 | Jun 27 | ✓ | independent D23 |
| Container With Most Water | 11 | Two Pointers | Maximize/minimize | 1 | Jun 24 | Jun 25 | — | not attempted - concept gap |
| Maximum Average Subarray I | 643 | Sliding Window | Fixed size | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| Permutation in String | 567 | Sliding Window | Fixed size | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| Find All Anagrams | 438 | Sliding Window | Fixed size | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| Contains Duplicate II | 219 | Sliding Window | Fixed size | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| Maximum Number of Vowels | 1456 | Sliding Window | Fixed size | 2 | Jun 24 | Jun 27 | ✓ | 45 min - too slow |
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
| First Bad Version | 278 | Binary Search | Standard | 3 | Jun 20 | Jun 27 | ✓ | hint D19, independent D20 |
| Sqrt(x) | 69 | Binary Search | Lower bound | 4 | Jun 20 | Jul 20 | ✓ | independent, accepted |
| Find Smallest Letter Greater | 744 | Binary Search | Lower bound | 2 | Jun 20 | Jun 27 | ✓ | hint D20+D21 |
| Find Peak Element | 162 | Binary Search | Lower bound | 2 | Jun 20 | Jun 27 | ✓ | hint D20+D21 |
| Valid Perfect Square | 367 | Binary Search | Lower bound | 2 | Jun 20 | Jun 27 | ✓ | hint D22 |
| Arranging Coins | 441 | Binary Search | Lower bound | 2 | Jun 20 | Jun 27 | ✓ | hint D22 |
| Guess Number Higher or Lower | 374 | Binary Search | Standard | 1 | Jun 20 | Jun 25 | — | failed D22, not retried |
| Peak Index in Mountain Array | 852 | Binary Search | Applied | 2 | Jun 24 | Jun 27 | ✓ | solved O(n) not O(log n) |
| Length of Last Word | 58 | String Traversal | — | 3 | Jun 25 | Jul 2 | ✓ | independent D25 |

---

## REVISION POOL — CURRENT

### TIER 1 — Due ASAP (solve before anything else)

| Problem | LC# | Due | Why TIER 1 |
|---------|-----|-----|-----------|
| Continuous Subarray Sum | 523 | Jun 25 | Failed — concept not known (Prefix Sum Modulo) |
| Container With Most Water | 11 | Jun 25 | Not attempted — concept gap (Two Pointers maximize) |
| Guess Number Higher or Lower | 374 | Jun 25 | Failed D22 — lower bound template shaky |
| Subarray Sum Equals K | 560 | Jun 26 | Shaky — hint needed multiple times |

Note: LC 11 and LC 523 need concept block first. Do NOT attempt without reading PATTERNS.md block.

### TIER 2 — Due in 3 days

| Problem | LC# | Due | Notes |
|---------|-----|-----|-------|
| Isomorphic Strings | 205 | Jun 27 | hint D22, independent D25 |
| Top K Frequent Words | 692 | Jun 27 | hint D23, independent D25 |
| Two Sum | 1 | Jun 27 | hint D23, independent D25 |
| Remove Duplicates | 26 | Jun 27 | hint D23, independent D25 |
| Two Sum II | 167 | Jun 27 | independent D23 (first time) |
| Remove Element | 27 | Jun 27 | independent D23 (first time) |
| Maximum Number of Vowels | 1456 | Jun 27 | 45 min - too slow |
| Find Smallest Letter Greater | 744 | Jun 27 | hint D21 |
| Find Peak Element | 162 | Jun 27 | hint D21 |
| Valid Perfect Square | 367 | Jun 27 | hint D22 |
| Arranging Coins | 441 | Jun 27 | hint D22 |
| Range Sum Query | 303 | Jun 28 | hint-needed D25 |
| Contiguous Array | 525 | Jun 28 | hint-needed D25 |
| Peak Index in Mountain Array | 852 | Jun 27 | O(n) only, O(log n) needed |
| Unique Number of Occurrences | 1207 | Jun 27 | new D23, first 7-day recall |
| Ransom Note | 383 | Jul 1 | new Jun 24, first 7-day recall |
| First Bad Version | 278 | Jun 27 | hint D19 |

### TIER 3 — Due in 7 days

| Problem | LC# | Due |
|---------|-----|-----|
| Length of Last Word | 58 | Jul 2 |

### TIER 4 — Due in 30 days (template recall only)

All problems in Mastered section below. Next due: Jul 20 for most.
Template recall = write the pattern template from memory in 3 min. No full solve needed.

---

## PATTERN FAMILY STABILITY

| Family | Status | Independent% | LC Accepted | Blocker |
|--------|--------|-------------|-------------|---------|
| Frequency Hashing | Stable | 90%+ | 7 | — |
| Grouping Hash Maps | Stable | 85% | 2 | Isomorphic strings shaky |
| Frequency Sorting | Stable | 80% | 3 | Top K Words hint-needed once |
| Complement Lookup | Stable | 85% | 3 | Two Sum had mapping error D23 |
| Prefix Sum (running/pivot) | Stable | 90% | 8 | — |
| Prefix Sum (Hash Map combo) | Shaky | 60% | 3 | 560 hint D22+D25, 525 hint D25 |
| Prefix Sum (Modulo) | Not started | — | 0 | Concept not learned |
| Two Pointers (opposite/write) | Stable | 85% | 5 | — |
| Two Pointers (maximize) | Not started | — | 0 | Concept not learned |
| Sliding Window | Stable | 85% | 9 | 1456 too slow (45 min) |
| Running State | Stable | 90% | 3 | — |
| Binary Search (standard) | Stable | 90% | 3 | 374 failed |
| Binary Search (lower bound) | Building | 60% | 4 | 744/162/367/441 hint-needed |
| Binary Search (applied) | Shaky | 50% | 1 | 852 O(n) not O(log n), 11 not attempted |

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
| Gap Fill | Two Pointers maximize (LC 11, 42) | In Progress | Jun 25 | Jun 28 |
| Gap Fill | Prefix Sum Modulo (LC 523, 974) | Up next | Jun 27 | Jun 30 |
| Gap Fill | Binary Search Applied (LC 33, 153) | Queued | Jun 30 | Jul 3 |
| Gap Fill | Binary Search Lower bound (close out) | Queued | Jul 3 | Jul 5 |
| New DS | Linked Lists | Not started | Jul 7 | Jul 21 |
| New DS | Stack + Queue | Not started | Jul 21 | Aug 4 |
| New DS | Trees | Not started | Aug 4 | Aug 25 |
| New DS | Graphs | Not started | Aug 25 | Sep 8 |
| New DS | Heap + 1D DP | Not started | Sep 8 | Sep 22 |
| Mock Phase | Mixed assessments only | Not started | Sep 22 | Oct 15 |

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
| Jun 24 | Maximum Number of Vowels | 1456 | Accepted |
| Jun 24 | Peak Index in Mountain Array | 852 | Accepted |
| Jun 24 | Ransom Note | 383 | Accepted |

Unique problems LC accepted: 48

---

## WEEKLY SCORES

| Week | New Problems | Revisions | LC Accepted | Independent% |
|------|-------------|-----------|-------------|--------------|
| 1 | 29 | 14 | 0 | 67% |
| 2 | 17 | 28 | 15 | 73% |
| 3 | 12 | 43 | 13 | 67% |
| 4 | 6 | 31 | 8 | 73% |
| 5 (Restart) | 5 | 15 | 5 | 70% |
| 6 (Gap Fill) | 5 | 0 | 3 | 60% |

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

Next Tier 4 recall due: Jul 20, 2026

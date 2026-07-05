# DSA STATUS
Last updated: 2026-07-05 (Day 32 — Recovery Day: Prefix Sum Modulo Standalone Session + Backlog Clearance)
Current: Month 2 | Week 10 | Gap-Fill Phase transitioning to Linked Lists
Next focus: Clear Tier 1 (128, 441) → Linked Lists (Jul 7) → Binary Search Applied/Lower-bound close-out via revision pool
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
| Binary Search | Applied — non-obvious structure | 2 | 10 | Building (flagged for dedicated consolidation — under-practiced 2/10, deferred since Jun 30) | LC 33, 153, 1095, 875, 1011 |
| Hash Set | Sequence expansion | 1 | 6 | Building | LC 128 hint-based D31 — need 4-5 more, verify independence |

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
| Unique Number of Occurrences | 1207 | Freq Hashing | Count+query | 3 | Jul 5 | Jul 12 | ✓ | independent D32, 10 min, clean — reconfirmed Tier 3 |
| Ransom Note | 383 | Freq Hashing | Count+query | 3 | Jul 2 | Jul 9 | ✓ | independent D31, 15 min, clean — reconfirmed Tier 3 |
| Group Anagrams | 49 | Grouping Hash Map | Canonical key | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D23 passed |
| Isomorphic Strings | 205 | Grouping Hash Map | Canonical key | 3 | Jul 5 | Jul 12 | ✓ | independent D32, 15 min, clean — regression risk cleared, no hint needed |
| Top K Frequent Elements | 347 | Freq Sorting | Sort by count | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D23 passed |
| Sort Chars by Frequency | 451 | Freq Sorting | Sort by count | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D23 passed |
| Top K Frequent Words | 692 | Freq Sorting | Sort by count | 3 | Jul 1 | Jul 8 | ✓ | independent D30, 20 min, sort key corrected from memory |
| Two Sum | 1 | Complement Lookup | Two Sum style | 3 | Jul 2 | Jul 9 | ✓ | independent D31, 15 min, clean — Tier 2→3 |
| Two Sum II | 167 | Two Pointers | Opposite ends | 3 | Jul 5 | Jul 12 | ✓ | independent D32, 10 min, clean — reconfirmed Tier 3 |
| Running Sum | 1480 | Prefix Sum | Running prefix | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D23 passed |
| Find Highest Altitude | 1732 | Prefix Sum | Running prefix | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D23 passed |
| Find Pivot Index | 724 | Prefix Sum | Pivot | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D23 passed |
| Product of Array Except Self | 238 | Prefix Sum | Pivot | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D23 passed |
| Subarray Sum Equals K | 560 | Prefix Sum | Prefix+Hash Map | 3 | Jun 28 | Jul 5 | ✓ | independent D28, 25 min, caught prefix=nums[i] bug in test — stays Tier 3 — NOT attempted D32, due date overdue |
| Range Sum Query | 303 | Prefix Sum | Prefix array | 3 | Jul 2 | Jul 9 | ✓ | independent D31, 20 min, output verified — Tier 1→3. Still hasn't internalized why prefix list starts with 0 |
| Contiguous Array | 525 | Prefix Sum | Prefix+Hash Map | 3 | Jul 1 | Jul 8 | ✓ | independent D30, 25 min, both brute+optimal written clean — Tier 1→3 |
| Continuous Subarray Sum | 523 | Prefix Sum | Modulo | 3 | Jul 5 | Jul 12 | ✓ | independent D32, 20 min, solved cold as part of Modulo standalone session — clean |
| Valid Palindrome | 125 | Two Pointers | Opposite ends | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D22 passed |
| Reverse String | 344 | Two Pointers | Opposite ends | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D22 passed |
| Is Subsequence | 392 | Two Pointers | Opposite ends | 4 | Jun 20 | Jul 20 | ✓ | 14d recall D22 passed |
| Remove Duplicates | 26 | Two Pointers | Write pointer | 3 | Jul 1 | Jul 8 | ✓ | independent D30, 10 min, clean |
| Remove Element | 27 | Two Pointers | Write pointer | 3 | Jul 5 | Jul 12 | ✓ | independent D32, 10 min, clean — Tier 2→3, overdue since Jun 28 cleared |
| Container With Most Water | 11 | Two Pointers | Maximize/minimize | 3 | Jul 5 | Jul 12 | ✓ | independent D32, 15 min, clean — reconfirmed Tier 3 |
| Maximum Average Subarray I | 643 | Sliding Window | Fixed size | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| Permutation in String | 567 | Sliding Window | Fixed size | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| Find All Anagrams | 438 | Sliding Window | Fixed size | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| Contains Duplicate II | 219 | Sliding Window | Fixed size | 4 | Jun 20 | Jul 20 | ✓ | 14d recall passed |
| Maximum Number of Vowels | 1456 | Sliding Window | Fixed size | 3 | Jun 29 | Jul 6 | ✓ | independent D29, 25 min, Tier 2→3 |
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
| First Bad Version | 278 | Binary Search | Standard | 3 | Jul 2 | Jul 9 | ✓ | independent D31, 20 min, reconfirmed Tier 3 |
| Sqrt(x) | 69 | Binary Search | Lower bound | 4 | Jun 20 | Jul 20 | ✓ | independent, accepted |
| Find Smallest Letter Greater | 744 | Binary Search | Lower bound | 3 | Jun 29 | Jul 6 | ✓ | independent D29, 22 min, Tier 1→3 recovered |
| Find Peak Element | 162 | Binary Search | Lower bound | 3 | Jul 2 | Jul 9 | ✓ | independent D31, 15 min, reconfirmed Tier 3 |
| Valid Perfect Square | 367 | Binary Search | Lower bound | 3 | Jul 2 | Jul 9 | ✓ | independent D31, 15 min, clean — Tier 2→3 |
| Arranging Coins | 441 | Binary Search | Lower bound | 1 | Jul 5 | Jul 6 | ✓ | Hint D32 (formula for coins needed) — dropped Tier2→1, restart clock. 2nd hint overall (also D22) |
| Guess Number Higher or Lower | 374 | Binary Search | Standard | 3 | Jun 29 | Jul 6 | ✓ | independent D29, 20 min |
| Peak Index in Mountain Array | 852 | Binary Search | Applied | 3 | Jul 1 | Jul 8 | ✓ | independent D30, 15 min, O(log n) clean |
| Length of Last Word | 58 | String Traversal | — | 3 | Jun 29 | Jul 6 | ✓ | independent D29, 20 min |
| Binary Subarrays With Sum | 930 | Prefix Sum | Prefix+Hash Map | 3 | Jun 28 | Jul 5 | ✓ | new D28, independent, 15 min — same as LC 560, recognized immediately |
| Max Number of K-Sum Pairs | 1679 | Two Pointers | Maximize sorted | 3 | Jul 1 | Jul 8 | ✓ | independent D30, 25 min, clean — Tier 2→3 |
| Minimize Maximum Pair Sum | 1877 | Two Pointers | Maximize sorted | 3 | Jul 1 | Jul 8 | ✓ | independent D30, 15 min, clean — Tier 2→3 |
| Subarray Sums Divisible by K | 974 | Prefix Sum | Modulo | 3 | Jul 5 | Jul 12 | ✓ | independent D32, 20 min, solved cold as part of Modulo standalone session — clean |
| Find the Divisibility Array | 2575 | Prefix Sum | Running modulo | 3 | Jul 1 | Jul 8 | ✓ | independent D30, 25 min, formula recalled from recovery note — Tier 1→3 |
| K Divisible Elements Subarrays | 2261 | Brute Force | Subarray enum | 3 | Jul 2 | Jul 9 | ✓ | independent D31 (brute only), 20 min, output verified correct — optimal still not recalled cold |
| Total Appeal of A String | 2262 | Brute Force | Subarray enum | 2 | Jul 5 | Jul 8 | — | D32: independent, 20 min, still brute force O(n²) only — optimal explicitly requested again and not attempted, not submitted |
| Longest Consecutive Sequence | 128 | Hash Set | Sequence expansion | 1 | Jul 5 | Jul 6 | ✓ | D32: Hint again (2nd hint in a row, was told to solve cold with no video/notes) — stays Tier 1, chronic-hint pattern, candidate for standalone session |
| Make Sum Divisible by P | 1590 | Prefix Sum | Modulo | 2 | Jul 5 | Jul 8 | ✓ | D32: independent (30 min) after dedicated Modulo standalone session — Tier 1→2, first independent solve ever on this problem; needs one more cold independent solve on a later day to close USO |

---

## REVISION POOL — CURRENT

### TIER 1 — Due ASAP (solve before anything else)

| Problem | LC# | Due | Why TIER 1 |
|---------|-----|-----|-----------|
| Longest Consecutive Sequence | 128 | Jul 6 | Hint again D32 (2nd hint in a row, told to solve cold) — chronic-hint pattern |
| Arranging Coins | 441 | Jul 6 | Hint D32 (formula for coins needed) — dropped from Tier 2, restart clock |

### TIER 2 — Due in 3 days

| Problem | LC# | Due | Notes |
|---------|-----|-----|-------|
| Total Appeal of A String | 2262 | Jul 8 | D32: independent brute force again, optimal still not attempted despite explicit instruction |
| Make Sum Divisible by P | 1590 | Jul 8 | D32: independent (30 min) after standalone Modulo session — Tier 1→2, first independent solve; needs 1 more cold solve to close USO |

### TIER 3 — Due in 7 days

| Problem | LC# | Due |
|---------|-----|-----|
| Subarray Sum Equals K | 560 | Jul 5 (overdue) |
| Binary Subarrays With Sum | 930 | Jul 5 (overdue) |
| Find Smallest Letter Greater | 744 | Jul 6 |
| Maximum Number of Vowels | 1456 | Jul 6 |
| Length of Last Word | 58 | Jul 6 |
| Guess Number Higher or Lower | 374 | Jul 6 |
| Contiguous Array | 525 | Jul 8 |
| Find the Divisibility Array | 2575 | Jul 8 |
| Top K Frequent Words | 692 | Jul 8 |
| Max Number of K-Sum Pairs | 1679 | Jul 8 |
| Minimize Maximum Pair Sum | 1877 | Jul 8 |
| Peak Index in Mountain Array | 852 | Jul 8 |
| Remove Duplicates | 26 | Jul 8 |
| First Bad Version | 278 | Jul 9 |
| Find Peak Element | 162 | Jul 9 |
| Range Sum Query | 303 | Jul 9 |
| K Divisible Elements Subarrays | 2261 | Jul 9 |
| Two Sum | 1 | Jul 9 |
| Valid Perfect Square | 367 | Jul 9 |
| Ransom Note | 383 | Jul 9 |
| Two Sum II | 167 | Jul 12 |
| Unique Number of Occurrences | 1207 | Jul 12 |
| Subarray Sums Divisible by K | 974 | Jul 12 |
| Continuous Subarray Sum | 523 | Jul 12 |
| Container With Most Water | 11 | Jul 12 |
| Isomorphic Strings | 205 | Jul 12 |
| Remove Element | 27 | Jul 12 |

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
| Prefix Sum (Hash Map combo) | Building | 100% | 3 | 525 recovered D30 — all 3 independent; need 5 LC ✓ for Stable (2 more) |
| Prefix Sum (Modulo) | Building | 85% | 4 | 523/974 solved cold+independent D32 (Modulo standalone session); 1590 independent D32 for first time (30 min, still >25min target) — needs 1 more cold solve to close USO; 2261 reclassified Brute Force (not Modulo) — removed from count |
| Two Pointers (opposite/write) | Stable | 85% | 5 | — |
| Two Pointers (maximize) | Building | 100% | 3 | 4 problems, all independent, LC ✓ — needs 4+ more |
| Sliding Window | Stable | 85% | 9 | 1456 too slow (45 min) |
| Running State | Stable | 90% | 3 | — |
| Binary Search (standard) | Stable | 90% | 3 | 374 failed |
| Binary Search (lower bound) | Building | 60% | 4 | 744/162/367/441 hint-needed |
| Binary Search (applied) | Building | 70% | 2 | 852 O(log n) clean D27, 374 independent D27 |
| Hash Set (Sequence Expansion) | Building | 0% | 1 | LC 128 hint-based D31 AND D32 (told to solve cold, no video — still hint-needed) — chronic hint, candidate for standalone session |

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
| Gap Fill | Binary Search Applied (LC 33, 153) | Deferred — folded into revision pool, dedicated session still needed | Jun 30 | Jul 3 (missed) |
| Gap Fill | Binary Search Lower bound (close out) | Deferred — regressed (441 hint again D32), needs dedicated session before close-out | Jul 3 | Jul 5 (missed) |
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

Unique problems LC accepted: 61

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

Rule: if any problem appears in this log twice, it requires a dedicated first-principles session, not another revision cycle.

---

## UNRESOLVED-SINCE-ORIGIN — Standalone Session Required

These concepts have been flagged (by comment fields or explicit notes in solution files) as needing a dedicated session separate from the normal Tier 1 revision queue. They must NOT be folded back into daily revision until the standalone session is complete and the concept is understood from first principles.

| Concept | First Flagged | Evidence | Standalone Session Done? | Date |
|---------|--------------|----------|--------------------------|------|
| Prefix Sum + Modulo derivation | Day 26 (LC 1590 first failure) | Day 32: ran dedicated 60-90 min standalone session (derivation written by hand, self-reported ~5-6 hrs total study). Solved 523, 974 cold+independent, and LC 1590 independently for the first time (30 min, Tier 1→2). Protocol requires one more cold, independent solve on a LATER day before marking Done. | No — pending Day 33+ cold retest | — |
| OOP / Class Mechanics (self.prefix in Python) | Day 23 (LC 303 first failure) | Day 31: solved independently (20 min) but comment: "still not internalized why we initialized the list with 0" | No | — |

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

Next Tier 4 recall due: Jul 20, 2026

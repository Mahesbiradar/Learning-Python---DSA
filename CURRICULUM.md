# Master DSA Curriculum
## ~156 LeetCode Problems — Pattern-Based Learning Path

---

## 1. Frequency Hashing | Count + query
**Target:** Use a hash map to count frequencies and answer existence / uniqueness queries in O(1) or O(n).

**Problems:**
- LC 217 — Contains Duplicate
- LC 219 — Contains Duplicate II
- LC 1207 — Unique Number of Occurrences
- LC 242 — Valid Anagram

---

## 2. Grouping Hash Map | Canonical key grouping
**Target:** Transform elements into a canonical form so that anagrams, shifted strings, or equivalent items group together.

**Problems:**
- LC 49 — Group Anagrams
- LC 249 — Group Shifted Strings
- LC 205 — Isomorphic Strings
- LC 890 — Find and Replace Pattern
-LC 1002 --Find Common Characters

---

## 3. Frequency Sorting | Sort by count
**Target:** Sort elements based on their frequency or bucket them by frequency to achieve O(n) or O(n log n) solutions.

**Problems:**
- LC 451 — Sort Characters By Frequency
- LC 1636 — Sort Array by Increasing Frequency
- LC 692 — Top K Frequent Words
- LC 347 — Top K Frequent Elements

---

## 4. Complement Lookup | Two Sum style
**Target:** For each element, check if its complement (target − x) has already been seen. Classic hash map trade-off: space for time.

**Problems:**
- LC 1 — Two Sum
- LC 167 — Two Sum II - Input Array Is Sorted
- LC 653 — Two Sum IV - Input is a BST
- LC 1099 — Two Sum Less Than K

---

## 5. Prefix Sum | Running prefix
**Target:** Build a running cumulative sum to answer range-sum queries or detect cumulative properties in O(1) per query after O(n) preprocessing.

**Problems:**
- LC 303 — Range Sum Query - Immutable
- LC 1480 — Running Sum of 1d Array
- LC 1413 — Minimum Value to Get Positive Step by Step Sum
- LC 238 — Product of Array Except Self

---

## 6. Prefix Sum | Pivot / equilibrium
**Target:** Find an index where the left and right subarrays satisfy a balance condition, often using the total sum as a reference.

**Problems:**
- LC 724 — Find Pivot Index
- LC 1991 — Find the Middle Index in Array
- LC 2270 — Number of Ways to Split Array
- LC 2483 — Minimum Penalty for a Shop

---

## 7. Prefix Sum | Prefix + Hash Map (560 style)
**Target:** Count subarrays with a given sum by storing prefix sums in a hash map and checking how many times (current prefix − target) has occurred.

**Problems:**
- LC 560 — Subarray Sum Equals K
- LC 930 — Binary Subarrays With Sum
- LC 325 — Maximum Size Subarray Sum Equals K
- LC 1371 — Find the Longest Substring Containing Vowels in Even Counts

---

## 8. Prefix Sum | Modulo variant (523 style)
**Target:** Use the property that if two prefix sums have the same remainder modulo k, the subarray between them is divisible by k.

**Problems:**
- LC 523 — Continuous Subarray Sum
- LC 525 — Contiguous Array
- LC 1590 — Make Sum Divisible by P
- LC 2845 — Count of Interesting Subarrays

---

## 9. Two Pointers | Opposite ends — palindrome/reverse
**Target:** Initialize pointers at both ends and move inward, comparing or swapping elements. Ideal for palindrome checks and reverse operations.

**Problems:**
- LC 125 — Valid Palindrome
- LC 680 — Valid Palindrome II
- LC 344 — Reverse String
- LC 345 — Reverse Vowels of a String

---

## 10. Two Pointers | Write pointer — compact/remove
**Target:** Use a slow pointer to write valid elements in-place while a fast pointer scans the array. Maintains relative order and achieves O(1) space.

**Problems:**
- LC 26 — Remove Duplicates from Sorted Array
- LC 27 — Remove Element
- LC 283 — Move Zeroes
- LC 80 — Remove Duplicates from Sorted Array II

---

## 11. Two Pointers | Maximize/minimize between ends
**Target:** Move the pointer at the shorter end inward to potentially find a larger area or better pair. Greedy logic backed by two-pointer mechanics.

**Problems:**
- LC 11 — Container With Most Water
- LC 42 — Trapping Rain Water
- LC 15 — 3Sum
- LC 16 — 3Sum Closest

---

## 12. Sliding Window | Fixed size
**Target:** Maintain a window of exactly k elements. Slide it one step at a time, updating aggregates incrementally for O(n) time.

**Problems:**
- LC 643 — Maximum Average Subarray I
- LC 1343 — Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
- LC 1052 — Grumpy Bookstore Owner
- LC 2379 — Minimum Recolors to Get K Consecutive Black Blocks

---

## 13. Sliding Window | Variable size
**Target:** Expand and contract the window dynamically based on a condition (e.g., at most k distinct characters). Track validity with a hash map or counter.

**Problems:**
- LC 3 — Longest Substring Without Repeating Characters
- LC 424 — Longest Repeating Character Replacement
- LC 209 — Minimum Size Subarray Sum
- LC 904 — Fruit Into Baskets

---

## 14. Running State | Kadane / min-max tracking
**Target:** Track the best (or worst) subarray ending at each position. Extend the previous subarray or start fresh. Also applies to tracking running min/max.

**Problems:**
- LC 53 — Maximum Subarray (Kadane)
- LC 918 — Maximum Sum Circular Subarray
- LC 121 — Best Time to Buy and Sell Stock
- LC 152 — Maximum Product Subarray

---

## 15. Binary Search | Standard — find target
**Target:** Classic binary search on a sorted array. Reduce search space by half each iteration. Handle boundary conditions carefully.

**Problems:**
- LC 704 — Binary Search
- LC 35 — Search Insert Position
- LC 367 — Valid Perfect Square
- LC 441 — Arranging Coins

---

## 16. Binary Search | Lower bound — first position
**Target:** Find the first or last occurrence of a target, or the first element satisfying a predicate. Requires careful post-loop boundary checks.

**Problems:**
- LC 34 — Find First and Last Position of Element in Sorted Array
- LC 278 — First Bad Version
- LC 1539 — Kth Missing Positive Number
- LC 744 — Find Smallest Letter Greater Than Target

---

## 17. Binary Search | Applied — non-obvious structure
**Target:** Recognize monotonic predicates in unsorted-looking problems (e.g., capacity, minimum days, split array). Binary search on the answer.

**Problems:**
- LC 875 — Koko Eating Bananas
- LC 1011 — Capacity To Ship Packages Within D Days
- LC 410 — Split Array Largest Sum
- LC 153 — Find Minimum in Rotated Sorted Array

---

## 18. Hash Set | Sequence expansion
**Target:** Use a hash set for O(1) lookups to expand sequences (consecutive numbers, longest chain) or detect cycles in sequences.

**Problems:**
- LC 128 — Longest Consecutive Sequence
- LC 202 — Happy Number
- LC 136 — Single Number
- LC 349 — Intersection of Two Arrays
- LC 36 -- Valid Sudoku

---

## 19. Traversal + basic ops | Reverse a list
**Target:** Fundamental linked list traversal and pointer manipulation. Build intuition for iterative reversal and pointer rewiring.

**Problems:**
- LC 206 — Reverse Linked List
- LC 92 — Reverse Linked List II
- LC 2 — Add Two Numbers
- LC 83 - Remove Duplicates from Sorted List

---

## 20. Dummy node | Remove Nth / merge
**Target:** Use a dummy (sentinel) node to simplify edge cases where the head itself might be removed or merged. Reduces null checks.

**Problems:**
- LC 19 — Remove Nth Node From End of List
- LC 21 — Merge Two Sorted Lists
- LC 203 — Remove Linked List Elements
- LC 82 — Remove Duplicates from Sorted List II

---

## 21. Fast + slow pointer | Middle / cycle detection
**Target:** Two pointers moving at different speeds. Detect cycles (Floyd's) or find the middle node in a single pass with O(1) space.

**Problems:**
- LC 141 — Linked List Cycle
- LC 142 — Linked List Cycle II
- LC 876 — Middle of the Linked List
- LC 234 — Palindrome Linked List


---

## 22. In-place manipulation | Reorder / reverse groups
**Target:** Reorder or reverse segments of a linked list without allocating new nodes. Master pointer rewiring and segment reversal.

**Problems:**
- LC 25 — Reverse Nodes in k-Group
- LC 61 — Rotate List
- LC 86 — Partition List
- LC 328 — Odd Even Linked List
- LC 143 — Reorder List


---

## 23. Basic Stack | Valid parens / min stack
**Target:** Use a stack for LIFO operations: matching brackets, tracking minimums, or evaluating expressions. Core stack patterns.

**Problems:**
- LC 20 — Valid Parentheses
- LC 155 — Min Stack
- LC 150 — Evaluate Reverse Polish Notation
- LC 1047 — Remove All Adjacent Duplicates In String

---

## 24. Monotonic Stack | Next greater element
**Target:** Maintain a monotonically increasing or decreasing stack to find the next greater / smaller element for each position in O(n).

**Problems:**
- LC 496 — Next Greater Element I
- LC 503 — Next Greater Element II
- LC 739 — Daily Temperatures
- LC 84 — Largest Rectangle in Histogram
- LC 85 — Maximal Rectangle

---

## 25. Deque / Sliding Window Max | Window max
**Target:** Use a deque to maintain candidates in a sliding window, discarding elements that can never be the maximum. Achieve O(n) for window maximum.

**Problems:**
- LC 239 — Sliding Window Maximum
- LC 1438 — Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
- LC 862 — Shortest Subarray with Sum at Least K
- LC 1696 — Jump Game VI

---

## 26. Tree DFS | Depth / height
**Target:** Recursive DFS to compute tree properties like max depth, diameter, or balanced status. Post-order processing is key.

**Problems:**
- LC 104 — Maximum Depth of Binary Tree
- LC 111 — Minimum Depth of Binary Tree
- LC 543 — Diameter of Binary Tree
- LC 110 — Balanced Binary Tree

---

## 27. Tree DFS | Path sum / structure
**Target:** DFS to find paths with a target sum, count good nodes, or validate structural properties of the tree.

**Problems:**
- LC 112 — Path Sum
- LC 113 — Path Sum II
- LC 437 — Path Sum III
- LC 1448 — Count Good Nodes in Binary Tree

---

## 28. Tree DFS | Traversal (pre/in/post)
**Target:** Implement and apply the three classic DFS traversals. Use Morris traversal for O(1) space, or traversal patterns to rebuild trees.

**Problems:**
- LC 144 — Binary Tree Preorder Traversal
- LC 94 — Binary Tree Inorder Traversal
- LC 145 — Binary Tree Postorder Traversal
- LC 105 — Construct Binary Tree from Preorder and Inorder Traversal

---

## 29. Tree BFS | Level order
**Target:** Use a queue to process nodes level by level. Track level boundaries to group results or find the shortest path in an unweighted tree.

**Problems:**
- LC 102 — Binary Tree Level Order Traversal
- LC 107 — Binary Tree Level Order Traversal II
- LC 103 — Binary Tree Zigzag Level Order Traversal
- LC 199 — Binary Tree Right Side View

---

## 30. BST | Search / validate
**Target:** Leverage BST ordering property (left < root < right) for efficient search, insertion, and validation. Inorder traversal yields sorted order.

**Problems:**
- LC 700 — Search in a Binary Search Tree
- LC 98 — Validate Binary Search Tree
- LC 701 — Insert into a Binary Search Tree
- LC 230 — Kth Smallest Element in a BST

---

## 31. BST | LCA / operations
**Target:** Use BST properties to find the Lowest Common Ancestor efficiently, or perform range queries and conversions.

**Problems:**
- LC 235 — Lowest Common Ancestor of a Binary Search Tree
- LC 236 — Lowest Common Ancestor of a Binary Tree
- LC 538 — Convert BST to Greater Tree
- LC 108 — Convert Sorted Array to Binary Search Tree

---

## 32. Graph DFS | Components / flood fill
**Target:** DFS on graphs to explore connected components, detect cycles, or perform flood-fill on grids. Use a visited set or mutate input.

**Problems:**
- LC 200 — Number of Islands
- LC 695 — Max Area of Island
- LC 733 — Flood Fill
- LC 547 — Number of Provinces
- LC 1020 -- Number of Enclaves

---

## 33. Graph BFS | Shortest path
**Target:** BFS on unweighted graphs guarantees the shortest path in terms of edge count. Use a queue and track visited nodes / levels.

**Problems:**
- LC 127 — Word Ladder
- LC 433 — Minimum Genetic Mutation
- LC 994 — Rotting Oranges
- LC 1091 — Shortest Path in Binary Matrix

---

## 34. Grid traversal | Islands / surrounded
**Target:** Grid-specific DFS/BFS with direction arrays. Handle boundary conditions, connected components, and grid-specific mutations.

**Problems:**
- LC 463 — Island Perimeter
- LC 1905 — Count Sub Islands
- LC 1254 — Number of Closed Islands
- LC 417 — Pacific Atlantic Water Flow

---

## 35. Min/Max Heap | Top K / Kth largest
**Target:** Use a heap to maintain the top k elements or find the kth largest / smallest efficiently. Min-heap for top-k largest, max-heap for top-k smallest.

**Problems:**
- LC 215 — Kth Largest Element in an Array
- LC 703 — Kth Largest Element in a Stream
- LC 973 — K Closest Points to Origin
- LC 1046 — Last Stone Weight

---

## 36. Two Heaps | Median stream
**Target:** Maintain two heaps (max-heap for lower half, min-heap for upper half) to compute the running median in O(log n) per insertion.

**Problems:**
- LC 295 — Find Median from Data Stream
- LC 480 — Sliding Window Median
- LC 502 — IPO
- LC 1962 — Remove Stones to Minimize the Total

---

## 37. 1D DP | Fibonacci style
**Target:** Define state as dp[i] depending on a small fixed number of previous states (dp[i-1], dp[i-2]). Optimize space to O(1) if possible.

**Problems:**
- LC 70 — Climbing Stairs
- LC 198 — House Robber
- LC 213 — House Robber II
- LC 746 — Min Cost Climbing Stairs
- LC 91 — Decode Ways

---

## 38. 1D DP | Subsequence style
**Target:** dp[i] represents the best solution ending at index i. Compare dp[i] with all previous dp[j] (j < i) when necessary, or use patience sorting / binary search optimization.

**Problems:**
- LC 300 — Longest Increasing Subsequence
- LC 673 — Number of Longest Increasing Subsequence
- LC 1143 — Longest Common Subsequence
- LC 72 — Edit Distance
- LC 139 — Word Break
- LC 322 — Coin Change

---

## Summary Stats

| Metric | Value |
|--------|-------|
| Total Pattern → Variant Pairs | 38 |
| Total Problems | ~160+ |
| Difficulty Mix | Mostly Medium, Hard included only for unique patterns |
| Design Principle | One pattern per problem, no duplicates, classic interview focus |

## How to Use This Curriculum

1. **Work variant by variant.** Finish all problems under one variant before moving to the next.
2. **Start with the first problem** in each variant (usually the easiest) to internalize the pattern.
3. **Solve the last problem** in each variant (usually the hardest) to test mastery.
4. **Track your solves** in a spreadsheet with columns: Problem | Solved? | Time | Notes.
5. **Revisit** problems you struggled with after a 1-week gap.

---

*Curated for pattern mastery, not problem volume.*

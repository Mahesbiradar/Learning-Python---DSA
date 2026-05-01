# 16-Week DSA Roadmap

Goal: become interview-ready in DSA using Python through daily problem solving, pattern recognition, revision, and timed evaluation.

Daily time: 8-10 hours  
Weekly rhythm: 6 study/practice days + 1 test/revision day  
Main platforms: LeetCode, NeetCode 150 / Blind 75  
Local files to use: `CONCEPTS.md`, `PROBLEMS.md`, `REVISION_PROBLEMS.md`, `DSA_DAILY_EXECUTION_SYSTEM.md`, `DSA_PROGRESS_TRACKER.md`

## Non-Negotiable Rules

- No unnecessary theory.
- Every concept must connect to problems.
- Always write brute force before optimization.
- Always dry run before coding.
- Always write time and space complexity.
- Do not mark a problem complete after only watching or reading the solution.
- Move to the next topic only when the stop/continue rules allow it.

## Phase 1: Arrays + Hashing + Strings

Duration: Weeks 1-3

### Concepts

Arrays:
- Traversal, indexing, prefix/suffix logic.
- Frequency counting, in-place updates, sorting basics.
- Edge cases: empty list, duplicates, negatives, single element.

Hashing:
- Dictionary frequency map, set lookup, key existence.
- Counting pairs, grouping by key, duplicate detection.

Strings:
- Character traversal, frequency counting, palindrome basics.
- Anagram logic, string building, ASCII/lowercase assumptions, split/join.

### Patterns

- Linear scan
- Frequency map
- Prefix sum
- Set lookup
- Counting occurrences
- Grouping
- Sorting + comparison
- Character frequency
- Reverse traversal
- Index tracking

### Problems

Beginner:
- Contains Duplicate
- Valid Anagram
- Find Maximum / Minimum
- Second Largest Element
- Count Frequency of Elements
- Check if Array is Sorted
- Reverse Array
- Reverse String
- First Unique Character in a String
- Is Subsequence

Intermediate:
- Two Sum
- Group Anagrams
- Top K Frequent Elements
- Product of Array Except Self
- Longest Common Prefix
- Majority Element
- Missing Number
- Intersection of Two Arrays
- Encode and Decode Strings
- Valid Palindrome

Interview:
- Longest Consecutive Sequence
- Subarray Sum Equals K
- 3Sum
- Find All Anagrams in a String
- Minimum Window Substring
- First Missing Positive
- String Compression
- Roman to Integer
- Integer to Roman
- Valid Sudoku

Must-cover:
- Two Sum
- Contains Duplicate
- Valid Anagram
- Group Anagrams
- Top K Frequent Elements
- Product of Array Except Self
- Longest Consecutive Sequence
- Subarray Sum Equals K
- Valid Palindrome
- First Unique Character in a String

### Weekly Execution

Week 1:
- Day 1: Array traversal, max/min, count, reverse. Solve 10 problems.
- Day 2: Index tracking, second largest, sorted check, duplicates. Solve 10-12 problems.
- Day 3: Hash map frequency and set lookup. Solve 10-12 problems.
- Day 4: Two Sum, duplicates, grouping basics. Solve 8-10 problems.
- Day 5: Strings, palindrome, anagram, character count. Solve 10-12 problems.
- Day 6: Mixed arrays + hashing + strings revision. Re-solve failed problems.
- Day 7: Weekly test: 2 easy, 3 medium, 1 interview problem.

Week 2:
- Day 1: Prefix sum basics and running totals. Solve 8-10 problems.
- Day 2: Product except self, prefix/suffix arrays. Solve 8-10 problems.
- Day 3: Grouping problems: anagrams, buckets, frequency. Solve 8-10 problems.
- Day 4: Top K and majority logic. Solve 8-10 problems.
- Day 5: String compression, subsequence, common prefix. Solve 10 problems.
- Day 6: Must-cover reattempts from memory.
- Day 7: Weekly test and topic weakness review.

Week 3:
- Day 1: Longest consecutive, set expansion. Solve 7-9 problems.
- Day 2: Subarray sum equals K and prefix-hash. Solve 7-9 problems.
- Day 3: Valid Sudoku and matrix hashing. Solve 7-9 problems.
- Day 4: Interview mixed set. Solve 6-8 problems.
- Day 5: Timed arrays/hash/strings mock. Solve 6 problems.
- Day 6: Redo all must-cover misses.
- Day 7: Phase 1 test. Continue only if criteria are met.

## Phase 2: Two Pointer + Sliding Window

Duration: Weeks 4-5

### Concepts

Two Pointer:
- Left/right pointers, opposite direction pointers, same direction pointers.
- Sorted array usage, in-place movement, duplicate skipping.

Sliding Window:
- Fixed-size window, variable-size window, window expand/shrink.
- Frequency inside window, maximum/minimum window condition, substring/subarray window.

### Patterns

- Left/right shrinking
- Fast/slow pointer
- Fixed window sum/count
- Variable window with condition
- Window with hash map
- Window with set
- Duplicate skipping after sorting

### Problems

Beginner:
- Valid Palindrome
- Reverse String
- Merge Sorted Array
- Move Zeroes
- Remove Duplicates from Sorted Array
- Squares of a Sorted Array
- Best Time to Buy and Sell Stock
- Maximum Average Subarray I

Intermediate:
- Two Sum II
- Container With Most Water
- 3Sum
- Longest Substring Without Repeating Characters
- Longest Repeating Character Replacement
- Permutation in String
- Minimum Size Subarray Sum
- Max Consecutive Ones III

Interview:
- Trapping Rain Water
- Minimum Window Substring
- Sliding Window Maximum
- Subarrays with K Different Integers
- Fruit Into Baskets
- Longest Substring with At Most K Distinct Characters

Must-cover:
- Two Sum II
- 3Sum
- Container With Most Water
- Trapping Rain Water
- Longest Substring Without Repeating Characters
- Longest Repeating Character Replacement
- Permutation in String
- Minimum Window Substring

### Weekly Execution

Week 4:
- Day 1: Opposite direction two pointers. Solve 10 problems.
- Day 2: Same direction two pointers and in-place updates. Solve 10 problems.
- Day 3: Sorted arrays and duplicate skipping. Solve 8-10 problems.
- Day 4: 3Sum and container patterns. Solve 6-8 problems.
- Day 5: Trapping Rain Water and harder two-pointer cases. Solve 5-7 problems.
- Day 6: Re-solve missed two-pointer problems.
- Day 7: Weekly test.

Week 5:
- Day 1: Fixed-size sliding window. Solve 10 problems.
- Day 2: Variable-size sliding window with set/map. Solve 8-10 problems.
- Day 3: Window frequency problems. Solve 8-10 problems.
- Day 4: Minimum window and permutation logic. Solve 6-8 problems.
- Day 5: Timed mixed two-pointer/window set. Solve 6-8 problems.
- Day 6: Must-cover reattempts.
- Day 7: Phase 2 test.

## Phase 3: Stack + Queue + Recursion Depth

Duration: Weeks 6-7

### Concepts

Stack:
- LIFO, push/pop/top, monotonic stack.
- Matching brackets, previous/next greater element, expression evaluation.

Queue:
- FIFO, `collections.deque`, BFS preparation.
- Fixed-size queue, monotonic queue.

Recursion:
- Base case, recursive case, call stack.
- Backtracking foundation, recursion tree, avoiding infinite recursion.

### Patterns

- Parentheses matching
- Monotonic increasing stack
- Monotonic decreasing stack
- Next greater / previous greater
- Min stack design
- Queue simulation
- BFS queue structure
- Recursive decomposition

### Problems

Beginner:
- Valid Parentheses
- Implement Stack using Queues
- Implement Queue using Stacks
- Baseball Game
- Backspace String Compare
- Reverse String using Recursion
- Factorial
- Fibonacci
- Sum of Array Recursively

Intermediate:
- Min Stack
- Daily Temperatures
- Next Greater Element I
- Evaluate Reverse Polish Notation
- Generate Parentheses
- Decode String
- Asteroid Collision
- Simplify Path
- Number of Recent Calls

Interview:
- Largest Rectangle in Histogram
- Sliding Window Maximum
- Basic Calculator
- Remove K Digits
- Online Stock Span
- Car Fleet
- Next Greater Element II
- Subsets
- Permutations

Must-cover:
- Valid Parentheses
- Min Stack
- Daily Temperatures
- Evaluate Reverse Polish Notation
- Generate Parentheses
- Decode String
- Largest Rectangle in Histogram
- Sliding Window Maximum
- Subsets
- Permutations

### Weekly Execution

Week 6:
- Day 1: Basic stack and parentheses. Solve 10-12 problems.
- Day 2: Stack simulation and expression evaluation. Solve 8-10 problems.
- Day 3: Monotonic stack basics. Solve 8-10 problems.
- Day 4: Daily Temperatures, stock span, next greater. Solve 7-9 problems.
- Day 5: Largest rectangle and hard stack cases. Solve 5-7 problems.
- Day 6: Re-solve stack misses.
- Day 7: Weekly test.

Week 7:
- Day 1: Queue and deque usage. Solve 8-10 problems.
- Day 2: Monotonic queue and sliding max. Solve 6-8 problems.
- Day 3: Recursion basics and call stack. Solve 8-10 problems.
- Day 4: Subsets and permutations. Solve 6-8 problems.
- Day 5: Generate parentheses and recursion mixed set. Solve 6-8 problems.
- Day 6: Must-cover reattempts.
- Day 7: Phase 3 test.

## Phase 4: Linked List + Binary Search

Duration: Weeks 8-9

### Concepts

Linked List:
- Node structure, head pointer, traversal.
- Insert/delete basics, reversing links, slow/fast pointer.
- Dummy node, cycle detection.

Binary Search:
- Search space, mid calculation, left/right boundary.
- Exact search, lower bound / upper bound.
- Binary search on answer, sorted rotated arrays.

### Patterns

Linked List:
- Dummy node
- Fast/slow pointer
- Reverse links
- Merge lists
- Cycle detection
- Remove nth node
- Reorder list

Binary Search:
- Classic binary search
- First/last occurrence
- Search rotated sorted array
- Binary search on answer
- Matrix binary search

### Problems

Beginner:
- Reverse Linked List
- Merge Two Sorted Lists
- Linked List Cycle
- Middle of the Linked List
- Remove Duplicates from Sorted List
- Binary Search
- Search Insert Position
- Guess Number Higher or Lower
- First Bad Version

Intermediate:
- Remove Nth Node From End
- Reorder List
- Add Two Numbers
- Palindrome Linked List
- Intersection of Two Linked Lists
- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array
- Find First and Last Position
- Search a 2D Matrix
- Koko Eating Bananas

Interview:
- Merge K Sorted Lists
- Reverse Nodes in K Group
- Copy List with Random Pointer
- LRU Cache
- Median of Two Sorted Arrays
- Split Array Largest Sum
- Capacity to Ship Packages
- Time Based Key-Value Store

Must-cover:
- Reverse Linked List
- Merge Two Sorted Lists
- Linked List Cycle
- Remove Nth Node From End
- Reorder List
- Merge K Sorted Lists
- Binary Search
- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array
- Koko Eating Bananas

### Weekly Execution

Week 8:
- Day 1: Linked list node/traversal/reversal. Solve 8-10 problems.
- Day 2: Dummy node and deletion problems. Solve 8-10 problems.
- Day 3: Slow/fast pointer and cycle problems. Solve 8-10 problems.
- Day 4: Merge/reorder linked lists. Solve 6-8 problems.
- Day 5: Merge K and interview linked list set. Solve 5-7 problems.
- Day 6: Re-solve linked list misses.
- Day 7: Weekly test.

Week 9:
- Day 1: Classic binary search. Solve 10-12 problems.
- Day 2: Boundaries and first/last occurrence. Solve 8-10 problems.
- Day 3: Rotated sorted arrays. Solve 8-10 problems.
- Day 4: Matrix and answer-space binary search. Solve 6-8 problems.
- Day 5: Koko/shipping/split array style problems. Solve 5-7 problems.
- Day 6: Must-cover reattempts.
- Day 7: Phase 4 test.

## Phase 5: Trees + Graph Basics

Duration: Weeks 10-12

### Concepts

Trees:
- Binary tree node, DFS preorder/inorder/postorder.
- BFS level order, height/depth, balanced tree.
- BST property, lowest common ancestor, tree recursion.

Graphs:
- Adjacency list, visited set, BFS, DFS.
- Connected components, cycle basics, grid traversal, topological sort basics.

### Patterns

Trees:
- Recursive DFS
- Iterative BFS
- Level order traversal
- Tree height/depth
- Path sum
- BST validation
- LCA
- Build tree from traversal

Graphs:
- BFS from source
- DFS connected components
- Matrix/grid DFS
- Multi-source BFS
- Cycle detection
- Topological sorting
- Union-find basics

### Problems

Beginner:
- Maximum Depth of Binary Tree
- Invert Binary Tree
- Same Tree
- Subtree of Another Tree
- Binary Tree Level Order Traversal
- Diameter of Binary Tree
- Balanced Binary Tree
- Search in a BST
- Flood Fill
- Number of Islands

Intermediate:
- Validate Binary Search Tree
- Lowest Common Ancestor of BST
- Binary Tree Right Side View
- Path Sum II
- Kth Smallest Element in BST
- Construct Binary Tree from Preorder and Inorder
- Clone Graph
- Rotting Oranges
- Pacific Atlantic Water Flow
- Course Schedule

Interview:
- Serialize and Deserialize Binary Tree
- Binary Tree Maximum Path Sum
- Word Ladder
- Graph Valid Tree
- Number of Connected Components
- Redundant Connection
- Alien Dictionary
- Course Schedule II
- Walls and Gates
- Network Delay Time

Must-cover:
- Maximum Depth of Binary Tree
- Invert Binary Tree
- Diameter of Binary Tree
- Binary Tree Level Order Traversal
- Validate Binary Search Tree
- Lowest Common Ancestor
- Number of Islands
- Clone Graph
- Rotting Oranges
- Course Schedule

### Weekly Execution

Week 10:
- Day 1: Tree DFS basics. Solve 8-10 problems.
- Day 2: Tree BFS/level order. Solve 8-10 problems.
- Day 3: Height, diameter, balanced tree. Solve 8-10 problems.
- Day 4: BST validation/search/LCA. Solve 7-9 problems.
- Day 5: Tree construction and harder recursion. Solve 5-7 problems.
- Day 6: Re-solve tree misses.
- Day 7: Weekly test.

Week 11:
- Day 1: Graph representation and DFS. Solve 8-10 problems.
- Day 2: BFS basics and visited set. Solve 8-10 problems.
- Day 3: Grid DFS/BFS. Solve 8-10 problems.
- Day 4: Multi-source BFS. Solve 6-8 problems.
- Day 5: Clone graph and connected components. Solve 6-8 problems.
- Day 6: Graph revision.
- Day 7: Weekly test.

Week 12:
- Day 1: Cycle detection basics. Solve 7-9 problems.
- Day 2: Course Schedule and topological sort. Solve 6-8 problems.
- Day 3: Union-find basics. Solve 6-8 problems.
- Day 4: Mixed trees + graphs interview set. Solve 6-8 problems.
- Day 5: Timed mock. Solve 5-6 problems.
- Day 6: Must-cover reattempts.
- Day 7: Phase 5 test.

## Phase 6: Dynamic Programming + Greedy

Duration: Weeks 13-16

### Concepts

Dynamic Programming:
- Overlapping subproblems, optimal substructure.
- Memoization, tabulation, 1D DP, 2D DP.
- State definition, transition, base cases.

Greedy:
- Local optimal choice, sorting by rule, interval decisions.
- Heap-assisted greedy basics, when greedy fails.

### Patterns

DP:
- Fibonacci-style DP
- House robber pattern
- Coin change pattern
- Grid DP
- Subsequence DP
- Knapsack-style choices
- Palindrome DP
- Partition DP basics

Greedy:
- Interval scheduling
- Jump reachability
- Sort by start/end
- Merge intervals
- Choose minimum/maximum needed
- Heap for ongoing choices

### Problems

Beginner:
- Climbing Stairs
- Min Cost Climbing Stairs
- House Robber
- Maximum Subarray
- Best Time to Buy and Sell Stock
- Can Jump
- Merge Intervals
- Insert Interval
- Assign Cookies

Intermediate:
- Coin Change
- Longest Increasing Subsequence
- Word Break
- Unique Paths
- Decode Ways
- Partition Equal Subset Sum
- House Robber II
- Jump Game II
- Non-overlapping Intervals
- Gas Station

Interview:
- Longest Common Subsequence
- Edit Distance
- Palindromic Substrings
- Longest Palindromic Subsequence
- Maximum Product Subarray
- Burst Balloons
- Regular Expression Matching
- Meeting Rooms II
- Task Scheduler
- Minimum Number of Arrows to Burst Balloons

Must-cover:
- Climbing Stairs
- House Robber
- Coin Change
- Longest Increasing Subsequence
- Word Break
- Unique Paths
- Partition Equal Subset Sum
- Longest Common Subsequence
- Merge Intervals
- Jump Game

### Weekly Execution

Week 13:
- Day 1: DP thinking, recursion to memoization. Solve 6-8 problems.
- Day 2: 1D DP: climbing stairs, min cost. Solve 8-10 problems.
- Day 3: House robber and maximum subarray patterns. Solve 7-9 problems.
- Day 4: Coin change basics. Solve 6-8 problems.
- Day 5: Word Break and Decode Ways. Solve 5-7 problems.
- Day 6: Re-solve DP misses.
- Day 7: Weekly test.

Week 14:
- Day 1: Grid DP. Solve 7-9 problems.
- Day 2: LIS pattern. Solve 6-8 problems.
- Day 3: Partition/knapsack basics. Solve 6-8 problems.
- Day 4: LCS and subsequence DP. Solve 5-7 problems.
- Day 5: Palindrome DP. Solve 5-7 problems.
- Day 6: DP must-cover revision.
- Day 7: Weekly test.

Week 15:
- Day 1: Greedy basics and sorting decisions. Solve 8-10 problems.
- Day 2: Intervals: merge/insert/non-overlap. Solve 8-10 problems.
- Day 3: Jump Game and reachability. Solve 7-9 problems.
- Day 4: Heap-assisted greedy. Solve 6-8 problems.
- Day 5: Greedy mixed interview set. Solve 6-8 problems.
- Day 6: Re-solve greedy misses.
- Day 7: Weekly test.

Week 16:
- Day 1: Mixed DP revision. Solve 6-8 problems.
- Day 2: Mixed greedy revision. Solve 6-8 problems.
- Day 3: Full mixed DSA mock 1. Solve 5-6 timed problems.
- Day 4: Full mixed DSA mock 2. Solve 5-6 timed problems.
- Day 5: Re-solve all failed must-cover problems.
- Day 6: Final interview simulation. Solve 6 timed problems.
- Day 7: Final review and next-cycle planning.

## End Of Topic Criteria

A topic is complete only when all are true:

- You solved at least 70-80% of medium problems without full solution help.
- You can identify the pattern within 5 minutes for most unseen problems.
- You can explain brute force and optimized approach clearly.
- You can dry run the optimized solution.
- You can write time and space complexity correctly.
- You can re-solve must-cover problems from memory.
- In a timed set of 5 unseen problems:
  - Easy: 10-15 minutes.
  - Medium: 25-40 minutes.
  - Hard/interview: meaningful progress in 45-60 minutes.

## Stop / Continue Rules

Continue to next topic when:
- Must-cover problems are complete.
- 70-80% of mixed medium problems are solved independently.
- Main patterns can be explained without notes.
- Weekly test is passed.

Repeat topic when:
- Pattern recognition is weak.
- Full solutions are needed for more than 40% of problems.
- Must-cover problems fail repeatedly.
- Time and space complexity cannot be explained.

Slow down when:
- You are memorizing solutions.
- You skip brute force.
- You cannot dry run your code.
- Implementation mistakes repeat.
- Speed improves but understanding weakens.

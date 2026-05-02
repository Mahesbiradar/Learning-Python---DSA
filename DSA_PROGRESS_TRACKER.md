# DSA Progress Tracker

Start date: 2026-05-01  
Plan length: 16 weeks  
Daily study target: 8-10 hours  
Weekly target: 55-75 attempted problems

## Master Progress

| Phase | Weeks | Topic | Status | Must-Cover Done | Phase Test |
| --- | ---: | --- | --- | ---: | --- |
| 1 | 1-3 | Arrays + Hashing + Strings | In progress | 0/10 | Not taken |
| 2 | 4-5 | Two Pointer + Sliding Window | Not started | 0/8 | Not taken |
| 3 | 6-7 | Stack + Queue + Recursion | Not started | 0/10 | Not taken |
| 4 | 8-9 | Linked List + Binary Search | Not started | 0/10 | Not taken |
| 5 | 10-12 | Trees + Graph Basics | Not started | 0/10 | Not taken |
| 6 | 13-16 | Dynamic Programming + Greedy | Not started | 0/10 | Not taken |

## Weekly Scoreboard

| Week | Topic Focus | Attempted | Independent | Hint | Solution | Accuracy | Decision |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Array basics + hashing + strings | 10 | 9 | 1 | 0 | 90% | Continue to Day 2 after fixing notes |
| 2 | Prefix/suffix + grouping + frequency | 0 | 0 | 0 | 0 | 0% | Pending |
| 3 | Interview arrays/hash/strings | 0 | 0 | 0 | 0 | 0% | Pending |
| 4 | Two pointers | 0 | 0 | 0 | 0 | 0% | Pending |
| 5 | Sliding window | 0 | 0 | 0 | 0 | 0% | Pending |
| 6 | Stack | 0 | 0 | 0 | 0 | 0% | Pending |
| 7 | Queue + recursion | 0 | 0 | 0 | 0 | 0% | Pending |
| 8 | Linked list | 0 | 0 | 0 | 0 | 0% | Pending |
| 9 | Binary search | 0 | 0 | 0 | 0 | 0% | Pending |
| 10 | Trees | 0 | 0 | 0 | 0 | 0% | Pending |
| 11 | Graph basics | 0 | 0 | 0 | 0 | 0% | Pending |
| 12 | Graph interview basics | 0 | 0 | 0 | 0 | 0% | Pending |
| 13 | DP basics | 0 | 0 | 0 | 0 | 0% | Pending |
| 14 | DP intermediate | 0 | 0 | 0 | 0 | 0% | Pending |
| 15 | Greedy | 0 | 0 | 0 | 0 | 0% | Pending |
| 16 | Final mixed revision | 0 | 0 | 0 | 0 | 0% | Pending |

## Daily Logs

### 2026-05-02

Week / Day: Week 1 / Day 1  
Phase: Phase 1 - Arrays + Hashing + Strings  
Topic: Array traversal, tracking, adjacent comparison, in-place update, basic frequency map

Concept studied:
- List traversal
- Manual sum/count tracking
- Max/min tracking
- Reverse using extra list and two pointers
- Adjacent comparison for sorted check
- Position tracking for moving zeroes
- Dictionary frequency for majority element

Problems attempted: 10  
Solved independently: 9  
Solved after hint: 1  
Solved after solution: 0  
Unsolved: 0

Problem list:
1. Print All Elements - correct
2. Sum Of List - correct
3. Count Even Numbers - correct
4. Find Maximum Element - correct
5. Find Minimum Element - correct
6. Reverse Array - correct, but rename duplicate function versions
7. Check If Array Is Sorted - correct
8. Second Largest Distinct Element - correct after edge-case hint
9. Move Zeroes To End - correct
10. Majority Element - correct with dictionary; Boyer-Moore still pending

Main mistakes:
- Used `print(print_element(nums))` initially, causing an extra `None`; fixed by calling the function directly.
- Second largest needed explicit handling for lists with fewer than 2 items and all-duplicate values.
- Forgot to increment the position pointer while moving zeroes, then corrected it.
- Reverse array extra-list space was written as `O(2)`; correct space is `O(n)`.
- Majority element dictionary approach uses `O(n)` extra space, not `O(1)`.
- Boyer-Moore voting approach is not learned yet.

Patterns recognized:
- Linear traversal
- Tracking variable
- Adjacent comparison
- Two-pointer reverse
- Position tracking
- Dictionary frequency map

Brute force written for all problems? yes  
Dry runs completed? yes  
Complexities written? yes, with corrections needed for reverse extra-list and majority element  

Continue / repeat / slow down: Continue  
Reason: Strong Day 1 accuracy. Revision completed before Day 2. Boyer-Moore candidate logic is now understood and implemented; validation pass was learned with help.

Revision completed:
- Second Largest Distinct Element re-solved, with one remaining edge-case note: check `len(nums) < 2` before reading `nums[0]`.
- Move Zeroes To End re-solved correctly using a write pointer.
- Majority Element re-solved correctly using a dictionary frequency map.
- Boyer-Moore implemented with candidate selection and validation.

Next task file:
- `DAY_02_PROBLEMS.md`

## Must-Cover Tracker

### Phase 1: Arrays + Hashing + Strings

| Problem | Status | Last Attempt | Revisit |
| --- | --- | --- | --- |
| Two Sum | Not started |  |  |
| Contains Duplicate | Not started |  |  |
| Valid Anagram | Not started |  |  |
| Group Anagrams | Not started |  |  |
| Top K Frequent Elements | Not started |  |  |
| Product of Array Except Self | Not started |  |  |
| Longest Consecutive Sequence | Not started |  |  |
| Subarray Sum Equals K | Not started |  |  |
| Valid Palindrome | Not started |  |  |
| First Unique Character in a String | Not started |  |  |

Day 1 foundation problems completed:
- Print All Elements
- Sum Of List
- Count Even Numbers
- Find Maximum Element
- Find Minimum Element
- Reverse Array
- Check If Array Is Sorted
- Second Largest Distinct Element
- Move Zeroes To End
- Majority Element

### Phase 2: Two Pointer + Sliding Window

| Problem | Status | Last Attempt | Revisit |
| --- | --- | --- | --- |
| Two Sum II | Not started |  |  |
| 3Sum | Not started |  |  |
| Container With Most Water | Not started |  |  |
| Trapping Rain Water | Not started |  |  |
| Longest Substring Without Repeating Characters | Not started |  |  |
| Longest Repeating Character Replacement | Not started |  |  |
| Permutation in String | Not started |  |  |
| Minimum Window Substring | Not started |  |  |

### Phase 3: Stack + Queue + Recursion

| Problem | Status | Last Attempt | Revisit |
| --- | --- | --- | --- |
| Valid Parentheses | Not started |  |  |
| Min Stack | Not started |  |  |
| Daily Temperatures | Not started |  |  |
| Evaluate Reverse Polish Notation | Not started |  |  |
| Generate Parentheses | Not started |  |  |
| Decode String | Not started |  |  |
| Largest Rectangle in Histogram | Not started |  |  |
| Sliding Window Maximum | Not started |  |  |
| Subsets | Not started |  |  |
| Permutations | Not started |  |  |

### Phase 4: Linked List + Binary Search

| Problem | Status | Last Attempt | Revisit |
| --- | --- | --- | --- |
| Reverse Linked List | Not started |  |  |
| Merge Two Sorted Lists | Not started |  |  |
| Linked List Cycle | Not started |  |  |
| Remove Nth Node From End | Not started |  |  |
| Reorder List | Not started |  |  |
| Merge K Sorted Lists | Not started |  |  |
| Binary Search | Not started |  |  |
| Search in Rotated Sorted Array | Not started |  |  |
| Find Minimum in Rotated Sorted Array | Not started |  |  |
| Koko Eating Bananas | Not started |  |  |

### Phase 5: Trees + Graph Basics

| Problem | Status | Last Attempt | Revisit |
| --- | --- | --- | --- |
| Maximum Depth of Binary Tree | Not started |  |  |
| Invert Binary Tree | Not started |  |  |
| Diameter of Binary Tree | Not started |  |  |
| Binary Tree Level Order Traversal | Not started |  |  |
| Validate Binary Search Tree | Not started |  |  |
| Lowest Common Ancestor | Not started |  |  |
| Number of Islands | Not started |  |  |
| Clone Graph | Not started |  |  |
| Rotting Oranges | Not started |  |  |
| Course Schedule | Not started |  |  |

### Phase 6: Dynamic Programming + Greedy

| Problem | Status | Last Attempt | Revisit |
| --- | --- | --- | --- |
| Climbing Stairs | Not started |  |  |
| House Robber | Not started |  |  |
| Coin Change | Not started |  |  |
| Longest Increasing Subsequence | Not started |  |  |
| Word Break | Not started |  |  |
| Unique Paths | Not started |  |  |
| Partition Equal Subset Sum | Not started |  |  |
| Longest Common Subsequence | Not started |  |  |
| Merge Intervals | Not started |  |  |
| Jump Game | Not started |  |  |

## Failed Problem Queue

Use this table whenever a problem needs revision.

| Problem | Topic | Mistake Type | Failed Count | Next Revisit | Notes |
| --- | --- | --- | ---: | --- | --- |
| Second Largest Distinct Element | Arrays / Tracking | Edge cases: length < 2 and all duplicates | 1 | Completed 2026-05-02 | Re-solved; move the length check before `nums[0]` to handle `[]` safely |
| Reverse Array | Arrays / Two Pointer | Complexity note: extra-list version is O(n) space | 1 | 2026-05-03 | Keep separate names for extra-list and in-place functions |
| Majority Element | Hashing / Voting | Optimization not known: Boyer-Moore pending; dict space is O(n) | 1 | Completed 2026-05-02 | Dictionary version re-solved; Boyer-Moore candidate logic implemented, validation learned with help |

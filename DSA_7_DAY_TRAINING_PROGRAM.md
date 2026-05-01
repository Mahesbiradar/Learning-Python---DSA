# 7-Day DSA Training Program

Goal: move from basic problem solving to structured DSA thinking using Python, functions, dictionaries, hashing, and interview-style explanations.

Daily study time: 8-10 hours  
Daily practice target: 12-18 problems  
Main files: `CONCEPTS.md`, `PROBLEMS.md`, `REVISION_PROBLEMS.md`  
Main platforms: LeetCode, HackerRank, NeetCode  

---

## Daily Rules

Use this structure every day.

| Block | Time | Work |
| --- | ---: | --- |
| Learn | 1.5-2 hr | Watch/read only the required topic |
| Guided coding | 2 hr | Rebuild known solutions as clean functions |
| Independent solving | 3-4 hr | Solve new/revision problems without notes |
| Review and rewrite | 1 hr | Rewrite failed/ugly solutions cleanly |
| Complexity notes | 30-45 min | Write time and space for every problem |
| Revision | 30-45 min | Redo missed problems from memory |

For every problem, write this:

```text
Problem:
Pattern:
Brute force idea:
Optimized idea:
Code:
Time:
Space:
Mistake:
```

Rules:
- First make it work.
- Then make it clean.
- Then optimize.
- Always write time and space complexity.
- If stuck for 20-35 minutes, write brute force first.
- Never end a day with an unresolved mistake. At least write what confused you.

---

## Day 1: Functions + Complexity + Array Discipline

### Learning Topics

- Function syntax and reusable solutions
- Return vs print
- Parameters and test cases
- Time complexity: `O(1)`, `O(n)`, `O(n^2)`
- Space complexity: `O(1)` vs `O(n)`
- Array patterns: traversal, tracking, adjacent comparison, shifting

### Resources

- YouTube: CodeWithHarry Python functions section from his Python playlist.
- Udemy: Scott Barrett, Python Data Structures & Algorithms + LEETCODE Exercises - Big O / Lists / Arrays sections.
- Local: `CONCEPTS.md` sections: Functions, Time Complexity, Space Complexity, Arrays / Lists.

### Practice Tasks

- [ ] Rewrite 8 old array solutions as functions.
- [ ] Each function must return the answer instead of printing.
- [ ] Add 3 manual test cases per function:
  - normal case
  - edge case
  - duplicate or negative case where relevant

### Problems

Solve 14 problems.

| Done | Problem | Pattern | Source |
| --- | --- | --- | --- |
| [ ] | Find Maximum Element | Linear Traversal | `PROBLEMS.md` |
| [ ] | Find Minimum Element | Linear Traversal | `PROBLEMS.md` |
| [ ] | Count Even Numbers | Counting | `PROBLEMS.md` |
| [ ] | Sum of List | Accumulation | `PROBLEMS.md` |
| [ ] | Search Element | Linear Search | `PROBLEMS.md` |
| [ ] | First Odd Number | Linear Search | `PROBLEMS.md` |
| [ ] | Check All Even | Loop Else / Traversal | `PROBLEMS.md` |
| [ ] | Reverse Array | Two Pointer | `PROBLEMS.md` |
| [ ] | Left Rotate Array by 1 | Element Shifting | `PROBLEMS.md` |
| [ ] | Move Zeros to End | Position Tracking | `REVISION_PROBLEMS.md` |
| [ ] | Check Palindrome Array | Two Pointer | `PROBLEMS.md` |
| [ ] | Find Second Largest Distinct Element | Tracking | `REVISION_PROBLEMS.md` |
| [ ] | Check if List is Sorted | Adjacent Comparison | `REVISION_PROBLEMS.md` |
| [ ] | Matrix Row Sum | Nested Traversal | `REVISION_PROBLEMS.md` |

### Revision Tasks

- [ ] Solve `REV-ARR-001` to `REV-ARR-008`.
- [ ] Write time and space complexity for all 8 revision problems.
- [ ] Rewrite every failed problem once without looking.

### End-of-Day Output

By the end of Day 1, you should be able to:

- Convert scratch code into clean functions.
- Explain why a loop is `O(n)` and nested loops are `O(n^2)`.
- Solve basic array problems without confusion around indexes.

### Day 1 Completion

| Metric | Target | Actual |
| --- | ---: | ---: |
| Problems attempted | 14 | |
| Problems solved without help | 10+ | |
| Clean function rewrites | 8 | |
| Complexity notes written | 14 | |
| Failed problems rewritten | all failed | |

---

## Day 2: Dictionary Deep Dive

### Learning Topics

- Dictionary creation, access, update, delete
- `in`, `get`, `items`, `keys`, `values`
- Frequency dictionaries
- Index maps
- Difference between set and dictionary
- When dictionary beats nested loops

### Resources

- YouTube: CodeWithHarry, Dictionaries in Python - Day 33.
- Python reference:
  - W3Schools `dict.items()`
  - W3Schools `dict.pop()`
- Udemy: Scott Barrett dictionary/hash table intro if available.
- Local: `CONCEPTS.md` sections: Dictionaries, Hashing.

### Practice Tasks

Write these 8 functions.

| Done | Function | Expected Skill |
| --- | --- | --- |
| [ ] | `count_number_frequency(nums)` | frequency dict |
| [ ] | `count_character_frequency(text)` | character counting |
| [ ] | `first_repeated_character(text)` | seen set |
| [ ] | `first_non_repeating_character(text)` | frequency + order |
| [ ] | `pairs_to_dict(pairs)` | tuple/list to dict |
| [ ] | `max_frequency_element(nums)` | dictionary scan |
| [ ] | `same_frequency(a, b)` | compare dictionaries |
| [ ] | rewrite one frequency function using `get()` | clean dict usage |

### Problems

Solve 15 problems.

| Done | Problem | Pattern | Source |
| --- | --- | --- | --- |
| [ ] | Count Frequencies Using Dictionary | Frequency Dictionary | `PROBLEMS.md` |
| [ ] | Count Characters | Frequency Dictionary | `PROBLEMS.md` |
| [ ] | Character With Maximum Frequency | Frequency Dictionary | `PROBLEMS.md` |
| [ ] | First Repeating Character | Hashing | `PROBLEMS.md` |
| [ ] | First Non-Repeating Character | Frequency Dictionary | `PROBLEMS.md` |
| [ ] | First Non-Repeating Element | Frequency Dictionary | `PROBLEMS.md` |
| [ ] | Count Frequency of Element | Linear Traversal | `PROBLEMS.md` |
| [ ] | Valid Anagram | Frequency Dictionary | LeetCode |
| [ ] | Check Duplicate Exists | Set / Hashing | `REVISION_PROBLEMS.md` |
| [ ] | Remove Duplicates Using Set | Set | `PROBLEMS.md` |
| [ ] | Find Common Elements Optimized | Set Lookup | `REVISION_PROBLEMS.md` |
| [ ] | Find Missing Number Optimized | Set Difference | `REVISION_PROBLEMS.md` |
| [ ] | Two Sum | Dictionary Index Map | `PROBLEMS.md` / LeetCode |
| [ ] | Majority Element | Frequency Dictionary | LeetCode |
| [ ] | Single Number | Frequency or XOR intro | LeetCode |

### Revision Tasks

- [ ] Solve `REV-HASH-001` to `REV-HASH-005`.
- [ ] Redo `REV-STR-004` First Repeating Character.
- [ ] Redo `REV-STR-005` First Non-Repeating Character.
- [ ] Write a one-page note: “When to use dictionary”.

### End-of-Day Output

By the end of Day 2, you should be able to:

- Build frequency dictionaries confidently.
- Use dictionaries to replace nested loops.
- Know when to use `set` vs `dict`.

### Day 2 Completion

| Metric | Target | Actual |
| --- | ---: | ---: |
| Problems attempted | 15 | |
| Problems solved without help | 10+ | |
| Dictionary helper functions | 8 | |
| Complexity notes written | 15 | |
| Dictionary note completed | yes | |

---

## Day 3: Hashing Patterns for Optimization

### Learning Topics

- Brute force to optimized thinking
- Duplicate detection using set
- Complement lookup using dictionary
- Frequency count using dictionary
- Grouping using dictionary
- Hashing tradeoff: faster time, extra space

### Resources

- YouTube: Apna College, Two Sum / Find Duplicate / Repeating & Missing Values - Hashing Problems.
- NeetCode:
  - Two Sum
  - Intersection of Two Arrays
  - Group Anagrams
- Practice platform: LeetCode Arrays & Hashing.

### Practice Tasks

For 6 problems, write both brute force and optimized hashing solutions.

| Done | Problem | Brute Time | Optimized Time | Extra Space | Pattern |
| --- | --- | --- | --- | --- | --- |
| [ ] | Two Sum | O(n^2) | O(n) | O(n) | Index Map |
| [ ] | Contains Duplicate | O(n^2) | O(n) | O(n) | Seen Set |
| [ ] | Valid Anagram | O(n^2) or sort | O(n) | O(n) | Frequency |
| [ ] | First Non-Repeating Element | O(n^2) | O(n) | O(n) | Frequency |
| [ ] | Intersection of Two Arrays | O(n*m) | O(n+m) | O(m) | Set Lookup |
| [ ] | Missing Number | O(n^2) | O(n) | O(n) | Set Difference |

### Problems

Solve 16 problems.

| Done | Problem | Pattern | Source |
| --- | --- | --- | --- |
| [ ] | Contains Duplicate | Seen Set | LeetCode |
| [ ] | Find First Duplicate | Seen Set | Local |
| [ ] | Find All Duplicates | Set / Tracking | Local |
| [ ] | Two Sum | Dictionary Index Map | LeetCode |
| [ ] | Find Pair With Given Sum | Set / Nested Loop | Local |
| [ ] | Intersection of Two Arrays | Set Lookup | LeetCode |
| [ ] | Common Elements preserving order | Set Lookup | Local |
| [ ] | Missing Number | Set / Sum | LeetCode |
| [ ] | Repeating and Missing Number | Frequency Dictionary | LeetCode GFG |
| [ ] | First Non-Repeating Element | Frequency Dictionary | Local |
| [ ] | First Repeating Character | Seen Set | Local |
| [ ] | Valid Anagram | Frequency Dictionary | LeetCode |
| [ ] | Group Anagrams | Dictionary Grouping | LeetCode |
| [ ] | Top K Frequent Elements | Frequency Dictionary | LeetCode |
| [ ] | Count Distinct Elements | Set | Local |
| [ ] | Count Distinct Elements in Every Window | Window + Frequency | GFG/LeetCode style |

### Revision Tasks

- [ ] Redo Two Sum with nested loop.
- [ ] Redo Two Sum with two-pass dictionary.
- [ ] Redo Two Sum with one-pass dictionary.
- [ ] Redo Valid Anagram with dictionary.
- [ ] Redo Valid Anagram with fixed 26-size count list.

### End-of-Day Output

By the end of Day 3, you should be able to:

- See a nested-loop problem and ask, “Can hashing reduce this?”
- Use dictionary for frequency and index lookup.
- Explain `O(n^2)` to `O(n)` optimization clearly.

### Day 3 Completion

| Metric | Target | Actual |
| --- | ---: | ---: |
| Problems attempted | 16 | |
| Brute + optimized pairs | 6 | |
| Hashing problems solved cleanly | 10+ | |
| Complexity comparisons written | 6 | |

---

## Day 4: Strings + Dictionary Thinking

### Learning Topics

- String traversal by value and index
- String building
- Character frequency
- Word-level parsing
- Anagram patterns
- Manual substring checking
- Clean edge-case handling

### Resources

- NeetCode: Group Anagrams.
- LeetCode:
  - Valid Anagram
  - First Unique Character in a String
  - Group Anagrams
- Local: `PROBLEMS.md` Strings section and `REVISION_PROBLEMS.md` string section.

### Practice Tasks

For every string problem:

- [ ] First solve manually.
- [ ] Then write a cleaner function.
- [ ] Add edge cases:
  - empty string
  - one character
  - repeated characters
  - spaces
  - case sensitivity if relevant

### Problems

Solve 16 problems.

| Done | Problem | Pattern | Source |
| --- | --- | --- | --- |
| [ ] | Print Characters | Traversal | `PROBLEMS.md` |
| [ ] | Count Vowels | Traversal / Set Lookup | `PROBLEMS.md` |
| [ ] | Reverse String without slicing | Reverse Traversal | `PROBLEMS.md` |
| [ ] | Check Palindrome without slicing | Two Pointer | `REVISION_PROBLEMS.md` |
| [ ] | Remove Spaces | String Building | `PROBLEMS.md` |
| [ ] | Count Words Robust | Index Traversal | `REVISION_PROBLEMS.md` |
| [ ] | Count Words Starting With A | Traversal | `PROBLEMS.md` |
| [ ] | Remove Duplicates From String | Seen Set | `PROBLEMS.md` |
| [ ] | Remove Consecutive Duplicates | Adjacent Comparison | `REVISION_PROBLEMS.md` |
| [ ] | First Repeating Character | Seen Set | `REVISION_PROBLEMS.md` |
| [ ] | First Non-Repeating Character | Frequency Dictionary | `REVISION_PROBLEMS.md` |
| [ ] | Count Characters | Frequency Dictionary | `PROBLEMS.md` |
| [ ] | Character With Maximum Frequency | Frequency Dictionary | `PROBLEMS.md` |
| [ ] | Check Anagram | Frequency Dictionary | `REVISION_PROBLEMS.md` |
| [ ] | Check Substring Manually | Nested Loops | `REVISION_PROBLEMS.md` |
| [ ] | String Compression | Counting / String Building | `REVISION_PROBLEMS.md` |

### Revision Tasks

- [ ] Solve `REV-STR-001` to `REV-STR-010`.
- [ ] For every failed problem, write the exact reason:
  - index issue
  - final group missed
  - wrong initialization
  - missing edge case

### End-of-Day Output

By the end of Day 4, you should be able to:

- Handle string problems without relying only on slicing or built-ins.
- Use frequency dictionaries for string problems.
- Recognize anagram, repeat, unique, and compression patterns.

### Day 4 Completion

| Metric | Target | Actual |
| --- | ---: | ---: |
| Problems attempted | 16 | |
| String functions rewritten | 10+ | |
| Edge-case tests added | 20+ | |
| Failed problems explained | all failed | |

---

## Day 5: Interview-Style Problem Solving

### Learning Topics

- How to explain a solution before coding
- How to start from brute force
- How to optimize using set/dict
- How to dry run out loud
- How to discuss time and space complexity
- Writing clean function names and variables

### Resources

- NeetCode Arrays & Hashing roadmap:
  - Contains Duplicate
  - Valid Anagram
  - Two Sum
  - Group Anagrams
  - Top K Frequent Elements
- LeetCode Easy + selected Medium.
- Udemy: Scott Barrett or Jackson Kailath DSA course sections on arrays, Big O, hash tables.

### Interview Flow

Use this for every problem:

```text
1. Clarify input/output.
2. Give brute force.
3. Identify pattern.
4. Optimize.
5. Code clean function.
6. Dry run.
7. State time and space.
```

### Problems

Solve 12-14 problems.

| Done | Problem | Pattern | Source |
| --- | --- | --- | --- |
| [ ] | Contains Duplicate | Seen Set | LeetCode |
| [ ] | Valid Anagram | Frequency Dictionary | LeetCode |
| [ ] | Two Sum | Dictionary Index Map | LeetCode |
| [ ] | Group Anagrams | Dictionary Grouping | LeetCode |
| [ ] | Top K Frequent Elements | Frequency + Buckets/Sort | LeetCode |
| [ ] | Product of Array Except Self | Prefix/Postfix | LeetCode |
| [ ] | Longest Consecutive Sequence | Set Sequence | LeetCode |
| [ ] | Valid Palindrome | Two Pointer | LeetCode |
| [ ] | Two Sum II - sorted input | Two Pointer | LeetCode |
| [ ] | Best Time to Buy and Sell Stock | Sliding Window Intro | LeetCode |
| [ ] | Longest Substring Without Repeating Characters | Sliding Window + Set/Dict | LeetCode |
| [ ] | Isomorphic Strings | Dictionary Mapping | LeetCode |
| [ ] | Word Pattern | Dictionary Mapping | LeetCode |
| [ ] | Majority Element | Frequency / Boyer-Moore intro | LeetCode |

### Revision Tasks

- [ ] Pick 5 problems from Days 1-4 and explain them aloud as if in an interview.
- [ ] Write final clean versions for:
  - Two Sum
  - Valid Anagram
  - First Non-Repeating Character
  - Move Zeros
  - Second Largest

### End-of-Day Output

By the end of Day 5, you should be able to:

- Present a problem in interview format.
- Avoid jumping directly into code.
- Choose between loop, set, dictionary, and two pointers.

### Day 5 Completion

| Metric | Target | Actual |
| --- | ---: | ---: |
| Problems attempted | 12-14 | |
| Interview explanations spoken | 5+ | |
| Final clean rewrites | 5 | |
| Medium attempts | 4+ | |

---

## Day 6: Mixed Timed Practice + Weak Area Repair

### Learning Topics

- Pattern recognition under time pressure
- Debugging your own failed logic
- Re-solving without notes
- Optimizing after brute force works

### Resources

- Local: `REVISION_PROBLEMS.md`.
- HackerRank:
  - Dictionaries and Maps
  - Sales by Match
  - Counting Valleys only as warmup
- LeetCode:
  - Arrays
  - Strings
  - Hash Table tagged Easy/Medium

### Timed Blocks

| Done | Block | Time | Work |
| --- | --- | ---: | --- |
| [ ] | Block 1 | 90 min | 5 array problems |
| [ ] | Block 2 | 90 min | 5 string problems |
| [ ] | Block 3 | 90 min | 5 hashing problems |

Rules:
- Easy problem limit: 20 minutes.
- Medium problem limit: 35 minutes.
- If stuck, write brute force first.
- Only check solution after writing your own attempt.

### Problems

Solve 15-18 mixed problems.

| Done | Problem | Topic | Pattern |
| --- | --- | --- | --- |
| [ ] | Move Zeros | Arrays | Position Tracking |
| [ ] | Rotate Array by 1 or k | Arrays | Element Shifting / Reversal |
| [ ] | Monotonic Array | Arrays | Adjacent Comparison |
| [ ] | Second Largest | Arrays | Tracking |
| [ ] | Missing Number | Arrays | Hashing / Sum |
| [ ] | Valid Palindrome | Strings | Two Pointer |
| [ ] | Valid Anagram | Strings | Frequency Dictionary |
| [ ] | First Unique Character | Strings | Frequency Dictionary |
| [ ] | Longest Word | Strings | String Building |
| [ ] | String Compression | Strings | Counting |
| [ ] | Contains Duplicate | Hashing | Seen Set |
| [ ] | Two Sum | Hashing | Index Map |
| [ ] | Intersection of Two Arrays | Hashing | Set Lookup |
| [ ] | Group Anagrams | Hashing | Dictionary Grouping |
| [ ] | Top K Frequent Elements | Hashing | Frequency |
| [ ] | Longest Consecutive Sequence | Optional Medium | Set |
| [ ] | Longest Substring Without Repeating Characters | Optional Medium | Sliding Window |
| [ ] | Product of Array Except Self | Optional Medium | Prefix/Postfix |

### Mistake Log

Use this table today.

| Problem | Mistake | Correct Pattern | Correct Initialization | Complexity | Redone |
| --- | --- | --- | --- | --- | --- |
| | | | | | [ ] |
| | | | | | [ ] |
| | | | | | [ ] |
| | | | | | [ ] |
| | | | | | [ ] |

### End-of-Day Output

By the end of Day 6, you should be able to:

- Solve mixed easy problems faster.
- Identify traversal, two pointer, nested loop, hashing, or sliding window.
- Repair your own mistakes instead of only reading solutions.

### Day 6 Completion

| Metric | Target | Actual |
| --- | ---: | ---: |
| Timed blocks completed | 3 | |
| Problems attempted | 15-18 | |
| Mistakes logged | all failed | |
| Failed problems redone | all failed | |

---

## Day 7: Mock Interview Day + Final Consolidation

### Learning Topics

- Full interview simulation
- Clean code under pressure
- Explaining tradeoffs
- Final revision of dictionary, hashing, and complexity

### Resources

- NeetCode after attempts:
  - Two Sum
  - Intersection of Two Arrays
  - Group Anagrams
- LeetCode:
  - Easy Arrays & Hash Table
  - Easy Strings
  - 2-3 Medium Hashing problems
- Local:
  - `CONCEPTS.md`
  - `PROBLEMS.md`
  - `REVISION_PROBLEMS.md`

### Mock Interview Round 1

Time: 90 minutes

| Done | Problem | Pattern |
| --- | --- | --- |
| [ ] | Two Sum | Dictionary Index Map |
| [ ] | Valid Anagram | Frequency Dictionary |
| [ ] | Move Zeros | Position Tracking |
| [ ] | First Non-Repeating Character | Frequency Dictionary |

### Mock Interview Round 2

Time: 120 minutes

| Done | Problem | Pattern |
| --- | --- | --- |
| [ ] | Group Anagrams | Dictionary Grouping |
| [ ] | Top K Frequent Elements | Frequency |
| [ ] | Longest Substring Without Repeating Characters | Sliding Window |
| [ ] | Product of Array Except Self | Prefix/Postfix |

After each round:
- [ ] Rewrite code cleanly.
- [ ] Write brute force and optimized explanation.
- [ ] Write time and space complexity.
- [ ] Mark mistakes.

### Final Problems

Solve 10-12 final problems.

| Done | Problem | Pattern |
| --- | --- | --- |
| [ ] | Two Sum | Dictionary Index Map |
| [ ] | Contains Duplicate | Seen Set |
| [ ] | Valid Anagram | Frequency Dictionary |
| [ ] | Group Anagrams | Dictionary Grouping |
| [ ] | Top K Frequent Elements | Frequency |
| [ ] | Move Zeros | Position Tracking |
| [ ] | Second Largest | Tracking |
| [ ] | Check Sorted | Adjacent Comparison |
| [ ] | First Non-Repeating Character | Frequency Dictionary |
| [ ] | String Compression | Counting |
| [ ] | Longest Consecutive Sequence | Set |
| [ ] | Product of Array Except Self | Prefix/Postfix |

### Final Cheat Sheet

Fill this before finishing Day 7.

```text
Pattern: Linear Traversal
Use when:
Example:
Time:
Space:

Pattern: Two Pointers
Use when:
Example:
Time:
Space:

Pattern: Hashing
Use when:
Example:
Time:
Space:

Pattern: Frequency Dictionary
Use when:
Example:
Time:
Space:

Pattern: Sliding Window
Use when:
Example:
Time:
Space:
```

### End-of-Day Output

By the end of Day 7, you should be able to:

- Solve core easy array/string/hash problems confidently.
- Attempt selected medium hashing problems.
- Explain brute force vs optimized solutions.
- Write cleaner function-based code.
- State time and space complexity without guessing.

### Day 7 Completion

| Metric | Target | Actual |
| --- | ---: | ---: |
| Mock rounds completed | 2 | |
| Final problems attempted | 10-12 | |
| Clean rewrites | 8+ | |
| Cheat sheet completed | yes | |

---

## Pattern Decision Rules

### Use Loops When

- You need to visit every element.
- You are counting, summing, searching, finding max/min.
- The problem is simple `O(n)` traversal.

### Use Nested Loops When

- You must compare every pair.
- You are first building brute force.
- Input size is small or optimization is not obvious yet.

### Use Set When

- You only care whether something exists.
- You need uniqueness.
- You are detecting duplicates.
- You do not need counts or indexes.

### Use Dictionary When

- You need frequency counts.
- You need value-to-index mapping.
- You need grouping.
- You need fast lookup plus stored information.

### Optimize When

- Your brute force has nested loops.
- You are repeatedly searching a list.
- You see words like duplicate, frequency, first unique, pair sum, anagram, common elements.
- You can trade `O(n)` extra space to reduce time from `O(n^2)` to `O(n)`.

---

## Weekly Acceptance Criteria

You complete the week successfully if:

- [ ] You solve or seriously attempt 80-100 problems.
- [ ] You write 25+ clean function-based solutions.
- [ ] You explain at least 15 problems in interview format.
- [ ] You convert at least 8 brute force solutions into optimized hashing solutions.
- [ ] You maintain a mistake log with corrections.
- [ ] You state time and space complexity for every solved problem.

---

## Final Level After This Week

Current level:

```text
Beginner problem solving
```

Target level:

```text
Structured beginner-to-early-intermediate DSA thinker
```

You should be ready to start a serious NeetCode/LeetCode roadmap with confidence in:

- Arrays
- Strings
- Dictionaries
- Sets
- Hashing basics
- Two pointers basics
- Complexity analysis
- Clean function-based coding

---

## Next Step: 21-Day Pattern Roadmap

### Week 1: Arrays & Hashing Deeper

- [ ] Group Anagrams
- [ ] Top K Frequent Elements
- [ ] Product of Array Except Self
- [ ] Longest Consecutive Sequence

### Week 2: Two Pointers + Sliding Window

- [ ] Valid Palindrome
- [ ] Two Sum II
- [ ] 3Sum
- [ ] Best Time to Buy/Sell Stock
- [ ] Longest Substring Without Repeating Characters

### Week 3: Stack + Binary Search Basics

- [ ] Valid Parentheses
- [ ] Min Stack
- [ ] Binary Search
- [ ] Search Insert Position
- [ ] Search 2D Matrix

---

## Daily Problem Log Template

Copy this block for every solved problem.

```text
Date:
Day:
Problem:
Topic:
Pattern:
Difficulty:

Brute force idea:

Optimized idea:

Code summary:

Time:
Space:

Mistake:

Redo needed: Yes / No
```

---

## Weekly Scorecard

| Day | Problems Attempted | Solved Without Help | Rewritten Cleanly | Mistakes Logged | Completed |
| --- | ---: | ---: | ---: | ---: | --- |
| Day 1 | | | | | [ ] |
| Day 2 | | | | | [ ] |
| Day 3 | | | | | [ ] |
| Day 4 | | | | | [ ] |
| Day 5 | | | | | [ ] |
| Day 6 | | | | | [ ] |
| Day 7 | | | | | [ ] |


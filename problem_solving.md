# Problem Solving SOP

Every problem. Every time. No exceptions.

---

## BEFORE KEYBOARD (8 min total)

### Step 1 — READ (2 min)
Read the full problem. Not just examples.
Read constraints — they tell you expected time complexity:
  n <= 10^4  → O(n²) acceptable
  n <= 10^5  → O(n log n) needed
  n <= 10^6  → O(n) needed

### Step 2 — RESTATE (1 min)
Write one line: "Given X, find Y such that Z"
If you cannot write this, re-read. Do not move forward.

### Step 3 — PATTERN CHECK (1 min)
Scan trigger words. Which pattern fires?
Write the pattern name before touching code.
If no pattern fires → write brute force first, then think.

Trigger word cheat sheet:
  frequency / count / appears k times → Frequency Hashing
  group together / same chars / anagram → Grouping Hash Map
  top k / most frequent / sort by count → Frequency Sorting
  two numbers add to target / pair sum → Complement Lookup
  running sum / prefix / subarray sum → Prefix Sum
  multiple of k / divisible by k + subarray → Prefix Sum Modulo
  reverse / palindrome / remove in-place / subsequence → Two Pointers
  maximize area / minimize distance between two ends → Two Pointers (maximize)
  contiguous subarray / longest window / at most k → Sliding Window
  max profit / min price so far / running max/min → Running State
  sorted array / find position / O(log n) → Binary Search
  next/prev node / reverse list / detect cycle → Linked List
  matching brackets / next greater element → Stack
  level by level / shortest path → Queue / BFS
  tree height / path sum / invert → Tree DFS
  ancestors / lowest common / BST validate → BST

### Step 4 — BRUTE FORCE (2 min, words only)
"I'll check every pair → O(n²) time"
Say it. Don't code it unless interviewer asks.

### Step 5 — OPTIMAL PLAN (2 min, words only)
"I'll use a hash map to store X, then for each element check Y → O(n)"
Write the plan in plain English. No code yet.

---

## AT KEYBOARD (20-30 min)

### Step 6 — DRY RUN (3 min)
Take the first example. Trace your plan in comments above your function.
Don't skip. This is where you catch logic errors before coding.

### Step 7 — CODE (10-15 min)
Follow your plan exactly. If your plan was wrong, go back to Step 5.
Don't change approach midway without redoing Step 5.

### Step 8 — TEST (5 min)
Run given examples first.
Then test 2 edge cases you pick yourself:
  - Empty input or single element
  - All same values, all negative, or boundary values

### Step 9 — SUBMIT
Only after local tests pass.

---

## COMMENT FIELDS (paste after every solution)

# Status: Independent / Hint / Failed
# Time taken: X min
# Tier: 1 / 2 / 3 / 4
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: [pattern name]
# Variant: [variant name]
# mistakes/confusion: [note or NA]

---

## TIER ASSIGNMENT RULES

Assign tier immediately after solving:

TIER 1 — SHAKY
  Hint needed OR wrong approach OR time taken > 40 min OR failed
  Revision: next day

TIER 2 — BUILDING
  Solved independently BUT time > 25 min OR first time solving this variant
  Revision: 3 days

TIER 3 — STABLE
  Independent + under 25 min + (LC already ✓ in STATUS.md OR LC Accepted today)
  For revision problems: if LC is already ✓ in STATUS.md → no re-submission needed
  For new problems: must submit and get Accepted to reach Tier 3
  Revision: 7 days

TIER 4 — MASTERED
  Stable + 14-day recall passed independently + under 10 min
  Revision: 30 days (template recall only, no full solve)

Tier movement rules:
  Solved independently + fast → move UP one tier
  Needed hint or failed → drop to TIER 1 (restart clock)
  New unseen problem → start at TIER 2
  TIER 4 fails on 30-day recall → drop to TIER 2

---

## TIME TARGETS PER PROBLEM TYPE

Easy problems: 15-20 min
Medium problems: 25-35 min
Hard problems: not in scope for now

If you exceed the target → that problem is TIER 1 regardless of correctness.

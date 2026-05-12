# DSA Progress Tracker

Start date: 2026-05-01  
Current review date: 2026-05-12  
Plan length: 4 months / 16 weeks  
Daily study target: 3-5 focused hours  
Daily problem target: max 5 new problems + mandatory revision  
Goal: placement-oriented DSA preparation using Python, LeetCode, revision, and interview pattern recognition.

## Current State Summary

You are in Month 1, Week 1: Arrays + Hashing + Strings foundation.

Overall status:
- Day 1 array basics: strong.
- Day 1 revision: completed.
- Day 2 array/write-pointer/hash basics: attempted and partially revised.
- Day 3 hash map frequency work completed with good effort but not yet LeetCode-submitted.
- Day 4 string/two-pointer work completed locally; `Reverse String`, `Two Sum`, and `First Unique Character` improved strongly.
- Day 5 prefix/running-state work completed locally; `Running Sum`, `Pivot Index`, and `Best Time To Buy And Sell Stock` were solved without solution viewing, and optional `Product of Array Except Self` was attempted.
- Day 6 hashing/grouping work completed locally: `Majority Element`, `Find Pivot Index`, and `Valid Palindrome` were marked independent; `Top K Frequent Elements` sorting version used syntax help; `Top K Frequent Elements` bucket version and `Group Anagrams` were marked solution viewed.
- LeetCode-ready must-cover set: `Contains Duplicate` is mastered; `Two Sum`, `First Unique Character`, `Running Sum`, `Best Time To Buy And Sell Stock`, `Valid Palindrome`, and `Pivot Index` are close locally but still need LeetCode proof and spaced recall; `Valid Anagram`, `Group Anagrams`, `Top K Frequent Elements`, `Is Subsequence`, and `Product of Array Except Self` remain revisit.
- Main risk: moving too fast before medium hashing, output-array prefix/suffix, no-pivot return values, optimized complexity claims, and LeetCode submission discipline become automatic.

## Strengths

| Area | Evidence | Status |
| --- | --- | --- |
| Basic traversal | Print, sum, count, max/min solved correctly | Strong |
| Tracking variables | Max/min, second largest, majority frequency | Strong but edge cases need care |
| Adjacent comparison | Sorted check, duplicate comparison | Strong |
| Basic in-place writes | Move zeroes, remove element, remove duplicates after concept help | Improving |
| Hashing for lookup | Contains duplicate, intersection, missing number set method, Two Sum complement attempt | Improving |
| Frequency counting | Day 3 frequency counter and First Unique count map were built locally | Improving |
| Basic frequency maximum | Day 06 Majority Element dictionary version solved independently | Strong locally; Boyer-Moore still pending |
| Dictionary grouping mechanics | Day 06 Group Anagrams implementation builds sorted keys and appends words correctly | Improving, but solution viewed |
| Frequency ranking mechanics | Day 06 Top K sorting and bucket versions both implemented locally | Improving, but syntax help/solution viewing used |
| Two Sum complement lookup | Day 04 optimized re-solve was independent and correct locally | Near mastered; needs LC + 3-day recall |
| Frequency + second pass | Day 04 First Unique brute and optimized versions were independent | Near mastered; needs LC + spaced recall |
| Running total / prefix basics | Day 05 Running Sum new-list and in-place versions solved independently | Strong locally; needs LC proof |
| One-pass minimum tracking | Day 05 stock brute force and optimized versions solved independently | Improving; needs 3-day recall |
| Basic in-place reverse | Day 04 Reverse String solved independently | Strong |
| Brute-force discipline | Written for most Day 1/Day 2 problems | Strong habit |
| Complexity awareness | Usually written, but some mistakes remain | Partial |

## Weak / Unstable Areas

| Area | Evidence | Action |
| --- | --- | --- |
| Write-pointer pattern | Remove duplicates needed concept help; remove element used reference | Re-solve 3 times across 7 days |
| Prefix/suffix product | Product except self solved but space complexity uncertain and concept conversion was hard | Revisit before marking mastered |
| One-pass stock profit | Best Time to Buy/Sell Stock needed AI help | Add to failed queue |
| Carry handling | Plus One required solution viewing | Revisit after 24h/3d/7d |
| Rotation edge cases | `k > n`, empty list, reverse method learned with guidance | Revisit |
| In-place cyclic placement | First Missing Positive optimized version not learned | Defer; set method is enough for now |
| Complexity precision | Set membership and sum-formula space were sometimes mislabeled | Daily 10-minute complexity drill |
| Dictionary storage semantics | Two Sum confused storing `needed` vs storing current number/index | Re-solve complement lookup before new hashing mediums |
| Second pass after frequency map | First Unique initially looped over dictionary and lost original index order | Drill count-first, scan-original-second pattern |
| Sorting complexity | Valid Anagram sorting method time complexity was not understood | Review `sorted()` cost: O(n log n) time, O(n) space in Python |
| Pointer skipping in strings | Day 06 Valid Palindrome optimized version was re-solved independently | Confirm with LeetCode proof and 3-day recall |
| Subsequence pointer movement | Is Subsequence required repeated hints on Day 04 and still had unnecessary membership-check thinking on Day 05 | Re-solve again with no membership checks |
| Optimized complexity validation | Valid Anagram final frequency version used `char not in t`, making the claimed O(n) version effectively O(n^2) | Compare dictionary membership vs string membership |
| Check-before-update ordering | Pivot Index required thought around comparing before adding current value to `left_sum` | Dry run left/current/right state |
| Output-array prefix/suffix | Product Except Self Day 05 used two extra arrays, not the target output + suffix variable form | Re-solve optimized version |
| LeetCode submission discipline | Day 04, Day 05, and Day 06 solved locally but still show no accepted submission proof | Day 07 must submit before optional work |
| Medium hashing independence | Day 06 Group Anagrams and bucket Top K were marked solution viewed | Re-solve from blank before advancing medium volume |
| No-match return values | Day 06 Pivot Index returns `0` instead of `-1` when no pivot exists | Add explicit failed-case test before marking stable |
| Function overwrite in practice files | Day 06 reused `top_k_elements` for sorting and bucket versions | Use distinct names or comment out older variants |

## Pattern Recognition State

| Pattern | Recognition Level | Notes |
| --- | --- | --- |
| Linear traversal | Mastered | Can solve and explain. |
| Tracking max/min/count | Mastered with edge-case caution | Initialize from input when non-empty; handle empty explicitly. |
| Adjacent comparison | Mastered | Trigger: sorted/neighbour relation. |
| Basic two pointer | Partial | Reverse and move zeroes seen; not yet broad enough. |
| String two pointer with skipping | Near mastered locally | Day 06 no-hint Valid Palindrome succeeded; needs LeetCode proof and 3-day recall. |
| Subsequence scan | Partial | Trigger understood after hints; needs independent recall. |
| Write pointer | Partial | Trigger: "in-place", "remove", "keep order", "return new length". |
| Set lookup | Partial-to-strong | Trigger: duplicate, membership, intersection, missing value. |
| Frequency dictionary | Partial | Trigger is visible, but manual comparison, second-pass indexing, and complexity still need repetition. |
| Dictionary grouping | Partial | Sorted-key grouping works locally, but Day 06 used solution viewing; re-solve `Group Anagrams` from memory. |
| Frequency ranking / bucket sort | Partial | Sorting by frequency works after syntax help; bucket version was solution viewed and needs a no-notes re-solve. |
| Complement lookup dictionary | Partial | Trigger: pair sum / target. Store seen values with indexes, not needed values. |
| Prefix sum / running total | Partial-to-strong | Running Sum is clean; Pivot Index still needs check-before-add recall. |
| Prefix/suffix products | Unstable | Trigger: product except self, left/right accumulated information. |
| Carry from right | Unstable | Trigger: digit array, plus one, addition simulation. |
| One-pass min tracking | Partial | Day 05 improved; needs repeat until `min_price` and `max_profit` feel automatic. |

## Problems Solved By Status

### Mastered Now

These are safe to treat as mastered, but still revise lightly once per week.

| Problem | Topic | Reason |
| --- | --- | --- |
| Print All Elements | Array traversal | Independent and simple. |
| Sum Of List | Array traversal | Independent with empty case. |
| Count Even Numbers | Counting | Independent. |
| Find Maximum Element | Tracking | Independent. |
| Find Minimum Element | Tracking | Independent. |
| Check If Array Is Sorted | Adjacent comparison | Independent. |
| Move Zeroes To End | Write pointer | Re-solved correctly after initial pointer mistake. |
| Majority Element - dictionary | Frequency map | Re-solved correctly, including Day 06 local independent solve. |
| Contains Duplicate - set | Hashing | Solved with correct pattern; time note corrected to O(n). |
| Intersection Of Two Arrays | Set operations | Independent; complexity corrected to O(n + m). |
| Reverse String | Two pointers / in-place swap | Day 04 independent local solve with correct O(n)/O(1). |

### Requires Revisit

| Problem | Topic | Reason |
| --- | --- | --- |
| Second Largest Distinct Element | Tracking edge cases | Correct now, but empty/all-duplicate handling was learned after hint. |
| Reverse Array | Two pointer / extra list | Function naming and space complexity need precision. |
| Boyer-Moore Majority | Voting | Candidate logic known; validation was learned with help. |
| Remove Duplicates From Sorted Array | Write pointer | Needed concept help. |
| Remove Element | Write pointer | Day 03 independent re-solve succeeded; needs spaced recall before mastery. |
| Missing Number | Set + sum formula | Set method needed hint; complexity note needs correction. |
| Best Time To Buy And Sell Stock | One-pass min tracking | Needed AI help. |
| Plus One | Carry simulation | Solution viewed. |
| Rotate Array | Extra list + reverse | Edge cases and reverse method learned with guidance. |
| Product Of Array Except Self | Prefix/suffix | Day 03 two-array prefix/suffix improved; output-array + suffix version still unstable. |
| First Missing Positive | Set / cyclic placement | Set solved; cyclic placement deferred. |
| Move Negative Numbers To End | Partition/write pointer | Revision solution copied from AI. |
| Third Largest Distinct Element | Tracking | Revision solution copied from AI. |
| Two Sum | Hashing / complement lookup | Optimized version required solution help for dictionary storage line. |
| Valid Anagram | Hashing / strings | Hash-map comparison needed hint; sorting complexity uncertain. |
| First Unique Character in a String | Hashing / strings | Optimized second pass needed hint to preserve original index order. |
| Valid Palindrome | Strings / two pointers | Day 06 independent optimized re-solve succeeded; needs proof/recall before mastered. |
| Is Subsequence | Strings / subsequence scan | Required repeated hints for pointer placement and match-order logic. |
| Find Pivot Index | Prefix sum | Solved locally but optimal check-before-add ordering was confusing. |
| Best Time To Buy And Sell Stock | One-pass running minimum | Solved independently on Day 05, but the mental model still needs spaced recall. |
| Group Anagrams | Hashing / Grouping | Day 06 solution was marked solution viewed; re-solve sorted-key version from memory. |
| Top K Frequent Elements | Hashing / Frequency ranking | Day 06 sorting syntax needed help and bucket version was solution viewed; re-solve sorting version first. |

## Master Progress

| Month | Weeks | Topic | Status | Must-Cover Done | Phase Test |
| --- | ---: | --- | --- | ---: | --- |
| 1 | 1-4 | Arrays + Hashing + Strings + revision discipline | In progress | 1/12 | Not taken |
| 2 | 5-8 | Two pointers + Sliding window + Stack + Queue | Not started | 0/16 | Not taken |
| 3 | 9-12 | Linked list + Binary search + Trees | Not started | 0/18 | Not taken |
| 4 | 13-16 | Graph basics + DP basics + Greedy basics + mocks | Not started | 0/18 | Not taken |

## Weekly Scoreboard

| Week | Topic Focus | Attempted | Independent | Hint | Solution/AI | Accuracy | Decision |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Array basics, write pointer, hashing intro | 43 new + revision | 29 | 8 | 7 | 67% clean / 88% completed | Continue, but Day 7 must consolidate and submit on LeetCode |
| 2 | Hash maps, strings, prefix/suffix, easy mediums | 0 | 0 | 0 | 0 | 0% | Pending |
| 3 | Arrays/hash/strings must-cover mediums | 0 | 0 | 0 | 0 | 0% | Pending |
| 4 | Month 1 mixed revision + timed practice | 0 | 0 | 0 | 0 | 0% | Pending |

## Daily Logs

### 2026-05-02

Week / Day: Week 1 / Day 1  
Phase: Month 1 - Arrays + Hashing + Strings  
Topic: Array traversal, tracking, adjacent comparison, in-place update, basic frequency map

Problems attempted: 10  
Solved independently: 9  
Solved after hint: 1  
Solved after solution: 0  
Unsolved: 0

Main mistakes:
- Extra `None` from `print(function_that_prints())`.
- Second largest needed empty and all-duplicate handling.
- Move zeroes initially missed `pos += 1`.
- Reverse extra-list space is O(n), not O(2).
- Dictionary majority is O(n) space, not O(1).
- Boyer-Moore validation was learned with help.

Decision: Continue, but keep edge-case and complexity revision active.

### 2026-05-08

Week / Day: Week 1 / Day 2 review  
Phase: Month 1 - Arrays + Hashing + Strings  
Topic: Duplicate detection, write pointer, missing values, carry, rotation, prefix/suffix

Problems attempted: 10  
Solved independently: 5 clear independent, 2 partial/reference-based, 3 after help/solution  
Solved after hint/help: Contains Duplicate optimized note, Remove Duplicates concept, Missing Number set method, Rotate edge cases/reverse method  
Solved after solution/AI: Best Time to Buy/Sell Stock, Plus One, some revision variants  
Unsolved: 0 visible, but several are not mastered

Problem list:
1. Contains Duplicate - mastered after correcting optimized time to O(n)
2. Remove Duplicates From Sorted Array - revisit
3. Remove Element - revisit
4. Missing Number - revisit
5. Intersection Of Two Arrays - mastered
6. Best Time To Buy And Sell Stock - revisit
7. Plus One - revisit
8. Rotate Array - revisit
9. Product Of Array Except Self - revisit until prefix/suffix is automatic
10. First Missing Positive - set version okay; cyclic placement not required yet

Decision: Do not increase volume. Next 3 study days should mix 3 new problems max with 2-3 revision problems.

### 2026-05-09

Week / Day: Week 1 / Day 3 review  
Phase: Month 1 - Arrays + Hashing + Strings  
Topic: Hash map frequency, complement lookup, dictionary counting, write-pointer revision, prefix/suffix revision

Problems attempted: 5 plus fundamentals frequency counter  
Solved independently: Fundamentals frequency counter, Remove Element revision, Product of Array Except Self two-array prefix/suffix version  
Solved after hint: Valid Anagram hash-map comparison, First Unique Character optimized second pass  
Solved after solution: Two Sum optimized complement dictionary line  
Unsolved: 0, but no new Day 3 must-cover problem is mastered yet

Problem list:
1. Two Sum - brute force correct; optimized pattern required solution help for `seen[nums[i]] = i`; revisit in 24h and submit only after clean local solve
2. Valid Anagram - brute/sorting/hash versions attempted; hash comparison needed hint and sorting complexity was unclear; revisit in 24h
3. First Unique Character in a String - brute force independent; optimized version needed hint for second pass over original string; revisit in 24h
4. Remove Element - independent revision success; keep in 3-day spaced revision before marking mastered
5. Product Of Array Except Self - improved from Day 2 and passed local examples using left/right arrays; still needs output-array plus one suffix variable version

Strong patterns:
- Brute-force-first habit is becoming reliable.
- Frequency counter fundamentals are workable.
- Write pointer for Remove Element improved meaningfully.
- Local test coverage used multiple edge cases from the work file.

Weak patterns and repeated mistakes:
- Confusing what the dictionary should store in complement lookup.
- Losing original index order when scanning a frequency dictionary.
- Missing or uncertain complexity notes, especially `sorted()` and optimized hash-map methods.
- Prefix/suffix still works mechanically but not yet at the target optimized-space form.
- No LeetCode submission proof yet for Day 3 must-cover problems.

Decision: Pace is sustainable only if Day 4 stays at 3 new problems and 2 revision problems. No optional medium. Revision is improving but still insufficient because Day 3 weak patterns need a 24-hour re-solve.

### 2026-05-10

Week / Day: Week 1 / Day 4 review  
Phase: Month 1 - Arrays + Hashing + Strings  
Topic: String two pointers, subsequence scan, and Day 3 hashing revision

Problems attempted: 6 plus prerequisites/fundamentals  
Solved independently: Reverse String, Two Sum brute force + optimized, First Unique Character brute force + optimized, Valid Anagram brute/sorted/frequency versions locally  
Solved after hint: Is Subsequence  
Solved after solution/hint exposure: Valid Palindrome optimized skip-loop version  
Unsolved: 0 locally, but no Day 04 problem was submitted on LeetCode

Problem list:
1. Valid Palindrome - brute-force cleaned-string version used syntax help; optimized two-pointer skip-loop version needed hint/solution exposure. Revisit in 24h.
2. Reverse String - independent and correct locally. Strong in-place swap pattern, but remember LeetCode expects mutation and no returned new list is required.
3. Is Subsequence - eventually correct locally, but required repeated hints around replacing nested loops with one scan and checking completion inside the loop. Revisit in 24h.
4. Two Sum - brute force and optimized complement lookup were independent and correct locally. Keep as revisit until LeetCode accepted and 3-day recall succeeds.
5. First Unique Character - brute force and optimized frequency + second pass were independent and correct locally. Move toward mastered after LeetCode proof and spaced recall.
6. Valid Anagram - multiple approaches completed independently, but the final "optimized" frequency version uses `char not in t`, so the claimed O(n) complexity is not fully clean. Revisit with dictionary membership or direct map comparison.

Strong patterns:
- Brute-force-first habit remained strong.
- In-place two-pointer swap is solid.
- Two Sum complement lookup improved meaningfully from Day 03.
- Frequency map + second pass improved meaningfully for First Unique Character.
- Sorting complexity for anagram was written correctly as O(n log n) time and O(n) space.

Weak patterns and repeated mistakes:
- Valid Palindrome skip loops were not independently recalled.
- Is Subsequence pointer movement was unstable and overcomplicated with nested-loop thinking.
- Valid Anagram optimized complexity was mislabeled because string membership inside a loop can add extra cost.
- Several tasks were solved locally but none were submitted to LeetCode.
- Some prerequisite code did not follow the requested `dict.get` style even though the concept was described.

Decision: Pace is mostly sustainable, but Day 04 was slightly overloaded because both revision options were completed and no LeetCode submission happened. Day 05 should use 3 new problems max, 2 revision problems, and one accepted LeetCode submission as the non-negotiable target.

### 2026-05-11

Week / Day: Week 1 / Day 5 review  
Phase: Month 1 - Arrays + Hashing + Strings  
Topic: Prefix sum, pivot reasoning, one-pass running minimum, Day 4 string revision

Problems attempted: 7 total: 2 fundamentals, 3 new problems, 2 required revision problems, plus optional Product Except Self  
Solved independently: Running Sum fundamentals, clean hash anagram after self-debug, Running Sum new-list and in-place, Pivot Index brute force and optimal, Best Time To Buy And Sell Stock brute force and optimal, Is Subsequence revision, Product Except Self two-array version  
Solved after hint: Valid Palindrome revision  
Solved after solution: 0 visible today  
Unsolved: 0 locally, but Product Except Self target optimized-space version is still unfinished and no LeetCode acceptance is recorded

Problem list:
1. Running Sum - independently solved in new-list and in-place forms. Can move toward mastered after LeetCode/local timed proof and 3-day recall.
2. Find Pivot Index - independently solved brute force and optimal, but compare-before-adding-current was a confusion point. Revisit in 24h.
3. Best Time To Buy And Sell Stock - independently solved brute force and optimal, a major improvement from Day 2. Revisit in 3 days to confirm the one-pass mental model.
4. Valid Palindrome - still needed hints for skip loops. Keep high-priority revisit.
5. Is Subsequence - solved independently, but the first instinct still included unnecessary membership/frequency thinking. Revisit once more.
6. Product Of Array Except Self - optional attempt succeeded with left/right arrays, but not with output array + one suffix variable. Keep revisit.
7. Clean Hash Anagram - fixed membership/key-error issue, but dictionary comparison should become simpler and cleaner.

Strong patterns:
- Running total / prefix basics improved clearly.
- Brute-force-first habit stayed strong.
- One-pass min tracking improved from help-needed to independent local solve.
- Local examples included empty list, decreasing stock prices, zeroes, and negative/pivot cases.

Weak patterns and repeated mistakes:
- Valid Palindrome skip-loop flow is still not automatic.
- Pivot Index ordering is fragile: compute right sum and compare before updating `left_sum`.
- Is Subsequence still tempts unnecessary membership checks, which can create wrong logic.
- Product Except Self still uses extra left/right arrays instead of the target output-array + suffix pass.
- LeetCode submission proof remains behind the plan.

Edge-case weaknesses:
- Dictionary key checks before frequency comparison.
- Empty input behavior is mostly handled, but should be stated before coding.
- Pivot at index `0` and all-zero arrays need deliberate dry runs.

Implementation weaknesses:
- Reusing the same function name multiple times in one file makes later tests override earlier versions.
- Some comments show conceptual uncertainty even when the code passes examples.
- Complexity notes are mostly correct today, but need more precision around what counts as extra space.

Decision: Current pace is barely sustainable because optional work was added even though LeetCode proof was still missing. Tomorrow should be a consolidation day: 3 new problems max, 2 revision problems, and LeetCode submission before any optional task.

### 2026-05-12

Week / Day: Week 1 / Day 6 review  
Phase: Month 1 - Arrays + Hashing + Strings  
Topic: Dictionary grouping, frequency ranking, majority frequency, pivot revision, palindrome revision

Problems attempted: 5 required problems, with 2 approaches attempted for Top K Frequent Elements  
Solved independently: Majority Element dictionary version, Find Pivot Index revision, Valid Palindrome optimized skip-loop revision  
Solved after hint: Top K Frequent Elements sorting version used help for dictionary sorting syntax  
Solved after solution: Group Anagrams sorted-key version, Top K Frequent Elements bucket-sort version  
Unsolved: No local problem left blank, but Pivot Index has a correctness bug for the no-pivot case and no LeetCode acceptance is recorded

Problem list:
1. Group Anagrams - implementation uses sorted string keys and dictionary lists correctly, but status says solution viewed. Keep revisit.
2. Top K Frequent Elements - sorting version works locally after syntax help; bucket version was solution viewed. Keep revisit and focus on sorting version first.
3. Majority Element - solved independently with dictionary count and correct `O(n)` time / `O(n)` space. Keep near mastered; Boyer-Moore remains optional revisit.
4. Find Pivot Index - marked independent and check-before-add order improved, but code returns `0` instead of `-1` when no pivot exists. Revisit immediately with `[1, 2, 3]`.
5. Valid Palindrome - solved independently with the correct inner skip-loop structure and `O(1)` extra space. This is a strong improvement from Day 05; needs LeetCode proof and 3-day recall before mastered.

Strong patterns:
- Frequency dictionary construction is becoming reliable.
- Valid Palindrome skip loops improved from hint-needed to independent local solve.
- Pivot Index check-before-add structure was recalled.
- Majority frequency solution is straightforward and correct locally.

Weak patterns and repeated mistakes:
- Medium hashing still depends on hints/solutions.
- LeetCode submission is still not happening despite being a daily target.
- Practice files reuse function names, which hides earlier implementations.
- Return values for failure cases need stricter testing.
- Several typos in comments/status labels make review harder, though they do not affect algorithm correctness.

Edge-case weaknesses:
- Pivot Index no-answer case should return `-1`, not `0`.
- Top K tie cases are acceptable in any order, but this should be stated while testing.
- Group Anagrams returns `dict_values`; LeetCode normally accepts list-like groups only after converting with `list(seen.values())`.

Implementation weaknesses:
- Reusing `top_k_elements` for two approaches overwrites the first function.
- Group Anagrams should return `list(seen.values())` for cleaner LeetCode compatibility.
- Frequency code is correct but can be simplified with `freq[x] = freq.get(x, 0) + 1`.

Complexity mistakes:
- Top K sorting version was marked `O(n log n)`; more precise is `O(n + m log m)`, where `m` is unique values. Worst case is `O(n log n)`.
- Group Anagrams complexity `O(n * k log k)` is correct if `n` words have max length `k`; space should mention stored output plus keys.
- Bucket Top K `O(n)` time / `O(n)` space is correct after counting and bucket traversal.

Decision: Current pace is overloaded for medium hashing because solution viewing increased and LeetCode proof is still absent. Day 07 should not be a heavy weekly mock yet. It should be a controlled consolidation day with 3 new/easy-to-medium problems max, 2 revision problems, and one accepted LeetCode submission before any optional work.

## Must-Cover Tracker

### Month 1: Arrays + Hashing + Strings

| Problem | Status | Last Attempt | Revisit |
| --- | --- | --- | --- |
| Contains Duplicate | Mastered | 2026-05-08 | Weekly |
| Two Sum | Revisit | 2026-05-10 | 3d, 7d; submit after one more clean local solve |
| Valid Anagram | Revisit | 2026-05-10 | 24h; fix O(n) hash version and submit after clean solve |
| First Unique Character in a String | Revisit | 2026-05-10 | 3d, 7d; submit after one more clean local solve |
| Group Anagrams | Revisit | 2026-05-12 | Next study day; re-solve sorted-key version without solution |
| Top K Frequent Elements | Revisit | 2026-05-12 | Next study day; re-solve sorting version without syntax help |
| Product of Array Except Self | Revisit | 2026-05-11 | 24h/3d; redo output-array + suffix version |
| Longest Consecutive Sequence | Not started |  | Week 3 |
| Subarray Sum Equals K | Not started |  | Week 3 |
| Valid Palindrome | Near mastered | 2026-05-12 | 3d recall + LeetCode accepted submission |
| Best Time To Buy And Sell Stock | Revisit | 2026-05-11 | 3d, 7d; submit after one clean local timed solve |
| Plus One | Revisit | 2026-05-08 | 24h, 3d, 7d |
| Running Sum of 1d Array | Near mastered | 2026-05-11 | 3d; submit or timed local proof |
| Find Pivot Index | Revisit | 2026-05-12 | Next study day; fix no-pivot return to `-1` |

### Month 2: Two Pointers + Sliding Window + Stack + Queue

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
| Valid Parentheses | Not started |  |  |
| Min Stack | Not started |  |  |
| Daily Temperatures | Not started |  |  |
| Sliding Window Maximum | Not started |  |  |

### Month 3: Linked List + Binary Search + Trees

| Problem | Status | Last Attempt | Revisit |
| --- | --- | --- | --- |
| Reverse Linked List | Not started |  |  |
| Merge Two Sorted Lists | Not started |  |  |
| Linked List Cycle | Not started |  |  |
| Remove Nth Node From End | Not started |  |  |
| Binary Search | Not started |  |  |
| Search in Rotated Sorted Array | Not started |  |  |
| Koko Eating Bananas | Not started |  |  |
| Maximum Depth of Binary Tree | Not started |  |  |
| Invert Binary Tree | Not started |  |  |
| Binary Tree Level Order Traversal | Not started |  |  |
| Validate Binary Search Tree | Not started |  |  |

### Month 4: Graph Basics + DP Basics + Greedy Basics

| Problem | Status | Last Attempt | Revisit |
| --- | --- | --- | --- |
| Number of Islands | Not started |  |  |
| Clone Graph | Not started |  |  |
| Rotting Oranges | Not started |  |  |
| Course Schedule | Not started |  |  |
| Climbing Stairs | Not started |  |  |
| House Robber | Not started |  |  |
| Coin Change | Not started |  |  |
| Longest Increasing Subsequence | Not started |  |  |
| Merge Intervals | Not started |  |  |
| Jump Game | Not started |  |  |

## Failed Problem Queue

| Problem | Topic | Mistake Type | Failed Count | Next Revisit | Notes |
| --- | --- | --- | ---: | --- | --- |
| Second Largest Distinct Element | Arrays / Tracking | Empty input and all duplicates | 1 | Weekly | Correct now; keep edge-case order strict. |
| Reverse Array | Arrays / Two Pointer | Extra-list space and duplicate function name | 1 | Weekly | Use separate names for extra-list and in-place. |
| Boyer-Moore Majority | Voting | Validation pass learned with help | 1 | Week 2 | Explain candidate cancellation before coding. |
| Remove Duplicates From Sorted Array | Write pointer | Concept learned from help | 1 | Next study day | Trigger: sorted + unique + in-place. |
| Remove Element | Write pointer | Previously solved from reference; Day 03 independent re-solve succeeded | 1 | 3 days | Trigger: keep non-target values at front. |
| Missing Number | Set / math | Set method needed hint; complexity confusion | 1 | Next study day | Sum formula uses O(1) extra space. |
| Best Time To Buy And Sell Stock | One-pass min tracking | Day 02 needed help; Day 05 independent local solve improved it | 1 | 3 days | Track `min_price`, update `max_profit`; submit after clean timed solve. |
| Plus One | Carry simulation | Saw solution | 1 | Next study day | Traverse right to left; return early if no carry. |
| Rotate Array | Reverse method | Edge cases learned with guidance | 1 | 3 days | Always reduce `k %= n`; handle empty before modulo. |
| Product Of Array Except Self | Prefix/suffix | Two-array version improved again; optimized output-array + suffix target still unstable | 1 | Next study day | Output array + suffix variable counts as O(1) extra beyond output. |
| Move Negative Numbers To End | Write pointer / partition | Copied from AI in revision | 1 | After write-pointer drill | Re-solve without notes. |
| Third Largest Distinct Element | Tracking | Copied from AI in revision | 1 | After second-largest review | Generalize first/second/third tracking. |
| Two Sum | Hashing / Complement lookup | Solution viewed for storing current value/index | 1 | Next study day | Check complement first, then store `seen[current] = index`. |
| Valid Anagram | Hashing / Character frequency | Hint used for manual dictionary comparison; sorting complexity unclear | 1 | Next study day | Count both maps or count/decrement; know sorted cost. |
| First Unique Character in a String | Hashing / Frequency + second pass | Hint used to scan original string for first index | 1 | Next study day | Count first, then loop over original indexes. |
| Valid Palindrome | Strings / Two pointers | Day 05 needed hints; Day 06 no-hint re-solve improved it | 2 | 3 days | Confirm skip loops with LeetCode proof and no-notes recall. |
| Is Subsequence | Strings / Two pointers | Day 05 independent solve, but unnecessary membership-check instinct remained | 1 | 3 days | Scan `t`; advance `s` pointer only on match; stop when pointer reaches `len(s)`. |
| Find Pivot Index | Prefix sum | Optimal solution worked, but check-before-update placement was confusing | 1 | Next study day | Compute `right_sum = total - left_sum - nums[i]`, compare, then add current. |
| Group Anagrams | Hashing / Grouping | Solution viewed for sorted-key grouping | 1 | Next study day | Use `key = ''.join(sorted(word))`; append word to `groups[key]`; return `list(groups.values())`. |
| Top K Frequent Elements | Hashing / Frequency ranking | Sorting syntax needed hint; bucket version solution viewed | 1 | Next study day | Count first, sort `freq.items()` by count for first clean version; bucket sort is optional later. |

## Revision Status

| Revision Type | Status | Next Action |
| --- | --- | --- |
| Day 1 required revision | Completed | Weekly light recall |
| Day 2 revision | Improving | Stock improved on Day 05; Product still needs optimized-space re-solve |
| Day 3 revision | Improving | Two Sum and First Unique re-solved independently; Valid Anagram needs clean O(n) hash version |
| Day 4 revision | Improving | Valid Palindrome improved on Day 06; Is Subsequence still needs spaced recall |
| Day 5 revision | Improving but incomplete | Pivot and palindrome were re-solved on Day 06; Pivot needs no-answer bug fix; Product optimized form still pending |
| Day 6 revision | Needed | Re-solve Group Anagrams, Top K sorting version, and Pivot no-answer case |
| 24-hour spaced repetition | Active but uneven | Use Day 7 revision slots for Day 6 medium hashing and Day 5 Product optimized form |
| 3-day spaced repetition | Pending | Schedule after next successful re-solve |
| 7-day spaced repetition | Pending | Use weekly review day |
| LeetCode submission proof | Behind | Day 07 requires at least one accepted submission before optional work |

## Pattern-Recognition Notes

| Trigger in Problem Statement | Pattern To Try | Example Problems |
| --- | --- | --- |
| "duplicate", "exists twice", "seen before" | Set lookup | Contains Duplicate |
| "frequency", "most common", "first unique" | Dictionary count | Majority Element, First Unique Character |
| "group anagrams", "same letters grouped together" | Dictionary grouping with sorted string key | Group Anagrams |
| "top k", "most frequent", "k most common" | Frequency count + ranking / bucket | Top K Frequent Elements |
| "two numbers", "target sum", "return indices" | Complement dictionary lookup | Two Sum |
| "same characters with same frequency" | Character frequency comparison | Valid Anagram |
| "first non-repeating" | Frequency map + second pass over original order | First Unique Character |
| "ignore punctuation", "case-insensitive palindrome" | Two pointers with skip loops | Valid Palindrome |
| "is a subsequence", "appears in same order" | One scan with match pointer | Is Subsequence |
| "in-place", "remove", "keep order", "return length" | Write pointer | Move Zeroes, Remove Element, Remove Duplicates |
| "buy before sell", "maximum profit" | One-pass min tracking | Best Time to Buy/Sell Stock |
| "left sum equals right sum", "pivot/equilibrium index" | Prefix sum with check-before-update | Find Pivot Index |
| "running sum", "sum so far", "prefix total" | Running total / prefix sum | Running Sum |
| "all elements except self", "without division" | Prefix/suffix products | Product of Array Except Self |
| "digits", "add one", "carry" | Right-to-left carry simulation | Plus One |
| "rotate by k" | Modulo + reverse / extra list | Rotate Array |
| "smallest missing positive" | Set scan first, cyclic placement later | First Missing Positive |

## Rules For Marking Mastered

Mark a problem `Mastered` only when all are true:
- Solved without hints on a fresh day.
- Accepted on LeetCode or passes all local tests.
- Brute force and optimized idea can be explained.
- Time and space are correct.
- Re-solved once after 3+ days without notes.

Mark `Revisit` when:
- Any hint/full solution was used.
- Complexity is uncertain.
- The pattern trigger is unclear.
- The solution was copied from AI/video/editorial.

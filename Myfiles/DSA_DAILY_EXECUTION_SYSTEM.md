# DSA Daily Execution System

Refactored after Week 1 analysis. Use this file as the operating reference every study day.

The original system built exposure and consistency but lacked:
- Concept introduction before problem exposure
- Pattern-family stability tracking (vs. individual problem lists)
- LeetCode proof as a hard requirement, not a soft goal
- Retrieval practice as a distinct mode with its own rules
- Adaptive load based on which families are shaky vs. stable

What is different now:
- Days have types: Learning, Reinforcement, Consolidation, Mixed Retrieval, Proof/Mock, Recovery
- Every new pattern must start with a Concept Block before any problem is attempted
- Revision is organized by pattern family, not by problem list
- LeetCode proof is a hard prerequisite to unlock optional work and advancement
- Weekly rhythm is fixed: guaranteed mixed retrieval, mock, and recovery slots

---

## Workspace Rules

Root-level files: global roadmaps, trackers, weekly plans, master concepts, this system.
`Daily_Work/`: daily problem files, solution files, evaluations, reflection logs.
File naming: `DAY_XX_WORK.md` for daily logs.

Do not create new roadmap copies, extra trackers, or duplicate planning files.

---

## Part 1: Day Types

### Learning Day

Use when introducing a new pattern family for the first time.

1. Read the Concept Block for the target family — 30 min. Write the template from memory after reading.
2. Revision — 2 old problems from a previously stable family — 30 min.
3. New problems — 1 maximum on the first exposure to a family, 2 maximum if the family was previewed — 60-90 min.
4. LeetCode submission — 1 accepted minimum before optional work.
5. Reflection — fill all fields the same day.

Rules:
- No problem before the concept block is done.
- If the first new problem needed a hint, the second new problem moves to tomorrow.
- Never introduce two new families on the same Learning Day.

---

### Reinforcement Day

Use when a family has been introduced but is not yet at Stable (still Building).

1. Pattern warm-up — write the family template from memory in 5 minutes, no notes.
2. Revision — 2 problems from the target family or an adjacent family — 30-40 min.
3. New problems — 1-2 from the same family — 60-90 min.
4. LeetCode submission — 1 accepted minimum.
5. Reflection — update family stability.

Rules:
- If the warm-up template cannot be recalled, read the Concept Block before proceeding.
- If revision fails (needs a hint), treat the day as Consolidation and skip new problems.
- Problems must belong to the same family or an adjacent one.

---

### Consolidation Day

Use when any active family has a known correctness bug, zero independent re-solves since solution viewing, or a failed retrieval two days in a row.

1. Identify the target family (weakest active pattern).
2. Write the family template from scratch, no notes — 5-10 min.
3. Re-solve 2-3 problems from this family — blank page, no old code — 60-90 min.
4. LeetCode submission — attempt at least one of today's re-solves.
5. Reflection — did the template fire? Where did implementation break?

Rules:
- No new problems on a Consolidation Day.
- If re-solving still requires solution viewing, add to failed queue and try again tomorrow. It does not count.
- Fix one family only. Do not try to consolidate two families in one day.

---

### Mixed Retrieval Day

Use once per week. This is a recall-testing day, not a solving day.

1. Choose 3-4 problems from different pattern families — stable or near-stable families only.
2. Timer: 20-25 minutes per problem.
3. Solve from memory — no hints, no notes, no old code visible.
4. Score each attempt: Independent, Hint-needed, or Failed.
5. Update family stability ratings based on results.
6. LeetCode submission for the cleanest retrieval result.

Rules:
- Do not introduce new concepts on this day.
- Do not open old solution files before attempting.
- Problems must span at least 3 different families.
- A Failed retrieval does not downgrade the problem's status — it adds it to the 3-day revision queue.

---

### Proof/Mock Day

Use once per week. Simulates placement interview conditions.

1. Mini mock: 60-75 minutes, 4 problems, no hints, timer running even when stuck.
   - 1 easy warm-up from a stable family.
   - 2 medium problems from active families.
   - 1 old failed problem from the failed queue.
2. Post-mock review: minimum 30-45 minutes.
   - Record which pattern triggers fired correctly.
   - Record where implementation broke.
   - Add all misses to the failed queue.
3. LeetCode submission: submit the 2 cleanest mock solutions.

Rules:
- Mock only runs if at least 2 accepted LC submissions exist this week.
- Review is mandatory — skipping it wastes the mock.
- Success threshold: 3/4 problems attempted seriously, 2/4 solved cleanly, complexity written for all.

---

### Recovery Day

1. No new problems.
2. Light: complexity drill (write time and space for 5 problems from memory), failed queue cleanup.
3. Update the pattern family stability table for the full week.
4. Write 3 specific goals for the next week.

Rules:
- Optional: one very easy re-solve from a stable family if energy is high.
- No heavy new topic, no mock, no pressure.

---

## Part 2: Weekly Workflow

### Standard 7-Day Rhythm

| Day | Type | Focus |
| --- | --- | --- |
| Day 1 | Learning Day | Introduce or deepen one pattern family |
| Day 2 | Reinforcement Day | Reinforce the Day 1 family + adjacent family |
| Day 3 | Reinforcement Day | Reinforce a different weak family |
| Day 4 | Consolidation Day | Repair the weakest active pattern |
| Day 5 | Mixed Retrieval Day | Cross-family recall test |
| Day 6 | Proof/Mock Day | Mini mock + LeetCode submissions |
| Day 7 | Recovery Day | Light maintenance, plan next week |

### Weekly Non-Negotiables

1. At least 3 accepted LeetCode submissions.
2. At least one Mixed Retrieval session across 3+ families.
3. At least one Mini Mock with post-mock review.
4. Reflection fields filled every day. A blank reflection means the day does not count toward stability upgrades.
5. Pattern family stability table updated at end of week.

### Volume Caps

| Day Type | New Problems | Revision Problems | LC Submissions |
| --- | ---: | ---: | --- |
| Learning Day | 1-2 | 2 | 1 minimum |
| Reinforcement Day | 1-2 | 2 | 1 minimum |
| Consolidation Day | 0 | 2-3 (re-solves only) | 1 attempt |
| Mixed Retrieval Day | 0 | 3-4 (retrieval) | 1 minimum |
| Proof/Mock Day | 0 | 4 (mock) | 2 minimum |
| Recovery Day | 0-1 optional | 1-2 light | 0 |

---

## Part 3: Concept-First Learning Structure

### Why Concept Blocks Come Before Problems

Attempting a problem without pattern context produces two bad outcomes:
1. You solve it randomly and cannot recreate the approach on a different problem.
2. You fail and view the solution, memorizing code without building recall strength.

A Concept Block gives your brain a schema before applying it. Twenty-five minutes of focused Concept Block study is more valuable than sixty minutes of guessing on a problem without context.

The goal is to understand WHY the pattern works — not to memorize code. The template in the block is a starting frame, not the answer.

### Concept Block Template

Every new pattern introduction uses this structure:

```
## CONCEPT BLOCK: [Pattern Name]

### Pattern Intuition
One or two sentences: what mental model captures this pattern?

### Why This Pattern Exists
"The brute force is [X]. This pattern reduces it to [Y] because [Z]."

### Common Trigger Words
Words and phrases in problem statements that signal this pattern.

### State Being Tracked
The exact variable(s) maintained during the scan. What each key and value represents.

### Brute Force vs Optimized
One sentence each: what each approach does and the complexity.

### Common Mistakes
Numbered list of specific errors that appear in first implementations.

### Mini Dry-Run
A 4-6 step trace on a small concrete example, tracking all state variables explicitly.

### Code Template
The minimal pattern skeleton — 5-10 lines. This is the frame, not the full solution.
```

---

## Part 4: Active Pattern Family Concept Blocks

---

### CONCEPT BLOCK: Frequency Hashing

**Pattern Intuition**
Build a dictionary counting how many times each element appears. Use those stored counts to answer questions in a second pass.

**Why This Pattern Exists**
The brute force repeatedly scans the input for every query — O(n²). Pre-counting in one pass converts every subsequent lookup to O(1), reducing total work to O(n).

**Common Trigger Words**
frequency, most common, appears k times, first unique, character count, anagram check, how many times, same frequency, duplicate detection, non-repeating

**State Being Tracked**
`freq = {element: count}` — key is the unique element, value is the number of times it appeared.

**Brute Force vs Optimized**
Brute: nested scan for every count query — O(n²) time, O(1) space.
Optimized: one build pass, one query pass — O(n) time, O(n) space.

**Common Mistakes**
1. `char not in some_string` inside a loop — string membership is O(k), not O(1). Use `char not in freq_dict`.
2. Iterating `freq.items()` for "first occurrence" questions — always iterate the ORIGINAL sequence on the second pass.
3. `freq[x] += 1` crashes with KeyError. Always use `freq.get(x, 0) + 1`.
4. Comparing two frequency maps when one may have keys the other does not — check length first, then compare.

**Mini Dry-Run — First Unique Character in "leetcode"**
Pass 1: `{l:1, e:2, t:1, c:1, o:1, d:1}`
Pass 2 (over original "leetcode"): l → freq=1 → return index 0.
Why not iterate the dict? "loveleetcode" would give 'l' first in the dict, but 'l' appears twice — the dict iteration would be wrong.

**Code Template**
```python
freq = {}
for x in items:
    freq[x] = freq.get(x, 0) + 1

# Second pass ALWAYS over the original sequence, not the dict
for i, x in enumerate(items):
    if freq[x] == 1:
        return i
return -1
```

---

### CONCEPT BLOCK: Grouping Hash Maps

**Pattern Intuition**
Compute a canonical key that is identical for all elements belonging to the same group. Map each canonical key to a growing list of group members.

**Why This Pattern Exists**
Brute-force grouping compares every pair — O(n² × k). A computed canonical key groups all n elements in a single O(n × k log k) pass.

**Common Trigger Words**
group together, same characters, anagram of each other, rearranged letters, classify strings, group by property, bucket by key, words that are anagrams

**State Being Tracked**
`groups = {canonical_key: [list of elements in this group]}`
Key = computed canonical form. Value = growing list of matching elements.

**Brute Force vs Optimized**
Brute: compare every pair to decide same-group — O(n² × k).
Optimized: compute canonical key once per element, insert — O(n × k log k) for sorted key.

**Common Mistakes**
1. Returning `groups.values()` — this is a `dict_values` view, not a list. Always `list(groups.values())`.
2. `groups[key] = groups.get(key, []) + [word]` — creates a new list every time. Use `.setdefault(key, []).append(word)`.
3. Forgetting `"".join(sorted(word))` — sorted() returns a list, which is not hashable. Join it.
4. Using the list directly as a key — lists are unhashable. Use a tuple or join to string.

**Mini Dry-Run — Group Anagrams on ["eat","tea","tan","ate"]**
"eat" → sorted → "aet" → groups["aet"] = ["eat"]
"tea" → sorted → "aet" → groups["aet"] = ["eat","tea"]
"tan" → sorted → "ant" → groups["ant"] = ["tan"]
"ate" → sorted → "aet" → groups["aet"] = ["eat","tea","ate"]
Return: `list(groups.values())` = `[["eat","tea","ate"],["tan"]]`

**Code Template**
```python
groups = {}
for word in words:
    key = "".join(sorted(word))
    if key not in groups:
        groups[key] = []
    groups[key].append(word)
return list(groups.values())
```

---

### CONCEPT BLOCK: Frequency Sorting

**Pattern Intuition**
Count element frequencies first. Then rank or select elements by count using sorting (O(m log m)) or bucket indexing (O(n)).

**Why This Pattern Exists**
You cannot rank by frequency without the frequencies. Once you have the count map, sorting by count is a two-step process — count then rank. Bucket sort avoids the log factor by using count as an array index.

**Common Trigger Words**
top k frequent, k most common, sort by frequency, most frequent elements, kth most frequent, rank by occurrence, k largest frequency

**State Being Tracked**
Phase 1: `freq = {element: count}`
Phase 2 (sorting): elements sorted by their count descending.
Phase 2 (bucket): `buckets[count]` = list of elements with that count; scan buckets right to left.

**Brute Force vs Optimized**
Brute: compare all pairs to rank — O(n²).
Sorting: count in O(n), sort m unique values by count in O(m log m) — total O(n + m log m), worst case O(n log n).
Bucket: count in O(n), bucket fill and scan in O(n) — total O(n).

**Common Mistakes**
1. Writing `O(n log n)` for the sorting version — the precise form is `O(n + m log m)` where m = unique values.
2. Sorting ascending when the problem wants most-frequent-first — use `key=lambda x: -freq[x]` or `reverse=True`.
3. Reusing the same function name for sorting and bucket versions in the same file — the second definition overwrites the first.
4. Bucket size: `buckets = [[] for _ in range(len(nums) + 1)]` — size is n+1 because max count is n.

**Mini Dry-Run — Top K Frequent, nums=[1,1,1,2,2,3], k=2**
Count: `{1:3, 2:2, 3:1}`
Sort keys by count descending: `[(1,3),(2,2),(3,1)]`
Take first k=2: `[1, 2]`

**Code Template — Sorting version (learn this first)**
```python
freq = {}
for x in nums:
    freq[x] = freq.get(x, 0) + 1

sorted_by_freq = sorted(freq.keys(), key=lambda x: -freq[x])
return sorted_by_freq[:k]
```

**Code Template — Bucket version (only after sorting is stable)**
```python
buckets = [[] for _ in range(len(nums) + 1)]
for x, count in freq.items():
    buckets[count].append(x)

result = []
for i in range(len(buckets) - 1, -1, -1):
    result.extend(buckets[i])
    if len(result) >= k:
        return result[:k]
```

---

### CONCEPT BLOCK: Complement Lookup

**Pattern Intuition**
For each element x, check whether the complement (target - x) was seen before. Store elements as you scan — check first, then store, so you never use the same element twice.

**Why This Pattern Exists**
Brute force checks all pairs to find one summing to the target — O(n²). Storing each element's index as you scan turns the complement check into O(1), reducing total work to O(n).

**Common Trigger Words**
two numbers that add up to, find pair with sum, return indices of two elements, target sum, complement pair, two elements sum to target

**State Being Tracked**
`seen = {element_value: index_in_input}` — key = value seen, value = its position.

**Brute Force vs Optimized**
Brute: two nested loops checking all pairs — O(n²) time, O(1) space.
Optimized: one pass with hash map — O(n) time, O(n) space.

**Common Mistakes**
1. Storing `needed = target - x` as the key instead of storing `x` itself. The next element won't find its complement.
2. Storing BEFORE checking — allows using the same element twice. Always check, then store.
3. Returning values instead of indices — the answer is `[seen[needed], i]`, using index values.
4. Forgetting `seen[x] = i` uses the element VALUE as the key and the INDEX as the value.

**Mini Dry-Run — nums=[2,7,11,15], target=9**
i=0, x=2: needed=7. 7 not in seen. seen={2:0}.
i=1, x=7: needed=2. 2 IS in seen at index 0. Return [0,1].

**Code Template**
```python
seen = {}
for i, x in enumerate(nums):
    needed = target - x
    if needed in seen:
        return [seen[needed], i]
    seen[x] = i  # Store AFTER checking — prevents using same element twice
```

---

### CONCEPT BLOCK: Prefix Sum

**Pattern Intuition**
Maintain a running total so that range sums, equilibrium checks, and accumulated products can be answered without rescanning from the beginning each time.

**Why This Pattern Exists**
Recomputing the sum of every range from scratch costs O(n) per query — O(n²) total. Pre-accumulating in O(n) turns each query into O(1).

**Common Trigger Words**
running sum, prefix total, left sum equals right sum, equilibrium index, pivot index, subarray sum, product of all except self, sum up to index, cumulative sum

**State Being Tracked**
Pivot Index: `left_sum` = accumulated sum before current index. `right_sum = total_sum - left_sum - nums[i]`.
Product Except Self: `output[i]` = product of everything to the left. Then multiply by a running suffix variable scanning right to left.

**Brute Force vs Optimized**
Brute: recompute left and right sums at every index — O(n²).
Optimized: one pass for total, one pass accumulating left sum — O(n) time, O(1) extra space for Pivot. O(n) time, O(1) extra space for Product (output array is not counted as extra).

**Common Mistakes**
1. **Pivot ordering**: adding `nums[i]` to `left_sum` BEFORE comparing. The rule: compute right_sum → compare → THEN add nums[i].
2. **Pivot no-match return**: returning `0` instead of `-1`. Always test `[1,2,3] → -1`.
3. **Product space**: building two separate O(n) prefix and suffix arrays. The optimized form uses the output array for left products, then one suffix variable scanning right to left.
4. **Empty input**: `sum([])` returns 0 safely, but the loop will not execute — handle empty explicitly if required.

**Mini Dry-Run — Pivot Index on [1,7,3,6,5,6]**
total=28, left=0.
i=0: right=28-0-1=27. 0≠27. left=0+1=1.
i=1: right=28-1-7=20. 1≠20. left=1+7=8.
i=2: right=28-8-3=17. 8≠17. left=8+3=11.
i=3: right=28-11-6=11. 11==11. Return 3.

**Code Template**
```python
total = sum(nums)
left_sum = 0
for i, x in enumerate(nums):
    right_sum = total - left_sum - x
    if left_sum == right_sum:
        return i
    left_sum += x  # Update AFTER comparison
return -1
```

---

### CONCEPT BLOCK: Two Pointers

**Pattern Intuition**
Place two indexes into a sequence and move them according to a condition — toward each other (opposite-direction), or in the same direction (write pointer, match pointer). This avoids checking all O(n²) pairs.

**Why This Pattern Exists**
Nested loops check all pairs. When the sequence has exploitable structure (sorted, or when you can provably skip certain positions), two pointers visit each element at most twice — O(n).

**Common Trigger Words**
reverse in-place, palindrome, remove elements, keep order, return new length, is subsequence, two numbers in sorted array, skip non-alphanumeric, find pair in sorted array, compact array

**State Being Tracked**
Opposite-direction: `left=0`, `right=len-1`. Move based on comparison result.
Write pointer: `write_pos` = next valid write location, advances only when condition met.
Subsequence match pointer: `s_ptr` = how far into s you have matched, advances only on a character match.

**Brute Force vs Optimized**
Brute: nested loops checking all pairs, or building a reversed copy — O(n²) or O(n) space.
Two pointers: single pass, O(1) space.

**Common Mistakes**
1. **Palindrome skip loops**: inner `while` must be guarded with `left < right`. Without this, an all-punctuation string causes an infinite loop.
2. **Subsequence wrong instinct**: `if char in s` inside a loop checks membership, not order. A character in s may appear later than where you are in s. Always advance `s_ptr` on a sequential match only.
3. **Write pointer**: `write_pos` advances only when a valid element is written, not on every loop iteration.
4. **In-place reverse**: do not return a new list. Mutate the input in-place and return nothing (or return the mutated list if asked).

**Mini Dry-Run — Valid Palindrome on "A man, a plan"**
left=0 (A), right=12 (n). Skip non-alnum inner loops (A is alnum, n is alnum). a==n? No, wait: lowercase: a≠n. Actually "A man, a plan" is not a full palindrome — let's use "racecar".
left=0 (r), right=6 (r). r==r. left=1, right=5.
left=1 (a), right=5 (a). a==a. left=2, right=4.
left=2 (c), right=4 (c). c==c. left=3, right=3.
left >= right. Return True.

**Code Template — Palindrome with skip loops**
```python
left, right = 0, len(s) - 1
while left < right:
    while left < right and not s[left].isalnum():
        left += 1
    while left < right and not s[right].isalnum():
        right -= 1
    if s[left].lower() != s[right].lower():
        return False
    left += 1
    right -= 1
return True
```

**Code Template — Subsequence match pointer**
```python
s_ptr = 0
for char in t:
    if s_ptr < len(s) and s[s_ptr] == char:
        s_ptr += 1
return s_ptr == len(s)
```

---

### CONCEPT BLOCK: Running-State Tracking

**Pattern Intuition**
Keep one or two variables that represent the best outcome so far. Update them as new elements arrive without revisiting earlier elements.

**Why This Pattern Exists**
Brute force evaluates all possible buy/sell pairs or all prefix outcomes — O(n²). When the best state can be maintained in a constant number of variables that update monotonically, one pass is sufficient.

**Common Trigger Words**
maximum profit, buy and sell, best time, minimum price so far, running maximum, track minimum while scanning, one transaction allowed, best result from beginning to current position

**State Being Tracked**
`min_price` = lowest price seen so far (initialized to `nums[0]`, never 0).
`max_profit` = best profit found so far (initialized to 0).
Update rule: if new price < min_price, update min_price. Otherwise, check if `price - min_price > max_profit`.

**Brute Force vs Optimized**
Brute: check all buy/sell pairs — O(n²).
Optimized: one pass, two variables — O(n) time, O(1) space.

**Common Mistakes**
1. `min_price = 0` — wrong when all prices are large positive values. Use `nums[0]`.
2. Updating `max_profit` before checking if price is a new minimum — computes profit using a future min as buy price.
3. Not returning 0 for a decreasing price array — `max_profit` starts at 0 and stays there, which is correct.

**Mini Dry-Run — [7,1,5,3,6,4]**
Start: min=7, profit=0.
price=1: 1<7. min=1.
price=5: 5-1=4>0. profit=4.
price=3: 3-1=2, no update.
price=6: 6-1=5>4. profit=5.
price=4: 4-1=3, no update.
Return 5.

**Code Template**
```python
min_price = nums[0]
max_profit = 0
for price in nums[1:]:
    if price < min_price:
        min_price = price
    elif price - min_price > max_profit:
        max_profit = price - min_price
return max_profit
```

---

## Part 5: Pattern Family Stability System

### Stability Levels

| Level | Criteria | What to Do |
| --- | --- | --- |
| **Shaky** | Trigger not reliably recognized; under 50% of family problems solved independently | Re-read Concept Block; run family drill on simpler problems |
| **Building** | Trigger recognized; implementation fragile (needs hints or syntax help on 1+ problems) | Reinforcement Days; no new families added until this is Stable |
| **Stable** | 70%+ of family problems independent; at least 2 LC acceptances in this family | Adjacent problems can be added; light weekly maintenance |
| **Solid** | All must-cover problems: independent + LC accepted + 3-day recall confirmed | Weekly light recall only |
| **Maintenance** | Solid; no active mistakes | Monthly revisit |

### Current Family Stability (Week 1 End)

| Pattern Family | Level | Primary Blocker | Next Action |
| --- | --- | --- | --- |
| Frequency Hashing | **Building** | Valid Anagram: `char not in string` hidden O(n²) | Fix comparison method; clean re-solve |
| Grouping Hash Maps | **Shaky** | Group Anagrams: zero independent re-solves since solution viewing | Concept Block + blank-page re-solve |
| Frequency Sorting | **Shaky** | Top K: syntax-dependent; bucket solution viewed | Concept Block + sorting re-solve without help |
| Complement Lookup | **Building** | Two Sum: independent locally but no LC proof | LC submission; 3-day recall pending |
| Prefix Sum | **Building** | Pivot Index: correctness bug (`0` vs `-1`); Product: optimized form unsolved | Fix Pivot bug; solve Product output+suffix |
| Two Pointers | **Building** | Palindrome: 1 independent solve only; Subsequence: pointer instinct fragile | 3-day recall test; Subsequence clean re-solve |
| Running-State Tracking | **Building** | Best Stock: 1 independent solve; 3-day recall unconfirmed | 3-day recall test; LC submission |

### How to Update Family Stability

Update the stability table when:
- A family problem was solved independently for the first time → potential Shaky→Building upgrade.
- A family problem got an accepted LC submission → progress toward Stable.
- A family problem failed on a Mixed Retrieval Day → flag for Consolidation.

Formally re-rate each family every Sunday (Recovery Day).

### Family Drill Format

Run on Consolidation or Reinforcement Days:
1. Write the family code template from memory — no notes. If you cannot write it, re-read the Concept Block.
2. Solve problem 1 from this family. Timer: 20 minutes.
3. Solve problem 2 from this family. Timer: 20 minutes.
4. Compare against known solutions without running code first. Find differences.
5. Mark: Independent / Hint-needed / Failed.

A family upgrades from Shaky to Building after 2 consecutive family drills where 70%+ of problems are Independent.
A family upgrades from Building to Stable after 70%+ independent rate across all family problems AND at least 2 LC acceptances.

---

## Part 6: Revision Spacing Structure

### Intervals

| Solve Quality | Revisit Schedule |
| --- | --- |
| Independent, first time | 3 days, 7 days, weekly |
| Solved after hint | 24 hours, 3 days, 7 days |
| Solved after full solution | 24 hours, 3 days, 7 days, 14 days |
| Failed on retrieval (was previously independent) | 24 hours re-solve; restart 3-day clock |
| Mastered (all criteria met) | Weekly light recall |

### Pattern-Level Revision

Old approach: "revise Problem X after 3 days."
New approach: "reinforce the Grouping Hash Maps family on Day 11's reinforcement slot."

In practice: when a problem is due for revision, treat it as a family drill — recall the template and run at least one other problem from the same family in the same session. Revision compounds: each re-solve reinforces both the specific problem and the family pattern.

### Weekly Revision Slots

| Slot | What to Revisit |
| --- | --- |
| Day 2 (Reinforcement) | 24h re-solves from Day 1; last week's weakest family |
| Day 3 (Reinforcement) | 24h re-solves from Day 2; 3-day re-solves due this week |
| Day 4 (Consolidation) | Family with zero independent re-solves or active correctness bug |
| Day 5 (Mixed Retrieval) | 7-day re-solves; cross-family recall |
| Day 6 (Mock) | Old failed problems; must-cover near-mastered |
| Day 7 (Recovery) | 1-2 easy recalls from failed queue only |

---

## Part 7: LeetCode Proof Structure

### What Counts as Proof

An accepted LeetCode submission proves your solution handles all edge cases, not just local examples. It runs within time and space limits. It is syntactically correct.

Local passing is preparation for proof. Local passing alone does not upgrade a problem's status.

### Submission Prerequisites

Before submitting any problem:
- Complexity is written: both time and space, with real variable names (n, m, k — not generic letters).
- At least one edge case was tested locally: empty input, single element, no-answer case.
- The pattern trigger was identified before coding (not reverse-engineered after the solution was found).
- The no-answer return value is correct (`-1` for Pivot Index, not `0` or `None` unless the problem specifies).

### Submission Discipline

1. Submit the problem you solved most cleanly first on any day.
2. Never submit more than twice in a row without understanding what broke.
3. A Wrong Answer must be written down (what test case failed, why the code missed it) before the next submission.
4. Two failed submissions = stop submitting and review the approach.
5. Do not submit random guesses. Every submission must follow from a traced dry run.

### Hard Stops

- Do not add new problems on any day where the LC target was not met.
- Do not upgrade a problem to Near-Mastered or Mastered without at least one accepted submission.
- Do not start the Weekly Mock until at least 2 accepted LC submissions exist for the current week.
- Do not open a new pattern family until LeetCode submissions happen consistently (3+ acceptances in the past 7 days).

---

## Part 8: Progression Rules

### When to Advance Within a Family

Move from easy to medium problems within a family when:
1. 70%+ of current family problems are Independent (no hints needed).
2. At least 2 problems from this family have LC acceptances.
3. The pattern trigger fires within 2 minutes on an unseen problem description.
4. The code template can be written from memory without notes.

### When to Add a New Pattern Family

Introduce a new family only when:
1. At least 2 active families are at Stable or above.
2. No active family has been Shaky for more than 5 consecutive study days.
3. LC acceptance habit is consistent: 3+ acceptances in the past 7 days.

Current blocker for new families: Grouping Hash Maps and Frequency Sorting are both Shaky. These must reach Building before any new pattern family is opened.

### Hard Stop Conditions

Stop advancing and run a Consolidation Day when:
- A family fails recall on Mixed Retrieval Day two sessions in a row.
- The same implementation mistake appears in 3 different problems across different days.
- Blank reflections occur 2 days in a row.
- LeetCode submissions go 3+ days with zero acceptances.

### Speed Limits

- Maximum 2 new pattern families introduced per week.
- Maximum 2 new problems per day on Learning or Reinforcement Days.
- No new family starts in the same week as a full Mock prep week.
- Month 2 topics (Two Pointers opposite-direction expansion, Sliding Window) do not begin until Frequency Hashing and Prefix Sum are both Stable.

---

## Part 9: Problem Solving Protocol

### Steps for Every Problem

1. **Identify pattern family** — before touching code. Which family does this belong to? If you cannot identify it within 3 minutes, re-read the best-match Concept Block.
2. **Restate** — one sentence: what does this problem actually ask for?
3. **Edge cases first** — list 2-3 before coding: empty input, no-answer case, single element, boundary values.
4. **Brute force** — write it, state the complexity. Even if you know the optimized version, brute force comes first.
5. **Optimize** — apply the family pattern. Name what the brute force wasted and what the pattern fixes.
6. **Dry run** — trace one normal case and one edge case by hand, tracking all state variables.
7. **Code** — from scratch, without reading old solutions.
8. **Submit** — only after complexity is written and edge cases are tested locally.
9. **Record** — status (Independent / Hint / Solution), mistake type, revisit date.

### If Stuck

1. Try independently for 25 minutes.
2. Write brute force even if slow — getting anything on paper breaks paralysis.
3. Dry run a tiny example (3-4 elements maximum).
4. Name the blocker: pattern recognition? edge case? implementation detail? optimization direction?
5. Take one hint only — a nudge, not the full solution.
6. Close the hint, re-attempt for 20 minutes.
7. If still stuck: read the approach description only, not the code.
8. Code from memory.
9. Revisit in 24 hours, 3 days, 7 days.

---

## Part 10: Daily Log Template

Copy into `Daily_Work/DAY_XX_WORK.md` each study day. All fields must be filled the same day.

```text
Date:
Week / Day:
Day Type: [Learning / Reinforcement / Consolidation / Mixed Retrieval / Proof/Mock / Recovery]
Pattern Family Focus:

Concept Block reviewed: yes/no — which family:
Template written from memory before solving: yes/no

New problems attempted:
Revision problems attempted:
LeetCode submissions:
LeetCode acceptances:

Solved independently:
Solved after hint:
Solved after solution:
Unsolved:

Problem list:
1. [problem] — [family] — [Independent / Hint / Solution / Unsolved]
2.
3.

Revision list:
1. [problem] — [family] — [result]
2.

Pattern family stability update:
[family]: stayed [level] / upgraded to [level] / downgraded to [level]

Pattern trigger that fired correctly today:
Pattern trigger that did NOT fire (or fired wrong):
Main implementation mistake:

Complexity written for all attempted problems: yes/no
Edge cases tested before submission: yes/no
Failed queue updated: yes/no

Continue / Repeat / Slow down:
Reason:
```

---

## Part 11: Mastery Criteria

A problem is Mastered only when ALL of the following are true:

1. Solved from scratch without hints on a fresh day (not immediately after reading the solution).
2. Accepted on LeetCode.
3. Brute force and optimized approaches can be explained aloud.
4. Time and space complexity are correct and use real variable names.
5. Re-solved once more after 3+ days without reading the previous solution.

A problem stays at Revisit when:
- Any hint or full solution was used.
- Complexity is uncertain.
- The pattern trigger was not identified before coding.
- The solution was copied from AI, video, or editorial.
- A no-answer / edge-case return value was wrong.

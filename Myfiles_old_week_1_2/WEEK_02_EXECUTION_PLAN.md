# Week 02 Execution Plan

Phase: Month 1 — Arrays + Hashing + Strings
Dates: 2026-05-14 through 2026-05-20
System: See `DSA_DAILY_EXECUTION_SYSTEM.md` for day types, concept blocks, and progression rules.

## Week 2 Theme

Stabilize Shaky pattern families before adding any new problem volume.

Grouping Hash Maps and Frequency Sorting are both Shaky — zero independent re-solves since solution viewing. These two families must reach Building before Week 3 begins. Everything else is secondary.

## Week 2 Success Criteria

| Target | Minimum Required |
| --- | --- |
| Accepted LC submissions | 5 |
| Shaky families stabilized | Both Grouping and Frequency Sorting reach Building |
| Independent clean rate | 70%+ on verified work |
| Must-cover upgrades | 3-5 problems to Near-Mastered or Mastered |
| Weekly mock completed | 1 mock, 4 problems, full post-mock review |

## Week 2 Family Focus Order

1. Frequency Hashing — fix Valid Anagram comparison bug
2. Grouping Hash Maps — first independent blank-page re-solve (Shaky → Building)
3. Frequency Sorting — first independent re-solve without syntax help (Shaky → Building)
4. Prefix Sum — fix Pivot Index correctness bug, solve Product optimized form
5. Two Pointers — 3-day recall confirmation for Palindrome and Subsequence
6. Complement Lookup — LC submission for Two Sum
7. Running-State Tracking — LC submission and 3-day recall for Best Stock

---

## Day 8 — Consolidation Day — Frequency Hashing Repair

**Date:** 2026-05-14
**Day Type:** Consolidation
**Family Focus:** Frequency Hashing

### Before Starting

Read the Frequency Hashing Concept Block in `DSA_DAILY_EXECUTION_SYSTEM.md`.
Write the two-pass frequency template from memory before opening any problem file.

### Consolidation Targets

Re-solve both from scratch — no notes, no old code, blank file:

1. **Valid Anagram** — must use dict-to-dict comparison only.
   Forbidden today: `char not in s` or `char not in t` inside any loop.
   Required: build `freq_s` and `freq_t`, then compare `freq_s == freq_t`.
   Test case that must pass: `("anagram","nagaram") → True`, `("rat","car") → False`.

2. **Find Pivot Index** — must return `-1` for no-pivot case.
   Test case that must pass before finishing: `[1,2,3] → -1`.
   Required: compare BEFORE adding `nums[i]` to `left_sum`.

### LeetCode Target

Required before any optional work: submit Valid Anagram or Find Pivot Index.

### Stop Rule

If Valid Anagram still uses string membership inside a comparison loop after the first attempt, stop and fix only that. Do not add any other problem today.

### Reflection Must Include

- What was the exact wrong line in Valid Anagram before? What is the correct line now?
- Did the Pivot Index `-1` test pass on the first attempt?
- Family stability update: Frequency Hashing — did it stay Building or move toward Stable?

---

## Day 9 — Consolidation Day — Grouping Hash Maps (Shaky → Building)

**Date:** 2026-05-15
**Day Type:** Consolidation
**Family Focus:** Grouping Hash Maps

### Before Starting

Read the Grouping Hash Maps Concept Block in `DSA_DAILY_EXECUTION_SYSTEM.md`.
Write the sorted-key grouping template from memory before opening any problem file.

### Consolidation Target

1. **Group Anagrams** — blank page, no notes, no viewing old code.
   Required output: `list(groups.values())` — not `groups.values()`.
   Required key: `"".join(sorted(word))`.
   One attempt only. If solution viewing becomes necessary, mark Exposed, add to 24h queue, and stop here.

### Revision (adjacent family)

2. **Two Sum** — timed, 15 minutes, no notes.
   Required: `seen = {}`, check complement first, then store current value.
   If clean, submit to LeetCode immediately after.

### LeetCode Target

Required before optional work: submit Two Sum. Submit Group Anagrams also if it passed locally.

### Stop Rule

If Group Anagrams requires solution viewing, it does not count as consolidation. Do not add any other problem. Revisit Group Anagrams in 24 hours.

### Reflection Must Include

- Could the sorted-key template be written from memory at the start?
- At which step did implementation break (if it did)?
- Family stability update: Grouping Hash Maps — Shaky or Building?

---

## Day 10 — Reinforcement Day — Prefix Sum Repair

**Date:** 2026-05-16
**Day Type:** Reinforcement
**Family Focus:** Prefix Sum

### Before Starting

Read the Prefix Sum Concept Block. Write the Pivot Index template from memory. State the check-before-add rule aloud before opening any file.

### Revision

1. **Find Pivot Index** — 24h recall test from Day 8. Must pass `[1,2,3] → -1` again. Confirm the fix held.
2. **Running Sum** — timed, 10 minutes. Confirm both new-list and in-place forms independently.

### New Problem

3. **Product Of Array Except Self** — output array + one suffix variable form only.
   Forbidden today: two separate prefix and suffix arrays.
   Required approach: output[i] = product of everything left of i (left pass), then multiply by `suffix` variable scanning right to left.
   Test case: `[1,2,3,4] → [24,12,8,6]`.

### LeetCode Target

Required before optional work: submit Running Sum or Find Pivot Index (confirm `-1` fix holds).

### Stop Rule

If Product Except Self still requires two separate arrays after the first attempt, stop after completing the revision problems. Re-attempt Product tomorrow with the Concept Block open only for the first 5 minutes.

### Reflection Must Include

- Did the output-array + suffix pattern work? What was `suffix` at each index during the dry run?
- Is the Pivot Index `-1` fix stable (Day 8 and Day 10 both passing)?
- Family stability update: Prefix Sum.

---

## Day 11 — Reinforcement Day — Frequency Sorting (Shaky → Building)

**Date:** 2026-05-17
**Day Type:** Reinforcement
**Family Focus:** Frequency Sorting

### Before Starting

Read the Frequency Sorting Concept Block. Write the sorting-version template from memory.
Confirm you can write `sorted(freq.keys(), key=lambda x: -freq[x])` without notes.

### Revision (24h recalls)

1. **Group Anagrams** — 24h recall from Day 9. Blank page, no notes.
2. **Valid Anagram** — confirm the clean comparison fix from Day 8 still holds.

### New Problem

3. **Top K Frequent Elements** — sorting version only.
   Forbidden today: bucket sort version.
   Required: build freq dict, sort by frequency descending, return first k keys.
   Complexity to write: `O(n + m log m)` where m = unique values. Worst case `O(n log n)`.

### LeetCode Target

Required before optional work: submit Group Anagrams or Top K Frequent Elements.

### Stop Rule

If Top K sorting version requires syntax help for the lambda expression, stop and re-read the Frequency Sorting Concept Block. No bucket sort attempt today.

### Reflection Must Include

- Was `lambda x: -freq[x]` recalled independently?
- What is the exact complexity for the sorting version?
- Family stability update: Frequency Sorting — Shaky or Building?

---

## Day 12 — Mixed Retrieval Day — Cross-Family Stability Check

**Date:** 2026-05-18
**Day Type:** Mixed Retrieval
**Family Focus:** All active families

### Rules for Today

No concept block. No new problems. No hints. No opening old solution files before attempting.
Timer: 20-25 minutes per problem.

### Retrieval Set

Solve all of these from memory:

1. **First Unique Character in a String** — Frequency Hashing family.
   Pattern must fire before coding: count first, second pass over original.

2. **Find Pivot Index** — Prefix Sum family.
   Must pass `[1,2,3] → -1` again. This is a third confirmation.

3. **Valid Palindrome** — Two Pointers family.
   This is the 3-day recall test from Day 9. Skip-loop structure must be recalled independently.

4. **Best Time To Buy And Sell Stock** — Running-State Tracking family.
   This is the 7-day recall test. `min_price = nums[0]`, update before checking profit.

### LeetCode Target

Submit whichever retrieval went cleanest. Two submissions if two were clean.

### After Retrieval

Update the family stability table for each tested family. Write one specific observation per family: did the trigger fire automatically or did it require thought?

### Reflection Must Include

- Family stability update for all 4 families tested.
- Which family showed the weakest retrieval and needs Day 4 (Consolidation) attention next cycle?

---

## Day 13 — Proof/Mock Day — Mini Mock

**Date:** 2026-05-19
**Day Type:** Proof/Mock

### Gate Check

Run this mock only if at least 2 accepted LC submissions exist from Days 8-12.
If the gate is not met, treat today as a Reinforcement Day and submit 2 problems before doing anything else.

### Mini Mock — 60 Minutes, No Hints

Problem selection (choose one from each slot at the start of mock):

| Slot | Options |
| --- | --- |
| Easy warm-up (10 min max) | Contains Duplicate or Majority Element |
| Medium 1 (20-25 min) | Valid Anagram or Group Anagrams |
| Medium 2 (20-25 min) | Two Sum or Top K Frequent Elements |
| Old failed (15 min) | Plus One or Product Of Array Except Self |

Rules:
- No hints. Timer runs even if stuck.
- If stuck for more than the time limit, move on and return at the end.
- Write complexity for every problem attempted.

### Post-Mock Review — Minimum 30 Minutes

Required:
- Record which pattern trigger fired correctly for each problem.
- Record which specific implementation step broke.
- Add all miss details to the failed queue.
- Submit the 2 cleanest mock solutions to LeetCode.

Success threshold: 3/4 problems attempted seriously, 2/4 solved cleanly, complexity written for all.

### Reflection Must Include

- Mock score: X/4 attempted, X/4 clean.
- Weakest pattern this mock: which family needs a Consolidation Day next cycle?

---

## Day 14 — Recovery Day — Week 2 Close

**Date:** 2026-05-20
**Day Type:** Recovery

### Tasks (maximum 60 minutes)

1. **Failed queue cleanup** — remove any entries solved independently 3+ times. Update revisit dates.
2. **Complexity drill** — write time and space complexity for 5 problems from memory (no code, just the analysis).
3. **Family stability table update** — formally re-rate all 7 families based on this week's evidence.
4. **Week 2 assessment** — did both Shaky families (Grouping, Frequency Sorting) reach Building? Write yes/no and evidence.
5. **Week 3 goals** — write 3 specific measurable goals based on this week's retrieval results.

### No New Problems

Optional only if energy is genuinely high: re-solve one Recovery-level problem (Contains Duplicate or Majority Element) from memory as a warmup. Nothing harder.

---

## Week 2 Daily Summary

| Day | Type | Family | New | Revision | LC Target |
| --- | --- | --- | ---: | ---: | --- |
| Day 8 | Consolidation | Frequency Hashing | 0 | 2 | Valid Anagram or Pivot Index |
| Day 9 | Consolidation | Grouping Hash Maps | 0 | 2 | Two Sum + Group Anagrams |
| Day 10 | Reinforcement | Prefix Sum | 1 | 2 | Running Sum or Pivot Index |
| Day 11 | Reinforcement | Frequency Sorting | 1 | 2 | Group Anagrams or Top K |
| Day 12 | Mixed Retrieval | All families | 0 | 4 | Cleanest retrieval |
| Day 13 | Proof/Mock | Mixed | 0 | 4 | 2 mock solutions |
| Day 14 | Recovery | All families | 0 | 1-2 light | None |

**Week 2 total new problems: 2**
**Week 2 total revision problems: 17-19**
**Week 2 LC submissions target: 5-7 accepted**

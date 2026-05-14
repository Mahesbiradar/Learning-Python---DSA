# Week 03 Execution Plan

Phase: Month 1 — Arrays + Hashing + Strings
Dates: 2026-05-21 through 2026-05-27
System: See `DSA_DAILY_EXECUTION_SYSTEM.md` for day types, concept blocks, and progression rules.

## Week 3 Prerequisite Check

Before Week 3 starts, verify Week 2 outcomes from the Recovery Day notes:

| Check | Required |
| --- | --- |
| Grouping Hash Maps | Must be Building (at least 1 independent re-solve on record) |
| Frequency Sorting | Must be Building (Top K sorting version independent, no syntax help) |
| Accepted LC submissions in Week 2 | Must be 5+ |
| Pivot Index `-1` bug | Must be fixed and confirmed twice |

If any check fails, repeat the relevant Day 8-11 structure before starting Week 3.

## Week 3 Theme

Controlled expansion: add opposite-direction Two Pointers as a formal skill, push Frequency Sorting and Grouping toward Stable, and introduce the first adjacent medium (Sort Characters By Frequency, Intersection II). No new major pattern family unless Grouping and Frequency Sorting have both reached Building.

## Week 3 Success Criteria

| Target | Minimum Required |
| --- | --- |
| Accepted LC submissions | 5 |
| Families reaching Stable | 1 (Frequency Hashing or Complement Lookup most likely) |
| Two Pointers expansion | Two Sum II solved independently |
| Frequency Sorting reinforced | Sort Characters By Frequency independent |
| Weekly mock completed | 1 mock, 4 problems, full post-mock review |

---

## Day 15 — Learning Day — Two Pointers Expansion

**Date:** 2026-05-21
**Day Type:** Learning
**Family Focus:** Two Pointers (opposite-direction expansion)

### Before Starting

Re-read the Two Pointers Concept Block in `DSA_DAILY_EXECUTION_SYSTEM.md`, specifically the opposite-direction section. Write the opposite-direction template from memory.

Why expansion now: Valid Palindrome (skip-loop) and basic reverse are stable. The next level is sorted-array opposite-direction (Two Sum II, then later 3Sum).

### Revision (recall tests due)

1. **Is Subsequence** — this is the 7-day recall test. Must be clean with no membership check instinct.
   If this fails (needs a hint), treat today as Consolidation for Two Pointers and skip the new problem.
2. **Group Anagrams** — 3-day recall from Day 12. Confirm Building stability held.

### New Problem

3. **Two Sum II — Input Array Is Sorted** — first opposite-direction two-pointer problem.
   The key difference from Two Sum: no hash map. The sorted property means you can move left or right based on the current sum.
   Do NOT use a hash map here — that defeats the point of this problem.
   Pattern: `left=0, right=len-1`. If sum < target: left++. If sum > target: right--. If equal: return.

### LeetCode Target

Required before optional work: submit Valid Palindrome (3-day recall from Day 12 confirmed it — now submit).

### Stop Rule

If Is Subsequence still shows the membership-check instinct on the recall test, stop and treat this as a Two Pointers Consolidation Day. Move Two Sum II to Day 16.

### Reflection Must Include

- Is Subsequence recall: clean or hint-needed?
- Did the opposite-direction pointer logic for Two Sum II fire independently, or was it needed to think through from scratch?
- Family stability update: Two Pointers.

---

## Day 16 — Reinforcement Day — Frequency Sorting Consolidation

**Date:** 2026-05-22
**Day Type:** Reinforcement
**Family Focus:** Frequency Sorting

### Before Starting

Write the Frequency Sorting template from memory (sorting version). Do not open the Concept Block unless the template cannot be recalled.

### Revision (3-day recalls)

1. **Top K Frequent Elements** — 3-day recall from Day 13 mock. Blank page.
   Must be sorting version only, independently. If it needs syntax help: stay on Consolidation, no new problem.
2. **First Unique Character in a String** — 7-day recall. Confirm Frequency Hashing family stability.

### New Problem

3. **Sort Characters By Frequency** — apply the Frequency Sorting template to a string context.
   Count character frequencies, sort by count descending, build the result string.
   This is the same pattern as Top K — count, sort, collect. The output format differs but the pattern is identical.

### LeetCode Target

Required before optional work: submit Top K Frequent Elements (sorting version).

### Stop Rule

If Top K still needs any syntax help for `sorted(..., key=lambda x: -freq[x])`, treat today as Consolidation. No new problem (Sort Characters moves to tomorrow).

### Reflection Must Include

- Was Top K recalled cleanly on the first attempt?
- How similar is Sort Characters By Frequency to Top K? Can you name the pattern difference in one sentence?
- Family stability update: Frequency Sorting.

---

## Day 17 — Reinforcement Day — Running State + Prefix Solidification

**Date:** 2026-05-23
**Day Type:** Reinforcement
**Family Focus:** Running-State Tracking + Prefix Sum

### Before Starting

Write the Running-State template from memory (Best Stock). Write the Pivot Index template. Both from memory, no notes.

### Revision (spaced recalls)

1. **Best Time To Buy And Sell Stock** — this is the 7-day recall from Week 2 Day 12. The most important test this week.
   Initialize from `nums[0]`. Update min before checking profit.
   If clean: submit to LeetCode immediately.

2. **Product Of Array Except Self** — 3-day recall from Day 10. Confirm output-array + suffix form held.

### New Problem

3. **Intersection of Two Arrays II** — bridge problem between Frequency Hashing and set lookup.
   Build a frequency map for one array, then consume counts while scanning the other.
   This is distinct from Intersection of Two Arrays (which returns unique values). Here counts matter.

### LeetCode Target

Required before optional work: submit Best Stock or Product Of Array Except Self.

### Stop Rule

If Product Except Self still reverts to two-array form on the recall test, treat today as Prefix Sum Consolidation. Move Intersection II to tomorrow.

### Reflection Must Include

- Best Stock 7-day recall: Independent or Hint-needed? This determines whether Running-State Tracking stays Building or upgrades.
- Product Except Self: is the output-array + suffix pattern now automatic?
- Family stability update: Running-State Tracking, Prefix Sum.

---

## Day 18 — Consolidation Day — Cross-Family Stabilization

**Date:** 2026-05-24
**Day Type:** Consolidation
**Family Focus:** Weakest active family (determined from Days 15-17 reflections)

### Before Starting

Check the family stability table from Days 15-17 reflections. Pick the single weakest active family. Options by likelihood:
- Grouping Hash Maps (if Day 9 re-solve did not hold at Day 15)
- Frequency Sorting (if Top K still needed help on Day 16)
- Two Pointers (if Is Subsequence failed the recall on Day 15)

### Structure

1. Write the target family's template from memory.
2. Re-solve 2 problems from this family — blank page, no notes.
3. LeetCode submission for at least one.

### No New Problems Today

This is a repair day, not an expansion day. If all families are Building or above: choose the one closest to Stable and run a family drill to push it over the threshold.

### LeetCode Target

2 LC submissions from re-solves.

### Reflection Must Include

- Which family was targeted and why?
- Did both re-solves go Independent?
- Full family stability table update for all 7 families.

---

## Day 19 — Reinforcement Day — Medium Two Pointers Preview

**Date:** 2026-05-25
**Day Type:** Reinforcement
**Family Focus:** Two Pointers (medium-level preview)

### Before Starting

Write the opposite-direction two-pointer template from memory. State: "sorted array + target sum → left/right pointers, no hash map."

### Revision

1. **Two Sum II** — 3-day recall from Day 15. Blank page, no notes.
2. **Is Subsequence** — confirm it is stable. This should now be a quick 10-minute recall.

### New Problem

3. **3Sum** — medium, first exposure.
   This is a preview only. 3Sum requires sorting + outer loop + two-pointer inner loop.
   Goal today: understand the approach and write a working solution — not necessarily in optimal time.
   Expected difficulty: 30-40 minutes. If it needs a hint, mark Assisted, not Failed — this is genuinely harder.
   Bucket Sort is not the pattern. The pattern is: sort, fix one element, two-pointer for the remaining pair.

### LeetCode Target

Required before optional work: submit Two Sum II.

### Stop Rule

If 3Sum requires full solution viewing (not just a hint), mark it Exposed and move on. 3Sum consolidation can happen in Week 4. The priority today is confirming Two Sum II is stable.

### Reflection Must Include

- Two Sum II 3-day recall: Independent or Hint?
- 3Sum first attempt: what specific step broke? (sorting + fixed pointer, skip duplicates, or two-pointer movement?)
- Family stability update: Two Pointers.

---

## Day 20 — Mixed Retrieval Day — Pre-Mock Stability Check

**Date:** 2026-05-26
**Day Type:** Mixed Retrieval
**Family Focus:** All active families

### Rules for Today

No concept block. No new problems. No hints. No opening old solution files.
Timer: 20-25 minutes per problem.

### Retrieval Set

Five problems, one from each of the most critical families:

1. **Valid Anagram** — Frequency Hashing. Must use dict comparison only.
2. **Group Anagrams** — Grouping Hash Maps. Sorted key, list return.
3. **Top K Frequent Elements** — Frequency Sorting. Sorting version, correct complexity.
4. **Find Pivot Index** — Prefix Sum. Returns `-1`, check before update.
5. **Valid Palindrome or Is Subsequence** — Two Pointers. Your choice.

### LeetCode Target

1 submission from cleanest retrieval.

### After Retrieval

Full family stability update for all 7 families. This is the pre-mock checkpoint. Which 2-3 problems will be strongest in tomorrow's mock? Which family is the biggest risk?

### Reflection Must Include

- Retrieval scores per family.
- Mock readiness: which 2 medium problems from tomorrow's options feel most confident?
- Family stability final update before mock.

---

## Day 21 — Proof/Mock Day — Full Mock

**Date:** 2026-05-27
**Day Type:** Proof/Mock

### Gate Check

Run this mock only if at least 3 accepted LC submissions exist from Days 15-20.
If not met, use today as a Reinforcement Day (submit 2 problems, then light retrieval).

### Full Mock — 75 Minutes, No Hints

Problem selection (choose one from each slot at the start of the mock):

| Slot | Options |
| --- | --- |
| Easy warm-up (10 min max) | Contains Duplicate or Running Sum |
| Medium 1 — Hashing (20-25 min) | Group Anagrams or Valid Anagram |
| Medium 2 — Prefix or Running State (20-25 min) | Product Of Array Except Self or Best Stock |
| Medium 3 — Two Pointers (20-25 min) | Two Sum II or Is Subsequence |

Rules:
- No hints. Timer runs even if stuck.
- Move on after the time limit per slot. Return at the end if time remains.
- Write complexity for every problem attempted, even if the solution is incomplete.

### Post-Mock Review — Minimum 45 Minutes

Required:
- Record which pattern trigger fired correctly for each problem.
- Record the exact implementation step that broke for each miss.
- Add all miss details to the failed queue.
- Submit the 2 cleanest mock solutions to LeetCode.

Success threshold: 3/4 problems attempted seriously, 2/4 solved cleanly, complexity written for all.

### Reflection Must Include

- Mock score: X/4 attempted, X/4 clean.
- Strongest pattern family this mock.
- Weakest pattern family this mock (will be priority for Week 4).
- Month 1 progress assessment: are Frequency Hashing and Prefix Sum approaching Stable?

---

## Week 3 Daily Summary

| Day | Type | Family | New | Revision | LC Target |
| --- | --- | --- | ---: | ---: | --- |
| Day 15 | Learning | Two Pointers expansion | 1 | 2 | Valid Palindrome |
| Day 16 | Reinforcement | Frequency Sorting | 1 | 2 | Top K Frequent |
| Day 17 | Reinforcement | Running State + Prefix | 1 | 2 | Best Stock or Product |
| Day 18 | Consolidation | Weakest active family | 0 | 2-3 | 2 from re-solves |
| Day 19 | Reinforcement | Two Pointers medium | 1 | 2 | Two Sum II |
| Day 20 | Mixed Retrieval | All families | 0 | 5 | 1 cleanest retrieval |
| Day 21 | Proof/Mock | Mixed | 0 | 4 | 2 mock solutions |

**Week 3 total new problems: 4**
**Week 3 total revision problems: 19-21**
**Week 3 LC submissions target: 5-7 accepted**

---

## 2-Week Adaptive Progression Summary (Days 8-21)

| Metric | Week 2 Target | Week 3 Target |
| --- | --- | --- |
| New problems | 2 | 4 |
| Revision problems | 17-19 | 19-21 |
| LC submissions | 5-7 accepted | 5-7 accepted |
| Families upgraded | Grouping + Frequency Sorting: Shaky→Building | 1 family: Building→Stable |
| New patterns opened | None | Two Pointers opposite-direction |
| Mock | 1 mini mock (Day 13) | 1 full mock (Day 21) |

The volume is intentionally low. Two new problems per week is not a sign of slow progress — it is a sign that consolidation is working. Retrieval practice across 17+ revision slots per week builds the retention that high-volume unsupported solving destroys.

---

## What Comes After Week 3

Week 4 is Month 1 mixed revision and the first full timed mock (2 easy + 3 medium in 90 minutes). The families that are not yet Stable by end of Week 3 become Week 4's priority consolidation targets.

The month boundary (Week 4 → Month 2) should only be crossed when:
- Frequency Hashing and Prefix Sum are both Stable.
- LeetCode submission habit is consistent: 3+ acceptances in the past 7 days.
- At least one full mock has been completed with 2/4 problems solved cleanly.

Do not start Month 2 (Two Pointers full suite + Sliding Window) early. The sliding window pattern depends on frequency hashing stability — a shaky frequency map inside a window produces bugs that are hard to trace.

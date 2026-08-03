# DSA STUDY SYSTEM — PROMPTS

All prompts require `SYSTEM_RULES.md` to be uploaded alongside the other files.

---

## PROMPT 1 — END OF DAY UPDATE

**Upload:** `SYSTEM_RULES.md`, `STATUS.md`, `DAY_N.md`, `DAY_N_SOLUTIONS.py`

You are the **DSA Validator**. Follow `SYSTEM_RULES.md` for all definitions, tier rules, and precedence.

### Tasks
1. **Validate** each solution in `DAY_N_SOLUTIONS.py` via static analysis. Classify each: `Verified Correct` / `Likely Correct` / `Incorrect`.
2. **Read metadata** comments. Auto-correct inconsistencies per `SYSTEM_RULES.md` §6.
3. **Compute Tier** for each problem using `SYSTEM_RULES.md` §3. Never read Tier from comments.
4. **Update `STATUS.md`**:
   - **Problem Tracker**: add new problems introduced today. Update `Tier`, `Last Solved`, `Next Due`, `LC`, and `Notes` for every problem solved today.
   - **Pattern Coverage Map**: for every newly solved curriculum problem, perform these three operations atomically: (a) increment `Actual`, (b) decrement `Remaining`, (c) remove the problem from `Pending Problems`. If the solved problem is not part of the curriculum, increment `Actual` only; do not modify `Remaining` or `Pending Problems`.
   - **Learning Phase Tracker**: update `Status` if the current phase target is met.
   - **Regression Log**: add entry if a previously Tier 3/4 problem now requires `Hint` or `Failed`.
   - **Unresolved-Since-Origin**: mark `Standalone Done = Yes` if resolution criteria are met.
   - **Pattern Assessment Log**: add entry if an assessment occurred today.
5. Do not modify any section not listed above. Do not generate derived tables.

### Output Format
1. **Evaluation Report** (10–15 lines):
   - New / Revision / Total counts
   - Validation summary (`Verified / Likely / Incorrect`)
   - Tier changes today
   - Metadata corrections made
   - Biggest mistake and biggest win
   - Top 5 revision priorities for tomorrow
2. **Full updated STATUS.md** (paste below the report)

---

## PROMPT 2 — NEXT DAY PLAN

**Upload:** `SYSTEM_RULES.md`, `STATUS.md`, `PATTERNS.md`, `problem_solving.md`

You are the **DSA Planner**. Follow `SYSTEM_RULES.md` for day types, scheduling precedence, and tier logic.

### Tasks
1. **Determine Day Type** by checking triggers in `SYSTEM_RULES.md` §2 order:
   - Standalone → Recovery → Consolidation → Assessment → Learning → Reinforcement.
2. **Source of truth**:
   - Use **Problem Tracker** exclusively for revision scheduling, due revisions, and tier ordering.
   - Use **Pattern Coverage Map** exclusively for selecting new learning problems, checking `Remaining`, and checking `Pending Problems`.
   - Never infer curriculum progress by scanning the Problem Tracker.
3. **Derive revision queue** 
         Build revision queue:

         Step 1
         Include all overdue revisions
         (Next Due < Today)

         Step 2
         Include today's revisions
         (Next Due == Today)

         Step 3
         If total workload is still below target,
         fill remaining slots using the earliest future
         Next Due dates.

         Never begin with future revisions.

4. **Build schedule**:
  Build schedule in this exact order

         1.Standalone (if any)

         2.Tier 1 revisions

         3.Tier 2 revisions

         4. New Problems Include the number of new problems specified by the active Day Type in SYSTEM_RULES.md .Select them from the Pattern Coverage Map.

         5.Tier 4 template recalls Maximum 2.

         6.Tier 3 revisions

         7.If workload is still below target,continue selecting future revisions by earliest Next Due.Never replace Mandatory New Problems or Tier 4 recalls with revisions.

         8.If mandatory work exceeds the recommended workload allow the total workload to exceed the recommendation.Never remove Tier 1, Tier 2, New Problems, or Tier 4 recalls.

5. **Learning block**: If introducing a pattern for the first time, include the full pattern block from `PATTERNS.md` before the first problem.
6. **SOP reminder**: Include at the top:  
   `Read → Restate → Identify Pattern → Plan in Words → Dry Run → Code → Test → Submit`
7. **Metadata template**: Paste the mandatory metadata block from `SYSTEM_RULES.md` §6 once near the top of `DAY_N.md`. Pattern and Variant must remain blank. The learner fills these after solving. Do **not** include `Tier`. Do not repeat this block after individual problems.
8. **Daily Summary** at end:  
   `New: X | Tier1: X | Tier2: X | Tier3: X | Tier4: X | Total: X`

### Output
Only the completed DAY_N.md using this layout:

# Status:
# Time Taken:
# Time Complexity:
# Space Complexity:
# Submitted to LC:
# Result:
# Pattern:
# Variant:
# Mistakes / Confusion:

---

Read → Restate → Identify Pattern → Plan in Words → Dry Run → Code → Test → Submit

---

## Schedule

### Tier 4

1. LC xxx — Problem Name

### New

1. LC xxx — Problem Name

### Tier 1

1. LC xxx — Problem Name

### Tier 2

1. LC xxx — Problem Name

### Tier 3

1. LC xxx — Problem Name

---

## Daily Summary

New: X | Tier1: X | Tier2: X | Tier3: X | Tier4: X | Total: X

---

## PROMPT 3 — WEEKLY REVIEW

**Upload:** `SYSTEM_RULES.md`, `STATUS.md`, and all `DAY_N.md` + `DAY_N_SOLUTIONS.py` from the review period.

You are the **DSA Reviewer**. Follow `SYSTEM_RULES.md` for stability thresholds and tier logic.

### Tasks
1. **Week Summary** (10 lines):
   - Date range and study days count
   - Total new problems introduced
   - Total revisions completed
   - Unique LC accepts (first-time only)
   - Independent solve rate
   - Average time per problem
   - Variants that reached Stable this week
   - Tier 1 problems carried over
   - Biggest pattern gap
   - Verdict: `On Track` / `Slightly Behind` / `Behind` + reason

2. **Pattern Coverage Progress**:
   - For each active DS: problems solved vs target, variants complete, estimated weeks remaining (`remaining ÷ current weekly new-problem rate`, rounded up).

3. **Next Week Plan**:
   - Day type forecast for each day (based on current state).
   - Focus variant.
   - Assessment scheduled if readiness conditions in `SYSTEM_RULES.md` §10 are met.

4. **Update `STATUS.md`**:
   - **Learning Phase Tracker**: advance phase or variant if targets met.
   - **Pattern Assessment Log**: add entry if assessment occurred.
   - **Problem Tracker**: add weekly observations to `Notes` where relevant.
   - **Unresolved-Since-Origin**: update if resolved.

Do not write derived tables.

### Output
1. Weekly Review text (under 30 lines)
2. Full updated `STATUS.md`

---

## PROMPT 4 — RANDOM DRILL

**Upload:** `SYSTEM_RULES.md`, `STATUS.md`

You are the **DSA Drill Agent**.

**User input format:** `N=___ filter=___`

**Available filters:**
- `all` — any problem in Problem Tracker
- `tier:1|2|3|4` — only problems at that tier
- `pattern:[name]` — only problems from that pattern family
- `variant:[name]` — only problems from that specific variant
- `weak` — Tier 1 and Tier 2 problems only
- `lc-pending` — problems where `LC = ✗` or blank
- `new` — problems not yet in Problem Tracker (select from Pattern Coverage Map Pending)

### Tasks
1. Derive candidate pool:
   - For `new`: use Pattern Coverage Map `Pending Problems` not present in Problem Tracker.
   - For all other filters: filter Problem Tracker.
2. Randomly select `N` matching problems. No repeats within the session.
3. Output drill cards in this format for each:


```
--- Drill [i/N] ---

Difficulty: Easy / Medium / Hard
Problem: [Name]
LC #: [Number]
Time Target: [X] min
Goal: [One-line objective]

[ ] Independent — time: ___ min
[ ] Hint — what: ___
[ ] Failed

Submitted to LC: Yes / No
Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
```


4. Wait for the user to share results. Then compute tiers per `SYSTEM_RULES.md` §3 and update `STATUS.md` Problem Tracker, Pattern Coverage Map, etc., following Prompt 1 update rules.

### Output
Drill cards first. Wait for results. Then updated `STATUS.md`.

---

## PROMPT 5 — PATTERN ASSESSMENT

**Upload:** `SYSTEM_RULES.md`, `STATUS.md`

You are the **DSA Assessment Agent**.

### Tasks
1. **Identify target DS**: Check Learning Phase Tracker. Select the DS that is complete (all variants at target) or the most recently active DS.
2. **Select problems**: From Pattern Coverage Map `Pending Problems` for that DS, pick 4 unseen problems (not in Problem Tracker): **2 Easy + 2 Medium**.
3. **Generate assessment** in `DAY_N.md` format:
   - Header: `## Assessment — [Date] — [DS Name]`
   - Rules: 30 min per problem. No hints. No pattern labels. Submit to LC after local solve.
   - Four problem blocks with full statements, constraints, examples, and metadata fields.
   - Scoring rubric at end:
     - 4/4 independent → DS Mastered → mark phase complete in Learning Phase Tracker.
     - 3/4 → One more reinforcement day, then reassess.
     - ≤2/4 → One more week on weakest variant before reassessment.

### After User Shares Results
Update `STATUS.md`:
- Add entry to **Pattern Assessment Log**.
- Add all 4 problems to **Problem Tracker** with computed tiers.
- Remove solved problems from **Pattern Coverage Map** Pending.
- Update **Learning Phase Tracker** based on score.

### Output
1. Assessment `DAY_N.md`
2. After results: updated `STATUS.md`
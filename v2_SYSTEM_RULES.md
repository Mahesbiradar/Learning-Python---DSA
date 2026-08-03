# SYSTEM RULES

Static rulebook for the DSA Study System. These rules are authoritative. LLM agents must follow them exactly. Humans modify this file only when changing system policy.

---

## 1. AUTHORITY & PRECEDENCE

### Data Precedence
When files conflict:
1. **SYSTEM_RULES.md** — definitions and policies always win.
2. **Today's work** — `DAY_N_SOLUTIONS.py` overrides historical state for problems solved today.
3. **STATUS.md Problem Tracker** — authoritative for all historical problem state.
4. **DAY_N.md** — plan intent only; execution truth is `DAY_N_SOLUTIONS.py`.

### Scheduling Precedence (highest → lowest)
1. Standalone
2. Recovery
3. Consolidation
4. Assessment
5. Tier 1 revisions
6. Tier 2 revisions
7. Mandatory New Problems (2–3)
8. Tier 4 template recalls (maximum 2)
9. Tier 3 revisions

If two items conflict, always obey the higher-priority rule.

---

## 2. DAY TYPES

Determined automatically by checking conditions in the order listed below. A day has exactly one type.

| Type | Trigger | New Problems |
|------|---------|-------------|
| **Standalone** | `STATUS.md` → Unresolved-Since-Origin declares a mandatory session | 1 |
| **Recovery** | Gap ≥ 3 days since last study day recorded in STATUS.md header | 0 |
| **Consolidation** | Count of Tier 1 problems in Problem Tracker ≥ 5 | 2-3 |
| **Assessment** | Current DS has all variants at target solved count AND no assessment logged for this DS in Pattern Assessment Log | 0 (assessment problems instead) |
| **Learning** | Current variant in Learning Phase Tracker has pending problems in Pattern Coverage Map | 2–3 mandatory |
| **Reinforcement** | Current variant has no pending problems but solved count &lt; target, OR the DS needs stabilization before assessment | 2–3|

---

## 3. TIER SYSTEM

### Definitions
| Tier | Name | Criteria | Next Due Offset |
|------|------|----------|-----------------|
| 1 | Shaky | Hint needed OR failed OR &gt;40 min OR wrong approach OR incorrect complexity annotation | +1 day |
| 2 | Building | Independent but &gt;25 min OR first successful solve of this variant | +3 days |
| 3 | Stable | Independent + ≤25 min + LC Accepted | +7 days |
| 4 | Mastered | Tier 3 + 14-day recall passed independently + &lt;10 min | +30 days (template recall only) |

### Movement Rules
- Independent + under time target → promote UP one tier.
- Hint needed or failed → drop to Tier 1 (restart clock).
- New unseen problem → start at Tier 2.
- Tier 4 fails 30-day recall → drop to Tier 2.

### Next Due Calculation
`Next Due = Last Solved + offset days` based on the tier assigned **today**.
If multiple problems receive the same Next Due date, the planner may stagger by ±1 day to prevent clumping.

---

## 4. PATTERN STABILITY

Computed dynamically from Problem Tracker. **Never stored in STATUS.md.**

| Status | Condition |
|--------|-----------|
| Building | &lt;70% independent solve rate on variant OR &lt;5 LC accepted in family |
| Stable | ≥70% independent solve rate on variant AND ≥5 LC accepted in family |
| Mastered | All variants Stable + assessment score ≥ 3/4 |

A variant is considered complete when solved count ≥ Target in Pattern Coverage Map.

---

## 5. TIME TARGETS

| Difficulty | Target |
|------------|--------|
| Easy | 15–20 min |
| Medium | 25–35 min |
| Hard | Not in scope |

Exceeding the target contributes to tier assignment but does not auto-fail a solution.

---

## 6. DAILY STRUCTURE

Mandatory Daily Allocation

Every study day must contain:

• New Problems:
  - The number of new problems is determined by the active Day Type defined in Section 2.
  - New problems are selected from the Pattern Coverage Map.


• Tier 4:
  - Maximum 2 recalls per day.
  - Skip if none are due.

• Tier 1:
  - All overdue/current due.

• Tier 2:
  - All overdue/current due.

• Tier 3:
  - Fill remaining workload.

Target workload remains 10–12 items.

If mandatory work exceeds 12,
allow workload to exceed 12.

Never remove mandatory blocks.

### Recommended Workload
10–12 items total (new problems + revisions + template recalls). This is a recommendation, not a hard cap. The learner may voluntarily increase workload.

### Mandatory Metadata (paste once at the top of each DAY_N.md)
```text
# Status:
# Time Taken:
# Time Complexity:
# Space Complexity:
# Submitted to LC:
# Result:
# Pattern:
# Variant:
# Mistakes / Confusion:
The learner fills these fields after solving each problem. Do not repeat this block after individual problems.

...
```

### SOP Reminder (top of every DAY_N.md)
Read → Restate → Identify Pattern → Plan in Words → Dry Run → Code → Test → Submit

---

## 7. LEARNING PHASE POLICY

- Never introduce a future Data Structure until the current phase is marked complete.
- Finish the current variant before moving to the next variant.
- A phase is complete when all variants reach target solved count AND are Stable.
- Mandatory Standalone Session overrides the Learning Phase for that day only.

---

## 8. OVERRIDE PROTOCOL

If the human wants to deviate from the generated plan:
1. Add `OVERRIDE: [reason]` at the top of `DAY_N.md` before solving.
2. Prompt 1 logs the override in the Problem Tracker `Notes` column.
3. The validator does not alter tier logic based on overrides.

---

## 9. DERIVED DATA POLICY

The following views are computed on demand from the Problem Tracker. They must **never** be stored in STATUS.md:
- Revision Pool
- Pattern Family Stability table
- Mastered (Tier 4) list
- LC Submission Log
- Weekly Scores table
- Solved count per variant

---

## 10. ASSESSMENT RULES

- **Trigger:** All variants of current DS at target solved count and Stable.
- **Format:** 4 unseen problems (2 Easy + 2 Medium) from Pattern Coverage Map Pending.
- **Conditions:** No pattern labels. No hints. 30 min per problem. Submit to LC after local solve.
- **Scoring:**
  - 4/4 independent → DS Mastered → mark phase complete.
  - 3/4 → One more reinforcement day, then reassess.
  - ≤2/4 → One more week on weakest variant before reassessment.

---

## 11. WEEKLY REVIEW RULES

- Triggered by the human when desired (recommended once per week).
- Inputs: STATUS.md + all DAY_N.md + all DAY_N_SOLUTIONS.py from the review period.
- Updates allowed: Learning Phase Tracker, Pattern Assessment Log, Problem Tracker notes, Unresolved-Since-Origin.
- Does not write derived tables.

---

## 12. SYSTEM TARGETS

- Total problems solved: 180-200
- LC accepted: 115–120
- Timeline: Oct 2026

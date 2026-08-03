# SYSTEM ARCHITECTURE

Version 2.0 | Deterministic Human-in-the-Loop DSA Learning Pipeline

---

## 1. OVERVIEW

A state-machine with human execution. The human solves problems; LLM agents plan, validate, and update state. All state is stored in markdown files. No databases. No JSON. No YAML.

This architecture eliminates drift by removing every derived table from the central state file.

---

## 2. FILE RESPONSIBILITIES

| File | Type | Who Writes | Who Reads | Purpose |
|------|------|------------|-----------|---------|
| `SYSTEM_RULES.md` | Static | Human | All Agents | Authoritative rulebook for tiers, precedence, and policy |
| `SYSTEM_ARCHITECTURE.md` | Static | Human | Human | Documentation and design rationale |
| `STATUS.md` | Dynamic | Prompt 1, Prompt 3 | Prompt 2, Prompt 4, Prompt 5, Human | Central state — contains only source-of-truth tables |
| `PATTERNS.md` | Static | Human | Prompt 2, Human | Pattern library with templates and common mistakes |
| `problem_solving.md` | Static | Human | Prompt 2, Human | SOP and problem-solving protocol |
| `DAY_N.md` | Generated | Prompt 2 | Human | Daily plan and problem statements |
| `DAY_N_SOLUTIONS.py` | Human | Human | Prompt 1, Prompt 3 | Ground truth of execution and metadata |

---

## 3. SINGLE SOURCE OF TRUTH

**Problem Tracker** (inside STATUS.md) is the only mutable state table.

Every other view is derived at read time by filtering, sorting, or aggregating the Problem Tracker:

| View | Derivation Rule |
|------|----------------|
| **Revision Pool** | Filter Problem Tracker where `Next Due ≤ today`, sort by `Tier` ascending, then `Next Due` ascending |
| **Pattern Family Stability** | Aggregate Problem Tracker by `Pattern + Variant`; compute independent rate and LC accepted count |
| **Mastered List** | Filter Problem Tracker where `Tier = 4` |
| **Weekly Scores** | Computed by Prompt 3 from the week's `DAY_N_SOLUTIONS.py` files |
| **LC Submission Count** | Count unique rows in Problem Tracker where `LC = ✓` |
| **Solved Count per Variant** | Count rows in Problem Tracker matching `Pattern + Variant` |

Because these views are computed, they can never drift out of sync with the Problem Tracker.

---

## 4. DATA FLOW

```
┌─────────────────┐     ┌─────────────────┐
│  SYSTEM_RULES   │     │   PATTERNS.md   │
│     .md         │     │                 │
└────────┬────────┘     └────────┬────────┘
         │                       │
         └───────────┬───────────┘
                     ▼
            ┌─────────────────┐
            │    STATUS.md    │
            │  (Problem       │
            │   Tracker)      │
            └────────┬────────┘
                     │
         ┌───────────┼───────────┐
         ▼           ▼           ▼
    ┌────────┐ ┌────────┐ ┌────────┐
    │Prompt 2│ │Prompt 1│ │Prompt 3│
    │ Plan   │ │Validate│ │ Review │
    └───┬────┘ └───┬────┘ └───┬────┘
        │          │          │
        ▼          ▼          ▼
    ┌────────┐ ┌────────┐ ┌────────┐
    │DAY_N.md│ │Updated │ │Updated │
    │        │ │STATUS.md│ │STATUS.md│
    └───┬────┘ └────────┘ └────────┘
        │
        ▼
┌─────────────────┐
│DAY_N_SOLUTIONS  │
│      .py        │
└─────────────────┘
```

---

## 5. DAY LIFECYCLE

1. **Plan** — Human uploads `SYSTEM_RULES.md`, `STATUS.md`, `PATTERNS.md`, `problem_solving.md` → **Prompt 2** generates `DAY_N.md`.
2. **Execute** — Human solves problems and writes `DAY_N_SOLUTIONS.py` with mandatory metadata comments.
3. **Validate** — Human uploads `SYSTEM_RULES.md`, `STATUS.md`, `DAY_N.md`, `DAY_N_SOLUTIONS.py` → **Prompt 1** updates `STATUS.md`.
4. **Paste** — Human replaces `STATUS.md` with the updated version.
5. **Review** — (Optional) Human uploads the week's files → **Prompt 3** updates `STATUS.md`.

---

## 6. AGENT BOUNDARIES

| Agent | Plans | Validates | Updates State | Reads Rules | Output |
|-------|-------|-----------|---------------|-------------|--------|
| **Prompt 1** (Validator) | No | Yes | Yes | Yes | Evaluation report + updated STATUS.md |
| **Prompt 2** (Planner) | Yes | No | No | Yes | DAY_N.md only |
| **Prompt 3** (Reviewer) | No | No | Yes | Yes | Weekly review + updated STATUS.md |
| **Prompt 4** (Drill) | No | No | Yes | Yes | Drill cards, then updated STATUS.md |
| **Prompt 5** (Assessment) | Yes* | No | Yes | Yes | Assessment problems, then updated STATUS.md |

\* Prompt 5 generates assessment problems, not daily plans.

No agent both plans and updates state. This separation prevents corruption from cascading.

---

## 7. DESIGN PRINCIPLES

- **No derived tables in STATUS.md** — eliminates an entire class of drift defects.
- **Rules externalized** — `SYSTEM_RULES.md` is the single contract. Prompts reference it, never duplicate it.
- **Deterministic day types** — checked in strict priority order. No weekday assumptions.
- **Mandatory new problems** — Learning Days always include 2–3 new problems from the current variant.
- **Soft workload target** — 10–12 items recommended, but no hard cap. The learner controls volume.
- **Variant completion focus** — finish one variant before starting the next. Prevents half-finished scatter.
- **Override transparency** — human deviations are logged but do not break tier logic.

---

## 8. TOKEN OPTIMIZATION

- STATUS.md shrank from ~400 lines to ~150 lines by deleting 6 derived sections.
- Prompts shrank by ~60% by removing embedded rule duplicates.
- Agents upload `SYSTEM_RULES.md` once per session; it is static and cacheable.
- Problem Tracker remains the largest table, but it is the only table that must be uploaded for planning.

---

## 9. TROUBLESHOOTING

**Q: The planner scheduled too many items.**
A: There is no hard cap. Use `OVERRIDE:` in DAY_N.md to trim, or solve what you can and let the rest remain due.

**Q: A derived view looks wrong.**
A: Recompute it manually from Problem Tracker. If the Problem Tracker is correct, the view is correct by definition.

**Q: Prompt 1 added a derived table back into STATUS.md.**
A: Reject the output. Paste the corrected STATUS.md without the derived table. Remind the agent: "Do not write derived tables."

**Q: I want to change a rule.**
A: Edit `SYSTEM_RULES.md`. Do not edit prompts. All prompts reference the rule file.

# DSA Daily Execution System

Use this file every study day. This is the sustainable operating system for the 4-month placement DSA roadmap.

## Workspace Organization Rules

Use only:
- `Daily_Work/` for daily problems, daily solutions, evaluations, and revision solutions.
- `Prompts/` for reusable AI prompts only.
- Root-level files for global roadmaps, trackers, weekly plans, master concepts, and progress systems.

Daily file names must follow this exact format:
- `DAY_XX_PROBLEMS.md`
- `DAY_XX_SOLUTIONS.py`
- `DAY_XX_EVALUATION.md`

All Python solutions must go inside the matching `Daily_Work/DAY_XX_SOLUTIONS.py` file. Do not create separate topic solution files, duplicate trackers, extra roadmap files, archive copies, or nested planning systems.

## Core Rule

Maximum new problems per day: 5.  
Minimum revision every day: 2 problems or 45 minutes.  
Target consistency: 70-80% of planned days completed.  
Do not chase 10+ problems/day. Retention beats volume.

## Recommended Daily Study Hours

Normal day: 3-4 focused hours.  
Strong day: 4-5 focused hours.  
Low-energy day: 90-120 minutes, but still do fundamentals + one revision problem.

## Daily Workflow

| Block | Time | Work |
| --- | ---: | --- |
| Fundamentals revision | 20-30 min | Python concept needed today: loops, functions, list/set/dict, strings, complexity |
| Pattern warm-up | 15-20 min | Recall yesterday's pattern trigger and write it in 2-3 lines |
| New DSA problems | 90-150 min | 3-5 new problems max; usually 2 easy + 2 medium + 1 optional |
| Revision problems | 45-75 min | Re-solve failed queue using 24h/3d/7d spacing |
| LeetCode submissions | 20-40 min | Submit must-cover or medium problems after local dry run |
| Pattern notes | 15 min | Write trigger, brute force, optimized idea, edge cases |
| Mistake tracking | 10 min | Update failed queue immediately |

## Problem Count Targets

Normal day:
- 3 new problems.
- 2 revision problems.
- 1 LeetCode submission minimum.

High-focus day:
- 5 new problems maximum.
- 2-3 revision problems.
- 2 LeetCode submissions.

Revision/mock day:
- 0-2 new problems.
- 4-6 old/failed problems.
- Timed practice only.

## Difficulty Progression

Month 1:
- 60% easy, 40% medium.
- Hard problems are optional and only for reading pattern exposure.

Month 2:
- 40% easy, 55% medium, 5% hard exposure.

Month 3:
- 30% easy, 60% medium, 10% interview-level exposure.

Month 4:
- 20% easy, 65% medium, 15% hard/interview exposure.

## Exact Problem Solving Steps

Follow this sequence for every important problem.

### 1. Understand

- Restate the problem in your own words.
- Identify input, output, constraints, and edge cases.
- Write 2-3 examples manually.

### 2. Prerequisite Check

Before coding, ask:
- Do I know the Python structure needed?
- Do I know the pattern trigger?
- Have I solved a simpler version?

If prerequisites are weak, revise for 10-20 minutes before solving.

### 3. Brute Force

- Write the simplest possible idea first.
- Estimate time and space.
- Keep it short; do not spend the whole session here.

### 4. Optimize

Ask which pattern can improve it:
- Hashing
- Sorting
- Two pointers
- Sliding window
- Stack
- Queue/deque
- Recursion
- BFS/DFS
- Binary search
- DP
- Greedy

### 5. Dry Run

- Use one normal case.
- Use one edge case.
- Track variables step by step.

### 6. Code Locally

- Write a clean Python function.
- Use clear names.
- Test with visible cases.
- Add one custom edge case.

### 7. Submit On LeetCode

Submit when:
- The local solution passes visible examples.
- You can explain the pattern.
- Complexity is written.

Do not submit random guesses repeatedly. If rejected twice, stop and review.

### 8. Record Result

Update:
- Status: independent / hint / solution / unsolved.
- Pattern trigger.
- Mistake type.
- Revisit date.

## If Stuck Rules

Use this ladder.

1. Try independently for 25-35 minutes.
2. Write brute force even if slow.
3. Dry run a tiny example.
4. Identify blocker: pattern, edge case, implementation, or optimization.
5. Take one hint only.
6. Close the hint and reattempt for 20 minutes.
7. If still stuck, read the solution idea only.
8. Code from memory.
9. Re-solve after 24 hours, 3 days, and 7 days.

Never mark mastered if you only understood after a full solution.

## Spaced Repetition System

| Result | Revisit |
| --- | --- |
| Independent and clean | 7 days |
| Solved after hint | 24 hours, 3 days, 7 days |
| Solved after full solution | 24 hours, 3 days, 7 days, 14 days |
| Failed twice | Return to concept + 3 easier pattern problems |
| Failed three times | Pause topic progression and rebuild prerequisites |

## Weekly Mock System

Every 7th study day:
- 1 easy warm-up, 15 minutes.
- 2 medium problems, 35-40 minutes each.
- 1 mixed old problem, 25 minutes.
- Review for 60-90 minutes.

Mock rules:
- No hints during the timed block.
- After the block, write why each miss happened.
- Failed mock problems go into the failed queue.

## Daily Log Template

Copy this into `DSA_PROGRESS_TRACKER.md` each day.

```text
Date:
Week / Day:
Month:
Topic:
Today's topic:
Why this topic now:
Prerequisites checked:
Weak prerequisites:
Prerequisite revision completed:

Fundamentals revised:

New problems attempted:
Revision problems attempted:
LeetCode submissions:

Solved independently:
Solved after hint:
Solved after solution:
Unsolved:

Problem list:
1.
2.
3.
4.
5.

Revision list:
1.
2.

Main mistakes:

Patterns recognized:

Brute force written? yes/no
Dry runs completed? yes/no
Complexities written? yes/no
Failed queue updated? yes/no

Continue / repeat / slow down:
Reason:
```

## Mastery Score

For each problem, assign:
- 4: independent, optimized, correct complexity, LeetCode accepted, re-solved later.
- 3: independent after thinking, minor mistakes fixed.
- 2: solved after hint or nearby reference.
- 1: solved after full solution.
- 0: unsolved.

Only scores 3-4 count toward interview readiness.

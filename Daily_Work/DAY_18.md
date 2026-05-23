# Day 18 — May 24, 2026 — Retrieval
Focus: Sliding Window (24h recall) + Grouping Hash Maps / Prefix Sum (7d final recall)
LC target today: Submit 1004 and 219 if today's 24h recall is fully independent — both are marked ready

---

## Note: No new problems today
8 revision items are due May 24. 5 slots are filled below by priority (24h overdue → 7d finals).
Sort Chars by Freq (451), Intersection II (350), and Product of Array Except Self (238) carry to tomorrow
(May 25 is the week's final retrieval day and already includes these three).

---

## Concept Warm-Up (5 min)
Write the variable-size Sliding Window template from memory. No notes.
Focus specifically on the shrink loop and the delete-vs-zero decision.

```python
# Variable-size sliding window




```

---

## Revision Problems (5 problems)

### Max Consecutive Ones III (LC 1004)
Pattern: Sliding Window
Due: 24h revision — independent D17 — ready to submit
Constraint: 1 <= nums.length <= 10^5; nums[i] is 0 or 1; 0 <= k <= nums.length.
Goal: Reproduce independently. Two valid approaches — zero-counter integer OR frequency map. Aim for the O(1) space version.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Find All Anagrams in a String (LC 438)
Pattern: Sliding Window + Frequency Hashing
Due: 24h revision — hint-needed D17 — must solve independently this time
Constraint: 1 <= s.length, p.length <= 3 * 10^4; both lowercase English letters.
Goal: Solve fully independently. Focus on: fixed window of `len(p)`, when to delete a key (count == 0), appending `left` (not `right`) to result.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Contains Duplicate II (LC 219)
Pattern: Sliding Window
Due: 24h revision — independent D17 — ready to submit
Constraint: 1 <= nums.length <= 10^5; -10^9 <= nums[i] <= 10^9; 0 <= k <= 10^5.
Goal: Reproduce the set-based fixed window independently. Focus on: check before add, shrink when set size exceeds k.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Group Anagrams (LC 49)
Pattern: Grouping Hash Maps
Due: 7d final recall
Constraint: 1 <= strs.length <= 10^4; strs[i] consists of lowercase English letters.
Goal: Sorted-key grouping from memory in under 5 minutes. This is the final scheduled recall.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

### Find Pivot Index (LC 724)
Pattern: Prefix Sum
Due: 7d final recall
Constraint: 1 <= nums.length <= 10^4; -1000 <= nums[i] <= 1000; return -1 if no pivot exists.
Goal: One-pass O(n) solution from memory. Recall: `right = total - left - nums[i]`. Final scheduled recall.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

## Carried to May 25
These three are May 24 7d final recalls that overflow the 5-slot limit.
They are already in the May 25 queue — solve them tomorrow alongside the other May 25 due items.

- Sort Chars by Freq (LC 451) — Frequency Sorting — 7d final recall
- Intersection Arrays II (LC 350) — Frequency Hashing — 7d final recall
- Product of Array Except Self (LC 238) — Prefix Sum — 7d final recall

---

Note: After solving each problem in your .py file, log these comment fields:
  # Status: Independent / Hint / Failed
  # Time complexity: O(?)
  # Space complexity: O(?)
  # LC status: Accepted / NA / Not submitted
  # mistakes/confusion: [note or NA]
  # Pattern: [pattern name]
Prompt 1 reads these directly — no separate reflection needed.

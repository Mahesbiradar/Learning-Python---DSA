# Day 35 — 2026-07-09 — Learning Day
Focus: Linked Lists — Dummy Node (Remove Nth / merge) — new variant | Continuing: Traversal+basic ops (Reverse), In-place manipulation (Reverse Between)
Phase: New DS — Linked Lists (Jul 7 – Jul 21)
Daily target: 10 problems (3 Tier1 + 0 Tier2 due + 2 Tier3 + 2 Tier4 recalls + 3 new)

---
## SOP Reminder (2 min before every problem)
Read fully → Restate in one line → Identify pattern → Plan in words → Dry run → Code → Test

Full SOP: problem_solving.md. Do not skip Step 3 (write `# Pattern: ... | Variant: ...` before coding).
RULE: complexity fields must be real answers with justification, never `O(?)`. Wrong complexity = automatic Tier 1.

---
## NEW PATTERN CONCEPT BLOCK — Linked Lists: Dummy Node (Remove Nth / Merge)

**Where to learn:** Neetcode.io → search "Dummy Node Linked List" or "Merge Two Sorted Lists" → watch the concept part only (15 min). Do not watch the coded solution before attempting LC 21 yourself.

**Trigger words:** merge two lists, remove nth node, node before the head might change, splice lists together, sentinel node

**Mental model:** Create a fake node that points to the real head. Do all your pointer surgery relative to the dummy, so you never need a special case for "the head itself changes."

**Why it exists:** Without a dummy node, removing or replacing the head requires an `if not head` branch every time the head changes. A dummy node makes "the node before position 0" always exist, so head-of-list edits use the exact same code path as any other edit.

**Template (fill in from memory after watching — do not copy from a solution):**
```python
def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    # ___ (two pointers, both start at dummy)
    # ___ (advance fast n+1 steps ahead of slow)
    # ___ (move both together until fast hits None)
    # ___ (slow.next now sits exactly before the node to remove — unlink it)
    return dummy.next
```

**Dry run — head = 1 -> 2 -> 3 -> 4 -> 5, n = 2:**
```
dummy -> 1 -> 2 -> 3 -> 4 -> 5
slow=dummy, fast=dummy
advance fast 3 steps (n+1=3): fast now at node 3
move slow,fast together until fast=None:
  slow=1,fast=4 -> slow=2,fast=5 -> slow=3,fast=None (stop)
slow.next (node 4) is the one to remove
slow.next = slow.next.next  → 1 -> 2 -> 3 -> 5
return dummy.next
```

**Common mistakes (first exposure to this pattern — none logged yet in PATTERNS.md):**
1. Forgetting the dummy node and special-casing "if the head itself must be removed"
2. Off-by-one on the fast-pointer head start — advancing n steps instead of n+1 leaves slow one node too early
3. Returning `head` instead of `dummy.next` — wrong if the original head was the node removed/replaced
4. Merge Two Sorted Lists: forgetting to attach the leftover tail of whichever list still has nodes after the loop ends

**Note for after solving today:** No Linked List block exists yet in PATTERNS.md (flagged Day 34, still not written). After today's session, write the Reverse-List template, the Reverse-Between template, and this Dummy-Node template into PATTERNS.md so Day 36's warm-up has something to recall against.

---
## TIER 4 Recalls (5 min each, no full solve)
Write the pattern template from memory. If you can't in 3 min → flag as Tier 2.
**Note: Sliding Window recall was self-graded "correct" on Day 34 but was actually buggy (returned the running window count instead of the tracked max) — output mismatch not caught by self-check. Retrying today; check the return line carefully.**
1. Sliding Window (Fixed size)
2. Binary Search (Standard)

```
# Pattern 1 recalled correctly (Y/N): ___
# Pattern 2 recalled correctly (Y/N): ___
```

---
## TIER 1 — Priority Revision (solve all 3, no hints)

### 1. Total Appeal of A String — Hard
The appeal of a string is the number of distinct characters found in the string. Given a string `s`, return the total appeal of all of its substrings.
Note: 3 consecutive attempts have been brute force O(n²) only. This time, before coding, write out: for each character at index `i`, how many substrings is it the LAST occurrence contributing to? (Hint: compare to the previous index that character appeared at.)

Example 1: `s = "abbca"` → Output: `28`
Example 2: `s = "code"` → Output: `20`

Constraints: `1 <= s.length <= 10^5`, lowercase English letters.

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```

### 2. Reverse a Singly Linked List — Easy
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1: `head = [1,2,3,4,5]` → Output: `[5,4,3,2,1]`
Example 2: `head = [1,2]` → Output: `[2,1]`
Example 3: `head = []` → Output: `[]`

Constraints: number of nodes is `0` to `5000`, `-5000 <= Node.val <= 5000`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```

### 3. Reverse a Linked List Between Two Positions — Medium
Given the head of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right` (1-indexed), and return the reversed list.

Example 1: `head = [1,2,3,4,5], left = 2, right = 4` → Output: `[1,4,3,2,5]`
Example 2: `head = [5], left = 1, right = 1` → Output: `[5]`

Constraints: number of nodes `n`, `1 <= n <= 500`, `-500 <= Node.val <= 500`, `1 <= left <= right <= n`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```

---
## TIER 2 — Revision (0 problems due today — none in the pool have hit their due date. Skipping this slot.)

---
## TIER 3 — Revision (2 problems — one overdue pick + one due today)

### 1. Length of Last Word — Easy
Given a string `s` consisting of words and spaces, return the length of the last word in the string. A word is a maximal substring consisting of non-space characters only.

Example 1: `s = "Hello World"` → Output: `5`
Example 2: `s = "   fly me   to   the moon  "` → Output: `4`
Example 3: `s = "luffy is still joyboy"` → Output: `6`

Constraints: `1 <= s.length <= 10^4`, `s` consists of only English letters and spaces `' '`. There will be at least one word in `s`.

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```

### 2. First Bad Version — Easy
You are a product manager leading a team to develop a new product. Since each version is developed based on the previous version, all the versions after a bad version are also bad. Suppose you have `n` versions `[1, 2, ..., n]` and you want to find the first bad one, which causes all the following ones to be bad. You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version, minimizing calls to the API.

Example 1: `n = 5, bad = 4` → Output: `4`
Example 2: `n = 1, bad = 1` → Output: `1`

Constraints: `1 <= bad <= n <= 2^31 - 1`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```

---
## New Problems (3 problems) — identify the pattern yourself, do not skip Step 3 of the SOP

### 1. Merge Two Sorted Lists — Easy
You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted list by splicing together the nodes of the first two lists. Return the head of the merged linked list.

Example 1: `list1 = [1,2,4], list2 = [1,3,4]` → Output: `[1,1,2,3,4,4]`
Example 2: `list1 = [], list2 = []` → Output: `[]`
Example 3: `list1 = [], list2 = [0]` → Output: `[0]`

Constraints: number of nodes in both lists is in the range `[0, 50]`, `-100 <= Node.val <= 100`, both `list1` and `list2` are sorted in non-decreasing order.

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```

### 2. Remove Nth Node From End of List — Medium
Given the head of a linked list, remove the `n`th node from the end of the list and return its head.

Example 1: `head = [1,2,3,4,5], n = 2` → Output: `[1,2,3,5]`
Example 2: `head = [1], n = 1` → Output: `[]`
Example 3: `head = [1,2], n = 1` → Output: `[1]`

Constraints: number of nodes `sz`, `1 <= sz <= 30`, `0 <= Node.val <= 100`, `1 <= n <= sz`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```

### 3. Maximum Twin Sum of a Linked List — Medium
*(Carried over from Day 34 — planned but not attempted.)*
In a linked list of size `n`, where `n` is even, the `i`th node (0-indexed) is the twin of the `(n-1-i)`th node, for `0 <= i <= (n/2)-1`. The twin sum is defined as the sum of a node and its twin. Given the head of a linked list of even length, return the maximum twin sum.

Example 1: `head = [5,4,2,1]` → Output: `6`
Example 2: `head = [4,2,2,3]` → Output: `7`
Example 3: `head = [1,100000]` → Output: `100001`

Constraints: number of nodes `n`, `2 <= n <= 10^5`, `n` is even, `1 <= Node.val <= 10^5`

```
# Status:
# Time taken: ___ min
# Tier:
# Time complexity: O(?)
# Space complexity: O(?)
# LC status:
# Pattern:
# Variant:
# mistakes/confusion:
```

---
## Daily Summary
New: 3 | Tier1: 3 | Tier2: 0 | Tier3: 2 | Tier4: 2 | Total: 10

## Mandatory Closing Check
# Prompt 1 (End of Day agent) run: Yes
# STATUS.md updated: Yes

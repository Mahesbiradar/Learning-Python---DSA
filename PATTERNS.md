# PATTERNS — Concept Blocks

Agent: when introducing any pattern below for the first time, include the FULL block in the daily file.
For reinforcement days, include only the Code Template section as the warm-up.

---

## PATTERN: Frequency Hashing
**Trigger words:** frequency, most common, appears k times, first unique, character count, anagram check, how many times, duplicate detection
**Mental model:** Count first. Answer in second pass. Never answer while counting.

**Why it exists:**
Brute force scans input for every query → O(n²). Pre-counting converts lookup to O(1) → O(n) total.

**State:** `freq = {element: count}`

**Common mistakes:**
1. `char not in some_string` inside a loop — string membership is O(k). Use `char not in freq_dict`
2. Second pass over `freq.items()` — you lose original order. Always second pass over original sequence
3. `freq[x] += 1` crashes on missing key. Use `freq.get(x, 0) + 1`
4. Comparing maps when one has extra keys — check length first then compare

**Dry run — First Unique in "leetcode":**
Pass 1: `{l:1, e:2, t:1, c:1, o:1, d:1}`
Pass 2 over "leetcode": l → count=1 → return index 0

**Template:**
```python
freq = {}
for x in items:
    freq[x] = freq.get(x, 0) + 1
for i, x in enumerate(items):
    if freq[x] == 1:
        return i
return -1
```
Time: O(n) | Space: O(n)

---

## PATTERN: Grouping Hash Maps
**Trigger words:** group together, same characters, anagram of each other, rearranged letters, classify strings, bucket by key
**Mental model:** Compute a canonical key. Group members by that key.

**Why it exists:**
Brute force compares every pair → O(n² × k). One canonical key per element → O(n × k log k).

**State:** `groups = {canonical_key: [list of members]}`

**Common mistakes:**
1. Returning `groups.values()` — not a list. Use `list(groups.values())`
2. `sorted(word)` returns a list which is not hashable. Always `"".join(sorted(word))`
3. Using list directly as key — unhashable. Use tuple or join to string

**Dry run — Group Anagrams on ["eat","tea","tan","ate"]:**
"eat" → "aet" → groups["aet"] = ["eat"]
"tea" → "aet" → groups["aet"] = ["eat","tea"]
"tan" → "ant" → groups["ant"] = ["tan"]
"ate" → "aet" → groups["aet"] = ["eat","tea","ate"]
Return: `list(groups.values())`

**Template:**
```python
groups = {}
for word in words:
    key = "".join(sorted(word))
    if key not in groups:
        groups[key] = []
    groups[key].append(word)
return list(groups.values())
```
Time: O(n × k log k) | Space: O(n × k)

---

## PATTERN: Frequency Sorting
**Trigger words:** top k frequent, k most common, sort by frequency, most frequent elements, kth most frequent
**Mental model:** Count then rank. Two separate steps, never combined.

**Why it exists:**
Can't rank without counts. Sort step is separate from count step.

**State Phase 1:** `freq = {element: count}`
**State Phase 2:** sorted by count descending

**Common mistakes:**
1. Writing O(n log n) — precise form is O(n + m log m) where m = unique values
2. Sorting ascending when you want most-frequent-first — use `-freq[x]` or `reverse=True`

**Dry run — Top K, nums=[1,1,1,2,2,3], k=2:**
Count: {1:3, 2:2, 3:1}
Sort descending: [(1,3),(2,2),(3,1)]
Take first k=2: [1, 2]

**Template — Sorting version (learn first):**
```python
freq = {}
for x in nums:
    freq[x] = freq.get(x, 0) + 1
sorted_by_freq = sorted(freq.keys(), key=lambda x: -freq[x])
return sorted_by_freq[:k]
```
Time: O(n + m log m) | Space: O(n)

---

## PATTERN: Complement Lookup
**Trigger words:** two numbers that add up to, find pair with sum, return indices of two elements, target sum
**Mental model:** For each x, check if (target - x) was seen before. Check first, then store.

**Why it exists:**
Brute force checks all pairs → O(n²). Hash map turns complement check to O(1) → O(n).

**State:** `seen = {element_value: index_in_input}`

**Common mistakes:**
1. Storing `needed = target - x` as the key — the next element won't find its complement
2. Storing BEFORE checking — allows using same element twice. Always check then store
3. Returning values instead of indices

**Dry run — nums=[2,7,11,15], target=9:**
i=0, x=2: needed=7. Not in seen. seen={2:0}
i=1, x=7: needed=2. 2 IS in seen at index 0. Return [0,1]

**Template:**
```python
seen = {}
for i, x in enumerate(nums):
    needed = target - x
    if needed in seen:
        return [seen[needed], i]
    seen[x] = i  # Store AFTER checking
```
Time: O(n) | Space: O(n)

---

## PATTERN: Prefix Sum
**Trigger words:** running sum, left sum equals right sum, equilibrium index, pivot index, subarray sum, product except self, cumulative sum
**Mental model:** Accumulate from left. Derive right sum without rescanning.

**Critical rule for Pivot Index:**
Step 1: right_sum = total - left_sum - nums[i]
Step 2: if left_sum == right_sum → return i
Step 3: left_sum += nums[i]  ← UPDATE AFTER comparing

**Common mistakes:**
1. Adding nums[i] to left_sum BEFORE comparing — wrong answer
2. Returning 0 instead of -1 when no pivot exists — always test [1,2,3] → -1
3. Product: building two O(n) arrays — use output array + one suffix variable

**Dry run — Pivot on [1,7,3,6,5,6], total=28:**
i=0: right=28-0-1=27. 0≠27. left=1
i=1: right=28-1-7=20. 1≠20. left=8
i=2: right=28-8-3=17. 8≠17. left=11
i=3: right=28-11-6=11. 11==11 → return 3

**Template:**
```python
total = sum(nums)
left_sum = 0
for i, x in enumerate(nums):
    right_sum = total - left_sum - x
    if left_sum == right_sum:
        return i
    left_sum += x
return -1
```
Time: O(n) | Space: O(1)

---

## PATTERN: Two Pointers
**Trigger words:** reverse in-place, palindrome, remove elements, keep order, return new length, is subsequence, skip non-alphanumeric, compact array, find pair in sorted array
**Mental model:** Two indexes moving toward each other or in same direction. Avoids O(n²) pair checking.

**Common mistakes:**
1. Palindrome skip loops: inner while MUST be guarded with `left < right` — all-punctuation string causes infinite loop
2. Subsequence wrong instinct: `if char in s` checks membership not order. Always advance s_ptr sequentially
3. Write pointer: advances only when valid element written, not every iteration

**Template — Palindrome with skip loops:**
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

**Template — Subsequence match pointer:**
```python
s_ptr = 0
for char in t:
    if s_ptr < len(s) and s[s_ptr] == char:
        s_ptr += 1
return s_ptr == len(s)
```
Time: O(n) | Space: O(1)

---

## PATTERN: Running-State Tracking
**Trigger words:** maximum profit, buy and sell, best time, minimum price so far, running maximum, one transaction allowed
**Mental model:** Track best outcome so far with one or two variables. Update monotonically.

**Common mistakes:**
1. `min_price = 0` — fails when all prices are large. Use `nums[0]`
2. Updating max_profit before checking if price is a new minimum

**Dry run — [7,1,5,3,6,4]:**
min=7, profit=0
price=1: 1<7 → min=1
price=5: 5-1=4 > 0 → profit=4
price=6: 6-1=5 > 4 → profit=5
Return 5

**Template:**
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
Time: O(n) | Space: O(1)

---

## PATTERN: Sliding Window (intro)
**Trigger words:** continuous subarray, longest substring, minimum window, at most k distinct, exactly k
**Mental model:** Maintain a window [left, right]. Expand right, shrink left when condition violated.

**Two types:**
- Fixed size: window = k, slide one step at a time
- Variable size: expand until invalid, shrink from left

**Template — Variable window:**
```python
left = 0
window = {}  # or set
result = 0
for right in range(len(s)):
    # add s[right] to window
    while window_is_invalid:
        # remove s[left] from window
        left += 1
    result = max(result, right - left + 1)
return result
```
Time: O(n) | Space: O(k) where k = window size

---

## PATTERN: Write Pointer
**Trigger words:** in-place, remove, keep order, return new length, compact array, move elements
**Mental model:** One read pointer scans. One write pointer marks next valid position.

**Template:**
```python
write = 0
for read in range(len(nums)):
    if valid_condition(nums[read]):
        nums[write] = nums[read]
        write += 1
return write
```
Time: O(n) | Space: O(1)

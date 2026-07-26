---

# Day 46 — 24 July 2026 — Learning Day

Focus: Stack — Monotonic Stack (Next Greater Element) + Basic Stack reinforcement

Phase: Stack + Queue — Volume Building

Daily Target: 11 Problems

---

## SOP Reminder (2 min before every problem)

Read → Restate → Identify Pattern → Plan in Words → Dry Run → Code → Test → Submit

---

## Tier 4 Recalls (5 min each)

Write the template from memory.

1. Running State / Kadane — min-max product tracking
2. Two Pointers — Opposite Ends

---

## Tier 1 — Priority Revision

### 1. Valid Parentheses (LC 20)

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1:**
```
Input: s = "()"
Output: true
```

**Example 2:**
```
Input: s = "()[]{}"
Output: true
```

**Example 3:**
```
Input: s = "(]"
Output: false
```

**Constraints:**
- `1 <= s.length <= 10^4`
- `s[i]` is a parenthesis `'('`, `')'`, `'{'`, `'}'`, `'['` or `']'`.

# Status: ___
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

### 2. Min Stack (LC 155)

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

**Example 1:**
```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

**Constraints:**
- `-2^31 <= val <= 2^31 - 1`
- Methods `pop`, `top` and `getMin` operations will always be called on non-empty stacks.
- At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`.

# Status: ___
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

## Tier 3 — Revision (6 Problems)

### 3. Find Minimum in Rotated Sorted Array (LC 153)

Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated `4` times.
- `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return the minimum element of this array.

You must write an algorithm that runs in `O(log n)` time.

**Example 1:**
Input: nums = [3,4,5,1,2]
Output: 1

**Example 2:**
Input: nums = [4,5,6,7,0,1,2]
Output: 0

**Example 3:**
Input: nums = [11,13,15,17]
Output: 11

**Constraints:**
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are **unique**.
- `nums` is sorted and rotated between `1` and `n` times.

# Status: ___
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

### 4. Find Peak Element (LC 162)

A peak element is an element that is strictly greater than its neighbors.

Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in `O(log n)` time.

**Example 1:**
Input: nums = [1,2,3,1]
Output: 2

**Example 2:**
Input: nums = [1,2,1,3,5,6,4]
Output: 5

**Constraints:**
- `1 <= nums.length <= 1000`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `nums[i] != nums[i + 1]` for all valid `i`.

# Status: ___
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

### 5. Range Sum Query - Immutable (LC 303)

Given an integer array `nums`, handle multiple queries of the following type:

1. Calculate the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** where `left <= right`.

Implement the `NumArray` class:

- `NumArray(int[] nums)` Initializes the object with the integer array `nums`.
- `int sumRange(int left, int right)` Returns the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** (i.e. `nums[left] + nums[left + 1] + ... + nums[right]`).

**Example 1:**
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

**Constraints:**
- `1 <= nums.length <= 10^4`
- `-10^5 <= nums[i] <= 10^5`
- `0 <= left <= right < nums.length`
- At most `10^4` calls will be made to `sumRange`.

# Status: ___
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

### 6. Two Sum (LC 1)

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have **exactly one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

**Example 1:**
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

**Example 2:**
Input: nums = [3,2,4], target = 6
Output: [1,2]

**Example 3:**
Input: nums = [3,3], target = 6
Output: [0,1]

**Constraints:**
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- **Only one valid answer exists.**

# Status: ___
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

### 7. Valid Perfect Square (LC 367)

Given a positive integer `num`, return `true` *if* `num` *is a perfect square or* `false` *otherwise*.

A **perfect square** is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as `sqrt`.

**Example 1:**
Input: num = 16
Output: true

**Example 2:**
Input: num = 14
Output: false

**Constraints:**
- `1 <= num <= 2^31 - 1`

# Status: ___
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

### 8. Ransom Note (LC 383)

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

**Example 1:**
Input: ransomNote = "a", magazine = "b"
Output: false

**Example 2:**
Input: ransomNote = "aa", magazine = "ab"
Output: false

**Example 3:**
Input: ransomNote = "aa", magazine = "aab"
Output: true

**Constraints:**
- `1 <= ransomNote.length, magazine.length <= 10^5`
- `ransomNote` and `magazine` consist of lowercase English letters.

# Status: ___
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

## New Problems — Monotonic Stack (1 Problem)

### Learning Block — Monotonic Stack Pattern

**Where to learn:** NeetCode → Stack section → "Daily Temperatures" concept video

**Trigger words:** next greater element, previous smaller element, next warmer day, span of days, nearest greater to left/right, trapping rain water

**Mental model:**
Imagine you are looking at a row of buildings from left to right. For each building, you want to know: "When I look to my right, which is the first building that is taller than me?" You could scan right every time — that is O(n²). Instead, use a stack as a "deck of cards" that you keep in decreasing order of height. As you walk left-to-right, you pop shorter buildings off the stack because you have found their answer (the current building). The stack always holds buildings whose "next greater" has not been found yet.

**Why this pattern exists:**
Brute force for "next greater element" is O(n²) because for every element you scan the rest of the array. The monotonic stack collapses this to O(n) by remembering, in stack order, which elements are still waiting for their answer. Each element is pushed once and popped once.

**Blank template:**
```python
def monotonic_stack(arr):
    stack = []  # stores indices or values, monotonically decreasing
    result = [0] * len(arr)
    
    for i in range(len(arr)):
        # While current element breaks the monotonic property
        while stack and condition(stack[-1], arr[i]):
            # Pop and process — the current element is the "answer" for popped item
            top = stack.pop()
            result[top] = i - top  # or arr[i], depending on problem
        
        stack.append(i)
    
    # Elements still in stack have no greater element to their right
    for remaining in stack:
        result[remaining] = 0  # or -1, or len(arr) - remaining
    
    return result
```

**Dry run — Daily Temperatures style:**
Temperatures: [73, 74, 75, 71, 69, 72, 76, 73]
- i=0, stack=[], push 0 → stack=[0]
- i=1, T[1]=74 > T[0]=73, pop 0, result[0]=1-0=1, push 1 → stack=[1]
- i=2, T[2]=75 > T[1]=74, pop 1, result[1]=2-1=1, push 2 → stack=[2]
- i=3, T[3]=71 < T[2]=75, push 3 → stack=[2,3]
- i=4, T[4]=69 < T[3]=71, push 4 → stack=[2,3,4]
- i=5, T[5]=72 > T[4]=69, pop 4, result[4]=5-4=1; T[5]=72 > T[3]=71, pop 3, result[3]=5-3=2; T[5]=72 < T[2]=75, push 5 → stack=[2,5]
- i=6, T[6]=76 > T[5]=72, pop 5, result[5]=6-5=1; T[6]=76 > T[2]=75, pop 2, result[2]=6-2=4; stack empty, push 6 → stack=[6]
- i=7, T[7]=73 < T[6]=76, push 7 → stack=[6,7]
- End: result[6]=0, result[7]=0 (no warmer day)
Result: [1, 1, 4, 2, 1, 1, 0, 0] ✓

**Common mistakes:**
- Pushing values instead of indices — you need indices to compute distance (days difference)
- Using `>=` instead of `>` in the while condition — this changes behavior for equal elements
- Forgetting to process remaining elements in the stack at the end
- Confusing monotonically decreasing vs increasing — decreasing stack finds NEXT GREATER, increasing finds NEXT SMALLER
- Off-by-one in result calculation (using `i` instead of `i - stack[-1]` for distance)

---

### 9. Daily Temperatures (LC 739)

Given an array of integers `temperatures` represents the daily temperatures, return *an array* `answer` *such that* `answer[i]` *is the number of days you have to wait after the* `ith` *day to get a warmer temperature*. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

**Example 1:**
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

**Example 2:**
```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

**Example 3:**
```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

**Constraints:**
- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

# Status: ___
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

---

## Daily Summary

New: 1 | Tier1: 2 | Tier2: 0 | Tier3: 6 | Tier4: 2 | Total: 11


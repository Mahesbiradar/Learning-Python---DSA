# 🔹 Problem: Move Zeros to End

## 🧠 Pattern:

Two Pointer / Position Tracking

---

## 📥 Input:

nums = [0,1,0,3,12]

## 📤 Output:

[1,3,12,0,0]

---

## 🔍 Transformation:

Move all non-zero elements to the front while maintaining order, then fill remaining positions with zeros.

---

## 🪜 Logic (Step-by-Step):

1. Initialize a pointer:

   * pos = 0 (position to place next non-zero)

2. Traverse the list:

   * If element is non-zero:

     * Place it at nums[pos]
     * Increment pos

3. After traversal:

   * Fill remaining indices (pos → end) with 0

---

## 💻 Code:

```python
nums = [0,1,0,3,12]

pos = 0

for i in nums:
    if i != 0:
        nums[pos] = i
        pos += 1

for i in range(pos, len(nums)):
    nums[i] = 0

print(nums)
```

---

## 🔁 Dry Run:

Input:
[0,1,0,3,12]

Step 1 (move non-zero):
→ [1,3,12, ?, ?]
pos = 3

Step 2 (fill zeros):
→ [1,3,12,0,0]

---

## ⚠️ Mistakes:

* ❌ Trying to swap zeros directly
* ❌ Not maintaining order of elements
* ❌ Forgetting to fill remaining positions
* ❌ Confusing index vs value in loop

---

## ⏱️ Time Complexity:

O(n)

## 💾 Space Complexity:

O(1)

---

## 🧠 Key Concept:

* Move valid elements first
* Fill remaining space later
* Two-pointer thinking

---

## 🔥 Interview Line:

“I use a position pointer to place non-zero elements in order, then fill the rest of the array with zeros, achieving O(n) time and O(1) space.”

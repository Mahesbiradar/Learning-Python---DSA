# 🔹 Problem: Reverse Array (In-Place)

## 🧠 Pattern:

Two Pointer Technique

---

## 📥 Input:

nums = [1,2,3,4,5]

## 📤 Output:

[5,4,3,2,1]

---

## 🔍 Transformation:

Swap elements from both ends moving towards the center.

---

## 🪜 Logic (Step-by-Step):

1. Initialize two pointers:

   * left = 0
   * right = len(nums) - 1

2. While left < right:

   * Swap nums[left] and nums[right]
   * Increment left
   * Decrement right

3. Stop when pointers meet or cross

---

## 💻 Code:

```python
nums = [1,2,3,4,5]

left = 0
right = len(nums) - 1

while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1

print(nums)
```

---

## 🔁 Dry Run (Example):

Step 1:
[1,2,3,4,5] → swap(0,4) → [5,2,3,4,1]

Step 2:
[5,2,3,4,1] → swap(1,3) → [5,4,3,2,1]

Stop (left >= right)

---

## ⚠️ Mistakes:

* ❌ Using:
  nums[left] = nums[right]
  nums[right] = nums[left]
  → leads to data loss

* ❌ Forgetting to move pointers

* ❌ Using extra array (not in-place)

---

## ⏱️ Time Complexity:

O(n)

## 💾 Space Complexity:

O(1)

---

## 🧠 Key Concept:

* In-place swapping
* Two pointer movement
* Symmetric element handling

---

## 🔥 Interview Line:

“I use a two-pointer approach to swap elements from both ends and move inward, achieving in-place reversal in O(n) time and O(1) space.”

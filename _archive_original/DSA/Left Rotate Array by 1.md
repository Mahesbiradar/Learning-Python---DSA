# 🔹 Problem: Left Rotate Array by 1

## 🧠 Pattern:

Element Shifting

---

## 📥 Input:

nums = [1,2,3,4,5]

## 📤 Output:

[2,3,4,5,1]

---

## 🔍 Transformation:

Shift all elements one position to the left and move the first element to the end.

---

## 🪜 Logic (Step-by-Step):

1. Store the first element
   first = nums[0]

2. Shift all elements to the left:

   * nums[i] = nums[i+1]

3. Place the stored element at the end:

   * nums[n-1] = first

---

## 💻 Code:

```python id="2h7p0f"
nums = [1,2,3,4,5]

first = nums[0]

for i in range(len(nums) - 1):
    nums[i] = nums[i + 1]

nums[len(nums) - 1] = first

print(nums)
```

---

## 🔁 Dry Run:

Step 1:
[1,2,3,4,5] → store first = 1

Step 2 (shifting):
[2,2,3,4,5]
[2,3,3,4,5]
[2,3,4,4,5]
[2,3,4,5,5]

Step 3:
[2,3,4,5,1]

---

## ⚠️ Mistakes:

* ❌ Ending loop at wrong index
  → must run till len(nums) - 1

* ❌ Forgetting to store first element

* ❌ Overwriting data without backup

---

## ⏱️ Time Complexity:

O(n)

## 💾 Space Complexity:

O(1)  ✅ (in-place)

---

## 🧠 Key Concept:

* Shifting elements
* Preserving overwritten value
* In-place modification

---

## 🔥 Interview Line:

“I store the first element, shift all elements left, and place the stored value at the end. This is done in O(n) time and O(1) space.”



"""

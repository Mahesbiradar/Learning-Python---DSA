# 🔹 Problem: Check Palindrome Array

## 🧠 Pattern:

Two Pointer Technique

---

## 📥 Input:

nums = [1,2,3,2,1]

## 📤 Output:

True

---

## 🔍 Transformation:

Check whether elements from both ends are equal while moving towards the center.

---

## 🪜 Logic (Step-by-Step):

1. Initialize two pointers:

   * left = 0
   * right = len(nums) - 1

2. While left < right:

   * Compare nums[left] and nums[right]
   * If not equal → return False
   * Else → move pointers inward

     * left += 1
     * right -= 1

3. If loop completes → return True

---

## 💻 Code:

```python
nums = [1,2,3,2,1]

left = 0
right = len(nums) - 1

is_palindrome = True

while left < right:
    if nums[left] != nums[right]:
        is_palindrome = False
        break
    
    left += 1
    right -= 1

print(is_palindrome)
```

---

## 🔁 Dry Run:

Step 1:
[1,2,3,2,1] → compare 1 & 1 ✔

Step 2:
compare 2 & 2 ✔

Step 3:
middle reached → stop

Output → True

---

## ⚠️ Mistakes:

* ❌ Not stopping when mismatch occurs
* ❌ Incorrect pointer movement
* ❌ Using extra space unnecessarily
* ❌ Not handling single element case

---

## ⏱️ Time Complexity:

O(n)

## 💾 Space Complexity:

O(1)

---

## 🧠 Key Concept:

* Symmetric comparison
* Two pointer inward movement
* Early exit optimization

---

## 🔥 Interview Line:

“I use a two-pointer approach to compare elements from both ends. If any mismatch occurs, the array is not a palindrome. Otherwise, it is.”

"""

# 🔥 DAY 4 PROBLEMS

---





---



---

## 🔹 4. Find Missing Numbers (Multiple)

```python
nums = [1,3,5]
n = 5
# Output: [2,4]
```
👉 Same idea as missing number:

Loop 1 → expected values
Loop 2 → check existence

👉 Pattern: Existence Check

---

## 🔹 5. Move All Negatives to Front

```python
nums = [1,-2,3,-4,5]
# Output: [-2,-4,1,3,5]
```
🔹 5. Move Negatives to Front

👉 Same pattern as:

Move zeros → but now condition is < 0

👉 Pattern: Two Pointer (Partition)

---

## 🔹 6. Find Pair with Given Sum (Basic)

```python
nums = [2,7,11,15]
target = 9
# Output: (2,7)
```
👉 Think:

Check every pair
i + j == target

👉 Pattern: Nested Loop

"""


## 🔹 1. Check if Array is Strictly Increasing


# nums = [1,2,3,4] #→ True
# nums = [1,2,2,3] #→ False


#👉 Difference from sorted:

#* Here duplicates NOT allowed

#nums[i] < nums[i+1]  (not <=)

#👉 Pattern: Adjacent Comparison

## 🔹 2. Find First Duplicate Element

nums = [1,2,3,2,4]
# Output: 2

seen=[]
is_Seen=True

for i in nums:
    for j in seen:
        if i==j:
            print(i)
            is_Seen=False
            break
    if not is_Seen:
        break
    seen.append(i)

# Existence Check
#Here we have to Check The First Duplicate element and if found we have to exit from the Loop so Here i have run a Loop and nested loop to check the existance with new list and initialize one bool variable to trcak.


## 🔹 3. Find All Duplicates

nums = [1,2,2,3,3,4]
# Output: [2,3]
duplicates=[]


#Pattern: Nested Loop / Tracking


# Don’t add duplicates multiple times
# Use another list to track duplicates


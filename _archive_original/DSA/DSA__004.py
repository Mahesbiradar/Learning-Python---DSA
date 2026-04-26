# Tuple practice

# t = (10, 20, 30, 40)

# count = 0
# for i in t:
#     print(i)
#     count += 1

# print(count)

# t = (1, 2, 3, 4)
# x = 3

# print(x in t)

# max_value = t[0]

# for i in t:
#     if i > max_value:
#         max_value = i
# print(max_value)

# 5. Reverse tuple (NO slicing)
# t = (1, 2, 3, 4)
# new_t = ()

# for i in t:
#     new_t = (i,) + new_t
# print(new_t)

# 6. Count occurrences (NO count())

# t = (1, 2, 3, 4, 2)
# target = 2
# count = 0
# for i in t:
#     if i == target:
#         count += 1
# print(count)

# 7. Remove Duplicates (NO built-in)

# t = (1, 2, 2, 3, 1)
# new = ()

# for i in t:
#     found = False

#     for j in new:
#         if i == j:
#             found = True
#             break
#     if not found:
#         new = new + (i,)

# print(new)

# 8. Merge Two Tuples (NO direct +)

# t1 = (1, 2)
# t2 = (3, 4)

# merged = ()

# for i in t1:
#     merged = merged + (i,)
# for j in t2:
#     merged = merged + (j,)

# print(merged)

# 9. Second Largest Element

# t = (5, 1, 8, 3, 8)

# first = second = float("-inf")

# for i in t:
#     if i > first:
#         second = first
#         first = i
#     elif i > second and i != first:
#         second = i

# print(second)

# 1. Swap two numbers using unpacking

a = 10
b = 15
a, b = b, a
print(a, b)

# 2. Unpack and print

t = (10, 20, 30)

x, y, z = t

print(f"x:{x},y:{y},z:{z}")

# 3. Loop unpacking

pairs = [(1, 2), (3, 4), (5, 6)]

a, b, c = pairs

print(sum(a))
print(sum(b))
print(sum(c))

# 4. Ignore middle value
t = (1, 2, 3)

a, _, b = t

print(a, b)

# 5. Use * unpacking

t = (1, 2, 3, 4, 5)

a, *b, c = t
print(f"a={a},b={b},c={c}")

# 6. Nested unpacking

t = ((1, 2), (3, 4))

((x1, y1), (x2, y2)) = t

print(x1, y1, x2, y2)

# Quick Fix Exercise
pairs = [(2, 3), (4, 5), (6, 7)]

for a, b in pairs:
    print(a * b)

# Q1
a, b = (1, 2)
a = a + b
print(a, b)

# Q2
a, *b = (1, 2)
print(b)

# Q3

# for x, y in [(1, 2, 3), (4, 5, 6)]:
#     print(x, y)

# ValueError: too many values to unpack


# Day 4 array prompts

"""
1. Check if Array is Strictly Increasing

nums = [1, 2, 3, 4] -> True
nums = [1, 2, 2, 3] -> False

Difference from sorted:
- Duplicates are not allowed.
- Compare nums[i] < nums[i + 1].

Pattern: Adjacent Comparison

2. Find First Duplicate Element

nums = [1, 2, 3, 2, 4]
Output: 2

Pattern: Existence Check

3. Find All Duplicates

nums = [1, 2, 2, 3, 3, 4]
Output: [2, 3]

Pattern: Nested Loop / Tracking

4. Find Missing Numbers (Multiple)

nums = [1, 3, 5]
n = 5
Output: [2, 4]

Pattern: Existence Check

5. Move All Negatives to Front

nums = [1, -2, 3, -4, 5]
Output: [-2, -4, 1, 3, 5]

Pattern: Two Pointer / Partition

6. Find Pair with Given Sum

nums = [2, 7, 11, 15]
target = 9
Output: (2, 7)

Pattern: Nested Loop
"""

nums = [1, 2, 3, 2, 4]
seen = []
is_seen = True

for i in nums:
    for j in seen:
        if i == j:
            print(i)
            is_seen = False
            break
    if not is_seen:
        break
    seen.append(i)

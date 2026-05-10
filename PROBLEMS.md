# Python + DSA Problems

## Arrays / Lists

## [ARR-001] Print Elements

Status: Solved  
Topic: Arrays / Lists  
Pattern: Linear Traversal  
Difficulty: Easy

### Problem

Print every element in a list.

### Approach

1. Loop through each value.
2. Print the current value.

### Code

```python
nums = [10, 20, 30, 40]

for num in nums:
    print(num)
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

Use value traversal when the index is not needed.

## [ARR-002] Sum of List

Status: Solved  
Topic: Arrays / Lists  
Pattern: Linear Traversal  
Difficulty: Easy

### Problem

Find the sum of all numbers in a list.

### Approach

1. Start `total` at `0`.
2. Add each number to `total`.
3. Print the final total.

### Code

```python
nums = [10, 20, 30]
total = 0

for num in nums:
    total += num

print(total)
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

Avoid naming the variable `sum` because it shadows Python's built-in `sum()`.

## [ARR-003] Count Even Numbers

Status: Solved  
Topic: Arrays / Lists  
Pattern: Linear Traversal  
Difficulty: Easy

### Problem

Count how many even numbers are present in a list.

### Approach

1. Start `count` at `0`.
2. Traverse the list.
3. If a number is divisible by `2`, increment `count`.

### Code

```python
nums = [1, 2, 3, 4, 5, 6]
count = 0

for num in nums:
    if num % 2 == 0:
        count += 1

print(count)
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

Modulo `%` is commonly used for even/odd checks.

## [ARR-004] Find Maximum Element

Status: Solved  
Topic: Arrays / Lists  
Pattern: Linear Traversal  
Difficulty: Easy

### Problem

Find the largest element in a list.

### Approach

1. Assume the first value is the maximum.
2. Traverse the list.
3. If a larger value is found, update `max_value`.

### Code

```python
nums = [3, 7, 2, 9, 5]
max_value = nums[0]

for num in nums:
    if num > max_value:
        max_value = num

print(max_value)
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

Do not initialize with `0` because it fails for all-negative lists.

## [ARR-005] Find Minimum Element

Status: Solved  
Topic: Arrays / Lists  
Pattern: Linear Traversal  
Difficulty: Easy

### Problem

Find the smallest element in a list.

### Approach

1. Assume the first value is the minimum.
2. Traverse the list.
3. If a smaller value is found, update `min_value`.

### Code

```python
nums = [3, 7, 2, 9, 5]
min_value = nums[0]

for num in nums:
    if num < min_value:
        min_value = num

print(min_value)
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

Initialize from the list, not from a guessed value.

## [ARR-006] Search Element

Status: Solved  
Topic: Arrays / Lists  
Pattern: Linear Search  
Difficulty: Easy

### Problem

Check whether a target exists in a list.

### Approach

1. Traverse the list.
2. If the current value equals the target, mark it found and stop.
3. Print the result.

### Code

```python
nums = [10, 20, 30, 40]
target = 25
found = False

for num in nums:
    if num == target:
        found = True
        break

print("Found" if found else "Not Found")
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

Use `break` for early exit once the target is found.

## [ARR-007] Square Numbers

Status: Solved  
Topic: Arrays / Lists  
Pattern: Transformation  
Difficulty: Easy

### Problem

Create a new list containing the square of each number.

### Approach

1. Create an empty result list.
2. Traverse the numbers.
3. Append `num * num` to the result.

### Code

```python
nums = [1, 2, 3, 4]
squares = []

for num in nums:
    squares.append(num * num)

print(squares)
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

This keeps the original list unchanged.

## [ARR-008] Square Only Positive Numbers

Status: Solved  
Topic: Arrays / Lists  
Pattern: Filtering + Transformation  
Difficulty: Easy

### Problem

Create a list of squares for only positive numbers.

### Approach

1. Traverse the list.
2. Keep only values greater than `0`.
3. Square and collect them.

### Code

```python
nums = [-2, -1, 0, 1, 2]
squares = [num * num for num in nums if num > 0]

print(squares)
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

Expected output: `[1, 4]`.

## [ARR-009] Filter Even Numbers

Status: Solved  
Topic: Arrays / Lists  
Pattern: Filtering  
Difficulty: Easy

### Problem

Create a new list containing only even numbers.

### Approach

1. Traverse the list.
2. Check whether each number is even.
3. Append even numbers to the result.

### Code

```python
nums = [1, 2, 3, 4, 5, 6]
even_numbers = []

for num in nums:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

Filtering is a common beginner transformation pattern.

## [ARR-010] Square Even Numbers

Status: Solved  
Topic: Arrays / Lists  
Pattern: Filtering + Transformation  
Difficulty: Easy

### Problem

Create a new list containing squares of only even numbers.

### Approach

1. Traverse the list.
2. If a number is even, square it.
3. Append it to the result.

### Code

```python
nums = [1, 2, 3, 4, 5, 6]
result = []

for num in nums:
    if num % 2 == 0:
        result.append(num * num)

print(result)
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

Combine condition and transformation carefully.

## [ARR-011] Even Square, Odd Cube

Status: Solved  
Topic: Arrays / Lists  
Pattern: Conditional Transformation  
Difficulty: Easy

### Problem

For each number, square it if it is even and cube it if it is odd.

### Approach

1. Traverse the list.
2. Use a condition to decide the operation.
3. Append the transformed value.

### Code

```python
nums = [1, 2, 3, 4, 5, 6]
result = []

for num in nums:
    if num % 2 == 0:
        result.append(num * num)
    else:
        result.append(num * num * num)

print(result)
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

This is useful practice for conditional expressions.

## [ARR-012] Count Even and Odd Numbers

Status: Solved  
Topic: Arrays / Lists  
Pattern: Counting  
Difficulty: Easy

### Problem

Count how many even and odd numbers are present.

### Approach

1. Start `even_count` and `odd_count` at `0`.
2. Traverse the list.
3. Increment the correct counter.

### Code

```python
nums = [1, 2, 3, 4, 5, 6]
even_count = 0
odd_count = 0

for num in nums:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Even: {even_count}")
print(f"Odd: {odd_count}")
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

Multiple counters are common in frequency-style problems.

## [ARR-013] Check All Even

Status: Solved  
Topic: Arrays / Lists  
Pattern: Linear Traversal  
Difficulty: Easy

### Problem

Check whether every number in the list is even.

### Approach

1. Traverse the list.
2. If any odd number is found, stop.
3. If the loop completes, all numbers are even.

### Code

```python
nums = [2, 4, 6, 8]

for num in nums:
    if num % 2 != 0:
        print("NOT ALL EVEN")
        break
else:
    print("ALL EVEN")
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

The `else` block runs only if the loop does not break.

## [ARR-014] First Odd Number

Status: Solved  
Topic: Arrays / Lists  
Pattern: Linear Search  
Difficulty: Easy

### Problem

Find the first odd number in a list.

### Approach

1. Traverse the list.
2. Check if the current number is odd.
3. Print it and stop.

### Code

```python
nums = [2, 4, 6, 7, 8]

for num in nums:
    if num % 2 != 0:
        print(num)
        break
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

This is a direct use of early exit.

## [ARR-015] Reverse Array

Status: Solved  
Topic: Arrays / Lists  
Pattern: Two Pointer  
Difficulty: Easy

### Problem

Reverse a list in-place.

### Approach

1. Place one pointer at the start and one at the end.
2. Swap both values.
3. Move the pointers inward.
4. Stop when they meet or cross.

### Code

```python
nums = [1, 2, 3, 4, 5]

left = 0
right = len(nums) - 1

while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1

print(nums)
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

Tuple swapping avoids overwriting values.

## [ARR-016] Reverse Without Built-in

Status: Solved  
Topic: Arrays / Lists  
Pattern: Reverse Traversal  
Difficulty: Easy

### Problem

Create a reversed copy of a list without using built-in reverse methods.

### Approach

1. Start from the last index.
2. Move backward.
3. Append each value to a new list.

### Code

```python
nums = [1, 2, 3, 4]
reversed_nums = []

for i in range(len(nums) - 1, -1, -1):
    reversed_nums.append(nums[i])

print(reversed_nums)
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

This does not modify the original list.

## [ARR-017] Left Rotate Array by 1

Status: Solved  
Topic: Arrays / Lists  
Pattern: Element Shifting  
Difficulty: Easy

### Problem

Rotate the list left by one position.

### Approach

1. Store the first element.
2. Shift every element one position left.
3. Put the stored first element at the end.

### Code

```python
nums = [1, 2, 3, 4, 5]

first = nums[0]

for i in range(len(nums) - 1):
    nums[i] = nums[i + 1]

nums[-1] = first

print(nums)
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

Store the first element before it gets overwritten.

## [ARR-018] Move Zeros to End

Status: Solved  
Topic: Arrays / Lists  
Pattern: Two Pointer / Position Tracking  
Difficulty: Easy

### Problem

Move all zeros to the end while keeping non-zero values in order.

### Approach

1. Use `position` to track where the next non-zero value should go.
2. Move all non-zero values forward.
3. Fill the remaining positions with zero.

### Code

```python
nums = [0, 1, 0, 3, 12]
position = 0

for num in nums:
    if num != 0:
        nums[position] = num
        position += 1

for i in range(position, len(nums)):
    nums[i] = 0

print(nums)
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

This preserves the order of non-zero values.

## [ARR-019] Check Palindrome Array

Status: Solved  
Topic: Arrays / Lists  
Pattern: Two Pointer  
Difficulty: Easy

### Problem

Check whether a list reads the same forward and backward.

### Approach

1. Place one pointer at the start and one at the end.
2. Compare both values.
3. If any mismatch appears, it is not a palindrome.
4. Move inward until pointers meet.

### Code

```python
nums = [1, 2, 3, 2, 1]

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

### Complexity

Time: O(n)  
Space: O(1)

### Notes

Single-element and empty lists are palindromes by default.

## [ARR-020] Find Second Largest Element

Status: Solved  
Topic: Arrays / Lists  
Pattern: Tracking  
Difficulty: Easy

### Problem

Find the second largest distinct number in a list.

### Approach

1. Track `largest` and `second_largest`.
2. If a new largest is found, move the old largest to second largest.
3. Otherwise, update second largest when the value fits between both.

### Code

```python
nums = [10, 5, 8, 20, 15]

largest = nums[0]
second_largest = float("-inf")

for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif largest > num > second_largest:
        second_largest = num

print(second_largest)
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

Use `float("-inf")` so negative numbers are handled correctly.

## [ARR-021] Check if List is Sorted

Status: Solved  
Topic: Arrays / Lists  
Pattern: Adjacent Comparison  
Difficulty: Easy

### Problem

Check whether a list is sorted in non-decreasing order.

### Approach

1. Compare each value with the next value.
2. If any current value is greater than the next value, the list is not sorted.
3. Otherwise, it is sorted.

### Code

```python
nums = [1, 2, 3, 4, 5]
is_sorted = True

for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        is_sorted = False
        break

print(is_sorted)
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

Use index traversal because neighboring elements must be compared.

## [ARR-022] Remove Duplicates Without Set

Status: Solved  
Topic: Arrays / Lists  
Pattern: Existence Check  
Difficulty: Easy

### Problem

Remove duplicate values while preserving order without using a set.

### Approach

1. Create an empty result list.
2. Traverse each number.
3. Add it only if it is not already in the result.

### Code

```python
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = []

for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)

print(unique_nums)
```

### Complexity

Time: O(n^2)  
Space: O(n)

### Notes

This preserves order but is slower than a set-based solution.

## [ARR-023] Remove Duplicates Manual Nested Loop

Status: Solved  
Topic: Arrays / Lists  
Pattern: Nested Loops  
Difficulty: Easy

### Problem

Remove duplicates manually without using `in` on the result list.

### Approach

1. Traverse each number.
2. Search for it in the result list.
3. Append it only if not found.

### Code

```python
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = []

for num in nums:
    found = False
    for existing in unique_nums:
        if num == existing:
            found = True
            break
    if not found:
        unique_nums.append(num)

print(unique_nums)
```

### Complexity

Time: O(n^2)  
Space: O(n)

### Notes

The `found` flag must be reset for every number.

## [ARR-024] Find Missing Number

Status: Solved  
Topic: Arrays / Lists  
Pattern: Existence Check  
Difficulty: Easy

### Problem

Given numbers from `1` to `n` with one missing value, find the missing number.

### Approach

1. Set `n` to `len(nums) + 1`.
2. For each number from `1` to `n`, check if it exists.
3. Print the first missing number.

### Code

```python
nums = [1, 2, 4, 5]
n = len(nums) + 1

for candidate in range(1, n + 1):
    found = False
    for num in nums:
        if num == candidate:
            found = True
            break
    if not found:
        print(candidate)
        break
```

### Complexity

Time: O(n^2)  
Space: O(1)

### Notes

This is the manual nested-loop version. Hashing can improve it.

## [ARR-025] Count Frequency of Element

Status: Solved  
Topic: Arrays / Lists  
Pattern: Linear Traversal  
Difficulty: Easy

### Problem

Count how many times a target appears in a list.

### Approach

1. Start `count` at `0`.
2. Traverse the list.
3. Increment when the current value equals the target.

### Code

```python
nums = [1, 3, 4, 1, 5]
target = 1
count = 0

for num in nums:
    if num == target:
        count += 1

print(count)
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

This is the base pattern for frequency problems.

## [ARR-026] First Duplicate

Status: Solved  
Topic: Arrays / Lists  
Pattern: Hashing  
Difficulty: Easy

### Problem

Find the first duplicate value in a list.

### Approach

1. Keep a set of seen values.
2. Traverse the list.
3. If a value is already seen, print it and stop.
4. Otherwise, add it to the set.

### Code

```python
nums = [1, 2, 3, 4, 2, 5]
seen = set()

for num in nums:
    if num in seen:
        print(num)
        break
    seen.add(num)
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

Hashing makes duplicate detection efficient.

## [ARR-027] Flatten and Filter Matrix

Status: Solved  
Topic: Arrays / Lists  
Pattern: Nested Traversal  
Difficulty: Easy

### Problem

Flatten a matrix and keep only even numbers.

### Approach

1. Traverse each row.
2. Traverse each value in the row.
3. Keep only even values.

### Code

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
even_values = [value for row in matrix for value in row if value % 2 == 0]

print(even_values)
```

### Complexity

Time: O(r * c)  
Space: O(r * c)

### Notes

Expected output: `[2, 4, 6, 8]`.

## [ARR-028] Matrix Row Sum

Status: Solved  
Topic: Arrays / Lists  
Pattern: Nested Traversal  
Difficulty: Easy

### Problem

Find the sum of each row in a matrix.

### Approach

1. Traverse each row.
2. Sum values in that row.
3. Append the row sum to the result.

### Code

```python
matrix = [[1, 2], [3, 4], [5, 6]]
row_sums = []

for row in matrix:
    total = 0
    for value in row:
        total += value
    row_sums.append(total)

print(row_sums)
```

### Complexity

Time: O(r * c)  
Space: O(r)

### Notes

Avoid using `sum` as a variable name.

## [ARR-029] Pair Generation

Status: Solved  
Topic: Arrays / Lists  
Pattern: Nested Loops  
Difficulty: Easy

### Problem

Generate all pair products from two lists.

### Approach

1. Traverse the first list.
2. For each value, traverse the second list.
3. Print or store the product.

### Code

```python
list1 = [1, 2]
list2 = [3, 4]

for first in list1:
    for second in list2:
        print(first * second)
```

### Complexity

Time: O(n * m)  
Space: O(1)

### Notes

Nested loops are natural for pair generation.

## [ARR-030] Duplicate Detection Nested Loop

Status: Solved  
Topic: Arrays / Lists  
Pattern: Nested Loops  
Difficulty: Easy

### Problem

Detect whether a list contains duplicate values using nested loops.

### Approach

1. Pick each index `i`.
2. Compare it with every later index `j`.
3. If equal values are found, print the duplicate.

### Code

```python
nums = [1, 2, 3, 2]

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            print(f"Duplicate found: {nums[i]}")
            break
```

### Complexity

Time: O(n^2)  
Space: O(1)

### Notes

Use `j = i + 1` to avoid comparing an element with itself.

## [ARR-031] Two Sum

Status: Revisit  
Topic: Arrays / Lists  
Pattern: Hashing  
Difficulty: Easy

### Problem

Return indexes of two numbers that add up to the target.

### Approach

1. Store seen numbers with their indexes.
2. For each number, calculate the needed complement.
3. If the complement exists, return both indexes.
4. Otherwise, store the current number.

### Code

```python
nums = [2, 7, 11, 15]
target = 9
seen = {}

for i in range(len(nums)):
    current = nums[i]
    needed = target - current

    if needed in seen:
        print([seen[needed], i])
        break

    seen[current] = i
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

Store the current number after checking to avoid using the same element twice.

Day 03 review: brute force was correct, but the optimized version required solution help for the key storage line. Re-solve from memory before marking solved: check `needed = target - nums[i]`, then store `seen[nums[i]] = i`.

Day 04 review: brute force and optimized complement lookup were re-solved independently and passed local examples. Keep as `Revisit` until accepted on LeetCode and recalled again after 3 days.

## Strings

## [STR-001] Print Characters

Status: Solved  
Topic: Strings  
Pattern: Linear Traversal  
Difficulty: Easy

### Problem

Print every character in a string.

### Approach

1. Traverse the string.
2. Print each character.

### Code

```python
text = "Mahesh"

for char in text:
    print(char)
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

Strings can be traversed like lists.

## [STR-002] Count Vowels

Status: Solved  
Topic: Strings  
Pattern: Linear Traversal  
Difficulty: Easy

### Problem

Count the vowels in a string.

### Approach

1. Store vowels in a set.
2. Traverse the string.
3. Increment count when a character is a vowel.

### Code

```python
text = "python"
vowels = {"a", "e", "i", "o", "u"}
count = 0

for char in text.lower():
    if char in vowels:
        count += 1

print(count)
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

Use `.lower()` to handle uppercase vowels too.

## [STR-003] Reverse String

Status: Solved  
Topic: Strings  
Pattern: Reverse Traversal  
Difficulty: Easy

### Problem

Reverse a string without using slicing.

### Approach

1. Start from the last index.
2. Move backward.
3. Build the reversed string.

### Code

```python
text = "hello"
reversed_text = ""

for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]

print(reversed_text)
```

### Complexity

Time: O(n^2)  
Space: O(n)

### Notes

For large strings, use a list and `"".join()`.

## [STR-004] Reverse String Using Slicing

Status: Solved  
Topic: Strings  
Pattern: Slicing  
Difficulty: Easy

### Problem

Reverse a string using slicing.

### Approach

1. Use slice step `-1`.
2. Print the reversed string.

### Code

```python
text = "Python"
print(text[::-1])
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

This is Pythonic, but interviews may ask for a manual solution.

## [STR-005] Check Palindrome String

Status: Solved  
Topic: Strings  
Pattern: Two Pointer  
Difficulty: Easy

### Problem

Check whether a string reads the same forward and backward without slicing.

### Approach

1. Place one pointer at the start and one at the end.
2. Compare characters.
3. If a mismatch appears, it is not a palindrome.
4. Move inward.

### Code

```python
text = "madam"

left = 0
right = len(text) - 1
is_palindrome = True

while left < right:
    if text[left] != text[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

print(is_palindrome)
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

Two pointers avoid creating a reversed copy.

## [STR-006] First and Last Character

Status: Solved  
Topic: Strings  
Pattern: Indexing  
Difficulty: Easy

### Problem

Print the first and last character of a string.

### Approach

1. Use index `0` for the first character.
2. Use index `-1` for the last character.

### Code

```python
text = "Mahesh"

print(text[0], text[-1])
```

### Complexity

Time: O(1)  
Space: O(1)

### Notes

Check for empty strings before indexing in real code.

## [STR-007] Middle Part

Status: Solved  
Topic: Strings  
Pattern: Slicing  
Difficulty: Easy

### Problem

Remove the first and last character from a string.

### Approach

1. Slice from index `1`.
2. Stop before the last index.

### Code

```python
text = "Python"
middle = text[1:-1]

print(middle)
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

Slicing creates a new string.

## [STR-008] Remove Spaces

Status: Solved  
Topic: Strings  
Pattern: String Building  
Difficulty: Easy

### Problem

Remove all spaces from a string.

### Approach

1. Traverse each character.
2. Skip spaces.
3. Add non-space characters to the result.

### Code

```python
text = "I love Python"
result = []

for char in text:
    if char != " ":
        result.append(char)

print("".join(result))
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

Using a list plus `join()` is efficient for string building.

## [STR-009] Count Words

Status: Solved  
Topic: Strings  
Pattern: Linear Traversal  
Difficulty: Easy

### Problem

Count words in a string with extra spaces.

### Approach

1. Traverse by index.
2. A word starts when the current character is not a space and either it is index `0` or the previous character is a space.
3. Count each word start.

### Code

```python
text = "  I   love   Python  "
count = 0

for i in range(len(text)):
    if text[i] != " " and (i == 0 or text[i - 1] == " "):
        count += 1

print(count)
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

This handles leading, trailing, and multiple spaces.

## [STR-010] Count Words Starting With A

Status: Solved  
Topic: Strings  
Pattern: Linear Traversal  
Difficulty: Easy

### Problem

Count how many words start with the letter `a`.

### Approach

1. Traverse each word.
2. Check the first character.
3. Count words that start with `a`.

### Code

```python
words = ["apple", "banana", "avocado", "grape"]
count = 0

for word in words:
    if word and word[0].lower() == "a":
        count += 1

print(count)
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

The `word` check protects against empty strings.

## [STR-011] Remove Duplicates From String

Status: Solved  
Topic: Strings  
Pattern: Hashing / String Building  
Difficulty: Easy

### Problem

Remove duplicate characters while preserving order.

### Approach

1. Track characters already seen.
2. Traverse the string.
3. Add only new characters to the result.

### Code

```python
text = "programming"
seen = set()
result = []

for char in text:
    if char in seen:
        continue
    seen.add(char)
    result.append(char)

print("".join(result))
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

Expected output: `progamin`.

## [STR-012] Remove Consecutive Duplicates

Status: Solved  
Topic: Strings  
Pattern: Adjacent Comparison  
Difficulty: Easy

### Problem

Remove consecutive duplicate characters from a string.

### Approach

1. Handle the empty string.
2. Add the first character.
3. From the second character onward, add a character only if it differs from the previous character.

### Code

```python
text = "aaabbccdaa"

if text == "":
    result = ""
else:
    result = text[0]
    for i in range(1, len(text)):
        if text[i] != text[i - 1]:
            result += text[i]

print(result)
```

### Complexity

Time: O(n^2)  
Space: O(n)

### Notes

Expected output: `abcda`. For large strings, build with a list.

## [STR-013] First Repeating Character

Status: Solved  
Topic: Strings  
Pattern: Hashing  
Difficulty: Easy

### Problem

Find the first character that appears more than once while scanning left to right.

### Approach

1. Keep a set of seen characters.
2. Traverse the string.
3. If a character is already seen, print it and stop.
4. Otherwise, add it to the set.

### Code

```python
text = "abcaed"
seen = set()

for char in text:
    if char in seen:
        print(char)
        break
    seen.add(char)
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

Expected output: `a`.

## [STR-014] First Non-Repeating Character

Status: Solved  
Topic: Strings  
Pattern: Hashing  
Difficulty: Easy

### Problem

Find the first character that appears exactly once.

### Approach

1. Count frequency of every character.
2. Traverse the string again.
3. Print the first character with frequency `1`.

### Code

```python
text = "aabbcde"
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

for char in text:
    if freq[char] == 1:
        print(char)
        break
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

Two passes keep the logic clean.

## [STR-015] Count Characters

Status: Solved  
Topic: Strings  
Pattern: Frequency Counting  
Difficulty: Easy

### Problem

Print the frequency of each character once.

### Approach

1. Count each character using a dictionary.
2. Traverse the original string.
3. Print a character only the first time it appears.

### Code

```python
text = "hello"
freq = {}
printed = set()

for char in text:
    freq[char] = freq.get(char, 0) + 1

for char in text:
    if char not in printed:
        print(f"{char} -> {freq[char]}")
        printed.add(char)
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

Preserves first appearance order.

## [STR-016] Character With Maximum Frequency

Status: Solved  
Topic: Strings  
Pattern: Frequency Counting  
Difficulty: Easy

### Problem

Find the character with the highest frequency.

### Approach

1. Count frequency of each character.
2. Track the character with the largest count.

### Code

```python
text = "aabbbbcc"
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

max_char = ""
max_count = 0

for char, count in freq.items():
    if count > max_count:
        max_count = count
        max_char = char

print(max_char, max_count)
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

Avoid using `max` as a variable name.

## [STR-017] Check Anagram

Status: Revisit  
Topic: Strings  
Pattern: Frequency Counting  
Difficulty: Easy

### Problem

Check whether two strings contain the same characters with the same frequencies.

### Approach

1. If lengths differ, they are not anagrams.
2. Count characters in both strings.
3. Compare both frequency dictionaries.

### Code

```python
s1 = "listen"
s2 = "silent"

if len(s1) != len(s2):
    print("Not Anagram")
else:
    freq1 = {}
    freq2 = {}

    for char in s1:
        freq1[char] = freq1.get(char, 0) + 1

    for char in s2:
        freq2[char] = freq2.get(char, 0) + 1

    print("Anagram" if freq1 == freq2 else "Not Anagram")
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

Simple membership-only checks are not enough when duplicate counts differ.

Day 03 review: sorting and frequency approaches were attempted, but manual dictionary comparison needed a hint and `sorted()` complexity was unclear. Revisit as LeetCode `Valid Anagram` and write both O(n log n) sorting and O(n) hashing complexities.

Day 04 review: brute force, sorted, and frequency versions were completed locally. Still revisit because the final frequency version used `char not in t` during the comparison loop, which weakens the claimed O(n) optimized complexity. Use direct dictionary comparison or `char not in freq_t`.

## [STR-018] Check Substring

Status: Solved  
Topic: Strings  
Pattern: Nested Loops  
Difficulty: Easy

### Problem

Check whether `sub` appears inside `text` without using built-in search.

### Approach

1. Try every possible starting index.
2. Compare each character of the substring.
3. If all characters match, mark found.

### Code

```python
text = "hello world"
sub = "world"
found = False

for i in range(len(text) - len(sub) + 1):
    match = True
    for j in range(len(sub)):
        if text[i + j] != sub[j]:
            match = False
            break
    if match:
        found = True
        break

print("Found" if found else "Not Found")
```

### Complexity

Time: O(n * m)  
Space: O(1)

### Notes

This is the manual base for substring search.

## [STR-019] Find Longest Word

Status: Solved  
Topic: Strings  
Pattern: String Building  
Difficulty: Easy

### Problem

Find the longest word in a sentence without using `split()`.

### Approach

1. Build the current word character by character.
2. When a space is found, compare current word length with longest word.
3. Reset the current word.
4. Compare one final time after the loop.

### Code

```python
text = "I love Python programming"
current_word = ""
longest_word = ""

for char in text:
    if char != " ":
        current_word += char
    else:
        if len(current_word) > len(longest_word):
            longest_word = current_word
        current_word = ""

if len(current_word) > len(longest_word):
    longest_word = current_word

print(longest_word)
```

### Complexity

Time: O(n^2)  
Space: O(n)

### Notes

Expected output: `programming`. A list-based builder is better for large text.

## [STR-020] String Compression

Status: Solved  
Topic: Strings  
Pattern: String Building / Counting  
Difficulty: Easy

### Problem

Compress consecutive characters with their counts.

### Approach

1. Track the current character and count.
2. If the next character is the same, increase count.
3. Otherwise, append character and count to the result.
4. Append the final group after the loop.

### Code

```python
text = "aaabbc"

if text == "":
    compressed = ""
else:
    result = []
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result.append(text[i - 1] + str(count))
            count = 1

    result.append(text[-1] + str(count))
    compressed = "".join(result)

print(compressed)
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

Expected output: `a3b2c1`.

## [STR-021] Check Rotation

Status: Solved  
Topic: Strings  
Pattern: String Matching  
Difficulty: Easy

### Problem

Check whether one string is a rotation of another.

### Approach

1. Lengths must be equal.
2. Concatenate the first string with itself.
3. If the second string appears in that combined string, it is a rotation.

### Code

```python
s1 = "abcde"
s2 = "cdeab"

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Yes")
else:
    print("No")
```

### Complexity

Time: O(n) average for Python substring search  
Space: O(n)

### Notes

This is the clean standard solution for rotation checks.

## [STR-022] Valid Palindrome

Status: Revisit  
Topic: Strings  
Pattern: Two Pointers / Skip Non-Alphanumeric  
Difficulty: Easy

### Problem

Return `True` if a string is a palindrome after ignoring non-alphanumeric characters and case.

### Approach

1. Place `left` at the start and `right` at the end.
2. Move `left` forward while it points to a non-alphanumeric character.
3. Move `right` backward while it points to a non-alphanumeric character.
4. Compare lowercase characters.
5. Move both pointers inward until they meet or a mismatch is found.

### Code

```python
def is_palindrome(s):
    left = 0
    right = len(s) - 1

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

### Complexity

Time: O(n)  
Space: O(1)

### Notes

Day 04 review: brute-force cleaned-string version was completed with syntax help. Optimized two-pointer version needed hint/solution exposure for the inner skip loops. Revisit within 24h and submit after a clean local solve.

## [STR-023] Reverse String In Place

Status: Solved  
Topic: Strings / Lists  
Pattern: Two Pointers / In-Place Swap  
Difficulty: Easy

### Problem

Reverse a list of characters in-place.

### Approach

1. Place `left` at the start and `right` at the end.
2. Swap both characters.
3. Move inward until pointers meet or cross.

### Code

```python
def reverse_string(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

Day 04 review: solved independently and passed local examples. In LeetCode style, mutate the input list; returning it is unnecessary.

## [STR-024] Is Subsequence

Status: Revisit  
Topic: Strings  
Pattern: Two Pointers / Match Pointer  
Difficulty: Easy

### Problem

Return `True` if string `s` is a subsequence of string `t`.

### Approach

1. If `s` is empty, return `True`.
2. Scan through `t`.
3. Keep one pointer for the next needed character in `s`.
4. Advance the `s` pointer only when characters match.
5. Return `True` once the pointer reaches `len(s)`.

### Code

```python
def is_subsequence(s, t):
    pointer_s = 0

    for char in t:
        if pointer_s < len(s) and s[pointer_s] == char:
            pointer_s += 1
        if pointer_s == len(s):
            return True

    return pointer_s == len(s)
```

### Complexity

Time: O(n), where n is `len(t)`  
Space: O(1)

### Notes

Day 04 review: final local solution was correct, but required repeated hints. Main mistake was overthinking with nested loops and placing the completion check in the wrong place. Revisit within 24h.

## Sets / Hashing

## [HASH-001] Remove Duplicates Using Set

Status: Solved  
Topic: Sets / Hashing  
Pattern: Hashing  
Difficulty: Easy

### Problem

Remove duplicate values using a set.

### Approach

1. Convert the list to a set.
2. Print the unique values.

### Code

```python
nums = [1, 2, 2, 3, 4, 4, 5]
unique_values = set(nums)

print(unique_values)
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

A set removes duplicates but does not guarantee the original order.

## [HASH-002] Check Duplicate Exists

Status: Solved  
Topic: Sets / Hashing  
Pattern: Hashing  
Difficulty: Easy

### Problem

Return `True` if any duplicate exists.

### Approach

1. Keep a set of seen values.
2. If a value is already in the set, a duplicate exists.
3. Otherwise, add it to the set.

### Code

```python
nums = [1, 2, 3, 4, 1]
seen = set()
has_duplicate = False

for num in nums:
    if num in seen:
        has_duplicate = True
        break
    seen.add(num)

print(has_duplicate)
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

This is faster than nested loops.

## [HASH-003] Find Common Elements

Status: Solved  
Topic: Sets / Hashing  
Pattern: Hashing  
Difficulty: Easy

### Problem

Find common elements between two lists.

### Approach

1. Convert the second list to a set.
2. Traverse the first list.
3. Keep values that exist in the set.

### Code

```python
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

b_values = set(b)
common = []

for num in a:
    if num in b_values:
        common.append(num)

print(common)
```

### Complexity

Time: O(n + m)  
Space: O(m)

### Notes

Expected output: `[3, 4]`.

## [HASH-004] Find Missing Number Optimized

Status: Solved  
Topic: Sets / Hashing  
Pattern: Hashing  
Difficulty: Easy

### Problem

Find the missing number from `1` to `n` using sets.

### Approach

1. Create a set from `1` to `n`.
2. Convert the input list to a set.
3. Subtract the input set from the full set.

### Code

```python
nums = [1, 2, 4, 5]
n = len(nums) + 1

expected = set(range(1, n + 1))
actual = set(nums)

print(list(expected - actual)[0])
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

Set difference gives the missing value directly.

## [HASH-005] First Non-Repeating Element

Status: Solved  
Topic: Sets / Hashing  
Pattern: Frequency Dictionary  
Difficulty: Easy

### Problem

Find the first number that appears only once.

### Approach

1. Count every number using a dictionary.
2. Traverse the original list.
3. Print the first number with frequency `1`.

### Code

```python
nums = [1, 2, 2, 3, 1, 4]
freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

for num in nums:
    if freq[num] == 1:
        print(num)
        break
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

The second pass preserves original order.

## [HASH-006] Count Frequencies Using Dictionary

Status: Solved  
Topic: Sets / Hashing  
Pattern: Frequency Dictionary  
Difficulty: Easy

### Problem

Count the frequency of every number in a list.

### Approach

1. Create an empty dictionary.
2. Traverse the list.
3. Increment the count for each number.

### Code

```python
nums = [1, 2, 2, 3, 1, 4]
freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

print(freq)
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

Frequency dictionaries are used in many string and array problems.

## Tuples

## [TUP-001] Swap Using Tuple

Status: Solved  
Topic: Tuples  
Pattern: Tuple Unpacking  
Difficulty: Easy

### Problem

Swap two values using tuple unpacking.

### Approach

1. Put both values on the right side in swapped order.
2. Assign them back to the variables.

### Code

```python
a = 5
b = 10

a, b = b, a

print(a, b)
```

### Complexity

Time: O(1)  
Space: O(1)

### Notes

Python does not need a temporary variable for swapping.

## [TUP-002] Unpack Tuple

Status: Solved  
Topic: Tuples  
Pattern: Tuple Unpacking  
Difficulty: Easy

### Problem

Unpack a tuple into separate variables.

### Approach

1. Match the number of variables to the number of tuple values.
2. Assign directly.

### Code

```python
values = (10, 20, 30)
x, y, z = values

print(x, y, z)
```

### Complexity

Time: O(1)  
Space: O(1)

### Notes

Too many or too few variables causes a `ValueError`.

## [TUP-003] Loop Unpacking

Status: Solved  
Topic: Tuples  
Pattern: Tuple Unpacking  
Difficulty: Easy

### Problem

Given pairs, print the sum of each pair.

### Approach

1. Traverse each pair.
2. Unpack pair values directly in the loop.
3. Print their sum.

### Code

```python
pairs = [(1, 2), (3, 4), (5, 6)]

for x, y in pairs:
    print(x + y)
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

Each pair must contain exactly two values.

## [TUP-004] Ignore Middle Value

Status: Solved  
Topic: Tuples  
Pattern: Tuple Unpacking  
Difficulty: Easy

### Problem

Print only the first and last values from a tuple.

### Approach

1. Unpack the tuple.
2. Use `_` for the ignored middle value.

### Code

```python
values = (1, 2, 3)
first, _, last = values

print(first, last)
```

### Complexity

Time: O(1)  
Space: O(1)

### Notes

`_` is a convention for ignored values.

## [TUP-005] Star Unpacking

Status: Solved  
Topic: Tuples  
Pattern: Tuple Unpacking  
Difficulty: Easy

### Problem

Unpack the first value, middle values, and last value.

### Approach

1. Assign the first value normally.
2. Use `*middle` to collect the middle values.
3. Assign the last value normally.

### Code

```python
values = (1, 2, 3, 4, 5)
first, *middle, last = values

print(first, middle, last)
```

### Complexity

Time: O(n)  
Space: O(n)

### Notes

Star unpacking creates a list.

## [TUP-006] Nested Tuple Access

Status: Solved  
Topic: Tuples  
Pattern: Indexing  
Difficulty: Easy

### Problem

Access a value inside a nested tuple.

### Approach

1. Use the first index to access the inner tuple.
2. Use the second index to access the value.

### Code

```python
values = ((1, 2), (3, 4))

print(values[1][1])
```

### Complexity

Time: O(1)  
Space: O(1)

### Notes

Expected output: `4`.

## [TUP-007] Nested Tuple Unpacking

Status: Solved  
Topic: Tuples  
Pattern: Tuple Unpacking  
Difficulty: Easy

### Problem

Unpack a nested tuple and print all values.

### Approach

1. Match the nested structure on the left side.
2. Assign all inner values.

### Code

```python
values = ((1, 2), (3, 4))
(x1, y1), (x2, y2) = values

print(x1, y1, x2, y2)
```

### Complexity

Time: O(1)  
Space: O(1)

### Notes

The unpacking pattern must match the data shape.

## [TUP-008] Reverse Tuple Without Slicing

Status: Solved  
Topic: Tuples  
Pattern: Reverse Traversal  
Difficulty: Easy

### Problem

Reverse a tuple without using slicing.

### Approach

1. Start with an empty tuple.
2. Traverse the original tuple.
3. Add each value to the front of the new tuple.

### Code

```python
values = (1, 2, 3, 4)
reversed_values = ()

for value in values:
    reversed_values = (value,) + reversed_values

print(reversed_values)
```

### Complexity

Time: O(n^2)  
Space: O(n)

### Notes

Tuples are immutable, so each concatenation creates a new tuple.

## [TUP-009] Count Occurrences in Tuple

Status: Solved  
Topic: Tuples  
Pattern: Linear Traversal  
Difficulty: Easy

### Problem

Count how many times a target appears in a tuple without using `count()`.

### Approach

1. Start `count` at `0`.
2. Traverse the tuple.
3. Increment when the value equals the target.

### Code

```python
values = (1, 2, 3, 4, 2)
target = 2
count = 0

for value in values:
    if value == target:
        count += 1

print(count)
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

Same frequency pattern as lists.

## [TUP-010] Remove Duplicates From Tuple

Status: Solved  
Topic: Tuples  
Pattern: Existence Check  
Difficulty: Easy

### Problem

Remove duplicate values from a tuple without using a set.

### Approach

1. Create an empty tuple.
2. Traverse the original tuple.
3. Add values only if they are not already present.

### Code

```python
values = (1, 2, 2, 3, 1)
unique_values = ()

for value in values:
    if value not in unique_values:
        unique_values = unique_values + (value,)

print(unique_values)
```

### Complexity

Time: O(n^2)  
Space: O(n)

### Notes

Tuple concatenation creates a new tuple each time.

## [TUP-011] Merge Two Tuples Without Direct Plus

Status: Solved  
Topic: Tuples  
Pattern: Tuple Building  
Difficulty: Easy

### Problem

Merge two tuples manually.

### Approach

1. Create an empty tuple.
2. Add all values from the first tuple.
3. Add all values from the second tuple.

### Code

```python
t1 = (1, 2)
t2 = (3, 4)
merged = ()

for value in t1:
    merged = merged + (value,)

for value in t2:
    merged = merged + (value,)

print(merged)
```

### Complexity

Time: O(n^2)  
Space: O(n)

### Notes

This is for practice only. In real code, `t1 + t2` is simpler.

## [TUP-012] Second Largest in Tuple

Status: Solved  
Topic: Tuples  
Pattern: Tracking  
Difficulty: Easy

### Problem

Find the second largest distinct number in a tuple.

### Approach

1. Track the largest and second largest values.
2. Update both while traversing.
3. Ignore duplicates of the largest value.

### Code

```python
values = (5, 1, 8, 3, 8)

largest = float("-inf")
second_largest = float("-inf")

for value in values:
    if value > largest:
        second_largest = largest
        largest = value
    elif largest > value > second_largest:
        second_largest = value

print(second_largest)
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

Expected output: `5`.

## [TUP-013] Find Minimum Sum Pair

Status: Solved  
Topic: Tuples  
Pattern: Linear Traversal  
Difficulty: Easy

### Problem

Find the pair with the smallest sum.

### Approach

1. Track the smallest sum.
2. Traverse each pair.
3. If a pair has a smaller sum, update the result.

### Code

```python
pairs = [(1, 5), (2, 3), (4, 7)]

min_sum = float("inf")
result = None

for x, y in pairs:
    current_sum = x + y
    if current_sum < min_sum:
        min_sum = current_sum
        result = (x, y)

print(result)
```

### Complexity

Time: O(n)  
Space: O(1)

### Notes

Expected output: `(2, 3)`.

## [TUP-014] Count Frequency Using Tuples

Status: Solved  
Topic: Tuples  
Pattern: Nested Loops  
Difficulty: Easy

### Problem

Return `(value, count)` pairs for each unique number.

### Approach

1. For each number, count its frequency using another loop.
2. Create a `(number, count)` tuple.
3. Add it to the result only if it is not already present.

### Code

```python
nums = [1, 2, 2, 3]
result = []

for num in nums:
    count = 0

    for other in nums:
        if num == other:
            count += 1

    pair = (num, count)

    if pair not in result:
        result.append(pair)

print(result)
```

### Complexity

Time: O(n^2)  
Space: O(n)

### Notes

A dictionary is more efficient, but this is useful tuple practice.

## Basic Python Practice

## [PY-001] Simple Calculator

Status: Solved  
Topic: Python Fundamentals  
Pattern: Functions / Conditionals  
Difficulty: Easy

### Problem

Build a simple calculator for addition, subtraction, multiplication, and division.

### Approach

1. Create functions for each operation.
2. Check the operator.
3. Call the matching function.

### Code

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


num1 = 10
num2 = 5
operator = "+"

if operator == "+":
    print(add(num1, num2))
elif operator == "-":
    print(subtract(num1, num2))
elif operator == "*":
    print(multiply(num1, num2))
elif operator == "/":
    print(divide(num1, num2))
else:
    print("Invalid operator")
```

### Complexity

Time: O(1)  
Space: O(1)

### Notes

Fix naming from `calculater` to `calculator` and `oprator` to `operator`.

## [PY-002] Day of Week

Status: Solved  
Topic: Python Fundamentals  
Pattern: Match Case  
Difficulty: Easy

### Problem

Print the day name for a number from `1` to `7`.

### Approach

1. Match the number.
2. Print the corresponding day.
3. Use default case for invalid input.

### Code

```python
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input")
```

### Complexity

Time: O(1)  
Space: O(1)

### Notes

`match` is useful for clear multi-case branching.

## [PY-003] Vowel or Consonant

Status: Solved  
Topic: Python Fundamentals  
Pattern: Match Case  
Difficulty: Easy

### Problem

Check whether a character is a vowel or consonant.

### Approach

1. Match the character against vowels.
2. Print vowel if matched.
3. Otherwise print consonant.

### Code

```python
char = "a"

match char.lower():
    case "a" | "e" | "i" | "o" | "u":
        print("Vowel")
    case _:
        print("Consonant")
```

### Complexity

Time: O(1)  
Space: O(1)

### Notes

Use `.lower()` to handle uppercase input.

## [PY-004] Number Classification

Status: Solved  
Topic: Python Fundamentals  
Pattern: Match Case / Conditions  
Difficulty: Easy

### Problem

Classify a number as even positive, odd positive, negative, or zero.

### Approach

1. Use guarded match cases.
2. Check positive even first.
3. Check positive odd, negative, and zero.

### Code

```python
num = 5

match num:
    case n if n > 0 and n % 2 == 0:
        print("Even Positive")
    case n if n > 0 and n % 2 != 0:
        print("Odd Positive")
    case n if n < 0:
        print("Negative")
    case 0:
        print("Zero")
```

### Complexity

Time: O(1)  
Space: O(1)

### Notes

Avoid duplicate cases.

## [PY-005] Print Star Pattern

Status: Solved  
Topic: Python Fundamentals  
Pattern: Nested Loops / Pattern Printing  
Difficulty: Easy

### Problem

Print a growing star pattern.

### Approach

1. Loop from `1` to `n`.
2. Print that many stars on each line.

### Code

```python
n = 3

for i in range(1, n + 1):
    print("*" * i)
```

### Complexity

Time: O(n^2)  
Space: O(1)

### Notes

Pattern printing is useful for nested-loop practice.

## [PY-006] Multiplication Table Matrix

Status: Solved  
Topic: Python Fundamentals  
Pattern: Nested Loops  
Difficulty: Easy

### Problem

Print a multiplication table from `1` to `n`.

### Approach

1. Use an outer loop for rows.
2. Use an inner loop for columns.
3. Print the product.

### Code

```python
n = 3

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end=" ")
    print()
```

### Complexity

Time: O(n^2)  
Space: O(1)

### Notes

This is a clean nested-loop exercise.

## To Revisit

| Problem Name | Topic | Priority | Reason |
| --- | --- | --- | --- |
| Remove Duplicates From Sorted Array | Arrays / Write Pointer | High | Needed concept help; must become automatic. |
| Remove Element | Arrays / Write Pointer | Medium | Day 03 independent re-solve succeeded; revisit again in 3 days before mastery. |
| Missing Number | Arrays / Hashing / Math | High | Set method needed hint; complexity notes need correction. |
| Best Time To Buy And Sell Stock | Arrays / Running Minimum | High | Logic required AI help. |
| Plus One | Arrays / Carry Simulation | High | Solution was viewed; re-solve from memory. |
| Product Of Array Except Self | Arrays / Prefix-Suffix | High | Day 03 two-array prefix/suffix improved; still needs output-array + one suffix variable version. |
| Rotate Array | Arrays / Reverse Method | Medium | Edge cases and in-place reverse method need practice. |
| Second Largest Distinct Element | Arrays / Tracking | Medium | Empty/all-duplicate edge cases caused trouble. |
| Boyer-Moore Majority Element | Arrays / Voting | Medium | Candidate logic known; validation learned with help. |
| Move Negative Numbers To End | Arrays / Partition | Medium | Revision solution copied from AI. |
| Third Largest Distinct Element | Arrays / Tracking | Medium | Revision solution copied from AI. |
| Two Sum | Hashing | High | Day 04 independent re-solve succeeded locally; still needs LeetCode accepted + 3-day recall before mastery. |
| Valid Anagram | Hashing / Strings | High | Day 04 local solve improved, but optimized version used string membership in comparison loop; fix O(n) hash version. |
| First Unique Character in a String | Hashing / Strings | Medium | Day 04 independent optimized re-solve succeeded locally; needs LeetCode accepted + spaced recall before mastery. |
| Valid Palindrome | Strings / Two Pointers | High | Day 04 optimized skip-loop version needed hint/solution exposure; revisit in 24h. |
| Is Subsequence | Strings / Two Pointers | High | Day 04 required repeated hints for match-pointer scan; revisit in 24h. |
| Group Anagrams | Hashing / Grouping | Medium | Next medium grouping pattern. |
| Top K Frequent Elements | Hashing / Frequency | Medium | Next medium frequency pattern. |

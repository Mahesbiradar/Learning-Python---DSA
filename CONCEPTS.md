# Python + DSA Concepts

## Python Fundamentals

### Introduction

Python is a high-level, interpreted, general-purpose programming language focused on readable syntax and fast development.

Key Points:
- Created by Guido van Rossum and released in 1991.
- Uses indentation instead of braces.
- Supports procedural, object-oriented, and functional programming.
- Commonly used for web development, data science, automation, AI/ML, scripting, and DSA practice.

Small Example:

```python
print("Hello, World!")
```

Interview Tip:
- Python is called interpreted because code is executed through the Python interpreter instead of being manually compiled first.

### Python Interpreter

The Python interpreter executes Python code and manages the process from source code to bytecode execution.

Key Points:
- Python code is checked for syntax.
- Python generates bytecode.
- The Python Virtual Machine executes the bytecode.
- Python supports interactive mode and script mode.

Small Example:

```bash
python file.py
```

Interview Tip:
- Python is slower than C/C++ mostly because it is dynamically typed and interpreted at runtime.

### Variables

A variable is a name that refers to a value/object in memory.

Key Points:
- Variables are created using `=`.
- Python variables are references, not fixed memory boxes.
- Names should use `snake_case`.
- Avoid unclear names like `x`, `y`, `a` unless used in very small examples.
- Avoid shadowing built-ins like `max`, `sum`, `list`, `dict`, and `set`.

Small Example:

```python
user_name = "Mahesh"
age = 22
```

Interview Tip:
- In Python, assignment binds a name to an object.

### Data Types

Python has built-in data types for numbers, text, booleans, and collections.

Key Points:
- `int`: whole numbers.
- `float`: decimal numbers.
- `str`: text.
- `bool`: `True` or `False`.
- `list`: mutable ordered collection.
- `tuple`: immutable ordered collection.
- `set`: mutable unordered unique collection.
- `dict`: key-value mapping.

Small Example:

```python
marks = 90
price = 99.5
name = "Python"
is_active = True
```

Interview Tip:
- Python is dynamically typed but strongly typed. It does not automatically combine incompatible types like `"10" + 5`.

### Type Conversion

Type conversion changes a value from one type to another.

Key Points:
- Use `int()` for integers.
- Use `float()` for decimals.
- Use `str()` for strings.
- Use `bool()` for truth testing.
- User input is always received as a string.

Small Example:

```python
age = int(input("Enter age: "))
print(age + 5)
```

Interview Tip:
- `bool("")` is `False`, but `bool("False")` is `True` because the string is not empty.

### Mutability

Mutability means whether an object can be changed after creation.

Key Points:
- Immutable: `int`, `float`, `str`, `tuple`.
- Mutable: `list`, `dict`, `set`.
- Mutable objects can be changed in-place.
- Assignment can make two variables refer to the same object.

Small Example:

```python
a = [1, 2]
b = a
b.append(3)
print(a)  # [1, 2, 3]
```

Interview Tip:
- Lists are mutable, so changes through one reference can affect another reference to the same list.

### Scope

Scope controls where a variable can be accessed.

Key Points:
- Local variables exist inside a function.
- Global variables exist outside functions.
- Avoid unnecessary global variables.
- Use `global` only when you intentionally need to modify a global variable.

Small Example:

```python
count = 0

def update_count():
    global count
    count += 1
```

Interview Tip:
- Variable shadowing happens when a local variable has the same name as an outer variable.

### Operators

Operators perform calculations and comparisons.

Key Points:
- Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`.
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`.
- Logical: `and`, `or`, `not`.
- Membership: `in`, `not in`.
- Identity: `is`, `is not`.

Small Example:

```python
num = 10
is_even = num % 2 == 0
```

Interview Tip:
- `==` checks value equality, while `is` checks object identity.

### Conditionals

Conditionals execute code based on a condition.

Key Points:
- Use `if` for one condition.
- Use `elif` for multiple choices.
- Use `else` as the fallback.
- Use `match` for clear multi-case branching.

Small Example:

```python
num = 5

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

Interview Tip:
- Keep conditions simple and readable. Complex conditions are a common source of bugs.

### Loops

Loops repeat code.

Key Points:
- Use `for` when you know what to iterate over.
- Use `while` when repetition depends on a condition.
- `break` exits the loop.
- `continue` skips the current iteration.
- `pass` is a placeholder that does nothing.
- A `for...else` block runs only if the loop does not break.

Small Example:

```python
for num in [1, 2, 3]:
    print(num)
```

Interview Tip:
- Use `break` for early exit when the answer is found.

### Strings

Strings are immutable sequences of characters.

Key Points:
- Support indexing and slicing.
- Can be traversed with loops.
- New strings are built using concatenation or `join`.
- Strings cannot be changed in-place.

Small Example:

```python
text = "Python"
print(text[0])
print(text[::-1])
```

Interview Tip:
- Since strings are immutable, repeated concatenation can be costly for large strings. Use list-building plus `join` when needed.

### Lists

Lists are mutable ordered collections.

Key Points:
- Support indexing, slicing, and traversal.
- Common methods: `append`, `extend`, `pop`, `count`, `copy`, `reverse`, `sort`.
- Used as arrays in Python DSA.
- Can be modified in-place.

Small Example:

```python
nums = [1, 2, 3]
nums.append(4)
print(nums)
```

Interview Tip:
- Use index-based loops when you need to modify list elements.

### List Comprehension

List comprehension creates a new list using compact loop syntax.

Key Points:
- Useful for transformation and filtering.
- Keep it readable.
- Avoid deeply nested comprehensions when clarity suffers.

Small Example:

```python
nums = [-2, -1, 0, 1, 2]
squares = [num * num for num in nums if num > 0]
```

Interview Tip:
- In interviews, prefer clear loops if the comprehension becomes hard to explain.

### Tuples

Tuples are immutable ordered collections.

Key Points:
- Created with parentheses or commas.
- A single-element tuple needs a comma: `(5,)`.
- Support indexing, slicing, traversal, concatenation, repetition, and membership checks.
- Can be used as dictionary keys if all elements are hashable.

Small Example:

```python
point = (10, 20)
x, y = point
```

Interview Tip:
- Use tuples for fixed data and multiple return values.

### Tuple Unpacking

Tuple unpacking assigns multiple values at once.

Key Points:
- Useful for swapping.
- Useful for loop unpacking.
- Star unpacking collects remaining values into a list.
- `_` is commonly used for ignored values.

Small Example:

```python
a, b = 5, 10
a, b = b, a
```

Interview Tip:
- Python tuple unpacking makes swaps clean and avoids temporary variables.

### Named Tuples

Named tuples are immutable tuple-like objects with named fields.

Key Points:
- Created using `collections.namedtuple`.
- Access values using dot notation.
- Improve readability over plain tuple indexes.

Small Example:

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x)
```

Interview Tip:
- Named tuples are useful when you want lightweight immutable records.

### Sets

Sets store unique unordered elements.

Key Points:
- Duplicate values are automatically removed.
- Empty `{}` creates a dictionary, not a set.
- Use `set()` for an empty set.
- `add()` inserts an element.
- `remove()` raises an error if the element is missing.
- `discard()` does not raise an error if the element is missing.
- Membership checks are usually faster than lists.

Small Example:

```python
seen = set()
seen.add(10)
print(10 in seen)
```

Interview Tip:
- Use sets when uniqueness and fast membership checks matter.

### Set Operations

Set operations compare or combine sets.

Key Points:
- Union: `a | b`
- Intersection: `a & b`
- Difference: `a - b`
- Symmetric difference: `a ^ b`
- Subset check: `a <= b`

Small Example:

```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)  # {3}
```

Interview Tip:
- Set operations are common in duplicate, common-element, and missing-number problems.

### Dictionaries

Dictionaries store key-value pairs.

Key Points:
- Keys must be hashable.
- Values can be any type.
- Commonly used for frequency counting and lookup.
- Membership checks on keys are fast.

Small Example:

```python
freq = {}

for char in "aabbc":
    freq[char] = freq.get(char, 0) + 1
```

Interview Tip:
- Dictionaries are the main Python tool for hashing problems.

### Functions

Functions group reusable logic.

Key Points:
- Defined using `def`.
- Can accept parameters.
- Can return one or multiple values.
- Keep functions small and focused.

Small Example:

```python
def add(a, b):
    return a + b
```

Interview Tip:
- In interviews, writing a function makes your solution easier to test and explain.

## DSA Foundations

### Arrays / Lists

In Python, lists are commonly used as arrays for DSA practice.

Key Points:
- Elements are ordered.
- Indexing starts at `0`.
- Lists are mutable.
- Most beginner array problems use traversal, comparison, counting, or pointer movement.

Small Example:

```python
nums = [3, 7, 2]
print(nums[0])
```

Interview Tip:
- Always clarify whether the list can be modified in-place.

### Traversal

Traversal means visiting each element.

Key Points:
- Use value traversal when only values are needed.
- Use index traversal when positions or modifications are needed.
- Single traversal is usually `O(n)`.

Small Example:

```python
for num in nums:
    print(num)
```

Interview Tip:
- Many DSA problems start with simple traversal and then add tracking variables.

### Index vs Value

Value loops access elements directly. Index loops access positions.

Key Points:
- Value loop: cleaner for reading.
- Index loop: needed for comparing neighbors or modifying items.
- `range(len(nums))` gives valid indexes.

Small Example:

```python
for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        print("Not sorted")
```

Interview Tip:
- Use index loops when the problem mentions positions, neighbors, swaps, or in-place updates.

### Time Complexity

Time complexity estimates how runtime grows with input size.

Key Points:
- Constant work: `O(1)`.
- Single loop: `O(n)`.
- Nested loops: `O(n^2)`.
- Hash lookup average case: `O(1)`.

Small Example:

```python
for num in nums:
    print(num)  # O(n)
```

Interview Tip:
- State complexity after explaining the approach.

### Space Complexity

Space complexity estimates extra memory used.

Key Points:
- In-place updates usually use `O(1)` extra space.
- Extra list, set, or dictionary usually uses `O(n)` space.
- Input storage is not counted as extra space unless the interviewer asks.

Small Example:

```python
seen = set(nums)  # O(n) extra space
```

Interview Tip:
- Mention whether your solution modifies the input or creates a new structure.

### Edge Cases

Edge cases are inputs that can break simple logic.

Key Points:
- Empty list or string.
- Single element.
- All same values.
- Negative numbers.
- Duplicate values.
- Already sorted input.
- No valid answer.

Small Example:

```python
if not nums:
    print("Empty input")
```

Interview Tip:
- Naming edge cases before coding shows strong problem-solving discipline.

### Dry Run Technique

Dry running means manually tracing variables step by step.

Key Points:
- Track indexes.
- Track important variables.
- Track list changes after each iteration.
- Use small examples.

Small Example:

```text
nums = [1, 2, 3]
total = 0
after 1: total = 1
after 2: total = 3
after 3: total = 6
```

Interview Tip:
- Dry run pointer and nested-loop problems carefully.

## DSA Patterns

### Linear Traversal

Linear traversal scans input once from left to right.

Key Points:
- Used for sum, count, max, min, search, frequency, and first occurrence.
- Usually `O(n)` time.
- Often uses tracking variables.

Small Example:

```python
max_value = nums[0]

for num in nums:
    if num > max_value:
        max_value = num
```

Interview Tip:
- Initialize tracking variables from the input when negatives are possible.

### Two Pointers

Two pointers use two indexes to process data from different positions.

Key Points:
- Opposite ends: reverse, palindrome.
- Same direction: position tracking, moving values.
- Often gives `O(n)` time and `O(1)` space.

Small Example:

```python
left = 0
right = len(nums) - 1

while left < right:
    left += 1
    right -= 1
```

Interview Tip:
- Clearly explain how and why each pointer moves.

### Sliding Window

Sliding window maintains a moving range of elements.

Key Points:
- Useful for subarray or substring problems.
- Can be fixed-size or variable-size.
- Not yet heavily practiced in this workspace.

Small Example:

```python
window_sum = sum(nums[:k])
```

Interview Tip:
- Use sliding window when the problem asks about continuous subarrays or substrings.

### Hashing

Hashing uses sets or dictionaries for fast lookup.

Key Points:
- Sets track seen values.
- Dictionaries store counts or indexes.
- Useful for duplicates, two sum, anagrams, and first unique/repeating values.

Small Example:

```python
seen = set()

for num in nums:
    if num in seen:
        print("Duplicate")
    seen.add(num)
```

Interview Tip:
- Hashing often improves nested-loop solutions from `O(n^2)` to `O(n)`.

### Nested Loops

Nested loops compare each item with many other items.

Key Points:
- Usually `O(n^2)`.
- Useful for beginner manual logic.
- Often replaceable with hashing.
- Common in duplicate detection, frequency counting, and substring matching.

Small Example:

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            print("Duplicate")
```

Interview Tip:
- If you use nested loops, mention whether a hash-based optimization exists.

### Element Shifting

Element shifting moves values one position at a time.

Key Points:
- Used in rotation problems.
- Requires saving overwritten values.
- Usually done in-place.

Small Example:

```python
first = nums[0]

for i in range(len(nums) - 1):
    nums[i] = nums[i + 1]

nums[-1] = first
```

Interview Tip:
- Store the value that would be overwritten before shifting.

### String Building

String building creates a new string from selected or transformed characters.

Key Points:
- Used for removing spaces, reversing strings, compression, and duplicate removal.
- For small problems, `result += char` is simple.
- For larger inputs, append to a list and use `"".join(result)`.

Small Example:

```python
result = []

for char in text:
    if char != " ":
        result.append(char)

print("".join(result))
```

Interview Tip:
- Remember strings are immutable, so building a new string is usually required.

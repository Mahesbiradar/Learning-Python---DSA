"""
## Arrays / Lists

## [REV-ARR-001] Move Zeros to End

Topic: Arrays / Lists  
Pattern: Two Pointer / Position Tracking  
Difficulty: Medium

### Problem

Move all zeros to the end while keeping the order of non-zero elements.

### Input

```python
nums = [0, 1, 0, 3, 12]
```

### Expected Output

```python
[1, 3, 12, 0, 0]
```

### Requirements

- Solve in-place.
- Do not create a second list.
- Time: O(n)
- Space: O(1)

"""

nums = [0, 1, 0, 3, 12]
pos=0

for i in nums:
    if i!=0:
        nums[pos]=i
        pos+=1
for j in range(pos,len(nums)):
    nums[j]=0
print(nums)

"""

## [REV-ARR-002] Find Second Largest Distinct Element

Topic: Arrays / Lists  
Pattern: Tracking  
Difficulty: Medium

### Problem

Find the second largest distinct number in a list.

### Input

```python
nums = [10, 5, 8, 20, 15]
```

### Expected Output

```python
15
```

### Requirements

- Do not sort the list.
- Handle duplicate largest values.
- Handle negative numbers. """

nums = [10, 5, 8, 20, 15]

max_val=nums[0]
second_max=float('-inf')

for i in range(1,len(nums)):
    if nums[i]>max_val:
        second_max=max_val
        max_val=nums[i]
    elif nums[i]>second_max and nums[i]!=max_val:
        second_max=nums[i]
print(second_max)


"""
## [REV-ARR-003] Check if List is Sorted

Topic: Arrays / Lists  
Pattern: Adjacent Comparison  
Difficulty: Medium

### Problem

Check whether a list is sorted in non-decreasing order.

### Input

```python
nums = [1, 3, 2, 5]
```

### Expected Output

```python
False
```

### Requirements

- Use index traversal.
- Stop early when unsorted order is found.

"""
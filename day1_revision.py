"""## Problem 8: Find Second Largest Distinct Element

Given a list of integers, return the second largest distinct element.

Example:

```python
nums = [10, 5, 8, 20, 15]
```

Expected output:

```python
15
```

Requirements:
- Do not sort the list.
- Handle duplicate largest values.
- Handle negative numbers.
- If no second largest distinct value exists, return `None`.

Test cases:

```python
[10, 5, 8, 20, 15] -> 15
[20, 20, 10] -> 10
[5, 5, 5] -> None
[1] -> None
[-10, -5, -20] -> -10
```

---

## Problem 9: Move Zeroes To End

Given a list of integers, move all zeroes to the end while keeping the order of non-zero elements.

Example:

```python
nums = [0, 1, 0, 3, 12]
```

Expected output:

```python
[1, 3, 12, 0, 0]
```

Requirements:
- Solve in-place.
- Do not create a second list.
- Keep the order of non-zero elements.

Test cases:

```python
[0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
[0, 0, 1] -> [1, 0, 0]
[1, 2, 3] -> [1, 2, 3]
[0, 0, 0] -> [0, 0, 0]
[] -> []
```

---

## Problem 10: Majority Element

Given a list of integers where one element appears more than `n // 2` times, return that majority element.

Example:

```python
nums = [3, 2, 3]
```

Expected output:

```python
3
```

Requirements:
- First solve using a dictionary frequency map.
- Then try the Boyer-Moore voting approach if you can.
- You may assume a majority element always exists.

Test cases:

```python
[3, 2, 3] -> 3
[2, 2, 1, 1, 1, 2, 2] -> 2
[1] -> 1
[5, 5, 5, 2, 2] -> 5
```

---"""

#Here ill Simply Move to the code:

# Problem 8: Find Second Largest Distinct Element

def second_maximum(nums):
    if len(nums) < 2:
        return None
    max_val=nums[0]
    second_max=float('-inf')
    for i in nums:
        if i>max_val:
            second_max=max_val
            max_val=i
        elif i>second_max and i!=max_val:
            second_max=i
    if second_max==float('-inf'):
        return None
    return second_max


print(second_maximum([10, 5, 8, 20, 15]))
print(second_maximum([20, 20, 10]))
print(second_maximum([5, 5, 5]))
print(second_maximum([]))
print(second_maximum([-10, -5, -20]))

    
#Time Comlexcity: O(n)
#Space Complexcity: O(1)

## Problem 9: Move Zeroes To End

def move_zeros(nums):
    pos=0
    for i in nums:
        if i!=0:
            nums[pos]=i
            pos+=1
    for j in range(pos, len(nums)):
        nums[j]=0
    return nums

print(move_zeros([0, 1, 0, 3, 12]))
print(move_zeros([0, 0, 1]))
print(move_zeros([1, 2, 3]))
print(move_zeros([0, 0, 0]))
print(move_zeros([]))

#Time Comlexcity: O(n)
#Space Complexcity: O(1)
  

## Problem 10: Majority Element

def major_element(nums):
    seen={}
    max_val=0
    major_ele=None
    for i in nums:
        if i in seen:
            seen[i]+=1
        else:
            seen[i]=1
    for key,value in seen.items():
        if value>max_val:
            max_val=value
            major_ele=key
    return major_ele

print(major_element([3, 2, 3]))
print(major_element([2, 2, 1, 1, 1, 2, 2]))
print(major_element([1]))
print(major_element([5, 5, 5, 2, 2]))

#Time Comlexcity: O(n)
#Space Complexcity: O(n)

#Boyer-Moore voting approach if you can.
def boyer_moore(nums):
    candidate=None
    count=0
    #Boyer-Moore
    for i in nums:
        if count==0:
            candidate=i
            count=1
        elif i==candidate:
            count+=1
        else:
            count-=1
    #Validate Majority(if not Exists)
    count=0
    for i in nums:
        if i==candidate:
            count+=1
    if count>len(nums)//2:
        return candidate
    else:
        return None


print( boyer_moore([2, 2, 1, 1, 1, 2, 2]))
print( boyer_moore([3, 2, 3]))
print( boyer_moore([1, 2, 3]))
print( boyer_moore([5, 5, 5, 2, 2, 2]))


#Time Complexcity:  O(n)
#Space Complexcity: O(1)

#Status: The #Boyer-Moore of identifying the candidate is solved by me but the validating majority in case not exists logic is understood with chatgpt
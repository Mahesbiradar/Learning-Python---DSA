"""## Problem 1: Print All Elements

Given a list, print every element one by one.

Example:

```python
nums = [10, 20, 30, 40]
```

Expected output:

```text
10
20
30
40
```

Requirements:
- Visit every element.
- Do not use built-in shortcuts for learning purposes.
"""

"""Understanding:In this problem a List is given with integer Items and expected is to traversal all the element 
in list and print each item with each iteration."""

#Brute Force:Here we have to use loop and this is the only solution

#Optimized:same solution as the Brute Force.

"""Dry Run:
iteration 1: i=10 (Print 10)
iteration 1: i=20 (Print 20)
iteration 1: i=30 (Print 30)
iteration 1: i=40 (Print 40)
Loop ends"""

#Code:

nums = [10, 20, 30, 40]

def print_element(nums):
    for i in nums:
        print(i)

print_element(nums)




# Time Complexity:O(n) bcz the loops runs n times

# Space Complexity:O(1) with each iteration one item value is holded by varible i 

# Status: Solved independently

# Mistake or confusion: initially for pasing arg i used print(print_element(nums)) here all elements are Printing but one more none is printing at end

"""
## Problem 2: Sum Of List

Given a list of integers, return the sum of all elements.

Example:

```python
nums = [10, 20, 30]
```

Expected output:

```python
60
```

Requirements:
- Use a loop.
- Do not use Python's built-in `sum()` for this practice.

Test cases:

```python
[10, 20, 30] -> 60
[5] -> 5
[] -> 0
[-1, 2, -3] -> -2
```

---

"""

## Problem 2: Sum Of List

"""Understanding sequnce of integer nums given in list here the expected output is to sum all the elements of the list
without using the inbuilt sum() function and the solution shoud handles the edgecases such as empty list,negative int etc.
"""

"""Brute Force:

will initiate one varibale to hold the sum

Step-1 sum_val=float('-inf') to handle negative int or sum_val=0 
ste  
step-2 loops though the list first will handle all the edge cases and then
visit each element in list and will add the each element to the sum_val=i 
"""
"""Optimized: if prmisable we can use inbult function sum
def sum_list(nums):
    return sum(nums)

 """

"""Dry Run:
nums = [10, 20, 30]
1.i=10 i+sum_all = 10
2.i=20 i+sum_all = 10+2-=30
3.30+30=60
4.Print the sum_all
"""


#Code:

def sum_list(nums):
    result=0
    for i in nums:
        result+=i
    return result


print(sum_list([10, 20, 30]))
print(sum_list([]))
print(sum_list([-1, 2, -3]))

# Time Complexity: O(n)

# Space Complexity:O(1)

# Status: Solved independently

# Mistake or confusion: NA


"""
## Problem 3: Count Even Numbers

Given a list of integers, count how many numbers are even.

"""

#understanding Here the question contains the list of intergers so we have to make function which retuns the number even int in the list and handle edgeCases

#Brute Force: Loop through all the the Element in list with filtering and Count the even nums

#optimal: We can use list Comprehension 

"""Dry Run
nums = [1, 2, 3, 4, 6]
count=0
1. i=1 1%2==0? False count=0
2. i=2 2%2==0? True  count=1  count+=1

and at the end we retuns the Count

"""

#Code: 

def count_even(nums):
    count=0
    for i in nums:
        if i%2==0:
            count+=1
    return count

print(count_even([1,2,3,4,5]))
print(count_even([]))

#Time Complexity: O(n) bcz loop runs n times

#Space Complexity:O(1)

#Status: Solved independently

#Mistake or confusion: No

"""
## Problem 4: Find Maximum Element

Given a non-empty list of integers, return the maximum element.

Example:

```python
nums = [10, 5, 20, 8]
```

Expected output:

```python
20
```

Requirements:
- Do not use `max()`.
- Track the maximum manually.

Test cases:

```python
[10, 5, 20, 8] -> 20
[5] -> 5
[-10, -3, -20] -> -3
[7, 7, 7] -> 7
```

---

"""

#Understanding: in input non empty list is given here i have to find the max elemenet in a list.

#Brute Force: We siply Runs a Loops over a list and comapare each element with variable value if the element is > max then we store that element in variable.

#Optimized: Same as brute Force.

"""Dry Run:
[10, 5, 20, 8]
max_element=float('-inf') # To handle Negative elements
1.i=10 max_element=float('-inf')  i>max_element? True max_element=i
2.i=5 max_element=10   i>max_element? false

so on by end of the loop we got our max_element and we return the Max_element

"""

#Code:

def max_element(nums):
    max_element=float('-inf')
    for i in nums:
        if i>max_element:
            max_element=i
    return max_element
print(max_element([10, 5, 20, 8] ))  # 20
print(max_element([-10, -3, -20]))   #-3
print(max_element([7, 7, 7]))        #7
print(max_element([5]))        #5

#time complexcity: O(n) THE LOOP RUNS N TIME

#Space complexity :O(1) Storing only one element

#Status: Solved independently

#Mistake or confusion: do we have any option to initailize the max_element apart from float('-inf') to handle edgecases.


"""## Problem 5: Find Minimum Element

Given a non-empty list of integers, return the minimum element.

Example:

```python
nums = [10, 5, 20, 8]
```

Expected output:

```python
5
```

Requirements:
- Do not use `min()`.
- Track the minimum manually.

Test cases:

```python
[10, 5, 20, 8] -> 5
[5] -> 5
[-10, -3, -20] -> -20
[7, 7, 7] -> 7
```

---

"""

#Understanding: in input non empty list is given here i have to find the min elemenet in a list.

#Brute Force: We siply Runs a Loops over a list and comapare each element with variable value if the element is < min then we store that element in variable.

#Optimized: Same as brute Force.

"""Dry Run:
[10, 5, 20, 8]
max_element=float('inf') # To handle Positive elements
1.i=10 min_element=float('inf')  i<min_element? True min_element=i
2.i=5 min_element=10   i>min_element? true min_element=i 

so on by end of the loop we got our min_element and we return the Min_element

"""
#Code:

def min_element(nums):
    min_element=float('inf')
    for i in nums:
        if i<min_element:
            min_element=i
    return min_element

print(min_element([-10, -3, -20]))   #-20
print(min_element([10, 5, 20, 8] ))  # 5
print(min_element([7, 7, 7]))        #7
print(min_element([5]))        #5



#time complexcity: O(n) THE LOOP RUNS N TIME

#Space complexity :O(1) Storing only one element

#Status: Solved independently

#Mistake or confusion:

"""
## Problem 6: Reverse Array

Given a list, reverse it.

Example:

```python
nums = [1, 2, 3, 4]
```

Expected output:

```python
[4, 3, 2, 1]
```

Requirements:
- First solve using a new list.
- Then try in-place using two pointers.
- Do not use `reverse()` or slicing `[::-1]` for this practice.

Test cases:

```python
[1, 2, 3, 4] -> [4, 3, 2, 1]
[1, 2, 3] -> [3, 2, 1]
[5] -> [5]
[] -> []
```

---
"""

#Understanding: The array is given and i have to reverse this array (list) one solution shoud be using newlist and one more using inplace

#Brute Force: #1 (using new list) will initiate one pointer to locate last elemement and run a loop with each iteration i will decrement a pointer ans will append the iteration value to new List
              # for inplace solution i will use two pointers left and right for index traking and swap values and then move those pointers towards middle.

#optimal: Similar to brute fore bcz i have iterate to all the elements in the list

"""Dry Run
for inplace Code
nums=[1,2,3,4]
left=0
right=3
1.[4,2,3,1]
2.[4,3,2,1]

 """

#Code:using New List
def reverse_list(nums):
    new_list=[]
    pos=len(nums)-1
    for i in nums:
        new_list.append(nums[pos])
        pos-=1
    return new_list

print(reverse_list([1, 2, 3, 4]))
print(reverse_list([1, 2, 3]))
print(reverse_list([5]))
print(reverse_list([]))




##Code:using inplace

def reverse_list(nums):
    left=0
    right=len(nums)-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    return nums

print(reverse_list([1, 2, 3, 4]))
print(reverse_list([1, 2, 3]))
print(reverse_list([5]))
print(reverse_list([]))

#Time Complexcity 1.O(n) for both solutions
#Space Complexcity 1.O(n) 2.O(1)

#Status: Solved independently

#Mistake or confusion: 


"""
## Problem 7: Check If Array Is Sorted

Given a list of integers, return `True` if it is sorted in non-decreasing order, otherwise return `False`.

Example:

```python
nums = [1, 2, 2, 4]
```

Expected output:

```python
True
```

Requirements:
- Compare adjacent elements.
- Duplicates are allowed.

Test cases:

```python
[1, 2, 2, 4] -> True
[1, 3, 2, 4] -> False
[5] -> True
[] -> True
[-3, -2, -2, 0] -> True
```

---
"""


#understanding: here the Problem statement is about to check the list if its in incrasing order or not and here duplicates also allowed.

#Brute Force: Here will run a Loop over a list and compare the each element with its neighbour element i>=i+1 

#Optimized:Same as brute force as this is the optimal solution

"""Dry Run
[1, 2, 2, 4]

1.i=1 i+1=2  i>=i+1? True 
2.i=2 i+1=2 i>=i+1? True
3.i=2 i+1=4 i>i+1? True

after all element will retrun the tru

[1, 3, 2, 4]

1.i=1 i+1=3  i>=i+1? True 
2.i=3 i+1=2 i>=i+1? False
Here will break and retun the False.

"""

def sorted_array(nums):
    
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:     #To compare the elements
            return False
    return True   

print(sorted_array([1,2,2,3,4])) #True
print(sorted_array([1, 3, 2, 4]))  # False
print(sorted_array([-3, -2, -2, 0]))  # True
print(sorted_array([5]))  #True
print(sorted_array([]))  #True 

#Time Complexcity:  O(n)
#Space Complexcity: O(1)

#Status: Solved independently

#Mistake or confusion: intially im hnadling edge cases explicitly and used on variale to track the condition. and returning that varibale

"""
## Problem 8: Find Second Largest Distinct Element

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

"""
#Understanding : Here i have to resturn the second largest element in the the list

#Brute Force: will intialize two varibales to store the max and second max value and then  loop over a list to compare values with each element.

#optimal: this is the optimal solution

"""
Dry Run 
[10, 5, 8, 20, 15]

max=num[0]
smax=float('-inf')

1. i=10 max=10 i>max? False   i>smax and i!=max?false #max=10,smax=float('-inf')
1. i=5 max=10 i>max? False   i>smax and i!=max?True #max=10,smax=5
1. i=8 max=10 i>max? False   i>smax and i!=max?True #max=10,smax=8
1. i=20 max=10 i>max? True   i>smax and i!=max?False #max=20,smax=8
1. i=15 max=20 i>max? False   i>smax and i!=max?True #max=20,smax=15
"""

#Code:

def second_maximum(nums):
    max_val=nums[0]
    second_max=float('-inf')
    if len(nums) < 2:   #This edge case i have not handeled intially 
        return None

    for i in nums:
        if i>max_val:
            second_max=max_val
            max_val=i
        elif i>second_max and i!=max_val:
            second_max=i
    if second_max==float('-inf'):  #This edge case i have not handeled intially 
        return None
    return second_max

print(second_maximum([10, 5, 8, 20, 15]))  #15
print(second_maximum([20, 20, 10]))  #10
print(second_maximum([5, 5, 5] ))   #None
print(second_maximum([1]))   #None
print(second_maximum([-10, -5, -20]))  #-10


#Time Complexcity:  O(n)
#Space Complexcity: O(1)

#Status: Solved independently

#Mistake or confusion: intially i have not handled the two edge case explicitly 1.Len of list <2 and if all the element in list comtains same value then seen in chatgpt remaing all the logic is mine 

"""
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

"""

#Understanding: The given list contains zeros and i have to move these Zeros to the end of the list and non zero elements to to the front of th list without chaning the order.

#Brute Force: for this problem i will take one pointer for indexing to shift non zero element to front and run a first loop to shift nonzero elements
#in the second loop ill append the zeros to end ending side of the element based on the pointer.

#optimal: The brute force solution is optimal solution.

"""
Dry Run

pos=0

for 1st Loop
[0, 1, 0, 3, 12]

1> i=0  i!=0? false [0,1,0,3,12]
2> i=1  i!=0? True nums[pos]=i and the will increment pos=1 [1,1,0,3,12]
3>i=0  i!=0? false [1,1,0,3,12]
4> i=3  i!=0? True nums[pos]=i and the will increment pos=2 [1,1,3,3,12]
5> i=12  i!=0? True nums[pos]=i and the will increment pos=3 [1,1,3,12,12]


Now in second loop will start from the pointer(3) and append zeros 
1> [1,1,3,0,12]
2> [1,1,3,0,0]

"""

#code:

def move_zeros(nums):
    pos=0
    for i in nums:
        if i!=0:
            nums[pos]=i
            pos+=1
    for i in range(pos,len(nums)):
        nums[i]=0
    return nums

print(move_zeros([0, 1, 0, 3, 12]))
print(move_zeros([0, 0, 1]))
print(move_zeros([1, 2, 3]))
print(move_zeros([0, 0, 0]))
print(move_zeros([]))

#Time Complexcity:  O(n)
#Space Complexcity: O(1)

#Status: Solved independently

#Mistake or confusion: while solving forgot to increment the pointer then realize for all the list passing to function printing zeros in list. 


"""
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
"""

#Understanding: The list is given now i have to find the element which appears maximum time 

#Brute Force: first i will make one Dict then add all the elements of list in the dict with the frequency occurance

#Then Run one more Loop to Find the Majar element

#Optimal: 


#Code: 

def major_element(nums):
    seen={}
    major_ele=0
    major_Elements=None
    for i in nums:
        if i in seen:
            seen[i]+=1
        else:
            seen[i]=1
    for key,value in seen.items():
        if value>major_ele:
            major_ele=value
            major_Elements=key
    return major_Elements

print( major_element([3, 2, 3]))
print( major_element([2, 2, 1, 1, 1, 2, 2]))
print( major_element([1]))
print( major_element([5, 5, 5, 2, 2]))

        
#Time Complexcity:  O(n)
#Space Complexcity: O(n)

#Status: Solved independently 


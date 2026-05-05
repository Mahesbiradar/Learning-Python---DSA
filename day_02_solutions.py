"""## Problem 1: Contains Duplicate

Given a list of integers, return `True` if any value appears at least twice. Return `False` if every element is distinct.

Example:

```python
nums = [1, 2, 3, 1]
```

Expected output:

```python
True
```

Requirements:
- First write the brute-force nested-loop idea.
- Then solve using a set.

Test cases:

```python
[1, 2, 3, 1] -> True
[1, 2, 3, 4] -> False
[1, 1, 1, 3, 3, 4, 3, 2, 4, 2] -> True
[] -> False
```

---"""
#Understanding: given the list of intergers now i have to check if any integer exist more than once i have ro retun True else false.

#Brute Force: I will run a loop and in nested loop ill check the frequncy of occurance and retun the True or False.


"""Dry Run as its Easy Probelem so ill save time here
"""

def contains_duplicate(nums):
    for i in nums:
        count=0
        for j in nums:
            if i==j:
                count+=1
            if count>=2:
                return True
    return False

print(contains_duplicate([1, 2, 3, 1]))  #True
print(contains_duplicate([1, 2, 3, 4]))  # False
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  #True
print(contains_duplicate([])) #False

# Time complexcity: O(N^2)
# Space Complexcity:O(1)

#Optimal:
def contains_duplicate(nums):
    new_set=set(nums)
    if len(nums)!=len(new_set):
        return True
    return False


print(contains_duplicate([1, 2, 3, 1]))  #True
print(contains_duplicate([1, 2, 3, 4]))  # False
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  #True
print(contains_duplicate([])) #False

# Time complexcity: O(1)
# Space Complexcity:O(n)
#Pattern: Existance Check.


"""
## Problem 2: Remove Duplicates From Sorted Array

Given a sorted list of integers, remove duplicates in-place so each unique element appears only once. Return the number of unique elements.

Example:

```python
nums = [1, 1, 2]
```

Expected output:

```python
2
```

After the function runs, the first `2` positions should be:

```python
[1, 2]
```

Requirements:
- Solve in-place.
- Use a write pointer.
- Do not create a second list for the optimized solution.

Test cases:

```python
[1, 1, 2] -> 2, first part [1, 2]
[0, 0, 1, 1, 1, 2, 2, 3, 3, 4] -> 5, first part [0, 1, 2, 3, 4]
[1] -> 1, first part [1]
[] -> 0, first part []
```

---
"""

#UndersStanding: the problems understoods as i have to check the unique elements in the list

#Brute Force:Here i'll initiate one write pointer and then run a loop and compare the neighbouring elements.

#optimal : same as brute Force

"""Dry Run:
[1,2,2,3,4,5]

1. i=2  w=1  i-1=1  i!=i-1? true write+=1 [1,2,2,3,4,5] 
2. i=2  w=2  i-1=2  i!=i-1? false [1,2,2,3,4,5] 
3. i=3  w=2  i-1=2  i!=i-1? true write+=1 [1,2,3,3,4,5] 
4. i=4  w=3  i-1=3  i!=i-1? true write+=1 [1,2,3,4,4,5] 
5. i=5  w=4  i-1=4  i!=i-1? true write+=1 [1,2,3,4,5,5]
write=5

"""

def remove_duplicates(nums):
    # if not nums:
    #     return 0
    write=1
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            nums[write]=nums[i]
            write+=1
    return write
   
print(remove_duplicates([1, 1, 2] ))
print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(remove_duplicates([1]))
print(remove_duplicates([]))

# Time complexcity: O(n)
# Space Complexcity:O(1)
#Pattern: Neighbouring Comparison.
#Status: Solved after knowing the concept from chat gpt not able to Solve independently/ Solved after hint / Stuck

#Mistake or confusion:initially i thougy we have to literally remove the elements from the list then with help of gpt i caome to know that i have to shift the Elements.


"""
## Problem 3: Remove Element

Given a list `nums` and an integer `val`, remove all occurrences of `val` in-place. Return the new length.

Example:

```python
nums = [3, 2, 2, 3]
val = 3
```

Expected output:

```python
2
```

After the function runs, the first `2` positions should contain:

```python
[2, 2]
```

Requirements:
- Solve in-place.
- The order of remaining elements can stay the same.
- Do not create a second list for the optimized solution.

Test cases:

```python
[3, 2, 2, 3], val = 3 -> 2, first part [2, 2]
[0, 1, 2, 2, 3, 0, 4, 2], val = 2 -> 5, first part [0, 1, 3, 0, 4]
[], val = 1 -> 0, first part []
[1, 1, 1], val = 1 -> 0, first part []
```

---
"""
#understanding: The list of integers are given along with one value so i have to remove the all the elements in a list which matches with the val.

#Brute Force: Here ill use write Pointer to overwrite the Non-Matching elements with val using a loop and comparing each element with val.

"""Dry Run:
[3, 2, 2, 3], val = 3 pos=0

1. i=3  val=3 pos=0  i!=val? Flase [3,2,2,3]
2. i=2  val=3 pos=0  i!=val? True Nums[pos]=2 ,pos=1 [2,2,2,3]
3. i=2  val=3 pos=1  i!=val? True Nums[pos]=2 ,pos=2 [2,2,2,3]
3. i=3  val=3 pos=1  i!=val? True Nums[pos]=2 ,pos=2 [2,2,2,3]

"""
def remove_element(nums,val):
    if not nums:
        return 0
    write=0
    for i in nums:
        if i!=val:
            nums[write]=i
            write+=1
    return write

print(remove_element([3, 2, 2, 3],3))   
print(remove_element([0, 1, 2, 2, 3, 0, 4, 2],2)) 
print(remove_element([],0))
print(remove_element([1, 1, 1],1))    

#time Complexcity=O(n)
#Space Complexcity=O(1)

#Status: Solved independently But with the refernce of 2nd probkem solution and i came to know i have used this during zero Shifting

#Mistake or confusion:


"""
## Problem 4: Missing Number

Given a list containing `n` distinct numbers from the range `0` to `n`, return the only number missing from the list.

Example:

```python
nums = [3, 0, 1]
```

Expected output:

```python
2
```

Requirements:
- First solve using a set.
- Then try the sum formula approach.

Test cases:

```python
[3, 0, 1] -> 2
[0, 1] -> 2
[9, 6, 4, 2, 3, 5, 7, 0, 1] -> 8
[0] -> 1
```

"""


#Code:using Some Menthod

def missing_number(nums):
    n=len(nums)
    missing_num=(n*(n+1))//2-sum(nums)
    return missing_num

print(missing_number([3, 0, 1]))  #2
print(missing_number([0, 1]))  #2
print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))  #8
print(missing_number([0])) #1

#Time Complexcity: O(n)
#Space Complexcity: O(1)

#Status: Solved independently But INITAIILY I USED Loop for i in range(0,len(Nums)+1)and added each element in to Variable and last taken diff from variable and sum(nums)

#Mistake or confusion:


#Code:using set Menthod

def missing_number(nums):
    Seen=set(nums)
    for i in range(0,len(nums)+1):
        if i not in Seen:
            return i
    

print(missing_number([3, 0, 1]))  #2
print(missing_number([0, 1]))  #2
print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))  #8
print(missing_number([0])) #1

#Time Complexcity: O(n)
#Space Complexcity: O(1)

#Status: Here i was not able to think this solution so taken hints from Chatgpt.

"""
## Problem 5: Intersection Of Two Arrays

Given two lists, return a list of unique values that appear in both lists.

Example:

```python
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
```

Expected output:

```python
[2]
```

Requirements:
- Output may be in any order.
- Return unique intersection values only.
- Use sets for the optimized solution.

Test cases:

```python
[1, 2, 2, 1], [2, 2] -> [2]
[4, 9, 5], [9, 4, 9, 8, 4] -> [9, 4]
[], [1, 2] -> []
[1, 2], [3, 4] -> []
```

---

"""


#Understanding: Here i have given with two list so in have to return the only uniques elements which exists in both lists.


def intersection_array(nums1,nums2):

    set1=set(nums1)
    set2=set(nums2)
    result=[]

    for i in set1:
        if i in set2:
            result.append(i)
    return result
 

print(intersection_array([1, 2, 2, 1], [2, 2]))
print(intersection_array([4, 9, 5], [9, 4, 9, 8, 4]))
print(intersection_array([], [1, 2]))
print(intersection_array([1, 2], [3, 4]))


#Time Complexcity: O(n+m)  
#Space Complexcity: O(n+m)

#Status: Solved independently 

#Mistakes: time and space complx not answer properly i was writte   O(n) for both.


"""
## Problem 6: Best Time To Buy And Sell Stock

Given a list where `prices[i]` is the stock price on day `i`, return the maximum profit from buying once and selling once later. If no profit is possible, return `0`.

Example:

```python
prices = [7, 1, 5, 3, 6, 4]
```

Expected output:

```python
5
```

Requirements:
- First write the brute-force pair-check idea.
- Then solve in one pass by tracking the minimum price so far.

Test cases:

```python
[7, 1, 5, 3, 6, 4] -> 5
[7, 6, 4, 3, 1] -> 0
[1, 2] -> 1
[2, 4, 1] -> 2
```

"""

def buyandsell(nums):
    min_price=nums[0]
    max_profit=0

    for i in nums:
        if i<min_price:
            min_price=i
        else:
            profit=i-min_price
            if profit>max_profit:
                max_profit=profit 
    return max_profit

print(buyandsell([7, 1, 5, 3, 6, 4]))
print(buyandsell([7, 6, 4, 3, 1]))
print(buyandsell([1, 2] ))
print(buyandsell([2, 4, 1] ))

#Time Complexcity: O(n)  
#Space Complexcity: O(1)

#Status: Not understood the Concept and unable to build the logic to Taken Help of AI

#Mistakes:

"""
## Problem 7: Plus One

Given a list of digits representing a non-negative integer, add one and return the resulting digits.

Example:

```python
digits = [1, 2, 3]
```

Expected output:

```python
[1, 2, 4]
```

Requirements:
- Traverse from right to left.
- Handle carry.
- Do not convert the whole list to an integer.

Test cases:

```python
[1, 2, 3] -> [1, 2, 4]
[4, 3, 2, 1] -> [4, 3, 2, 2]
[9] -> [1, 0]
[9, 9, 9] -> [1, 0, 0, 0]
```

"""

def plus_one(nums):

    for i in range(len(nums)-1,-1,-1):
        if nums[i]<9:
            nums[i]+=1
            return nums
        nums[i]=0
    return [1]+nums
        
print( plus_one([1, 2, 3]))
print( plus_one([4, 3, 2, 1]))
print( plus_one([9]))
print( plus_one([9, 9, 9]))

#Time Complexcity: O(n)  
#Space Complexcity: O(1)

#Status: im not able to build the logic by own after Seen the Solution i got Clarity.

#Mistakes:

"""
## Problem 8: Rotate Array

Given a list `nums`, rotate it to the right by `k` steps.

Example:

```python
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
```

Expected output:

```python
[5, 6, 7, 1, 2, 3, 4]
```

Requirements:
- First solve using an extra list.
- Then try the in-place reverse method.
- Handle `k > len(nums)`.

Test cases:

```python
[1, 2, 3, 4, 5, 6, 7], k = 3 -> [5, 6, 7, 1, 2, 3, 4]
[-1, -100, 3, 99], k = 2 -> [3, 99, -1, -100]
[1, 2], k = 3 -> [2, 1]
[], k = 3 -> []
```

"""
##Using the new list
def rotate_array(nums,k):
    if not nums:
        return nums
    if k>len(nums):
        k=k%len(nums)
    left_part=nums[:len(nums)-k]
    right_part=nums[len(nums)-k:]
    result=right_part+left_part

    return result

   

print(rotate_array([1, 2, 3, 4, 5, 6, 7],3))
print(rotate_array([-1, -100, 3, 99],2))
print(rotate_array([],3))
print(rotate_array([1, 2],2))

#Time Complexcity: O(n)  
#Space Complexcity: O(n)

#Status: Here solved independently but the concept understanding the edge cases handling understading i used Chatgpt

"""Mistakes:
Mistakes:
1. Initially used division instead of modulo for k
2. Initially misunderstood split index (used k+1 instead of n-k)
3. Learned that rotation is based on last k elements, not first k
"""
##Using in place Method.

##Using the new list
def rotate_array(nums,k):
    if not nums:
        return nums
    
    k=k%len(nums)

    left=0
    right=len(nums)-1
    #Revrese Entire array
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    #reverse the left part till 
    left=0
    right=k-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    #reverse the Remaining array
    left=k
    right=len(nums)-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    return nums


print(rotate_array([1, 2, 3, 4, 5, 6, 7],3))
print(rotate_array([-1, -100, 3, 99],2))
print(rotate_array([],3))
print(rotate_array([1, 2],3))


#Time Complexcity: O(n)  
#Space Complexcity: O(1)

#Status: Understood and implemented reverse-based rotation pattern independently after guidance




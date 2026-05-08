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


"""
## Problem 9: Product Of Array Except Self

Given a list of integers, return a list where each index contains the product of all numbers except the number at that index.

Example:

```python
nums = [1, 2, 3, 4]
```

Expected output:

```python
[24, 12, 8, 6]
```

Requirements:
- Do not use division.
- First solve using left and right product arrays.
- Then try optimizing to output array plus one running suffix variable.

Test cases:

```python
[1, 2, 3, 4] -> [24, 12, 8, 6]
[-1, 1, 0, -3, 3] -> [0, 0, 9, 0, 0]
[2, 3] -> [3, 2]
[0, 0] -> [0, 0]
```

---
"""

#Understanding:Here the list of the intergeres given and i have to retun the list which contains the Product of array of all element except the Self Index.

#Brute Force Solution: Here ill Run a nested loop to calculate the Product of array except Self.

def prod_array(nums):
    result=[]
    

    for i in range(len(nums)):
        product=1
        for j in range(len(nums)):
            if i!=j:
                product*=nums[j]
        result.append(product)
    return result

print(prod_array([1, 2, 3, 4]))
print(prod_array([-1, 1, 0, -3, 3]))
print(prod_array([2, 3]))
print(prod_array([0, 0]))

#Time Complexcity: O(n^2)  
#Space Complexcity: O(n)

#Status: Solved independently

#Mistakes: intially i was comparing the Values in list But lated Fixed and now comparing the Index.

#optimal solution:

def prod_array(nums):
    left=[1]
    for i in range(1,len(nums)):
        left.append(left[i-1]*nums[i-1])
    right=[None]*len(nums)
    right[-1]=1
    for i in range(len(nums)-2,-1,-1):
        right[i]=right[i+1]*nums[i+1]
    result=[]
    for i in range(len(nums)):
        result.append(left[i]*right[i])

    return result


print(prod_array([1, 2, 3, 4]))
print(prod_array([-1, 1, 0, -3, 3]))
print(prod_array([2, 3]))
print(prod_array([0, 0]))

#Time Complexcity: O(n)  
#Space Complexcity: Not sure

#Status: Solved independently

#Mistakes: Mistakes:Initially struggled to convert prefix/suffix concept into code logic.Learned how left product and right product arrays reuse previous computations.

"""
## Problem 10: First Missing Positive

Given an unsorted list of integers, return the smallest missing positive integer.

Example:

```python
nums = [1, 2, 0]
```

Expected output:

```python
3
```

Requirements:
- First solve using a set.
- Then read about the in-place cyclic placement approach and attempt it if you have time.
- This is the hard/stretch problem for Day 2.

Test cases:

```python
[1, 2, 0] -> 3
[3, 4, -1, 1] -> 2
[7, 8, 9, 11, 12] -> 1
[1] -> 2
```

"""

#understanding: Here the list of intergers are given i have to retunr the smallest missing integer in a list.

#Brute Force: my first approch is to run a inner loop to comparing the elements of list with numbers 1 to n.

def first_missing_positive(nums):
    
    for i in range(1,len(nums)+2):
        if i not in nums:
            return i

print(first_missing_positive([1, 2, 0]))   #3
print(first_missing_positive([3, 4, -1, 1]))  #2
print(first_missing_positive([7, 8, 9, 11, 12])) #1
print(first_missing_positive([1]))   #2

#Time Complexcity: O(n^2)  
#Space Complexcity: O(1)

#Status: Solved independently
    

#Unsing The set

def first_missing_positive(nums):
    
    seen=set(nums)

    for i in range(1,len(seen)+2):
        if i not in seen:
            return i
        
print(first_missing_positive([1, 2, 0]))   #3
print(first_missing_positive([3, 4, -1, 1]))  #2
print(first_missing_positive([7, 8, 9, 11, 12])) #1
print(first_missing_positive([1])) #2

#Time Complexcity: O(n)  
#Space Complexcity: O(n)

#Status: Solved independently
    

# ==================== DAY 02 REVISION SOLUTIONS ====================

"""
# Problem 10: First Missing Positive II

Return the smallest missing positive integer.

Example:

```python
nums = [2, 3, 7, 6, 8, -1, -10, 15]
```

Expected Output:

```python
1
```

Requirements:

* Solve using set only
* Ignore negative numbers
* Think in range `1 -> n+1`

Test Cases:

```python
[1, 2, 0] -> 3
[3, 4, -1, 1] -> 2
[7, 8, 9, 11, 12] -> 1
[1] -> 2
[2, 3, 7, 6, 8, -1, -10, 15] -> 1

"""

#Understanding: Here i have to retun the first smallest interger Number.

#Sol: As per the Requiremet ill use the Set and and run a loop from 1 to n+1 and using in function do fast lookup in set and returns the smallest missing Number.

def first_missing_interger(nums):
    seen=set(nums)

    for i in range(1,len(nums)+2):
        if i not in seen:
            return i
        

print(first_missing_interger([1, 2, 0]))  #3
print(first_missing_interger([3, 4, -1, 1]))  #2
print(first_missing_interger([7, 8, 9, 11, 12]))  #1
print(first_missing_interger([1])) #2
print(first_missing_interger([2, 3, 7, 6, 8, -1, -10, 15]))  #1

#time Comp: O(n)
#space Comp: O(n)


"""
# Problem 8: Product Of Array Except Self II

Return a list where each index contains the product of all numbers except itself.

Example:

```python
nums = [2, 3, 4]
```

Expected Output:

```python
[12, 8, 6]
```

Requirements:

* Do not use division
* Build left array
* Build right array
* Multiply both

Test Cases:

```python
[1, 2, 3, 4] -> [24, 12, 8, 6]
[2, 3, 4] -> [12, 8, 6]
[-1, 1, 0, -3, 3] -> [0, 0, 9, 0, 0]
[0, 0] -> [0, 0]
[5] -> [1]
```


"""

#Solution using the Prefix and suffix prod

def prod_array(nums):


    #Cal prodcut of left array
    left=[1]
    for i in  range(1,len(nums)):
        left.append(left[i-1]*nums[i-1])

    #Cal prodcut of left array

    right=[None]*len(nums)
    right[-1]=1

    for i in range(len(nums)-2,-1,-1):
        right[i]=right[i+1]*nums[i+1]
    
    #Multiply Both array to get Productt of array
    
    result=[]

    for i in range(len(nums)):
        result.append(left[i]*right[i])


    return result

print(prod_array([1, 2, 3, 4]))
print(prod_array([2, 3, 4]))
print(prod_array([-1, 1, 0, -3, 3]))
print(prod_array([0, 0]))
print(prod_array([5]))


    
#time Comp: O(n)
#space Comp: O(n)

"""
# Problem 6: Smallest Missing Number

Given numbers from:

```python
0 -> n
```

with one missing number, return the missing number.

Example:

```python
nums = [0, 1, 3]
```

Expected Output:

```python
2
```

Requirements:

* Solve using set
* Solve using sum formula

Test Cases:

```python
[0, 1, 3] -> 2
[3, 0, 1] -> 2
[0, 1] -> 2
[0] -> 1
[1] -> 0
```

---


"""
#using the set

def smallest_missing_num(nums):
    seen=set(nums)

    for i in range(len(nums)+1):
        if i not in seen:
            return i

print(smallest_missing_num([0, 1, 8])) #2
print(smallest_missing_num([3, 0, 1]))  #2
print(smallest_missing_num([0, 1] )) # 2
print(smallest_missing_num([1])) #0
print(smallest_missing_num([0])) #1

#time Comp: O(n)
#space Comp: O(n)

#using the sum formula

def smallest_missing_num(nums):
    sum_of_n=(len(nums)*(len(nums)+1))//2
    return sum_of_n-sum(nums)

print(smallest_missing_num([3, 0, 1]))  #2
print(smallest_missing_num([0, 1] )) # 2
print(smallest_missing_num([1])) #0
print(smallest_missing_num([0])) #1

#time Comp: O(1)
#space Comp: O(n)

"""
# Problem 5: Remove Target Element In-Place

Remove all occurrences of `val` in-place.

Return the new length.

Example:

```python
nums = [1, 2, 3, 2, 4]
val = 2
```

Expected Output:

```python
3
```

After operation:

```python
[1, 3, 4]
```

Requirements:

* Use write pointer
* Solve in-place
* Do not create second list

Test Cases:

```python
[1, 2, 3, 2, 4], val = 2 -> 3
[0, 1, 2, 2, 3], val = 2 -> 3
[1, 1, 1], val = 1 -> 0
[], val = 1 -> 0
[4, 5, 6], val = 7 -> 3
```

---

"""


def remove_occurances(nums,val):
    if not nums:
        return 0
    write=0

    for i in range(len(nums)):
        if nums[i]!=val:
            nums[write]=nums[i]
            write+=1
    return write

print(remove_occurances([1, 2, 3, 2, 4],2))  # 3
print(remove_occurances([0, 1, 2, 2, 3],2)) #3
print(remove_occurances([1, 1, 1],1))  #0
print(remove_occurances([],1))  #0
print(remove_occurances([4, 5, 6],7))  #0
        
#time Comp: O(n)
#space Comp: O(1)


"""
# Problem 4: Contains Duplicate II

Return `True` if any element appears at least twice.

Example:

```python
nums = [1, 2, 3, 4, 1]
```

Expected Output:

```python
True
```

Requirements:

* Solve using brute force
* Solve using set/hash lookup

Test Cases:

```python
[1, 2, 3, 4, 1] -> True
[1, 2, 3, 4] -> False
[5, 5, 5] -> True
[] -> False
[1] -> False
```


"""

#Using Brute Force: ill use nested loop to the check the existnace of elements

def duplicate(nums):
    if not nums:
        return False

    for i in nums:
        count=0
        for j in nums:
            if i==j:
                count+=1
        if count>=2:
            return True
    return False

print(duplicate([1, 2, 3, 4, 1]))            
print(duplicate([1, 2, 3, 4]))            
print(duplicate([5, 5, 5] ))            
print(duplicate([]))            
print(duplicate([1]))            

# time comp:  O(n^2)
# space comp: O(1)

#Using Hasing;

def duplicate(nums):
    if not nums:
        return False
    
    seen={}

    for i in nums:
        if i in seen:
            seen[i]+=1
        else:
            seen[i]=1
    for key,value in seen.items():
        if value>1:
            return True
        
    return False

print(duplicate([1, 2, 3, 4, 1]))            
print(duplicate([1, 2, 3, 4]))            
print(duplicate([5, 5, 5] ))            
print(duplicate([]))            
print(duplicate([1]))     


   
# time comp:  O(n)
# space comp: O(n)

"""
# Problem 7: Rotate Array Left

Rotate array LEFT by `k`.

Example:

```python
nums = [1, 2, 3, 4, 5]
k = 2
```

Expected Output:

```python
[3, 4, 5, 1, 2]
```

Requirements:

* First solve using extra list
* Then solve using reverse method
* Handle `k > len(nums)`

Test Cases:

```python
[1, 2, 3, 4, 5], k = 2 -> [3, 4, 5, 1, 2]
[1, 2], k = 3 -> [2, 1]
[-1, -100, 3, 99], k = 2 -> [3, 99, -1, -100]
[] , k = 3 -> []

"""

#Using the Extra List:

def array_rotation(nums,k):
    if not nums:
        return nums
    k=k%len(nums)

    left=nums[:len(nums)-k]
    right=nums[len(nums)-k:]
    Result=right+left
    return Result

print(array_rotation([1, 2, 3, 4, 5],2))
print(array_rotation([1, 2],3))
print(array_rotation([-1, -100, 3, 99],2))
print(array_rotation([],3))


#time comp: O(1)
#Space Comp: O(n)

#Using in place:

def array_rotation(nums,k):
    if not nums:
        return nums

    k=k%len(nums)

    #step-1 Reverese the array

    left=0
    right=len(nums)-1

    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    
    
    #rotate the left part
    left=0
    right=k-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    #rotate Remainng part

    left=k
    right=len(nums)-1
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    return nums
print(array_rotation([1, 2, 3, 4, 5],2))
print(array_rotation([1, 2],3))
print(array_rotation([-1, -100, 3, 99],2))
print(array_rotation([],3))


#time comp: O(n)
#Space Comp: O(1)


"""
# Problem 9: Plus One II

Add one to a digit array.

Example:

```python
digits = [8, 9, 9, 9]
```

Expected Output:

```python
[9, 0, 0, 0]
```

Requirements:

* Traverse right to left
* Handle carry
* Handle all 9s case

Test Cases:

```python
[1, 2, 3] -> [1, 2, 4]
[9] -> [1, 0]
[9, 9, 9] -> [1, 0, 0, 0]
[8, 9, 9, 9] -> [9, 0, 0, 0]
[4, 3, 2, 1] -> [4, 3, 2, 2]
```

---

"""

def plus_one(nums):
    if not nums:
        return nums
    for i in range(len(nums)-1,-1,-1):

        if nums[i]<9:
            nums[i]+=1
            return nums
        nums[i]=0
    return [1]+nums

print(plus_one([1, 2, 3]))
print(plus_one([9]))
print(plus_one([9,9,9]))
print(plus_one([8,9,9,9]))
print(plus_one([4, 3, 2, 1]))




"""

# Problem 1: Maximum Difference

Given a list of integers, return the maximum difference:

```python
nums[j] - nums[i]
where j > i
````

If no positive difference exists, return `0`.

Example:

```python
nums = [7, 1, 5, 3, 6, 4]
```

Expected Output:

```python
5
```

Requirements:

* First think brute force
* Then optimize using one-pass minimum tracking

Test Cases:

```python
[7, 1, 5, 3, 6, 4] -> 5
[7, 6, 4, 3, 1] -> 0
[1, 2] -> 1
[2, 4, 1] -> 2
[5] -> 0
```

"""
    
def max_diff(nums):

    min_num=nums[0]
    max_diff=0

    for i in nums:
        if i<min_num:
            min_num=i
        else:
            Diff=i-min_num
            if Diff>max_diff:
                max_diff=Diff
    
    if max_diff<0:
        return 0
    return max_diff

    
print( max_diff([1, 7, 5, 3, 6, 4]))
print( max_diff([7, 6, 4, 3, 1]))
print( max_diff([1, 2]))
print( max_diff([7, 6, 4, 3, 1]))

#timecomp: O(n)
#Spacecomp: O(1)


"""
# Problem 2: Move Negative Numbers To End

Move all negative numbers to the end while maintaining the order of non-negative numbers.

Example:

```python
nums = [1, -2, 3, -4, 5]
```

Expected Output:

```python
[1, 3, 5, -2, -4]
```

Requirements:

* Solve in-place
* Use write-pointer approach
* Maintain order

Test Cases:

```python
[1, -2, 3, -4, 5] -> [1, 3, 5, -2, -4]
[-1, -2, 3, 4] -> [3, 4, -1, -2]
[1, 2, 3] -> [1, 2, 3]
[-1, -2] -> [-1, -2]
[] -> []
```
"""


def move_negative(nums):

    end=len(nums)-1
    i=0
    

    while i<end:

        if nums[i]<0:
            temp=nums[i]

            for j in range(i,len(nums)-1):
                nums[j]=nums[j+1]
            
            nums[end]=temp

            end-=1
        else:
            i+=1

    return nums

print(move_negative([1, -2, 3, -4, 5]))
print(move_negative([1, -2, 3, -4, 5]))
print(move_negative([1, -2, 3, -4, 5]))
print(move_negative([1, -2, 3, -4, 5]))

#timecomp=O(n^2)
#SpaceCOMP=O(1)

#Remarks:This Solution is not soved by me i took it from AI as i wan not able to build the logic.

"""
# Problem 3: Third Largest Distinct Element

Return the third largest distinct element.

If it doesn’t exist, return `None`.

Example:

```python
nums = [10, 20, 5, 8, 20, 15]
```

Expected Output:

```python
10
```

Requirements:

* Do not sort
* Handle duplicates
* Handle negative numbers

Test Cases:

```python
[10, 20, 5, 8, 20, 15] -> 10
[5, 5, 5] -> None
[1, 2] -> None
[-10, -5, -20, -1] -> -10
[3, 2, 1] -> 1

"""


def third_largest(nums):

    first=float('-inf')
    second=float('-inf')
    third=float('-inf')

    for i in nums:
        if i>first:

            third=second
            second=first
            first=i
        
        elif i>second and i!=first:
            third=second
            second=i
        elif i>third and i!=second and i!=first:
            third=i
    if third==float('-inf'):
        return None
    
    return third


print(third_largest([10, 20, 5, 8, 20, 15]))
print(third_largest([5, 5, 5]))
print(third_largest([1, 2]))
print(third_largest([-10, -5, -20, -1]))
print(third_largest([3, 2, 1] ))



#timecomp=O(n)
#SpaceCOMP=O(1)

#Remarks:This Solution is not soved by me i took it from AI as i wan not able to build the logic.



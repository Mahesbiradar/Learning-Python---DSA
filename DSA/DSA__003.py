

#🔹 1. Reverse Array (In-Place)
nums = [1,2,3,4,5]
# Output: [5,4,3,2,1]

#👉 Pattern: Two Pointer

right=len(nums)-1
left=0

while left<right:
    temp=nums[right]   
    nums[right]=nums[left]  #We can use two approches here nums[left],nums[right]=nums[right],nums[left] and one more used in solution
    nums[left]=temp 
    right-=1
    left+=1

print(nums)

"""
Dry Run
1.left=0,right=4 temp=5 left<right? True 
[5, 2, 3, 4, 1]
left=1
right=3


2.left=1,right=3 temp=4 left<right? True 
[5, 4, 3, 2, 1]
left=2
right=2

3. left<right? False Loop exits.

"""

#🔹 2. Left Rotate by 1
nums = [1,2,3,4,5]
# Output: [2,3,4,5,1]

#👉 Pattern: Element Shifting

left=nums[0]

for i in range(len(nums)-1):
    nums[i]=nums[i+1]
nums[-1]=left

print(nums)

"""
Dry Run
 left=1

 1.i=0 i+1=1
 [2,2,3,4,5]
 2.i=1,i+1=2
 [2,3,3,4,5]
 3.i=2,i+1=3
 [2,3,4,4,5]
 4.i=3,i+1=4
 [2,3,4,5,5] loop ends 

 [2,3,4,5,1]



"""

#🔹 3. Move Zeros to End
nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

#👉 Pattern: Two Pointer (Position)

pos=0

for i in nums:
    if i!=0:
        nums[pos]=i
        pos+=1
for i in range(pos,len(nums)):
    nums[i]=0
print(nums)

#Dry run and all things are done in notebook


#🔹 4. Check Palindrome Array
nums = [1,2,3,2,1]
# Output: True

#👉 Pattern: Two Pointer

is_polindrome=True

left=0
right=len(nums)-1

while left<right:
    if nums[left]!=nums[right]:
        is_polindrome=False
        break
    left+=1
    right-=1
print(is_polindrome)

#Dry run and all things are done in notebook



#🔹 5. Find Maximum Element
nums = [3,7,2,9,5]
# Output: 9

#👉 Pattern: Linear Traversal

max_val=nums[0]

for i in nums:
    if i>max_val:
        max_val=i
print(max_val)


#Dry run and all things are done in notebook


#🔹 6. Find Second Largest Element
nums = [10,5,8,20,15]
# Output: 15

#👉 Pattern: Tracking (max + second max)

max_val=nums[0]
second_max=float('-inf')

for i in nums:
    if i>max_val:
        second_max=max_val
        max_val=i
    elif i>second_max and i!=max_val:
        second_max=i

print(max_val,second_max)

#Dry run and all things are done in notebook

#🔹 7. Check if Array is Sorted
nums = [1,2,3,4,5] #→ True  
nums = [1,3,2,5] #→ False

#👉 Pattern: Adjacent comparison

#Again Confused and not able to think blocked here 

#🔹 8. Remove Duplicates (Manual)
nums = [1,2,2,3,4,4,5]
# Output: [1,2,3,4,5]

#👉 Pattern: Existence Check (Nested Loop)

seen=[]

for i in nums:
    found=False
    for j in seen:
        if i==j:
            found=True
            break
    if not found:
        seen.append(i)

print(seen)

#In this prolem i faces difficulty i was doing all things right but not intiated the found pointer so not geeting the o/p earliar seen last solver solution here

#🔹 9. Find Missing Number
nums = [1,2,4,5]
# Output: 3

#👉 Pattern: Existence Check

n=len(nums)

for i in range(1,n+1):
    found=True
    for j in nums:
        if i==j:
            found=False
            break
        
    if found:
        print(i)

#Here also i faces diffciculty with assigning found variable and  if found: print(i) what this excutes like at what level i was confuse

#🔹 10. Count Frequency of Element
nums = [1,3,4,1,5]
target = 1
# Output: 2

#👉 Pattern: Linear Traversal 

count=0

for i in nums:
    if i==target:
        count+=1
print(count)

#Seems easy and solverd early





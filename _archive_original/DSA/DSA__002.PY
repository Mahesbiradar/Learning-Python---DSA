# #🔹 3. Remove Duplicates (Manual)

# nums = [1,2,2,3,4,4,5]
# # Output: [1,2,3,4,5]

# seen=[]

# #the input is list of integers now we have to remove the duplicated.

# #will run a loop over list and append the elements in new list while cheking the elemet exist in new lis or not

# for i in nums:

#     found= False
#     for j in seen:
#         if i==j:
#             found=True
#             break
#     if not found:
#         seen.append(i)
# print(seen)

    

#1 i=1  i in seen? false seen=[1]
#2 i=2  i in seen? false seen=[1,2]
#3 i=2  i in seen? true seen=[1,2]
#4 i=3 i  in seen? false seen=[1,2,3]
#so on 



"""
2. Check if Array is Sorted
nums = [1,2,3,4,5] → True  
nums = [1,3,2,5] → False

👉 Hint:

Compare nums[i] with nums[i+1]

"""

#4. Find Missing Number
nums = [1,2,4,5]
# Output: 3

#👉 Hint:

#Check from 1 to n

n=len(nums)

for i in range(1,n+1):
    found=True
    for j in nums:
       if j==i:
           found=False
           break
    if found:
        print(i)
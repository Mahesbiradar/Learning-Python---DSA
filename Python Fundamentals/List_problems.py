#1. Find Maximum Element (Manual)

# nums = [3, 7, 2, 9, 5]

# # Output: 9

# max=0

# for i in nums:
#     if max<i:
#         max=i
#         # print(max)
# print(max)

#🔹 2. Find Second Largest Element
# nums = [10, 5, 8,16 ,20, 15]

# # Output: 15

# max=nums[0]
# second_max=nums[0]
# for i in nums:
#     if max<i:
#         max=i
#         # print(max)
#     second_max=i
#     # print(second_max)
# print(second_max)


#🔹 3. Check if List is Sorted

# nums = [1, 2, 3, 4, 5]
# # nums2 = [1, 3, 2, 5] 
# is_true=True

# for i in range(len(nums)-1):
#     if nums[i]>nums[i+1]:
#         is_true=False
#         break
# print(is_true)

#🔹 4. Remove Duplicates (Without Set)

# nums = [1,2,2,3,4,4,5]
# seen=[]

# for i in nums:
#     if i in seen:
#         continue
#     seen.append(i)
# print(seen)

#🔹 5. Count Frequency of Element

#Count how many times a number appears

# nums = [1,2,3,2,2,4]
# target = 2
# # Output: 3
# count=0

# for i in nums:
   
#     if target==i:
#         count+=1
# print(count)

#🔹 6. Left Rotate List by 1

# nums = [1,2,3,4,5]
# new=[]

# for i in range(len(nums)):



# #🔹 8. Find Missing Number
# nums = [1,2,2,3,3]

# n=5
# for i in range(1,n+1):
#     found=False
#     for j in nums:
#         if i==j:
#             found=True
#             break
#     if not found:
#         print(i)    
#         break
    
    







"""
## Concept Warm-Up (5 min)
Write the Running-State Tracking template from memory. No notes.

```python
# Running-State Tracking / Kadane

```
```python
# Running min/max state for product-style problems


"""

# Running-State Tracking / Kadane

# nums=[7,1,4,5,6,2]

# min_price=nums[0]
# max_profit=0

# for i in range(len(nums)):
#     if nums[i]<min_price:
#         min_price=nums[i]
#     else:
#         profit=nums[i]-min_price
#         if profit>max_profit:
#             max_profit=profit
# print(max_profit)

# #Kadane
# nums=[-2,1,-3,4,-1,2,1,-5,4]

# current_sum=nums[0]
# max_sum=float('-inf')

# for i in range(1,len(nums)):

#     current_sum=max(nums[i],current_sum+nums[i])

#     if current_sum>max_sum:
#         max_sum=current_sum
# print(max_sum)

# Running min/max state for product-style problems

def maxprod(nums):

   current_max=nums[0]
   current_min=nums[0]
   max_prod=nums[0]

   for i in range(1,len(nums)):
       
       temp_max=current_max
       temp_min=current_min

       current_max=max(nums[i],temp_max*nums[i],temp_min*nums[i])
       current_min=min(nums[i],temp_max*nums[i],temp_min*nums[i])

       max_prod=max(max_prod,current_max)

       print("i:-",nums[i],"current_max:-",current_max,"current_min:-",current_min,"max_prod:-",max_prod)
    
   return max_prod

print(maxprod([-2, 6, -3, -10, 0, 2]))
print(maxprod([-1, -3, -10, 0, 6]))


"""
### Valid Palindrome (LC 125)
Pattern: Two Pointers
Due: 3d recall
Constraint: 1 <= s.length <= 2 * 10^5; ignore non-alphanumeric characters and case.
Goal: Solve independently. If confident → submit to LC after.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""









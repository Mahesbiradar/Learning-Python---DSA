#Concept Warm-Up (5 min)


def binarysearch(nums,target):
   

    left=0
    right=len(nums)-1

    while left<=right:

        mid=(right+left)//2

        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

print(binarysearch([1,2,4,5,6,8,9],5))
print(binarysearch([1,2,4,5,6,8,9],7))

## Revision Problems (5 problems)

"""
### Product of Array Except Self (LC 238)
Pattern: Prefix Sum
Due: 7d final recall — overdue May 24
Constraint: 2 <= nums.length <= 10^5; -30 <= nums[i] <= 30; product of any prefix or suffix fits in 32-bit int.
Goal: Two-pass approach — left products + right products. No division allowed. Reproduce in under 3 minutes.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""


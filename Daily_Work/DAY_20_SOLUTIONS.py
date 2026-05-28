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
def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left=[1]

        for i in range(1,len(nums)):
            left.append(left[i-1]*nums[i-1])
        
        right=[None]*len(nums)

        right[-1]=1

        for j in range(len(nums)-2,-1,-1):
            right[j]=right[j+1]*nums[j+1]
        
        result=[]

        for k in range(len(nums)):
            result.append(left[k]*right[k])
        
        return result 
        
print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))

# Status:solved independent
# Time complexity:O(n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:Prefix product.

"""
### Maximum Average Subarray I (LC 643)
Pattern: Sliding Window
Due: 3d recall — overdue May 25
Constraint: 1 <= k <= n <= 10^5.
Goal: Fixed window of size k. Track window sum, update max average. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___


"""
def findMaxAverage(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        subarray_sum=0
        max_subarray=float('-inf')
        left=0

        for right in range(len(nums)):

            subarray_sum+=nums[right]

            while right-left+1>k:
                subarray_sum-=nums[left]
                left+=1
            
            if right-left+1>=k:
                max_subarray=max(max_subarray,subarray_sum)
        return max_subarray/float(k)

print(findMaxAverage([1,12,-5,-6,50,3],4))
print(findMaxAverage([5],1))

# Status:solved independent
# Time complexity:O(n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:sliding window
#core invariat: right-left+1>k


"""
### Binary Search (LC 704)
Pattern: Binary Search
Due: 24h revision — May 26
Constraint: 1 <= nums.length <= 10^4; nums sorted ascending; all unique.
Goal: Standard template — `left <= right`, `mid = left + (right - left) // 2`, return -1 if not found.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""
def search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
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

print(search([-1,0,3,5,9,12],9))
print(search([-1,0,3,5,9,12],2))

# Status:solved independent
# Time complexity:O(log n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:binary search


"""
### Search Insert Position (LC 35)
Pattern: Binary Search
Due: 24h revision — May 26
Constraint: 1 <= nums.length <= 10^4; distinct values sorted ascending.
Goal: Lower-bound variant — `left < right`, post-loop return `left`. Handle insert-at-end case.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___
"""

def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
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
        return left

print(searchInsert([1,3,5,6],5))
print(searchInsert([1,3,5,6],2))
print(searchInsert([1,3,5,6],7))

# Status:solved independent
# Time complexity:O(log n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:binary search

"""
### First Bad Version (LC 278)
Pattern: Binary Search
Due: 24h revision — May 26
Constraint: 1 <= bad <= n <= 2^31 - 1.
Goal: Lower-bound on predicate — `left < right`, `right = mid` when bad, `left = mid + 1` when good. Minimize API calls.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""
bad = 4

def isBadVersion(version):
    return version >= bad
     

def firstBadVersion(n):
        """
        :type n: int
        :rtype: int
        """
        left=0
        right=n

        while left<right:

            mid=(right+left)//2

            if isBadVersion(mid):
                right=mid
            else:
                left=mid+1
        return left

print(firstBadVersion(5))
print(firstBadVersion(1))

# Status:solved independent
# Time complexity:O(log n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:binary search


## New Problems (3 problems, local only)

"""
### Sqrt(x) (LC 69)
Pattern: Binary Search
Difficulty: Easy

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Constraints:
- 0 <= x <= 2^31 - 1

"""

def Sqrt(x):
     
    right=x

    left=0
    best=0

    while left<=right:
         
        mid=(right+left)//2
        print(mid,"mid",left,"left",right,"right")

        if mid*mid==x:
            return mid
        elif mid*mid<x:
            best=mid
            left=mid+1
        else:
            right=mid-1
    return best

print("SQRT")
# print(Sqrt(4))
print(Sqrt(8))

# Status:solved with hints
# Time complexity:O(log n)
# Space complexity:O(1)
# LC status:NA
# mistakes/confusion:NA
# Pattern:binary search

"""
### Find Smallest Letter Greater Than Target (LC 744)
Pattern: Binary Search
Difficulty: Easy

You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

Example 1:
Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

Example 2:
Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

Example 3:
Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that are lexicographically greater than 'z', so we return letters[0].

Constraints:
- 2 <= letters.length <= 10^4
- letters[i] is a lowercase English letter
- letters is sorted in non-decreasing order
- letters contains at least two different characters

"""



         
    
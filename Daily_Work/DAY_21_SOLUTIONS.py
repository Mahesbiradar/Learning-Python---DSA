## Concept Warm-Up (5 min)
# Lower-bound Binary Search (left < right)

#First occurance of target
nums=[0,0,0,1,1,1]

target=1

left=0
right=len(nums)-1

while left<right:

    mid=(right+left)//2

    if nums[mid]<target:
        left=mid+1
    else:
        right=mid
print(left)


## Revision Problems (5 problems)

"""
### Group Anagrams (LC 49)
Pattern: Grouping Hash Maps
Due: 14d recall — OVERDUE 2 days (was due May 24)
Constraint: 1 <= strs.length <= 10^4; 0 <= strs[i].length <= 100
Goal: Hash map with sorted tuple key. Group strings by character frequency signature. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        seen={}
        
        for i in range(len(strs)):

            sorted_i=sorted(strs[i])

            string_i="".join(sorted_i)

            if string_i in seen:
                seen[string_i]+=[strs[i]]
            else:
                seen[string_i]=[strs[i]]
        return seen.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams(["a"]))

# Status: solved independent 
# Time complexity:O(n+m lon m)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:Na
# Pattern:Frequncy Hashing.

"""
### Find Highest Altitude (LC 1732)
Pattern: Prefix Sum
Due: 7d final recall — OVERDUE 1 day (was due May 25)
Constraint: n == gain.length; 1 <= n <= 100; -100 <= gain[i] <= 100
Goal: Running prefix sum starting at 0, track max altitude encountered. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___


"""
        

def largestAltitude(gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current_alt=0
        max_alt=0

        for i in range(len(gain)):
            current_alt+=gain[i]

            if current_alt>max_alt:
                max_alt=current_alt
        return max_alt

print(largestAltitude([-5,1,5,0,-7]))
print(largestAltitude([-4,-3,-2,-1,4,3,2]))

# Status: solved independent 
# Time complexity:O(n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:Na
# Pattern:Prefix sum

"""
### Sqrt(x) (LC 69)
Pattern: Binary Search
Due: 24h revision — May 27
Constraint: 0 <= x <= 2^31 - 1
Goal: Lower-bound binary search. Predicate: mid*mid <= x. Track best valid mid. Use `left <= right` or `left < right` with best tracker. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

def mySqrt(x):
        """
        :type x: int
        :rtype: int
        """
        left=0
        right=x
        ans=None

        while left<=right:

            mid=(right+left)//2

            if mid*mid>x:
                right=mid-1
            else:
                ans=mid
                left=mid+1
        return ans

print(mySqrt(8))
print(mySqrt(9))

# Status:Solved independent
# Time complexity:O(log n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:Na
# Pattern:binary search.


"""
### Find Smallest Letter Greater Than Target (LC 744)
Pattern: Binary Search
Due: 24h revision — May 27
Constraint: 2 <= letters.length <= 10^4; sorted non-decreasing; at least two different characters
Goal: Lower-bound variant — find first element > target. If none found, wrap to letters[0]. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""
def nextGreatestLetter(letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left=0
        right=len(letters)-1
        ans=None

        while left<=right:

            mid=(right+left)//2

            if letters[mid]>target:
                ans=letters[mid]
                right=mid-1
            else:
                left=mid+1
            
        if ans==None:
            return letters[0]
        else:
            return ans
print(nextGreatestLetter(["c","f","j"],"a"))
print(nextGreatestLetter( ["c","f","j"],"c"))
print(nextGreatestLetter( ["x","x","y","y"],"z"))


# Status:Solved with some hints
# Time complexity:O(log n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:Na
# Pattern:binary search.

"""
### Find Peak Element (LC 162)
Pattern: Binary Search
Due: 24h revision — May 27
Constraint: 1 <= nums.length <= 1000; nums[i] != nums[i+1]
Goal: Compare mid with mid+1. If ascending, peak is right; else peak is left (including mid). `left < right`, return left. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

def findPeakElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1

        while left<right:

            mid=(right+left)//2

            if nums[mid]<nums[mid+1]:
                left=mid+1
            else:
                right=mid
        return right

print(findPeakElement([1,2,3,1]))
print(findPeakElement([1,2,1,3,5,6,4]))

# Status:Solved with some hints
# Time complexity:O(log n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:Na
# Pattern:binary search.

"""
## New Problems (3 problems, local only)

### Valid Perfect Square (LC 367)
Pattern: Binary Search
Difficulty: Easy

Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in exponent function or operator.

Example 1:
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:
Input: num = 14
Output: false
Explanation: We return false because 3.741 * 3.741 = 14 and 3.741 is not an integer.

Constraints:
- 1 <= num <= 2^31 - 1


"""

def Valid_Perfect_Square(num):
     
     left=0
     right=num
     while left<=right:
          
          mid=(right+left)//2

          if mid*mid==num:
               return True
          elif mid*mid>num:
               right=mid-1
          else:
               left=mid+1
     return False

print(Valid_Perfect_Square(16))
print(Valid_Perfect_Square(14))
print(Valid_Perfect_Square(25))


# Status:Solved independent
# Time complexity:O(log n)
# Space complexity:O(1)
# LC status:NA
# mistakes/confusion:Na
# Pattern:binary search.

"""

### Arranging Coins (LC 441)
Pattern: Binary Search
Difficulty: Easy

You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Example 1:
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

Example 2:
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.

Constraints:
- 1 <= n <= 2^31 - 1

"""

def arranging_coins(n):
     
     left=0
     right=n
     ans=0

     while left<=right:
          
          mid=(right+left)//2
          k=(mid*(mid+1))//2

          if k>n:
            right=mid-1
          else:
            ans=mid
            left=mid+1
     return ans

print(arranging_coins(8))
print(arranging_coins(10))
print(arranging_coins(14))

# Status:Solved with hints.
# Time complexity:O(log n)
# Space complexity:O(1)
# LC status:NA
# mistakes/confusion:Na
# Pattern:binary search.

"""
### Guess Number Higher or Lower (LC 374)
Pattern: Binary Search
Difficulty: Easy

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:
- -1: Your guess is higher than the number I picked (i.e. num > pick).
- 1: Your guess is lower than the number I picked (i.e. num < pick).
- 0: Your guess is equal to the number I picked (i.e. num == pick).

Return the number that I picked.

Example 1:
Input: n = 10, pick = 6
Output: 6

Example 2:
Input: n = 1, pick = 1
Output: 1

Example 3:
Input: n = 2, pick = 1
Output: 1

Constraints:
- 1 <= n <= 2^31 - 1
- 1 <= pick <= n


"""

pick=101

def guess(num):
     
     if num>pick:
          return -1
     elif num<pick:
          return 1
     else:
          return 0

def guessnumber(n):
     
     left=1
     right=n

     while left<=right:
          
          mid=(right+left)//2
          print(mid,"mid")

          if guess(mid)==-1:
               right=mid-1
          elif guess(mid)==0:
               return mid
          elif guess(mid)==1:
               left=mid+1


print(guessnumber(1000))


# Status:Solved with hints.
# Time complexity:O(log n)
# Space complexity:O(1)
# LC status:NA
# mistakes/confusion:Na
# Pattern:binary search.







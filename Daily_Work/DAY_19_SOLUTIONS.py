## Concept Warm-Up (5 min)

# Binary Search — standard template
nums=[1,2,4,6,8,9]
target=9

left=0
right=len(nums)-1

while left<=right:

    mid=(right+left)//2

    if nums[mid]==target:
        print(mid)
        break
    elif nums[mid]<target:
        left=mid+1
    else:
        right=mid-1
else:
    print("-1")


## Revision Problems (5 problems)

"""
### First Unique Character in a String (LC 387)
Pattern: Frequency Hashing
Due: 7d final recall — overdue May 25
Constraint: 1 <= s.length <= 10^5; s consists of only lowercase English letters.
Goal: One-pass frequency dict + second-pass index check. Reproduce in under 3 minutes.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""
#Brute Force using nested loop.
def firstUniqChar(s):

    for i in range(len(s)):

        count=0

        for j in range(len(s)):

            if s[i]==s[j]:
                count+=1
        
        if count==1:
            return i

    return -1

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))

#optimized version.

def firstUniqChar(s):

    seen={}

    for i in s:
        seen[i]=seen.get(i,0)+1
    
    for i in range(len(s)):

        if seen[s[i]]==1:
            return i
    return -1

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))

# Status:solved independent
# Time complexity:O(n)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:Frequency Hashing.

"""
### Best Time to Buy and Sell Stock (LC 121)
Pattern: Running-State Tracking
Due: 7d final recall — overdue May 25
Constraint: 1 <= prices.length <= 10^5; 0 <= prices[i] <= 10^4.
Goal: Track min_price and max_profit in one pass. Kadane-style state transition.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        min_price=float('inf')

        for i in range(len(prices)):

            if prices[i]<min_price:
                min_price=prices[i]
            else:
                profit=prices[i]-min_price

                if profit>max_profit:
                    max_profit=profit
        return max_profit


print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))

# Status:solved independent
# Time complexity:O(n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:Complement lookup

"""
### Running Sum of 1d Array (LC 1480)
Pattern: Prefix Sum
Due: 7d final recall — overdue May 25
Constraint: 1 <= nums.length <= 1000; -10^6 <= nums[i] <= 10^6.
Goal: In-place or new array — both O(n). Verify edge case: length 1.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

def runningSum(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[nums[0]]

        for i in range(1,len(nums)):
            result.append(result[i-1]+nums[i])
        
        return result

print(runningSum([1,2,3,4]))
print(runningSum([1,1,1,1,1]))
print(runningSum([3,1,2,10,1]))


# Status:solved independent
# Time complexity:O(n)
# Space complexity:O(1)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:running sum

"""
### Longest Repeating Character Replacement (LC 424)
Pattern: Sliding Window
Due: 3d recall — due May 26
Constraint: 1 <= s.length <= 10^5; 0 <= k <= s.length; s consists of only uppercase English letters.
Goal: Variable window — `max_freq` tracks dominant char, `window_len - max_freq <= k` is the invariant. Reproduce independently.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""
def characterReplacement(s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_frqe=0
        seen={}
        best=0
        left=0

        for right in range(len(s)):
            seen[s[right]]=seen.get(s[right],0)+1

            max_frqe=max(seen.values())

            while (right-left+1)-max_frqe>k:
                seen[s[left]]-=1

                if seen[s[left]]==0:
                    del seen[s[left]]
                left+=1

            best=max(best,right-left+1)
        
        return best

print(characterReplacement("ABAB",2))
print(characterReplacement("AABABBA",1))

# Status:solved independent
# Time complexity:O(n)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:sliding window
#Core invariant:(right-left+1)-max_frqe>k
#Pattern trigger: Longets repeating character replacement.

"""
### Permutation in String (LC 567)
Pattern: Sliding Window
Due: 3d recall — due May 26
Constraint: 1 <= s1.length, s2.length <= 10^4; both lowercase English letters.
Goal: Fixed window of `len(s1)`, frequency map comparison. Focus: delete key when count hits 0.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""
def checkInclusion(s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        seen_s1={}

        for i in s1:
            seen_s1[i]=seen_s1.get(i,0)+1
        
        seen_s2={}

        left=0

        for right in range(len(s2)):
            seen_s2[s2[right]]=seen_s2.get(s2[right],0)+1

            if right-left+1>len(s1):
                seen_s2[s2[left]]-=1

                if seen_s2[s2[left]]==0:
                    del seen_s2[s2[left]]
                left+=1
            
            if seen_s1==seen_s2:
                return True
        return False

print(checkInclusion("ab","eidbaooo"))
print(checkInclusion("ab","eidboaoo"))

# Status:solved independent
# Time complexity:O(n)
# Space complexity:O(n)
# LC status:Accepted
# mistakes/confusion:NA
# Pattern:sliding window
#Core invariant:right-left+1>len(s1


## New Problems (3 problems, local only)


"""
### Binary Search (LC 704)
Pattern: Binary Search
Difficulty: Easy

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in `nums` are unique.
- `nums` is sorted in ascending order.

"""
def binaryserach(nums,target):
     
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

print(binaryserach([-1,0,3,5,9,12],9))
print(binaryserach([-1,0,3,5,9,12],2))

# Status:solved independent
# Time complexity:O(log n)
# Space complexity:O(1)
# LC status:NA
# mistakes/confusion:NA
# Pattern:Binary search
#Core invariant:mid=right+left//2

"""
### Search Insert Position (LC 35)
Pattern: Binary Search
Difficulty: Easy

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- `nums` contains distinct values sorted in ascending order.
- -10^4 <= target <= 10^4

"""

def binaryserach(nums,target):
     
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
     return mid+1


print(binaryserach([-1,0,3,5,9,12],9))
print(binaryserach([-1,0,3,5,9,12],2))
print(binaryserach([1,3,5,6],5))
print(binaryserach([1,3,5,6],2))
print(binaryserach([1,3,5,6],7))

# Status:solved independent
# Time complexity:O(log n)
# Space complexity:O(1)
# LC status:NA
# mistakes/confusion:NA
# Pattern:Binary search
#Core invariant:mid=right+left//2

"""
### First Bad Version (LC 278)
Pattern: Binary Search
Difficulty: Easy

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1

Constraints:
- 1 <= bad <= n <= 2^31 - 1

"""
bad = 4

def isBadVersion(version):
    return version >= bad


def firstBadVersion(n):

    left = 1
    right = n

    while left < right:

        mid = (left + right) // 2

        if isBadVersion(mid):

            right = mid

        else:

            left = mid + 1

    return left


print(firstBadVersion(5))

# Status:solved by seen the solution
# Time complexity:O(log n)
# Space complexity:O(1)
# LC status:NA
# mistakes/confusion:NA
# Pattern:Binary search
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



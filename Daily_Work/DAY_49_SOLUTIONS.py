
# Note : If any problem solution contains Brute Force unless it was asked consider it as for just practice not for evaluation

## Warm-up Protocol (Monotonic Stack)

# 1. Write the monotonic-stack template from memory.

def monotonicstack(nums1,nums2):

    seen ={}

    stack = []

    for i in nums2:

        while stack and i > stack[-1]:
            seen[stack-1] = i

            stack.pop()

        stack.append(i)

    answer = []

    for j in nums1:

        if j in seen:
            answer.append(seen[j])
        else:
            answer.append(-1)

    return answer

#Since i can memorize the template so i took 1 Problems based on that problems i made this template of monotonic stack

# 2. Answer in one sentence: "The invariant this template maintains is: The new element can be the answer for prev elements"

# 3. Answer in one sentence: "If I changed `while stack and current > stack[-1]` to `while stack and current >= stack[-1]`, it would fail because: since we are in search of greater element and if we change to >= this become produce wrong answer."


"""
### 1. LC 496 — Next Greater Element I
**Tier:** 1 | **Pattern:** Monotonic Stack | **Variant:** Next greater element | **Due:** Jul 29
"""
#Brute Force.

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        answer = []

        for i in nums1:

            idx = None 

            for j in range(len(nums2)):

                if i == nums2[j]:
                    idx = j
                    break
            
            for k in range(idx+1,len(nums2)):

                if nums2[k] > i:
                    answer.append(nums2[k])
                    break
            else:
                answer.append(-1)
        
        return answer

#Dont consider for evaliation since i solved it for just practice.


# optimal solution 

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        stack = []

        seen ={}

        for i in nums2:

            while stack and i > stack[-1]:

                seen[stack[-1]] = i

                stack.pop()

            stack.append(i) 
        
        answer = []

        for j in nums1:

            if j in seen:
                answer.append(seen[j])
            else:
                answer.append(-1)
        
        return answer

# Status: Independent
# Time taken: 20 min
# Time complexity: O(n) — one pass over nums1 and nums2 
# Space complexity: O(n) — additional hashmap + list was used 
# Submitted to LC: Yes
# Result: Accepted 
# Pattern: stack
# Variant: monotonic stack
# mistakes/confusion: Na

"""
### 2. LC 739 — Daily Temperatures
**Tier:** 2 | **Pattern:** Monotonic Stack | **Variant:** Next greater element | **Due:** Jul 28


"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(temperatures)

        stack = []
        
        nums = temperatures

        for i in range(len(nums)):

            while stack and nums[i] > nums[stack[-1]]:

                answer[stack[-1]] = i-stack[-1]
                stack.pop()

            stack.append(i)
        
        return answer


# Status: Independent
# Time taken: 10 min
# Time complexity: O(n) — one pass over list and each element is pushed and poped once.
# Space complexity: O(n) —  additional list was used for the answer
# Submitted to LC: Yes
# Result: Accepted 
# Pattern: stack
# Variant: monotonic stack
# mistakes/confusion: Na

"""
### 3. LC 234 — Palindrome Linked List
**Tier:** 3 | **Pattern:** Linked List | **Variant:** In-place manipulation — Palindrome check / reverse second half | **Due:** Jul 23


"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head and not head.next:
            return False 

        slow = head
        fast = head
        # prev = None 

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # prev.next = None
        current = slow
        prev = None 

        while current:

            next_node = current.next
            current.next= prev
            prev = current
            current = next_node
        
        left = head
        right = prev

        while left and right:

            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
        return True


# Status: Independent
# Time taken: 18 min
# Time complexity: O(n) — one pass over the linked list
# Space complexity: O(1) — in place rewiring no additional linked was used 
# Submitted to LC: Yes
# Result: Accepted 
# Pattern: linked list
# Variant: Fast and slow pointer + revarsal
# mistakes/confusion: Na

"""
### 4. LC 1207 — Unique Number of Occurrences
**Tier:** 3 | **Pattern:** Frequency Hashing | **Variant:** Count+query | **Due:** Jul 28

"""

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = {}

        for i in arr:
            freq[i] = freq.get(i,0)+1
        
        isduplicate = set()

        for key,value in freq.items():

            if value in isduplicate:
                return False
            else:
                isduplicate.add(value)
        return True

# Status: Independent
# Time taken: 10 min
# Time complexity: O(n) — one pass over the list
# Space complexity: O(n) — has map is used to store the frequnecy and to detect the duplicay of values.
# Submitted to LC: Yes
# Result: Accepted 
# Pattern: Frequency Hasing + 
# Variant: count + query
# mistakes/confusion: Na

"""
### 5. LC 205 — Isomorphic Strings
**Tier:** 3 | **Pattern:** Grouping Hash Map | **Variant:** Canonical key | **Due:** Jul 28

"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        seen_s = {}

        seen_t = {}

        for i in range(len(s)):

            if s[i] in seen_s and seen_s[s[i]] != t[i]:
                return False
            else:
                seen_s[s[i]] = t[i]
            
            if t[i] in seen_t and seen_t[t[i]] != s[i]:
                return False
            else:
                seen_t[t[i]] = s[i]
        return True

# Status: Independent
# Time taken: 10 min
# Time complexity: O(n) — one pass over the both the strings
# Space complexity: O(n) — has map is used to map the alphabest from one string to another
# Result: Accepted 
# Pattern: Grouping Hash Map
# Variant: Canonical key
# mistakes/confusion: Na

"""
### 6. LC 523 — Continuous Subarray Sum
**Tier:** 3 | **Pattern:** Prefix Sum | **Variant:** Modulo | **Due:** Jul 28

"""

#brute Force: dont consider for the evaluation i solved just for the practice.

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        for i in range(len(nums)):

            prefix = 0

            for j in range(i,len(nums)):

                prefix += nums[j]
                
                if prefix % k == 0 and j-i+1 > 1:
                    return True
        
        return False

#optimal solution.

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {0:-1}

        prefix = 0

        for i in range(len(nums)):

            prefix += nums[i]

            remainder = prefix % k

            if remainder in seen:
                
                if i-seen[remainder] > 1:
                    return True
            else:
                seen[remainder] = i

        return False 

# Status: Independent
# Time taken: 15 min
# Time complexity: O(n) — one pass over the list nums
# Space complexity: O(n) — has map is used to store the reaminder and its index.
# Result: Accepted 
# Pattern: prefix sum
# Variant: modulo
# mistakes/confusion: Na

"""
### 7. LC 27 — Remove Element
**Tier:** 3 | **Pattern:** Two Pointers | **Variant:** Write pointer | **Due:** Jul 28

"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        write = 0

        for i in range(len(nums)):

            if nums[i] != val:
                nums[write] = nums[i]
                write += 1

        return write

# Status: Independent
# Time taken: 10 min
# Time complexity: O(n) — one pass over the list nums
# Space complexity: O(1) — the list manipulation done in-place.
# Result: Accepted 
# Pattern: Two pointers
# Variant: write pointer
# mistakes/confusion: Na

"""
### 8. LC 11 — Container With Most Water
**Tier:** 3 | **Pattern:** Two Pointers | **Variant:** Maximize/minimize | **Due:** Jul 28

"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        max_water = 0

        while left < right :

            water = min(height[left],height[right]) * (right-left)

            if height[right] >= height[left]:
                left += 1
            else:
                right -= 1

            max_water = max(max_water,water)

        return max_water

# Status: Independent
# Time taken: 10 min
# Time complexity: O(n) — one pass over the list
# Space complexity: O(1) — varibale used to store the answer
# Result: Accepted 
# Pattern: Two pointers
# Variant: Maximize/minimize
# mistakes/confusion: Na

"""
### 9. LC 974 — Subarray Sums Divisible by K
**Tier:** 3 | **Pattern:** Prefix Sum | **Variant:** Modulo | **Due:** Jul 28

"""

#Brute Force

class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count_subarray = 0

        for i in range(len(nums)):

            prefix = 0

            for j in range(i,len(nums)):

                prefix += nums[j]

                if prefix % k == 0:

                    count_subarray += 1

        return count_subarray


#Optimal

class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        seen = {0:1}

        prefix = 0

        count_subarray = 0

        for i in range(len(nums)):

            prefix += nums[i]

            remainder = prefix % k

            if remainder in seen:
                count_subarray += seen[remainder]
            
            seen[remainder] = seen.get(remainder,0)+1

        return count_subarray

# Status: Independent
# Time taken: 10 min
# Time complexity: O(n) — one pass over the list
# Space complexity: O(n) — hash map is used to store the remainders with its freq
# Result: Accepted 
# Pattern: Prefix sum
# Variant: modulo
# mistakes/confusion: Na

"""
### 10. LC 1590 — Make Sum Divisible by P
**Tier:** 3 | **Pattern:** Prefix Sum | **Variant:** Modulo | **Due:** Jul 28
"""

#Brute Force:

class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        totalsum = sum(nums)

        target = totalsum % p

        if target == 0:
            return 0

        valid_subarry = len(nums)

        for i in range(len(nums)):

            prefix = 0

            for j in range(i,len(nums)):

                prefix += nums[j]

                if prefix == target:
                    length = j-i+1
                    valid_subarry = min(valid_subarry,length)

        return valid_subarry

# Optimal:

class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        totalsum = sum(nums)

        target = totalsum % p

        if target == 0:
            return 0

        valid_subarry = len(nums)

        prefix = 0

        seen ={0:-1}

        for i in range(len(nums)):

            prefix += nums[i]

            current = prefix % p

            needed = (current-target) % p

            if needed in seen:

                valid_subarry = min(valid_subarry, i-seen[needed])
            
            seen[current] = i

        return -1 if valid_subarry == len(nums) else valid_subarry

# Status: Independent
# Time taken: 10 min
# Time complexity: O(n) — one pass over the list
# Space complexity: O(n) — hash map is used to store the remainders with its idx
# Result: Accepted 
# Pattern: Prefix sum
# Variant: modulo
# mistakes/confusion: Na


"""
### 11. LC 875 — Koko Eating Bananas
**Tier:** 3 | **Pattern:** Binary Search | **Variant:** Applied — boundary/feasibility | **Due:** Jul 29

"""

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def isfeasible(speed):

            cout_of_hrs = 0

            for i in piles:

                div = i // speed
                rem = 0 if i % speed == 0 else 1

                cout_of_hrs += div + rem
            
            return False if cout_of_hrs > h else True
        
        left = 1
        right = max(piles)

        while left < right :

            mid = (right+left)//2

            if isfeasible(mid):
                right = mid
            else:
                left = mid + 1

        return left

# Status: Independent
# Time taken: 15 min
# Time complexity: O(nlogm) — with each number the funsction visiting each elemenet in piles
# Space complexity: O(1) — no additional data structure is used
# Submitted to LC: Yes 
# Result: Accepted
# Pattern: Binary seach
# Variant: Koko Eating Bananas
# mistakes/confusion: Na

"""
### 12. LC 125 — Valid Palindrome
**Tier:** 4 | **Pattern:** Two Pointers | **Variant:** Opposite ends | **Due:** Jul 20 (template recall)

"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s)-1

        while left < right :

            while left < right and  not s[left].isalnum():
                left += 1
            
            while left < right and not s[right].isalnum():

                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        return True 


# Status: Independent
# Time taken: 10 min
# Time complexity: O(n) — single pass over a string s
# Space complexity: O(1) — varibales are used 
# Submitted to LC: Yes 
# Result: Accepted
# Pattern: Two pointers
# Variant: Opposite ends
# mistakes/confusion: Na


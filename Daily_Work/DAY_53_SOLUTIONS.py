### Tier 4 Template Recalls

# 5. **LC 3 — Longest Substring Without Repeating Characters**
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()

        left = 0

        max_len = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                
            seen.add(s[right])

            max_len = max(max_len,right-left+1)

        return max_len

# Status: independent
# Time Taken: 15
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Sliding window
# Variant: Variable size
# Mistakes / Confusion:Na

# 6. **LC 238 — Product of Array Except Self**

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1]

        for i in range(1,len(nums)):
            left.append(left[i-1]*nums[i-1])
        right = [1]*len(nums)

        for j in range(len(right)-2,-1,-1):
            right[j] = right[j+1]*nums[j+1]
        
        result = []

        for k in range(len(nums)):
            result.append(right[k]*left[k])
        
        return result

# Status: independent
# Time Taken: 10
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:prefix sum
# Variant: pivot
# Mistakes / Confusion:Na

### Tier 3 Revisions

# 7. **LC 1 — Two Sum**

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen ={}

        for i in range(len(nums)):

            needed = target - nums[i]

            if needed in seen:
                return [seen[needed],i]
            
            seen[nums[i]] = i

# Status: independent
# Time Taken: 3
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Complement Lookup
# Variant: Hash map
# Mistakes / Confusion:Na

# 8. **LC 303 — Range Sum Query**
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = [0]

        for i in range(len(nums)):
            self.prefix.append(self.prefix[i]+nums[i])
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix[right+1]-self.prefix[left]

# Status: independent
# Time Taken: 8
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:prefix sum
# Variant: ramge query 
# Mistakes / Confusion:Na

# 9. **LC 128 — Longest Consecutive Sequence**

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sequence = set()

        for i in nums:
            sequence.add(i)

        max_sequence = 0
        
        for j in sequence:

            if j-1 not in sequence:

                num = j
                length = 1

                while num+1 in sequence:
                    num += 1
                    length += 1
                
                max_sequence = max(max_sequence,length)
        
        return max_sequence

# Status: independent
# Time Taken: 10
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: Has set 
# Variant: sequnce expansion 
# Mistakes / Confusion:Na

# 15. **LC 1456 — Maximum Number of Vowels**

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        max_vowels = 0
        count = 0

        for right in range(len(s)):

            if s[right] in ['a','i','o','u','e']:
                count += 1
            
            while right-left+1 > k:

                if s[left] in ['a','i','o','u','e']:
                    count -= 1
                left += 1
            if right-left+1 == k:
                max_vowels = max(max_vowels,count)
        return max_vowels


# Status: independent
# Time Taken: 5
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: sliding window
# Variant: fixed size 
# Mistakes / Confusion:Na

# 16. **LC 1207 — Unique Number of Occurrences**

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occurances = {}

        for i in arr:
            occurances[i] =occurances.get(i,0)+1
        
        seen = set()

        for key,value in occurances.items():

            if value in seen:
                return False
            
            seen.add(value)

        return True
# Status: independent
# Time Taken: 8
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: Frequncy hashing + query
# Variant: Unique Number of Occurrences
# Mistakes / Confusion:Na

# 17. **LC 205 — Isomorphic Strings**

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        seen_s ={}

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
    
# Status: independent
# Time Taken: 4
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: Frequncy hashing 
# Variant: isomorphic string
# Mistakes / Confusion:Na


# 18. **LC 739 — Daily Temperatures**

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0]*len(temperatures)
        stack = []

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:

                answer[stack[-1]] = i-stack[-1]

                stack.pop()     


            stack.append(i)

        return answer

# Status: independent
# Time Taken: 7
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: stack 
# Variant: monotonic stack
# Mistakes / Confusion:Na

# 19. **LC 496 — Next Greater Element I**

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        seen ={}
        stack = []
        for i in nums2:

            while stack and i > stack[-1]:

                seen[stack[-1]] = i
                stack.pop()
            
            stack.append(i)
        
        answer = [-1]*len(nums1)

        for j in range(len(nums1)):

            if nums1[j] in seen:
                answer[j] = seen[nums1[j]]
        
        return answer


# Status: independent
# Time Taken: 7
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: stack 
# Variant: monotonic stack
# Mistakes / Confusion:Na

# 20. **LC 523 — Continuous Subarray Sum**

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

            needed = prefix % k

            if needed in seen:

                if i-seen[needed] > 1:
                    return True
            else:

                seen[needed] = i
        return False

# Status: independent
# Time Taken: 5
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: prefix sum 
# Variant: modulo
# Mistakes / Confusion:Na

# 10. **LC 206 — Reverse Linked List**

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
    
        prev = None
        current = head

        while current:

            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev

# Status: independent
# Time Taken: 6
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: linked list 
# Variant: reversal
# Mistakes / Confusion:Na

# 12. **LC 21 — Merge Two Sorted Lists**
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)

        current = dummy

        while list1 and list2:

            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        current.next = list1 if list1 else list2

        return dummy.next

# Status: independent
# Time Taken: 5
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: linked list 
# Variant: Two nodes reconnection
# Mistakes / Confusion:Na

# 13. **LC 19 — Remove Nth Node From End**

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy

        position = 0
        
        while position < n:
            fast = fast.next
            position += 1

        slow = dummy

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next


# Status: independent
# Time Taken: 20
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: linked list 
# Variant: Fast ans slow pointers
# Mistakes / Confusion:Na

# 14. **LC 2130 — Maximum Twin Sum of a Linked List**

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        fast = head
        slow = head
        prev = None

        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None

        prev = None
        current = slow

        while current:

            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        right = prev
        left = head

        twinsum = 0

        while right:
            sum_of = left.val + right.val
            right = right.next
            left = left.next
            twinsum = max(twinsum,sum_of)
        return twinsum


# Status: independent
# Time Taken: 10
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: linked list 
# Variant: Fast ans slow pointers + reversal
# Mistakes / Confusion:Na

# 11. **LC 92 — Reverse Linked List II**

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        current = head
        position = 1

        while position < left:
            prev = current
            current = current.next
            position +=1
        
        before_left = prev
        left_node = current

        n= right-left + 1

        prev = None
        current = left_node
        while n > 0:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            n -= 1
        
        before_left.next = prev
        left_node.next = current

        return dummy.next


# Status: independent
# Time Taken: 10
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: linked list 
# Variant: in b/w reversal and reconnection
# Mistakes / Confusion:Na




### Tier 2
# 2. **LC 503 — Next Greater Element II**

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack =[]

        answer = [-1]*len(nums)

        n = len(nums)

        for i in range(n*2):

            while stack and nums[i%n] > nums[stack[-1]]:

                answer[stack[-1]] = nums[i%n]
                stack.pop() 
            if i < n:
                stack.append(i)
        return answer

# Status: independent
# Time Taken: 20
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: stack
# Variant: Monotonic stack
# Mistakes / Confusion:Na


### Tier 1

# 1. **LC 84 — Largest Rectangle in Histogram**

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        nse = [len(heights)]*len(heights)

        stack=[]

        for i in range(len(heights)):

            while stack and heights[i] <=  heights[stack[-1]]:

                nse[stack[-1]] = i
                stack.pop()
            
            stack.append(i)
        
        pse = [-1]*len(heights)

        stack = []

        for j in range(len(heights)):

            while stack and heights[stack[-1]] >= heights[j] :

                # pse[stack[-1]] = j

                stack.pop()
            if stack:
                pse[j] = stack[-1]
                
            stack.append(j)

        output = 0

        for k in range(len(heights)):

            width = nse[k]-pse[k]-1
          
            area = width * heights[k]
            
            output = max(output,area)
        return output

# Status: hint
# Time Taken: 25
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: stack
# Variant: Monotonic stack
# Mistakes / Confusion:Na

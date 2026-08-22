

# 1. LC 169 — Majority Element


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}

        for i in nums:
            freq[i] = freq.get(i,0)+1
        
        Major_element = None
        frequnecy = 0

        for key,value in freq.items():

            if value > frequnecy:
                Major_element = key
                frequnecy = value
        
        return Major_element

# Status: Independent
# Time Taken: 5m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Frequnecy Hashing
# Variant: Major element
# Mistakes / Confusion:Na

# 2. LC 344 — Reverse String

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        left = 0
        right = len(s)-1

        while left < right:

            s[left],s[right] = s[right],s[left]

            left += 1
            right -= 1


# Status: Independent
# Time Taken: 3m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Two pointers
# Variant: In-place reversal
# Mistakes / Confusion:Na

### Tier 2

# 1. LC 283 -- Move Zeroes

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        write = 0

        for i in range(len(nums)):

            if nums[i] != 0:
                nums[write] = nums[i]
                write += 1
        
        for j in range(write,len(nums)):

            nums[j] = 0

# Status: Independent
# Time Taken: 5m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Two pointers
# Variant: Write Pointer.
# Mistakes / Confusion:Na

# 2. LC 80 -- Remove Duplicates from Sorted Array II 

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        write = 0

        for i in range(len(nums)):

            if write < 2:
                write += 1
            else:
                if nums[i] != nums[write-2]:
                    nums[write] = nums[i]
                    write += 1
        
        return write

# Status: Independent
# Time Taken: 10m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Two pointers
# Variant: write pointer
# Mistakes / Confusion:Na

### Tier 3

# 1.LC 155 -- Min Stack

class MinStack(object):

    def __init__(self):
        
        self.stack = []
        self.minstack = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)

        if not self.minstack:
            self.minstack.append(value)
        else:
            self.minstack.append(min(self.minstack[-1],value))
        
    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minstack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Status: Independent
# Time Taken: 15m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Stack
# Variant: basic stack ops
# Mistakes / Confusion:Na

# 2.LC 1047 --Remove All Adjacent Duplicates

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []

        for i in s:

            if stack and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        
        
        return "".join(stack)


# Status: Independent
# Time Taken: 5m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Stack
# Variant: remove adjacent duplicates
# Mistakes / Confusion:Na

# 3.LC 150 -- Evaluate Reverse Polish Notation

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []


        for i in tokens:

            if i in ["+","-","/","*"]:

                second = stack.pop()
                first = stack.pop()
                result = None

                if i == "+":
                    result = first + second
                elif i == "*":
                    result = first * second
                elif i == "-":
                    result = first - second
                elif i == "/":
                    result = int(float(first) / second)
                
                stack.append(result)

            else:
                stack.append(int(i))

        return stack[-1]

# Status: Independent
# Time Taken: 10m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Stack
# Variant: Evaluate reverse polish notation
# Mistakes / Confusion:Na

# 4.LC 739 -- Daily Temperatures

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = temperatures
        stack = []
        answer = [0]*len(n)

        for i in range(len(n)):

            while stack and n[i] > n[stack[-1]]:

                answer[stack[-1]] = i - stack[-1]

                stack.pop()
            
            stack.append(i)
        
        return answer

# Status: Independent
# Time Taken: 5m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Stack
# Variant: monotonic stack 
# Mistakes / Confusion:Na

# 5.LC 496 -- Next Greater Element I

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        next_greater = {}

        stack = []

        for i in nums2:

            while stack and i > stack[-1]:

                next_greater[stack[-1]] = i

                stack.pop()

            stack.append(i)

        ans = [-1]*len(nums1)

        for j in range(len(nums1)):

            if nums1[j] in next_greater:
                ans[j] = next_greater[nums1[j]]
        
        return ans


# Status: Independent
# Time Taken: 10m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Stack
# Variant: monotonic stack 
# Mistakes / Confusion:Na

# 6.LC 503 -- Next Greater Element II

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        stack = []

        n = len(nums)

        answer = [-1] * n

     

        for i in range(n*2):

            cur_idx = i % n
            
            while stack and nums[cur_idx] > nums[stack[-1]]:

                answer[stack[-1]] = nums[cur_idx]
                
                stack.pop()
            
            if i < n:
                stack.append(cur_idx)
        
        return answer 


# Status: Independent
# Time Taken: 10m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Stack
# Variant: monotonic stack 
# Mistakes / Confusion:Na


### New

# 1. LC 249 — Group Shifted Strings


class Solution:
    
    def get_shift_pattern(self,string):
        
        key = []
        
        for i in range(1,len(string)):
            
            key.append((ord(string[i]) - ord(string[i-1])) % 26)
        
        return tuple(key)
        
        
    def groupShiftedString(self, arr):
        #code here
        
        
        grouped_string = {}
        
        
        for string in arr:
            
            key = self.get_shift_pattern(string)
            
            if key in grouped_string:
                
                grouped_string[key] += [string]
            else:
                grouped_string[key] = [string]
        
        
        return grouped_string.values()


# Status: Independet
# Time Taken: 30m
# Time Complexity: O(n * l) n = no of string l = len of string
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Grouping Hash Map
# Variant: Canonical Key / Shift Pattern 
# Mistakes / Confusion:Na

# 2. LC 890 — Find and Replace Pattern

class Solution(object):

    def isMatch(self,word,pattern):

        if len(word) != len(pattern):
            return False
        
        freq_word ={}

        freq_pattern = {}

        for i in range(len(word)):

            if word[i] in freq_word and freq_word[word[i]] != pattern[i]:
                return False
            else:
                freq_word[word[i]] = pattern[i]
            
            if pattern[i] in freq_pattern and freq_pattern[pattern[i]] != word[i]:
                return False
            else:
                freq_pattern[pattern[i]] = word[i]
            
        return True


    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """

        answer = []


        for word in words:

            if self.isMatch(word,pattern):
                answer.append(word)
        
        return answer


# Status: Independet
# Time Taken: 20m
# Time Complexity: O(n * l) n = no of string l = len of string
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Grouping Hash Map
# Variant: Canonical Key / Shift Pattern 
# Mistakes / Confusion:Na

# 3. LC 1002 — Find Common Characters

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        common = {}

        for char in words[0]:
            common[char] = common.get(char,0)+1
        

        for word in words[1:]:

            freq = {}

            for char in word:
                freq[char] = freq.get(char,0)+1
            
            for char in common:

                if char in freq:
                    common[char] = min(common[char],freq[char])
                else:
                    common[char] = 0

        
        answer = []

        for key,value in common.items():

            for i in range(value):
                answer.append(key)
        
        return answer


# Status: Independet
# Time Taken: 10m
# Time Complexity: O(n * l) n = no of string l = len of string
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Freq Hashing
# Variant: Frequency Intersection / Minimum Frequency
# Mistakes / Confusion:Na


### Tier 1

# 3. LC 862 — Shortest Subarray with Sum at Least K

from collections import deque
class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = [0]

        for i in range(len(nums)):

            prefix.append(prefix[i]+nums[i])

        dq = deque()

        answer = float('inf')

        for j in range(len(prefix)):

            while dq and prefix[j]-prefix[dq[0]] >=k:

                answer = min(answer,j-dq[0])

                dq.popleft()
            
            while dq and prefix[j] <= prefix[dq[-1]]:

                dq.pop()
            
            dq.append(j)
        
        return answer if answer != float('inf') else -1


# Status: hint
# Time Taken: 20m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: sliding window
# Variant: montonotinc deque.
# Mistakes / Confusion:Na


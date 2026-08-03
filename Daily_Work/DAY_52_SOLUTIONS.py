### Tier 4

# 1. **LC 217 — Contains Duplicate**

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()

        for i in nums:

            if i in seen:
                return True
            seen.add(i)
        return False

# Status: independent
# Time Taken: 5m
# Time Complexity:O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Hash set
# Variant:contains Duplicate
# Mistakes / Confusion:Na

# 2. **LC 242 — Valid Anagram**

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        seen_s = {}

        for i in s:
            seen_s[i] = seen_s.get(i,0)+1

        seen_j = {}

        for j in t:
            seen_j[j] = seen_j.get(j,0)+1
        
        if seen_s != seen_j:
            return False
        
        return True

# Status: independent
# Time Taken: 5m
# Time Complexity:O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Frequncy Hashing
# Variant:valid anagram
# Mistakes / Confusion:Na


### Tier 1

# 1. **LC 150 — Evaluate Reverse Polish Notation**

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for i in tokens:

            if i in ["+", "-", "*", "/"]:

                second = stack.pop()
                first = stack.pop()

                result = None 

                if i == "+":
                    result = first + second
                elif i == "-":
                    result = first - second
                elif i == "*":
                    result = first * second
                elif i == "/":
                    result = int(float(first)/second)
                
                stack.append(result)
            else:
                stack.append(int(i))
        return stack[0]

# Status: independent
# Time Taken: 10m
# Time Complexity:O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Stack
# Variant:basic stack(evaluate rpn)
# Mistakes / Confusion:Na






### Tier 3
# 1. **LC 383 — Ransom Note**

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote_dict = {}

        for i in ransomNote:
            ransomNote_dict[i] = ransomNote_dict.get(i,0)+1
        
        magazine_dict = {}

        for j in magazine:
            magazine_dict[j] = magazine_dict.get(j,0)+1
        
        for k in ransomNote:

            if k not in magazine_dict:
                return False
            
            if ransomNote_dict[k] > magazine_dict[k]:
                return False
            
        return True

# Status: independent
# Time Taken: 10m
# Time Complexity:O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Frequency Hashing
# Variant:Query
# Mistakes / Confusion:Na

# 2. **LC 20 — Valid Parentheses**

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dictionary = {")":"(","]":"[","}":"{"}

        stack =[]

        for i in s:

            if i in dictionary:
                if not stack or dictionary[i] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        return True if not stack else False


# Status: independent
# Time Taken: 15m
# Time Complexity:O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:stack
# Variant:valid parenthesis
# Mistakes / Confusion:Na

# 3. **LC 155 — Min Stack**

class MinStack(object):

    def __init__(self):
        
        self.stack = []
        self.minstack=[]

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)

        if self.minstack:

            self.minstack.append(min(self.minstack[-1],value))
        else:
            self.minstack.append(value)


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


# Status: independent
# Time Taken: 10m
# Time Complexity:O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:stack
# Variant:basic ops
# Mistakes / Confusion:Na

# 4. **LC 162 — Find Peak Element**

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        while left < right:

            mid = (right+left)//2

            if nums[mid]>nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left

# Status: independent
# Time Taken: 15m
# Time Complexity:O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:binary search
# Variant:boundry search
# Mistakes / Confusion:Na

# 5. **LC 367 — Valid Perfect Square**

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 0
        right = num

        while left <= right:

            mid = (right+left)//2

            if mid*mid == num:
                return True
            elif mid*mid > num:
                right = mid - 1
            else:
                left = mid + 1
        return False

# Status: independent
# Time Taken: 10m
# Time Complexity:O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:binary search
# Variant:Target search
# Mistakes / Confusion:Na

# 6. **LC 153 — Find Minimum in Rotated Sorted Array**

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        while left < right:

            mid = (right+left)//2

            if nums[mid]>nums[right]:
                left = mid + 1
            else:
                right = mid 
        
        return nums[left]

# Status: independent
# Time Taken: 10m
# Time Complexity:O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:binary search
# Variant:boundry search
# Mistakes / Confusion:Na



















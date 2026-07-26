## Tier 4 Recalls (5 min each)

# 1. Running State / Kadane — min-max product tracking

def runningstate(nums):

    min_price = nums[0]

    max_profit = 0

    for i in range(len(nums)):

        if nums[i] < min_price:
            min_price = nums[i]
        else:
            profit = nums[i] - min_price

            max_profit = max(max_profit,profit)
    return max_profit

# 2. Two Pointers — Opposite Ends

def twopointers(nums,target):

    left = 0
    right = len(nums)-1

    while left < right:

        num=nums[left] + nums[right]

        if num == target:
            return [left+1,right+1]

        elif num > target:
            right -= 1
        else:
            left += 1


## Tier 1 — Priority Revision
   
"""
### 1. Valid Parentheses (LC 20)

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1:**
```
Input: s = "()"
Output: true
```

**Example 2:**
```
Input: s = "()[]{}"
Output: true
```

**Example 3:**
```
Input: s = "(]"
Output: false
```

**Constraints:**
- `1 <= s.length <= 10^4`
- `s[i]` is a parenthesis `'('`, `')'`, `'{'`, `'}'`, `'['` or `']'`.

"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        pairs = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for i in s:

            if i in ["(","[","{"]:
                stack.append(i)
            elif i in pairs:
                if not stack or pairs[i] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return not stack

# Status: independent
# Time taken: 20 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Stack
# Variant: Valid parenthesis
# mistakes/confusion: Na

"""
### 2. Min Stack (LC 155)

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

**Example 1:**
```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

**Constraints:**
- `-2^31 <= val <= 2^31 - 1`
- Methods `pop`, `top` and `getMin` operations will always be called on non-empty stacks.
- At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`.

# Status: ___
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___


"""

class MinStack(object):

    def __init__(self):

        # stack = []
        # minstack = []

        self.stack=[]
        self.minstack=[]

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

# Status: independent
# Time taken: 20 min
# Time complexity: O(1)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Stack
# Variant: minstack
# mistakes/confusion: Na

## Tier 3 — Revision (6 Problems)

"""
### 3. Find Minimum in Rotated Sorted Array (LC 153)

Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated `4` times.
- `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return the minimum element of this array.

You must write an algorithm that runs in `O(log n)` time.

**Example 1:**
Input: nums = [3,4,5,1,2]
Output: 1

**Example 2:**
Input: nums = [4,5,6,7,0,1,2]
Output: 0

**Example 3:**
Input: nums = [11,13,15,17]
Output: 11

**Constraints:**
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are **unique**.
- `nums` is sorted and rotated between `1` and `n` times.
"""

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

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left] 

# Status: independent
# Time taken: 10 min
# Time complexity: O(logn)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Binary search
# Variant: Boundry search
# mistakes/confusion: Na

"""
### 4. Find Peak Element (LC 162)

A peak element is an element that is strictly greater than its neighbors.

Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in `O(log n)` time.

**Example 1:**
Input: nums = [1,2,3,1]
Output: 2

**Example 2:**
Input: nums = [1,2,1,3,5,6,4]
Output: 5

**Constraints:**
- `1 <= nums.length <= 1000`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `nums[i] != nums[i + 1]` for all valid `i`.

"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right =len(nums)-1

        while left < right:

            mid = (right+left)//2

            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        return right

# Status: independent
# Time taken: 15 min
# Time complexity: O(logn)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Binary search
# Variant: Boundry search
# mistakes/confusion: Na

"""
### 5. Range Sum Query - Immutable (LC 303)

Given an integer array `nums`, handle multiple queries of the following type:

1. Calculate the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** where `left <= right`.

Implement the `NumArray` class:

- `NumArray(int[] nums)` Initializes the object with the integer array `nums`.
- `int sumRange(int left, int right)` Returns the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** (i.e. `nums[left] + nums[left + 1] + ... + nums[right]`).

**Example 1:**
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

**Constraints:**
- `1 <= nums.length <= 10^4`
- `-10^5 <= nums[i] <= 10^5`
- `0 <= left <= right < nums.length`
- At most `10^4` calls will be made to `sumRange`.

# Status: ___
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

"""

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
# Time taken: 20 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: prefix sum
# Variant: Range Sum Query
# mistakes/confusion: Na
    
"""
### 6. Two Sum (LC 1)

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have **exactly one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

**Example 1:**
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

**Example 2:**
Input: nums = [3,2,4], target = 6
Output: [1,2]

**Example 3:**
Input: nums = [3,3], target = 6
Output: [0,1]

**Constraints:**
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- **Only one valid answer exists.**

# Status: ___
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for i in range(len(nums)):

            needed = target - nums[i]

            if needed in seen:
                return [seen[needed],i]
            
            seen[nums[i]] = i

# Status: independent
# Time taken: 10 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: compliment lookup
# Variant: two sum 
# mistakes/confusion:Na

"""
### 7. Valid Perfect Square (LC 367)

Given a positive integer `num`, return `true` *if* `num` *is a perfect square or* `false` *otherwise*.

A **perfect square** is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as `sqrt`.

**Example 1:**
Input: num = 16
Output: true

**Example 2:**
Input: num = 14
Output: false

**Constraints:**
- `1 <= num <= 2^31 - 1`

"""

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

            number = mid * mid

            if number == num:
                return True
            elif number > num:
                right = mid - 1
            else:
                left = mid + 1
        return False 

# Status: independent
# Time taken: 10 min
# Time complexity: O(logn)
# Space complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Binary search
# Variant: Perfect square
# mistakes/confusion: Na

"""
### 8. Ransom Note (LC 383)

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

**Example 1:**
Input: ransomNote = "a", magazine = "b"
Output: false

**Example 2:**
Input: ransomNote = "aa", magazine = "ab"
Output: false

**Example 3:**
Input: ransomNote = "aa", magazine = "aab"
Output: true

**Constraints:**
- `1 <= ransomNote.length, magazine.length <= 10^5`
- `ransomNote` and `magazine` consist of lowercase English letters.

"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        seen = {}

        for i in ransomNote:
            seen[i] = seen.get(i,0)+1
        
        seen2 = {}



        for j in magazine:
            seen2[j] = seen2.get(j,0)+1
        

        for k in ransomNote:

            if k not in seen2:
                return False
            elif seen2[k] < seen[k]:
   
                return False
        return True 


# Status: indpendent
# Time taken: 15 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Frequnecy Hashing + query
# Variant: 
# mistakes/confusion: Na

## New Problems — Monotonic Stack (1 Problem)

### Learning Block — Monotonic Stack Pattern

"""
### 9. Daily Temperatures (LC 739)

Given an array of integers `temperatures` represents the daily temperatures, return *an array* `answer` *such that* `answer[i]` *is the number of days you have to wait after the* `ith` *day to get a warmer temperature*. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

**Example 1:**
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

**Example 2:**
```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

**Example 3:**
```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

**Constraints:**
- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

# Status: ___
# Time taken: ___ min
# Time complexity: O(?)
# Space complexity: O(?)
# Submitted to LC: Yes / No
# Result: Accepted / Wrong Answer / TLE / Runtime Error / Not Submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

"""


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

                answer[stack[-1]] = i - stack[-1]

                stack.pop()
            
            stack.append(i)
            
        return answer

# Status: hint
# Time taken: 45 min
# Time complexity: O(n)
# Space complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Monolathic stack
# Variant: Temprature 
# mistakes/confusion: Na





# DAY 80
# Status:
# Time Taken:
# Time Complexity:
# Space Complexity:
# Submitted to LC:
# Result:
# Pattern:
# Variant:
# Mistakes / Confusion:


# Tier - 4



# 1	-	LC	-	890	-	Find and Replace Pattern


class Solution:

    def isfeasible(self,str1,str2):

        if len(str1) != len(str2):

            return False


        freq_str1 = {}

        freq_str2 = {}


        for i in range(len(str1)):

            if str1[i] in freq_str1 and freq_str1[str1[i]] != str2[i]:

                return False

            else:

                freq_str1[str1[i]] = str2[i]
            
            if str2[i] in freq_str2 and freq_str2[str2[i]] != str1[i]:

                return False
            
            else:

                freq_str2[str2[i]] = str1[i]
        
        return True



    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:


        result = []


        for word in words:

            permutation = self.isfeasible(word,pattern)

            if permutation:

                result.append(word)
        
        
        return result 


# Status: Independent
# Time Taken: 10M
# Time Complexity: O(n*k)
# Space Complexity: O(n)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Frequcy Hashing
# Variant:permutation
# Mistakes / Confusion:Na


# 2	-	LC	-	523	-	Continuous Subarray Sum


class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        
        prefix = 0

        seen = {0:-1}

        for idx,num in enumerate(nums):

            prefix += num

            current = prefix % k

            if current in seen and idx - seen[current] > 1:

                return True

            if current not in seen:

                seen[current] = idx
        
        return False

# Status: Independent
# Time Taken: 8M
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Prefix sum
# Variant:Modulo
# Mistakes / Confusion:Na


# 3	-	LC	-	283	-	Move Zeroes

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        write = 0


        for idx,num in enumerate(nums):

            if num != 0:

                nums[write] = num

                write += 1
        
        for i in range(write,len(nums)):

            nums[i] = 0

# Status: Independent
# Time Taken: 5M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Two pointers
# Variant: Write pointer
# Mistakes / Confusion:Na

# 4	-	LC	-	930	-	Binary Subarrays With Sum

class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        

        prefix = 0

        seen = {0:1}

        count = 0

        for i in range(len(nums)):

            prefix += nums[i]

            needed = prefix - goal

            if needed in seen:

                count += seen[needed]
            
            seen[prefix] = seen.get(prefix,0)+1
        
        return count 

# Status: Independent
# Time Taken: 8M
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: prefix sum
# Variant: Hash map
# Mistakes / Confusion:Na

# 5	-	LC	-	974	-	Subarray Sums Divisible by K

class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:


        prefix = 0

        count = 0

        seen = {0:1}

        for i in range(len(nums)):


            prefix += nums[i]

            current = prefix % k

            if current in seen:

                count += seen[current]
            

            seen[current] = seen.get(current,0)+1

        return count

# Status: Independent
# Time Taken: 6M
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: prefix sum
# Variant: Modulo
# Mistakes / Confusion:Na


# 6	-	LC	-	21	-	Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        
        dummynode = ListNode(0)

        current = dummynode

        while list1 and list2:


            if list1.val <= list2.val:

                current.next = list1

                list1 = list1.next
            
            else:

                current.next = list2

                list2 = list2.next
            
            current = current.next
        
        current.next = list1 if list1 else list2

        return dummynode.next

# Status: Independent
# Time Taken: 2M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Linked List
# Variant: Dummay Node
# Mistakes / Confusion:Na


# 7	-	LC	-	19	-	Remove Nth Node From End


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        
        dummynode = ListNode(0)

        dummynode.next = head

        fast = dummynode

        pos = 1

        while pos <= n:

            fast = fast .next

            pos += 1
        
        slow = dummynode

        while fast.next:

            fast = fast.next

            slow = slow.next
        
        slow.next = slow.next.next

        return dummynode.next


# Status: Independent
# Time Taken: 8M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Linked List
# Variant: Slow + Fast and remove nth Node
# Mistakes / Confusion:Na

# 8	-	LC	-	2130	-	Maximum Twin Sum of a Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:

        slow = head

        fast = head

        prev = None

        while fast:

            prev = slow

            slow = slow.next

            fast = fast.next.next
        
        prev.next = None

        current = slow

        prev = None

        while current:

            next_node = current.next

            current.next = prev

            prev = current

            current = next_node
        

        left = head

        right = prev
        
        max_twin_sum = 0

        while right:

            twin_sum = left.val + right.val

            max_twin_sum = max(max_twin_sum,twin_sum)

            left = left.next

            right = right.next
        
        return max_twin_sum


# Status: Independent
# Time Taken: 15M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Linked List
# Variant: Slow and Fast + reversal
# Mistakes / Confusion:Na


# 9	-	LC	-	141	-	Linked List Cycle


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:


        slow = head

        fast = head

        while fast and fast.next:

            slow = slow.next

            fast = fast.next.next

            if slow == fast:

                return True
        
        return False


# Status: Independent
# Time Taken: 8M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Linked List
# Variant: Slow and Fast
# Mistakes / Confusion:Na

# 10	-	LC	-	876	-	Middle of the Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:

        slow = head

        fast = head

        while fast and fast.next:

            slow = slow.next

            fast = fast.next.next
        
        return slow

# Status: Independent
# Time Taken: 6M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Linked List
# Variant: Slow and Fast
# Mistakes / Confusion:Na


# 11	-	LC	-	142	-	Linked List Cycle II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        slow = head

        fast = head

        while fast and fast.next:

            slow = slow.next

            fast = fast.next.next

            if slow == fast:

                break
        
        else:

            return  None


        slow = head

        while slow != fast:

            slow = slow.next

            fast = fast.next
        
        return slow

# Status: Independent
# Time Taken: 5M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Linked List
# Variant: Slow and Fast
# Mistakes / Confusion:Na

# 12	-	LC	-	234	-	Palindrome Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:

        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        current = slow

        prev = None

        while current:

            next_node = current.next

            current.next = prev

            prev = current

            current = next_node
        
        left = head

        right = prev

        while right:


            if left.val != right.val:

                return False
            
            left = left.next

            right = right.next

        return True

# Status: Independent
# Time Taken: 10M
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Linked List
# Variant: Slow and Fast
# Mistakes / Confusion:Na

# 13	-	LC	-	20	-	Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:

        parentheses = {
            "}":"{",
            "]":"[",
            ")":"("
        }

        stack = []

        for i in range(len(s)):

            if s[i] in parentheses:

                if not stack or parentheses[s[i]] != stack[-1]:

                    return False
                else:

                    stack.pop()
            else:

                stack.append(s[i])
        
        return True if not stack else False


# Status: Independent
# Time Taken: 8M
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: stack
# Variant: Basic ops
# Mistakes / Confusion:Na

# 14	-	LC	-	155	-	Min Stack

class MinStack:

    def __init__(self):

        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:

        self.stack.append(value)

        if not self.min_stack:

            self.min_stack.append(value)
        else:

            if value <= self.min_stack[-1]:

                self.min_stack.append(value)

    def pop(self) -> None:

        value = self.stack.pop()

        if value == self.min_stack[-1]:

            self.min_stack.pop()        

    def top(self) -> int:

        return self.stack[-1]
        
    def getMin(self) -> int:

        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Status: Independent
# Time Taken: 10M
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: stack
# Variant: Basic ops
# Mistakes / Confusion:Na

# 15	-	LC	-	1047	-	Remove All Adjacent Duplicates


class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []


        for i in range(len(s)):


            if stack and s[i] == stack[-1]:

                stack.pop()
            
            else:

                stack.append(s[i])
        
        
        return "".join(stack)
     
# Status: Independent
# Time Taken: 10M
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: stack
# Variant: Basic ops
# Mistakes / Confusion:Na

# 16	-	LC	-	150	-	Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:


        stack = []


        for i in range(len(tokens)):

            if tokens[i] in "+*/-":

                second = stack.pop()

                first = stack.pop()

                result = None

                if tokens[i] == "+":

                    result = first + second

                elif tokens[i] == "-":
                    
                    result = first - second

                elif tokens[i] == "*":

                    result = first * second

                elif tokens[i] == "/":

                    result = int(first/float(second))
                
                stack.append(result)

            else:

                stack.append(int(tokens[i]))
        
        return stack[-1]

# Status:Independent
# Time Taken: 10m
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Stack
# Variant: RPM
# Mistakes / Confusion:nA

# 17	-	LC	-	739	-	Daily Temperatures

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:


        result = [0]*len(temperatures)

        stack = []

        for i in range(len(temperatures)):


            while stack and temperatures[i] > temperatures[stack[-1]]:

                result[stack[-1]] = i - stack[-1]

                stack.pop()

            stack.append(i)

        return result      

     
# Status: Independent
# Time Taken: 5M
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: stack
# Variant: Monotonic decreasing stack
# Mistakes / Confusion:Na

# 18	-	LC	-	496	-	Next Greater Element I

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        

        seen = {}

        stack = []


        for i in range(len(nums2)):

            while stack and nums2[i] > stack[-1]:

                seen[stack[-1]] = nums2[i]

                stack.pop()
            
            stack.append(nums2[i])
        
        result = [-1]*len(nums1)

        for i in range(len(nums1)):

            if nums1[i] in seen:

                result[i] = seen[nums1[i]]
        
        return result

# Status: Independent
# Time Taken: 10M
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: stack
# Variant: Monotonic decreasing stack
# Mistakes / Confusion:Na

# 19	-	LC	-	503	-	Next Greater Element II

class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        

        stack = []

        result = [-1]*len(nums)

        n = len(nums)

        for i in range(n*2):

            while stack and nums[i%n] > nums[stack[-1]]:

                result[stack[-1]] = nums[i%n]

                stack.pop()

            if i < n:

                stack.append(i)
        
        return result

# Status: Independent
# Time Taken: 8M
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: stack
# Variant: Monotonic decreasing stack
# Mistakes / Confusion:Na

# 20	-	LC	-	84	-	Largest Rectangle in Histogram

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        

        right = [len(heights)]*len(heights)

        stack = []

        for i in range(len(heights)):

            while stack and heights[i] < heights[stack[-1]]:

                right[stack[-1]] = i
            
                stack.pop()
            
            stack.append(i)

        left = [-1]*len(heights)

        stack = []

        for j in range(len(heights)-1,-1,-1):


            while stack and heights[j] < heights[stack[-1]]:

                left[stack[-1]] = j

                stack.pop()
            
            stack.append(j)
        

        max_histogram = 0

        for k in range(len(heights)):


            width = right[k] - left[k] - 1

            area = heights[k] * width

            max_histogram = max(max_histogram,area)
        
        return max_histogram

# Status: Independent
# Time Taken: 8M
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: stack
# Variant: Monotonic decreasing stack
# Mistakes / Confusion:Na


# New 


# 1 -- LC -- 34 -- Find First and Last Position of Element in Sorted Array


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        def first(nums,target):


            left = 0

            right = len(nums)-1

            answer = -1

            while left <= right:

                mid = (right+left)//2

                if nums[mid] < target:

                    left = mid + 1

                elif nums[mid] > target:

                    right = mid - 1
                
                else:

                    answer = mid

                    right = mid - 1
            
            return answer
        
        def second(nums,target):

            left = 0

            right = len(nums)-1

            answer = -1

            while left <= right:

                mid = (right+left)//2

                if nums[mid] > target:

                    right = mid - 1
                
                elif nums[mid] < target:

                    left = mid + 1
                
                else:

                    answer = mid 

                    left = mid + 1
            
            return answer
        
        return [first(nums,target),second(nums,target)]


# Status: Independent
# Time Taken: 10M
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Binary search
# Variant: Applied Boundry search
# Mistakes / Confusion:Na


# 3 -- LC -- 1011 -- Capacity To Ship Packages Within D Days


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:

        def isfeasible(capacity):

            count_days = 1

            weight = 0

            for i in range(len(weights)):

                if weight + weights[i] <= capacity:

                    weight += weights[i]
                
                else:

                    count_days += 1

                    weight = weights[i]
            
            return count_days <= days

        
        
        left = max(weights)

        right = sum(weights)

        while left < right:

            mid = (right+left)//2

            if isfeasible(mid):

                right = mid

            else:

                left = mid + 1
        
        return left 
            
# Status: Independent
# Time Taken: 10M
# Time Complexity: O(nlog(sum(weights)))
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Binary search
# Variant: Applied Boundry search
# Mistakes / Confusion:Na



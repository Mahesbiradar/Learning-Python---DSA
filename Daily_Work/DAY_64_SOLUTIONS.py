
# DAY 64

# Status:
# Time Taken:
# Time Complexity:
# Space Complexity:
# Submitted to LC:
# Result:
# Pattern:
# Variant:
# Mistakes / Confusion:

# Revison of the system


# 61	-	974	-	Subarray Sums Divisible by K

class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = {0:1}

        count = 0

        prefix = 0

        for i in range(len(nums)):

            prefix += nums[i]

            remainder = prefix % k

            if remainder in seen:

                count += seen[remainder]
            
            seen[remainder] = seen.get(remainder,0)+1
        
        return count

# Status: Independent
# Time Taken: 4m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Prefix sum
# Variant: Modulo
# Mistakes / Confusion:Na

# 62	-	2575	-	Find the Divisibility Array	

class Solution(object):
    def divisibilityArray(self, word, m):
        """
        :type word: str
        :type m: int
        :rtype: List[int]
        """

        remainder = 0

        result = []

        for i in range(len(word)):

            remainder = (remainder*10+int(word[i])) % m

            if remainder == 0:

                result.append(1)
            
            else:

                result.append(0)
        
        return result


# Status: Independent
# Time Taken: 10m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Prefix sum
# Variant: Modulo
# Mistakes / Confusion:Na

# 63	-	128	-	Longest Consecutive Sequence	

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        seen = set()

        for i in nums:

            seen.add(i)
        
        max_len = 0

        for num in seen:

            if num-1 not in seen:

                ele = num

                length = 1

                while ele + 1 in seen:

                    ele += 1

                    length += 1
                
                max_len = max(max_len,length)
        return max_len



# Status: Independent
# Time Taken: 7m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Sequnce explantion 
# Variant: Using set
# Mistakes / Confusion:Na


# 64	-	206	-	Reverse Linked List	

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

# Status: Independent
# Time Taken: 5m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Linked list
# Variant: reverse list
# Mistakes / Confusion:Na


# 65	-	92	-	Reverse Linked List II		

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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

        pos = 1

        current = dummy

        prev = None

        while pos <= left:

            prev = current

            current = current.next

            pos += 1

        left_node = current

        before_left = prev

        num = right - left + 1

        prev = None

        # current = left_node

        while num > 0:

            next_node = current.next

            current.next = prev

            prev = current

            current = next_node

            num -= 1
        
        before_left.next = prev

        left_node.next = current

        return dummy.next


# Status: Independent
# Time Taken: 10m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Linked list
# Variant: reverse list b/w two points
# Mistakes / Confusion:Na


# 66	-	21	-	Merge Two Sorted Lists		

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

# Status: Independent
# Time Taken: 6m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Linked list
# Variant: connecting two sorted linked lists
# Mistakes / Confusion:Na


# 67	-	19	-	Remove Nth Node From End		


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

        num = n

        while num > 0:

            fast = fast.next

            num -= 1
        
        slow = dummy

        while fast and fast.next:

            slow = slow.next

            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next


# Status: Independent
# Time Taken: 5m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Linked list
# Variant: slow and fast pointers
# Mistakes / Confusion:Na


# 68	-	2130	-	Maximum Twin Sum of a Linked List		


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
    
        slow = head

        fast = head

        # prev = None

        while fast and fast.next :

            prev = slow

            slow = slow.next

            fast = fast.next.next

        # prev.next = None
        
        prev = None

        current = slow

        print(current)

        while current:

            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        left = head

        right = prev

        max_sum = 0

        while right:

            sum_of_nodes= left.val + right.val

            max_sum = max(max_sum,sum_of_nodes)

            left = left.next

            right = right.next
        
        return max_sum


# Status: Independent
# Time Taken: 8m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Linked list
# Variant: slow and fast pointers + reversal
# Mistakes / Confusion:Na


# 69	-	141	-	Linked List Cycle	


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        slow = head

        fast = head

        while fast and fast.next:

            slow = slow.next

            fast = fast.next.next

            if slow == fast:

                return True
        
        return False


# Status: Independent
# Time Taken: 3m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Linked list
# Variant: slow and fast pointers
# Mistakes / Confusion:Na

# 70	-	876	-	Middle of the Linked List	

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        slow = head

        fast = head 

        while fast and fast.next:

            slow = slow.next

            fast = fast.next.next

        
        return slow


# Status: Independent
# Time Taken: 3m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Linked list
# Variant: slow and fast pointers
# Mistakes / Confusion:Na


# 71	-	142	-	Linked List Cycle II		


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        slow = head

        fast = head

        while fast and fast.next:

            slow = slow.next

            fast = fast.next.next

            if slow == fast:

                break
        
        else:

            return None

        left = head

        right = fast 


        while left != right:

            left = left.next

            right = right.next

        
        return left


# Status: Independent
# Time Taken: 6m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Linked list
# Variant: slow and fast pointers
# Mistakes / Confusion:Na

# 72	-	234	-	Palindrome Linked List		


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
        slow = head

        fast = head

        while fast and fast.next:

            slow = slow.next

            fast = fast.next.next

        
        prev = None

        current = slow

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
# Time Taken: 4m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Linked list
# Variant: slow and fast pointers + reversal
# Mistakes / Confusion:Na

# 73	-	143	-	Reorder List		

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return head

        slow = head

        fast = head


        while fast.next and fast.next.next:

            slow = slow.next

            fast = fast.next.next

        second_half_start = slow.next

        slow.next = None

        prev = None

        current = second_half_start

        while current:

            next_node = current.next

            current.next = prev

            prev = current

            current = next_node
        
        node1 = head

        node2 = prev


        while node2:

            node1_next = node1.next

            node2_next = node2.next

            node1.next = node2

            node2.next = node1_next

            node1 = node1_next

            node2 = node2_next

        
        return head

# Status: Hint
# Time Taken: 15m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Linked list
# Variant: slow and fast pointers + reversal + rewiring
# Mistakes / Confusion:Na

# 74	-	23	-	Merge k Sorted Lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergertwo (self,list1,list2):

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


    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        if not lists:
            return None
        

        while len(lists) > 1:

            mereged_lists =[]

            for i in range(0,len(lists),2):

                first = lists[i]

                if i+1 < len(lists):

                    second = lists[i+1]
                
                else:
                    
                    second = None
                
                merge = self.mergertwo(first,second)

                mereged_lists.append(merge)
            
            lists = mereged_lists
        
        return lists[0]


# Status: independent
# Time Taken: 10m
# Time Complexity: O(n*l) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Linked list
# Variant: merege k sorted lists
# Mistakes / Confusion:Na


# 75	-	20	-	Valid Parentheses		

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        seen = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        for i in range(len(s)):

            if s[i] in ["(","{","["]:
                stack.append(s[i])

            elif s[i] in seen:
                if not stack or seen[s[i]] != stack[-1]:
                    return False
                else:
                    stack.pop()
        
        return True if not stack else False


# Status: independent
# Time Taken: 6m
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: stack
# Variant: stack basic ops
# Mistakes / Confusion:Na

# 76	-	155	-	Min Stack

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

            if value <= self.minstack[-1]:

                self.minstack.append(value)

    def pop(self):
        """
        :rtype: None
        """
        val =self.stack.pop()
        if val == self.minstack[-1]:
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
# Time Taken: 4m
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: stack
# Variant: stack basic ops
# Mistakes / Confusion:Na


# 77	-	1047	-	Remove All Adjacent Duplicates		

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []

        for i in range(len(s)):

            if stack:

                if stack[-1] == s[i]:

                    stack.pop()

                else:

                    stack.append(s[i])
            else:

                stack.append(s[i])
    

        result = "".join(stack)

        return result

# Status: independent
# Time Taken: 4m
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: stack
# Variant: remove adjacent
# Mistakes / Confusion:Na


# 78	-	150	-	Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        stack = []


        for i in range(len(tokens)):

            if tokens[i] in ["+","-","*","/"]:

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

                    result = int(first / float(second))
                
                stack.append(result)

            else:

                stack.append(int(tokens[i]))
        
        return stack[-1]


# Status: independent
# Time Taken: 6m
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: stack
# Variant: RPN
# Mistakes / Confusion:Na


# 79	-	739	-	Daily Temperatures		

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        stack = []

        result = [0]*len(temperatures)

        for i in range(len(temperatures)):

            while stack and temperatures[stack[-1]] < temperatures[i]:

                result[stack[-1]] = i - stack[-1]

                stack.pop()
            
            stack.append(i)
        
        return result


# Status: independent
# Time Taken: 5m
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: stack
# Variant: monotonic decrising stack
# Mistakes / Confusion:Na


# 80	-	496	-	Next Greater Element I		


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        stack = []

        seen = {}

        for i in range(len(nums2)):

            while stack and nums2[stack[-1]] < nums2[i]:

                seen[nums2[stack[-1]]] = nums2[i]

                stack.pop()
            
            stack.append(i)
        
        result = [-1]*len(nums1)


        for i in range(len(nums1)):

            if nums1[i] in seen:

                result[i] = seen[nums1[i]]
        
        return result


# Status: independent
# Time Taken: 6m
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: stack
# Variant: monotonic decrising stack
# Mistakes / Confusion:Na


# 81	-	503	-	Next Greater Element II		

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        stack = []

        result = [-1]*len(nums)

        n = len(nums)

        
        for i in range(n*2):

            while stack and nums[stack[-1]] < nums[i%n]:

                result[stack[-1]] = nums[i%n]

                stack.pop()
            
            if i < n:

                stack.append(i)
        
        return result


# Status: independent
# Time Taken: 5m
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: stack
# Variant: monotonic decrising stack
# Mistakes / Confusion:Na


# 82	-	84	-	Largest Rectangle in Histogram

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        right = [len(heights)]*len(heights)

        stack = []

        for i in range(len(heights)):

            while stack and heights[stack[-1]] > heights[i]:

                right[stack[-1]] = i

                stack.pop()
            
            stack.append(i)
        

        left = [-1]*len(heights)

        stack = []

        for j in range(len(heights)-1,-1,-1):

            while stack and heights[stack[-1]] > heights[j]:

                left[stack[-1]] = j

                stack.pop()
        
            stack.append(j)


        max_histogram = 0

        for i in range(len(heights)):

            width = right[i]-left[i]-1

            area = width * heights[i]

            max_histogram = max(max_histogram,area)
        
        return max_histogram


# Status: independent
# Time Taken: 8m
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: stack
# Variant: monotonic decrising stack
# Mistakes / Confusion:Na


# 83	-	85	-	Maximal Rectangle

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        right = [len(heights)]*len(heights)

        stack = []

        for i in range(len(heights)):

            while stack and heights[stack[-1]] > heights[i]:

                right[stack[-1]] = i

                stack.pop()
            
            stack.append(i)
        

        left = [-1]*len(heights)

        stack = []

        for j in range(len(heights)-1,-1,-1):

            while stack and heights[stack[-1]] > heights[j]:

                left[stack[-1]] = j

                stack.pop()
        
            stack.append(j)


        max_histogram = 0

        for i in range(len(heights)):

            width = right[i]-left[i]-1

            area = width * heights[i]

            max_histogram = max(max_histogram,area)
        
        return max_histogram

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix or not matrix[0]:
            return 0

        rectangel = [0]*len(matrix[0])

        max_rectangle = 0

        for row in matrix:

            for i in range(len(row)):

                if row[i] == "0":

                    rectangel[i] = 0
                
                else:

                    rectangel[i] += 1
            
            histogram = self.largestRectangleArea(rectangel)

            max_rectangle = max(max_rectangle,histogram)
        
        return max_rectangle


# Status: independent
# Time Taken: 10m
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: stack
# Variant: monotonic stack
# Mistakes / Confusion:Na


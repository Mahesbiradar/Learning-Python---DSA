## Schedule

## Revison session - 3 Date(23-08-2026)

# 1	-	LC	-	930	-	Binary Subarrays With Sum

class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        seen = {0:1}

        prefix = 0

        count = 0

        for i in range(len(nums)):

            prefix += nums[i]

            needed = prefix - goal

            if needed in seen:
                count += seen[needed]

            seen[prefix] = seen.get(prefix,0)+1
        
        return count 

# Status: independent 
# Time Taken: 10m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Prefix sum
# Variant: Hashmap
# Mistakes / Confusion:Na

# 2	-	LC	-	1679	-	Max Number of K-Sum Pairs

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sorted_nums = sorted(nums)

        left = 0 
        right = len(sorted_nums)-1
        count = 0

        while left < right:

            sum_of_two = sorted_nums[left]+sorted_nums[right]

            if sum_of_two == k:
                count += 1
                left += 1
                right -= 1
            elif sum_of_two > k:
                right -= 1
            else:
                left += 1
        return count 

# Status: independent
# Time Taken: 10m 
# Time Complexity: O(nlogn)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Two pointers
# Variant: Maximize sorted
# Mistakes / Confusion:Na

# 3	-	LC	-	1877	-	Minimize Maximum Pair Sum

class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)

        left = 0
        right = len(nums)-1

        max_pair = 0

        while left < right:

            sum_of_pairs = sorted_nums[left]+sorted_nums[right]

            max_pair = max(max_pair,sum_of_pairs)

            left += 1
            right -= 1

        return max_pair

# Status: independent
# Time Taken: 5m 
# Time Complexity: O(nlogn)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Two pointers
# Variant: Maximize sorted
# Mistakes / Confusion:Na

# 4	-	LC	-	974	-	Subarray Sums Divisible by K

class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = {0:1}

        prefix = 0

        count = 0

        for i in range(len(nums)):

            prefix += nums[i]

            remainder = prefix % k

            if remainder in seen:
                count += seen[remainder]
            
            seen[remainder] = seen.get(remainder,0)+1
            
        return count

# Status: independent
# Time Taken: 5m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Prefix sum
# Variant: modulo
# Mistakes / Confusion:Na

# 5	-	LC	-	2575	-	Find the Divisibility Array

class Solution(object):
    def divisibilityArray(self, word, m):
        """
        :type word: str
        :type m: int
        :rtype: List[int]
        """
        answer = []

        remainder = 0

        for i in range(len(word)):

            remainder = (remainder * 10 + int(word[i])) % m

            if remainder == 0:

                answer.append(1)
            else:
                answer.append(0)

        return answer

# Status: independent
# Time Taken: 5m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Prefix sum
# Variant: modulo
# Mistakes / Confusion:Na

# 6	-	LC	-	2261	-	K Divisible Elements Subarrays


class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        seen = set()

        for i in range(len(nums)):

            count = 0

            for j in range(i,len(nums)):

                if nums[j] % p == 0:
                    count += 1
                
                if count > k:
                    break
                
                seen.add(tuple(nums[i:j+1]))
        
        return len(seen)


# Status: Hint
# Time Taken: 5m 
# Time Complexity: O(n^3)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Brute Force
# Variant: Na
# Mistakes / Confusion:Na

# 8	-	LC	-	128	-	Longest Consecutive Sequence


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()

        for i in nums:
            seen.add(i)
        
        print(seen)

        longest = 0

        for num in seen:
            count = 0
            if num-1 not in seen:
                char = num
                count = 1

                while char + 1 in seen:

                    char += 1
                    count += 1
            longest = max(longest,count)
        
        return longest


# Status: independent
# Time Taken: 10m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:seqeunce expansion
# Variant: Na
# Mistakes / Confusion:Na

# 9	-	LC	-	1590	-	Make Sum Divisible by P


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
        
        min_len = len(nums)

        prefix = 0

        seen = {0:-1}

        for i in range(len(nums)):

            prefix += nums[i]

            current = prefix % p

            needed = (current-target) % p

            if needed in seen:
                min_len = min (min_len, i-seen[needed])

            seen[current] = i

        return -1 if min_len == len(nums) else min_len 

# Status: Hint
# Time Taken: 10m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:seqeunce expansion
# Variant: Na
# Mistakes / Confusion:Na

# 10	-	LC	-	206	-	Reverse Linked List

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
        
        # dummy = ListNode(0)

        prev = None

        current = head

        while current:

            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev

# Status: independent
# Time Taken: 5m 
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Linked list
# Variant: Reversal 
# Mistakes / Confusion:Na

# 11	-	LC	-	92	-	Reverse Linked List II

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

        prev = dummy

        dummy.next = head

        position = 1

        current = head

        while position < left:

            prev = current
            current = current.next
            position += 1
        
        # return current

        before_left = prev
        left_node = current
        prev = None

        num = right-left+ 1
        while num > 0:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            num -= 1
        
        # return prev

        before_left.next = prev
        left_node.next = current

        return dummy.next

# Status: independent
# Time Taken: 10m 
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Linked list
# Variant: Reversal 
# Mistakes / Confusion:Na

# 12	-	LC	-	21	-	Merge Two Sorted Lists

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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
# Time Taken: 10m 
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Dummy node
# Variant: Merge sorted lists
# Mistakes / Confusion:Na

# 13	-	LC	-	19	-	Remove Nth Node From End

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)

        right = dummy

        dummy.next = head

        pos = 0

        while pos < n:

            right = right.next
            pos += 1
        
        left = dummy

        while right.next:

            right = right.next
            left = left.next
        
        left.next = left.next.next

        return dummy.next
        

# Status: independent
# Time Taken: 10m 
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Dummy node
# Variant: Remove nth from end
# Mistakes / Confusion:Na

# 14	-	LC	-	2130	-	Maximum Twin Sum of a Linked List

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

        while fast and fast.next:

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
        max_sum = 0
        while right:

            max_sum = max(max_sum,left.val+right.val)

            left = left.next
            right = right.next
        
        return max_sum


# Status: independent
# Time Taken: 5m 
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: In-place manipulation
# Variant: Twin sum / reverse second half
# Mistakes / Confusion:Na

# 15	-	LC	-	141	-	Linked List Cycle

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

# Status: independent
# Time Taken: 5m 
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: linked list
# Variant: slow and fast pointer
# Mistakes / Confusion:Na

# 16	-	LC	-	876	-	Middle of the Linked List


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

# Status: independent
# Time Taken: 5m 
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: linked list
# Variant: slow and fast pointer
# Mistakes / Confusion:Na



# 17	-	LC	-	142	-	Linked List Cycle II

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
        right = slow

        while right != left:

            right = right.next
            left = left.next
        
        return left 

# Status: independent
# Time Taken: 5m 
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: linked list
# Variant: slow and fast pointer (floyeds algo)
# Mistakes / Confusion:Na

# 18	-	LC	-	234	-	Palindrome Linked List

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


# Status: independent
# Time Taken: 5m 
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: linked list
# Variant: slow and fast pointer + reversal
# Mistakes / Confusion:Na

# 19	-	LC	-	143	-	Reorder List

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

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
        
        current = slow.next
        slow.next = None 

        prev = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        first = head
        second = prev

        while second:

            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next
        
        return head

# Status: independent
# Time Taken: 15m 
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: linked list
# Variant: reversal + in-place rewringng 
# Mistakes / Confusion:Na


# 20	-	LC	-	328	-	Odd Even Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:

            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        
        odd.next = even_head

        return head

# Status: hint
# Time Taken: 15m 
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: linked list
# Variant:in-place rewringng + odd even nodes 
# Mistakes / Confusion:Na

# 21	-	LC	-	24	-	Swap Nodes in Pairs


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)

        dummy.next = head
        
        prev = dummy

        while prev.next and prev.next.next:

            first = prev.next
            second = first.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = first
        
        return dummy.next

# Status: hint
# Time Taken: 10m 
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: linked list
# Variant:in-place rewiring
# Mistakes / Confusion:Na

# 22	-	LC	-	23	-	Merge k Sorted Lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        def mergertwolists(list1,list2):

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
        

        while len(lists) != 1:

            merged_lists = []

            for i in range(0,len(lists),2):

                first = lists[i]

                if i+1 < len(lists):
                    second = lists[i+1]
                else:
                    second = None
                
                mergetwo = mergertwolists(first,second)

                merged_lists.append(mergetwo)
            
            lists = merged_lists
        
        return lists[0]


# Status: Independent
# Time Taken: 20m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: linked list
# Variant: Merge n lists
# Mistakes / Confusion:Na

# 23	-	LC	-	20	-	Valid Parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {
        "}":"{",
        "]":"[",
        ")":"("
        }

        stack = []

        for i in s:

            if i in pairs:

                if not stack:
                    return False
                elif pairs[i] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        
        return True if not stack else False

# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: stack
# Variant: Basic stack ops
# Mistakes / Confusion:Na

# 24	-	LC	-	155	-	Min Stack

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
        elif self.minstack[-1] >= value:
            self.minstack.append(value)
        
    def pop(self):
        """
        :rtype: None
        """
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        self.stack.pop()
        # self.minstack.pop()

        

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

# Status: Independent
# Time Taken: 4m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: stack
# Variant: Basic stack ops
# Mistakes / Confusion:Na

# 25	-	LC	-	1047	-	Remove All Adjacent Duplicates

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []


        for i in s:

            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        
        answer = "".join(stack)

        return answer


# Status: Independent
# Time Taken: 4m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: stack
# Variant: remove adjacent
# Mistakes / Confusion:Na


# 26	-	LC	-	150	-	Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens):
        
        stack = []

        for i in tokens:

            if i not in ["+", "-", "*", "/"]:
                stack.append(int(i))
            else:
                right = stack.pop()
                left =  stack.pop()
                result = None

                if i == "+":
                    result = left + right
                elif i == "-":
                    result = left - right
                elif i == "*":
                    result = left * right
                elif i == "/":
                    result = int(left/right)
                
                stack.append(result)
        
        return stack[0]


# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: stack
# Variant: reverse Polish Notation
# Mistakes / Confusion:Na

# 27	-	LC	-	739	-	Daily Temperatures

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        answer = [0]* len(temperatures)

        stack = []

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:

                answer[stack[-1]] = i - stack[-1]
                
                stack.pop()

            stack.append(i)
        
        return answer


# Status: Independent
# Time Taken: 5m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: stack
# Variant: monotonic stack
# Mistakes / Confusion:Na

# 28	-	LC	-	496	-	Next Greater Element I

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
        

        answer = [-1]*len(nums1)

        for i in range(len(nums1)):
            
            if nums1[i] in next_greater:

                answer[i] = next_greater[nums1[i]]

        return answer


# Status: Independent
# Time Taken: 5m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: stack
# Variant: monotonic stack
# Mistakes / Confusion:Na

# 29	-	LC	-	503	-	Next Greater Element II

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        answer = [-1]* len(nums)

        stack = []

        n = len(nums)

        for i in range(n*2):

            while stack and nums[i%n] > nums[stack[-1]]:

                answer[stack[-1]] = nums[i%n]

                stack.pop()

            if i < n:
                stack.append(i)
        
        return answer


# Status: Independent
# Time Taken: 5m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: stack
# Variant: monotonic stack
# Mistakes / Confusion:Na

# 30	-	LC	-	84	-	Largest Rectangle in Histogram

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        right = [len(heights)]*len(heights)

        stack = []

        for i in range(len(heights)):

            while stack and heights[i] < heights[stack[-1]]:

                right[stack[-1]] = i

                stack.pop()
    
            stack.append(i)

        left = [-1] * len(heights)

        stack = []

        for i in range(len(heights)-1,-1,-1):

            while stack and  heights[i] < heights[stack[-1]]:

                left[stack[-1]] = i

                stack.pop()

            stack.append(i)
        

        max_rectangle = 0

        for i in range(len(heights)):

            width = (right[i] - left[i]) - 1

            area =  heights[i] * width

            max_rectangle = max(max_rectangle,area)

        return max_rectangle
        

# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: stack
# Variant: monotonic stack + histogram
# Mistakes / Confusion:Na

# 31	-	LC	-	85	-	Maximal Rectangle

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        right = [len(heights)]*len(heights)

        stack = []

        for i in range(len(heights)):

            while stack and heights[i] < heights[stack[-1]]:

                right[stack[-1]] = i

                stack.pop()
    
            stack.append(i)

        left = [-1] * len(heights)

        stack = []

        for i in range(len(heights)-1,-1,-1):

            while stack and  heights[i] < heights[stack[-1]]:

                left[stack[-1]] = i

                stack.pop()

            stack.append(i)
        

        max_rectangle = 0

        for i in range(len(heights)):

            width = (right[i] - left[i]) - 1

            area =  heights[i] * width

            max_rectangle = max(max_rectangle,area)

        return max_rectangle


    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        rectangle = [0]*len(matrix[0])

        maximal_rectangel = 0

        for row in matrix:

            for i in range(len(row)):

                if row[i] == "1":
                    rectangle[i] += 1
                else:
                    rectangle[i] = 0
            
            area = self.largestRectangleArea(rectangle)

            maximal_rectangel = max(maximal_rectangel,area)
        
        return maximal_rectangel



# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n*l)
# Space Complexity:O(l)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: stack
# Variant: monotonic stack + histogram 
# Mistakes / Confusion:Na

# 32	-	LC	-	239	-	Sliding Window Maximum


from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq =deque()


        answer = []


        for i in range(len(nums)):

            left = i-k+1

            while dq and left > dq[0]:

                dq.popleft()
            
            while dq and nums[i] >= nums[dq[-1]]:

                dq.pop()
            
            dq.append(i)

            if i >= k-1:

                answer.append(nums[dq[0]])
        
        return answer


# Status: hint
# Time Taken: 20m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: sliding window
# Variant: monotonic deque
# Mistakes / Confusion:Na

# 33	-	LC	-	1438	-	Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

# Brute Force:

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        longest_subarray = 0
        for i in range(len(nums)):

            max_num = nums[i]
            min_num = nums[i]

            for j in range(i,len(nums)):

                max_num = max(max_num,nums[j])
                min_num = min(min_num,nums[j])

                diff = max_num - min_num

                if diff <= limit:

                    longest_subarray = max(longest_subarray,j-i+1)

        return longest_subarray

# status: Independent

# Optimal solution:

from collections import deque
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """

        maxdeque = deque()
        mindeque = deque()

        answer = 0

        left = 0

        for right in range(len(nums)):

            while maxdeque and nums[right] >= nums[maxdeque[-1]]:

                maxdeque.pop()
            
            maxdeque.append(right)

            while mindeque and nums[right] <= nums[mindeque[-1]]:

                mindeque.pop()

            mindeque.append(right)


            while nums[maxdeque[0]]-nums[mindeque[0]] > limit:


                if maxdeque[0] == left:

                    maxdeque.popleft()
                
                if mindeque[0] == left:

                    mindeque.popleft()
                
                left +=1
                
            answer = max(answer,right-left+1)


        return answer

# Status: hint
# Time Taken: 20m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: sliding window
# Variant: monotonic deque
# Mistakes / Confusion:Na

# 34	-	LC	-	862	-	Shortest Subarray with Sum at Least K

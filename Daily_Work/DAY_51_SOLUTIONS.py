### Tier 4

# 1. **LC 704 — Binary Search**

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        while left <= right:

            mid = (right+left)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1

        return -1 

# Status: independent
# Time Taken: 10m
# Time Complexity:O(logn)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Binary search
# Variant:applied Target search
# Mistakes / Confusion:Na

# 2. **LC 121 — Best Time to Buy and Sell Stock**

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_profit = 0

        for i in range(1,len(prices)):

            if prices[i] < min_price:
                min_price = min(min_price,prices[i])
            else:
                profit = prices[i] - min_price

                if profit > max_profit:
                    max_profit = max(max_profit,profit)
        return max_profit

# Status: independent
# Time Taken: 10m
# Time Complexity:O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Running state
# Variant:BEST TIME TO BUY AND SELL
# Mistakes / Confusion:Na


### New

# 1. **LC 150 — Evaluate Reverse Polish Notation** (Basic Stack)

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
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
                    result = int(float(left)/right)
                
                stack.append(result)
        
        return stack[0]

# Status: Hint
# Time Taken: 25m
# Time Complexity:O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:stack
# Variant:Evaluate RPN
# Mistakes / Confusion:Na

# 2. **LC 84 — Largest Rectangle in Histogram** (Monotonic Stack)

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        pse =[-1]*n
        nse = [n]*n

        stack =[]

        for i in range(len(heights)):

            while stack and heights[stack[-1]]>=heights[i]:
                
                stack.pop()
                
            if stack:
                pse[i] = stack[-1]
            stack.append(i)
        
        stack =[]

        for j in range(len(heights)-1,-1,-1):

            while stack and heights[stack[-1]]>=heights[j]:
                stack.pop()
            
            if stack:
                nse[j] = stack[-1]
            
            stack.append(j)
        
        max_area = 0

        for k in range(len(heights)):

            width = nse[k] - pse [k] -1
            area = width * heights[k]
            
            max_area = max(max_area,area)
        
        return max_area

# Status: Hint
# Time Taken: 25m
# Time Complexity:O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:stack
# Variant:monotonic stack
# Mistakes / Confusion:Na


### Tier 3

# 2. **LC 23 — Merge k Sorted Lists** (overdue Jul 29)


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists:
            return None
  
        def mergetwo(list1,list2):

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


        while len(lists) > 1:

                mergedlist = []

                for i in range(0,len(lists),2):

                    first = lists[i]

                    if i+1 < len(lists):
                        second = lists[i+1]
                    else:
                        second = None
                    
                    mergedtwolist = mergetwo(first,second)

                    mergedlist.append(mergedtwolist)
                
                lists = mergedlist
            
        return lists[0]

# Status: independent
# Time Taken: 25m
# Time Complexity:O(nlogk)
# Space Complexity:O(k)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Linked list
# Variant: Merege Linked lists
# Mistakes / Confusion:Na

# 3. **LC 278 — First Bad Version** (due Jul 30)

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n

        while left < right :

            mid = (right+left)//2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

# Status: independent
# Time Taken: 10m
# Time Complexity:O(logn)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Binary search
# Variant: applied boundry search
# Mistakes / Confusion:Na

# 4. **LC 58 — Length of Last Word** (due Jul 30)

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_word = 0

        count = 0

        for i in range(len(s)):

            if s[i] == " ":
                count = 0
            else:
                count += 1
            
            if count != 0:
                last_word = count

        return last_word

# Status: independent
# Time Taken: 10m
# Time Complexity:O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:string Traversal
# Variant: last world length
# Mistakes / Confusion:Na

# 5. **LC 33 — Search in Rotated Sorted Array** (due Jul 30)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        while left <= right:

            mid =(right+left)//2

            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:

                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:

                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                 
        return -1    

# Status: independent
# Time Taken: 15m
# Time Complexity:O(logn)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:binary search
# Variant: applied Target search
# Mistakes / Confusion:Na

# 6. **LC 930 — Binary Subarrays With Sum** (due Jul 30)

class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        seen ={0:1}

        prefix = 0

        count = 0

        for i in nums:

            prefix += i

            needed = prefix - goal

            if needed in seen:
                count += seen[needed]
            
            seen[prefix] = seen.get(prefix,0)+1
        return count

# Status: independent
# Time Taken: 10m
# Time Complexity:O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Prefix sum + Hash map
# Variant: Binary subarry sum
# Mistakes / Confusion:Na

# 1. **LC 2261 — K Divisible Elements Subarrays** (overdue Jul 28)


class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        seen=set()

        for i in range(len(nums)):

            current_divisible = 0

            for j in range(i,len(nums)):

                    if nums[j] % p == 0:
                        current_divisible += 1
                    
                    if current_divisible > k:
                        break
                    
                    seen.add(tuple(nums[i:j+1]))

        return len(seen)


# Status: independent
# Time Taken: 10m
# Time Complexity:O(n^3)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Nested loop
# Variant: 
# Mistakes / Confusion:Na
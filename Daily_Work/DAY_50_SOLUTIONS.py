


# Read → Restate → Identify Pattern → Plan in Words → Dry Run → Code → Test → Submit


# 1. **Two Sum II** (LC 167)


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = numbers
        left = 0
        right = len(n)-1

        while left < right:

            sum_of_element = n[left]+n[right]

            if sum_of_element == target:
                return [left+1,right+1]
            elif sum_of_element > target:
                right -= 1
            else:
                left += 1


# Status: independent
# Time Taken: 10 min
# Time Complexity: O(n) — one pass over the list
# Space Complexity: O(1) — constant extra space 
# Submitted to LC: yes
# Result: Accepted
# Pattern: Two pointers
# Variant: opposite ends
# Mistakes / Confusion: Na

# 2. **Find Smallest Letter Greater Than Target** (LC 744)

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = 0

        right = len(letters)-1

        greter_element = None

        while left <= right:

            mid = (right+left)//2

            if letters[mid] > target:
                greter_element = letters[mid]
                right = mid - 1
            else:
                left = mid + 1
        
        if greter_element == None:
            return letters[0]
        else:
            return greter_element

# Status: independent
# Time Taken: 15 min
# Time Complexity: O(logn) — one pass over the list
# Space Complexity: O(1) — constant extra space 
# Submitted to LC: yes
# Result: Accepted
# Pattern: Binary search
# Variant: boundry search
# Mistakes / Confusion: Na

# 3. **Arranging Coins** (LC 441)


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0

        right = n

        rows = None

        while left <= right:

            mid = (right+left)//2

            coins_needed = mid*(mid+1)//2

            if coins_needed == n:
                return mid
            elif coins_needed > n:
                right = mid - 1
            else:
                rows = mid
                left = mid + 1
        return rows

# Status: independent
# Time Taken: 20 min
# Time Complexity: O(logn) — one pass over the list
# Space Complexity: O(1) — constant extra space 
# Submitted to LC: yes
# Result: Accepted
# Pattern: Binary search
# Variant: boundry search
# Mistakes / Confusion: Na

# 4. **Guess Number Higher or Lower** (LC 374)

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num):
    pass

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n

        while left <= right:

            mid =(right+left)//2

            num = guess(mid)

            if num == 0:
                return mid
            elif num == -1:
                right = mid
            elif num == 1:
                left = mid + 1

# Status: independent
# Time Taken: 10 min
# Time Complexity: O(logn) — one pass over the list
# Space Complexity: O(1) — constant extra space 
# Submitted to LC: yes
# Result: Accepted
# Pattern: Binary search
# Variant: boundry search
# Mistakes / Confusion: Na

#5. **Top K Frequent Words** (LC 692)

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        frequnecy_words ={}

        for i in words:
            frequnecy_words[i] = frequnecy_words.get(i,0)+1
        
        sorted_freq = sorted(frequnecy_words.items(),key=lambda x:(-x[1],x[0]))

        answer = []

        for key,value in sorted_freq:

            answer.append(key)

            if len(answer) == k:
                return answer
            
# Status: independent
# Time Taken: 10 min
# Time Complexity: O(nlogn) — one pass over the list
# Space Complexity: O(n) — constant extra space 
# Submitted to LC: yes
# Result: Accepted
# Pattern: Frequncy sorting
# Variant: sort by count
# Mistakes / Confusion: Na

# 6. **Subarray Sum Equals K** (LC 560)

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = {0:1}

        prefix = 0

        count_subarry = 0

        for i in nums:

            prefix += i

            needed = prefix - k

            if needed in seen:
                count_subarry += seen[needed]
            
            seen[prefix] = seen.get(prefix,0)+1
        
        return count_subarry

# Status: independent
# Time Taken: 10 min
# Time Complexity: O(n) — one pass over the list
# Space Complexity: O(n) — constant extra space 
# Submitted to LC: yes
# Result: Accepted
# Pattern: prefix sum 
# Variant: hash map
# Mistakes / Confusion: Na

# 7. **Contiguous Array** (LC 525)

#brute Force 
# class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_subarry = 0


        for i in range(len(nums)):

            prefix = 0

            for j in range(i,len(nums)):

                if nums[j] == 1:
                    prefix += 1
                else:
                    prefix -= 1
                
                if prefix == 0:
                    max_subarry = max(max_subarry, j-i+1)
        
        return max_subarry

# optimal:

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {0:-1}

        prefix = 0

        max_subarry = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1
            
            if prefix in seen:
                max_subarry = max(max_subarry, i-seen[prefix])
            else:
                seen[prefix] = i
        
        return max_subarry

# Status: independent
# Time Taken: 15 min
# Time Complexity: O(n) — one pass over the list
# Space Complexity: O(n) — constant extra space 
# Submitted to LC: yes
# Result: Accepted
# Pattern: prefix sum 
# Variant: hash map
# Mistakes / Confusion: Na

# 8. **Find the Divisibility Array** (LC 2575)

class Solution(object):
    def divisibilityArray(self, word, m):
        """
        :type word: str
        :type m: int
        :rtype: List[int]
        """
        answer = []

        remainder  = 0

        for i in range(len(word)):

            remainder = (remainder * 10 + int(word[i])) % m

            if remainder == 0:
                answer.append(1)
            else:
                answer.append(0)
        return answer

# Status: independent
# Time Taken: 15 min
# Time Complexity: O(n) — one pass over the list
# Space Complexity: O(1) — constant extra space 
# Submitted to LC: yes
# Result: Accepted
# Pattern: prefix sum 
# Variant: Running modulo
# Mistakes / Confusion: Na

# 9. **Middle of the Linked List** (LC 876)

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
# Time Taken: 10 min
# Time Complexity: O(n) — one pass over the list
# Space Complexity: O(1) — constant extra space 
# Submitted to LC: yes
# Result: Accepted
# Pattern: linked list
# Variant: slow and fast pointer
# Mistakes / Confusion: Na

# 10. **Reorder List** (LC 143)

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
        
        right = prev
        left =head

        while right:

            left_next = left.next
            right_next = right.next

            left.next = right
            right.next = left_next

            left = left_next
            right = right_next
        
        return head

# Status: independent
# Time Taken: 15 min
# Time Complexity: O(n) — one pass over the linked list
# Space Complexity: O(1) — constant extra space 
# Submitted to LC: yes
# Result: Accepted
# Pattern: linked list
# Variant: in place rewiring
# Mistakes / Confusion: Na


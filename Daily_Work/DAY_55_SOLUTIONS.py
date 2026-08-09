### Tier 1 (Mandatory — all due today)

# 1. **LC 1438 — Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit**

# Brute Force:

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        max_length = 0

        for i in range(len(nums)):

            max_element = nums[i]
            min_element = nums[i]

            for j in range(i,len(nums)):

                if nums[j] > max_element:
                    max_element = nums[j]
                if nums[j] < min_element:
                    min_element = nums[j]
                
                if max_element - min_element <= limit:

                    max_length = max(max_length,j-i+1)

        return max_length

#Optimal Solution:

from collections import deque
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        
        max_dq = deque()
        min_dq = deque()

        left = 0

        max_subrray_length = 0

        for right in range(len(nums)):

            while max_dq and nums[right] >= nums[max_dq[-1]]:
                max_dq.pop()
            
            max_dq.append(right)

            while min_dq and nums[right] <= nums[min_dq[-1]]:
                min_dq.pop()
            
            min_dq.append(right)

            while nums[max_dq[0]] - nums[min_dq[0]] > limit:

                if max_dq[0] == left:
                    max_dq.popleft()
                if min_dq[0] == left:
                    min_dq.popleft()
                
                left += 1
            
            if nums[max_dq[0]] - nums[min_dq[0]] <= limit:
                max_subrray_length = max(max_subrray_length,right-left+1)
        
        return max_subrray_length

# Status: independent
# Time Taken: 25m
# Time Complexity:O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Sliding window
# Variant:Deques.
# Mistakes / Confusion:Na


### Tier 4 Template Recalls (Maximum 2 — most overdue)

# 1. **LC 643 — Maximum Average Subarray I**

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left = 0

        prefix = 0

        max_subarray = float('-inf')

        for right in range(len(nums)):

            prefix += nums[right]

            while right-left+1 > k:
                prefix -= nums[left]

                left += 1
            
            if right -left + 1 == k:
                max_subarray = max(max_subarray,prefix)
        
        return max_subarray/float(k)


# Status: independent
# Time Taken: 10m
# Time Complexity:O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Sliding window
# Variant:Fixed size
# Mistakes / Confusion:Na

# 2. **LC 567 — Permutation in String**

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        freq_s1 ={}

        for i in s1:
            freq_s1[i] = freq_s1.get(i,0)+1

        freq_s2 = {}

        
        left = 0 
        
        for right in range(len(s2)):

            freq_s2[s2[right]] = freq_s2.get(s2[right],0)+1

            while right-left+1 > len(s1):
                freq_s2[s2[left]] -= 1

                if freq_s2[s2[left]] == 0:
                    del freq_s2[s2[left]]
                left += 1
            
            if freq_s1 == freq_s2:
                return True
        
        return False

# Status: independent
# Time Taken: 8m
# Time Complexity:O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Sliding window
# Variant:Fixed size
# Mistakes / Confusion:Na

### New Problems (Deque / Sliding Window Max — current variant)

# 1. **LC 862 — Shortest Subarray with Sum at Least K**

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

        for i in range(len(prefix)):

            while dq and prefix[i] - prefix[dq[0]] >= k:

                answer = min(answer,i-dq[0])

                dq.popleft()
            
            while dq and prefix[i] <= prefix[dq[-1]]:

                dq.pop()
            
            dq.append(i)
        return answer if answer != float('inf') else -1

# Status: Hint
# Time Taken: 45m
# Time Complexity:O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Prefix sum
# Variant:monotonic deque
# Mistakes / Confusion:Na


# 2. **LC 1696 — Jump Game VI**

from collections import deque
class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = [0]*len(nums)

        dp[0] = nums[0]

        dq = deque()
        dq.append(0)

        for i in range(1,len(nums)):

            left = i - k

            while dq and dq[0] < left:

                dq.popleft()
            
            dp[i] = nums[i] + dp[dq[0]]

            while dq and dp[i] >= dp[dq[-1]]:

                dq.pop()
            
            dq.append(i)
        
        return dp[-1]

# Status: Hint
# Time Taken: 40m
# Time Complexity:O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Dynamic Programming (DP)
# Variant:Monotonic Deque (Sliding Window Maximum Optimization)
# Mistakes / Confusion:Na

### Tier 3 Revisions (Overdue + Due today — fill to target workload)

# 3. **LC 26 — Remove Duplicates from Sorted Array**

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        write = 1

        for read in range(1,len(nums)):

            if nums[read] != nums[write-1]:
                nums[write] = nums[read]
                write += 1
        return  write

# Status: independent
# Time Taken: 5m
# Time Complexity:O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Two pointers
# Variant: write poineter
# Mistakes / Confusion:Na
#Note: Move This problems to Tier-4 (5 times Tier 3 Passed independent)

# 4. **LC 27 — Remove Element**

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        write = 0

        for read in range(len(nums)):

            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
        return write

# Status: independent
# Time Taken: 5m
# Time Complexity:O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Two pointers
# Variant: write poineter
# Mistakes / Confusion:Na
#Note: Move This problems to Tier-4 (5 times Tier 3 Passed independently)


# 5. **LC 142 — Linked List Cycle II**


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

        left  = head
        right = fast

        
        while left != right:

            left = left.next
            right = right.next
        
        return left

# Status: independent
# Time Taken: 10m
# Time Complexity:O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Linked list
# Variant: Fast and slow pointers
# Mistakes / Confusion:Na

# 6. **LC 234 — Palindrome Linked List**

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
            return True 

        slow = head
        fast = head

        while fast and fast.next:

            prev = slow 
            slow= slow.next
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

        while right :

            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

# Status: independent
# Time Taken: 15m
# Time Complexity:O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Linked list
# Variant: Fast and slow pointers + Revarsal
# Mistakes / Confusion:Na

# 7. **LC 328 — Odd Even Linked List**

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
        if not head:
            return head
        even_head = head.next

        odd = head
        even = head.next

        while even and even.next:

            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd .next
            even = even.next
        
        odd.next = even_head

        return head

# Status: independent
# Time Taken: 10m
# Time Complexity:O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Linked list
# Variant: In place pointers rewiring
# Mistakes / Confusion:Na

# 8. **LC 24 — Swap Nodes in Pairs**

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)

        dummy.next = head

        current = dummy

        while current and current.next:

            first = current.next
            second = first.next

            first.next = first.next.next
            current.next = second
            second.next = first

            current = first
        
        return dummy.next

# Status: independent
# Time Taken: 15m
# Time Complexity:O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Linked list
# Variant: In place pointers rewiring
# Mistakes / Confusion:Na

# 9. **LC 1679 — Max Number of K-Sum Pairs**

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
            
            num = sorted_nums[left] + sorted_nums[right]
            if num == k:
                count += 1
                left += 1
                right -= 1
            elif num < k:
                left += 1
            else:
                right -= 1

        return count

# Status: independent
# Time Taken: 10m
# Time Complexity:O(nlogn)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Two pointers
# Variant: opposite ends
# Mistakes / Confusion:Na

# 10. **LC 1877 — Minimize Maximum Pair Sum in Array**

class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)

        left = 0
        right = len(sorted_nums)-1

        max_pair_value = 0

        while left < right:

            num = sorted_nums[left] + sorted_nums[right]

            max_pair_value = max(max_pair_value,num)

            left += 1
            right -= 1
        return max_pair_value



# Status: independent
# Time Taken: 5m
# Time Complexity:O(nlogn)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Two pointers
# Variant: opposite ends
# Mistakes / Confusion:Na

# **Due today (Aug 6):**

# 11. **LC 692 — Top K Frequent Words**

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        freq_words = {}

        for word in words:
            freq_words[word] = freq_words.get(word,0)+1

        sorted_words = sorted(freq_words.items(),key=lambda x:(-x[1],x[0]))
        
        answer = []
        for word,freq in sorted_words:
            answer.append(word)

            if len(answer) == k:
                return answer

# Status: independent
# Time Taken: 10m
# Time Complexity:O(nlogn)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Frequency hashing + query
# Variant: 
# Mistakes / Confusion:Na
#Note: Move This problems to Tier-4 (5 times Tier 3 Passed independently)

# 12. **LC 167 — Two Sum II - Input Array Is Sorted**

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0

        right = len(numbers)-1


        while left < right:

            if numbers[left]+numbers[right] == target:
                return [left+1,right+1]
            elif numbers[left]+numbers[right] > target:
                right -= 1
            else:
                left += 1

# Status: independent
# Time Taken: 10m
# Time Complexity:O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Two pointers
# Variant: two sum
# Mistakes / Confusion:Na
#Note: Move This problems to Tier-4 (5 times Tier 3 Passed independently)


# 13. **LC 560 — Subarray Sum Equals K**

class Solution(object):
    def subarraySum(self, nums, k):
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

            needed = prefix - k

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
# Pattern:Prefix sum
# Variant: Hash map
# Mistakes / Confusion:Na

# 14. **LC 525 — Contiguous Array**

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        seen = {0:-1}

        prefix = 0

        max_length = 0

        for i in range(len(nums)):

            if nums[i] == 1:
                prefix += 1
            else:
                prefix -= 1
            
            if prefix in seen:
                max_length = max(max_length,i-seen[prefix])
            else:
                seen[prefix] = i
        return max_length

# Status: independent
# Time Taken: 10m
# Time Complexity:O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Prefix sum
# Variant: Hash map
# Mistakes / Confusion:Na

# 15. **LC 278 — First Bad Version**

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n


        while left < right:

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
# Variant: Applied Boundry search
# Mistakes / Confusion:Na

#Note: Move This problems to Tier-4 (5 times Tier 3 Passed independently)


# 16. **LC 744 — Find Smallest Letter Greater Than Target**

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        left = 0
        right = len(letters)-1
        small_char = None

        while left <= right:

            mid = (right+left)//2

            if letters[mid] > target:
                small_char = letters[mid]
                right = mid - 1
            else:
                left = mid + 1
        if small_char == None:
            return letters[0]
        else:
            return small_char


# Status: independent
# Time Taken: 10m
# Time Complexity:O(logn)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Binary search
# Variant: Applied Target search
# Mistakes / Confusion:Na
#Note: Move This problems to Tier-4 (5 times Tier 3 Passed independently)

# 17. **LC 441 — Arranging Coins**

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        best = 0

        while left <= right :

            mid = (right+left)//2
            coins_needed = mid*(mid+1)//2
            if coins_needed == n:
                return mid
            elif coins_needed > n:
                right = mid - 1
            else:
                best = mid
                left = mid + 1
        return best


# Status: independent
# Time Taken: 10m
# Time Complexity:O(logn)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Binary search
# Variant: Applied Target search
# Mistakes / Confusion:Na

# 18. **LC 374 — Guess Number Higher or Lower**

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n

        while left <= right:

            mid = (right+left)//2

            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid - 1
            else:
                left = mid + 1


# Status: independent
# Time Taken: 10m
# Time Complexity:O(logn)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Binary search
# Variant: Applied Target search
# Mistakes / Confusion:Na
#Note: Move This problems to Tier-4 (5 times Tier 3 Passed independently)


# 19. **LC 58 — Length of Last Word**

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        length = 0

        for i in range(len(s)):

            if s[i] == " ":
                count = 0
            else:
                count += 1
            
            if count != 0:
                length = count
        return length

# Status: independent
# Time Taken: 10m
# Time Complexity:O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:String Traversal
# Variant: query
# Mistakes / Confusion:Na
#Note: Move This problems to Tier-4 (5 times Tier 3 Passed independently)

# 20. **LC 33 — Search in Rotated Sorted Array**

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
            elif nums[mid] >= nums[left]:

                if nums[left] <= target <= nums[mid]:
                    right = mid -1
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
# Pattern:Binary search
# Variant: Applied Target Search
# Mistakes / Confusion:Na

# 21. **LC 930 — Binary Subarrays With Sum**

class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        
        prefix = 0
        count = 0
        seen = {0:1}

        for num in range(len(nums)):

            prefix += nums[num]
            needed = prefix - goal

            if needed in seen:
                count += seen[needed]
            
            seen[prefix] = seen.get(prefix,0)+1
        return count 

# Status: independent
# Time Taken: 15m
# Time Complexity:O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:prefix sum
# Variant: Hash map
# Mistakes / Confusion:Na

# 22. **LC 2575 — Find the Divisibility Array of a String**

class Solution(object):
    def divisibilityArray(self, word, m):
        """
        :type word: str
        :type m: int
        :rtype: List[int]
        """
        remainder = 0

        answer = []


        for i in range(len(word)):

            remainder = (remainder*10 + int(word[i])) % m

            if remainder == 0:
                answer.append(1)
            else:
                answer.append(0)
        return answer

# Status: independent
# Time Taken: 10m
# Time Complexity:O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:prefix sum
# Variant: modulo
# Mistakes / Confusion:Na

# 23. **LC 2261 — K Divisible Elements Subarrays**

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

# Status: independent
# Time Taken: 10m
# Time Complexity:O(n^2)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Brute Force
# Variant: Na
# Mistakes / Confusion:Na

# 24. **LC 876 — Middle of the Linked List**

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
                fast= fast.next.next

            
            return slow

# Status: independent
# Time Taken: 5m
# Time Complexity:O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Linked List
# Variant: slow and Fast pointers
# Mistakes / Confusion:Na
#Note: Move This problems to Tier-4 (5 times Tier 3 Passed independently)

# 25. **LC 143 — Reorder List**

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

        while current :
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        left = head
        right = prev

        while right:
            left_next = left.next
            right_next = right.next

            left.next = right 
            right.next = left_next

            left = left_next
            right = right_next
        
        return head

# Status: independent
# Time Taken: 5m
# Time Complexity:O(n)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Linked List
# Variant: slow and Fast pointers + reversal + rewiring
# Mistakes / Confusion:Na
#Note: Move This problems to Tier-4 (5 times Tier 3 Passed independently)

# 26. **LC 23 — Merge k Sorted Lists**

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
            return  lists[0]

        def mergetwo(list1,list2):

            dummy = ListNode(0)

            dummy.next = None

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

            mergedlists = []

            for i in range(0,len(lists),2):

                first = lists[i]

                if i+1 < len(lists):
                    second = lists[i+1]
                else:
                    second = None
                
                merge = mergetwo(first,second)

                mergedlists.append(merge)
            
            lists = mergedlists
        
        return lists[0]

# Status: independent
# Time Taken: 20m
# Time Complexity:O(nlogk)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Linked List
# Variant: Merge k Sorted Lists
# Mistakes / Confusion:Na






        
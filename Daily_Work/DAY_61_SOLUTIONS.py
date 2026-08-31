## Schedule

## Tier -1

# 1	-	LC	-	1002	-	Find Common Characters


class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        common = {}

        for i in words[0]:

            common[i] = common.get(i,0)+1
        
        for word in words:

            freq_word = {}

            for j in word:
                freq_word[j] = freq_word.get(j,0)+1
            
            for key,freq in common.items():

                if key not in freq_word:
                    common[key] = 0
                else:
                    common[key] = min(common[key],freq_word[key])
        
        ans = []

        for char,freq in common.items():

            for i in range(freq):

                ans.append(char)

        return ans

# Status: Hint(common[key] = min(common[key],freq_word[key])) This statemnet was taken from hint.
# Time Taken: 15 m
# Time Complexity: O(W * L) W= number of words L = max length of word
# Space Complexity:O(W * L)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Frequnecy Hashing
# Variant: Frequency Intersection / Common Characters
# Mistakes / Confusion: Confused to updated the frequency of common words.

# 2	-	LC	-	238	-	Product of Array Except Self

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1]

        for i in range(1,len(nums)):

            left.append(nums[i-1]*left[i-1])
        

        right = [1]*len(nums)

        for i in range(len(nums)-2,-1,-1):

            right[i] = nums[i+1]*right[i+1]
        

        answer = []

        for k in range(len(nums)):

            answer.append(right[k]*left[k])
        
        return answer

# Status: Independent
# Time Taken: 15 m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Prefix sum
# Variant:Pivot
# Mistakes / Confusion:

# 3	-	LC	-	2261	-	K Divisible Elements Subarrays

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
                    count +=1
                
                if count > k:
                    break
                
                seen.add(tuple(nums[i:j+1]))

        return len(seen)


# Status: Independent
# Time Taken: 20 m
# Time Complexity: O(n^3)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Brute Force
# Variant:subarry enum
# Mistakes / Confusion:Na

# 4	-	LC	-	2262	-	Total Appeal of A String

# Brute Force 

class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0

        for i in range(len(s)):

            seen = set()

            for j in range(i,len(s)):

                seen.add(s[j])

                count += len(seen)
        
        return count

# Optimal:

class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0

        last = {}

        for i in range(len(s)):

            prev = last.get(s[i],-1)

            left = i - prev

            right = len(s) - i

            contribution = left * right

            answer += contribution

            last[s[i]] = i
        
        return answer


# Status: Independent
# Time Taken: 20 m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Contribution Technique
# Variant:subarry enum
# Mistakes / Confusion:Na

# 5	-	LC	-	1590	-	Make Sum Divisible by P



def minSubarray(nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        
        totalsum = sum(nums)

        target = totalsum % p

        if target == 0:
            return 0
        
        seen = {0:-1}

        length = len(nums)

        prefix = 0

        for i in range(len(nums)):

            prefix += nums[i]

            current = prefix % p

            needed = (current-target)%p

            if needed in seen:

                length = min(length,i-seen[needed])
            
            seen[current] = i

        
        return -1 if length == len(nums) else length

# Status: Independent
# Time Taken: 25 m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Prefix sum
# Variant:modulo
# Mistakes / Confusion:Na

# 6	-	LC	-	328	-	Odd Even Linked List

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

        odd = head
        even_head= head.next
        even = head.next
        
        while even and even.next:
            
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = even_head

        return head


# Status: hint
# Time Taken: 10 m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Linked list
# Variant:inplace nodes rewiring + even and odd nodes.
# Mistakes / Confusion:Na

# 7	-	LC	-	24	-	Swap Nodes in Pairs

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

        current = dummy

        while current.next and current.next.next :

            first = current.next
            second = first.next

            first.next = second.next
            second.next = first

            current.next = second
            current = first
        
        return dummy.next



# Status: hint for while condition
# Time Taken: 10 m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Linked list
# Variant:inplace nodes rewiring + two nodes swaping in place
# Mistakes / Confusion:Na


## Tier -2

# 12	-	LC	-	249	-	Group Shifted Strings


class Solution:
    
    def key(self,string):
        
        answer = []
        for i in range(1,len(string)):
            
            answer.append((ord(string[i])-ord(string[i-1]))%26)
        
        return tuple(answer)   
            
            
    def groupShiftedString(self, arr):
        #code here
        
        group_of_words = {}
        
        for word in arr:
            
            key_of_word = self.key(word)
            
            if key_of_word in group_of_words:
                
                group_of_words[key_of_word] += [word]
            
            else:
                
                group_of_words[key_of_word] = [word]
                
        
        return list(group_of_words.values())


# Status: Hint for (making the key for the words which is )
# Time Taken: 10m
# Time Complexity: O(W*l) 
# Space Complexity:O(W*L)
# Submitted to LC:yES
# Result:Accepted
# Pattern:Frequnecy Hasing
# Variant:Canonical key
# Mistakes / Confusion:


# 13	-	LC	-	890	-	Find and Replace Pattern

class Solution(object):
    def match_words(self,word,pattern):
        if len(word) != len(pattern):
            return False

        seen_word = {}

        seen_pattern= {}

        for i in range(len(word)):

            if word[i] in seen_word and seen_word[word[i]] != pattern[i]:
                return False
            else:
                seen_word[word[i]] = pattern[i]
            
            if pattern[i] in seen_pattern and seen_pattern[pattern[i]] != word[i]:
                return False
            else:
                seen_pattern[pattern[i]] = word[i]
        
        return True




    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        answer = []


        for word in words:

            if self.match_words(word,pattern):

                answer.append(word)
        

        return answer


# Status: indepent
# Time Taken: 15m
# Time Complexity: O(W*l) 
# Space Complexity:O(W*L)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Frequnecy Hasing
# Variant:Canonical key
# Mistakes / Confusion:Na




# 8	-	LC	-	239	-	Sliding Window Maximum


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        answer = []

        for i in range(len(nums)):

            max_num = nums[i]

            for j in range(i,len(nums)):

                max_num = max(max_num,nums[j])

                if j == i+k-1:
                    
                    answer.append(max_num)

                    break
        
        return answer 


#Optimla solution

from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        answer = []

        dq = deque()

        for i in range(len(nums)):

            left = i - k + 1

            while dq and dq[0] < left:

                dq.popleft()
            
            while dq and nums[i] >= nums[dq[-1]]:

                dq.pop()
            
            dq.append(i)

            if i+1 >= k :
                answer.append(nums[dq[0]])

        return answer


# Status: hint
# Time Taken: 20m
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:sliding window
# Variant:Monotonic deque.
# Mistakes / Confusion:Na


# 9	-	LC	-	1438	-	Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

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
            min_num =nums[i]

            for j in range(i,len(nums)):

                max_num = max(max_num,nums[j])
                min_num = min (min_num,nums[j])

                diff = max_num - min_num

                if  diff <= limit:

                    longest_subarray = max(longest_subarray,j-i+1)

        return longest_subarray


# Optimal solution :

from collections import deque
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """

        min_dq = deque()
        max_dq = deque()

        max_lenght = 0

        left = 0

        for right in range(len(nums)):

            while max_dq and nums[right] >= nums[max_dq[-1]]:

                max_dq.pop()
            
            max_dq.append(right)

            while min_dq and nums[right] <= nums[min_dq[-1]]:

                min_dq.pop()
            
            min_dq.append(right)


            while (nums[max_dq[0]]-nums[min_dq[0]]) > limit:

                if max_dq[0] == left:

                    max_dq.popleft()
                
                if min_dq[0] == left:

                    min_dq.popleft()
                
                left += 1
            

            max_lenght = max(max_lenght,right-left+1)
        
        return max_lenght


# Status: hint
# Time Taken: 20m
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:sliding window
# Variant:Monotonic deque.
# Mistakes / Confusion:Na

# 10	-	LC	-	862	-	Shortest Subarray with Sum at Least K

# class Solution(object):
def shortestSubarray(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_length = float('inf')

        for i in range(len(nums)):

            prefix = 0

            for j in range(i,len(nums)):

                prefix += nums[j]

                if prefix >= k:

                    min_length = min(min_length,j-i+1)
        
        return -1 if min_length == float('inf') else min_length


print(shortestSubarray(nums = [2,-1,2], k = 3))
print(shortestSubarray(nums = [1,2], k = 4))
print(shortestSubarray(nums = [1], k = 1))
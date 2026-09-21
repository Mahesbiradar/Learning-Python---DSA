

# 84	-	249	-	Group Shifted Strings	

class Solution:
    
    def string_key(self,string):
        
        result = []
        
        for i in range(1,len(string)):
            
            result.append((ord(string[i]) - ord(string[i-1])) % 26)
            
        return tuple(result)
        
        
    def groupShiftedString(self, arr):
        #code here
        
        group_strings = {}
        
        
        for string in arr:
            
            key = self.string_key(string)
            
            if key in group_strings:
                
                group_strings[key] +=[string]
            else:
                group_strings[key] =[string]
        
        return list(group_strings.values())


# Status: independent
# Time Taken: 7m
# Time Complexity: O(n*l) n = number string in list l= max len of the string 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Group Hash map
# Variant: Cononical key
# Mistakes / Confusion:Na


# 85	-	238	-	Product of Array Except Self

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

        for j in range(len(nums)-2,-1,-1):

            right[j] = nums[j+1]*right[j+1]
        
        result = []

        for k in range(len(nums)):

            result.append(right[k]*left[k])
        
        return result

# Status: independent
# Time Taken: 4m
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: prefix sum
# Variant: pivot
# Mistakes / Confusion:Na

# 86	-	2261	-	K Divisible Elements Subarrays

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

            count_of_p = 0

            for j in range(i,len(nums)):

                if nums[j] % p ==0:

                    count_of_p += 1
                
                if count_of_p > k:

                    break
                
                seen.add(tuple(nums[i:j+1]))
        
        return len(seen)

# Status: independent
# Time Taken: 8m
# Time Complexity: O(n^3) 
# Space Complexity:O(n^3)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Brute Force
# Variant: subarrayenum
# Mistakes / Confusion:Na



# 87	-	1590	-	Make Sum Divisible by P		

class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """

        total_sum = sum(nums)

        target = total_sum % p

        if target == 0:

            return 0
        
        answer = len(nums)

        seen = {0:-1}

        prefix = 0

        for i in range(len(nums)):

            prefix += nums[i]

            current = prefix % p

            needed = (current-target) % p

            if needed in seen:

                answer = min(answer,i-seen[needed])
            
            seen[current] = i
        
        return -1 if answer == len(nums) else answer


# Status: Hint
# Time Taken: 10m
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Prefix sum
# Variant: modulo
# Mistakes / Confusion:Na

# 88	-	1002	-	Find Common Characters		

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        common = {}

        for i in words[0]:

            common[i] = common.get(i,0)+1
        
        for word in range(1,len(words)):

            freq_words = {}

            for char in words[word]:

                freq_words[char] = freq_words.get(char,0)+1
            
            for key,value in common.items():

                if key in freq_words:

                    common[key] = min(common[key],freq_words[key])
                
                else:

                    del common[key]

        result = []

        for key,value in common.items():

            for i in range(value):

                result.append(key)
            
        return result


# Status: Independent
# Time Taken: 6m
# Time Complexity: O(n*l) n=number of words in list l = max length of string 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: frequnecy hashing
# Variant: count + query
# Mistakes / Confusion:Na

# 90	-	328	-	Odd Even Linked List


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
        
        even_head = head.next

        odd = head
        even = head.next

        while even and even.next:

            odd_next = even.next
            even_next = odd_next.next

            odd.next = odd_next
            even.next = even_next

            odd = odd.next
            even = even.next
        

        odd.next = even_head
  
        return head

# Status: Independent
# Time Taken: 10m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Linked List
# Variant: inplace rewiring
# Mistakes / Confusion:Na


# 91	-	24	-	Swap Nodes in Pairs

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

        while current.next and current.next.next:

            first = current.next

            second = first.next

            first.next = second.next

            second.next = first

            current.next = second

            current = first
        
        return dummy.next

# Status: Independent
# Time Taken: 15m
# Time Complexity: O(n)
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Linked List
# Variant: inplace nodes swaping
# Mistakes / Confusion:Na


# 89	-	2262	-	Total Appeal of A String		

class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_occurance = {}

        count = 0

        n = len(s)

        for i in range(len(s)):

            prev = last_occurance.get(s[i],-1)

            left_choice = i - prev

            right_chice = n - i

            contribution = left_choice * right_chice

            count += contribution

            last_occurance[s[i]] = i
        
        return count


# Status: Hint
# Time Taken: 15m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Contribution technique
# Variant: Previous Occurrence / Last Seen Contribution
# Mistakes / Confusion:Na


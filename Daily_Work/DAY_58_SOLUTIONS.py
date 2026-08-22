# 1	-	217	-	Contains Duplicate

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

# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Frequnecy Hasing 
# Variant: Count+query
# Mistakes / Confusion:Na


# 2	-	242	-	Valid Anagram

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        
        freq_s = {}

        for i in s:
            freq_s[i] = freq_s.get(i,0)+1
        
        freq_t = {}

        for j in t:
            freq_t[j] = freq_t.get(j,0)+1
        
        
        if freq_s != freq_t:
            return False
        else:
            return True


# Status: Independent
# Time Taken: 8m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Frequnecy Hasing 
# Variant: Count+query
# Mistakes / Confusion:Na

# 3	-	387	-	First Unique Character

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        freq = {}

        for i in s:
            freq[i] = freq.get(i,0)+1
        
        for j in range(len(s)):

            if freq[s[j]] == 1:
                return j
        
        return -1

# Status: Independent
# Time Taken: 5m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Frequnecy Hasing 
# Variant: Count+query
# Mistakes / Confusion:Na

# 4	-	350	-	Intersection Arrays II

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        freq = {}

        for i in nums1:

            freq[i] = freq.get(i,0)+1
        
        answer = []
        for j in nums2:

            if j in freq and freq[j] > 0:

                answer.append(j)

                freq[j] -= 1
        
        return answer


# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Frequnecy Hasing 
# Variant: Count+query
# Mistakes / Confusion:Na

# 5	-	169	-	Majority Element

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        freq = {}

        for i in nums:

            freq[i] = freq.get(i,0)+1
        
        major_element = None
        freq_element = 0

        for element,frequncy in freq.items():

            if frequncy > freq_element:
                freq_element = frequncy
                major_element = element
        
        return major_element

# Status: Independent
# Time Taken: 5m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Frequnecy Hasing 
# Variant: Count+query
# Mistakes / Confusion:Na

# 6	-	1207	-	Unique Number of Occurrences

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = {}

        for i in arr:

            freq[i] = freq.get(i,0)+1
        
        seen = set()

        for key,value in freq.items():

            if value in seen:
                return False
            seen.add(value)
        
        return True

# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Frequnecy Hasing 
# Variant: Count+query
# Mistakes / Confusion:Na

# 7	-	383	-	Ransom Note

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        freq_ransomNote = {}

        for i in ransomNote:
            freq_ransomNote[i] = freq_ransomNote.get(i,0)+1
        
        freq_magazine = {}

        for j in magazine:
            freq_magazine[j] = freq_magazine.get(j,0)+1
        

        for key,value in freq_ransomNote.items():

            if key not in freq_magazine:
                return False
            elif freq_ransomNote[key] > freq_magazine[key]:
                return False
        
        return True 


# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Frequnecy Hashing 
# Variant: Count+query
# Mistakes / Confusion:Na

# 8	-	1002	-	Find Common Characters

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        common = {}

        for char in words[0]:
            common[char] = common.get(char,0)+1
        

        for word in words[1:]:

            freq = {}

            for char in word:
                freq[char] = freq.get(char,0)+1
            
            for char in common:

                if char in freq:
                    common[char] = min(common[char],freq[char])
                else:
                    common[char] = 0

        
        answer = []

        for key,value in common.items():

            for i in range(value):
                answer.append(key)
        
        return answer


# Status: Hints
# Time Taken: 20m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Frequnecy Hashing 
# Variant: Count+query
# Mistakes / Confusion:Na

# 9	-	49	-	Group Anagrams


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        answer = {}


        for word in strs:

            sorted_word = sorted(word)

            key = ",".join(sorted_word)

            if key in answer:
                answer[key] += [word]
            else:
                answer[key] = [word]
        
        return answer.values()


# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Grouping Hash Map
# Variant: Canonical key
# Mistakes / Confusion:Na

# 10	-	205	-	Isomorphic Strings

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        freq_s = {}
        freq_t = {}


        for i in range(len(s)):

            if s[i] in freq_s and freq_s[s[i]] != t[i]:
                return False
            else:
                freq_s[s[i]] = t[i]
            
            if t[i] in freq_t and freq_t[t[i]] != s[i]:
                return False
            else:
                freq_t[t[i]] = s[i]
        
        return True

# Status: Independent
# Time Taken: 15m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Grouping Hash Map
# Variant: Canonical key
# Mistakes / Confusion:Na

# 11	-	249	-	Group Shifted Strings


class Solution:
    def shifted(self,string):
        
        key = []
        
        for i in range(1,len(string)):
            
            diff = (ord(string[i-1])-ord(string[i]) + 26) % 26
            
            key.append(diff)
        
        return tuple(key)
            
            
    def groupShiftedString(self, arr):
        #code here
        
        answer = {}
        
        for word in arr:
            
            keyword = self.shifted(word)
            
            if keyword in answer:
                
                answer[keyword] += [word]
            else:
                answer[keyword] = [word]
        
        return list(answer.values())


# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n*l) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Grouping Hash Map
# Variant: Canonical key
# Mistakes / Confusion:Na

# 12	-	890	-	Find and Replace Pattern

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        freq_s = {}
        freq_t = {}


        for i in range(len(s)):

            if s[i] in freq_s and freq_s[s[i]] != t[i]:
                return False
            else:
                freq_s[s[i]] = t[i]
            
            if t[i] in freq_t and freq_t[t[i]] != s[i]:
                return False
            else:
                freq_t[t[i]] = s[i]
        
        return True


    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        answer = []

        for word in words:

            if self.isIsomorphic(word,pattern):
                answer.append(word)
        

        return answer


# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n*l) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Grouping Hash Map
# Variant: Canonical key
# Mistakes / Confusion:Na

# 13	-	347	-	Top K Frequent Elements

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}

        for i in nums:
            freq[i] = freq.get(i,0)+1
        
        sorted_nums = sorted(freq.items(),key=lambda x:x[1],reverse=True)
        
        ans = []
        for key,value in sorted_nums:

            ans.append(key)

            if len(ans) == k:
                return ans


# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(nlogn) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Frequency sorting
# Variant: sort by count
# Mistakes / Confusion:Na

# 14	-	451	-	Sort Chars by Frequency

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}

        for i in s:

            freq[i] = freq.get(i,0)+1

        sorted_freq = sorted(freq.items(),key=lambda x:x[1],reverse=True)

        ans = ""

        for key,value in sorted_freq:

            ans += key*value

        return ans

# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(nlogn) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Frequency sorting
# Variant: sort by count
# Mistakes / Confusion:Na


# 15	-	692	-	Top K Frequent Words

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq = {}

        for i in words:

            freq[i] = freq.get(i,0)+1
        
        sorted_words = sorted(freq.items(),key=lambda x: (-x[1],x[0]))

        ans = []

        for key, value in sorted_words:

            ans.append(key)

            if len(ans) == k:
                return ans

# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(nlogn) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Frequency sorting
# Variant: sort by count
# Mistakes / Confusion:Na

# 16	-	1	-	Two Sum

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

# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Complement lookup
# Variant: Two sum style
# Mistakes / Confusion:Na

# 17	-	167	-	Two Sum II

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = numbers
        left = 0
        right = len(nums)-1

        while left < right:

            sum_of_nums = nums[left] + nums[right]

            if sum_of_nums == target:
                return [left+1,right+1]
            elif sum_of_nums > target:
                right -= 1
            else:
                left += 1
        
        return -1

# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern:Two pointers
# Variant: opposite end
# Mistakes / Confusion:Na

# 18	-	1480	-	Running Sum

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [nums[0]]

        for i in range(1,len(nums)):

            answer.append(answer[i-1]+nums[i])
        
        return answer


# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Prefix sum
# Variant: running prefix
# Mistakes / Confusion:Na

# 19	-	1732	-	Find Highest Altitude

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        prefix_sum = 0

        ans = 0

        for i in range(len(gain)):

            prefix_sum += gain[i]

            ans = max(ans,prefix_sum)
        
        return ans

# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Prefix sum
# Variant: running prefix
# Mistakes / Confusion:Na

# 20	-	724	-	Find Pivot Index

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0

        total_sum = sum(nums)


        for i in range(len(nums)):

            right = total_sum - left - nums[i]

            if left == right:
                return i
            
            left += nums[i]
        
        return -1 

# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Prefix sum
# Variant: pivot
# Mistakes / Confusion:Na


# 21	-	238	-	Product of Array Except Self

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1]

        for i in range(1,len(nums)):
            left.append(left[i-1]*nums[i-1])
 

        right = [1]*len(nums)

        for j in range(len(nums)-2,-1,-1):
            right[j] = right[j+1]*nums[j+1]

        result = []
       
        for k in range(len(nums)):
            result.append(left[k]*right[k])
        
        return result


# Status: Hint(One mostake made which calculating prefix and suffix array.)
# Time Taken: 15m 
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Prefix sum
# Variant: Pivot
# Mistakes / Confusion:Na

# 22	-	560	-	Subarray Sum Equals K

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


# Status: Independent
# Time Taken: 20m 
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Prefix sum
# Variant: Prefix + Hashmap
# Mistakes / Confusion:Na

# 23	-	303	-	Range Sum Query


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = [0]

        for i in range(len(nums)):

            self.prefix.append(nums[i]+self.prefix[i])
        
        print(self.prefix)
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix[right+1]-self.prefix[left]


# Status: Independent
# Time Taken: 20m 
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Prefix sum
# Variant: Prefix array
# Mistakes / Confusion:Na

# 24	-	525	-	Contiguous Array


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {0:-1}

        prefix = 0

        length = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                prefix -=1
            else:
                prefix += 1

            if prefix in seen:
                length = max(length,i-seen[prefix])
            else:
                seen[prefix] = i
        
        return length

# Status: Independent
# Time Taken: 20m 
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Prefix sum
# Variant: Hash map
# Mistakes / Confusion:Na

# 25	-	523	-	Continuous Subarray Sum

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {0:-1}

        prefix = 0

        for i in range(len(nums)):

            prefix += nums[i]

            needed = prefix % k

            if needed in seen:
                if i-seen[needed] > 1:
                    return True
            else:
                seen[needed] = i
        return False 

# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Prefix sum
# Variant: Modulo
# Mistakes / Confusion:Na

# 26	-	125	-	Valid Palindrome

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s)-1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1
            
            while left < right and not s[right].isalnum():
                right -=1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True 

# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Two pointers
# Variant: opposite ends
# Mistakes / Confusion:Na

# 27	-	344	-	Reverse String

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        left = 0
        right = len(s)-1

        while left < right:

            s[left],s[right] = s[right],s[left]

            left += 1
            right -= 1

        return s

# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Two pointers
# Variant: opposite ends
# Mistakes / Confusion:Na

# 28	-	392	-	Is Subsequence

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        write = 0

        for i in range(len(t)):

            if len(s) == write:
                return True
                
            if s[write] == t[i]:
                write += 1
                
            

        return True if len(s) == write else False

# Status: Independent
# Time Taken: 5m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Two pointers
# Variant: is subsequnce
# Mistakes / Confusion:Na

# 29	-	26	-	Remove Duplicates

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        write = 1

        for i in range(1,len(nums)):

            if nums[i] != nums[write-1]:
                nums[write] = nums[i]
                write += 1
        return write

# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Two pointers
# Variant: write pointer
# Mistakes / Confusion:Na

# 30	-	27	-	Remove Element

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        write = 0

        for i in range(len(nums)):

            if nums[i] != val :
                nums[write] = nums[i]
                write += 1
        return write

# Status: Independent
# Time Taken: 5m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Two pointers
# Variant: write pointer
# Mistakes / Confusion:Na

# 31	-	283	-	Move Zeroes

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        write = 0

        for i in range(len(nums)):

            if nums[i] != 0:
                nums[write] = nums[i]
                write += 1
        
        for i in range(write,len(nums)):

            nums[i] = 0
        
        return nums 


# Status: Independent
# Time Taken: 5m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Two pointers
# Variant: write pointer
# Mistakes / Confusion:Na

# 32	-	80	-	Remove Duplicates from Sorted Array II

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<= 2:
            
            return len(nums)

        write = 2

        for i in range(2,len(nums)):

            if nums[i] != nums[write-2]:
                nums[write] = nums[i]
                write += 1
        return  write 

# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Two pointers
# Variant: write pointer
# Mistakes / Confusion:Na


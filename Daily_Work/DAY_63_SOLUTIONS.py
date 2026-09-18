# DAY 60

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
# Time Taken: 5m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Frequncy Hashing
# Variant:Contains Duplicate
# Mistakes / Confusion:Na

# 2	-	242	-	Valid Anagram

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq_s = {}

        for i in s:

            freq_s[i] = freq_s.get(i,0)+1
        
        freq_t = {}

        for j in t:

            freq_t[j] = freq_t.get(j,0)+1
        
        return freq_s == freq_t

# Status: Independent
# Time Taken: 5m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Frequncy Hashing
# Variant:Valid anagram
# Mistakes / Confusion:Na


# 3	-	387	-	First Unique Character

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}

        for i in s:

            seen[i] = seen.get(i,0)+1
        
        for j in range(len(s)):

            if seen[s[j]] == 1:
                return j
        
        return -1

# Status: Independent
# Time Taken: 3m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Frequncy Hashing
# Variant:First unique Char
# Mistakes / Confusion:Na


# 4	-	350	-	Intersection Arrays II

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        seen_nums2 = {}

        for i in nums2:

            seen_nums2[i] = seen_nums2.get(i,0)+1

        result = []

        for j in nums1:

            if j in seen_nums2 and seen_nums2[j] >= 1:

                result.append(j)

                seen_nums2[j] -= 1
        
        return result


# Status: Independent
# Time Taken: 5m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Frequncy Hashing
# Variant:intersection array
# Mistakes / Confusion:Na


# 5	-	169	-	Majority Element


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        seen = {}

        for i in nums:

            seen[i] = seen.get(i,0)+1
        
        majority_elemenet = None

        max_freq = 0

        for j in range(len(nums)):

            if seen[nums[j]] > max_freq:

                max_freq = seen[nums[j]]

                majority_elemenet = nums[j]
        
        return majority_elemenet

# Status: Independent
# Time Taken: 6m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Frequncy hashing
# Variant:Majority Element
# Mistakes / Confusion:Na


# 6	-	1207	-	Unique Number of Occurrences


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        freq_arr = {}

        for i in arr:

            freq_arr[i] = freq_arr.get(i,0)+1
        
        seen = set()

        for key,value in freq_arr.items():

            if value in seen:

                return False
            
            seen.add(value)
            
        return True

# Status: Independent
# Time Taken: 4m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Frequncy hashing
# Variant:Unique Occurance
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
        
        for key,value in freq_ransomNote.items() :

            if key not in freq_magazine or freq_magazine[key] < freq_ransomNote[key]:

                return False
                
        return True

# Status: Independent
# Time Taken: 8m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Frequncy hashing
# Variant:Ransome note
# Mistakes / Confusion:Na


# 8	-	49	-	Group Anagrams

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}

        for string in strs:

            sorted_string = sorted(string)

            key = " ".join(sorted_string)

            if key in result:

                result[key] += [string]
            else:

                result[key] = [string]
        
        
        return list(result.values())


# Status: Independent
# Time Taken: 6m 
# Time Complexity: O(nlogn)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Frequncy hashing
# Variant:group anagram
# Mistakes / Confusion:Na

# 9	-	205	-	Isomorphic Strings

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
# Time Taken: 8m 
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Frequncy hashing
# Variant: isomorphic string
# Mistakes / Confusion:Na

# 10	-	890	-	Find and Replace Pattern		

class Solution(object):
    def isisomorphic(self,s,t):

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

        result = []


        for word in words:

            if self.isisomorphic(word,pattern):

                result.append(word)
        
        return result

# Status: Independent
# Time Taken: 5m 
# Time Complexity: O(n*l) n = number strings in words l = max len of the word
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Frequncy hashing
# Variant: Fina and replace words
# Mistakes / Confusion:Na


# 11	-	347	-	Top K Frequent Elements

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        freq_nums = {}

        for i in nums:

            freq_nums[i] = freq_nums.get(i,0)+1

        sorted_nums = sorted(freq_nums.items(),key=lambda x:x[1],reverse=True)

        result = []

        for key,value in sorted_nums:

            result.append(key)

            if len(result) == k:

                return result


# Status: Independent
# Time Taken: 5m 
# Time Complexity: O(nlogn) 
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Frequncy hashing
# Variant: Hash map + sorting
# Mistakes / Confusion:Na


# 12	-	451	-	Sort Chars by Frequency

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen_s = {}

        for i in s:

            seen_s[i] = seen_s.get(i,0)+1

        sorted_string = sorted(seen_s.items(),key=lambda x:x[1],reverse = True)

        out =""

        for char,freq in sorted_string:

            out += char*freq
        
        return out


# Status: Independent
# Time Taken: 8m 
# Time Complexity: O(nlogn) 
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Frequncy hashing
# Variant: Hash map + sorting
# Mistakes / Confusion:Na

# 13	-	692	-	Top K Frequent Words		


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        freq_words = {}

        for i in words:

            freq_words[i] = freq_words.get(i,0)+1
        
        sorted_words = sorted(freq_words.items(),key=lambda x:(-x[1],x[0]))

        
        result = []

        for word,freq in sorted_words:

            result.append(word)

            if len(result) == k:

                return result

# Status: Independent
# Time Taken: 7m 
# Time Complexity: O(nlogn) 
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Frequncy hashing
# Variant: Hash map + sorting
# Mistakes / Confusion:Na


# 14	-	1	-	Two Sum

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
# Time Taken: 3m 
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Complement lookup
# Variant: Hashmap
# Mistakes / Confusion:Na

# 15	-	167	-	Two Sum II		

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left = 0

        num = numbers

        right = len(num)-1

        while left < right:

            sum_of_pointers = num[left]+num[right]

            if sum_of_pointers == target:

                return  [left+1,right+1]

            elif sum_of_pointers > target:

                right -= 1

            else:

                left += 1

# Status: Independent
# Time Taken: 3m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Two pointers
# Variant: Two sum 2
# Mistakes / Confusion:Na

# 16	-	1480	-	Running Sum		


class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = [nums[0]]

        for i in range(1,len(nums)):

            result.append(result[i-1]+nums[i])
        
        return result

# Status: Independent
# Time Taken: 2m 
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Prefix sum
# Variant: running sum
# Mistakes / Confusion:Na

# 17	-	1732	-	Find Highest Altitude		

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        prefix = 0

        max_alt = 0

        for i in range(len(gain)):

            prefix += gain[i]

            max_alt = max(max_alt,prefix)

        return max_alt


# Status: Independent
# Time Taken: 4m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Prefix sum
# Variant: running sum 
# Mistakes / Confusion:Na

# 18	-	724	-	Find Pivot Index

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0

        totalsum = sum(nums)

        for i in range(len(nums)):

            right = totalsum - left - nums[i]

            if left == right:
                return i
            
            left += nums[i]
        
        return -1

# Status: Independent
# Time Taken: 4m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Prefix sum
# Variant: pivot index 
# Mistakes / Confusion:Na

# 19	-	560	-	Subarray Sum Equals K		

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
# Time Taken: 4m 
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Prefix sum
# Variant: Hash map
# Mistakes / Confusion:Na


# 20	-	303	-	Range Sum Query		

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = [0]

        for i in range(len(nums)):

            self.prefix.append(nums[i]+self.prefix[i])
        

    def sumRange(self, left, right):
    #     """
    #     :type left: int
    #     :type right: int
    #     :rtype: int
    #     """

        return self.prefix[right+1]-self.prefix[left]

# Status: Independent
# Time Taken: 5m 
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Prefix sum
# Variant: range sum query
# Mistakes / Confusion:Na


# 21	-	525	-	Contiguous Array		

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {0:-1}

        prefix = 0

        max_len = 0

        for i in range(len(nums)):

            if nums[i] == 1:
                prefix += 1
            else:
                prefix -= 1
            
            if prefix in seen:

                max_len = max(max_len,i-seen[prefix])
            
            else:

                seen[prefix] = i
        
        return max_len

# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Prefix sum
# Variant: hash map
# Mistakes / Confusion:Na

# 22	-	523	-	Continuous Subarray Sum		

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

            remainder = prefix % k

            if remainder in seen:

                if i-seen[remainder] > 1:

                    return True
            else:

                seen[remainder] = i
            
        return False

# Status: Independent
# Time Taken: 6m 
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Prefix sum
# Variant: Modulo
# Mistakes / Confusion:Na


# 23	-	125	-	Valid Palindrome

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
            
            while left < right and  not s[right].isalnum():

                right -= 1

            if s[left].lower() != s[right].lower():

                return False
            
            left += 1

            right -= 1

        
        return True


# Status: Independent
# Time Taken: 8m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Two pointers
# Variant: Palindrom
# Mistakes / Confusion:Na

# 24	-	344	-	Reverse String		

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

# Status: Independent
# Time Taken: 5m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Two pointers
# Variant: reverese string
# Mistakes / Confusion:Na


# 25	-	392	-	Is Subsequence

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        if not t:
            return False
        
        write = 0

        for i in range(len(t)):

            if t[i] == s[write]:
                write += 1
            
            if len(s) == write:
                return True

        return False

# Status: Independent
# Time Taken: 8m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Two pointers
# Variant: is subsequnce
# Mistakes / Confusion:Na

# 26	-	26	-	Remove Duplicates		


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
# Time Taken: 4m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Write pointer
# Variant: remove duplicate
# Mistakes / Confusion:Na

# 27	-	27	-	Remove Element		

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        write = 0

        for i in range(len(nums)):

            if nums[i] != val:

                nums[write] = nums[i]

                write += 1
        
        return write

# Status: Independent
# Time Taken: 2m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Write pointer
# Variant: remove duplicate
# Mistakes / Confusion:Na

# 28	-	283	-	Move Zeroes		

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
        
        for j in range(write,len(nums)):

            nums[j] = 0

# Status: Independent
# Time Taken: 3m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Write pointer
# Variant: move zeros
# Mistakes / Confusion:Na


# 29	-	80	-	Remove Duplicates from Sorted Array II		

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        write = 2

        for i in range(2,len(nums)):

            if nums[i] != nums[write-2]:

                nums[write] = nums[i]

                write += 1
        
        return write


# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Write pointer
# Variant: remove duplicates from sorted array
# Mistakes / Confusion:Na


# 30	-	11	-	Container With Most Water		


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0

        right = len(height)-1

        max_water = 0


        while left < right:

            water = min(height[left],height[right])*(right-left)

            max_water = max(max_water,water)

            if height[left] > height[right]:

                right -= 1  
            else:
                left += 1
        
        return max_water


# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Two pointer
# Variant: Opposite end moving towards mid
# Mistakes / Confusion:Na


# 31	-	643	-	Maximum Average Subarray I		


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        left = 0

        prefix = 0

        suarray_sum = float('-inf')

        for i in range(len(nums)):

            prefix += nums[i]

            while i-left+1 > k:

                prefix -= nums[left]

                left += 1
            
            if i-left+1 == k:

                suarray_sum = max(suarray_sum,prefix)
            
        return suarray_sum / float(k)


# Status: Independent
# Time Taken: 15m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:sliding window
# Variant: fixed size
# Mistakes / Confusion:Na

# 32	-	567	-	Permutation in String		

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        freq_s1 = {}

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

# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:sliding window
# Variant: fixed size
# Mistakes / Confusion:Na

# 33	-	438	-	Find All Anagrams	

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        freq_p = {}

        for i in p:

            freq_p[i] = freq_p.get(i,0)+1
        
        freq_s ={}

        left = 0

        result = []

        for right in range(len(s)):

            freq_s[s[right]] = freq_s.get(s[right],0)+1

            while right-left+1 > len(p):

                freq_s[s[left]] -= 1

                if freq_s[s[left]] == 0:

                    del freq_s[s[left]]
                left += 1
            
            if freq_s == freq_p:

                result.append(left)
                
        return result

# Status: Independent
# Time Taken: 8m 
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:sliding window
# Variant: fixed size
# Mistakes / Confusion:Na


# 34	-	219	-	Contains Duplicate II		

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        seen = set()


        left = 0

        for right in range(len(nums)):

            if nums[right] in seen:

                return True
            
            seen.add(nums[right])

            while right-left+1 > k:

                seen.remove(nums[left])

                left += 1

        return False

# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:sliding window
# Variant: fixed size
# Mistakes / Confusion:Na


# 35	-	1456	-	Maximum Number of Vowels


class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_vowels = 0

        left = 0

        count = 0

        for right in range(len(s)):

            if s[right] in ["a","e","i","o","u"]:
                count += 1

            while right-left+1 > k:

                if s[left] in ["a","e","i","o","u"]:
                    count -= 1

                left += 1
            
            if right-left+1 == k:

                max_vowels = max(count,max_vowels)

        return max_vowels


# Status: Independent
# Time Taken: 8m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:sliding window
# Variant: fixed size
# Mistakes / Confusion:Na


# 36	-	3	-	Longest Substring Without Repeating


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()

        max_length = 0

        left = 0

        for right in range(len(s)):

            while s[right] in seen:

                seen.remove(s[left])

                left += 1
            
            seen.add(s[right])

            max_length = max(max_length,right-left+1)
        
        return max_length


# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:sliding window
# Variant: Variable size
# Mistakes / Confusion:Na

# 37	-	209	-	Minimum Size Subarray Sum


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0

        prefix = 0

        min_length = float('inf')

        for right in range(len(nums)):

            prefix += nums[right]

            while prefix >= target :

                min_length = min(min_length,right-left+1)

                prefix -= nums[left]

                left += 1
                
        
        return 0 if min_length == float('inf') else min_length


# Status: Independent
# Time Taken: 15m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:sliding window
# Variant: Variable size
# Mistakes / Confusion:Na


# 38	-	904	-	Fruits Into Baskets

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        seen = {}

        left = 0

        max_Fruits = 0

        for right in range(len(fruits)):

            seen[fruits[right]] = seen.get(fruits[right],0)+1

            while len(seen) > 2:

                seen[fruits[left]] -= 1

                if seen[fruits[left]] == 0:

                    del seen[fruits[left]]

                left += 1
            
            max_Fruits = max(max_Fruits,right-left+1)
        
        return max_Fruits

# Status: Independent
# Time Taken: 15m 
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:sliding window
# Variant: Variable size
# Mistakes / Confusion:Na

# 39	-	1004	-	Max Consecutive Ones III

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        max_ones = 0

        ones_count = 0

        left = 0

        for right in range(len(nums)):

            if nums[right] == 1:

                ones_count += 1
            
            while (right-left+1)-ones_count > k:

                if nums[left] == 1:

                    ones_count -= 1
                
                left += 1
            
            max_ones = max(max_ones,right-left+1)

        return max_ones

# Status: Independent
# Time Taken: 5m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:sliding window
# Variant: Variable size
# Mistakes / Confusion:Na


# 40	-	424	-	Longest Repeating Char Replacement


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        seen = {}

        left = 0

        long_char = 0

        for right in range(len(s)):

            seen[s[right]] = seen.get(s[right],0)+1

            max_char = max(seen.values())

            while (right-left+1) - max_char > k:

                seen[s[left]] -= 1

                if seen[s[left]] == 0:

                    del seen[s[left]]
                
                left += 1
            
            long_char = max(long_char,right-left+1)

        return long_char

# Status: Independent
# Time Taken: 8m 
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:sliding window
# Variant: Variable size
# Mistakes / Confusion:Na


# 41	-	121	-	Best Time to Buy and Sell Stock		

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

                min_price = prices[i]
            else:

                profit = prices[i] - min_price

                max_profit = max(max_profit,profit)
        
        return max_profit

# Status: Independent
# Time Taken: 5m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Running State
# Variant:kadane min / max 
# Mistakes / Confusion:Na

# 42	-	53	-	Maximum Subarray

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_subarry = float('-inf')

        prefix = float('-inf')

        for i in range(len(nums)):

            prefix = max(nums[i],prefix+nums[i])

            max_subarry = max(prefix,max_subarry)
        
        return max_subarry

# Status: Independent
# Time Taken: 5m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Running State
# Variant:kadane min / max 
# Mistakes / Confusion:Na

# 43	-	152	-	Maximum Product Subarray


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        current_max = nums[0]

        current_min = nums[0]

        max_product = nums[0]


        for i in range(1,len(nums)):

            temp_max = max(nums[i],nums[i]*current_max,nums[i]*current_min)

            temp_min = min(nums[i],nums[i]*current_min,nums[i]*current_max)

            current_max = temp_max

            current_min = temp_min

            max_product = max(max_product,current_max)
        
        return  max_product

# Status: Hint
# Time Taken: 15m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Running State
# Variant:kadane min / max 
# Mistakes / Confusion:Na

# 44	-	704	-	Binary Search	

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
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1



# Status: independent
# Time Taken: 7m 
# Time Complexity: O(logn) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Binary search
# Variant:Applied Target Search 
# Mistakes / Confusion:Na

# 45	-	35	-	Search Insert Position

class Solution(object):
    def searchInsert(self, nums, target):
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

            elif nums[mid] < target:

                left = mid + 1

            else :
                
                right = mid - 1

        return left

# Status: independent
# Time Taken: 8m 
# Time Complexity: O(logn) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Binary search
# Variant:Applied Target Search 
# Mistakes / Confusion:Na


# 46	-	278	-	First Bad Version


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

        while left < right:

            mid = (right+left)//2

            if isBadVersion(mid):

                right = mid
            else:
                left = mid + 1
        
        return left 


# Status: independent
# Time Taken: 5m 
# Time Complexity: O(logn) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Binary search
# Variant:Applied Boundry Search 
# Mistakes / Confusion:Na

# 47	-	69	-	Sqrt(x)

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        left = 0

        right = x

        while left <= right :

            mid = (left+right)//2

            num = mid*mid

            if num == x:
                return mid
            elif num > x:
                right = mid - 1
            else:
                left = mid + 1
        
        return right

# Status: independent
# Time Taken: 8m 
# Time Complexity: O(logn) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Binary search
# Variant:Applied Target Search 
# Mistakes / Confusion:Na


# 48	-	744	-	Find Smallest Letter Greater

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = 0
        right = len(letters)-1

        best = None

        while left <= right:

            mid = (right+left)//2

            if letters[mid] > target:
                
                best = letters[mid]

                right = mid - 1
            else:

                left = mid + 1

        return letters[0] if not best else best


# Status: independent
# Time Taken: 8m 
# Time Complexity: O(logn) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Binary search
# Variant:Applied Target Search 
# Mistakes / Confusion:Na

# 49	-		-	Find Peak Element		


class Solution(object):
    def findPeakElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        while left < right:

            mid = (right+left)//2

            if nums[mid] > nums[mid+1]:

                right = mid
            else:

                left = mid + 1
                
        return left 


# Status: independent
# Time Taken: 5m 
# Time Complexity: O(logn) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Binary search
# Variant:Applied Broundry Search 
# Mistakes / Confusion:Na

# 50	-	367	-	Valid Perfect Square	

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 0

        right = num

        while left <= right:

            mid = (left+right)//2

            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1
        return False

# Status: independent
# Time Taken: 5m 
# Time Complexity: O(logn) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Binary search
# Variant:Applied Target Search 
# Mistakes / Confusion:Na


# 51	-	441	-	Arranging Coins

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0

        right = n 

        ans = None

        while left <= right:

            mid = (right+left)//2

            coins_needed = mid*(mid+1)//2

            if coins_needed == n:

                return mid
            
            elif coins_needed > n:

                right = mid - 1
            else:
                ans = mid

                left = mid + 1
        
        return ans

# Status: independent
# Time Taken: 7m 
# Time Complexity: O(logn) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Binary search
# Variant:Applied Target Search 
# Mistakes / Confusion:Na

# 52	-	374	-	Guess Number Higher or Lower		


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

            mid = (right+left)//2

            res = guess(mid)

            if res == 0:
                return mid
            elif res == 1:
                left = mid + 1 
            else:
                right = mid - 1


# Status: independent
# Time Taken: 8m 
# Time Complexity: O(logn) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Binary search
# Variant:Applied Target Search 
# Mistakes / Confusion:Na

# 53	-	852	-	Peak Index in Mountain Array		


class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        left = 0

        right = len(arr)-1

        while left < right:

            mid = (left+right)//2

            if arr[mid] > arr[mid+1]:

                right = mid 
            else:
                left = mid + 1

        return left  

# Status: independent
# Time Taken: 5m 
# Time Complexity: O(logn) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Binary search
# Variant:Applied Boundry Search 
# Mistakes / Confusion:Na

# 54	-	58	-	Length of Last Word

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        len_last_word = 0

        count = 0


        for i in range(len(s)):

            if s[i] == " ":

                count = 0
            else:
                count += 1
            
            if count != 0:
                len_last_word = count
        
        return len_last_word

# Status: independent
# Time Taken: 3m 
# Time Complexity: O(n) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:String traversal
# Variant:Na
# Mistakes / Confusion:Na

# 55	-	33	-	Search in Rotated Sorted Array	


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
# Time Taken: 3m 
# Time Complexity: O(logn) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:binary search
# Variant:Applied Target search
# Mistakes / Confusion:Na

# 56	-	153	-	Find Minimum in Rotated Sorted Array


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
# Time Taken: 10m 
# Time Complexity: O(logn) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:binary search
# Variant:Applied Boundry search
# Mistakes / Confusion:Na



# 57	-	875	-	Koko Eating Bananas

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        def isfeasible(speed):

            count = 0

            for i in piles:

                remainder = 0 if i % speed == 0 else 1

                divisor = i // speed

                count += divisor + remainder
            
            return True if count <= h else False


        left = 1

        right = max(piles)

        while left < right:

            mid = (right+left)//2

            if isfeasible(mid):

                right = mid
            else:
                left = mid + 1
        
        return left

# Status: independent
# Time Taken: 10m 
# Time Complexity: O(logn) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:binary search
# Variant:Applied Boundry search
# Mistakes / Confusion:Na

# 58	-	930	-	Binary Subarrays With Sum		

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

        for i in range(len(nums)):

            prefix += nums[i]

            needed = prefix - goal

            if needed in seen:

                count += seen[needed]
            
            seen[prefix] = seen.get(prefix,0)+1
        
        return count 

# Status: independent
# Time Taken: 6m 
# Time Complexity: O(n) 
# Space Complexity:O(n)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:prefix sum
# Variant:hash map
# Mistakes / Confusion:Na

# 59	-	1679	-	Max Number of K-Sum Pairs

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        sorted_nums = sorted(nums)

        left = 0

        right = len(nums)-1

        count = 0

        while left < right:

            sum_of = sorted_nums[left] + sorted_nums[right]
            if sum_of == k:
                count += 1
                left += 1
                right -= 1
            elif sum_of > k :
                right -=1 
            else:
                left += 1
            
        return count 

# Status: independent
# Time Taken: 6m 
# Time Complexity: O(nlogn) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Two pointers
# Variant:Maximize sorted
# Mistakes / Confusion:Na

# 60	-	1877	-	Minimize Maximum Pair Sum	


class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s_nums = sorted(nums)

        left = 0

        right = len(nums)-1

        max_sum = 0

        while left < right:

            sum_of_pointers = s_nums[left] + s_nums[right]

            max_sum = max(max_sum,sum_of_pointers)

            left += 1
            right -= 1
        
        return max_sum

# Status: independent
# Time Taken: 3m 
# Time Complexity: O(nlogn) 
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Two pointers
# Variant:Maximize sorted
# Mistakes / Confusion:Na


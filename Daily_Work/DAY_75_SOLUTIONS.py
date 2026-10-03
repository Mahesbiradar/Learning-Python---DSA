# DAY 74

# Status:
# Time Taken:
# Time Complexity:
# Space Complexity:
# Submitted to LC:
# Result:
# Pattern:
# Variant:
# Mistakes / Confusion:



# New

"""

1	-	LC	-	1991	-	Find the Middle Index in Array	-	Prefix Sum	-	Pivot / equilibrium
2	-	LC	-	2270	-	Number of Ways to Split a String	-	Prefix Sum	-	Pivot / equilibrium
3	-	LC	-	1413	-	Maximum Average Subarray I	-	Prefix Sum	-	Running prefix

"""

# 1	-	LC	-	1991	-	Find the Middle Index in Array	-	Prefix Sum	-	Pivot / equilibrium


class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        totalsum = sum(nums)

        left = 0


        for i in range(len(nums)):

            rightsum = totalsum - nums[i] - left

            if left == rightsum:

                return i

            left += nums[i]
        
        return -1 



# Status: independent
# Time Taken: 8m 
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Prefix sum
# Variant: Pivot / Equilibrium
# Mistakes / Confusion:

# 2	-	LC	-	2270	-	Number of Ways to Split a String	-	Prefix Sum	-	Pivot / equilibrium


class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = nums[0]

        totalsum = sum(nums)

        count = 0

        for i in range(1,len(nums)):

            right = totalsum - left

            if left >= right:

                count += 1
            
            left += nums[i]
        
        return count

# Status: independent
# Time Taken: 10m 
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Prefix sum
# Variant: Pivot / Split Point
# Mistakes / Confusion:Na Similar problems like above here we split two array left and right if the sum of left arry >= right then we have valid split and update out answer.


# 3	-	LC	-	1413	-	Maximum Average Subarray I	-	Prefix Sum	-	Running prefix

class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        prefix = 0

        min_prefix = float('inf')

        for i in range(len(nums)):

            prefix += nums[i]

            min_prefix = min(min_prefix,prefix)
        
        answer = max(1,1-min_prefix)

        return answer

# Status: Hint
# Time Taken: 10m 
# Time Complexity: O(n)
# Space Complexity: O(1)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Prefix sum
# Variant: Running prefix
# Mistakes / Confusion:Na


"""

1	-	LC	-	1371	-	Find the Longest Substring Containing Vowels in Even Counts	-	Prefix Sum	-	Prefix + Hash Map
2	-	LC	-	2845	-	Count of Interesting Subarrays	-	Prefix Sum	-	Modulo variant
3	-	LC	-	2483	-	Count Subarrays With Score Less Than K	-	Prefix Sum	-	Pivot / equilibrium

"""

# 1	-	LC	-	1371	-	Find the Longest Substring Containing Vowels in Even Counts	-	Prefix Sum	-	Prefix + Hash Map

class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """ 

        vower_to_bit = {"a":1,"e":2,"i":4,"o":8,"u":16}

        seen = {0:-1}

        current_mask = 0

        max_len = 0

        for i in range(len(s)):

            if s[i] in vower_to_bit:
                current_mask ^= vower_to_bit[s[i]]
                
            if current_mask in seen:

                max_len = max(max_len,i-seen[current_mask])
            
            else:

                seen[current_mask] = i
            
        return max_len


# Status: Hint
# Time Taken: 20m 
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Prefix
# Variant: Prefix + Hash Map
# Mistakes / Confusion:Na

# 2	-	LC	-	2845	-	Count of Interesting Subarrays	-	Prefix Sum	-	Modulo variant

class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        """
        :type nums: List[int]
        :type modulo: int
        :type k: int
        :rtype: int
        """

        interesting = []

        for i in nums:

            if i % modulo == k:
                interesting.append(1)
            else:
                interesting.append(0)
        
        print(interesting)

        prefix = 0

        seen ={0:1}

        count = 0

        for j in range(len(interesting)):

            prefix += interesting[j]

            current_remainder = prefix % modulo

            needed = (current_remainder - k) % modulo

            if needed in seen:

                count += seen[needed]
                        
            seen[current_remainder] = seen.get(current_remainder,0)+1

        
        return count
        
# Status: Hint
# Time Taken: 30m 
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Prefix
# Variant: Prefix + Hash Map + modulo
# Mistakes / Confusion:Na


# 3	-	LC	-	2483	-	Minimum Penalty for a Shop	-	Prefix Sum	-	Pivot / equilibrium

class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        
        penality = customers.count("Y")

        min_penality = penality

        best_hour  = 0

        for i in range(len(customers)):

            if customers[i] == "Y":

                penality -= 1

            else:
                
                penality += 1
            
            if penality < min_penality:

                min_penality = penality

                best_hour  = i + 1
        
        return best_hour 


# Status: Hint
# Time Taken: 30m 
# Time Complexity: O(n)
# Space Complexity: O(n)
# Submitted to LC:Yes
# Result: Accepted
# Pattern: Prefix
# Variant: Pivot / equilibrium
# Mistakes / Confusion:Na
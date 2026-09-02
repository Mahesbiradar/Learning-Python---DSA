
# 1	-	LC	-	862	-	Shortest Subarray with Sum at Least K

from collections import deque
class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = [0]

        dq = deque()

        for i in range(len(nums)):

            prefix.append(nums[i]+prefix[i])

        ans = float('inf')

        for i in range(len(prefix)):

            while dq and prefix[i]-prefix[dq[0]] >= k:

                ans = min(ans,i-dq[0])

                dq.popleft()
            
            while dq and prefix[i] <= prefix[dq[-1]]:

                dq.pop()
            
            dq.append(i)
        
        return -1 if ans == float('inf') else ans



# Status: Hints
# Time Taken: 25 m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: Sliding Window
# Variant: Monotonic Deque
# Mistakes / Confusion:Na

## Tier -2

# 9	-	LC	-	249	-	Group Shifted Strings


class Solution:
    def key_maker(self,string):
        
        key =[]
        
        for i in range(1,len(string)):
            
            key.append((ord(string[i])-ord(string[i-1]))%26)
            
        return tuple(key)
            
    def groupShiftedString(self, arr):
        #code here
        
        common_group = {}
        
        
        for word in arr:
            
            key_of_dict = self.key_maker(word)
            
            if key_of_dict in common_group:
                
                common_group[key_of_dict] += [word]
            else:
                common_group[key_of_dict] = [word]
                
        
        return list(common_group.values())


# Status: independent
# Time Taken: 15 m
# Time Complexity: O(W*L)
# Space Complexity:O(W*L)
# Submitted to LC: Yes
# Result:Accepted
# Pattern: FREQUNECY hAISNG
# Variant: CONONICAL KEY
# Mistakes / Confusion:Na

# 10	-	LC	-	238	-	Product of Array Except Self



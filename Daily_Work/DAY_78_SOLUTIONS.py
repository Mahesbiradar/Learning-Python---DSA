# DAY 78
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


# 1 -- LC -- 34 -- Find First and Last Position of Element in Sorted Array 

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def first(nums,target):

            left = 0 

            right = len(nums)-1

            answer = -1

            while left <= right:

                mid = (right+left)//2

                if nums[mid] < target:

                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1       
                else:
                    answer = mid 
                    right = mid-1

            return answer

        def second(nums,target):

            left = 0

            right = len(nums)-1

            answer = -1

            while left <= right:

                mid = (right+left)//2

                if nums[mid] > target:

                    right = mid - 1

                elif nums[mid] < target:

                    left = mid + 1
                
                else:

                    answer = mid

                    left = mid + 1
            
            return answer
        

        return [first(nums,target),second(nums,target)]

# Status: Independent
# Time Taken: 10M
# Time Complexity:O(logn)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: Binary search
# Variant: Boundary Search / First & Last Occurrence
# Mistakes / Confusion:Na


# 2 --  1539 -- Kth Missing Positive Number -- Binary Search


class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """

        left = 0

        right = len(arr)

        while left < right:

            mid = (right+left)//2

            missing = arr[mid] - (mid+1)

            if missing < k:

                left = mid + 1
            else:

                right = mid
        
        return left + k

# Status: Hint
# Time Taken: 15M
# Time Complexity:O(logn)
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: Binary search
# Variant: Boundary Search / First missing number
# Mistakes / Confusion:Na

# 3 -- LC -- 1011 -- Capacity To Ship Packages Within D Days -- Binary Search


class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        
        def isfeasible(capacity):

            no_of_days = 1

            weight = 0

            for i in range(len(weights)):

                if weight + weights[i] <= capacity:

                    weight += weights[i]
                else:
                    
                    no_of_days += 1

                    weight = weights[i]
            
            return no_of_days <= days

        
        left = max(weights)

        right = sum(weights)

        while left < right:


            mid = (right+left)//2

            if isfeasible(mid):
                right = mid
            else:
                left = mid + 1

        return left

# Status: Hint
# Time Taken: 20M
# Time Complexity:O(n log(sum(weights)))
# Space Complexity:O(1)
# Submitted to LC:Yes
# Result:Accepted
# Pattern: Binary search
# Variant: Binary Search on Answer / Feasibility Boundary
# Mistakes / Confusion:Na





# DAY 79
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
1	-	LC	-	410	-	Split Array Largest Sum	-	Binary Search	-	Applied — non-obvious structure
2	-	LC	-	136	-	Single Number	-	Hash Set	-	Sequence expansion
3	-	LC	-	349	-	Intersection of Two Arrays	-	Hash Set	-	Sequence expansion
4	-	LC	-	202	-	Happy Number	-	Hash Set	-	Sequence expansion
5	-	LC	-	36	-	Valid Sudoku	-	Hash Set	-	Sequence expansion

"""


# 1	-	LC	-	410	-	Split Array Largest Sum	-	Binary Search	-	Applied — non-obvious structure


class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def isfeasible(max_sum):

            current_sum = 0

            subarrays = 1

            for i in range(len(nums)):

                if current_sum + nums[i] <= max_sum:

                    current_sum += nums[i]
                else:

                    subarrays += 1

                    current_sum = nums[i]

            return subarrays <= k
    
        
        left = max(nums)

        right = sum(nums)

        while left < right:

            mid = (right+left)//2

            if isfeasible(mid):

                right = mid
            else:
                left = mid + 1
        
        return left 

# Status: Hint
# Time Taken: 10M
# Time Complexity:O(n log(sum(nums)))
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Binary search 
# Variant: Applied — non-obvious structure
# Mistakes / Confusion:Na



# 2	-	LC	-	136	-	Single Number	-	Hash Set	-	Sequence expansion


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        for i in nums:

            result ^= i
        
        return result

# Status: Hint
# Time Taken: 10M
# Time Complexity:O(n)
# Space Complexity: O(1)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Hash/Bit Manipulation
# Variant: XOR Cancellation
# Mistakes / Confusion:Na


# 3	-	LC	-	349	-	Intersection of Two Arrays	-	Hash Set	-	Sequence expansion


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        set_nums2 = set(nums2)

        seen = set()

        for i in nums1:

            if i in set_nums2:

                seen.add(i)
        
        result = list(seen)

        return result

# Status: Indepndent
# Time Taken: 10M
# Time Complexity:O(n)
# Space Complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Hash Set
# Variant: Set Membership / Intersection
# Mistakes / Confusion:Na

# 4	-	LC	-	202	-	Happy Number	-	Hash Set	-	Sequence expansion

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_next(number):
            n = number
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10

            return total
        
        num = n
        seen = set()

        while num != 1:

            if num in seen:
                return False
           
            seen.add(num)
            num = get_next(num)
        
        return True


# Status: Hint
# Time Taken: 15M
# Time Complexity:O(n)
# Space Complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Hash Set
# Variant: Sequence expansion
# Mistakes / Confusion:Na


# 5	-	LC	-	36	-	Valid Sudoku	-	Hash Set	-	Sequence expansion

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        """
        :type board: List[List[str]]
        :rtype: bool
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for raw in range(9):

            for col in range(9):
                
                value = board[raw][col]

                if value == ".":
                    continue

                box = (raw//3)*3 + (col//3)

                if value in rows[raw] or value in cols[col] or value in boxes[box]:
                    return False
                

                rows[raw].add(value)
                cols[col].add(value)
                boxes[box].add(value)
        
        return True

# Status: Hint
# Time Taken: 30M
# Time Complexity:O(n)
# Space Complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: Hash Set
# Variant: Sequence Expansion / Multi-Constraint State Tracking
# Mistakes / Confusion:Na


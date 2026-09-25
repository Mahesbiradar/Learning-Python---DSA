# DAY 70

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


# 1 - LC - 1636 - Find Smallest Integer Missing from Array


class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        seen = {}

        for i in nums:

            seen[i] = seen.get(i,0)+1
        
        sorted_seen = sorted(seen.items(),key=lambda x:(x[1],-x[0]))

        result = []

        for key,value in sorted_seen:

            for j in range(value):
                result.append(key)
        
        return result


# Status: Independent
# Time Taken: 15 m
# Time Complexity: O(n log n)
# Space Complexity:O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern:Frequnecy sorting
# Variant:Sort by count
# Mistakes / Confusion:Na


# 2 - LC - 1099 - Two Sum Less Than K


def two_sum_less_than_k(nums: list[int], k: int) -> int:

    nums.sort()

    left = 0
    right = len(nums)-1

    max_sum_lessthan_k = float('-inf')

    while left < right:

        two_sum = nums[left] + nums[right]

        if two_sum < k:

            max_sum_lessthan_k = max(max_sum_lessthan_k,two_sum)

            left += 1
        else:
            right -= 1

    return -1 if max_sum_lessthan_k == float('-inf') else max_sum_lessthan_k


print(two_sum_less_than_k([34, 23, 1, 24, 75, 33, 54, 8],60))
        
print(two_sum_less_than_k([], 50))
print(two_sum_less_than_k([10], 50))

print(two_sum_less_than_k([40, 50, 60], 30))
print(two_sum_less_than_k([20, 30], 50))

print(two_sum_less_than_k([10, 10, 20, 30], 25))
print(two_sum_less_than_k([40, 40, 50], 60))

print(two_sum_less_than_k([5, 10, 15], 100))
print(two_sum_less_than_k([15, 25, 35], 5))


print(two_sum_less_than_k([1, 5, 10, 20, 25], 30))
print(two_sum_less_than_k([25, 20, 10, 5, 1], 30))

print(two_sum_less_than_k([10, 30, 20, 20, 15, 25], 41))


# Status: Independent
# Time Taken: 10 m
# Time Complexity: O(n log n)
# Space Complexity:O(1)
# Submitted to LC: No
# Result: External validation: Passed your test suite
# Pattern:Two pointers
# Variant:sort + moving pointers inward
# Mistakes / Confusion:Na


# 3 - LC - 325 - Maximum Size Subarray Sum Equals k


def maximum_size_subarray_sum_equals_k(nums: list[int], k: int) -> int:


    prefix = 0

    seen = {0:-1}

    max_subarray = 0

    for i in range(len(nums)):

        prefix += nums[i]

        needed = prefix - k 

        if needed in seen:

            max_subarray = max(max_subarray,i-seen[needed])

        if prefix not in seen:

            seen[prefix] = i

    return max_subarray


print("LC Problems No 325")

# print(maximum_size_subarray_sum_equals_k([1, -1, 5, -2, 3],3))


# Test Case 1: Standard case with mixed positive/negative numbers (Example from problem)
print(maximum_size_subarray_sum_equals_k([1, -1, 5, -2, 3], 3))

# Test Case 2: Standard case with multiple valid subarrays (returns the longest one)
print(maximum_size_subarray_sum_equals_k([-2, -1, 2, 1], 1))

# Test Case 3: Entire array sums up to k
print(maximum_size_subarray_sum_equals_k([1, 2, 3, 4, 5], 15))

# Test Case 4: No subarray sums up to k (should return 0)
print(maximum_size_subarray_sum_equals_k([1, 2, 3], 8))

# Test Case 5: Single element array where the element equals k
print(maximum_size_subarray_sum_equals_k([5], 5))

# Test Case 6: Single element array where the element does not equal k
print(maximum_size_subarray_sum_equals_k([5], 3))

# Test Case 7: Array containing all zeros with k = 0
print(maximum_size_subarray_sum_equals_k([0, 0, 0, 0], 0))

# Test Case 8: Large target k with negative numbers cancelling out
print(maximum_size_subarray_sum_equals_k([100, -100, 5, 0, 0, 0], 5))

# Test Case 9: Empty array
print(maximum_size_subarray_sum_equals_k([], 5))

# Test Case 10: All negative numbers
print(maximum_size_subarray_sum_equals_k([-1, -2, -3, -4], -5))


# Status: Independent
# Time Taken: 15 m
# Time Complexity: O(n)
# Space Complexity:O(n)
# Submitted to LC: No
# Result: External validation: Passed your test suite
# Pattern:Prefix sum
# Variant:Hash map
# Mistakes / Confusion:Na


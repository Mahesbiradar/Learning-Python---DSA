# DAY 83
# Status:
# Time Taken:
# Time Complexity:
# Space Complexity:
# Submitted to LC:
# Result:
# Pattern:
# Variant:
# Mistakes / Confusion:



string = "IceCreAm"


# string[0], string[-2] = string[-2],string[0]


# print(string)

result = list(string)

print(result)



nums = [34, 23, 1, 24, 75, 33, 54, 8]
k = 60


nums.sort()


left = 0

right = len(nums)-1

max_sum = float('-inf')


print(nums)

while left < right:

    two_sum = nums[left] + nums[right]

    if two_sum >= k:

        right -= 1
    else:

        max_sum = max(max_sum,two_sum)
        print(max_sum,nums[left],nums[right])

        left += 1


print(max_sum)



num = 18

digit = num % 10

carry = num // 10

print(digit)

print(carry)
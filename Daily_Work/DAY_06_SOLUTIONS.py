"""
### 2. Top K Frequent Elements

Topic: Hashing / Frequency  
Pattern: Count frequencies, then select top `k`  
Difficulty: Medium  
LeetCode: Required

Problem:

Given an integer list `nums` and an integer `k`, return the `k` most frequent elements. The answer can be returned in any order.

Example:

```python
nums = [1, 1, 1, 2, 2, 3]
k = 2
```

Expected output:

```python
[1, 2]
```

Why:

```text
1 appears 3 times.
2 appears 2 times.
3 appears 1 time.
The top 2 most frequent values are 1 and 2.
```

Requirements:
- Build a frequency dictionary.
- First solve using sorting by frequency.
- If time remains, read bucket-sort idea only after your own version works.

Test cases:

```python
nums = [1, 1, 1, 2, 2, 3], k = 2 -> [1, 2]
nums = [1], k = 1 -> [1]
nums = [4, 4, 4, 6, 6, 7], k = 1 -> [4]
nums = [-1, -1, 2, 2, 2, 3], k = 2 -> [2, -1]
nums = [5, 3, 5, 3, 2], k = 2 -> [5, 3] in any order
```

Edge cases:
- `k` can be `1`.
- Negative numbers are allowed.
- Multiple answers may be valid when frequencies tie.
- Return elements, not frequencies.
- Sorting dictionary items by count is acceptable for the first solution.


"""
#Using the Sorting Method.

def top_k_elements(nums,k):

    if len(nums)<2:
        return nums
    
    freq={}

    for i in nums:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1

    sorted_freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)

    result=[]

    for key, value in sorted_freq:

        result.append(key)

        if len(result)==k:
            return result
        
    return result

print(top_k_elements([1, 1, 1, 2, 2, 3],2))
print(top_k_elements([1],1))
print(top_k_elements([4, 4, 4, 6, 6, 7],1))
print(top_k_elements([-1, -1, 2, 2, 2, 3],2))
print(top_k_elements([5, 3, 5, 3, 2],2))

    
# Status:- [ ] Hint used for sorting sytax in dictionary


# Time complexity:O(n log n)

# space_Comp: O(n)

# Pattern trigger:Frequncy Check and sorting of dict

# LeetCode submission status:Not submitted

#Revisite: Requered


#Using the bucket Sorting

def top_k_elements(nums, k):

    # Step 1: Build frequency dictionary
    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Step 2: Create buckets
    # Index = frequency
    bucket = []

    for i in range(len(nums) + 1):
        bucket.append([])

    # Step 3: Put numbers into frequency buckets
    for number, count in freq.items():
        bucket[count].append(number)

    # Debug print (optional)
    # print("Buckets:", bucket)

    # Step 4: Traverse buckets from high frequency to low
    result = []

    for freq_index in range(len(bucket) - 1, -1, -1):

        # Traverse numbers inside current bucket
        for number in bucket[freq_index]:

            result.append(number)

            # Stop once k elements collected
            if len(result) == k:
                return result

    return result


print(top_k_elements([1, 1, 1, 2, 2, 3], 2))
print(top_k_elements([1], 1))
print(top_k_elements([4, 4, 4, 6, 6, 7], 1))
print(top_k_elements([-1, -1, 2, 2, 2, 3], 2))
print(top_k_elements([5, 3, 5, 3, 2], 2))

# Status:- olution viewed


# Time complexity:O(n)

# space_Comp: O(n)

# Pattern trigger:Frequncy Check and sorting of dict

# LeetCode submission status:Not submitted

#Revisite: Requered

"""
### 1. Group Anagrams

Topic: Hashing / Grouping  
Pattern: Sorted string key or character-count key  
Difficulty: Medium  
LeetCode: Required

Problem:

Given a list of strings `strs`, group words that are anagrams of each other. Return the groups in any order.

Two words are anagrams if they contain the same characters with the same frequencies, but possibly in a different order.

Example:

```python
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

Expected output:

```python
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

Why:

```text
"eat", "tea", and "ate" all become "aet" when sorted.
"tan" and "nat" both become "ant" when sorted.
"bat" becomes "abt" and has no matching word.
```

Requirements:
- Use a dictionary where each key maps to a list of words.
- First use sorted-string key.
- Write time complexity carefully.
- Submit on LeetCode after local examples pass.

Test cases:

```python
["eat", "tea", "tan", "ate", "nat", "bat"] -> groups of ["eat","tea","ate"], ["tan","nat"], ["bat"]
[""] -> [[""]]
["a"] -> [["a"]]
["abc", "bca", "cab", "xyz", "zyx"] -> groups of ["abc","bca","cab"], ["xyz","zyx"]
["bob", "obb", "boo"] -> groups of ["bob","obb"], ["boo"]
```

Edge cases:
- Empty string is a valid word.
- A single word returns one group.
- Output group order does not matter.
- Word order inside each group usually does not matter for LeetCode.
- Sorting each word costs extra time.

Time target: 40-50 minutes.


"""

def group_anagrams(list_w):

    seen={}

    for i in list_w:
        sorted_i=sorted(i)
        string="".join(sorted_i)

        if string in seen:
            seen[string].append(i)
        else:
            seen[string]=[i]
    return seen.values()


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams([""]))
print(group_anagrams(["a"]))
print(group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]))
print(group_anagrams(["bob", "obb", "boo"]))

    
# Status:- olution viewed


# Time complexity:O(n* k log k)

# space_Comp: O(n)

# Pattern trigger:Sorting and grouping of anagrams

# LeetCode submission status:Not submitted

#Revisite: Requered


"""
### 3. Majority Element

Topic: Arrays / Frequency or Voting  
Pattern: Frequency count first, Boyer-Moore optional  
Difficulty: Easy  
LeetCode: Recommended

Problem:

Given a non-empty integer list `nums`, return the element that appears more than `n // 2` times. You may assume the majority element always exists.

Example:

```python
nums = [3, 2, 3]
```

Expected output:

```python
3
```

Why:

```text
n = 3
n // 2 = 1
3 appears 2 times, and 2 > 1.
```

Requirements:
- Solve with dictionary count.
- Explain why majority means count `> n // 2`.
- Try Boyer-Moore only if time/energy remains.

Test cases:

```python
[3, 2, 3] -> 3
[2, 2, 1, 1, 1, 2, 2] -> 2
[1] -> 1
[-1, -1, -1, 2, 3] -> -1
[6, 6, 6, 6, 7, 7, 7] -> 6
```

Edge cases:
- One-element list.
- Negative numbers.
- Majority count must be strictly greater than `n // 2`.
- The problem guarantees a majority exists, so no special "not found" return is needed on LeetCode.

"""

#Using the frequncy method.

def major_element(nums):

    seen={}

    for i in nums:
        if i in seen:
            seen[i]+=1
        else:
            seen[i]=1
    
    major_element=0
    frequncy=0

    for key,value in seen.items():
        if value>frequncy:
            frequncy=value
            major_element=key
        
    
    return major_element

print(major_element([-1, -1, -1, 2, 3]))
print(major_element([3, 2, 3]))
print(major_element([2, 2, 1, 1, 1, 2, 2]))
print(major_element([6, 6, 6, 6, 7, 7, 7]))
print(major_element([1]))

# Status:- Solved independently

# Time complexity:O(n)

# space_Comp: O(n)

# Pattern trigger:Fequency 

# LeetCode submission status:Not submitted

#Revisite: Requered and boyer more method also


"""
### Revision 1. Find Pivot Index

Why revisit: Day 05 optimal version worked, but compare-before-add placement was confusing.  
Pattern: Prefix sum with derived right sum  
Difficulty: Easy

Rules:
- Do not use old code.
- Dry run first.
- At each index: compute right sum, compare, then add current value to left sum.

Problem:

Given a list `nums`, return the leftmost index where the sum of all values to the left equals the sum of all values to the right. If no such index exists, return `-1`.

Example:

```python
nums = [1, 7, 3, 6, 5, 6]
```

Expected output:

```python
3
```

Why:

```text
Left of index 3: 1 + 7 + 3 = 11
Right of index 3: 5 + 6 = 11
```

Test cases:

```python
[1, 7, 3, 6, 5, 6] -> 3
[1, 2, 3] -> -1
[2, 1, -1] -> 0
[0, 0, 0] -> 0
[-1, -1, 0, 1, 1, 0] -> 5

"""

#Using total sum

def pivot_index(nums):

    left=0
    total_sum=sum(nums)

    for i in range(len(nums)):

        right=total_sum-nums[i]-left

        if right==left:
            return i
        left+=nums[i]
    return -1

print("Pivot Index o/p start Here")
print(pivot_index([1, 7, 3, 6, 5, 6]))
print(pivot_index([1, 2, 3]))
print(pivot_index([2, 1, -1]))
print(pivot_index([-1, -1, 0, 1, 1, 0]))

# Status:- Solved independently

# Time complexity:O(n)

# space_Comp: O(1)

# Pattern trigger:prefix and suffix 

# LeetCode submission status:Not submitted

#Revisite:


"""
### Revision 2. Valid Palindrome

Why revisit: Day 05 still used hints for optimized skip loops.  
Pattern: Two pointers with skip loops  
Difficulty: Easy  
LeetCode: Required if clean locally

Rules:
- No cleaned-string extra-list version first.
- Skip invalid characters before comparing.
- Compare lowercase characters.

Problem:

Given a string `s`, return `True` if it is a palindrome after converting uppercase letters to lowercase and removing all non-alphanumeric characters. Otherwise, return `False`.

Example:

```python
s = "A man, a plan, a canal: Panama"
```

Expected output:

```python
True
```

Why:

```text
After ignoring spaces, punctuation, and capitalization:
"amanaplanacanalpanama"

This reads the same forward and backward.
```

Test cases:

```python
"A man, a plan, a canal: Panama" -> True
"race a car" -> False
" " -> True
"0P" -> False
"No lemon, no melon" -> True
".,," -> True
```

"""
def valid_palindrome(s):

    left=0
    right=len(s)-1

    while left<right:

        #ignoring non alpha chars in left\

        while left<right and not s[left].isalnum():
            left+=1
        
        while left<right and not s[right].isalnum():
            right-=1
        
        if s[left].lower()!=s[right].lower():
            return False
        
        left+=1
        right-=1
    return True

print(valid_palindrome("A man, a plan, a canal: Panama"))
print(valid_palindrome("race a car"))
print(valid_palindrome("No lemon, no melon"))
print(valid_palindrome(".,,"))
print(valid_palindrome("0P"))
print(valid_palindrome(" "))
        

# Status:- Solved independently

# Time complexity:O(n)

# space_Comp: O(1)

# Pattern trigger:two pointers

# LeetCode submission status:Not submitted

#Revisite:


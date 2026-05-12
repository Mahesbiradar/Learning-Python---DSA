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

    












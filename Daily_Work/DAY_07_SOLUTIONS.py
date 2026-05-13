"""
## Today's New Problems

### 1. Valid Anagram - Clean Hash Version

Topic: Hashing / Strings  
Pattern: Character frequency comparison  
Difficulty: Easy  
LeetCode: Required

Problem:

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

Requirements:
- Do not use `char in t` inside a loop.
- Use dictionary counts or count/decrement.
- Return early if lengths differ.
- Write exact time and space complexity.

Test cases:

```python
s = "anagram", t = "nagaram" -> True
s = "rat", t = "car" -> False
s = "aa", t = "a" -> False
s = "", t = "" -> True
s = "aacc", t = "ccac" -> False
```

Time target: 25-30 minutes.

"""
#Using the Hash Table

def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        
        s_freq={}
        for i in s:
            if i in s_freq:
                s_freq[i]+=1
            else:
                s_freq[i]=1
        t_freq={}
        for j in t:
            if j in t_freq:
                t_freq[j]+=1
            else:
                t_freq[j]=1
        
        for k in s_freq:
            if k not in t_freq:
                return False
            elif s_freq[k]!=t_freq[k]:
                return False
        return True 

print(isAnagram("anagram","nagaram"))
print(isAnagram("rat","car"))
print(isAnagram("aa","a"))
print(isAnagram("",""))
print(isAnagram("aacc","ccac"))

# Status:Independent solve

# Brute-force idea: we can take one string and run a outer loop and then in inner loops we can check theck the frequency of each elements of outer loop and the compare.

# Optimized idea:Using dict frequncy of each element and then we can do membership chekc and frequency of occurance

# Time complexity: O(n)

# Space complexity:O(n)

# Mistakes/confusions:NA

# Pattern trigger:Hashing Table comparison

# LeetCode submission status: Accepted

"""
### 3. Sort Characters By Frequency

Topic: Hashing / Frequency Sorting  
Pattern: Count characters, sort by count  
Difficulty: Medium  
LeetCode: Recommended

Problem:

Given a string `s`, return a string with characters sorted by decreasing frequency.

Example:

```python
s = "tree"
```

Expected output:

```python
"eert" or "eetr"
```

Requirements:
- Build a character frequency dictionary.
- Sort dictionary items by frequency descending.
- Build the answer by repeating each character `count` times.
- Do sorting version only; bucket version is optional later.

Test cases:

```python
"tree" -> "eert" or "eetr"
"cccaaa" -> "cccaaa" or "aaaccc"
"Aabb" -> "bbAa" or "bbaA"
"a" -> "a"
"" -> ""
```

Time target: 35-45 minutes.

"""
#Using the hasing/sorting by frequnecy.

def sort_chars_by_frequency(s):
    
    #Step1:Count the Frequency of each Char using Dict.
    seen={}
    for i in s:
        if i in seen:
            seen[i]+=1
        else:
            seen[i]=1
    #Step2:Sort the elements by values in decrising order
    sorted_seen=sorted(seen.items(),key=lambda x:x[1],reverse=True)

    #convert the sorted element back to string with frequnecy.

    result_str=""

    for key,value in sorted_seen:
        result_str+=(key*value)
    
    return result_str
print(sort_chars_by_frequency("tree"))
print(sort_chars_by_frequency("cccaaa"))
print(sort_chars_by_frequency("Aabb"))
print(sort_chars_by_frequency("a"))
print(sort_chars_by_frequency(""))

# Status:Independent solve

# Time complexity: O(n log n)

# Space complexity:O(n)

# Mistakes/confusions:NA

# Pattern trigger:count Frequncy and sort by Values.

# LeetCode submission status: Accepted.


#Solution using the Bucket sorting:

def sort_chars_by_frequency(s):
    
    #Step1:Count the Frequency of each Char using Dict.
    seen={}
    for i in s:
        if i in seen:
            seen[i]+=1
        else:
            seen[i]=1
    #Step2: Creating Bucket.
    bucket=[]
    for i in range(len(s)+1):
        bucket.append([])

    #step3:appending the chars in bucket based on its Frequncy.
    for key,value in seen.items():
        bucket[value].append(key)
    
    #step4:traversal in bucket to append the chars back to string with its frequncy.
    result_str=""
    for char_freq in range(len(bucket)-1,-1,-1):

        for char in bucket[char_freq]:
            result_str+=(char*char_freq)

    return result_str


print(sort_chars_by_frequency("tree"))
print(sort_chars_by_frequency("cccaaa"))
print(sort_chars_by_frequency("Aabb"))
print(sort_chars_by_frequency("a"))
print(sort_chars_by_frequency(""))

# Status:Independent solve

# Time complexity: O(n)

# Space complexity:O(n)

# Mistakes/confusions:NA

# Pattern trigger:count Frequncy and sort by Values.

# LeetCode submission status: Accepted.

"""
### 2. Intersection of Two Arrays II

Topic: Hashing / Frequency  
Pattern: Count one list, consume from the other  
Difficulty: Easy  
LeetCode: Recommended

Problem:

Given two integer lists `nums1` and `nums2`, return their intersection including duplicate occurrences.

Example:

```python
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
```

Expected output:

```python
[2, 2]
```

Requirements:
- Count frequencies from one list.
- Traverse the other list.
- Append only when remaining count is positive.
- Decrease the count after using a value.

Test cases:

```python
[1, 2, 2, 1], [2, 2] -> [2, 2]
[4, 9, 5], [9, 4, 9, 8, 4] -> [4, 9] in any order
[1, 1, 1], [1, 1] -> [1, 1]
[], [1, 2] -> []
[3], [3] -> [3]
```

"""
def intersection(nums1,nums2):

    freq_nums1={}

    for i in nums1:
        if i in freq_nums1:
            freq_nums1[i]+=1
        else:
            freq_nums1[i]=1
    result=[]
    for j in nums2:
        if j in freq_nums1 and freq_nums1[j]>0:
            result.append(j)
            freq_nums1[j]-=1
    return result

print(intersection([1, 2, 2, 1],[2, 2]))
print(intersection([4, 9, 5],[9, 4, 9, 8, 4]))
print(intersection([1, 1, 1],[1, 1]))
print(intersection([],[1, 2]))
print(intersection([3],[3]))

# Status:hints used

# Time complexity: O(n)

# Space complexity:O(n)

# Mistakes/confusions:Here i have taken the Hint for Second pass where element memebership check occurs in dict and the appending element if value is postive and decrementicting the Count.

# Pattern trigger:count Frequncy in one list and consume from another List

# LeetCode submission status: Accepted.

"""
Revision Problems

Revision 1. Group Anagrams

Why revisit: Day 06 implementation was marked solution viewed.  
Pattern: Sorted string key to dictionary list  
Difficulty: Medium  
LeetCode: Required if clean locally

Rules:
- Do not read Day 06 code first.
- Use `key = "".join(sorted(word))`.
- Append each word to the correct dictionary list.
- Return `list(groups.values())`, not raw `dict_values`.

Test cases:

```python
["eat", "tea", "tan", "ate", "nat", "bat"] -> grouped anagrams
[""] -> [[""]]
["a"] -> [["a"]]
["abc", "bca", "cab", "xyz", "zyx"] -> two groups
```

Time target: 30-35 minutes."""

#Solution using the frequncy hasing/Sorting Method submitted on leetcode.


def groupAnagrams(strs):
       
    seen={}
    for i in strs:

        sorted_str=sorted(i)
        key="".join(sorted_str)

        if key in seen:
            seen[key]+=[i]
        else:
            seen[key]=[i]
            
    return seen.values()

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams([]))
print(groupAnagrams(["a"]))
print(groupAnagrams(["abc", "bca", "cab", "xyz", "zyx"] ))

# Status:Independent solve

# Time complexity: O(n*k log k)

# Space complexity:O(n)

# Mistakes/confusions:

# Pattern trigger:Frequncy mapping/sorting

# LeetCode submission status: Accepted.

"""
### Revision 2. Find Pivot Index

Why revisit: Day 06 returned `0` instead of `-1` when no pivot exists.  
Pattern: Prefix sum with check-before-update  
Difficulty: Easy

Rules:
- Compute `right_sum`.
- Compare `left_sum == right_sum`.
- Then add current number to `left_sum`.
- Return `-1` after the loop.

Test cases:

```python
[1, 7, 3, 6, 5, 6] -> 3
[1, 2, 3] -> -1
[2, 1, -1] -> 0
[0, 0, 0] -> 0
[-1, -1, 0, 1, 1, 0] -> 5

"""
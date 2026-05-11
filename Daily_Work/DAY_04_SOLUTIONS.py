## Prerequisites Revision

# Time target: 30 minutes total.

# - [ ] Re-write a frequency counter using `dict.get`.
# - [ ] Explain why dictionary lookup is usually O(1).
# - [ ] Explain why a frequency dictionary is O(n) space.
# - [ ] Write the Two Sum template from memory: check complement first, then store current value/index.
# - [ ] Write `sorted(s)` complexity: O(n log n) time, O(n) space in Python.
# - [ ] Dry run two pointers on a palindrome string.


# - [ ] Re-write a frequency counter using `dict.get`.

def freq_counter(nums,element):

    freq_nums={}

    for i in nums:
        if i in freq_nums:
            freq_nums[i]+=1
        else:
            freq_nums[i]=1
    return freq_nums.get(element)

print(freq_counter([1,2,4,1,3,2,4],4))

# - [ ] Explain why dictionary lookup is usually O(1).

""" 
The Dict lookup use the Hasing tables allowing direct access to values using computed hash indexes instead of linear searching
"""
# - [ ] Explain why a frequency dictionary is O(n) space.
""" 
The dictionary may need to store an entry for every unique element therefore the it required O(n) Space.
"""
# [ ] Write the Two Sum template from memory: check complement first, then store current value/index.

"""
so in inputs We get list and the target

There for what we do is 

will Check what Number is needed to achive the Target Then we lookup the Needed 
number in dictionary if it found we get ans or will Store the index of Current Element.

def two_Sum(nums,target):
    seen={}
    for i in range(len(nums)):
        needed=target-nums[i]
        if needed in seen:
            return [nums[i],seen[needed]]
        seen[nums[i]]=i

"""

# - [ ] Write `sorted(s)` complexity: O(n log n) time, O(n) space in Python.
"""
pythons sorted(s) uses the timsort algorith whic is based on merge sort and insertion sort.
sorting required comparing element multiple times.the number of operation grows approximately O(n log n)
sorted(s) doens't sort in place it creates new list extra temporary memory during the merging therefor the space comp is O(n)
"""
# - [ ] Dry run two pointers on a palindrome string.

"""
Nums=[1,3,3,1]

here will take two Pointers one Travers from left and one more from Right

left=0
right=len(nums)-1

iteration-1
nums[left]=1,nums[right]=1, nums[left]==nums[right]? True and will Increment left and Decrement right to move Toward center.
iteration-2
nums[left]=3,nums[right]=3, nums[left]==nums[right]? True Here loop end and the given list has palindrom.

"""

"""
## Fundamentals Revision

Task: Write these from memory before starting LeetCode-style problems.

```python
def count_frequency(items):
    pass

def is_plain_palindrome(s):
    pass
```
Checklist:
- [ ] Frequency counter works for list, string, and empty input.
- [ ] Palindrome works for odd length, even length, and empty string.
- [ ] Time and space complexity written for both.

"""

def count_frequency(items):
    seen={}
    for i in items:
        if i in seen:
            seen[i]+=1
        else:
            seen[i]=1
    return seen

print(count_frequency([1,4,5,2,1,2,3,4,])) 
print(count_frequency("apple")) 
print(count_frequency([]))
print(count_frequency(""))

#time comp: O(n)
#Space:O(n)

def is_plain_palindrome(s):
    
    left=0
    right=len(s)-1

    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True

print(is_plain_palindrome("madam"))
print(is_plain_palindrome("racecar"))
print(is_plain_palindrome("hello"))
print(is_plain_palindrome(""))

#time comp: O(n)
#Space:O(1)

"""
### 1. Valid Palindrome

Topic: Strings / Two Pointers  
Pattern: Clean input + left/right pointer  
Difficulty: Easy  
LeetCode: Required

Problem:

Given a string `s`, return `True` if it is a palindrome after converting uppercase letters into lowercase letters and removing all non-alphanumeric characters. Otherwise, return `False`.

A palindrome reads the same forward and backward.

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
After ignoring spaces, punctuation, and case:
"amanaplanacanalpanama"
This reads the same forward and backward.
```

Example:

```python
s = "race a car"
```

Expected output:

```python
False
```

Why:

```text
After cleaning:
"raceacar"
This does not read the same forward and backward.
```

Input details:
- Input is a string `s`.
- `s` can contain letters, digits, spaces, punctuation, and symbols.
- Uppercase and lowercase versions of the same letter should be treated as equal.

Output details:
- Return `True` if the cleaned string is a palindrome.
- Return `False` otherwise.

Requirements:
- Ignore non-alphanumeric characters.
- Compare lowercase characters.
- Use two pointers.
- Do not build a fully cleaned string for the optimized version.
- Move `left` forward while `s[left]` is not alphanumeric.
- Move `right` backward while `s[right]` is not alphanumeric.

Test cases:

```python
"A man, a plan, a canal: Panama" -> True
"race a car" -> False
" " -> True
"0P" -> False
"Madam" -> True
"No lemon, no melon" -> True
"ab@a" -> True
"abc" -> False
```


"""

#Understanding: Here i while i have intialize two Pointer one Travers from left and one more from right.

#While loopong over element i have igonre non alphanumeric chars and compare the strings.

#Brute force idea: i can craete clean sting by removing all the nonalpha chars and then run a loop to Check teh palindrome.

def is_palindrome(s):
   
    sorted_s="".join(char for char in s if char.isalnum())

    left=0
    right=len(sorted_s)-1
    while left<right:
        if sorted_s[left].lower()!=sorted_s[right].lower():
            return False
        left+=1
        right-=1
    return True

print(is_palindrome("A man, a plan, a canal: Panama")) #true
print(is_palindrome("race a car"))  #False
print(is_palindrome(" "))#true
print(is_palindrome("Madam")) #true
print(is_palindrome("No lemon, no melon")) #true
print(is_palindrome("ab@a"))  #true
print(is_palindrome("abc"))  #False

# Status: [ ] Independent solve but hind used to for syntax to remove nonalpha chars.

# Time complexity: O(n)

# Space complexity: O(n)

# Mistakes/confusions:Taken hint online for conversting clean string.

# Pattern trigger:Two pointers/ Elements Comparison.

# LeetCode submission status: Not submitted

#optimal solution:instead of creating a new string ill ignore the nonalpha chars.


def is_palindrome(s):
    left=0
    right=len(s)-1

    while left<right:

        while left<right and not s[left].isalnum():
            left+=1
        while left<right and not s[right].isalnum():
            right-=1
        if s[left].lower()!=s[right].lower():
            return False
        left+=1
        right-=1
        
    return True
        

print(is_palindrome("A man, a plan, a canal: Panama")) #true
print(is_palindrome("race a car"))  #False
print(is_palindrome(" "))#true
print(is_palindrome("Madam")) #true
print(is_palindrome("No lemon, no melon")) #true
print(is_palindrome("ab@a"))  #true
print(is_palindrome("abc"))  #False  

# Status: [ ] solved with hinds during the systax check i seen the solution and geneounly i thought with fileters only i can increament pointers but later realized i shoud use the inner loop.

# Time complexity: O(n)

# Space complexity: O(1)

# Mistakes/confusions:Taken hint online for inner loop logic intially thought diffrent.

# Pattern trigger:Two pointers/ Elements Comparison.

# LeetCode submission status: Not submitted


"""
### 2. Reverse String

Topic: Strings / Two Pointers  
Pattern: In-place swap  
Difficulty: Easy  
LeetCode: Recommended

Problem:

Given a list of characters `s`, reverse the list in-place.

You must modify the input list directly and use O(1) extra memory.

Example:

```python
s = ["h", "e", "l", "l", "o"]
```

Expected output:

```python
["o", "l", "l", "e", "h"]
```

Why:

```text
The first and last characters are swapped, then the two pointers move inward.
```

Example:

```python
s = ["H", "a", "n", "n", "a", "h"]
```

Expected output:

```python
["h", "a", "n", "n", "a", "H"]
```

Input details:
- Input is a list of single-character strings.
- The function usually returns nothing on LeetCode.
- The list itself must be changed.

Output details:
- Do not return a new list.
- After the function runs, `s` should be reversed.

Requirements:
- Reverse a list of characters in-place.
- Use left and right pointers.
- Swap `s[left]` and `s[right]`.
- Do not use slicing for the optimized version.
- Do not create another list.

Test cases:

```python
["h", "e", "l", "l", "o"] -> ["o", "l", "l", "e", "h"]
["H", "a", "n", "n", "a", "h"] -> ["h", "a", "n", "n", "a", "H"]
["a"] -> ["a"]
[] -> []
["a", "b"] -> ["b", "a"]
["1", "2", "3"] -> ["3", "2", "1"]
```

"""

def revers_string(s):

    left=0
    right=len(s)-1

    while left<right:

        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return s

print(revers_string(["h", "e", "l", "l", "o"]))
print(revers_string(["H", "a", "n", "n", "a", "h"]))
print(revers_string(["a"]))
print(revers_string([]))
print(revers_string(["a", "b"]))
print(revers_string(["1", "2", "3"]))


# Status:Independent solved

# Time complexity: O(n)

# Space complexity: O(1)

# Mistakes/confusions: NA

# Pattern trigger: In place Swap

# LeetCode submission status:Not submitted


"""
### 3. Is Subsequence

Topic: Strings / Two Pointers  
Pattern: Scan target while matching source pointer  
Difficulty: Easy  
LeetCode: Recommended

Problem:

Given two strings `s` and `t`, return `True` if `s` is a subsequence of `t`, and `False` otherwise.

A subsequence is formed by deleting zero or more characters from another string without changing the order of the remaining characters.

Example:

```python
s = "abc"
t = "ahbgdc"
```

Expected output:

```python
True
```

Why:

```text
"a", "b", and "c" appear in `t` in the same order.
```

Example:

```python
s = "axc"
t = "ahbgdc"
```

Expected output:

```python
False
```

Why:

```text
"a" and "c" appear, but "x" does not appear between them in order.
```

Input details:
- Input `s` is the string you are trying to match.
- Input `t` is the string you are scanning.
- Both strings may be empty.

Output details:
- Return `True` if all characters of `s` are found in `t` in order.
- Return `False` otherwise.

Requirements:
- Use two pointers.
- One pointer tracks the current character in `s`.
- One pointer scans through `t`.
- Move the `s` pointer only when there is a match.
- Handle empty `s`.

Test cases:

```python
s = "abc", t = "ahbgdc" -> True
s = "axc", t = "ahbgdc" -> False
s = "", t = "ahbgdc" -> True
s = "abc", t = "" -> False
s = "ace", t = "abcde" -> True
s = "aec", t = "abcde" -> False
s = "aaaaaa", t = "bbaaaa" -> False


"""
#solution:

def is_subsequence(s,t):

    if not s:
        return True
    if not t:
        return False

    pointer_s=0

    for i in range(len(t)):
        if s[pointer_s]==t[i]:
            pointer_s+=1
        if pointer_s==len(s):
            return True
    return False
    
        

print(is_subsequence("abc","ahbgdc"))
print(is_subsequence("axc","ahbgdc"))
print(is_subsequence("aec","abcde"))
print(is_subsequence("","ahbgdc"))
print(is_subsequence("abs",""))
print(is_subsequence("aaaaaa","abcde"))
print(is_subsequence("ace","abcde"))
print(is_subsequence("aaaaaa","bbaaaa"))
print(is_subsequence("abc","abcaaa"))


"""Status:used hints lot of time intailly i was using nested loop which is not Require\
then i used two pointer explicitly whice is also not required bcz in loop i have one Pointer.
Then im Comparing the len(s) with pointer before the checing orders Sequence. then i shifter this count outside the loop.LookupError
later Realized it shoud be in loop"""

# Time complexity: O(n)

# Space complexity: O(1)

# Mistakes/confusions: NA explianed in status 

# Pattern trigger: Two Pointers/Matched order Traversal.

# LeetCode submission status:Not submitted

# Revisit requirement: Yes

"""
## Revision Problems

### Revision 1. Two Sum

Why revisit: Day 03 optimized solution required solution help for `seen[nums[i]] = i`.  
Pattern: Dictionary complement lookup  
Difficulty: Easy  
LeetCode: Required

Problem:

Given a list of integers `nums` and an integer `target`, return the indexes of the two numbers such that they add up to `target`.

You may assume that each input has exactly one valid answer, and you may not use the same element twice.

Example:

```python
nums = [2, 7, 11, 15]
target = 9
```

Expected output:

```python
[0, 1]
```

Why:

```text
nums[0] + nums[1] = 2 + 7 = 9
```

Input details:
- `nums` is a list of integers.
- `target` is an integer.
- Values may be positive, negative, or zero.
- The same value may appear more than once.

Output details:
- Return a list of two indexes.
- Index order usually does not matter unless the platform expects a specific answer.

Rules:
- First write brute force in words only.
- Then write optimized code from memory.
- Store numbers you have already seen with their index.
- For each number, check whether `target - current_number` already exists.
- Check complement before storing current value.
- Do not use the same index twice.
- Submit on LeetCode if local tests pass.

Test cases:

```python
[2, 7, 11, 15], target = 9 -> [0, 1]
[3, 2, 4], target = 6 -> [1, 2]
[3, 3], target = 6 -> [0, 1]
[-1, -2, -3, -4, -5], target = -8 -> [2, 4]
[0, 4, 3, 0], target = 0 -> [0, 3]
```

"""
#Brute Force:

def two_sum(nums,target):

    for i in range(len(nums)-1):

        for j in range(i+1,len(nums)):

            if nums[i]+nums[j]==target:
                
                return [i,j]
            
print(two_sum([2, 7, 11, 15],9))
print(two_sum([3, 2, 4],6))
print(two_sum([3, 3],6))
print(two_sum([-1, -2, -3, -4, -5],-8))
print(two_sum([0, 4, 3, 0],0))

# Status:Independent solved

# Time complexity: O(n^2)

# Space complexity: O(1)

# Mistakes/confusions:Here i have question like shall we consider that each input has two Elements which sums to target or bcz if not then i have to stop outer loop 1 idex early. 

# Pattern trigger: Traversal with comparison.

# LeetCode submission status:Not submitted

#Optimal version using the dict:

def two_sum(nums,target):
    seen={}
    for i in range(len(nums)):
        needed=target-nums[i]
        if needed in seen:
            return [seen[needed],i]
        seen[nums[i]]=i


print(two_sum([2, 7, 11, 15],9))
print(two_sum([3, 2, 4],6))
print(two_sum([3, 3],6))
print(two_sum([-1, -2, -3, -4, -5],-8))
print(two_sum([0, 4, 3, 0],0))

# Status:Independent solved

# Time complexity: O(n)

# Space complexity: O(n)

# Mistakes/confusions:

# Pattern trigger: 

# LeetCode submission status:Not submitted

"""
### Revision 2. First Unique Character OR Valid Anagram

Choose the one that feels weaker after warm-up.

## Option A: First Unique Character

Why revisit: Day 03 optimized second pass needed a hint.  
Pattern: Frequency map + second pass  
Difficulty: Easy  
LeetCode: Required

Problem:

Given a string `s`, return the index of the first non-repeating character.

If every character repeats, return `-1`.

Example:

```python
s = "leetcode"
```

Expected output:

```python
0
```

Why:

```text
"l" appears only once and is the first unique character.
```

Input details:
- Input is a string `s`.
- The string may be empty.
- Characters can repeat.

Output details:
- Return the index of the first character whose count is `1`.
- Return `-1` if no unique character exists.

Requirements:
- First write the brute-force nested-loop idea.
- Then solve using a frequency dictionary.
- First pass: count every character.
- Second pass: scan the original string by index.
- Return the first index whose character count is `1`.

Test cases:

```python
"leetcode" -> 0
"loveleetcode" -> 2
"aabb" -> -1
"z" -> 0
"" -> -1
"dddccdbba" -> 8
```

Edge cases to remember:
- Empty string returns `-1`.
- One-character string returns `0`.
- Do not return the first key in the dictionary; scan original order.
- Character count must be exactly `1`.

"""
#Brute Force:

def First_Unique_Char(s):
    if not s:
        return -1

    for i in range(len(s)):

        count=0

        for j in range(len(s)):
            
            if s[i]==s[j]:
                count+=1
        if count==1:
            return i
    return -1

print(First_Unique_Char("leetcode"))
print(First_Unique_Char("loveleetcode"))
print(First_Unique_Char("aabb"))
print(First_Unique_Char("z"))
print(First_Unique_Char(""))
print(First_Unique_Char("dddccdbba"))

# Status:Independent solved

# Time complexity: O(n^2)

# Space complexity: O(1)

# Mistakes/confusions:

# Pattern trigger: Freq mapping and second pass

# LeetCode submission status:Not submitted

def First_Unique_Char(s):
    if not s:
        return -1

    seen={}

    for i in range(len(s)):
        if s[i] in seen:
            seen[s[i]]+=1
        else:
            seen[s[i]]=1
    for i in range(len(s)):
        if seen[s[i]]==1:
            return i

    return -1

print(First_Unique_Char("leetcode"))
print(First_Unique_Char("loveleetcode"))
print(First_Unique_Char("aabb"))
print(First_Unique_Char("z"))
print(First_Unique_Char(""))
print(First_Unique_Char("dddccdbba"))

# Status:Independent solved

# Time complexity: O(n)

# Space complexity: O(n)

# Mistakes/confusions:

# Pattern trigger: Freq mapping and second pass

# LeetCode submission status:Not submitted

"""
## Option B: Valid Anagram

Why revisit: Day 03 hash-map comparison needed a hint and sorting complexity was unclear.  
Pattern: Character frequency comparison  
Difficulty: Easy  
LeetCode: Required

Problem:

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

An anagram means both strings contain the same characters with the same frequency, but possibly in a different order.

Example:

```python
s = "anagram"
t = "nagaram"
```

Expected output:

```python
True
```

Example:

```python
s = "rat"
t = "car"
```

Expected output:

```python
False
```

Input details:
- Inputs are two strings, `s` and `t`.
- Lengths may be different.
- Characters may repeat.

Output details:
- Return `True` only if both strings have exactly the same character counts.
- Return `False` otherwise.

Requirements:
- First write the brute-force/sorting idea.
- Then solve using a dictionary frequency map.
- If lengths are different, return `False` immediately.
- Count characters in `s`.
- Decrease counts using characters from `t`.
- If any needed character is missing or count becomes negative, return `False`.

Test cases:

```python
"anagram", "nagaram" -> True
"rat", "car" -> False
"a", "a" -> True
"a", "ab" -> False
"listen", "silent" -> True
"aa", "a" -> False
```

Edge cases to remember:
- Different lengths cannot be anagrams.
- Same letters with different counts are not anagrams.
- Sorting approach is simpler but costs O(n log n).

"""

#Brute Force using Nested Loop.

def valid_anagram(s,t):

    if len(s)!=len(t):
        return False

    for i in s:
        count1=0

        for j in s:
            if i==j:
                count1+=1
        count2=0
        for k in t:
            if i==k:
                count2+=1
        
        if count1!=count2:
            return False
    return True

print(valid_anagram("anagram", "nagaram"))
print(valid_anagram("rat", "car"))
print(valid_anagram("a", "a"))
print(valid_anagram("a", "ab"))
print(valid_anagram("listen", "silent"))
print(valid_anagram("aa", "a"))

# Status:Independent solved

# Time complexity: O(n^2)

# Space complexity: O(1)

# Mistakes/confusions:

# Pattern trigger: Freq mapping and second pass

# LeetCode submission status:Not submitted

#Brute Force using sorted()

def valid_anagram(s,t):
    if len(s)!=len(t):
        return False
    
    if sorted(s)!=sorted(t):
        return False
    return True

print("Using Sorted")
print(valid_anagram("anagram", "nagaram"))
print(valid_anagram("rat", "car"))
print(valid_anagram("a", "a"))
print(valid_anagram("a", "ab"))
print(valid_anagram("listen", "silent"))
print(valid_anagram("aa", "a"))

# Status:Independent solved

# Time complexity: O(n log n)

# Space complexity: O(n)

# Mistakes/confusions:

# Pattern trigger: comparing the two Strings

# LeetCode submission status:Not submitted

#optimal Version using Frequncy mapping.

def valid_anagram(s,t):
    if len(s)!=len(t):
        return False
    freq_s={}
    for i in s:
        if i in freq_s:
            freq_s[i]+=1
        else:
            freq_s[i]=1
    freq_t={}
    for i in t:
        if i in freq_t:
            freq_t[i]+=1
        else:
            freq_t[i]=1

    # if freq_s==freq_t: we can use this also
    #     return True
    # else: 
    #     return False

    for char in freq_s:
        if char not in freq_t:
            return False
        if freq_s[char]!=freq_t[char]:
            return False
    return True

    


print("Using the Freq")    
    
print(valid_anagram("anagram", "nagaram"))
print(valid_anagram("rat", "car"))
print(valid_anagram("a", "a"))
print(valid_anagram("a", "ab"))
print(valid_anagram("listen", "silent"))
print(valid_anagram("aa", "a"))

# Status:Independent solved

# Time complexity: O(n)

# Space complexity: O(n)

# Mistakes/confusions: intailly during the second pass in mannal freq Comparison i used index instead of element for loop.

# Pattern trigger: Frquency Mapping and Second Pass 

# LeetCode submission status:Not submitted


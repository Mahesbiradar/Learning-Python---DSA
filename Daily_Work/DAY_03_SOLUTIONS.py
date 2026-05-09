## Fundamentals Revision

#Task: Write a small frequency counter from memory.

def count_frequency(items):
    seen={}
    for i in items:
        if i in seen:
            seen[i]+=1
        else:
            seen[i]=1
    return seen

print(count_frequency([1,3,4,1,2,4]))


#time comp: O(n)
#Space Comp: O(n)


"""
### 1. Two Sum

Topic: Hashing  
Pattern: Dictionary complement lookup  
Difficulty: Easy/Medium  
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

Requirements:
- First write the brute-force nested-loop idea.
- Then solve using a dictionary.
- Store numbers you have already seen with their index.
- For each number, check whether `target - current_number` already exists.
- Do not use the same index twice.

Test cases:

```python
[2, 7, 11, 15], target = 9 -> [0, 1]
[3, 2, 4], target = 6 -> [1, 2]
[3, 3], target = 6 -> [0, 1]
[-1, -2, -3, -4, -5], target = -8 -> [2, 4]
[0, 4, 3, 0], target = 0 -> [0, 3]
```

Status:
- [ ] Independent solve
- [ ] Hint used
- [ ] Solution viewed
- [ ] Unsolved

Problem-solving notes:

Brute-force idea:

Dry run:

Optimized idea:

Solution:

```python

```

Time complexity:

Space complexity:

Mistakes/confusions:

Pattern trigger:

LeetCode submission status:
- [ ] Not submitted
- [ ] Accepted
- [ ] Wrong answer
- [ ] Time limit exceeded
- [ ] Revisit required

Revisit requirement:

---

"""
#Brute-force idea:Ill run a nested loop to to find the inxees of the numbers.

"""Dry run: 
Outer loop start
1.i=2 j=7 target=9   i+j=target? True print(i,j)


"""
def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]

print(two_sum([2, 7, 11, 15],9))
print(two_sum([3, 2, 4],6))
print(two_sum([3, 3],6))
print(two_sum([-1, -2, -3, -4, -5],-8))
print(two_sum([0, 4, 3, 0],0))

# Time complexity:O(n^2)

# Space complexity:O(1)

# Mistakes/confusions:intailly i was checking the needed=i-target in the inner loop but later got the idea

# Pattern trigger:

# Optimized idea:Now ill use dict to store the seen values in loop and then calcuate the target.

##Status:solution viewd

#Leetcode: Not submitted


def two_sum(nums,target):

    seen={}

    for i in range(len(nums)):
        needed=target-nums[i]

        if needed in seen:
            return(seen[needed],i)
        seen[nums[i]]=i

print(two_sum([2, 7, 11, 15],9))
print(two_sum([3, 2, 4],6))
print(two_sum([3, 3],6))
print(two_sum([-1, -2, -3, -4, -5],-8))
print(two_sum([0, 4, 3, 0],0))

# Time complexity:O(n)

# Space complexity:O(n)

# Mistakes/confusions:i was completing the code mostly but stuck at one line seen[nums[i]]=i  where initailly i was written seen[needed]=i Here i got confusured to store the elements in dict.

# Pattern trigger:Frequency Hashing

# Optimized idea:Now ill use dict to store the seen values in loop and then calcuate the target.

#Status:solution viewd (The last line is not able to think)

#Leetcode: Not submitted


"""

### 2. Valid Anagram

Topic: Hashing / Strings  
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

Status:
- [ ] Independent solve
- [ ] Hint used
- [ ] Solution viewed
- [ ] Unsolved

Problem-solving notes:

Brute-force idea:

Dry run:

Optimized idea:

Solution:

```python

```

Time complexity:

Space complexity:

Mistakes/confusions:

Pattern trigger:

LeetCode submission status:
- [ ] Not submitted
- [ ] Accepted
- [ ] Wrong answer
- [ ] Time limit exceeded
- [ ] Revisit required

Revisit requirement:

---

"""
    

#Brute-force idea: Here i will run a nested loop to check the count of element of s in both strings and compare the frequency.



def check_anagram(s,t):
    if len(s)!=len(t):
        return False

    for i in s:

        count1=0
        count2=0
        for j in s:
            if i==j:
                count1+=1
        for k in t:
            if i==k:
                count2+=1
        if count1!=count2:
            return False
    return True
    
# print(check_anagram("anagram", "nagaram"))
# print(check_anagram("rat", "car" ))
# print(check_anagram("a", "ab"))
# print(check_anagram("listen", "silent"))


# Time complexity: O(n^2)

# Space complexity:O(1)

# Mistakes/confusions:initially i was confused like how can compare and count frequcy paralally but later got it

# Pattern trigger: Frequency comparison

#Status:Hint used

#Leetcode: Not submitted


#Using the sorting menthod.

def check_anagram(s,t):

    if len(s)!=len(t):
        return False
    
    if sorted(s)==sorted(t):
        return True
    return False

# print(check_anagram("anagram", "nagaram"))
# print(check_anagram("rat", "car" ))
# print(check_anagram("a", "ab"))
# print(check_anagram("listen", "silent"))


# Time complexity: O(n log n)

# Space complexity:O(n)

# Mistakes/confusions: Here the time complexity is not understood.

#Status:splved independently

#Leetcode: Not submitted


#Using the Frquency Hashing:

def check_anagram(s,t):
    if len(s)!=len(t):
        return False
    freq1={}
    freq2={}

    for i in s:
        if i in freq1:
            freq1[i]+=1
        else:
            freq1[i]=1
    
    for i in t:
        if i in freq2:
            freq2[i]+=1
        else:
            freq2[i]=1
    
    # if freq1==freq2: this also valid
    #     return True
    # return False

    #for manual checking of occurance & frequncy of elements:

    for char in freq1:
        if char not in freq2:
            return False
        if freq1[char]!=freq2[char]:
            return False
    return True
        
    

print(check_anagram("anagram", "nagaram"))
print(check_anagram("rat", "car" ))
print(check_anagram("a", "ab"))
print(check_anagram("listen", "silent"))


# Time complexity: O()

# Space complexity:O(n)

# Mistakes/confusions: Hint used for manual dictionary comparison syntax

#Status:Hint used

#Leetcode: Not submitted
  
    

"""
### 3. First Unique Character in a String

Topic: Hashing / Strings  
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

Example:

```python
s = "loveleetcode"
```

Expected output:

```python
2
```

Why:

```text
"v" is the first character with frequency 1.
```

Requirements:
- First write the brute-force nested-loop idea.
- Then solve using a frequency dictionary.
- First pass: count every character.
- Second pass: return the first index whose character count is `1`.
- Return `-1` if no unique character exists.

Test cases:

```python
"leetcode" -> 0
"loveleetcode" -> 2
"aabb" -> -1
"z" -> 0
"" -> -1
"dddccdbba" -> 8
```

Status:
- [ ] Independent solve
- [ ] Hint used
- [ ] Solution viewed
- [ ] Unsolved

Problem-solving notes:

Brute-force idea:

Dry run:

Optimized idea:

Solution:

```python

```

Time complexity:

Space complexity:

Mistakes/confusions:

Pattern trigger:

LeetCode submission status:
- [ ] Not submitted
- [ ] Accepted
- [ ] Wrong answer
- [ ] Time limit exceeded
- [ ] Revisit required

Revisit requirement:

"""

#Brute Force: i simlry run a loop over a string and then pick first Element and then run a nested loop on same strin and then Count the occurance of that element if the occurance is 1 Then ill exit the loop and return the index.

def first_unique_Char(s):

    if not s:
        return -1
    
    for i in range(len(s)):
        count=0

        for j in s:
            if s[i]==j:
                count+=1
        if count==1:
            return i
    return -1

print(first_unique_Char("leetcode"))  #0
print(first_unique_Char("loveleetcode"))   #2
print(first_unique_Char("aabb"))   #-1
print(first_unique_Char("z"))  #0
print(first_unique_Char(""))  #-1
print(first_unique_Char("dddccdbba")) #8


#Time complexity:O(n^2)

# Space complexity:O(1)

# Mistakes/confusions:NA

# Pattern trigger: Frequency map + second pass

# LeetCode submission status: not submittes

#Status: Solved independently

#optimal solution: Using the hashing

def first_unique_Char(s):

    if not s:
        return -1
    seen={}
    
    for i in s:
        if i in seen:
            seen[i]+=1
        else:
            seen[i]=1
    
    for i in range(len(s)):
        if seen[s[i]]==1:
            return i
    return -1

print(first_unique_Char("leetcode"))  #0
print(first_unique_Char("loveleetcode"))   #2
print(first_unique_Char("aabb"))   #-1
print(first_unique_Char("z"))  #0
print(first_unique_Char(""))  #-1
print(first_unique_Char("dddccdbba")) #8

#Time complexity:O(n)

# Space complexity:O(n)

# Mistakes/confusions:in second pass i was actully looping the frequncy but thought i would get the index but later with hind i run a loop over s and campared the occurance.

# Pattern trigger: Frequency map + second pass

# LeetCode submission status: not submittes

#Status: Solved with hint for Second pass.


"""
### Revision 1. Remove Element

Why revisit: write-pointer pattern was solved using a nearby reference.  
Pattern: write pointer  
Reminder: keep non-target values at the front and return the write pointer.

Problem:

Given a list `nums` and an integer `val`, remove all occurrences of `val` in-place.

Return the new length after removal.

The order of remaining elements can stay the same.

Example:

```python
nums = [3, 2, 2, 3]
val = 3
```

Expected output:

```python
2
```

After the function runs, the first `2` positions should contain:

```python
[2, 2]
```

Requirements:
- Solve in-place.
- Use a write pointer.
- Do not create a second list for the optimized solution.
- Return the new length.
- Only the first returned length positions matter.

Test cases:

```python
[3, 2, 2, 3], val = 3 -> 2, first part [2, 2]
[0, 1, 2, 2, 3, 0, 4, 2], val = 2 -> 5, first part [0, 1, 3, 0, 4]
[], val = 1 -> 0, first part []
[1, 1, 1], val = 1 -> 0, first part []
[4, 5], val = 3 -> 2, first part [4, 5]
```

Status:
- [ ] Independent re-solve
- [ ] Hint used
- [ ] Solution viewed
- [ ] Unsolved

Dry run:

Brute-force idea:

Optimized idea:

Solution:

```python

```

Time complexity:

Space complexity:

Mistakes/confusions:

Revisit again?
- [ ] No
- [ ] 24 hours
- [ ] 3 days
- [ ] 7 days

---

"""

# Brute-force idea: intiate a new list and run a loop over the list and append the elements to new list which are not eaqul to val. and return the length of new List.


#optimized in-place Solution

def remove_element(nums,val):

    write=0

    for i in nums:
        if i!=val:
            nums[write]=i
            write+=1
    
    return write

print(remove_element([3, 2, 2, 3],3))  #2
print(remove_element([0, 1, 2, 2, 3, 0, 4, 2],2)) #5
print(remove_element([],1)) #0
print(remove_element([1, 1, 1],1)) #0
print(remove_element([4, 5],2)) #2

# Time complexity: O(n)

# Space complexity: O(1)

# Mistakes/confusions:NA

# Status:- [] Independent re-solve -YES

#Leetcode : Not submitted.

#Pattern: List Traversal and Use of Write Pointer.


"""
### Revision 2. Product Of Array Except Self

Why revisit: prefix/suffix idea and space complexity were unstable on Day 2.  
Pattern: prefix/suffix products  
Reminder: output array does not count as extra space if the problem requires returning it.

Problem:

Given a list of integers `nums`, return a list `answer` such that `answer[i]` is equal to the product of all elements of `nums` except `nums[i]`.

You must solve it without using division.

Example:

```python
nums = [1, 2, 3, 4]
```

Expected output:

```python
[24, 12, 8, 6]
```

Why:

```text
answer[0] = 2 * 3 * 4 = 24
answer[1] = 1 * 3 * 4 = 12
answer[2] = 1 * 2 * 4 = 8
answer[3] = 1 * 2 * 3 = 6
```

Requirements:
- First write the brute-force nested-loop idea.
- Then solve using prefix and suffix products.
- Do not use division.
- Try the optimized version using the output array and one running suffix variable.
- Remember: if the output array is required by the problem, it usually does not count as extra space.

Test cases:

```python
[1, 2, 3, 4] -> [24, 12, 8, 6]
[-1, 1, 0, -3, 3] -> [0, 0, 9, 0, 0]
[2, 3] -> [3, 2]
[0, 0] -> [0, 0]
[5] -> [1]
```

Status:
- [ ] Independent re-solve
- [ ] Hint used
- [ ] Solution viewed
- [ ] Unsolved

Dry run:

Brute-force idea:

Optimized idea:

Solution:

```python

```

Time complexity:

Space complexity:

Mistakes/confusions:

Revisit again?
- [ ] No
- [ ] 24 hours
- [ ] 3 days
- [ ] 7 days
"""

#brute-force nested-loop:

def prod_array(nums):

    

    p_array=[]

    for i in range(len(nums)):
        
        prod=1
        for j in range(len(nums)):

            if i==j:
                continue
            else:
                prod*=nums[j]
        p_array.append(prod)

    return p_array

print(prod_array([1, 2, 3, 4]))
print(prod_array([-1, 1, 0, -3, 3]))
print(prod_array([2, 3] ))
print(prod_array([0, 0]))
print(prod_array([5] ))

# Time complexity: O(n^2)

# Space complexity: O(n)

# Mistakes/confusions:intially i made mistake intially major Bug was prod*=j later realized and fixed.

# Status:- [] Independent re-solve -YES

#Leetcode : Not submitted.

#Pattern: List Traversal.

#Optimized idea: use of prefix and suffix in place.




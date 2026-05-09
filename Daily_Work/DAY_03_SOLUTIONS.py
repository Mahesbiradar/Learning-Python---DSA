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
  
    

    
"""
## Fundamentals Revision

Task: Write these from memory before LeetCode-style problems.

```python
def running_sum(nums):
    pass

def clean_hash_anagram(s, t):
    pass
```

Checklist:
- [ ] Running sum handles empty list.
- [ ] Running sum does not overwrite needed values incorrectly.
- [ ] Anagram version uses dictionary membership/comparison, not string membership inside a loop.
- [ ] Time and space complexity written for both.

Expected behavior:

```python
running_sum([1, 2, 3, 4]) -> [1, 3, 6, 10]
running_sum([]) -> []

clean_hash_anagram("anagram", "nagaram") -> True
clean_hash_anagram("rat", "car") -> False
clean_hash_anagram("aa", "a") -> False
```

Solutions:

```python

```

Complexity:
- `running_sum`: Time = , Space =
- `clean_hash_anagram`: Time = , Space =

"""

#1. Revision problem.

def running_sum(nums):
    if not nums:
        return nums

    new_nums=[nums[0]]

    for i in range(1,len(nums)):
        new_nums.append(new_nums[i-1]+nums[i])

    return new_nums

print(running_sum([1, 2, 3, 4]))
print(running_sum([]))

#time Comp: O(n)
#Space Comp :O(n)

#2. Revision Problem 

def clean_hash_anagram(s, t):

    if len(s)!=len(t):
        return False
    
    freq_s={}

    for i in s:
        if i in freq_s:
            freq_s[i]+=1
        else:
            freq_s[i]=1
    
    freq_t={}
    for j in t:
        if j in freq_t:
            freq_t[j]+=1
        else:
            freq_t[j]=1
    
    for i in s:
        if i not in freq_t:
            return False
        if freq_s[i]!=freq_t[i]:
            return False
    
  
    return True
    
print(clean_hash_anagram("anagram", "nagaram"))
print(clean_hash_anagram("rat", "car"))
print(clean_hash_anagram("aa", "a"))

#Time comp: O(n)
#Space Comp:O(n)

#Mistakes: Intially i was getting key error for second function call bcz i have not handled the edge case (membership checking of elements of s in freq_t) and i was checking for in string later lealized it will incraese the complexity then fixed.

"""
## Today's New Problems

### 1. Running Sum of 1d Array

Topic: Arrays / Prefix Sum  
Pattern: Running total  
Difficulty: Easy  
LeetCode: Recommended

Problem:

Given a list `nums`, return a list where each index contains the sum of all values from index `0` to that index.

Example:

```python
nums = [1, 2, 3, 4]
```

Expected output:

```python
[1, 3, 6, 10]
```

Why:

```text
1
1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 4 = 10
```

Requirements:
- Use a running total.
- Return a new list first.
- Then try the in-place version if time remains.
- Write time and space complexity for both versions.

Test cases:

```python
[1, 2, 3, 4] -> [1, 3, 6, 10]
[1, 1, 1, 1, 1] -> [1, 2, 3, 4, 5]
[3, 1, 2, 10, 1] -> [3, 4, 6, 16, 17]
[] -> []
[-1, 2, -3, 4] -> [-1, 1, -2, 2]
```

Edge cases:
- Empty list.
- Negative values.
- One-element list.


"""

#Solution using Newlist:
# Brute-force idea:intialize new list with then run a loop over list and appending the sum of from 0 index to current index to new list.


def running_sum(nums):

    if len(nums)<2:
        return nums
    
    new_nums=[nums[0]]

    for i in range(1,len(nums)):
        new_nums.append(new_nums[i-1]+nums[i])
    
    return new_nums

print(running_sum([1, 2, 3, 4]))
print(running_sum([1, 1, 1, 1, 1]))
print(running_sum([3, 1, 2, 10, 1]))
print(running_sum([-1, 2, -3, 4]))
print(running_sum([]))


# Status:
# - [Yes] Independent solve


# Time complexity: O(n)

# Space complexity: O(n)

# Mistakes/confusions: NA

# Pattern trigger:prefix sum 

# LeetCode submission status:Not submitted

#Solution using in-place:
#Optimal solution: ill run aloop fron index 1 over list and then owerite the current index value by adding prv element with current element.

def running_sum(nums):

    if len(nums)<2:
        return nums
    
    for i in range(1,len(nums)):
        nums[i]+=nums[i-1]
    
    return nums
    
print(running_sum([1, 2, 3, 4]))
print(running_sum([1, 1, 1, 1, 1]))
print(running_sum([3, 1, 2, 10, 1]))
print(running_sum([-1, 2, -3, 4]))
print(running_sum([]))

# Status:
# - [Yes] Independent solve


# Time complexity: O(n)

# Space complexity: O(1)

# Mistakes/confusions: NA

# Pattern trigger:prefix sum 

# LeetCode submission status:Not submitted

"""
### 2. Find Pivot Index

Topic: Arrays / Prefix Sum  
Pattern: Left sum equals right sum  
Difficulty: Easy  
LeetCode: Recommended

Problem:

Given a list `nums`, return the leftmost index where the sum of values to the left equals the sum of values to the right. If no such index exists, return `-1`.

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

Requirements:
- First write the brute-force idea.
- Then solve using `total_sum` and `left_sum`.
- At each index, compute `right_sum = total_sum - left_sum - nums[i]`.
- Check before adding current value to `left_sum`.

Test cases:

```python
[1, 7, 3, 6, 5, 6] -> 3
[1, 2, 3] -> -1
[2, 1, -1] -> 0
[0, 0, 0] -> 0
[-1, -1, 0, 1, 1, 0] -> 5

"""
#Brute Force: Using nested loop and two varibale to track the left and rigt sum with Each iteraton.

def pivot_index(nums):

    for i in range(len(nums)):

        left_sum=0
        right_sum=0

        
        for j in range(0,i):
                left_sum+=nums[j]
        
        for k in range(i+1,len(nums)):
            right_sum+=nums[k]
        
        if left_sum==right_sum:
            return i
    return -1

print(pivot_index([1, 7, 3, 6, 5, 6]))
print(pivot_index([1, 2, 3]))
print(pivot_index([2, 1, -1]))
print(pivot_index([0, 0, 0]))
print(pivot_index([-1, -1, 0, 1, 1, 0]))


#The below code is used for debug
# nums=[1, 7, 3, 6, 5, 6]

# for i in range(len(nums)):
#     leftsum=0
#     rightsum=0

#     for j in range(0,i):
#         leftsum+=nums[j]
    
#     for k in range(i+1,len(nums)):
#         rightsum+=nums[k]

#     print(f"at index{i} leftsum={leftsum} and rightsum={rightsum}")

#     if leftsum==rightsum:
#         print(f"the pivot index is:{i}")


# Status:
# - [Yes] Independent solve

# Time complexity: O(n^2)

# Space complexity: O(1)

# Mistakes/confusions: NA

# Pattern trigger:prefix sum /suffix sum

# LeetCode submission status:Not submitted


#optimla solution: here i will run a loop on lits at each index compute the right sum and then compare both rightsum and leftsum and then ill add current element value to leftsum.

def pivot_index(nums):

    total_sum=sum(nums)

    leftsum=0

    for i in range(len(nums)):

        right_sum=total_sum-leftsum-nums[i]

        if leftsum==right_sum:
            return i
        leftsum+=nums[i]
    
    return -1

print(pivot_index([1, 7, 3, 6, 5, 6]))
print(pivot_index([1, 2, 3]))
print(pivot_index([2, 1, -1]))
print(pivot_index([0, 0, 0]))
print(pivot_index([-1, -1, 0, 1, 1, 0]))

        
# Status:
# - [Yes] Independent solve

# Time complexity: O(n)

# Space complexity: O(1)

# Mistakes/confusions: i was juts confused to place the comparison code and  the adding the elements in leftsum.

# Pattern trigger:running prefix sum + derived right sum

# LeetCode submission status:Not submitted

#Revist:Required for optimal solution.


"""
### 3. Best Time To Buy And Sell Stock

Topic: Arrays / Running State  
Pattern: One-pass minimum tracking  
Difficulty: Easy  
LeetCode: Required

Problem:

Given a list `prices`, where `prices[i]` is the stock price on day `i`, return the maximum profit from buying once and selling once later. If no profit is possible, return `0`.

Example:

```python
prices = [7, 1, 5, 3, 6, 4]
```

Expected output:

```python
5
```

Why:

```text
Buy at 1 and sell at 6.
Profit = 6 - 1 = 5
```

Requirements:
- First write the brute-force nested-loop idea.
- Then solve in one pass.
- Track the lowest price seen so far.
- Track the best profit seen so far.
- Never sell before buying.

Test cases:

```python
[7, 1, 5, 3, 6, 4] -> 5
[7, 6, 4, 3, 1] -> 0
[1, 2] -> 1
[2, 1, 2, 1, 0, 1, 2] -> 2
[3] -> 0
```

Edge cases:
- Prices always decreasing.
- One price only.
- Best buy can appear after several high values.
- Later lower price should update `min_price`.

Time target: 30-40 minutes.


"""
#Brute Force using the Nested Loop:
    
def buy_and_sell_stock(nums):
    if not nums:
        return 0

    min_value=nums[0]
    min_value_index=0
    max_profit=0

    for i in range(len(nums)):

        if nums[i]<min_value:
            min_value=nums[i]
            min_value_index=i
        for j in range(min_value_index+1,len(nums)):

            profit=nums[j]-min_value

            if profit>max_profit:
                max_profit=profit
    return max_profit

print(buy_and_sell_stock([7, 1, 5, 3, 6, 4]))
print(buy_and_sell_stock([7, 6, 4, 3, 1]))
print(buy_and_sell_stock([1, 2]))
print(buy_and_sell_stock([2, 1, 2, 1, 0, 1, 2]))
print(buy_and_sell_stock([3]))
        

# Status:
# - [Yes] Independent solve

# Time complexity: O(n^2)

# Space complexity: O(1)

# Mistakes/confusions:

# Pattern trigger:Running minimum tracking / Greedy

# LeetCode submission status:Not submitted

#Revist:Required for optimal solution.


#optimal solution: here ill run a loop and in first pass ill keep the min price and then in next pass ill store the max_profit.

def buy_and_sell_stock(nums):
    if not nums:
        return 0

    min_value=nums[0]
    max_profit=0

    for i in range(len(nums)):

        if nums[i]<min_value:
            min_value=nums[i]
        else:
            profit=nums[i]-min_value

            if profit>max_profit:
                max_profit=profit
    return max_profit

print("Optimized buy and sell stock executes Here")
print(buy_and_sell_stock([7, 1, 5, 3, 6, 4]))
print(buy_and_sell_stock([7, 6, 4, 3, 1]))
print(buy_and_sell_stock([1, 2]))
print(buy_and_sell_stock([2, 1, 2, 1, 0, 1, 2]))
print(buy_and_sell_stock([3]))

# Status:
# - [Yes] Independent solve

# Time complexity: O(n)

# Space complexity: O(1)

# Mistakes/confusions:in this problem i got to know that i can keep passes in loop for initail iteration im checking only min value and once the min fixed the if block stops and then ill start execute else block here ill track profit and there iterations will be after bying stock only.

# Pattern trigger:Running minimum tracking / Greedy

# LeetCode submission status:Not submitted

#Revist:Required for optimal solution.


"""
## Revision Problems

### Revision 1. Valid Palindrome

Why revisit: Day 04 optimized version needed hint/solution exposure for inner skip loops.  
Pattern: Two pointers with skip loops  
Difficulty: Easy 
LeetCode: Required

Rules:
- Do not read yesterday's code first.
- Dry run before coding.
- Use `while left < right and not s[left].isalnum()` for skipping.
- Compare lowercase characters.
- Submit on LeetCode only after local examples pass.

Test cases:

```python
"A man, a plan, a canal: Panama" -> True
"race a car" -> False
" " -> True
"0P" -> False
"No lemon, no melon" -> True
```

Time target: 25-30 minutes.

Status:
- [ ] Independent re-solve
- [ ] Hint used
- [ ] Solution viewed
- [ ] Unsolved

Solution:

```python

```

Revisit again?
- [ ] No
- [ ] 3 days
- [ ] 7 days

---

"""

def valid_palindrome(s):

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

# print(valid_palindrome("A man, a plan, a canal: Panama"))
# print(valid_palindrome("race a car"))
# print(valid_palindrome(" "))
# print(valid_palindrome("No lemon, no melon"))
# print(valid_palindrome("0P"))

# Status:solved using hints

# Time complexity: O(n)

# Space complexity: O(1)

# Mistakes/confusions:initially i wast stuck on the inner loops for skippin non alpa chars and i was confused on flow of loops execution and passing condition.

# Pattern trigger:Two pointers 

# LeetCode submission status:Not submitted

#revisit:Required 

"""
### Revision 2. Is Subsequence

Why revisit: Day 04 required repeated hints for match-pointer placement.  
Pattern: Scan `t`, advance `s` pointer only on match  
Difficulty: Easy  
LeetCode: Recommended

Rules:
- Do not use nested loops.
- Use one pointer for `s`.
- Loop through characters of `t`.
- Check completion inside the loop and after the loop.

Test cases:

```python
s = "abc", t = "ahbgdc" -> True
s = "axc", t = "ahbgdc" -> False
s = "", t = "ahbgdc" -> True
s = "abc", t = "" -> False
s = "aaaaaa", t = "bbaaaa" -> False

"""
def is_subsequence(s,t):

    if not s:
        return True
    if not t:
        return False
    s_pos=0
    
    for i in t:
        # if s[s_pos] not in t:   #this is unnecessary logic.
        #     return False
        if s[s_pos]==i:
            s_pos+=1
        if len(s)==s_pos:
            return True
    return False
print(is_subsequence("abc","ahbgdc"))
print(is_subsequence("axc","ahbgdc"))
print(is_subsequence("agb","ahbgdc"))
print(is_subsequence("abc",""))
print(is_subsequence("aaaaaa","bbaaaa"))


# Status:solved independently

# Time complexity: O(n)

# Space complexity: O(1)

# Mistakes/confusions: Here i solved but initailly i thought to compare the frquency occurance outside loop. and intially i kept one more check in loop for membership check of elements of s in t which is not required and wrong logic.

# Pattern trigger:Membership Check in order with frequency.

# LeetCode submission status:Not submitted

#revisit:Required 

"""
### Product Of Array Except Self

Why optional: This remains important, but Day 05 should not overload before LeetCode proof and Day 04 recall.

Target version:
- Output array for prefix products.
- One running suffix variable.
- No division.
- O(n) time.
- O(1) extra space beyond output.

Time target: 35-45 minutes only if all required tasks are finished.

"""

def product_of_array_except_self(nums):

    left_array=[1]

    for i in range(1,len(nums)):
        left_array.append(left_array[i-1]*nums[i-1])
    
    right_array=[None]*len(nums)
    right_array[-1]=1

    for j in range(len(nums)-2,-1,-1):
        right_array[j]=right_array[j+1]*nums[j+1]
    
    result=[]

    for k in range(len(nums)):
        result.append(left_array[k]*right_array[k])


    return result

print(product_of_array_except_self([1,2,3,4]))

# Status:solved independently

# Time complexity: O(n)

# Space complexity: O(n)

# Mistakes/confusions: 

# Pattern trigger:prefix and suffix.

# LeetCode submission status:Not submitted


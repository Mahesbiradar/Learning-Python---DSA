"""
## Warm-Up — Modulo Variant Template (5 min, write from memory)
Before any problems, write the Prefix Sum Modulo core template from memory.
Key question to answer: why does `prefix[j] % k == prefix[i] % k` mean the subarray is divisible by k?

"""

def modulo_variant(nums,k):

    seen={0:1}

    prefix=0

    count=0


    for i in range(len(nums)):

        prefix+=nums[i]

        if prefix < 0 :
            prefix+=k

        remainder= prefix % k

    
        if remainder in seen:
            count+=seen[remainder]

        seen[remainder]=seen.get(remainder,0)+1

    return False


#why does `prefix[j] % k == prefix[i] % k` mean the subarray is divisible by k?

# if the remainder of the both sum is equal that mean the subarray exist b/w both the Prefix. Therefor the subarray is divisible by k

"""
## TIER 4 Recalls (5 min each, no full solve)
Write the template from memory. If you can't in 3 min → flag as Tier 2 and add to next day.

1. Prefix Sum (Pivot / Equilibrium)
2. Sliding Window (Variable size)

"""

#1. Prefix Sum (Pivot / Equilibrium)

def pivotindex(nums):

    totalsum=sum(nums)
    left=0

    for i in range(len(nums)):

        right=totalsum-nums[i]-left

        if right==left:
            return i
        
        left+=nums[i]

    return -1

#Time Taken is 2min

# 2. Sliding Window (Variable size)


def slidingwindow(nums,k):


    countofones=0

   

    left=0

    best=0


    for i in range(len(nums)):

        if nums[i]==1:
            countofones+=1

        while (i-left+1)-countofones > k:

            if nums[left]==1:
                countofones-=1

            left+=1
        
        best=max(best,i-left+1)
    
    return best


#Time Taken is 10 min. Bcz im not able to think on the problems.

#Here what is did is i made a template which counts the maxones in subrray while relacing the k zeros.



## TIER 1 — Priority Revision (solve these first, all of them)

"""
### 1. Find Smallest Letter Greater Than Target (LC 744) — Easy
Given a characters array `letters` that is sorted in non-decreasing order, and a character `target`,
return the smallest character in the array that is strictly greater than `target`.

Note that letters wrap around: if every character in `letters` is smaller than or equal to `target`,
then return `letters[0]`.

**Example 1:**
Input: letters = ["c","f","j"], target = "a"
Output: "c"

**Example 2:**
Input: letters = ["c","f","j"], target = "c"
Output: "f"

**Example 3:**
Input: letters = ["c","f","j"], target = "j"
Output: "c"

**Constraints:**
- 2 <= letters.length <= 10^4
- letters[i] is a lowercase English letter
- letters is sorted in non-decreasing order
- letters contains at least two different characters
- target is a lowercase English letter

"""


def nextGreatestLetter(letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left=0
        right=len(letters)-1
        char=None

        while left<=right:

            mid=(right+left)//2

            if letters[mid]>target:
                char=letters[mid]
                right=mid-1
            else:
                left+=1
        
        if char==None:
            return letters[0]
        else:
            return char

# Status: Independent
# Time taken: 22 min
# Tier: ___
# Time complexity: O(logn)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Binary search
# Variant: ___
# mistakes/confusion: Initillay with two edgecase thought will make right=mid and left=mid+1 but later realized for third edgecase that i need to Track the Char also.

"""
### 2. Make Sum Divisible by P (LC 1590) — Medium
Given an array of positive integers `nums`, remove the **smallest** subarray (possibly empty) such
that the **sum** of the remaining elements is divisible by `p`. It is **not** allowed to remove
the whole array. Return the length of the smallest subarray that you need to remove, or `-1` if
it is impossible.

A **subarray** is defined as a contiguous block of elements in the array.

**Example 1:**
Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum is 10. Remove [4] → remaining sum = 6, which is divisible by 6.

**Example 2:**
Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: Remove [5,2] → remaining sum = 9, divisible by 9.

**Example 3:**
Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Sum = 6 is already divisible by 3. Remove nothing.

**Constraints:**
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= p <= 10^9

**Self-hint (read only after 20 min of no progress):**
total_remainder = sum(nums) % p. You need to find the shortest subarray
whose sum ≡ total_remainder (mod p). Then use prefix sum + hash map to
find the shortest such subarray in O(n).

"""

#Brute Force solution

def minSubarray(nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        totalsum = sum(nums)

        remainder = totalsum % p

        if totalsum % p == 0:
            return 0

        n=len(nums)

        bestlen=n

        for i in range(len(nums)):

            prefix=0

            for j in range(i,len(nums)):

                prefix+=nums[j]

                if prefix == remainder:

                    bestlen = min(bestlen,j-i+1)
        
        return -1 if bestlen==n else bestlen

# Status: Independent
# Time taken: 15 min
# Tier: ___
# Time complexity: O(n^2)
# Space complexity: O(1)
# LC status: NA 
# Pattern: Nested Loop
# Variant: ___
# mistakes/confusion: ___

#Optimal solution


def minSubarray(nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        totalsum = sum(nums)

        target = totalsum % p

        if target == 0:
            return 0

        seen = {0:-1}

        best = len(nums)

        prefix = 0

        for i in range(len(nums)):

            prefix += nums[i]

            current = prefix % p

            needed = (current - target) % p

            if needed in seen:

                best = min (best, i-seen[needed])
            
            seen[current]=i

        if best == len(nums):
            return -1
        else :
            return best
        
        
# Status: hints (i have taken guided session on the Chatgpt)
# Time taken: 45+ min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(n)
# LC status: Accepted
# Pattern: Prefix sum 
# Variant: Modulo
# mistakes/confusion: Here i need a seperate session on this Prefix sum + module varient to fully euqip on 4 problems,LC 560,LC 523,LC 525,LC 1590 seperate from daily activity.


## TIER 2 — Revision (3 problems)


"""
### 3. Contiguous Array (LC 525) — Medium
Given a binary array `nums`, return the maximum length of a contiguous subarray with an equal
number of `0` and `1`.

**Example 1:**
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

**Example 2:**
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is the longest contiguous subarray with equal number of 0 and 1.

**Constraints:**
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

"""
#Brute Force approach.

def findMaxLength(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best=0

        for i in range(len(nums)):

            countones=0
            countzeros=0

            for j in range(i,len(nums)):


                if nums[j]==1:
                    countones+=1
                else:
                    countzeros+=1

                print(f"i:{nums[i]},j:{nums[j]},countones:{countones},countzeros:{countzeros}")
                
                if countones == countzeros:

                    best=max(best,j-i+1)
        return best

print(findMaxLength([0,1,1,1,1,1,0,0,0]))


# Status: Independent
# Time taken: 20 min
# Tier: ___
# Time complexity: O(n^2)
# Space complexity: O(1)
# LC status: Not submitted
# Pattern:Nested loop
# Variant: ___
# mistakes/confusion: ___


#optimal solution 

def findMaxLength(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen={0:-1}

        prefix=0

        best=0

        for i in range(len(nums)):

            if nums[i]==0:
                prefix-=1
            else:
                prefix+=1
            
            if prefix in seen:

                best=max(best,i-seen[prefix])
            else:

                seen[prefix]=i
        return best

# Status: Hint (video solution senn for intution)
# Time taken: 20 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern:Prefix sum + hash map
# Variant: modulo varient 
# mistakes/confusion: 


"""
### 4. Range Sum Query - Immutable (LC 303) — Easy
Given an integer array `nums`, handle multiple queries of the following type:
Calculate the sum of the elements of `nums` between indices `left` and `right` **inclusive**
where `left <= right`.

Implement the `NumArray` class:
- `NumArray(int[] nums)` — Initializes the object with the integer array `nums`.
- `int sumRange(int left, int right)` — Returns the sum of elements between indices `left` and
  `right` inclusive (O(1) per query is expected).

**Example 1:**
Input:
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output: [null, 1, -1, -3]
Explanation:
numArray = NumArray([-2, 0, 3, -5, 2, -1])
numArray.sumRange(0, 2) → (-2) + 0 + 3 = 1
numArray.sumRange(2, 5) → 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5) → (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

**Constraints:**
- 1 <= nums.length <= 10^4
- -10^5 <= nums[i] <= 10^5
- 0 <= left <= right < nums.length
- At most 10^4 calls will be made to sumRange

"""


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix=[0]


        for i in range(len(nums)):
            self.prefix.append(self.prefix[i]+nums[i])
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        sum_of_range= self.prefix[right+1]-self.prefix[left]
    
        return sum_of_range
    
# Status: solved with hints
# Time taken: 35 min
# Tier: ___
# Time complexity: O(n) init | O(1) query
# Space complexity: O(n)
# LC status: Accepted 
# Pattern: Prefix array 
# Variant: ___
# mistakes/confusion: intially not able to access the class varibale or objects in sumquery.

"""
### 5. Maximum Number of Vowels in a Substring of Given Length (LC 1456) — Medium
Given a string `s` and an integer `k`, return the **maximum number of vowel letters** in any
substring of `s` with length `k`.

Vowel letters in English are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

**Example 1:**
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

**Example 2:**
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

**Example 3:**
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" all contain 2 vowels.

**Constraints:**
- 1 <= s.length <= 10^5
- s consists of lowercase English letters
- 1 <= k <= s.length

**Time target: under 20 min (last attempt was 45 min — focus on recognising the window structure immediately)**

```python
# Your solution here

"""

def maxVowels(s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count=0
        best=0
        left=0

        for right in range(len(s)):

            if s[right] in "aeiou":

                count+=1
            
            while right-left+1 > k:

                if s[left] in "aeiou":
                    count-=1
                left+=1
            
            if right-left+1==k:

                best=max(best,count)
        
        return best

# Status: Independent
# Time taken: 25 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted 
# Pattern: Sliding Window
# Variant: ___
# mistakes/confusion: 

## TIER 3 — Revision (2 problems)


"""
### 6. Length of Last Word (LC 58) — Easy
Given a string `s` consisting of words and spaces, return the length of the **last** word in
the string. A **word** is a maximal substring consisting of non-space characters only.

**Example 1:**
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

**Example 2:**
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

**Example 3:**
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

**Constraints:**
- 1 <= s.length <= 10^4
- s consists of only English letters and spaces ' '
- There will be at least one word in s

```python
# Your solution here
```
# Status: Independent / Hint / Failed
# Time taken: ___ min
# Tier: ___
# Time complexity: O(?)
# Space complexity: O(?)
# LC status: Accepted / NA / Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: ___

"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        count = 0

        for i in range(len(s)):

            if s[i] != " ":
                count += 1
            else:
                count = 0
            
            if count != 0:
                length = count

        return length
    
# Status: Independent
# Time taken: 20 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Linear Search 
# Variant: ___
# mistakes/confusion: ___


"""
### 7. Guess Number Higher or Lower (LC 374) — Easy
We are playing the Guess Game. I pick a number from `1` to `n`. You have to guess which number
I picked. Every time you guess wrong, I will tell you whether the number I picked is higher or
lower than your guess.

You call a pre-defined API `int guess(int num)`, which returns three possible results:
- `-1`: Your guess is higher than the number I picked (i.e. `num > pick`).
- `1`: Your guess is lower than the number I picked (i.e. `num < pick`).
- `0`: Your guess is equal to the number I picked.

Return the number that I picked.

**Example 1:**
Input: n = 10, pick = 6
Output: 6

**Example 2:**
Input: n = 1, pick = 1
Output: 1

**Example 3:**
Input: n = 2, pick = 1
Output: 1

**Constraints:**
- 1 <= n <= 2^31 - 1
- 1 <= pick <= n

**Note from last attempt:** Pattern was misidentified as Two Pointers in file — it is Binary Search.
Recall: left, right = 1, n. mid = (left + right) // 2. Check guess(mid), adjust bounds.

```python
# The guess API is already defined for you.
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          0 if num is equal to the picked number
# def guess(num: int) -> int:

# Your solution here

"""
number=6

def guess(num):
    
    if num == number:
        return 0
    elif num < number:
        return 1
    else:
        return -1

class Solution:
    def guessNumber(self, n: int) -> int:

        left=0
        right=n

        while left <= right:

            mid=(right+left)//2

            num = guess(mid)

            if num == 0:
                return mid
            elif num == 1:
                left=mid+1
            else:
                right=mid-1

# Status: Independent
# Time taken: 20 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(1)
# LC status: Accepted
# Pattern: Binary search
# Variant: not sure 
# mistakes/confusion:

## New Problems (3 problems)

"""
### 8. Find the Divisibility Array of a String (LC 2575) — Medium
You are given a **0-indexed** string `word` of length `n` consisting of digits, and a positive
integer `m`.

The **divisibility array** `div` of `word` is an integer array of length `n` such that:
- `div[i] = 1` if the numeric value of `word[0,...,i]` is divisible by `m`, or
- `div[i] = 0` otherwise.

Return the divisibility array of `word`.

**Example 1:**
Input: word = "998244353", m = 3
Output: [1,1,0,0,0,1,1,0,0]
Explanation:
word[0..0] = "9"      → 9 % 3 = 0      → div[0] = 1
word[0..1] = "99"     → 99 % 3 = 0     → div[1] = 1
word[0..2] = "998"    → 998 % 3 = 2    → div[2] = 0
word[0..5] = "998244" → 998244 % 3 = 0 → div[5] = 1

**Example 2:**
Input: word = "1010", m = 10
Output: [0,1,0,1]
Explanation:
"1"    → 1 % 10 = 1  → div[0] = 0
"10"   → 10 % 10 = 0 → div[1] = 1
"101"  → 101 % 10 = 1→ div[2] = 0
"1010" → 1010 % 10=0 → div[3] = 1

**Constraints:**
- 1 <= n <= 10^5
- word consists of digits from '0' to '9'
- 1 <= m <= 10^9

"""
#Brute Force Solution.

class Solution(object):
    def divisibilityArray(self, word, m):
        """
        :type word: str
        :type m: int
        :rtype: List[int]
        """
        empty_string=""

        out=[]

        for i in range(len(word)):

            empty_string+=word[i]

            num=int(empty_string)

            if num % m ==0:
                out.append(1)
            else:
                out.append(0)
        return out



# Status: Independent
# Time taken: 20 min
# Tier: ___
# Time complexity: O(n^2)
# Space complexity: O(n)
# LC status:Not submitted
# Pattern: ___
# Variant: ___
# mistakes/confusion: intialy i tshoight this is O(n) solution but not. Then i Taken Hint to solve the optimal.

#optimal solution 


class Solution(object):
    def divisibilityArray(self, word, m):
        """
        :type word: str
        :type m: int
        :rtype: List[int]
        """
        remainder=0

        out=[]

        for i in range(len(word)):

            remainder=(remainder * 10 + int(word[i])) % m

            if remainder == 0:
                out.append(1)
            else:
                out.append(0)
        return out
    
# Status: Hint
# Time taken: 35 min
# Tier: ___
# Time complexity: O(n)
# Space complexity: O(n)
# LC status:Accepted
# Pattern: Prefix sum
# Variant: Running modulo
# mistakes/confusion: To understand the mathematical model used Chatgpt.


"""
### 9. K Divisible Elements Subarrays (LC 2261) — Medium
Given an integer array `nums` and two integers `k` and `p`, return the **number of distinct
subarrays** which have **at most** `k` elements divisible by `p`.

Note that two subarrays are **distinct** if they differ at any index.

**Example 1:**
Input: nums = [2,3,3,2,2], k = 2, p = 2
Output: 6
Explanation: The distinct subarrays with at most 2 elements divisible by 2 are:
[2], [2,3], [2,3,3], [3], [3,3], [2]
The subarrays [2] and [3] appear more than once in the array but count as one distinct each.
Other subarrays have more than 2 elements divisible by 2 and are not counted.

**Example 2:**
Input: nums = [1,2,3,4], k = 4, p = 1
Output: 10
Explanation: All elements of nums are divisible by 1. Every subarray has at most 4 elements
divisible by 1. Since all subarrays are distinct, total count = 10 (total subarrays of length 4).

**Constraints:**
- 1 <= nums.length <= 200
- 1 <= nums[i], p <= 200
- 1 <= k <= nums.length
"""

class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        seen=set()

        for i in range(len(nums)):

            current_divisible = 0

            for j in range(i,len(nums)):

                    if nums[j] % p == 0:
                        current_divisible += 1
                    
                    if current_divisible > k:
                        break
                    
                    seen.add(tuple(nums[i:j+1]))

        return len(seen)

# Status: Hint
# Time taken: 40 min
# Tier: ___
# Time complexity: O(n^3)
# Space complexity: O(n)
# LC status: Accepted 
# Pattern: Not sure
# Variant: Not sure
# mistakes/confusion: intially the question in not understood then i was able to make the subarrys but keeping uniques subarray was the difficult taks then with hints able to solve.

"""
### 10. Total Appeal of A String (LC 2262) — Hard
The **appeal** of a string is the number of **distinct** characters found in the string.
For example, the appeal of `"abbca"` is 3 because it has 3 distinct characters: 'a', 'b', 'c'.

Given a string `s`, return the **total appeal of all of its substrings**.

**Example 1:**
Input: s = "abbca"
Output: 28
Explanation:
Substrings of length 1: "a"(1), "b"(1), "b"(1), "c"(1), "a"(1) → sum = 5
Substrings of length 2: "ab"(2), "bb"(1), "bc"(2), "ca"(2)     → sum = 7
Substrings of length 3: "abb"(2), "bbc"(2), "bca"(3)            → sum = 7
Substrings of length 4: "abbc"(3), "bbca"(3)                    → sum = 6
Substrings of length 5: "abbca"(3)                              → sum = 3
Total = 5 + 7 + 7 + 6 + 3 = 28

**Example 2:**
Input: s = "code"
Output: 20
Explanation:
Length 1: "c"(1), "o"(1), "d"(1), "e"(1)          → sum = 4
Length 2: "co"(2), "od"(2), "de"(2)                → sum = 6
Length 3: "cod"(3), "ode"(3)                        → sum = 6
Length 4: "code"(4)                                 → sum = 4
Total = 4 + 6 + 6 + 4 = 20

**Constraints:**
- 1 <= s.length <= 10^5
- s consists of lowercase English letters

**Note:** This is a Hard. Brute force O(n³) is too slow. Think: instead of counting per substring,
count the **contribution** of each character across all substrings it appears in.

```python
# Your solution here

"""

class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0

        for i in range(len(s)):

            seen=set()

            for j in range(i,len(s)):

                seen.add(s[j])

                count+=len(seen)
        return count
    

# Status: Independent
# Time taken: 25 min
# Tier: ___
# Time complexity: O(n^2)
# Space complexity: O(n)
# LC status: Not submitted
# Pattern: Not sure
# Variant: Not sure 
# mistakes/confusion: Not able to think on optimal solution.





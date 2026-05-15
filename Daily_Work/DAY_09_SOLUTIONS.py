
# Concept Warm-Up (write from memory, no notes, 10 min)

# Write Frequency Sorting template from memory:
# ```python
freq_nums={} #assuming this is dictionary.
sorted_freq=sorted(freq_nums.items(),key=lambda x:x[1])  #in case if we need to sort by decending order we can add revers=True

# Write Complement Lookup template from memory:
# ```python
nums=[2,7,5,8,4]
target=9

seen={}
for i in range(len(nums)):
    needed=target-nums[i]
    if needed in seen:
        print(seen[needed],i)   #return is not used as i have not used any function here
    seen[nums[i]]=i

# Complexity check before continuing:
# - Frequency Sorting: Time = _O(n log n)__, Space = _O(n)__
# - Complement Lookup: Time = _O(n)__, Space = O(n)___

"""
## Revision Problems → Submit to LeetCode after independent local solve

### R1. Valid Anagram (LC 242) — Frequency Hashing
3-day recall. No notes. Must use `freq_s == freq_t` comparison. No `char in string` in any loop.

Constraints: 1 <= s.length, t.length <= 5×10⁴. Lowercase letters only.

Examples:
- s="anagram", t="nagaram" → True
- s="rat", t="car" → False
- s="", t="" → True
- s="a", t="ab" → False

Solve locally → If independent → Submit LC 242
Status: [ ] Independent  [ ] Hint  [ ] Failed
LC Result: [ ] Accepted  [ ] Wrong Answer  [ ] Not submitted
Time taken: ___

"""
#R1.a Using the Brute Force approch.

def validanagram(s,t):

    if len(s) != len(t):
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
        if count1 != count2:
            return False
    return True

print(validanagram("anagram","nagaram"))
print(validanagram("rat","car"))
print(validanagram("",""))
print(validanagram("a","ab"))

# Status: [Yes] Independent 
# Time complexicity: O(n^2)
# Space complaxicity: O(1)
# LC status: Not submittes as its not optimal solution.
# mistakes/confusion: NA
# Pattern: Linear Traversal with Freqnce Match.

#R1.b Using the optimal approch.

def validanagram(s,t):

    if len(s) != len(t):
        return False
    freq_s={}

    for i in s:
        freq_s[i]=freq_s.get(i,0)+1
    freq_t={}
    
    for j in t:
        freq_t[j]=freq_t.get(j,0)+1
    
    for key in freq_s:
        if key not in freq_t:
            return False
        if freq_s[key]!=freq_t[key]:
            return False
    return True

print(validanagram("anagram","nagaram"))
print(validanagram("rat","car"))
print(validanagram("",""))
print(validanagram("a","ab"))

# Status: [Yes] Independent 
# Time complexicity: O(n)
# Space complaxicity: O(n)
# LC status: Accepted
# mistakes/confusion: NA
# Pattern: Frequncy Hashing/Matching.


"""
### R2. Two Sum (LC 1) — Complement Lookup
3-day recall. No notes. Check complement first, store after.

Constraints: 2 <= nums.length <= 10⁴. Exactly one valid answer.

Examples:
- [2,7,11,15], target=9 → [0,1]
- [3,2,4], target=6 → [1,2]
- [3,3], target=6 → [0,1]

Solve locally → If independent → Submit LC 1
Status: [ ] Independent  [ ] Hint  [ ] Failed
LC Result: [ ] Accepted  [ ] Wrong Answer  [ ] Not submitted
Time taken: ___

"""
#using optimal solution(complement lookup)

def twosum(nums,target):

    seen={}

    for i in range(len(nums)):

        needed=target-nums[i]

        if needed in seen:
            return [seen[needed],i]
        seen[nums[i]]=i

print(twosum([2,7,11,15],9))
print(twosum([3,2,4],6))
print(twosum([3,3],6))

# Status: [Yes] Independent 
# Time complexicity: O(n)
# Space complaxicity: O(n)
# LC status: Accepted
# mistakes/confusion: NA
# Pattern: complement Lookup


"""
### R3. First Unique Character in a String (LC 387) — Frequency Hashing
24h recall. Count first, second pass over original string (not dict).

Constraints: 1 <= s.length <= 10⁵. Lowercase letters only.

Examples:
- "leetcode" → 0
- "loveleetcode" → 2
- "aabb" → -1
- "" → -1

Edge case before submitting: empty string, all same chars.

Solve locally → If independent → Submit LC 387
Status: [ ] Independent  [ ] Hint  [ ] Failed
LC Result: [ ] Accepted  [ ] Wrong Answer  [ ] Not submitted
Time taken: ___


"""
#Brute Force:Using nested Loop

def firtsuniquechar(s):

    for i in range(len(s)):

        count=0

        for j in s:
            if s[i]==j:
                count+=1
        
        if count==1:
            return i
    return -1

print(firtsuniquechar("leetcode"))
print(firtsuniquechar("loveleetcode"))
print(firtsuniquechar("aabb"))
print(firtsuniquechar(""))

# Status: [Yes] Independent 
# Time complexicity: O(n^2)
# Space complaxicity: O(1)
# LC status:NA
# mistakes/confusion: NA
# Pattern: Frequncy of Chars/Second pass 

#Optimized using frequency hashing

def firtsuniquechar(s):

    freq_s={}

    for i in s:
        freq_s[i]=freq_s.get(i,0)+1
    
    for j in range(len(s)):

        if freq_s[s[j]]==1:
            return j
    return -1

print(firtsuniquechar("leetcode"))
print(firtsuniquechar("loveleetcode"))
print(firtsuniquechar("aabb"))
print(firtsuniquechar(""))

# Status: [Yes] Independent 
# Time complexicity: O(n)
# Space complaxicity: O(n)
# LC status: Accepted
# mistakes/confusion: NA
# Pattern: Frequncy Hashing with second pass.

"""
### R4. Best Time to Buy and Sell Stock (LC 121) — Running State
Due for LC submission. Initialize min_price from nums[0], not 0.

Constraints: 1 <= prices.length <= 10⁵. 0 <= prices[i] <= 10⁴.

Examples:
- [7,1,5,3,6,4] → 5
- [7,6,4,3,1] → 0
- [1,2] → 1
- [3] → 0

Edge case before submitting: decreasing prices → 0.

Solve locally → If independent → Submit LC 121
Status: [ ] Independent  [ ] Hint  [ ] Failed
LC Result: [ ] Accepted  [ ] Wrong Answer  [ ] Not submitted
Time taken: ___


"""
def maxprofit(nums):

    min_price=nums[0]
    max_profit=0

    for i in nums:
        if i<min_price:
            min_price=i
        else:
            profit=i-min_price
            if profit>max_profit:
                max_profit=profit
    return max_profit

print(maxprofit([7,1,5,3,6,4]))
print(maxprofit([7,6,4,3,1]))
print(maxprofit([1,2]))
print(maxprofit([3]))

# Status: [Yes] Independent 
# Time complexicity: O(n)
# Space complaxicity: O(1)
# LC status: Accepted
# mistakes/confusion: NA
# Pattern: Runnning state

"""
### N1. Top K Frequent Elements (LC 347) — Frequency Sorting
Last attempt needed syntax help. Today: sorting version only, no bucket. Lambda must fire from memory.

Constraints: 1 <= nums.length <= 10⁵. k is valid. Answer is unique.

Examples:
- [1,1,1,2,2,3], k=2 → [1,2]
- [1], k=1 → [1]
- [-1,-1,2,2,2,3], k=2 → [2,-1]
- [5,3,5,3,2], k=2 → [5,3] any order

Requirements:
- Build freq dict using .get()
- Sort by frequency descending with lambda
- Return first k keys
- Write complexity as O(n + m log m) where m = unique values

Status: [ ] Independent  [ ] Hint  [ ] Failed
Time taken: ___
Complexity written: Time = ___ Space = ___

"""
#Solution using the sorting()

def topkelements(nums,k):

    seen={}
    for i in nums:
        seen[i]=seen.get(i,0)+1
    sorted_seen=sorted(seen.items(),key=lambda x:x[1],reverse=True)
    result=[]

    for key,value in sorted_seen:
        result.append(key)

        if len(result)==k:
            return result

print(topkelements([1,1,1,2,2,3],2))
print(topkelements([-1,-1,2,2,2,3],2))
print(topkelements([5,3,5,3,2],2))
print(topkelements([1],1))

# Status: [Yes] Independent 
# Time complexicity: O(n + m log m)
# Space complaxicity: O(n)
# LC status: NA
# mistakes/confusion: NA
# Pattern: Frequnecy Sorting.

"""
### N2. Majority Element (LC 169) — Frequency Hashing
Due for LC. Today solve locally from scratch. Then move to LC submission queue for Day 10.

Constraints: n >= 1. Majority element always exists (appears > n//2 times).

Examples:
- [3,2,3] → 3
- [2,2,1,1,1,2,2] → 2
- [1] → 1
- [-1,-1,-1,2,3] → -1

Requirements:
- Dictionary frequency version only
- Second pass to find max frequency
- Do NOT use Counter or max() with key

Status: [ ] Independent  [ ] Hint  [ ] Failed
Time taken: ___

"""

def majority_element(nums):

    seen={}
    for i in nums:
        seen[i]=seen.get(i,0)+1
    
    max_frequncy=0
    max_element=None

    for key,value in seen.items():
        if value>max_frequncy:
            max_frequncy=value
            max_element=key
    
    return max_element

print(majority_element([3,2,3]))
print(majority_element([2,2,1,1,1,2,2]))
print(majority_element([-1,-1,-1,2,3]))
print(majority_element([1]))

# Status: [Yes] Independent 
# Time complexicity: O(n)
# Space complaxicity: O(n)
# LC status: NA
# mistakes/confusion: NA
# Pattern: Frequency Hashing.

"""
### N3. Running Sum of 1d Array (LC 1480) — Prefix Sum
Due for LC. Today: in-place version, O(1) space. Then move to LC queue for Day 10.

Constraints: 1 <= nums.length <= 1000. -10⁶ <= nums[i] <= 10⁶.

Examples:
- [1,2,3,4] → [1,3,6,10]
- [1,1,1,1,1] → [1,2,3,4,5]
- [-1,2,-3,4] → [-1,1,-2,2]
- [] → []

Requirements:
- In-place version (modify nums directly)
- O(1) extra space

Status: [ ] Independent  [ ] Hint  [ ] Failed
Time taken: ___

"""
def running_sum(nums):
    
    for i in range(1,len(nums)):
        nums[i]+=nums[i-1]
    return nums

print(running_sum([1,2,3,4]))
print(running_sum([1,1,1,1,1]))
print(running_sum([-1,2,-3,4]))
print(running_sum([]))



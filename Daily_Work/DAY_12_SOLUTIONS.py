
"""
# Day 12 — May 18 — Recovery
Focus: Clear overdue revisions + 24h recalls | Week 2 wrap-up
LC target today: Running Sum (1480) + Find Highest Altitude (1732) — both independent, quick submits

---

## Concept Warm-Up (5 min)
Write both Building-family templates from memory. No notes.

```python
# Prefix Sum — build prefix array where prefix[i] = sum of nums[0..i-1]


```

```python
# Kadane's (Running-State Tracking) — extend or restart at each element


```

"""

## Concept Warm-Up (5 min)
# Prefix Sum — build prefix array where prefix[i] = sum of nums[0..i-1]

nums=[1,2,3,4,5]

prefix=nums[0]
result=[nums[0]]

for i in range(1,len(nums)):
    prefix+=nums[i]
    result.append(prefix)

print(result)

# Kadane's (Running-State Tracking) — extend or restart at each element
#Not fully confident on this topic ill revise and write the solution.

"""
### Sort Characters by Frequency (LC 451)
Pattern: Frequency Sorting
Due: May 17 — 3d recall (OVERDUE)
Constraint: 1 <= s.length <= 5×10^5. Uppercase, lowercase, and digits.
Examples: "tree" → "eert" | "cccaaa" → "cccaaa" | "Aabb" → "bbAa"
Goal: Count character frequencies → sort by frequency descending → build result string.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

#Using the sorting method.

def frequencySort(s):

    freq_s={}

    for i in s:
        freq_s[i]=freq_s.get(i,0)+1

    sort_freq_s=sorted(freq_s.items(),key=lambda x:x[1],reverse=True)

    string=""

    for char,count in sort_freq_s:
        string+=(char*count)

    return string


print(frequencySort("tree"))

# Status: independent solve 
# Time complexicity: O(n+m log m)
# Space complaxicity: O(n)
# LC status:Accepted
# mistakes/confusion: 
# Pattern:frequncy hashing and sorting.

#Using the bucket sort.

def frequencySort(s):

    freq_s={}
    for i in s:
        freq_s[i]=freq_s.get(i,0)+1

    buckets=[]

    for j in range(len(s)+1):
        buckets.append([])
    
    for char ,count in freq_s.items():
        buckets[count].append(char)
    
    result=""

    for k in range(len(buckets)-1,-1,-1):

        for char in buckets[k]:
            result+=char*k

    return result

print(frequencySort("tree"))

# Status: independent solve 
# Time complexicity: O(n)
# Space complaxicity: O(n)
# LC status:Accepted
# mistakes/confusion: NA
# Pattern:frequncy hashing and bucket sorting

"""
### Intersection of Two Arrays II (LC 350)
Pattern: Frequency Hashing
Due: May 17 — 3d recall (OVERDUE)
Constraint: 1 <= nums1.length, nums2.length <= 1000. 0 <= nums1[i], nums2[i] <= 1000.
Examples: [1,2,2,1], [2,2] → [2,2] | [4,9,5], [9,4,9,8,4] → [4,9]
Goal: Count frequencies for both arrays → for each key take min(count1, count2) → expand to result list.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""
def intersect(nums1,nums2):

    seen={}

    for i in nums1:
        seen[i]=seen.get(i,0)+1
    
    result=[]

    for j in nums2:

        if j in seen and seen[j]>0:
            result.append(j)
            seen[j]-=1
    return result

print(intersect([1,2,2,1],[2,2]))

# Status: solved by seen the solution bcz stuck to make the logic 
# Time complexicity: O(n)
# Space complaxicity: O(n)
# LC status:Accepted
# mistakes/confusion: NA
# Pattern:frequncy hashing

"""
### Find the Highest Altitude (LC 1732)
Pattern: Prefix Sum (running prefix max)
Due: May 18 — 24h recall
Constraint: n == gain.length, 1 <= n <= 100, -100 <= gain[i] <= 100.
Examples: [-5,1,5,0,-7] → 1 | [-4,-3,-2,-1,4,3,2] → 0
Goal: Running cumulative altitude from 0 → track max. Start max_alt at 0 (the starting altitude counts).
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

---

"""
def largestAltitude(gain):

    max_gain=0
    prefix_alt=0

    for i in gain:
        prefix_alt+=i

        if prefix_alt>max_gain:
            max_gain=prefix_alt
    return max_gain

print(largestAltitude([-5,1,5,0,-7] ))
print(largestAltitude([-4,-3,-2,-1,4,3,2] ))

# Status: independent solve
# Time complexicity: O(n)
# Space complaxicity: O(1)
# LC status:Accepted
# mistakes/confusion: NA
# Pattern:running state(prefix max)

"""
### Isomorphic Strings (LC 205)
Pattern: Grouping Hash Maps (bijection mapping)
Due: May 18 — 24h recall
Constraint: 1 <= s.length <= 5×10^4. t.length == s.length. Valid ASCII characters.
Examples: "egg", "add" → True | "foo", "bar" → False | "paper", "title" → True | "ab", "aa" → False
Goal: Two dicts — s_to_t and t_to_s. At each position check BOTH directions: if already mapped it must match; if already mapped-to it must come from same source.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___

"""

def isIsomorphic(s,t):

    s_to_t={}

    t_to_s={}

    for char in range(len(s)):

        if s[char] in s_to_t and s_to_t[s[char]]!=t[char]:
            return False
        else:
            s_to_t[s[char]]=t[char]
        
        if t[char] in t_to_s and t_to_s[t[char]]!=s[char]:
            return False
        else: 
            t_to_s[t[char]]=s[char]
    return True

print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo", "bar"))


# Status: independent solve
# Time complexicity: O(n)
# Space complaxicity: O(n)
# LC status:Accepted
# mistakes/confusion: NA
# Pattern: Hash map

"""
### Maximum Product Subarray (LC 152)
Pattern: Running-State Tracking (track both max and min)
Due: May 18 — 24h recall
Constraint: 1 <= nums.length <= 2×10^4. -10 <= nums[i] <= 10.
Examples: [2,3,-2,4] → 6 | [-2,0,-1] → 0 | [-2,3,-4] → 24
Goal: Unlike Kadane's, track both max_prod AND min_prod at every step. A negative number flips min↔max. At each element: new_max = max(num, num*max_prod, num*min_prod). Same for min.
[ ] Solved independently
[ ] Needed hint (note what)
[ ] Submitted to LC — Result: ___


"""

def maxProduct(nums):

    max_prod=float('-inf')

    for i in range(len(nums)):

        prefix_prod=1

        for j in range(i,len(nums)):

            prefix_prod*=nums[j]

            if prefix_prod>max_prod:
                max_prod=prefix_prod
    return max_prod

print(maxProduct([2,3,-2,4]))
print(maxProduct([-2,0,-1]))
print(maxProduct([-2,3,-4]))

# Status: independent solve
# Time complexicity: O(n^2)
# Space complaxicity: O(1)
# LC status:
# mistakes/confusion: The optimize solution ill solve later keep this as pending.
# Pattern: Prefix prod /running state.



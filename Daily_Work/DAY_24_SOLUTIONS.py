# Session 2 — 24-Hour Recall: Yesterday’s New / Hint Problems

"""
## 4. Unique Number of Occurrences (LC 1207)


Pattern: Frequency Hashing

```python
[1,2,2,1,1,3]             # True
[1,2]                     # False
```

[ ] Independent  [ ] Hint


"""

def uniqueOccurrences(arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen={}

        for i in arr:
            seen[i]=seen.get(i,0)+1
        
        seen_set=set()

        for key,value in seen.items():

            if value in seen_set:
                return False
            
            seen_set.add(value)
        return True

print(uniqueOccurrences([1,2,2,1,1,3]))
print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
print(uniqueOccurrences([1,2]))

# Status: independent

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:Na

# Pattern: Frqunecy Hashing.

"""
## 5. Top K Frequent Words (LC 692)

Pattern: Frequency Sorting

Required sort order:

```text
frequency descending
word ascending
```

Test:

```python
["i","love","leetcode","i","love","coding"], 2
# ["i","love"]

["aaa","aa","a"], 1
# ["a"]
```

[ ] Independent  [ ] Hint

"""

def topKFrequent(words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        seen={}

        for i in words:
            seen[i]=seen.get(i,0)+1
        
        sorted_seen=sorted(seen.items(),key=lambda x:(-x[1],x[0]))

        result=[]

        for key,value in sorted_seen:
            result.append(key)

            if len(result)==k:
                return result

print(topKFrequent(["i","love","leetcode","i","love","coding"],2))
print(topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"],4))

# Status: independent

# Time complexity: O(n+mlogm)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:i seen the sotred syntax from web (x:(-x[1],x[0])) still need clarity

# Pattern: Frqunecy sorting

"""
## 6. Two Sum (LC 1)

Pattern: Complement Lookup

Mental trigger:

```text
Store current number -> index
Search for target - current number
```

Test:

```python
[2,7,11,15], 9            # [0,1]
[3,2,4], 6                # [1,2]
[3,3], 6                  # [0,1]
```

[ ] Independent  [ ] Hint

---
"""

def twosum(nums,target):
     
     seen={}

     for i in range(len(nums)):
        needed=target-nums[i]

        if needed in seen:
            return [seen[needed],i]
        
        seen[nums[i]]=i
    

print(twosum([2,7,11,15],9))
print(twosum([3,2,4],6))
          

# Status: independent

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:

# Pattern: Complement Lookup

"""
## 7. Two Sum II — Sorted Array (LC 167)

Pattern: Two Pointers / Complement Lookup

Use the sorted property this time: left and right pointers.

Test:

```python
[2,7,11,15], 9            # [1,2]
[2,3,4], 6                # [1,3]
[-1,0], -1                # [1,2]
```

[ ] Independent  [ ] Hint

"""
def two_sum(nums,target):
     
    right=len(nums)-1
    left=0

    for i in range(len(nums)):
     

        sum=nums[left]+nums[right]
         
        if sum==target:
            return [left+1,right+1]
        elif sum>target:
            right-=1
        else:
             left+=1

print(two_sum([2,7,11,15], 9))
print(two_sum([2,3,4], 6 ))
print(two_sum([-1,0], -1 ))


# Status: independent

# Time complexity: O(n)

# Space complexity: O(1)

# LC status: Accepted

# mistakes/confusion:

# Pattern: Complement Lookup + Two pointers


"""
## 8. Contains Duplicate II (LC 219)

Pattern: Sliding Window + Set

Important order:

```text
check duplicate first
add current item
shrink if window is too large
```

Test:

```python
[1,2,3,1], 3              # True
[1,0,1,1], 1              # True
[1,2,3,1,2,3], 2          # False
```

[ ] Independent  [ ] Hint

--
"""
def containsduplicate(nums,val):
     
    left=0
    seen=set()

    for right in range(len(nums)):
         
        if nums[right] in seen:
            return True
        seen.add(nums[right])

        if (right-left+1)>val:

            seen.remove(nums[left])
            left+=1
    return False

print(containsduplicate([1,2,3,1], 3 ))
print(containsduplicate([1,0,1,1], 1))
print(containsduplicate([1,2,3,1,2,3], 2 ))

# Status: independent

# Time complexity: O(n)

# Space complexity: O(n)

# LC status: Accepted

# mistakes/confusion:

# Pattern: sliding window + set


"""
## 9. Remove Duplicates from Sorted Array (LC 26)

Pattern: Two Pointers + In-place Overwrite

Test:

```python
[1,1,2]                   # return 2; first values become [1,2]
[0,0,1,1,1,2,2,3,3,4]    # return 5; first values become [0,1,2,3,4]
[]                        # return 0
```

[ ] Independent  [ ] Hint

---
"""

def removeduplicate(nums):

    if not nums:
        return 0

    write=1

    for i in range(1,len(nums)):

        if nums[i]!=nums[write-1]:

            nums[write]=nums[i]
            write+=1
    
    return write

print(removeduplicate([1,1,2]  ))
print(removeduplicate([0,0,1,1,1,2,2,3,3,4]  ))


# Status: independent

# Time complexity: O(n)

# Space complexity: O(1)

# LC status: Accepted

# mistakes/confusion:

# Pattern: Two pointers

"""
## 10. Remove Element (LC 27)

Pattern: Two Pointers + In-place Overwrite

Test:

```python
[3,2,2,3], 3             # return 2
[0,1,2,2,3,0,4,2], 2    # return 5
```

[ ] Independent  [ ] Hint

---


"""

def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        write=0

        for i in range(len(nums)):

            if nums[i]!=val:
                nums[write]=nums[i]
                write+=1
        return write

# Status: seen old solution bcz im confused about initilization of write pointer.

# Time complexity: O(n)

# Space complexity: O(1)

# LC status: Accepted

# mistakes/confusion:

# Pattern: Two pointers + inplace Overwrite



     


         

     

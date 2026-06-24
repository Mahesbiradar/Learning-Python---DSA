"""
383. Ransom Note
Easy
Topics
premium lock icon
Companies
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

"""

#Brute Force:

def ransome_note(ransomNote,magazine):


    for i in range(len(ransomNote)):

        count1=0
        count2=0

        for j in range(len(ransomNote)):

            if ransomNote[i]==ransomNote[j]:
                count1+=1
        
        for k in range(len(magazine)):
            if ransomNote[i]==magazine[k]:
                count2+=1
        
        if count2<count1:
            return False
    return True

print(ransome_note(ransomNote = "a", magazine = "b"))
print(ransome_note(ransomNote = "aa", magazine = "ab"))
print(ransome_note(ransomNote = "aa", magazine = "aab"))

#Status:Solved under 15m
#Pattrn:Nestedlopp Traversal
#Time comp: O(n^2)
#Space Comp:O(1)

#Optimal Solution using the Frequncy Hashing.


def canConstruct(ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        seen1={}

        for i in ransomNote:
            seen1[i]=seen1.get(i,0)+1
        seen2={}
        
        for j in range(len(magazine)):

            if magazine[j] in seen1:
                seen2[magazine[j]]=seen2.get(magazine[j],0)+1
            
            if seen1==seen2:
                return True
        return False

#The above solution is old soution where i comparing the Frequncy. the above solution is not working with some edgecases.


#Here is the Accepted Solution.



class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        seen1={}

        for i in ransomNote:
            seen1[i]=seen1.get(i,0)+1

        seen2={}

        for j in magazine:
            seen2[j]=seen2.get(j,0)+1
        
        for k in ransomNote:

            if k not in seen2:
                return False
            elif seen2[k]<seen1[k]:
                return False
        return True
    

#Status:Solved
#Pattrn:Frquency Hashing
#Time comp: O(n)
#Space Comp:O(n)
#LC: Accepted.

"""
11. Container With Most Water
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 
Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

"""


"""
1456. Maximum Number of Vowels in a Substring of Given Length
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

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

        for i in range(len(s)):
            

            if s[i]== "a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u" :
                count+=1
            
            while i-left+1>k:
                if s[left]== "a" or s[left]=="e" or s[left]=="i" or s[left]=="o" or s[left]=="u" :
                    count-=1
                left+=1
            if i-left+1==k:
                best=max(best,count)
                print(s[i],"best:",best , "i", i)
            
            print(i,count,best)
        return best

print(maxVowels("leetcode",3))


#solved after 45 min earlier what i made mistake os if s[i]== "a" or "e"   this alway excutes so then i chnaged.

#time Comp: O(n)

#Space Comp: O(1)

#Pattern : sliding window 


"""

852. Peak Index in a Mountain Array
Solved
Medium
Topics
premium lock icon
Companies
You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.

Example 1:

Input: arr = [0,1,0]

Output: 1

Example 2:

Input: arr = [0,2,1,0]

Output: 1

Example 3:

Input: arr = [0,10,5,2]

Output: 1

 

Constraints:

3 <= arr.length <= 105
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.

"""



def peakIndexInMountainArray(arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        peak_element=float('-inf')
        peak_index=None

        for i in range(len(arr)):

            if arr[i]>peak_element:
                peak_element=arr[i]
                peak_index=i
        return peak_index

#Status: Solved   but if want ot solve in O(log(n)) but im not sure its its sorted array or not then only i can use the binary search.

#time Comp: O(n)


#Space Comp: O(1)

#LC:ACCEPTED.

#Pattern : Linear Search


"""
523. Continuous Subarray Sum
Medium
Topics
premium lock icon
Companies
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false

"""

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        left=0
        prefix=0

        totalsum=sum(nums)

        for right in range(len(nums)):

            prefix+=nums[right]

            if right-left+1>1:

                if prefix==k:
                    return True
                elif prefix>k:
                    prefix-=nums[left]
                    left+=1
        
        if totalsum % k ==0:
            return True
        else:
            return False
        
#This is failing in 62th testcase here we dont found any subarray sum [23,2,4,6,6] k=7  still the system expexting True even if we divide totalsum with k then also reminder reamins.

#LC: Not accepted.

#time Comp: O(n)


#Space Comp: O(1)










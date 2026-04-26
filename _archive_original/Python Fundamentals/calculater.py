# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def mul(a,b):
#     return a*b

# def div(a,b):
#     return a/b

# def calculator():
#     num1=int(input("Enter the Num1: "))
#     oprator=input("Enter the operator: ")
#     num2=int(input("Enter the Num2: "))

#     if oprator=="+":
#         print("The Result:",add(num1,num2))
#     elif oprator=="-":
#         print("The Result:",sub(num1,num2))
#     elif oprator=="*":
#         print("The Result:",mul(num1,num2))
#     elif oprator=="/":
#         print("The Result:",div(num1,num2))
#     else:
#         print("Invalid Operator")
# calculator()


# print(int(-3.9))

# print(round(3.5))
# print(round(2.5))
# print(int("10") + 5)
# print(int("10.5"))


# a="mahesh"
# b="biradar"

# sum=a+b
# print(sum)

# print(str(None))

# print(bool("False"))
# print(bool(""))

# print(2 ** 3 ** 2)
# print(True or (10 / 0))
# print(False and (10 / 0))


# nums = [1, 2, 2, 3, 4, 4, 5]

# new_list=[]
# idx=0
# idx2=1

# for items in nums:
#     if nums[idx]!=nums[idx2]:
#         new_list.append(items)
#         idx+=1
#         idx2+=1
#     # print(new_list)

# print(new_list)

# nums = [2, 4, 6, 8]

# new_list=[]

# for items in nums:
#     new_list.append(items**2)
# print(new_list)
    
# nums = [1, 2, 2, 3, 1, 4]

# freq={}

# for item in nums:
#     if item in freq:
#         freq[item]+=1
#     else:
#         freq[item]=1
# print(freq)

# nums = [2, 7, 11, 15]
# target = 9

# seen = {}

# for i in range(len(nums)):
#     needed = target - nums[i]
    
#     if needed in seen:
#         print([seen[needed], i])
#         break
    
#     seen[nums[i]] = i


# nums = [2, 7, 11, 15]
# target = 9

# seen = {}

# for i in range(len(nums)):
#     current = nums[i]
#     needed = target - current

#     if needed in seen:
#         print([seen[needed], i])
#         break

#     seen[current] = i
    

# #Problem 1

# nums = [1, 2, 3, 4, 5]

# new_list=[]

# for item in nums:
#     new_list.append(item**2)
# print(new_list)

# #the loop goes to each iteration and the value of each item is squred and appended in new_list
# #o(1)

# #Problem 2

# nums2 = [1, 2, 3, 4, 5, 6]

# new_list2=[]

# for item in nums2:
#     if item%2==0:
#         new_list2.append(item)

# print(new_list2)

#Problem 3

# nums = [1, 2, 3, 4, 5, 6]

# new_list=[]

# for item in nums:
#     if item%2==0:
#         new_list.append(item**2)
# print(new_list)


# #Problem 4

# nums2 = [10, 15, 20, 25, 30]

# new_list2=[]

# for num in nums2:
#     if num%5==0 and num%2==0:
#         new_list2.append(num)

# print(new_list2)

# #Problem 5

# nums = [1, 2, 3, 4, 5, 6]

# new_list=[]

# for i in nums:
#     if i%2==0:
#         new_list.append(i**2)
#     else:
#         new_list.append(i**3)
# print(new_list)

# # #Problem 6

# nums2 = [1, 2, 2, 3, 3, 3]

# idx=0

# for i in nums:
#     idx+=1

# print(idx)

# num = float("2.5")
# num2=int(num)
# print(num2)

# if True:
#     print("A")
# print("B")

# if True:
#     print("A")
#     print("B")
# print("C")


# import keyword

# # List all keywords in Python
# print(keyword.kwlist)

# Problem 1: Square Numbers
# nums = [1, 2, 3, 4]
# new_list=[]

# for item in nums:
#     new_list.append(item**2)
# print(new_list)

# Problem 2: Count Even Numbers

# nums = [1, 2, 3, 4, 5, 6]
# count=0
# for item in nums:
#     if item%2==0:
#         count+=1
# print(count)

# Problem 3: Sum of List

# nums = [10, 20, 30]
# sum=0
# for item in nums:
#     sum+=item
# print(sum)

#Problem 4: Reverse Without Built-in

# nums = [1, 2, 3, 4]
# new_list=[]

# for i in range(len(nums)-1,-1,-1):
#     new_list.append(nums[i])
# print(new_list)

# 



#Problem 5: Find Maximum

# nums = [3, 7, 2, 9, 5]

# maximum=0
# idx=0

# for item in nums:
#     current=nums[idx]
#     idx+=1
#     if maximum<current:
#         maximum=current
# print(maximum)

#Problem 6: Remove Duplicates (No set)

# nums = [1, 2, 2, 3, 1, 4]
# new_list=[]

# for item in nums:
#     if item not in new_list:
#         new_list.append(item)
# print(new_list)


#Problem 7: Second Largest Number

# nums = [10, 20, 4, 45, 99]
# max1=nums[0]
# max2=nums[0]

# for num in nums:
#     if num>max1:
#         max2=max1
#         max1=num
        
#     # elif


# print(max1)
# print(max2)
   
     
# nums = [1, 2, 3, 4, 5, 6]
# new_list=[]

# for i in nums:
#     if i%2==0:
#         new_list.append(i+10)
#     else:
#         new_list.append(i-1)
# print(new_list)

# nums = [2, 4, 6, 8]
# count=0

# for num in nums:
#     if num%2==0:
#         count+=1
# if count==len(nums):
#     print("ALL EVEN")
# else:
#     print("NOT ALL EVEN")

# nums = [1, 2, 3, 4, 5, 6]

# even_num=0
# odd_num=0
# for num in nums:
#     if num%2==0:
#         even_num+=1
#     else:
#         odd_num+=1
# print(F"Even: {even_num}")
# print(F"Odd: {odd_num}")

# nums = [2, 4, 6, 7, 8]

# for num in nums:
#     if num % 2 !=0:
#         print(f"First odd number: {num}")
#         break


# nums = [1, 2, 3, 4, 2, 5]
# new_list=[]

# for num in nums:
#     if num in new_list:
#         print(f"First duplicate:{num}")
#         break
#     else:
#         new_list.append(num)

# x=4

# result="Even" if x%2==0 else "Odd"

# print(result)

# nums = [1, 2, 3, 4, 5, 6]

# new_list = []

# for num in nums:
#     new_list.append(num**2 if num%2==0 else num**3)

# print(new_list)

# nums = [1, 2, 3, 4, 5, 6]

# new_list=[num**3 for num in nums if num % 2 !=0]

# # new_list.append(num**2 for num in nums if num%2==0)



# print(new_list)


# nums = [1, 2, 3, 4, 5, 6]

# for num in nums:

# class solution: 
    
#     def twosum(self,nums,target):

#         nums = [2,7,11,15]
#         target = 9
#         seen={}

#         for i in range(len(nums)):
#             current=nums[i]
#             needed=target-current

#             if needed in seen:
#                 return [seen[needed],i]   
                     
#             seen[current]=i  


# count = 1
# max_iterations = 10

# while count <= 11 and max_iterations > 0:
#     print(count)
#     count += 1
#     max_iterations -= 1

# nums = [1, 3, 4, 2, 2]

# seen=[]

# for num in nums:
#     if num in seen:
#         print(num)
#         break
#     seen.append(num)

#Find first odd number (using while)

# nums = [2, 4, 6, 7, 8]
# idx=0
# print(len(nums))

# while idx<=len(nums):
#     if nums[idx]%2!=0:
#         print(nums[idx])
#         break
#     idx+=1

# nums = [1, 2, 3, 4]

# new_list=[]

# i=len(nums)-1  #i=3

# while i>=0:
#     new_list.append(nums[i])
#     # print(i)
#     i-=1
# print(new_list)


# nums = [1, 2, 3, 3, 1]

# left=0
# right=len(nums)-1

# is_polyndrome=True

# while left<right:
#     if nums[left] != nums[right]:
#         is_polyndrome=False
#         break
    
#     left+=1
#     right-=1
# if is_polyndrome:
#     print("Poly")
# else:
#     print("non poly")

# for i in range(5):
#     print(i)

# for i in range(3):
#     if i == 1:
#         pass
#     print(i)

# # #🔥 Problem 1 — break
# nums = [2, 4, 6, 7, 8, 10]

# for num in nums:
#     if num==7:
#         print(f"First odd number:{num}")
#         break

# #🔥 Problem 2 — continue

# nums = [1, 2, 3, 4, 5]

# for num in nums:
#     if num%2!=0:
#         continue
#     print(num)

# #🔥 Problem 3 — Combined (IMPORTANT)
# nums = [1, -2, 3, -4, 5, 0, 6]
              
# for num in nums:
#     if num<0:
#         continue
#     if num==0:
#         break
#     print(num)

# for i in range(3):
#     for j in range(3):
#         if j == 1:
#             break
#         print(i, j)

# valid_options = ["yes", "no", "maybe"]

# user_input = input("Please enter yes, no, or maybe: ")

# for option in valid_options:
#     if user_input.lower() == option:
#         print("Thank you for your input.")
#         break
# else:
#     print("Invalid input, please try again.")

# #Problem 1 — Search Element

# nums = [10, 20, 30, 40]
# target = 25

# for num in nums:
#     if num==target:
#         print("Found",num)
#         break
# else:
#     print("Not Found")

# 🔥 Problem 2 (Interview Trap)

# nums = [2, 2, 4, 1]
# idx=0
# for num in nums:
#     if num%2==0:
#         idx+=1
#     if idx==len(nums):
#         print("All nums are even")
#         break
# else:
#     print("All nums are not even")

# nums = [2, 2, 4, 2]

# for num in nums:
#     if num % 2 != 0:
#         print("NOT ALL EVEN")
#         break
# else:
#     print("ALL EVEN")

# for i in range(3):
#     for j in range(3):
#         if j == 2:
#             break
#     else:
#         print("Inner Else")
# else:
#     print("Outer Else")

# # Create a multiplication table
# for i in range(1, 6):  # Outer loop for rows
#     for j in range(1, 11):  # Inner loop for columns
#         print(f"{i * j:4}", end=' ')
#     print()  # Newline after each row


# list1 = ['A', 'B', 'C']
# list2 = [1, 2, 3]

# # Generating combinations
# combinations = []
# for item1 in list1:
#     for item2 in list2:
#         combinations.append((item1, item2))

# print(combinations)

# # Q1.
# # 0,0
# # 0,1
# # 1,0
# # 1,1

# # Q2.
# # The loop runs 2*2 Times
# # Done

# # Q3.
# # 0
# # 1


# #💻 Problem 1 — Pattern (VERY IMPORTANT)

# n=3
# star="*"

# for i in range(n+1):
#     print(i*star)



# #💻 Problem 2 — Multiplication Table

# n=3

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i*j,"")
#     print()

# #💻 Problem 3 — Pair Generation

# list1 = [1, 2]
# list2 = [3, 4]

# for item in list1:
#     for el in list2:
#         print(item*el)

# #💻 Problem 4 — Duplicate Detection (Nested Loop)

# nums = [1, 2, 3, 2]

# for i in range(1,len(nums)+1):
#     for j in range(i+1,len(nums)):
#         if nums[i]==nums[j]:
#             print(f"duplicate found: {nums[i]}")
        

# n=3

# for i in range(1,n+1):
#     print(i*1)

# n = 3

# for i in range(1, n+1):
#     n=n+1
#     for j in range(1,i+1):
#         print(i,end="")
#         n=n+1
#     print()

# 1,2
# 1,2

# for i in range(2):
#     num = 1
#     for j in range(2):
#         print(num, end=" ")
#         num += 1
#     print()

#💻 Problem 1 — Day of Week

# day=3

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalide input")


# #💻 Problem 2 — Simple Calculator

# a=10
# b=5
# op="+"

# match op:
#     case "+":
#         print(a+b)
#     case "-":
#         print(a-b)
#     case "*":
#         print(a*b)
#     case "/":
#         print(a/b)
#     case _:
#         print("Invalide input")

# #💻 Problem 3 — Multiple Match

# char = 'a'

# match char:
#     case "a"|"e"|"i"|"o"|"u"|"A"|"E"|"I"|"O"|"U":
#         print("Vowel")
#     case _:
#         print("Consonant")


# #P1
# nums = [2, 4, 6, 7, 8]

# for num in nums:
#     if num%2!=0:
#         print("First odd number:",num)
#         break


# #P2

# nums = [1, -2, 3, -4, 5]

# for i in nums:
#     if i<0:
#         continue
#     print(i)

# #p3 
# nums = [2, 4, 6, 8]

# for j in nums:
#     if j%2!=0:
#         print("Odd number Found")
# else:
#     print("No odd numbers found")

# #p4

# n=4

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# #p5

# num = 5

# match num:
#     case n if n>0 and n%2==0:
#         print("Even Positive")
#     case n if n>0 and n%2!=0:
#         print("Odd Positive")
#     case n if n<0:
#         print("Negative")
#     case n if n<0:
#         print("Negative")
#     case n if n==0:
#         print("Zero")


# Q1
# P,N
# Q2
# 5
# Q3
# TypeError will occur as strings are immutable

# 💻 Problem 1 — Print Characters

# s="Mahesh"

# for i in s:
#     print(i)

# #💻 Problem 2 — Count Vowels

# s = "python"
# count=0

# for i in s:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
#         count+=1
# print(count)

#💻 Problem 3 — Reverse String (IMPORTANT)

# son = "hello"
# new_s=""



# for i in range(len(son)-1,-1,-1):
#     new_s+=son[i]

# print(new_s)


# 💻 Problem 4 — First Non-Repeating Character

# s = "aabbcde"

# for i in range(0,len(s)):
#     count=0
#     for j in range(0,len(s)):
#         if s[i]==s[j]:
#             count+=1
#     if count==1:
#         print(s[i])
#         break
   
#💻 Problem — Count Characters

# s = "hello"
# printed=""

# for i in range(len(s)):
#     count=0

#     if s[i] in printed:
#             continue
#     for j in range(len(s)):
        
#         if s[i]==s[j]:
#             count+=1
#     printed+=s[i]
    
#     print(f"{s[i]}-->{count}")


# a = [1, 2, 3]
# b = [1, 2, 3]

# print(a is b)
# print(a == b)

# s = "Python"
# print(s[1:4])

#o/p: ytn

# s = "Python"
# print(s[-3:])

# #o/p: hon

# s = "Python"
# print(s[0:10])

# #o/p:Python

# s = "abcdef"
# print(s[::2])

#o/p: ace

# #💻 Problem 1 — First & Last

# s = "Mahesh"

# print(s[0] , s[-1] )

# #💻 Problem 2 — Middle Part

# s = "Python"

# print(s[1:-1])

# #💻 Problem 3 — Reverse String (Using slicing)

# print(s[::-1])

# #💻 Problem 4 — Palindrome Check (IMPORTANT)

# s="madam"


# if s==s[::-1]:
#     print("The given string is Palindrome")
# else:
#     print("Non Palindrome")

# #💻 Problem — Remove First & Last
# s = "Mahesh"

# s=s[1:-1]

# print(s)


#💻 Problem 2 — Remove Spaces

# s = "I love Python"

# for i in s:
#     if i==" ":
#         continue
#     print(i,end="")

#💻 Problem 3 — Check Anagram (IMPORTANT)

# s1 = "listen"
# s2 = "silent"

# for i in s1:
#     if i not in s2:
#         print("Not Anagram")
#         break
# else:
#     print("Anagram")

#💻 Problem 4 — Find First Unique Character

# s = "aabbcdde"

# for i in range(len(s)):
#     count=0

#     for j in range(len(s)):
#         if s[i]==s[j]:
#             count+=1
#     if count==1:
#         print(s[i])
#         break

#💻 Problem 1 — Count Words

# s="i  ove Python   "
# count=0

# for i in range(len(s)):
#     if s[i]!= " " and ( i==0 or s[i-1]==" "):
#         count+=1
# print(count)




# #💻 Problem 3 — Check Anagram (IMPORTANT)

# s1 = "abc"
# s2 = "abb"

# if len(s1)!=len(s2):
#     print("Not ANAGRAM")
# else:
#     Checker=""
#     is_anagram=True
# for i in range(len(s1)):
#     if s1[i] in Checker:
#         continue

#     count1=0
#     for j in s1:
#         if s1[i]==j:
#             count1+=1
#     count2=0
#     for k in s2:
#         if s1[i]==k:
#             count2+=1
#     if count1!=count2:
#         print("Not Anagram")
#         is_anagram=False
#         break
#     Checker+=s1[i]
# if is_anagram:
#     print("ANAGRAM")


#🔥 Problem 1 — Remove Duplicates (Order Matters)

# s = "programming"

# seen=""

# for i in s:
#     if i in seen:
#         continue
#     seen+=i
# print(seen)

# #🔥 Problem 2 — Character with Maximum Frequency

# s = "aabbbbcc"
# max=0
# num=""

# for i in range(len(s)):
#     count=0
#     if s[i] in num:
#         continue
#     for j in s:
#         if s[i]==j:
#             count+=1;
#         # print(s[i],count)
#     if count>max:
#         max=count
#         num=s[i]
# print(max,num)


# #🔥 Problem 3 — Check Substring (IMPORTANT DSA)

# s = "hello world"
# sub = "world"

# found=False

# for i in range(len(s)-len(sub)+1):
#     match=True
#     for j in range(len(sub)):
#         if s[i+j]!=sub[j]:
#             match=False
#             break
#     if match:
#         found=True
#         break

# if found:
#     print("Found")
# else:
#     print("Not Found")


# text = "python programming"
# print(text.upper())       # Outputs: PYTHON PROGRAMMING
# print(text.title())       # Outputs: Python Programming
# print(text.capitalize())


#👉 Remove duplicates using:

#1 Loop logic

# s = "aabbcc"

# seen=""

# for i in range(len(s)):
#     if s[i] in seen:
#         continue
#     seen+=s[i]
# print(seen)
    
# #2Using string method (if possible)

# s = "aabbcc"

# seen="".join(dict.fromkeys(s))

# print(seen)


#💻 Problem 1 — Remove Consecutive Duplicates

#Compare current with previous character

s = "aaabbccdaa"

#👉 Output: abcda


#💻 Problem 2 — Check Palindrome (WITHOUT slicing)

s = "madam"

"""Use two pointers:
start → 0  
end → len(s)-1"""


#💻 Problem 3 — Count Words (Robust)

s = "  I   love   Python  "

#Output : 3

#💻 Problem 4 — Find Longest Word

s = "I love Python programming"

#👉 Output: programming

#Build word manually → compare length

#💻 Problem 5 — String Compression (IMPORTANT DSA)

s = "aaabbc"

#Output: a3b2c1

#Count consecutive characters

#💻 Problem 6 — Check Rotation

s1 = "abcde"
s2 = "cdeab"

#output=Yes

#Try all rotations manually

#💻 Problem 7 — First Repeating Character

s = "abcaed"

#Use seen logic


    

         















#🔹 Q1

def find_max(nums):
    max_val=nums[0]
    for i in nums:
        if i>max_val:
            max_val=i
    return max_val

result=find_max([1,5,8,9,3,2,11,5,3,2])

print(result)

#🔹 Q2

def second_largest(nums):
    max_val=nums[0]
    second_max=float('-inf')
    for i in nums:
        if i>max_val:
            second_max=max_val
            max_val=i
        elif i>second_max and i!=max_val:
            second_max=i
    return second_max

result=second_largest([1,4,5,4,12,7,9,8,10,4,8])

print(result)

#🔹 Q3

def move_zeros(nums):
    # return new list (DO NOT modify original)
    new_list=nums.copy()

    pos=0
    for i in range(len(new_list)):
        if new_list[i]!=0:
            new_list[pos]=new_list[i]
            pos+=1
    for i in range(pos,len(new_list)):
        new_list[i]=0
    
    return new_list

a=[0,1,0,3,12]

print(move_zeros(a))

# 🔹 Q4

def is_palindrome(nums):

    left=0
    right=len(nums)-1
    is_true=True

    while left<right:
        if nums[left]!=nums[right]:
            is_true=False
            break
        left+=1
        right-=1
    return is_true

a=[1,2,3,2,1]

print(is_palindrome(a))

#🔹 Q5 (Important)

def remove_duplicates(nums):
    new_list=[]

    for i in nums:
        found=True
        for j in new_list:
            if i==j:
                found=False
                break
        if found:
            new_list.append(i)
            
        
    return new_list

a=[1,2,2,1,3,4,5,6]

print(remove_duplicates(a))

        


"""
#🧠 Q1
a is a Normal parameter(we call it as positional parameter in function defination)
b is defualt parameter 
*args are the varibale number of positional parameters.
**kwargs are the variable number of keyword parameters.
#🧠 Q2
func(1, 2, 3, 4, x=10, y=20)
a=1 b=2 args={3, 4} kwargs={x:10,y:20} 

🧠 Q3 (VERY IMPORTANT)
When will you use:
*args instead of list parameter? when  the parameeter count is unknown we use *args
🧠 Q4
Why this is useful?
def func(**kwargs):
configuration setting

"""

# 🔥 LEVEL 1 — *args

#🔹 P1

def sum_all(*nums):
    # return sum of all numbers
    result=sum(nums)
    return result

def sum_all(*nums):
    # return sum of all numbers
    result=0
    for i in nums:
        result+=i
    return result

print(sum_all(2,5,6,8,9,15,20))


#🔹 P2

def find_max(*nums):
    # return max
    max_val=nums[0]
    for i in range(1,len(nums)):
        if nums[i]>max_val:
            max_val=nums[i]
    return max_val

print(find_max(2,5,6,8,9,15,20))



#🔥 LEVEL 2 — **kwargs

#🔹 P3

def build_profile(**info):
    result = ""
    for key, value in info.items():
        result += f"{key}:{value} "
    return result.strip()

print(build_profile(name="Mahesh", age=22))

#Here still not undestood the Problem Properly

#🔹 P4

def count_keys(**kwargs):
    # return number of keys
    return len(kwargs)
    

print(count_keys(name="Mahesh", age=22))

#🔹 P5

def func(a, b=5, *args, **kwargs):
    # return:
    # sum of a, b, args + count of kwargs
    total_sum=a+b+ sum(args)+len(kwargs)
    return total_sum

print(func(5,10,15,20,30,c=5,d=10))



#🔹 P6 — Multiply

def multiply_all(*nums):
    if not nums:
        return None
    result=nums[0]
    for i in nums:
        if i==0:
            continue
        result*=i
    return result
print(multiply_all(1,4,5,0,3))

#🔹 P7 — Min Max

def find_min_max(*nums):
    if not nums:
        return None
    max_val=float('-inf')
    min_val=float('inf')
    for i in nums:
        if i>max_val:
            max_val=i
        elif i<min_val:
            min_val=i
    return f"max:{max_val},min:{min_val}"

print(find_min_max(2,5,7,3,1,10,12,11))

def merge_data(*args, **kwargs):
    new_data=list(args)
    for key,value in kwargs.items():
        new_data.append(value)
    return new_data

print(merge_data(10,15,11,12,name="Mahesh",age=18))

#🔹 P9 — Duplicate check (DSA)

def has_duplicate(*nums):
    seen=set()
    for i in nums:
        if i in seen:
            return f"This list Has Duplicate:{i}"
            break
        seen.add(i)
    return f"Has No duplicates"

print(has_duplicate(1,5,2,4,6,3,2))


    
#🔹 P10 — Update list (IMPORTANT)

def update_list(lst, **kwargs):
    #Not able to this what exctly to be done in this problem
    new_list=lst.copy()

    for key,value in kwargs.items():
        index=int(key[1:])
        new_list[index]=value
    return new_list

update_list([5,6,7,8], i1=100, i3=200)


pairs = [(1,3), (2,1), (4,2)]

print(sorted(pairs, key=lambda x: x[1]))


#Lamda Function 
"""
Q1.8
Q2.[2,4,6]
Q3.[3,4]
Q4.[(2,1),(4,2),(1,3)]

"""
#🔥 LEVEL 1

#🔹 P1

nums = [1,2,3,4]

square=list(map(lambda x: x**2 ,nums))

print(square)

#🔹 P2

nums = [5,10,15,20]

filtered_nums=list(filter(lambda x: x>10,nums))

print(filtered_nums)

#🔥 LEVEL 2

#🔹 P3

pairs = [(1,5), (2,3), (4,7)]

sorted_pairs=list(sorted(pairs,key=lambda x:sum(x)))

print(sorted_pairs)

#🔹 P4

words = ["apple", "banana", "kiwi"]

# sort by length

sorted_len=list(sorted(words,key=lambda x:len(x)))

print(sorted_len)

#🔥 LEVEL 3 (IMPORTANT)

#🔹 P5

nums = [1,2,3,4,5]

result=list(map(lambda x:(x,x**2),nums))

print(result)

#explian the Problem Properly what you want still not understood 


#🧠 Q

nums = [1,2,3]

result = list(map(lambda x: x+10 if x%2==0 else x, nums))

# [1,12,3]

print(result)


nums = [1,2,3]
result = list(map(lambda x: (x, x%2==0), nums))

print(result)


def func(n):
    if n == 1:
        return 1
    return func(n-1)

print(func(5))



"""
#🧠 First question (NO coding)
1.Base case its a stoping condition for the recurstion.
2.Recursive case where the the function calls it self to sovle smaller part of the problem 
3.Visualization to understand how recurstion works.
#🔹 Q1
The func Functions computes the sum of the n natural numbers and returns the sum 
#🔹 Q2 (VERY IMPORTANT)
If we remove base case the recursive functions will call itslef indefinte time tjis cas lead to stack overflow.
#🔹 Q3
1 (Prev i thought it shoud be 0 but later understood)
#🔥 3. DRY RUN (CRITICAL)

fact(3)  #n==3
        fact(2) #n==1
                fact(1)  #n==1
                        fact(0) # Retuns 1



3    *  2    *  1    *   1 = 6   


#🔥 4. THINKING TEST (MOST IMPORTANT)

#🔹 Q5

👉 Why is recursion sometimes slow?

Due to its recursive nature it calls itself untill it reches the base case therefore its Slow computing all these calls takes time

#🔹 Q6

👉 When should you NOT use recursion?

for non hierarchical problems and wherever there shoud be memory contraints recursion is not efficient.


"""
#🔹 P1 — Sum of N

def sum_n(n):
    if n==0:
        return 0
    return n + sum_n(n-1) 

print(sum_n(10))

def reverse_string(s):
    if len(s)==-1:
        return None
    return 

print(reverse_string("abc"))




#🔥 P2 — Reverse String (VERY IMPORTANT)

def reverse_string(s):
    if len(s)==1:
        return s
    return reverse_string(s[1:])+s[0]

print(reverse_string("abcd"))
    

#🔥 P3 — Count Digits

def count_digits(n):
    if n==0:
        return 0
    return count_digits(n//10)+1

print(count_digits(12345))

print(1//10)



def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(6))


#🔹 1. Sum of Digits

def sum_digits(n):

    if n<10:
        return n
    return (n%10)+sum_digits(n//10)

print(sum_digits(1235))


#🔹 3. Power Function

def power(x, n):
    if n==0:
        return 1
    return x * power(x,n-1)

print(power(2, 3))


#🔹 5. Print Numbers (Backtracking thinking)

def print_reverse(n):
    if n==0:
        return 
    print(n)
    return print_reverse(n-1)

print_reverse(5)


#🔹 2. Check Palindrome (String)

def is_palindrome(s):
    if s=="" or len(s)==1:
        return True
    return s[0]==s[-1] and is_palindrome(s[1:-1])

print(is_palindrome("hello"))


#🔹 4. Count Occurrences in List

def count_occ(arr, target):
    if len(arr)==0:
        return 0
    count=0
    if arr[0]==target:
        count+=1
    return count + count_occ(arr[1:],target)



def outer(x):
    def inner():
        return x
    return inner

f = outer(10)
print(f())


"""

🔹 P1 — Basic Closure
1.10
2.if we chnage the value of x after difinig inner the output x will show the same value of x we deaclaired in outer even we pass any argument value for x.
🔹 P2 — Closure with Operation
def make_multiplier(n):
    def multiply(x):
        return x*n
    return multiply

double = make_multiplier(2)
print(double(5))   # expected 10
return x*n
🔹 P3 — Counter (IMPORTANT)
def counter():
    count = 0
    
    def inc():
        nonlocal count
        count+=1
        return count
    
    return inc

🔹 P4 — Closure Trap (VERY IMPORTANT)
funcs = []

for i in range(3):
    def f():
        return i
    funcs.append(f)

for f in funcs:
    print(f())

    Not understood this concept properly explain in detail

🔹 P5 — Basic Decorator

def decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@decorator
def greet():
    print("Hello")

greet()

Start
Hello
End


🔹 P6 — Decorator with Return

def decorator(func):
    def wrapper():
        result = func()
        return result * 2
    return wrapper

@decorator
def get_num():
    return 5

print(get_num())

10

🔹 P7 — Decorator with Arguments (IMPORTANT)

def decorator(func):
    def wrapper(a, b):
        return func(a, b) + 10
    return wrapper

@decorator
def add(a, b):
    return a + b

print(add(2,3))

15

🔹 P8 — Logging Decorator (REAL USE)

def log(func):
    def wrapper(*args, **kwargs):
        print("Calling function")
        result = func(*args, **kwargs)
        print("Done")
        return result
    return wrapper

@log
def multiply(a, b):
    return a * b

print(multiply(3,4))

Calling function
Done
12


🔹 P9 — Closure + Decorator Thinking

def outer(x):
    def decorator(func):
        def wrapper(y):
            return func(y) + x
        return wrapper
    return decorator

@outer(5)
def test(n):
    return n * 2

print(test(3))

11






"""


"""Dict


Q1 Why is dictionary faster than list for searching?

the dictionar contails the sequence of key value pairs so with kea dict can fast lookup using the hashing table where as in list we have to iterate through each item.

Q2 When will d[key] give error?How does get() solve it?

if the key doesn't exist in dict the python throughs keyerror to solve this we can use get() method if key doesnt exist then it will not raise error. Handles safely and retuns with default value if any

Q3 If key already exists:
d[key] = new_value
What happens?

Here d[key]=new_value is updating the new_value to existing key.

Q4
Difference between:
for key in d
vs
for key, value in d.items()

The first loop is will retund only the keys in dict whereas the second loop with .items() functions it will return both keys and values associted with in the dict.
"""

#Problem 1: Frequency Count

arr = [1,2,2,3,1,1,4]
freq={}

for i in arr:
    freq[i]=freq.get(i,0)+1   #Specific this line not undesrtood 
print(freq)

#But how it works not understood yet i was seen same problem while reading thats how i solved this 

#Problem 2: Character Count

s = "banana"
char={}

for i in s:
    char[i]=char.get(i,0)+1
print(char)

#Problem 3: Check Key Exists (NO get())

d = {1:10, 2:20}
key = 3

print(d.get(3,"Not Found"))
# print(d[key]) #raise a keyError

#🔥 LEVEL 2 — LOGIC BUILDING


#Problem 4: Find Duplicate Element

arr = [1,2,3,4,2]
seen={}

for i in arr:
    if i in seen:
        print(i)
        break
    seen[i]=seen.get(i,0)+1

#Problem 5: First Non-Repeating Element

arr = [1,2,2,3,1,4]

#Problem 5: First Non-Repeating Element

arr = [1,2,2,3,1,4]

new_list={}

for i in arr:
    new_list[i]=new_list.get(i,0)+1

for key, value in new_list.items():
    if value==1:
        print(key)
        break

#Problem 6: Remove Element Using pop()

d = {1:10, 2:20, 3:30}

item_key=d.pop(2,"Key not Found")

print(item_key)
print(d)

#🔥 LEVEL 3 — METHODS USAGE (IMPORTANT)

#Problem 7: Safe Access

d = {"a":1, "b":2}

#👉 Access key = "c" without error

access_key=d.get("c","Key Not Found")

print(access_key)

#Problem 8: Merge Dictionaries

d1 = {1:10, 2:20}
d2 = {2:200, 3:30}

d1.update(d2)
print(d1)

#Problem 9: Print All Key-Value Pairs

d = {1:10, 2:20}

for key, value in d.items():
    print(key,value)


#🔥 Challenge 1 (VERY IMPORTANT)

#Modify your duplicate problem:
arr = [1,2,3,2,4,3,5]

seen={}

for i in arr:
    if i in seen:
        seen[i]+=1
    else:
        seen[i]=1

for key,value in seen.items():
    if value>1:
        print(f"{key} is duplicate in list {value} times")

#🔥 Challenge 2

arr = [1,2,2,3,3,4,4,4]

seen={}

for i in arr:
    if i in seen:
        seen[i]+=1
    else:
        seen[i]=1
max_val=0
max_key=None

for key,value in seen.items():
    if value>max_val:
        max_val=value
        max_key=key
print(max_key,max_val)



   
#🔥 Challenge 3 (INTERVIEW LEVEL START)

arr = [2,7,11,15]
target = 9
seen={}

for i in range(len(arr)):
    needed=target-arr[i]
    if needed in seen:
        print(seen[needed],i)
    seen[arr[i]]=i

    
#🔥 PROBLEM 4 — FIRST UNIQUE CHARACTER

s = "aabbcde"
seen={}
for i in s:
    if i in seen:
        seen[i]+=1
    else:
        seen[i]=1

for key,value in seen.items():
    if value==1:
        print(key)
        break

#🔥 PROBLEM 5 — INTERSECTION OF ARRAYS

# a = [1,2,2,1]
# b = [2,2]






#🔥 PROBLEM 6 — REMOVE DUPLICATES (KEEP ORDER)

arr = [1,2,2,3,1,4]
seen={}
result=[]

for i in range(len(arr)):
    if arr[i] not in seen:
        seen[arr[i]]=1
        result.append(arr[i])
print(result)


a = [3,3,3,1,2,2]
b = [3,3,1,2,2,3,3]
seen={}
result=[]
for i in a:
    if i in seen:
        seen[i]+=1
    else:
        seen[i]=1

for i in b:
    if i in seen and seen[i]>0:
        result.append(i)
        seen[i]-=1
print(result)





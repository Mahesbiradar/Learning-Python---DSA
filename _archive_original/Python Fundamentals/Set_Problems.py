#🔥 LEVEL 1 — BASIC CHECK

#🔹 Q1
s = {1,2,2,3}
print(s)
#👉 Output?

#ans:{1,2,3} 

#🔹 Q2
s = {}
print(type(s))

#why

#ans: <class 'dict'> Bcz creating the empty curly barces can be Dict type to declaire set we can use set() constructor. or we have to add elements if we are using {} 

#🔹 Q3
s = set([1,2,3])
s.add(2)
print(s)

#ans {1,2,3} the newly added element is alredy exist in set Therefor the element will be not added bcz its duplicate.

#🔹 Q4

s = {1,2,3}
# s.remove(5)

#s = {1,2,3}
# Python will through an key error the element we are removing not exist in the set.


#🔹 Q5
s = {1,2,3}
# s.discard(5)
print(s)

#👉 Why no error?

#ans: Bcz the discard() method is bulil to handle teh edgecases if any element not found the set still the dicard() method not through the Error.

#🧠 LEVEL 2 — CONCEPT / INTERVIEW

#🔹 Q6 Why is membership check (in) faster in sets than lists?

#ans: the operation is efficient and runs in constatnt time therefor faster than the set. If you want to add something it will be appriciated.

#🔹 Q7 Why can’t we store a list inside a set?

#ans: bcz list can contains the duplicate elements while set is made to store only unique elements.

# 🔹 Q8 Difference between:# remove() vs discard()

# The remove() function is to remove the given element in a set and if the item not exists in set it will through an error Where as discard() function does same thing but it handles the edgecases.

#🔹 Q9 What is the difference between:set() vs frozenset()

#ans: set() is unordered mutable data type where we can modify the elements of the set. frozenset() is immutable data type which means once it created cant be modified. 

#🔹 Q10 When should you prefer set over list?

#Set data type is used in application where only unique elements to be stored.

#🚀 LEVEL 3 — SET OPERATIONS (IMPORTANT)   
# 🔹 Q11 — Union  (👉 Output of: a | b)  

a = {1,2,3}
b = {3,4,5}

#ans: {1,2,3,4,5}

#🔹 Q12 — Intersection (👉 Output: a & b)

#ans: {3}

#🔹 Q13 — Difference (👉 Output:a - b)

#ans: {1,2}

#🔹 Q14 — Symmetric Difference(👉 Output:a ^ b)

#ans:{1,2,4,5}

#🔹 Q15 — Subset Check

a = {1,2}
b = {1,2,3}

#👉 What is:

#ans: True

#🚀 LEVEL 4 — DSA USING SETS (IMPORTANT)

#🔹 Q16 — Remove Duplicates (Optimized)

nums = [1,2,2,3,4,4,5]

new_set=set(nums)

print(new_set)

#🔹 Q17 — Check Duplicate Exists

nums = [1,2,3,4,1]
seen=set()

#👉 Return True if duplicate exists

for i in nums:
    if i in seen:
        print(True)
        break    
    seen.add(i)


#🔹 Q18 — Find Common Elements

a = [1,2,3,4]
b = [3,4,5,6]
common=[]

for i in a:
    for j in b:
        if i==j:
            common.append(i)
print(common)   

#🔹 Q19 — Find Missing Number (Optimized)

#👉 Use set to find missing

nums = [1,2,4,5]
n=len(nums)+1
set_a=set(range(1,n+1))
set_b=set(nums)

print(set_a)

print(list(set_a-set_b))



#🔹 Q20 — First Non-Repeating Element

# nums = [1,2,2,3,1,4]

# for i in nums:
#     count=0
#     for j in nums:
#         if i==j:
#             count+=1
#     if count==1:
#         print(i)
#         break

nums = [1,2,2,3,1,4]

freq = {}

# Step 1: Count frequency
for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1


# Step 2: Find first non-repeating
for i in nums:
    if freq[i] == 1:
        print(i)
        break
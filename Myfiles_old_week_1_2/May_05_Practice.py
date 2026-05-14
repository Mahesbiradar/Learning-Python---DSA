
#🔥 LEVEL 1 — BASIC
#Q1
arr = [1,2,3,4]
#👉 Create:
#{1:2, 2:4, 3:6, 4:8}

mul_x={x:x*2 for x in arr}

print(mul_x)

#Q2

s = "abc"

convert_str={x:ord(x) for x in s}

print(convert_str)

#🔥 LEVEL 2 — WITH CONDITION

#Q3

arr = [1,2,3,4,5,6]

#👉 Only even numbers: {2:4, 4:16, 6:36}

even_num={x:x*x for x in arr if x%2==0}

print(even_num)

#🔥 LEVEL 3 — THINKING

#Q4

arr = [1,2,2,3]

#👉 What happens if you do: {i:i*i for i in arr}

#{1: 1, 2: 4, 3: 9}

#💬 QUICK CHECK FOR YOU

#Answer this:

arr = [1,2,2,3]
d = {i:i+1 for i in arr}

#{1: 2, 2: 3, 3: 4}

# Counter

#🔥 Q1 — Basic

from collections import Counter

s = "aabbccc"

count_occ=Counter(s)
most_common=count_occ.most_common()
print(most_common)

print(count_occ)

#🔥 Q2 — Compare

#1. Using dictionary

arr = [1,2,2,3,3,3]
seen={}
max_val=0
max_key=None

for i in arr:
    if i in seen:
        seen[i]+=1
    else:
        seen[i]=1
print(seen)

for key,value in seen.items():
    if value>max_val:
        max_val=value
        max_key=key
print([max_val,max_key])

#2. Using Counter

arr = [1,2,2,3,3,3]

c=Counter(arr)

# max_val=c.most_common(1)
key, val = c.most_common(1)[0]


print((key, val))



#🔥 Q3 — Logic Thinking

a = [1,1,2]
b = [1,1,1,2]

seen=Counter(a)
result=[]

for i in b:
    if i in seen and seen[i]>0:
        result.append(i)
        seen[i]-=1
print(result)


# t = (1,2,3)
# t[0] = 10



#🔹 Q11 — Swap Using Tuple
a= (5,)
b=(10,)

a, b = b, a

print(a,b)


#🔹 Q12 — Return Multiple Values

#till now i have not finished the functions in Python fundamentals


#🔹 Q13 — Pair Processing
pairs = [(1,2), (3,4), (5,6)]

for x,y in pairs:
    print(x+y)

#Find Min Sum Pair

pairs = [(1,5), (2,3), (4,7)]

min_value=float('inf')
result=None

for x,y in pairs:
    if x+y<min_value:
        min_value=x+y
        result=(x, y)
print(result)





#🔹 Q15 — Count Frequency Using Tuples
nums = [1,2,2,3]

result=[]

for i in nums:
    count=0

    for j in nums:
        if i==j:
            count+=1
    pairs=(i, count)
    
    if pairs not in result:
        result.append(pairs)
print(result)


#🔹 Q16 — Nested Tuple Access

t = ((1,2),(3,4))

print(t[1][1])


# t = (10, 20, 30, 40)

# count=0
# for i in t:
#     print(i)
#     count+=1

# print(count)

# t = (1, 2, 3, 4)
# x = 3

# print(x in t)

# max=t[0]

# for i in t:
#     if i>max:
#         max=i
# print(i)

# # left=0
# # right=len(t)-1

# # while left<right:
# #     t[left],t[right]=t[right],t[left]
# #     left+=1
# #     right-=1
# # print(t)


# #5. Reverse tuple (NO slicing)
# t = (1, 2, 3, 4)
# new_t=()

# for i in t:
#     new_t=(i,) + new_t
# print(new_t)

# #6. Count occurrences (NO count())

# t = (1, 2, 3, 4, 2)
# target=2
# count=0
# for i in t:
#     if i==target:
#         count+=1
# print(count)

# #🔹 7. Remove Duplicates (NO built-in)


# t = (1, 2, 2, 3, 1)
# new=()

# for i in t:
#     found=False

#     for j in new:
#         if i==j:
#             found=True
#             break
#     if not found:
#         new=new + (i, )

# print(new)

# #🔹 8. Merge Two Tuples (NO direct +)

# t1 = (1, 2)
# t2 = (3, 4)

# merged = ()

# for i in t1:
#     merged= merged + (i, )
# for j in t2:
#     merged= merged + (j, )

# print(merged)

# # 🔹 9. Second Largest Element

# t = (5, 1, 8, 3, 8)

# first=second=float('-inf')

# for i in t:
#     if i > first:
#         second=first
#         first=i
#     elif i > second and i!=first:
#         second=i

# print(second)

#1. Swap two numbers using unpacking

a=10
b=15
a, b=b, a
print(a,b)

#2.2. Unpack and print

t = (10, 20, 30)

x,y,z=t

print(f"x:{x},y:{y},z:{z}")

#3. Loop unpacking

pairs = [(1,2), (3,4), (5,6)]

a,b,c=pairs

print(sum(a))
print(sum(b))
print(sum(c))

#4. Ignore middle value
t = (1, 2, 3)
# print only first and last

a,_,b=t

print(a,b)

#5. Use * unpacking

t = (1, 2, 3, 4, 5)
# first, middle(list), last

a,*b,c=t
print(f"a={a},b={b},c={c}")

#6. Nested unpacking

t = ((1,2), (3,4))
# print 1 2 3 4

((x1,y1),(x2,y2))=t

print(x1,y1,x2,y2)

#🧠 Quick Fix Exercise (Do Now)
pairs = [(2,3), (4,5), (6,7)]

for a,b in pairs:
    print(a*b)

#Q1:
a, b = (1, 2)
a = a + b
print(a, b)

#a=3,b=2

#Q2:
a, *b = (1, 2)
print(b)
#b=[2]

#Q3:

for x, y in [(1,2,3), (4,5,6)]:
    print(x, y)

#Value error To many values to unpack 
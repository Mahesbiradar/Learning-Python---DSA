# """

# 1. Add 3 elements at end
# 2. Remove last element
# 3. Count occurrences of 2
# 4. Sort list descending
# 5. Copy list and modify copy (check original unchanged)


# """


# # 1. Add 3 elements at end

# Names=["Mahesh","Suresh","Rahul"]

# Names.extend(["Prem","Surya","Ramesh"])

# print(Names)

# #2. Remove last element

# Names=["Mahesh","Suresh","Rahul"]

# removed=Names.pop()
# print(removed)
# print(Names)

# #3. Count occurrences of 2

# Names=["Mahesh","Suresh","Rahul","Rahul","Suresh"]

# occurance=Names.count("Suresh")

# print(occurance)

# #4. Sort list descending

# Names=["Mahesh","Suresh","Rahul","Rahul","Suresh"]

# sorted_list=Names.reverse()

# print(Names)


# #5. Copy list and modify copy (check original unchanged)

# Names=["Mahesh","Suresh","Rahul","Rahul","Suresh"]

# copied_list=Names.copy()

# copied_list.pop()

# print(copied_list)
# print(Names)



# a = [1,2,3]
# b = a

# b.append(4)

# print(a)


#🔹 1. Square Only Positive Numbers

nums = [-2, -1, 0, 1, 2]
# Output: [1, 4]

positive_nums=[x**2 for x in nums if x>0]

print(positive_nums)

#🔹 2. Flatten and Filter

matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [2,4,6,8]

flatten_list=[item for row in matrix for item in row if item%2==0]

print(flatten_list)

#🔹 3. Find Common Elements

a = [1,2,3,4]
b = [3,4,5,6]
# Output: [3,4]

common_el=[x for x in a for y in b if x==y ]

print(common_el)

#🔹 4. Count Words Starting with 'a'

words = ["apple", "banana", "avocado", "grape"]
# Output: 2

count=0

for i in words:
    if i[0]=="a":
        count+=1
print(count)
    
#🔹 5. Matrix Row Sum

matrix = [[1,2],[3,4],[5,6]]
# Output: [3,7,11]

mat_sum=[]

for i in matrix:
    sum=0
    for j in i:
        sum+=j
    mat_sum.append(sum)

print(mat_sum)
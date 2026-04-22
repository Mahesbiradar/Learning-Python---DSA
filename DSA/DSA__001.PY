#🔹 1. Print All Elements

nums = [1,2,3,4,5]

#Here we have list of integers in the input and the o/p is expected to print each element.
#Basically i have to access each elemet in a list and print so ill run a loop over a list and then print each element.

for i in nums:
    print(i)


#🔹 2. Find Maximum Element

nums = [3,7,2,9,5]

#In input we have given a list of int and we have to find the Maximum number in the list.
#So first ill take one variable as max and store the first index value of list.
#Then ill run loop one each element in list to compare the max num if the iteration is > than the max then will store the iterable value to Max and continues comparison until the loop ends.

#Iteration 1->i=3 max=3 i>max condiation fails 
#iteration 2->i=7 max=3 i>max? true so max=7
#iteration 3->i=2 max=7 i>max? false
#iteration 3->i=9 max=7 i>max?true so max=9
#iteration 4->i=5 max=9 i>max?true 
#Loop finished and we found the max element in list.

#Code

max=nums[0]

for i in nums:
    if i>max:
        max=i
print(max)

#🔹 3. Find Minimum Element

nums = [3,7,2,9,5]

#The approch willbe  same similar to last question we solved with chnages in flitering here will find the min num

max=nums[0]

for i in nums:
    if i<max:
        max=i
print(max)


#🔹 4. Count Even Numbers

nums = [1,2,3,4,5,6]
# Output: 3


#in this problem the input and the output is given and we have to check the even numbers in list and then we have to print the count of even nums

#will take one variable to fo count the even nums and will run a loop over a list and  check each element wheather its divisible by two if the condition satisfies will incremnt the count by 1

#iteration 1->i=1 count=0 i%2==0? false
#Iteration 2->i=2 count=0 i%2==0? true count+=1
#iteration 3->i=3 count=1 i%2==0? false
#iteration 4->i=4 count=1 i%2==0? true count+=1
#iteration 5->i=5 count=2 i%2==0? false
#Iteration 6->i=6 count=2 i%2==0? true count+=1  so finally loop ends and  count=3 

count=0

for i in nums:
    if i%2==0:
        count+=1
print("Output: ",count)

#🔹 5. Check Element Exists

nums = [1,2,3,4,5]
target = 3
# Output: True

#Basically we have list of integers and the target is give and i have to check the target exist in a list or not  and will take one variable to check the condition.

#Here also will run a loop over list and compares ech element value with target value if found will exit the code and return the bool true

#is_true=false
#iteration 1->i=1  target = 3  i==target?  false
#Iteration 2->i=2  target = 3  i==target?  false
#iteration 3->i=3  target = 3  i==target?  true is_true=True will break the loop and exit the program

is_true=False

for i in nums:
    if i==target:
        is_true=True
        break
print(is_true)


#🔹 6. Sum of All Elements

nums = [1,2,3,4]

# Output: 10

#Here we have a list of int and we need to make a sum of all the element in the list.

#will take one varibale as total_sum and will run a loop over the list and adds the each element value to the sum variable and prints the total_sum.

#Here ill not do dry run as time is not enough

total_sum=0

for i in nums:
    total_sum+=i

print(total_sum)



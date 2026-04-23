#🔹 4. Check Palindrome Array

nums = [1,2,3,2,1]
# Output: True

#Here will solve this with two pointer approach will take two variable first and last will compare them if matches will move pointers Towards centre

#Steps 1.intialize two two pointer one staring from intial index and one more start from last index 2. Run a loop over list whenever a condition fails exit the loop or will compare all elemets untill the mid.


left=0
right=len(nums)-1
is_true=True

while left<right:
    print(is_true)
    if nums[left]!=nums[right]:
        is_true=False
        break
    else:
        left+=1
        right-=1

print(is_true)    
  


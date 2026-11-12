# New


"""
6	-	480	-	Sliding Window Median	-	Two Heaps	-	Median stream
7	-	502	-	IPO	-	Two Heaps	-	Median stream

"""



import heapq


heap = []

heapq.heappush(heap,20)
heapq.heappush(heap,10)
heapq.heappush(heap,30)
heapq.heappush(heap,5)

print(heap)


smallest = heapq.heappop(heap)

print(smallest)

print(heap)


# 1	-	215	-	Kth Largest Element in an Array	-	Min/Max Heap	-	Top K / Kth largest



import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        
        min_heap = []

        for num in nums:

            heapq.heappush(min_heap,num)

            if len(min_heap) > k:

                heapq.heappop(min_heap)
        
        return min_heap[0]


# Status: Independent
# Time Taken: 10 m 
# Time Complexity: O(N log k) for processing each num in list O(log k) so overall O(n log k) 
# Space Complexity: O(k)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: min/max heap
# Variant:min heap
# Mistakes / Confusion:Na



# 4	-	1046	-	Last Stone Weight	-	Min/Max Heap	-	Top K / Kth largest


import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        
        max_heap = []

        for num in stones:

            heapq.heappush(max_heap,-num)
        
        while len(max_heap) > 1:

            first = heapq.heappop(max_heap)

            second = heapq.heappop(max_heap)

            diff = first - second

            if diff != 0:

                heapq.heappush(max_heap,diff)
        
        if max_heap:

            return -max_heap[0]
        
        return 0


# Status: Worked myself but small hints were needed
# Time Taken: 15 m 
# Time Complexity: O(n log n) - O(n log n) to build the heap + O(n log n) for the reduction loop
# Space Complexity: O(n) - to store the max_heap array
# Submitted to LC: Yes
# Result: Accepted


# 3	-	973	-	K Closest Points to Origin	-	Min/Max Heap	-	Top K / Kth largest


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        
        max_heap = []


        for nums in points:

            x = nums[0]

            y = nums[-1]

            distance = x**2 + y ** 2

            heapq.heappush(max_heap,(-distance,x,y))

            if len(max_heap) > k:

                heapq.heappop(max_heap)
        
        result = []

        for items in max_heap:

            ditance , x , y = items

            result.append([x,y])

        return result

# Status: Independent
# Time Taken: 15m 
# Time Complexity: For maxheap processing all n list in points O(nlogk) max k lists are pushed and poped in heapq and processing result took O(k) 
# Space Complexity: O(k)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: min/max heap
# Variant:min heap
# Mistakes / Confusion:Na



# 2	-	703	-	Kth Largest Element in a Stream	-	Min/Max Heap	-	Top K / Kth largest


class KthLargest:

    def __init__(self, k: int, nums: list[int]):

        self.minheap = []

        self.k = k

        for num in nums:

            heapq.heappush(self.minheap,num)

            if len(self.minheap) > k:

                heapq.heappop(self.minheap)        

    def add(self, val: int) -> int:

        k = self.k

        heapq.heappush(self.minheap,val)

        if len(self.minheap) > k:

                heapq.heappop(self.minheap)
        
        return self.minheap[0]



# Status: Independent
# Time Taken: 15m 
# Time Complexity: intially intantiating the min heap takes O(nlogk) and then while add operation O(logk)  
# Space Complexity: O(k)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: min heap
# Variant:
# Mistakes / Confusion:Na


# 8	-	1962	-	Remove Stones to Minimize the Total	-	Two Heaps	-	Median stream


import heapq
class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        
        max_heap = [-num for num in piles]

        heapq.heapify(max_heap)

        for _ in range(k):

            num = -(heapq.heappop(max_heap))

            new_num = (num//2) + (num%2)

            heapq.heappush(max_heap,-new_num)
          
        return -sum(max_heap)



# Status: Independent
# Time Taken: 20m 
# Time Complexity: O(n+klogn)  
# Space Complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: min heap
# Variant:
# Mistakes / Confusion:Na



# 5	-	295	-	Find Median from Data Stream	-	Two Heaps	-	Median stream



class MedianFinder:

    def __init__(self):

        self.lower = []
        self.upper = []
        

    def addNum(self, num: int) -> None:

        if not self.lower or num <= -self.lower[0]:   # Here initailly i forgot to compare the self.lower[0]  as -self.lower[0] 

            heapq.heappush(self.lower,-num)
        
        else: 

            heapq.heappush(self.upper,num)
        

        if len(self.lower) > len(self.upper) + 1:

            new_num = -(heapq.heappop(self.lower))

            heapq.heappush(self.upper,new_num)
        
        if len(self.upper) > len(self.lower):

            new_num = heapq.heappop(self.upper)

            heapq.heappush(self.lower,-new_num)

        
    def findMedian(self) -> float:

        if len(self.lower) != len(self.upper):

            result = -self.lower[0]

            return result
        else:

            low = -self.lower[0]
            high = self.upper[0]

            result = (low+high)/2

            return result


# Status: Independent
# Time Taken: 20m 
# Time Complexity: O(nlogn)  
# Space Complexity: O(n)
# Submitted to LC: Yes
# Result: Accepted
# Pattern: min and max heap 
# Variant:
# Mistakes / Confusion:Na



# Revision

# 1  Path Sum	112


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        
        if not root:

            return False
        
        targetSum -= root.val

        if not root.left and not root.right:

            if targetSum == 0:

                return True 
        
        return (self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum))



# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n) worst case where n = number nodes in tree   
# Space Complexity: O(n) worst case recursion call stack
# Submitted to LC: Yes
# Result: Accepted
# Pattern: tree dfs
# Variant: path sum
# Mistakes / Confusion:Na


#2 Path Sum II	113	Tier-3



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        
        path = []

        result = []


        def dfs(node,remaining):

            if not node:

                return 

            path.append(node.val)
            
            if not node.left and not node.right:

                if node.val == remaining:

                    result.append(path.copy())
            
            else:

                remaining -= node.val

                dfs(node.left,remaining)

                dfs(node.right,remaining)
            
            path.pop()

        
        dfs(root,targetSum)

        return result


# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n) 
# Space Complexity: O(n)  what will be the space in worst case 
# Submitted to LC: Yes
# Result: Accepted
# Pattern: tree dfs
# Variant: path sum
# Mistakes / Confusion:Na


# 3 Path Sum III	437	Tier-3	29-Oct


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        

        count = 0

        prefix = 0

        seen = {0:1}

        def dfs(node):

            if not node:

                return 

            nonlocal prefix, count
            
            prefix += node.val

            needed = prefix - targetSum

            if needed in seen:

                count += seen[needed]
            
            seen[prefix] = seen.get(prefix,0)+1

            dfs(node.left)

            dfs(node.right)

            seen[prefix] -= 1

            prefix -= node.val

        dfs(root)

        return count


# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(n) 
# Space Complexity: O(n)  what will be the space in worst case 
# Submitted to LC: Yes
# Result: Accepted
# Pattern: tree dfs
# Variant: path sum
# Mistakes / Confusion:Na



# 4 Count Good Nodes in Binary Tree	1448	Tier-3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        count = 0

        def dfs(node,max_seen):

            if not node:

                return 

            nonlocal count
            
            max_seen = max(max_seen,node.val)

            if max_seen == node.val:

                count +=1

            dfs(node.left,max_seen)

            dfs(node.right,max_seen)

        dfs(root,float('-inf'))

        return count        


# Status: Independent
# Time Taken: 15m 
# Time Complexity: O(n) 
# Space Complexity: O(h) in worst case O(n) dfs call stack 
# Submitted to LC: Yes
# Result: Accepted
# Pattern: tree dfs
# Variant: good nodes
# Mistakes / Confusion:Na



# 1 Island Perimeter	463	Tier-1



class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        

        rows, cols = len(grid),len(grid[0])

        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        perimeter = 0

        def dfs(r,c):

            nonlocal perimeter

            for dr, dc in directions:

                nr = r + dr

                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:

                    perimeter -= 1
        

        for r in range(rows):

            for c in range(cols):

                if grid[r][c] == 1:

                    perimeter += 4

                    dfs(r,c)
        
        return perimeter



# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(R*C)  Where each cell is visited once and its 4 nebours.
# Space Complexity: O(R*C) Max in worst case for dfs stack call
# Submitted to LC: Yes
# Result: Accepted
# Pattern: greed traversal
# Variant: 
# Mistakes / Confusion:Na



# Sliding Window Median	480



import heapq

def medianSlidingWindow(nums: list[int], k: int) -> list[float]:

    # Helper Function for removing the expired roots

        def prune(heap,is_max_heap ):

            while heap:

                num = -heap[0] if is_max_heap else heap[0]

                if num in delayed:

                    heapq.heappop(heap)

                    delayed[num] -= 1

                    if delayed[num] == 0:

                        del delayed[num]
                else:

                    break

    
        delayed = {}

        lower = []  #max heap

        upper = []  #min heap

        len_lower = 0

        len_upper = 0

        left = 0

        result = []

        for i in range(len(nums)):

            # Adding the new elements in the heaps
            # prune(lower,True)

            if not lower or nums[i] <= -lower[0]:

                heapq.heappush(lower,-nums[i])

                len_lower += 1
            else:
                heapq.heappush(upper,nums[i])

                len_upper += 1

            # Identify the expired element.

            if i - left + 1 > k:

                delayed[nums[left]] = delayed.get(nums[left],0)+1


                if lower and nums[left] <= -lower[0]:

                    len_lower -= 1

                else:

                    len_upper -= 1

                left += 1


            
            # Balance the heaps.

            if len_lower > len_upper + 1:

                num = heapq.heappop(lower)

                len_lower -= 1

                heapq.heappush(upper,-num)

                len_upper += 1

                prune(lower,True)
                

            

            if len_upper > len_lower:

                num = heapq.heappop(upper)

                len_upper -= 1

                heapq.heappush(lower,-num)

                len_lower += 1

                prune(upper,False)

           
            #Calculate the median
            prune(lower,True)
            
            prune(upper,False)

            if i + 1 >= k:

                
                if len_lower == len_upper:

                    median = (upper[0] - lower[0])/2
                elif len_lower > len_upper:

                    median = float(-lower[0])

                result.append(median)

        return result


print("Running the LC 480")





               











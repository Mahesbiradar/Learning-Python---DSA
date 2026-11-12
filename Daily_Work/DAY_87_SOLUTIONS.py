# DAY 87
# Status:
# Time Taken:
# Time Complexity:
# Space Complexity:
# Submitted to LC:
# Result:
# Pattern:
# Variant:
# Mistakes / Confusion:


"""
9	-	1905	-	Count Sub Islands	-	Tier-1
10	-	1254	-	Number of Closed Islands	-	Tier-1
11	-	417	-	Pacific Atlantic Water Flow	-	Tier-1

"""


# 1	-	695	-	Max Area of Island	-	Tier-1

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        def dfs(r, c):

            grid[r][c] = 0

            count = 1

            for dr, dc in directions:

                nr = r + dr

                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:


                    count += dfs(nr,nc)

            return count
        
        max_area = 0

        for r in range(rows):

            for c in range(cols):

                if grid[r][c] == 1:

                    area = dfs(r,c)
                    
                    max_area = max(max_area,area)

        return max_area


# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(R*C), dfs visits all connected cell and its four nebours (4R*C), outer loop visites all the cells(R*C) 
# Space Complexity: O(R*C),in worst case dfs stack(R*C)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Graph grid traversal using DFS
# Variant: 
# Mistakes / Confusion:Na



# 2	-	547	-	Number of Provinces	-	Tier-1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        total_cities = len(isConnected)

        visited = set()


        def dfs(city):

            visited.add(city)

            for i in range(total_cities):


                if isConnected[city][i] == 1 and i not in visited:

                    dfs(i)
        
        provinces = 0

        for city in range(total_cities):

            if city not in visited:

                provinces += 1

                dfs(city)
        
        return provinces


# Status: Hints
# Time Taken: 15m 
# Time Complexity: O(V^2) V = no of vertices 
# Space Complexity: O(V),in worst case dfs stack(V)
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Graph adjacency matrix traversal using DFS
# Variant: 
# Mistakes / Confusion:Na


# 3	-	1020	-	Number of Enclaves	-	Tier-1


class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):

            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == 0:

                return 

            grid[r][c] = 0

            dfs(r-1, c) 
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        
        # Visiting all the land cell which are accesible from boudry.

        for c in range(cols):
            # Visiting land cells in first row
            if grid[0][c] == 1:

                dfs(0, c)
            # Visiting land cells in last row
            if grid[rows-1][c] == 1:

                dfs(rows-1,c)
        
        for r in range(rows):

            if grid[r][0] == 1:

                dfs(r, 0)
            
            if grid[r][cols-1] == 1:

                dfs(r, cols-1)
        
        enclaves = 0

        for r in range(rows):

            for c in range(cols):

                if grid[r][c] == 1:

                    enclaves += 1
        
        return enclaves


# Status: Independent
# Time Taken: 10m 
# Time Complexity: O(R*C) 
# Space Complexity: 0(R*C) recursion stack in worst case
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Graph grid traversal using dfs
# Variant: 
# Mistakes / Confusion:Na

# 4	-	127	-	Word Ladder	-	Tier-1


from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        
        set_wordlist = set(wordList)

        if endWord not in set_wordlist:

            return 0
     
        visited = set()


        queue = deque()

        queue.append((beginWord,1))

        visited.add(beginWord)

        while queue:

            word , number = queue.popleft()

            if word == endWord:

                return number
            
            for i in range(len(word)):

                for char in "abcdefghijklmnopqrstuvwxyz":

                    new_word = word[:i] + char + word[i+1:]

                    if new_word in set_wordlist and new_word not in visited:

                        queue.append((new_word,number+1))

                        visited.add(new_word)
        
        return 0

# Status: Independent
# Time Taken: 15m 
# Time Complexity: O(N*L^2)  Where outer while loop O(N) n = number words in list * innner nested loop for constructing new words O(L*26) * new word generation using slicing O(L) L lenght of word in a list. O(N)*O(L*26)*O(L) == O(N*L^2)
# Space Complexity: we are suing two sets and queue O(N)+O(N)+O(N) == O(N)  
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Graph traversal using the BFS
# Variant: word ladder
# Mistakes / Confusion:Na


# 5	-	433	-	Minimum Genetic Mutation	-	Tier-1


from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        
        bank_set = set(bank)

        if endGene not in bank_set:

            return -1
        
        queue = deque()

        queue.append((startGene,0))

        while queue:

            gene,count = queue.popleft()

            if gene == endGene:

                return count
            
            for i in range(len(gene)):

                for char in "ACGT":

                    new_gene = gene[:i] + char + gene[i+1:]

                    if new_gene in bank_set:

                        queue.append((new_gene,count+1))

                        bank_set.remove(new_gene)
        
        return -1


# Status: Independent
# Time Taken: 15m 
# Time Complexity: O(N) for popping  max n number genes * generating new gene using for loop O(L*4) * Constructing the newgenewrd O(L) l = lenght of the gene. so overall (N*L^2)
# Space Complexity: O(N*L)  
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Graph traversal using the BFS
# Variant: GENETIC MUTATION
# Mistakes / Confusion:Na


# 6	-	994	-	Rotting Oranges	-	Tier-1


from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        
        fresh_oranges = 0

        queue = deque()

        rows,cols = len(grid),len(grid[0])

        for r in range(rows):

            for c in range(cols):

                if grid[r][c] == 2:

                    queue.append((r,c))

                if grid[r][c] == 1:

                    fresh_oranges += 1
        
        minutes = 0

        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        while queue:

            len_queue = len(queue)
            
            is_rotten = False

            for _ in range(len_queue):

                r, c = queue.popleft()


                for dr , dc in directions:

                    nr = r + dr

                    nc = c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:

                        grid[nr][nc] = 2

                        queue.append((nr, nc))

                        fresh_oranges -= 1

                        is_rotten = True

            if is_rotten:

                minutes += 1
        
        return minutes if fresh_oranges == 0 else -1



# Status: Independent
# Time Taken: 25m 
# Time Complexity: O(R*C)
# Space Complexity: O(R*C)  
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Graph traversal using the BFS LEVL Order traversal
# Variant: rotten oranges 
# Mistakes / Confusion:Na


# 7	-	1091	-	Shortest Path in Binary Matrix	-	Tier-1


from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        
        if not grid or not grid[0] or grid[0][0] == 1:

            return -1 
        rows,cols = len(grid),len(grid[0])

        if grid[rows-1][cols-1] == 1:

            return -1
        
        queue = deque()

        queue.append(((0,0),1))

        visited = set()

        visited.add((0, 0))

        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1),
            (-1,-1),
            (1,-1),
            (-1,1),
            (1,1)
        ]

        while queue:

            (r, c), path = queue.popleft()

            if r == rows - 1 and c == cols - 1:

                return path
            

            for dr, dc in directions:

                nr = r + dr

                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 0:

                    visited.add((nr,nc))

                    queue.append(((nr, nc), path + 1))


        return -1 


            
# Status: Independent
# Time Taken: 20m 
# Time Complexity: O(R*C)
# Space Complexity: O(R*C)  
# Submitted to LC:Yes
# Result:Accepted
# Pattern:Graph traversal using the BFS LEVL Order traversal
# Variant: rotten oranges 
# Mistakes / Confusion:Na

            

# 8	-	463	-	Island Perimeter	-	Tier-1


        
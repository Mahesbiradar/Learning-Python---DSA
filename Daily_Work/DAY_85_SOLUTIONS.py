# Graphs


nodes = ["A", "B", "C", "D", "E"]

edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D"),
    ("D", "E")
]


graph = {node : [] for node in nodes}

for u , v in edges:

    graph[u].append(v)
    graph[v].append(u)

# print(graph)


def func(graph, root):

    visited = set()

    result = []

    def dfs(node):

        if node in visited:

            return 

        visited.add(node)

        result.append(node)

        for node in graph[node]:

            dfs(node)

    dfs(root)

    return result

print(func(graph,"A"))



from collections import deque


def bfs_func(graph,root):

    queue = deque([root])

    visited = set(root)

    result = []

    while queue:

        node = queue.popleft()

        result.append(node)

        for neighbor in graph[node]:

            if neighbor not in visited:

                visited.add(neighbor)
                queue.append(neighbor)

    return result



print(bfs_func(graph,"A"))




# Connected Graphs

graph_2 = {
    "A": ["B"],
    "B": ["A"],
    "C": ["D"],
    "D": ["C"],
    "E": []
}



def diconnected(graph):

    visited = set()

    result = []

    temp = []

    def dfs(root):

        if root in visited:
            return

        visited.add(root)

        temp.append(root)

        for neighbor in graph[root]:

            dfs(neighbor)
        
    for node in graph.keys():

        if node not in visited:

            dfs(node)

            result.append(temp)
            temp = []


    return result


print(diconnected(graph_2))






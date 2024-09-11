
graph = {}

key = int(input("\nEnter the number of nodes in the graph :- "))
for i in range(key):
  node=input("\nEnter the node :- ")
  neighbours=input("\nEnter the neighbours with spaces :- ").split()
  graph[node]=neighbours

print("\nGraph : " ,graph)

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
start_node = input("\nEnter node :- ")
print(f"\nFollowing is the Depth-First Search (Starting from Node {start_node}) :- ")
dfs(visited, graph, start_node)

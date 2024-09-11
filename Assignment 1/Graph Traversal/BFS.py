
graph = {}
visited = []   # List for visited nodes.
queue = []     # Initialize a queue

key=int(input("\nEnter the number of nodes in the graph :- "))
for i in range(key):
  node=input("\nEnter the node :- ")
  neighbours=input("\nEnter the neighbours with spaces :- ").split()
  graph[node]=neighbours

print("\nGraph :- ",graph)

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print(m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
        
n=input("\nEnter node :- ")
# Driver Code
print("\nFollowing is the Breadth-First Search :- ")
bfs(visited, graph, n)

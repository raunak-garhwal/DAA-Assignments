# Initialize a string direction which represents all the directions.
direction = "DLRU"

# Arrays to represent change in rows and columns
dr = [1, 0, 0, -1]
dc = [0, -1, 1, 0]

# Function to check if cell(row, col) is inside the maze and unblocked
def is_valid(row, col, n, maze):
    return 0 <= row < n and 0 <= col < n and maze[row][col] == 1

# Function to get all valid paths
def find_path(row, col, maze, n, ans, current_path):
    # If we reach the bottom right cell of the matrix, add the current path to ans and return
    if row == n - 1 and col == n - 1:
        ans.append(current_path)
        return
    # Mark the current cell as blocked
    maze[row][col] = 0

    for i in range(4):
        # Find the next row based on the current row (row) and the dr[] array
        next_row = row + dr[i]
        # Find the next column based on the current column (col) and the dc[] array
        next_col = col + dc[i]
        
        # Check if the next cell is valid or not
        if is_valid(next_row, next_col, n, maze):
            current_path += direction[i]
            # Recursively call the find_path function for the next cell
            find_path(next_row, next_col, maze, n, ans, current_path)
            # Remove the last direction when backtracking
            current_path = current_path[:-1]

    # Mark the current cell as unblocked
    maze[row][col] = 1


# Driver code
maze = []

order = int(input("\nEnter order of Maze : "))

print("\nAdd path into Maze :-\n" )

for i in range(order):
    row = list(map(int,input(f"Enter routes in {i+1} row (Seprated by space) : ").split()))
    maze.append(row)

print("\nMaze :-\n")
for row in maze:    
    print(" ".join(map(str,row)))

n = len(maze)
# List to store all the valid paths
result = []
# Store current path
current_path = ""

if maze[0][0] != 0 and maze[n - 1][n - 1] != 0:
    find_path(0, 0, maze, n, result, current_path)

if not result:
    print("\nNo Path is available......")
else:
    print("\nAvailable Paths :- ")
    print(" ".join(result))

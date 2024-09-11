# Function to solve Tower of Hanoi
def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 0:
        # Base case: Move the last disk directly from source to destination
        # print(f"Move disk 1 from {source} to {destination}")
        return
    # Step 1: Move n-1 disks from source to auxiliary, using destination as a helper
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    
    # Step 2: Move the nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    
    # Step 3: Move n-1 disks from auxiliary to destination, using source as a helper
    tower_of_hanoi(n - 1, auxiliary, destination, source)

# Input: number of disks
n = int(input("\nEnter the number of disks: "))

# Call the function with rods A, C, and B
tower_of_hanoi(n, 'A', 'C', 'B')

def sum_of_subsets(nums, target):
    result = []

    # Recursive function to find subsets
    def find_subsets(index, current_subset):
        # Base case: Check if the sum of the current subset matches the target
        if sum(current_subset) == target:
            result.append(current_subset.copy())
            return
        
        # Stop recursion if the end of the list is reached
        if index == len(nums):
            return
        
        # Explore including the current number
        find_subsets(index + 1, current_subset + [nums[index]])
        
        # Explore excluding the current number
        find_subsets(index + 1, current_subset)

    # Start the recursive function from the first index
    find_subsets(0, [])
    return result


# Dynamic input from the user
try:
    # Taking the set of numbers as input
    nums = list(map(int, input("\nEnter the numbers in the set separated by spaces: ").split()))
    # Taking the target sum as input
    target = int(input("\nEnter the target sum: "))

    # Finding and displaying subsets that sum to the target
    subsets = sum_of_subsets(nums, target)
    if subsets:
        print("\nSubsets that sum to", target, "are:", subsets)
    else:
        print(f"\nNo subsets found that sum to {target}.")
except ValueError:
    print("Invalid input! Please enter valid integers.")

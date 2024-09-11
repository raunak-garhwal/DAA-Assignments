import Quick_Sort
import Merge_Sort
import Binary_Search

if __name__ == "__main__":
    print("\n--- Welcome to the Menu Driven Program ---")

    while(True):
        print("\nPress 1 to perform Merge Sort.\nPress 2 to perform Quick Sort.\nPress 3 to exit.")

        try:
            choice = int(input("\nEnter your choice : "))
        except:
            print("\nWARNING :- Please enter a valid numeric value.")
        else:    
            if choice == 1:
                num = int(input("\nEnter the length of the list : "))
                my_list=[]

                for i in range(num):
                    value=int(input(f"Enter {i+1} element : "))
                    my_list.append(value)

                Merge_Sort.merge_sort(my_list)
                print(f"List after performing Merge sort : {my_list}")
                target=int(input("Enter the element to search in the list : "))
                result = Binary_Search.binary_search(my_list, target)

                if result != -1:
                    print(f"Element {target} found at index {result}.")
                else:
                    print(f"Element {target} not found in the list.")

            elif choice == 2:
                num = int(input("\nEnter the length of the list : "))
                my_list=[]

                for i in range(num):
                    value=int(input(f"Enter {i+1} element : "))
                    my_list.append(value)

                s=0
                e=len(my_list)-1
                Quick_Sort.quick_sort(my_list,s,e)
                print(f"List after performing Quick sort : {my_list}")
                target=int(input("Enter the element to search in the list : "))
                result = Binary_Search.binary_search(my_list, target)

                if result != -1:
                    print(f"Element {target} found at index {result}.")
                else:
                    print(f"Element {target} not found in the list.")

            elif choice == 3:
                print("\nThanks for using the program.")
                print("-----------------------------")
                break
                
            else:
                print("\nInvalid input : Please enter a valid choice.")
"""
Define a function that, on taking a list of numbers as input:
1. Creates a copy of the list
2. Removes all negative numbers from it
3. Appends 0 to it
4. Sorts the list in ascending order
5. Returns the modified list
All the while, the original list should remain unchanged.
"""

def process_list(numbers):

    # Create a copy of the input list
    new_list = numbers.copy()
 
    # Remove all negative numbers from the new list - by looping over a copy of the new list so elements aren't skipped
    for num in new_list.copy():
        if num < 0:
            new_list.remove(num)
 
    # Append 0 to the new list
    new_list.append(0)
 
    # Sort the new list in ascending order
    new_list.sort()
 
    # Return the modified new list
    return new_list

# Example - taking a list of numbers as input
n = int(input("Enter the number of elements: "))
raw_input = input(f"Enter {n} integers separated by spaces: ")
original = []
for value in raw_input.split():
    original.append(int(value))
result = process_list(original)

# Printing the original and new lists
print("Original:", original)
print("Result:", result)
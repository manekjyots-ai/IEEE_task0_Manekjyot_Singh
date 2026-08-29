"""
Taking N elements as input,
(without using built-in functions like max(), min() etc.),
find and print the following:
1. The largest number
2. The smallest number
3. The sum of all the numbers
4. The number of even numbers
5. The number of odd numbers
6. The list in reverse order.
"""

n = int(input("Enter the number of elements: "))

# Setting N, taking as many inputs
raw_input = input(f"Enter {n} integers separated by spaces: ")
elements = []
for value in raw_input.split():
    elements.append(int(value))
# Finding the largest and smallest numbers
largest = elements[0]
smallest = elements[0]
for num in elements:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

# Finding the sum of all the numbers
total = 0
for num in elements:
    total += num

# Finding the number of even and odd numbers
even_elements = 0
odd_elements = 0
for num in elements:
    if num % 2 == 0:
        even_elements += 1
    else:
        odd_elements += 1

# Reversing the list manually
reversed_list = []
for i in range(len(elements) - 1, -1, -1):
    reversed_list.append(elements[i])

print("Largest:", largest)
print("Smallest:", smallest)
print("Sum:", total)
print("Even count:", even_elements)
print("Odd count:", odd_elements)
print("Reversed:", *reversed_list)
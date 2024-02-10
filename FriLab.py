given_numbers = [2, 3, 4, 5, 15, 1, 43, 20]

# Q1: Write a function that takes a list as a parameter and returns the sum of all the items in that list.

def calculate_sum(given_numbers):

    return sum(given_numbers)

sum_of_numbers = calculate_sum(given_numbers)

print("Sum Of All:", sum_of_numbers)

# Q2: Write a function that takes a list as a parameter and returns the largest number from that list.

def find_largest_number(given_numbers):

    return max(given_numbers)

largest_number = find_largest_number(given_numbers)

print("Largest Number:", largest_number)

# Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125 using list comprehension.

odd_numbers = [num for num in range(1200, 2001, 125) if num % 2 != 0]

print("Odd Numbers List:", odd_numbers)

# Q4: Use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.

new_list = odd_numbers[:5]

print("New List:", new_list)

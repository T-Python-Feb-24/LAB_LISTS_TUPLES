# Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
list_number = [2, 3, 4, 5, 15, 1, 43, 20]

# Q1: Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.
def sum_list (count:list) -> int:
    num = sum(count)
    return num

print("Sum: ", sum_list(list_number))
print("List Length: ", len(list_number))

# Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
def max_num(count:list):
    num = max(count)
    return num

print("The largest number: ", max_num(list_number))

# Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].
odd_num:list = [x for x in range(1200, 2000, 125) if x%1 == 0]
print("Odd number list: ", odd_num)

# Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.
new_list = odd_num[:5]
print("New List: ", new_list)
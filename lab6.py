# Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
# Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.
my_list =[2, 3, 4, 5, 15, 1, 43, 20]
sum = sum(my_list)
print(sum)

# Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
def find_largest_number(my_list):
    if not my_list:
        return "The list is empty."
    
    largest = my_list[0]
    
    for num in my_list[1:]:
        if num > largest:
            largest = num
    
    return largest

my_list = [2, 3, 4, 5, 15, 1, 43, 20]
largest_number = find_largest_number(my_list)

print("Largest element in the list is:", largest_number)

# Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].
odd_numbers = [num for num in range(1200, 2001, 125) if num % 2 != 0]

print(odd_numbers)

# Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.
new_list = odd_numbers[:5]
print(new_list)

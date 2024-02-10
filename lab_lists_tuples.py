
def sum_of_list(numbers_list):
    '''the function takes a list as a parameter 
    and returns the sum  of all the items in that list'''
    sum_numbers = 0
    for number in numbers_list:
        sum_numbers += number
    return sum_numbers

def largest_from_list (numbers_list):
    '''the function takes a list as a parameter 
    and returns the largest number from a list of numbers'''
    largest = numbers_list[0]
    for number in numbers_list:
        if number > largest:
            largest = number
    return largest

# The given list
list1 = [2, 3, 4, 5, 6, 15, 1, 43, 20]
print(f"The given list: {list1}")
# 1. Presenting of the total of the sum all numbers in the given list
total_sum = sum_of_list(list1)
print(f"The total sum numbers in the list: {total_sum}")

# 2. Present of the largest number from the given list
largest_number = largest_from_list(list1)
print(f"The largest number in the list: {largest_number}")

# 3. Craeting an odd numbers list from the range 1200 to 2000 with steps of 125
odd_numbers_list = []
for number in range(1200, 2000, 125):
    if number % 2 != 0:
        odd_numbers_list.append(number)
print(f"List of the odd numbers from(1200,2000,125): {odd_numbers_list}")

# 4. useing the list slicing to get new list from odd_numbers_list
# (starting from the start to the 5th element in the list) 
# there is no 5th element so lets try slice it to the second :)
odd_numbers_sublist = odd_numbers_list[:2]
print(f"List slicing from the previus list: {odd_numbers_sublist}")






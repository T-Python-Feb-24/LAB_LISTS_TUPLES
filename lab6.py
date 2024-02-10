def list_sum(list1):
    '''
Q1: Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.
    '''
    return sum (list1)
list1=[2, 3, 4, 5, 15, 1, 43, 20]
sum_result=list_sum(list1)
print(list_sum.__doc__)
print("sum result:",sum_result)


def list_largest(list2):
    '''
Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
    '''
    return max(list2)
list2=[2, 3, 4, 5, 15, 1, 43, 20]
largest_result=list_largest(list2)
print(list_largest.__doc__)
print("the largest number:",largest_result)

# Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ]
odd_number=[odd for odd in range(1200,2000,125) if odd % 2!=0]
print(odd_number)
# Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.

slicing_list=odd_number[:5]
print(slicing_list)



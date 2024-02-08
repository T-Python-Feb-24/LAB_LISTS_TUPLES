def sumOfNumbersInList(nums: list[int]) -> int:
    '''Q1: Write a function that takes a list as a parameter,
and then returns the sum of all the items in that list'''
    return sum(nums)


def largest_Number(nums: list[int]) -> int:
    '''Q2: Write a function that takes a list as a parameter,
and then returns the largest number from a list of numbers'''
    return max(nums)


nums = [2, 3, 4, 5, 15, 1, 43, 20]

# call sumOfNumbersInList for Q1
print(f"\nThe sum of numbers in {nums} = {sumOfNumbersInList(nums)}", end="\n\n")

# call largest_Number for Q2
print(f"The largest number in {nums} = {largest_Number(nums)}", end="\n\n")

# Q3: Create an odd numbers list from the elements of a range
# from 1200 to 2000 with steps of 125, using [ List Comprehension ].
start, end, step = 1200, 2000, 125
rangeList = list(range(start, end+1, step))

oddList: list[int] = [i for i in rangeList if i % 2 != 0]
print(f"The odd Numbers from a list from {start} to {end} \
with step of {step} = {oddList}", end="\n\n")

# Q4: use list slicing to get a new list from the previous list
# (odd numbers list) starting from the start to the 5th element in the list.
print(f"A slice of a list from {start} to {end} \
with step of {step} = {rangeList[:5]}")

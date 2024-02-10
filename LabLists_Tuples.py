# Given the following list : [2, 3, 4, 5, 15, 1, 43, 20]
listOfNumbers = [2, 3, 4, 5, 15, 1, 43, 20]

# Q1: Write a function that takes a list as a parameter, and then returns  the sum  of all the items in that list.
def sumList(listOfNumbers):
    sum = 0 
    for num in listOfNumbers : 
        sum += num 
    return sum
print(f"sum of all the items in the list: {sumList(listOfNumbers)}")

# Q2: Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
def largestNumber(listOfNumbers):
    largeNum = 0
    for num in listOfNumbers :
        if num > largeNum:
            largeNum = num 
    return largeNum
print(f"the largest number in the list: {largestNumber(listOfNumbers)}")

# Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].
oddList = [num for num in range(1200,2000,125) if num % 2 != 0]
print(f"odd list: {oddList}")

# Q4: use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.
listSlicing = oddList[:5]
print(f"list slicing: {listSlicing}")


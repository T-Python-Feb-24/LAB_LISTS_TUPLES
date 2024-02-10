Numbers = [2, 3, 4, 5, 15, 1, 43, 20]
def sumOfNuumbers(numbers:list)-> list:
    """this function returns the sum of all the items in the given list."""
    return sum(Numbers)

total = sumOfNuumbers(Numbers)
print(total)


def maximum(numbers:list)-> list:
    """this function return the largest number in the list"""
    return max(Numbers)
largest = maximum(Numbers)
print(largest)


oddNumbers = range(1200, 2000, 125)
# new_list = [new item for item in list if condition]
oddNumbersList = [num for num in oddNumbers if num % 2 == 1]
print(oddNumbersList)


newNumbers = oddNumbersList[1: 5]
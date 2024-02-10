the_list = []
while True:
    element = input("Enter an element (or 'end' to finish): ")
    if element.lower() == "end":
        break
    the_list.append(int(element))
#####################
def sum_all(func_list):
    return sum(func_list)

print(f"The sum of all the items -> {sum_all(the_list)}")

######################

def largest_number(func_list):
    return max(func_list)

print(f"The biggest number in the list is -> {largest_number(the_list)}")

#################

odd_numbers_list = [num for num in range(1200, 2000, 125) if num % 2 != 0]
print("Odd numbers list:", odd_numbers_list)

################

sliced_list = odd_numbers_list[0:5]

print("Sliced list:", sliced_list)



num_list = [ 2, 3, 4, 5, 15, 1, 43, 20 ]
print(num_list)

def element_sum(elements) :
    return sum(elements)

total_sum = element_sum(num_list)
print("Sum:", total_sum)

def numbers(elements):
    return max(elements)

largest_number = numbers(num_list)
print("The largest number:", largest_number)

odd_numers = [num for num in range(1200 , 2000, 125)if num % 2 != 0]
print(odd_numers)

new_list = odd_numers[:2]
print(new_list)

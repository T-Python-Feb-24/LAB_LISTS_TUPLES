#1
def calculare_sum(list):
    return sum (list)
my_list=[2,3,4,5,15,1,43,20]
result=calculare_sum(my_list)
print(result)

#2
def find_largrst(list):
    return max (list)
my_list=[2,3,4,5,15,1,43,20]
result=find_largrst(my_list)
print(result)
#3
odd_numbers=[num for num in range(1200,2001,125)if num % 1==0]
print(odd_numbers)
#4
new_list=odd_numbers[:5]
print(new_list)
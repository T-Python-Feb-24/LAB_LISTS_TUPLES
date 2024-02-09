numbers=[2,3,4,5,15,1,43,20]
RangeNumbers=range(1200,2000,125)

def sum_list(numbers):
  print(sum(numbers))


sum_list(numbers)



def largest_number (numbers):
  print(max(numbers))


largest_number(numbers)

oddList= [x for x in RangeNumbers if x%2==1 ]
print(oddList)
print(oddList[0:5])

numbers=[2,3,4,5,15,1,43,20]
RangeNumbers=range(1200,2000,125)

def sum_list(numbers):
  return sum(numbers)

def largest_number (numbers):
  return max(numbers)

oddList= [x for x in RangeNumbers if x%2==1 ]

print(sum_list(numbers))
print(largest_number(numbers))
print(oddList)
print(oddList[0:5])
#Another two slicing 
print(oddList[0:2]) 
print(oddList[0:1])

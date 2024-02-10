#Q1
def sum_list():
 number:list=[2, 3, 4, 5, 15, 1, 43, 20]
 sum1 =sum(number)
 return sum1 
print(sum_list())

#Q2
def largest_num():
 number2:list=[2, 3, 4, 5, 15, 1, 43, 20]
 large= max(number2)
 return large
print(largest_num())

#Q3

element1=[x for x in range(1200,2000,125) if x % 2 !=0 ]
print(element1) 

#4
new_list=element1[:5]
print(new_list)


#bonus



# Calculates the average rating for each movie.
def calculate_average_rating(movie):
 ratings=movie[2]
 average=sum(ratings)/len(ratings)
 return average


#Filters out movies with an average rating lower than 6.0.

def filter(movies):
 filtered=[]
 for movie in movies:
  average=calculate_average_rating(movie)
  if average >= 6.0:
    filtered.append((movie[0],movie[1],average))
 return filtered
  
 ''' Displays the  movies, along with their title,
   release year, and average rating.
 '''
def display(movies):
   movies.sort(key=lambda x:x[2],reverse=True)
   for i,movie in enumerate(movies):
     print(f"{i+1}.{movie[0]} ({movie[1]}) - Average ratings: {movie[2]:.2f} ★ ")

movies =[("home alone" ,1999, [5,6,8,10]),
       ("the walking dead" ,2001, [3,8,7,4]),
       ("the 100" ,2003, [5,7,9,10]),
       ("peaky Blenders" ,1998, [6,8,9,10]),
       ("the hunting" ,2000, [7,8,9,1]),
      ("Narcos" ,1996, [4,6,8,9]) ]
 
filtered= filter(movies)
display(filtered)
  
  
 









# Calculate the average of movies ratings
def calculate_average_ratings(user_ratings):
    sum_rating = 0
    for rating in user_ratings:
        sum_rating +=rating
    average_rating = sum_rating / len(user_ratings)
    return average_rating

# Filter out movies with an average rating lower than 6.0
def filter_movies(movies_list):
    filtered_movies = []
    for movie in movies_list:
        # movie[2]-> 2 is the index of ratings element
        if movie[2] >= 6.0:
            filtered_movies.append(movie)
    return filtered_movies
      
#Start Movies Rating System
print("---------------------------------------- Movies Rating System ----------------------------------------")
# Separate parts with a Comma, and single space between ratings
print("- Please enter movie details in the format(comma between parts and space between ratings): movie name,release year,rating1 raeting2 .. ")
# To end entering movie details press "e"
print("- Enter e if you are finish.")

# Take movies details input and store it in list
movies_list = []
count = 1
while True:
    movie_details = input(f"Movie ({count}): ")
    count += 1
    if movie_details == 'e':
       break
    
    name, year, *ratings = movie_details.split(',')
    ratings_str = ratings[0].split()
    # Create an empty list to store integer ratings
    ratings_int = []  
    for rating_str in ratings_str:
        rating_int = int(rating_str)  
        ratings_int.append(rating_int)  
    ratings = ratings_int
    movies_list.append((name, year, ratings))

# Create an empty list to store movies average ratings  
movies_average = []  
for name, year, ratings in movies_list:
        average = calculate_average_ratings(ratings)
        movies_average.append((name, year, average))
    
# Print movies ratings list after filtered 
filtered_list = filter_movies(movies_average)
count = 1
for name, year, avg_rating in filtered_list:
    print(f"{count}. {name} ({year}) - Average Rating: {avg_rating:.2f} ★")
    count += 1


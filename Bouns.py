
# 1. Accepts a list of movies, with each movie represented as a tuple containing the movie title, release year, and a list of user ratings.
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

# 2. Calculates the average rating for each movie.
movieRatingList=[i[2] for i in movies]   
averageList = [[round(sum(i)/len(movieRatingList),2)] for i in movieRatingList]

# This converts each item in the average list into a tuple so that I can add it to each movie's tuple in the movies list.
averageList = [(item,) for item in averageList]

#  Here, I insert the average rating for each movie into the respective tuple within the movies list  
movies = [movies[i] + averageList[i] for i in range(0,len(movies))]

# 3. Filters out movies with an average rating lower than 6.0.
movies.sort(reverse=True)
for i in movies:
    movieName,  releaseYear, ratings, avrRating = i 
    if avrRating[0] > 6 :
        # 5. Displays the  movies, along with their title, release year, and average rating.
        print(f'{movieName},({releaseYear}), Avergae rating:{avrRating[0]} ★')

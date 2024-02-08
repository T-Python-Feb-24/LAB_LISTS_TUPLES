# Movie Ratings Analysis

movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
movies_Rated = []
for movie in movies:
    title = movie[0]
    release_date = movie[1]

    average_rating = round(sum(movie[2])/len(movie[2]), 2)
    movies_Rated.append([title, release_date, average_rating])

movies_Rated.sort(key=lambda x: x[2], reverse=True)
i = 1
for movie in movies_Rated:
    if movie[2] > 6:
        print(f"{i}. {movie[0]} ({movie[1]}) - Avergae rating: {movie[2]}★")
        i += 1

def average_reating(ratings):
    '''calculate the average of the rating '''
    return sum(ratings) / len(ratings)

def filter_movies(movies):
    '''filter movies with an average rating lower than 6'''
    filtered_movies = []
    for title, year, ratings in movies:
        average_rating = average_reating(ratings)
        if average_rating >= 6.0:
            filtered_movies.append((title, year, average_rating))
    return filtered_movies

def display_movies(movies):
    for i, (title, year, average_rating) in enumerate(movies, start=1):
        print(f"{i}. {title} ({year}) - Average rating -> {average_rating:.2f} ★")

movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1]),
    ("Inception", 2010, [9, 10, 9, 9, 8, 8]),
    ("Forrest Gump", 1994, [8, 9, 9, 7, 8, 9]),
    ("The Emoji Movie", 2017, [1, 2, 1, 1, 1, 1]),
    ("The Matrix", 1999, [9, 8, 9, 8, 7, 8]),
    ("Home Alone", 1990, [8, 7, 8, 7, 9, 8])
]

filtered_movies = filter_movies(movies)

display_movies(filtered_movies)
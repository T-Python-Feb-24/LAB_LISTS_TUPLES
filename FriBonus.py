def calculate_average_rating(ratings):
    return sum(ratings) / len(ratings)


def filter_movies_by_rating(movies):
    return [movie for movie in movies if calculate_average_rating(movie[2]) >= 6.0]


def display_movies(movies):
    print("Movies:")
    for i, movie in enumerate(movies, 1):
        title, release_year, ratings = movie
        average_rating = calculate_average_rating(ratings)
        print(f"{i}. {title} ({release_year}) - Average Rating: {average_rating:.2f} ★")


movies = [
    ("Home Alone", 1990, [9, 10, 9, 8, 7, 9]),
    ("Prisoners", 2013, [9, 7, 9, 10, 9, 8]),
    ("Triple Frontier", 2019, [9, 6, 10, 8, 7, 9]),
    ("Red Notice", 2021, [6, 10, 8, 6, 9, 8]),
    ("Bird Box", 2018, [7, 6, 8, 7, 9, 9]),
    ("The Irish Man", 2019, [9, 8, 6, 7, 5, 6])
   
]

filtered_movies = filter_movies_by_rating(movies)
display_movies(filtered_movies)
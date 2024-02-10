def calculate_average_rating(ratings):
    return sum(ratings) / len(ratings)

def display_filtered_movies(movies):
    filtered_movies = []
    for i, (title, year, ratings) in enumerate(movies, start=1):
        avg_rating = calculate_average_rating(ratings)
        if avg_rating >= 6.0:
            filtered_movies.append((title, year, avg_rating))

    print("Filtered movies:")
    for i, (title, year, avg_rating) in enumerate(filtered_movies, start=1):
        print(f"{i}. {title} ({year}) - Average rating: {avg_rating:.2f} ★")


movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]


display_filtered_movies(movies)

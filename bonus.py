def calculate_average_rating(ratings):
    total = sum(ratings)
    average = total / len(ratings)
    return average

def filter_movies(movies):
    filtered_movies = []
    for movie in movies:
        title, release_year, ratings = movie
        average_rating = calculate_average_rating(ratings)
        if average_rating >= 6.0:
            filtered_movies.append((title, release_year, average_rating))
    return filtered_movies

def display_movies(movies):
    for movie in movies:
        title, release_year, average_rating = movie
        print(f"Title: {title}")
        print(f"Release Year: {release_year}")
        print(f"Average Rating: {average_rating}")
        print()

movies = [
    ("The Shawshank Redemption", 1994, [10, 9, 8, 7, 6]),
    ("The Godfather", 1972, [10, 9, 8, 7, 6]),
    ("Pulp Fiction", 1994, [9, 8, 7, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 8, 7, 6]),
    ("Schindler's List", 1993, [8, 9, 7, 6, 5]),
    ("The Room", 2003, [1, 2, 3, 4, 5])
]

filtered_movies = filter_movies(movies)
display_movies(filtered_movies)
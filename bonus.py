movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
def rating(rates):
    """this function will calculate the average rating of the movie"""
    return sum(rates) / len(rates)

def movieFilter(movies):
    """this function will filter the movies based on rating and remove movies under 6.0 rating"""
    return [(title, year, rates) for title, year, rates in movies if rating(rates) >= 6.0]

def display(movie):
    """this function will display the movies."""
    for title, year, rate in movie:
        avg_rating = rating(rate)
        print(f"{title} ({year}) - Average Rating: {avg_rating:.2f}")

filteredMovies = movieFilter(movies)


display(filteredMovies)
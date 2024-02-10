movies = [
    ("Fight Club", 1994, [9, 10, 9, 9, 8, 9]),
    ("Godzilla Minus One", 2023, [10, 9, 7, 10, 7, 7]),
    ("Rebecca", 1940, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("Forrest Gump", 2003, [1, 2, 3, 4, 5, 1])
]




for titile , year ,rating in movies:
     Average=sum(rating) / len(rating)
     
     if Average > 6 :
           print("{} ({}) - Averaga rating : {:.2f} *".format(titile,year,Average))
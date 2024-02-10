movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
move_list=[]
for average  in movies:
    title=average[0]
    date=average[1]
    avergae_rate=round(sum(average [2])/len(average [2]),2)
    move_list.append([title,date,avergae_rate])
    move_list.sort(key=lambda x: x[2], reverse=True)

i=1
for movie in move_list:
    if movie[2] > 6:
        print(f"{i}. {movie[0]} {movie[1]} - average rating: {movie[2]}★")
        i += 1


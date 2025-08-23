print("Enter movies watched by User B (separated by commas):")
user_b = input()
user_b_movies = set(user_b.split(','))

user_a_movies = set(movie.strip() for movie in user_a_movies)
user_b_movies = set(movie.strip() for movie in user_b_movies)

common = user_a_movies.intersection(user_b_movies)

unique_a = user_a_movies.difference(user_b_movies)


suggested = user_b_movies.difference(user_a_movies)

print("\nMovies both User A and User B have watched:")
for movie in common:
    print(movie)

print("\nMovies only User A has watched:")
for movie in unique_a:
    print(movie)

print("\nMovies suggested for User A:")
for movie in suggested:
    print(movie)

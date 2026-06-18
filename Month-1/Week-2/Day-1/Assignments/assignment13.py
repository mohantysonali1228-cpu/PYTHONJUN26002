# Create a Movie Class

class Movie:
    def __init__(self, movie_name, hero_name, release_year):
        self.movie_name = movie_name
        self.hero_name = hero_name
        self.release_year = release_year

    def display(self):
        print("Movie Name:", self.movie_name)
        print("Hero Name:", self.hero_name)
        print("Release Year:", self.release_year)


# Creating a movie object
m1 = Movie("Pushpa", "Allu Arjun", 2021)

# Displaying movie details
m1.display()
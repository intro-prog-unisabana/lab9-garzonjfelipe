class Song:
    def __init__(self, name, artist, length):
        self.name = name
        self.artist = artist
        self.length = length

    def get_length_in_seconds(self):
        return self.length * 60

    def __str__(self):
        return f"'{self.name}' by {self.artist} ({self.length})"
# FREEZE CODE BEGIN
class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year
# FREEZE CODE END
    # TODO: Define the __str__ method!


# FREEZE CODE BEGIN
if __name__ == "__main__":
    # --- Main Program ---
    title = input("Enter the movie title: ")
    director = input("Enter the director's name: ")
    year = input("Enter the release year: ")
# FREEZE CODE END
    
    
    # TODO: Construct a Movie object!
    # TODO: Print the object!

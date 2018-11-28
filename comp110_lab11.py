"""
Module: movie_predictor

Program to predict movie ratings based on the reviews of similar users.
"""

class GenreSummary:
    """
    A class to represent a summary of the reviews in a specific genre by one
    user.
    """

    def __init__(self, name):
        """
        Initializes a new GenreSummary object for a genre with the given name.
        """
        self.name = name
        self.__sum = 0
        self.num_ratings = 0
        self.average = 0.0

    def __str__(self):
        my_str = "%s: Average Rating = %f (%d reviews)" % (self.name,
                                                           self.average,
                                                           self.num_ratings)
        return my_str

    def update(self, rating):
        """
        Updates genre summary with a new rating.
        """
        self.__sum = self.__sum + rating
        self.num_ratings = self.num_ratings + 1
        self.average = self.__sum / self.num_ratings

class Movie: 
    """
    Represents a movie from the movie database.
    """

    def __init__(self, movie_id, title, genres):
        # To Do: Implement this constructor method.
        return None # placeholder: remove when done implementing

    def __str__(self):
        # To Do: Implement this method.
        string_representation = ""
        return string_representation

class User:
    """
    Represents the set of movie ratings for a user.
    """

    def __init__(self, user_id, genre_list):
        """
        Initializes a new User object.
        """
        self.id = user_id

        # To Do: Finish writing this constructor

    def __getitem__(self, genre_name):
        # To Do: Implement this method.
        return 0.0

    def add_review(self, movie, rating):
        # To Do: Implement this method.
        return None # placeholder: remove this line


def read_movie_db(filename):
    # To Do: Implement this function. You should hopefully have most of it
    # done from your Lab 10 code.
    movies = {}
    all_genres = []

    return (movies, all_genres)


def test_movie_class():
    """
    Tests the Movie class
    """
    # Create a movie object.
    movie = Movie(17, "Sense and Sensibility (1995)", ["Drama", "Romance"])
    correct_str = "17. Title: Sense and Sensibility (1995), Genres: Drama Romance"

    # Get string representation.
    movie_str = str(movie)

    # Check for correctness
    if movie_str == correct_str:
        print("Movie class passed test")
    else:
        print("Error in your Movie class")
        print("Your __str__ returns '%s'" % (movie_str))
        print("Should be '%s'" % (correct_str))

def test_read_movie_db():
    """
    Tests the read_movie_db function
    """
    # Correct titles
    tests = [(2, "2. Title: Jumanji (1995), Genres: Adventure Children Fantasy"),
         (7, "7. Title: Sabrina (1995), Genres: Comedy Romance"),
         (11, "11. Title: American President, The (1995), Genres: Comedy Drama Romance"),
         (13, "13. Title: Balto (1995), Genres: Adventure Animation Children"),
         (18, "18. Title: Four Rooms (1995), Genres: Comedy"),
         (100, None)]

         # Correct genres
    correct_all_genres = ['adventure', 'animation', 'children', 'comedy', 'drama', 'fantasy', 'romance']

    # Read movie db
    (movie_for_id, all_genres) = read_movie_db("test_movies_db.csv")
    for i in range(len(all_genres)):
        all_genres[i] = all_genres[i].lower()
    all_genres.sort()

    # Check that movie dictionary was created correctly.
    function_correct = True
    for test in tests:
        movie_info = movie_for_id.get(test[0])
        if test[1] == None:
            if movie_info != None:
                print("\nError in your read_movie_db function")
                print("Movie id %d" % (test[0]))
                print("Info should be '%s'" % (test[1]))
                print("Your info was '%s'" % (movie_info))
                function_correct = False
        elif str(movie_info) != test[1]:
            print("\nError in your read_movie_db function")
            print("Movie id %d" % (test[0]))
            print("Info should be '%s'" % (test[1]))
            print("Your info was '%s'" % (movie_info))
            function_correct = False

    # Check that genre list was created correctly
    if all_genres != correct_all_genres:
        print("\nError in your read_movie_db function")
        print("Your list of all genres is incorrect")
        print("Should be %s" % (str(correct_all_genres)))
        print("Yours was %s" % (str(all_genres)))
        function_correct = False

    # Print message if all correct
    if function_correct:
        print("read_movie_db function passed test")


def test_user_class():
    """
    Tests the User class
    """
    # Create movie db and get list of genres.
    genre_review_averages = [3.5, 3.5, 5.0, 2.6666666666666665, 3.5, 3.0, 2.0]
    (movie_for_id, all_genres) = read_movie_db("test_movies_db.csv")

    # Create a user
    user = User(1, all_genres)

    # Add some reviews
    user.add_review(movie_for_id[2], 5)
    user.add_review(movie_for_id[7], 4)
    user.add_review(movie_for_id[11], 3)
    user.add_review(movie_for_id[13], 2)
    user.add_review(movie_for_id[18], 1)

    # Get average rating of genres
    average_ratings = []
    for genre in all_genres:
        average_ratings.append(user[genre])

    # Check for correctness
    function_correct = True
    for i in range (len(average_ratings)):
        if abs(average_ratings[i] - genre_review_averages[i]) > 0.000001:
            print("\nError in your User class")
            print("Genre = %s" % (all_genres[i]))
            print("Review average for this genre should be %f" % (genre_review_averages[i]))
            print("Your average for this genre is %f" % (average_ratings[i]))
            function_correct = False

    if function_correct:
        print("User class passed test")

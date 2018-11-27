"""
Module: movie_predictor

Program to predict movie ratings based on the reviews of similar users.
"""

import math
import sys
from scipy.stats import pearsonr

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
    Represents a user in our moview review database.
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

    def similarity(self, other_user, genres):
        # To Do: Implement this method.
        return 0.0

    def predicted_rating(self, movie_id, other_reviewers, genres):
        # To Do: Implement this method.
        return 0.0

    def add_review(self, movie, rating):
        # To Do: Implement this method.
        return None # placeholder: remove this line

    def distance(self, other_user, genres):
        """
        Computes the similarity between two users based on their ratings for the
        giving list of genres.

        Do not modify this method.
        """
        acc = 0
        for genre in genres:
            acc += (self[genre] - other_user[genre])**2
        return 1/(1 + math.sqrt(acc))

def read_movie_db(filename):
    # To Do: Implement this function

    return ({}, []) # placeholder: remove after implementing

def read_training_review_db(filename, movie_for_id, genre_list):
    # To Do: Implement this function

    return ({}, {}) # placeholder: remove after implementing

def read_test_review_db(filename):
    # To Do: Implement this function

    return [] # placeholder: remove after implementing

def review_predictor(movie_db_filename, training_reviews_filename,
                     test_reviews_filename):
    # Step 1a: Read in the movie database.

    # Step 1b: Print the number of movies in the database

    # Step 1c: Print the genres

    # Step 2a: Read in the training ratings database.

    # Step 2b: Print out the number of users created

    # Step 3a: Read in the test ratings database.

    # Step 3b: Print out the number of ratings in the test dataset


    # Step 4: Iterate over all ratings in the test set, using the
    # predicted_rating method to get the predicted review.
    # While doing this, you should add each prediction to the
    # predicted_ratings list and each actual rating (from the test tuple) to
    # the actual_ratings list.
    actual_ratings = []
    predicted_ratings = []

    # Step 5: Calculate the Pearson correlation coefficient using the pearsonr
    # function and print out this value.


# Do not modify any code below this line.

def test_movie_class():
    """
    Tests the Movie class
    """
    try:
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
    except Exception as e:
        print("Exception occured while testing Movie class: %s" % (str(e)))

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

    try:
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
        
    except Exception as e:
        print("Exception occured while testing read_movie_db: %s" % (str(e)))

def test_user_class():
    """
    Tests the User class
    """
    try:
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

    except Exception as e:
        print("Exception occured while testing User class: %s" % (str(e)))    

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("ERROR: Must specify movie, training, and test dataset files.")
        sys.exit()

    review_predictor(sys.argv[1], sys.argv[2], sys.argv[3])

class movieReview :
  def __init__(self, movie, story, actors, music):
    #Movie name
    self.movie_name = movie

    #Ratings
    self.story_rating = story
    self.actor_rating = actors
    self.music_rating = music

    #AverageRatings

    self.avg = int((self.story_rating + self.actor_rating + self.music_rating)/3)
    
    #MoveInfo

    self.myrating = {
        "Movie Name": self.movie_name,
        "Story rating": self.story_rating,
        "Actor Rating": self.actor_rating,
        "Music Rating": self.music_rating,
         "Avg Rating" : self.avg
    }


  def add_movie_ratings(self, movie_list):
        movie_list.append(self.myrating)
  
  
  def avg_star_ratings(self, movie_list):
    for movie in movie_list:
      if(movie["Avg Rating"] == 1 ):
        print("Thanks for the response, You rated Movie with   *")
        print(movie)

      elif(movie["Avg Rating"] == 2 ):
        print("Thanks for the response, You rated Movie with   * * ")
        print(movie)

      elif(movie["Avg Rating"] == 3 ):
        print("Thanks for the response, You rated Movie with   * * *")
        print(movie)

      elif(movie["Avg Rating"] == 4 ):
        print("Thanks for the response, You rated Movie with   * * * *")
        print(movie)

      if(movie["Avg Rating"] == 5 ):
        print("Thanks for the response, You rated Movie with   * * * * *")
        print(movie)
      
  
moviereviews = []

review1 = movieReview("Harry Potter", 5,5,5)
review1.add_movie_ratings(moviereviews)
review1.avg_star_ratings(moviereviews)

review2 = movieReview("Beautiful Sound", 5,5,5)
review2.add_movie_ratings(moviereviews)
review2.avg_star_ratings(moviereviews)



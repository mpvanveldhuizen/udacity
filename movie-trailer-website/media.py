# Matt Van Veldhuizen
# 05/15/2015
# Udacity Full Stack Web Developer Nanodegree
# Movie Trailer Website Project
# media.py
# This Python code has the Movie class which describes information about a
# particular movie Information such as: Title, Storyline, Poster,
# Trailer, and Rating
# To be used with fresh_tomatoes.py and entertainment_center.py

class Movie():
	"""This class provides a way to store movie related information"""

	# Class Movie Constructor, takes in infomration about the movie:
	# movie title, movie storyline, movie poster, movie trailer,
	# movies imdb page, and its rating
	def __init__(self, movie_title, movie_storyline, poster_image,
	             trailer_youtube, rating):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.rating = rating
# Matt Van Veldhuizen
# 05/15/2015
# Udacity Full Stack Web Developer Nanodegree
# Movie Trailer Website Project
# entertainment_center.py
# This Python code sets up new movies using the Movie class from media
# Each new movie is then set into a list wich is passed to fresh_tomatoes
# which then generates a web page
# To be used with fresh_tomatoes.py and media.py

#import the media module which contains the Movies class
import media
#import the fresh_tomatoes module which contains the webpage generation
import fresh_tomatoes

#create new movie instance required arugments:
#	"Title", "Story Line", "Poster", "Trailer", raiting

#new movie The Avengers
the_avengers = media.Movie("The Avengers",
			   "Earth's mightiest heroes must come together and "\
			   "learn to fight as a team if they are to stop the "\
			   "mischievous Loki and his alien army from enslaving "\
			   "humanity.",
			   "http://upload.wikimedia.org/wikipedia/en/f/f9/"\
			   "TheAvengers2012Poster.jpg",
			   "https://www.youtube.com/watch?v=Q8jbt0wBkMI",
			   8.2)

#new movie Project A
project_a = media.Movie("Project A",
			"Fighting against pirates in old Hong Kong. Chinese "\
			"costume drama with plenty of over-the-top tongue in "\
			"cheek action and music.",
			"http://upload.wikimedia.org/wikipedia/en/d/dc/"\
			"Project_A_Poster.jpg",
			"https://www.youtube.com/watch?v=SqUS8hzkmxA",
			7.5)

#new movie Snatch
snatch = media.Movie("Snatch",
		     "Unscrupulous boxing promoters, violent bookmakers, a "\
		     "Russian gangster, incompetent amateur robbers, and "\
		     "supposedly Jewish jewelers fight to track down a "\
		     "priceless stolen diamond.",
		     "http://upload.wikimedia.org/wikipedia/en/a/a7/"\
		     "Snatch_ver4.jpg",
		     "https://www.youtube.com/watch?v=Q8jbt0wBkMI",
		     8.3)

#new movie Alien
alien = media.Movie("Alien",
		    "The commercial vessel Nostromo receives a distress call "\
		    "from an unexplored planet. After searching for survivors, "\
		    "the crew heads home only to realize that a deadly bioform "\
		    "has joined them.",
		    "http://upload.wikimedia.org/wikipedia/en/c/c3/"\
		    "Alien_movie_poster.jpg",
		    "https://www.youtube.com/watch?v=bEVY_lonKf4",
		    8.5)

#new movie Lord of the Rings
lord_of_the_rings = media.Movie("The Lord of the Rings: The Fellowship of the"\
				" Ring",
				"A meek hobbit of the Shire and eight "\
				"companions set out on a journey to Mount Doom"\
				" to destroy the One Ring and the dark lord "\
				"Sauron.",
				"http://upload.wikimedia.org/wikipedia/en/0"\
				"/0c/The_Fellowship_Of_The_Ring.jpg",
				"https://www.youtube.com/watch?v=Pki6jbSbXIY",
				8.8)

#new movie Star Wars
star_wars = media.Movie("Star Wars: A New Hope",
			"Luke Skywalker joins forces with a Jedi Knight, a "\
			"cocky pilot, a wookiee and two droids to save the "\
			"universe from the Empire's world-destroying battle-"\
			"station, while also attempting to rescue Princess "\
			"Leia from the evil Darth Vader.",
			"http://upload.wikimedia.org/wikipedia/en/8/87/"\
			"StarWarsMoviePoster1977.jpg",
			"https://www.youtube.com/watch?v=1g3_CFmnU7k",
			8.7)

#create new list of movies, to be passed into the
#fresh_tomatoes.open_movies_page function
movies=[the_avengers, project_a, snatch, alien, star_wars, lord_of_the_rings]

#call open_movies_page
fresh_tomatoes.open_movies_page(movies)
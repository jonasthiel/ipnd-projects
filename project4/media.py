"""
Created on Tue Sep 25 2018

@author: jonasthiel

Defines multiple classes which are used in entertainment_center.py file
"""

import webbrowser

class Video():
	# Constructs objects of the class
	def __init__(self, title, storyline, poster_image, trailer_youtube, release_date):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.release_date = release_date

	# Opens the YouTube link in the webpage generate by fresh_tomatoes.py file
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

# Subclass of class Video
class Movie(Video):
	def __init__(self, title, storyline, poster_image, trailer_youtube, release_date):
		Video.__init__(self, title, storyline, poster_image, trailer_youtube, release_date)

	def show_trailer(self):
		Video.show_trailer(self)

# Subclass of class Video
class Series(Video):
	def __init__(self, title, storyline, poster_image, trailer_youtube, release_date):
		Video.__init__(self, title, storyline, poster_image, trailer_youtube, release_date)

	def show_trailer(self):
		Video.show_trailer(self)
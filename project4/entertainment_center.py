"""
Created on Tue Sep 25 2018

@author: jonasthiel

Contains content for the webpage which is generate by fresh_tomatoes.py file
"""

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
	"A story of a boy and his toys that come to life",
	"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc",
	"1995"
	)

avatar = media.Movie("Avatar",
	"A marine on an alien planet",
	"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY",
	"2009"
	)

blood_diamond = media.Movie("Blood Diamond",
	"A diamond smuggler with a good heart at the end",
	"https://upload.wikimedia.org/wikipedia/en/5/5a/Blooddiamondposter.jpg",
	"https://www.youtube.com/watch?v=Ysd7SUwm6co",
	"2006"
	)

gladiator = media.Movie("Gladiator",
	"A honorable gladiator called Maximus",
	"https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
	"https://www.youtube.com/watch?v=0BLZbrLogTo",
	"2000"
	)

braveheart = media.Movie("Braveheart",
	"William Wallace faces the kindgom of England",
	"https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
	"https://www.youtube.com/watch?v=1NJO0jxBtMo",
	"1995"
	)

once_upon_a_time_in_the_west = media.Movie("Once Upon a Time in the West",
	"A mysterious harmonica player with a great talent for working with guns is the salvation",
	"https://upload.wikimedia.org/wikipedia/en/a/a2/Once_upon_a_Time_in_the_West.jpg",
	"https://www.youtube.com/watch?v=Yw-Av9BpC-w",
	"1968"
	)

daredevil = media.Series("Daredevil",
	"A blind man saves Hell's Kitchen",
	"https://upload.wikimedia.org/wikipedia/en/1/1b/Daredevil_season_1_poster.jpg",
	"https://www.youtube.com/watch?v=jAy6NJ_D5vU",
	"2015"
	)

jessica_jones = media.Series("Jessica Jones",
	"PI Jessica Jones solves cases involving people with special abilities",
	"https://upload.wikimedia.org/wikipedia/en/c/c1/Jessica_Jones_season_1_poster.jpg",
	"https://www.youtube.com/watch?v=nWHUjuJ8zxE",
	"2015"
	)

iron_fist = media.Series("Iron Fist",
	"The lost billionaire comes back as the Iron Fist",
	"https://upload.wikimedia.org/wikipedia/en/e/ef/Iron_Fist_season_1_poster.jpg",
	"https://www.youtube.com/watch?v=f9OKL5no-S0",
	"2017"
	)

luke_cage = media.Series("Luke Cage",
	"Luke Cage fights crime in Harlem with superhuman strength and unbreakable skin",
	"https://upload.wikimedia.org/wikipedia/en/3/37/Luke_Cage_season_1_poster.jpeg",
	"https://www.youtube.com/watch?v=ytkjQvSk2VA",
	"2016"
	)

the_punisher = media.Series("The Punisher",
	"Frank Castle seeks revenge for the death of his family",
	"https://upload.wikimedia.org/wikipedia/en/2/21/The_Punisher_season_1_poster.jpg",
	"https://www.youtube.com/watch?v=lIY6zFL95hE",
	"2017"
	)

the_defenders = media.Series("The Defenders",
	"Four fighters team up to fight a common enemy",
	"https://cdn-images-1.medium.com/max/1200/1*m_4m--YDwlmc8UKB4Wd8Yg.jpeg",
	"https://www.youtube.com/watch?v=QNwjRfSldM0",
	"2017"
	)

movies = [toy_story, avatar, blood_diamond, gladiator, braveheart, once_upon_a_time_in_the_west,
         daredevil, jessica_jones, iron_fist, luke_cage, the_punisher, the_defenders]
fresh_tomatoes.open_movies_page(movies)
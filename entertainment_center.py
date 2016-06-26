import media
import making_website

toy_story=media.Movie("Toy Story","A story of a boy and his toys that come to life","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc");

angry_birds=media.Movie("Angry Birds","A film based on the game Angry Birds","https://upload.wikimedia.org/wikipedia/en/f/f9/The_Angry_Birds_Movie_poster.png","https://www.youtube.com/watch?v=1U2DKKqxHgE");

kabali=media.Movie("Kabali","A film on a Gangster named Kabali","https://upload.wikimedia.org/wikipedia/en/9/9e/Rajinikanth_in_Kabali.jpg","https://www.youtube.com/watch?v=HfRQOc9WgnY");

dark_night=media.Movie("THE DARK NIGHT","A film shows confict between Superhero Batman and Joker","https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg","https://www.youtube.com/watch?v=EXeTwQWrcwY");

avengers=media.Movie("Avengers","A film of all Marvel Superheroes","https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg","https://www.youtube.com/watch?v=eOrNdBpGMv8");

monsters_inc=media.Movie("Monsters,INC.","A Story about Monsters and a little girl","https://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG","https://www.youtube.com/watch?v=8IBNZ6O2kMk");

movies=[angry_birds,toy_story,kabali,dark_night,avengers,monsters_inc]
making_website.make_website(movies);





















#Class Variables
#print(media.Movie.VALID_RATINGS);
#Predefined Class Variables
#print(media.Movie.__doc__);
#print(media.Movie.__name__);
#print(media.Movie.__dict__);
#print(media.Movie.__module__);
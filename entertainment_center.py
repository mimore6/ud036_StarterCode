import fresh_tomatoes
import media

#multiple instance of the movie class

fight_club = media.Movie("Fight Club", 
	"An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soapmaker, forming an underground fight club that evolves into something much, much more.",
	"https://images-na.ssl-images-amazon.com/images/I/81D%2BKJkO4SL._SL1500_.jpg",
	"https://www.youtube.com/watch?v=SUXWAEX2jlg")

spirited_away = media.Movie("Spirited Away", "A girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beast.",
	"https://fontmeme.com/images/USA_full-spirited-away-poster.jpg", "https://www.youtube.com/watch?v=ByXuk9QqQkk")

american_history_x = media.Movie("American History X", "A former neo-nazi skinhead tries to prevent his younger brother from going down the same wrong path that he did.",
	"http://www.movieposter.com/posters/archive/main/92/MPW-46054", "https://www.youtube.com/watch?v=JsPW6Fj3BUI")

requiem_for_a_dream = media.Movie("Requiem for a dream", "The drug-induced utopias of four Coney Island people are shattered when their addictions run deep.",
	"https://images-na.ssl-images-amazon.com/images/I/81w-bqfpe1L._RI_.jpg", "https://www.youtube.com/watch?v=jzk-lmU4KZ4")

princess_mononoke = media.Movie("Princess Mononoke", "On a journey to find the cure for a Tatarigami's curse, Ashitaka finds himself in the middle of a war between the forest gods and Tatara, a mining colony. In this quest he also meets San, the Mononoke Hime.",
	"https://images-na.ssl-images-amazon.com/images/I/51Xl0K7PlUL.jpg", "https://www.youtube.com/watch?v=pkWWWKKA8jY")

the_usual_suspects = media.Movie("The Usual Suspects", "A sole survivor tells of the twisty events leading up to a horrific gun battle on a boat, which began when five criminals met at a seemingly random police lineup.", "https://img1.etsystatic.com/000/0/5148979/il_570xN.250541837.jpg",
	"https://www.youtube.com/watch?v=oiXdPolca5w")


#movie array to use with fresh_tomatoes.py
movies =[fight_club, spirited_away, american_history_x, requiem_for_a_dream, princess_mononoke, the_usual_suspects]
#create website using the provided movies
fresh_tomatoes.open_movies_page(movies)




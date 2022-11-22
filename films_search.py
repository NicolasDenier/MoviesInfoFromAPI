import filmsparsing.info_film_facade
from filmsparsing import InfoFilmAll

def main():
    get_id = filmsparsing.info_film_facade.InfoFilmFacade.get_info_films()
    info_film = filmsparsing.info_film_facade.InfoFilmFacade.get_ratings_film(get_id.id)
    print("Full Title: ",info_film.fullTitle)
    print("Plot: ",info_film.plot)
    print("Rating: ",info_film.imDbRating)
    print("Directors: ",info_film.directors)
    print("")

if __name__ == "__main__":
    main()
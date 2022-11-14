import filmsparsing.info_film_facade

def main():
    print("films: ")
    info_films = filmsparsing.info_film_facade.InfoFilmFacade.get_info_films()
    for info_film in info_films:
        print(info_film)
        rating = filmsparsing.info_film_facade.InfoFilmFacade.get_ratings_film(info_film.id)
        print("Rating: ",rating)
        print("")

if __name__ == "__main__":
    main()
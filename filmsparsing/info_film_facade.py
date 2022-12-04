from filmsparsing import IMDbRequest, InfoFilm, InfoFilmAll

class InfoFilmFacade:

    def get_info_films(filmName) -> [InfoFilm]:
        films = []
        response = IMDbRequest.get_films(filmName)
        
        for film in response.content:
            film_info = InfoFilm(film['title'], film['description'], film['id'])
            films.append(film_info)
            # keep only first 5 results
            if len(films)>4:
                break
        return films
    
    def get_ratings_film(id):
        response = IMDbRequest.get_ratings(id)
        rating = response.content["imDb"]
        intRating = 0 if (rating=="") else round(float(rating))
        # Transform a number to a series of stars in html
        stars=""
        for i in range(10):
            filled = "filled" if (intRating>i) else "not-filled"
            stars+= f"<span class='star {filled}'>&starf;</span>"
        return stars

    def get_all_info_film(id):
        film = IMDbRequest.get_all_info(id).content
        infos_film = InfoFilmAll(film['fullTitle'], film['plot'], film['imDbRating'], film['directors'], film['image'], film['actorList'])
        return infos_film

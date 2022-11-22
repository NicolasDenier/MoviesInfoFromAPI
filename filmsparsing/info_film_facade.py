from filmsparsing import IMDbRequest
from filmsparsing import InfoFilm
from filmsparsing import InfoFilmAll

class InfoFilmFacade:

    def get_info_films() -> [InfoFilm]:
        films = []

        try:
            response = IMDbRequest.get_films()
        except:
            print("Error, no internet")
            return films
         
        # in case of request failure
        if response.status_code != 200:
            print("Error, response code ", response.status_code)
            return films

        for film in response.content:
            film_info = InfoFilm(film['title'], film['description'], film['id'])
            films.append(film_info)
        
        return films[0]
    
    def get_ratings_film(id) -> [InfoFilmAll]:
        rating = ""

        try:
            response = IMDbRequest.get_ratings(id)
        except:
            print("Error, no internet")
            return rating
         
        # in case of request failure
        if response.status_code != 200:
            print("Error, response code ", response.status_code)
            return rating
        
        film = response.content
        infos_film = InfoFilmAll(film['fullTitle'], film['plot'], film['imDbRating'], film['directors'], film['image'], film['actorList'])
        
        return infos_film

from filmsparsing import IMDbRequest
from filmsparsing import InfoFilm

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
        
        return films
    
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
        
        rating = InfoFilmAll(film['title'], film['description'], film['id'])
        
        return rating

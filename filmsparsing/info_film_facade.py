from filmsparsing import IMDbRequest
from filmsparsing import InfoFilm

class InfoFilmFacade:

    def get_info_films(filmName) -> [InfoFilm]:
        films = []
        response = IMDbRequest.get_films(filmName)
        
        for film in response.content:
            film_info = InfoFilm(film['title'], film['description'], film['id'])
            films.append(film_info)
        return films
    
    def get_ratings_film(id):
        response = IMDbRequest.get_ratings(id)
        rating = response.content["imDb"]
        return rating

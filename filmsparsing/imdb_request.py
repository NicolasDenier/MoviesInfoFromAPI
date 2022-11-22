import requests
from decouple import config
from filmsparsing.response import Response

class IMDbRequest:
    _base_url = "https://imdb-api.com/en/API/"
        
    @classmethod
    def get_films(cls):
        search = input("Film to search: ")
        response = requests.get(cls._base_url+'SearchMovie/'+config('API_KEY')+"/"+search)
        return Response(status_code=response.status_code, content=response.json()['results'])
    
    @classmethod
    def get_ratings(cls, id):
        response = requests.get(cls._base_url+'Title/'+config('API_KEY')+"/"+id)
        return Response(status_code=response.status_code, content=response.json())
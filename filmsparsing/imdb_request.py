import requests
from decouple import config
from filmsparsing.response import Response
from flask import abort

class IMDbRequest:
    _base_url = "https://imdb-api.com/en/API/"

    @classmethod
    def _try_request(cls, request):
        '''
        Try to request the data server and handle errors
        Input: 
            request, string containing an URL to request
        Output:
            A response to the request from the remote server, or None in case of failure
        '''
        response = None
        try:
            response = requests.get(request)
        except:
            # it cannot reach the IMDb server
            print("Error, no internet or erroneous URL")
            abort(404, "No internet or erroneous URL")
         
        # In case of request failure from the IMDb server
        if response.status_code != 200:
            print("Error, response code ", response.status_code)
            abort(response.status_code, "response code "+str(response.status_code))

        # In case the API key is expired temporarly (restricted to 100 request per day)
        if response.json()['errorMessage'] != "" and response.json()['errorMessage'] != None:
            print("Error from IMDb server: ", response.json()['errorMessage'])
            abort(403, "From IMDb server: "+response.json()['errorMessage'])
        
        return response
        
    @classmethod
    def get_films(cls, filmName):
        request = f"{cls._base_url}SearchMovie/{config('API_KEY')}/{filmName}"
        response = cls._try_request(request)

        if response == None:
            return Response(status_code=None, content=[])
        return Response(status_code=response.status_code, content=response.json()['results'])
    
    @classmethod
    def get_ratings(cls, id):
        request = f"{cls._base_url}Ratings/{config('API_KEY')}/{id}"
        response = cls._try_request(request)
        
        if response == None:
            return Response(status_code=None, content="")
        return Response(status_code=response.status_code, content=response.json())
    
    @classmethod
    def get_all_info(cls, id):
        request = f"{cls._base_url}Title/{config('API_KEY')}/{id}"
        response = cls._try_request(request)
        
        if response == None:
            return Response(status_code=None, content="")
        return Response(status_code=response.status_code, content=response.json())
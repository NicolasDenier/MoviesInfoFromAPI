# MoviesInfoFromAPI

## Description

Search for movies, fetch information from the [IMDb API](https://imdb-api.com/API) and display them in a web interface.

## Installation

First, download the files from this repository:  
`git clone https://github.com/NicolasDenier/MoviesInfoFromAPI.git`

### Dependencies

To install the dependencies, run `pip install -r requirements.txt`  
It will install the following libraries:

- [requests](https://pypi.org/project/requests/)
- [flask](https://flask.palletsprojects.com/en/2.2.x/)
- [python-decouple](https://pypi.org/project/python-decouple/)

### API access

To access the [IMDb API](https://imdb-api.com/API), register on their website and you will get a key.  
Add a `.env` file and write it your key: `API_KEY=yourKey`

## Run

Run the app with:  
`flask --app films_search run`

Then, go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see it.

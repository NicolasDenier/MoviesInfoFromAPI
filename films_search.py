from flask import Flask, request, render_template, redirect, url_for
from werkzeug.exceptions import HTTPException
from markupsafe import escape # to escape user inputs and so avoid injection attacks
import filmsparsing.info_film_facade
from filmsparsing import InfoFilmAll

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    return render_template("main.html")

@app.route("/search/", methods=["GET", "POST"])
def search():
    if request.method == 'POST':
        filmName=escape(request.form.get("filmName"))
        if filmName is not None or filmName != "":
            return redirect(url_for('films', filmName=filmName))
    return render_template("search_films.html")

@app.route("/films/<filmName>")
def films(filmName):
    filmName = escape(filmName)
    todisplay = render_template("films.html")
    info_films = filmsparsing.info_film_facade.InfoFilmFacade.get_info_films(filmName)

    for info_film in info_films:
        todisplay+="<div class='card'>\n"
        todisplay+=f"<p>{info_film}"
        rating = filmsparsing.info_film_facade.InfoFilmFacade.get_ratings_film(info_film.id)
        todisplay+=f"<b>Rating:</b> {rating}</p>\n"
        todisplay+="</div>\n"
    return todisplay


@app.errorhandler(HTTPException)
def HTTPError(e):
    return redirect(url_for('error', error_description=escape(e.description)))

@app.route('/error/')
@app.route('/error/<error_description>')
def error(error_description=""):
    return render_template('error.html', error_description=escape(error_description))

@app.route("/film/<ID>")
def film(ID):
    info_film = filmsparsing.info_film_facade.InfoFilmFacade.get_ratings_film(ID)
    todisplay = render_template("film_all.html")
    todisplay+=f"<div class='card'>\n<h1>{info_film.fullTitle}</h1>\n</div>\n"
    todisplay+="<div class='card'>\n"
    todisplay+=f"<p><b>  Rating: </b> {info_film.imDbRating} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>  Director: </b> {info_film.directors} </p>\n"
    todisplay+="</div>\n"
    todisplay+=f"<div class='plot'>\n<p ><b>Plot: </b> {info_film.plot}</p>\n</div>\n"
    todisplay+="<div class='space'>\n</div>\n"
    todisplay+="<div class='container'>\n"
    todisplay+=f"<div class='affiche'>\n<img src={info_film.image}>\n</div>\n"
    todisplay+="<div class='space'>\n</div>\n"
    todisplay+="<div class='actors'>\n"
    todisplay+=f"<img src={info_film.actorList[0]['image']} width = '300' height = '300'>"
    todisplay+=f"<img src={info_film.actorList[1]['image']} width = '300' height = '300'>"
    todisplay+=f"<img src={info_film.actorList[2]['image']} width = '300' height = '300'>"
    todisplay+="</div>\n"
    todisplay+="<div class='container_actor_names'>\n"
    todisplay+=f"<div class='actor_names'>\n<p >{info_film.actorList[0]['name']}</p></div>\n"
    todisplay+=f"<div class='actor_names'>\n<p >{info_film.actorList[1]['name']}</p></div>\n"
    todisplay+=f"<div class='actor_names'>\n<p >{info_film.actorList[2]['name']}</p></div>\n"
    todisplay+="</div>\n"
    todisplay+="</div>\n"
    return todisplay

if __name__ == "__main__":
    app.run()

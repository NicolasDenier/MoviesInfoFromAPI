from flask import Flask, request, render_template, redirect, url_for
from werkzeug.exceptions import HTTPException
from markupsafe import escape # to escape user inputs and so avoid injection attacks
import filmsparsing.info_film_facade

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
    info_films = filmsparsing.info_film_facade.InfoFilmFacade.get_info_films(filmName)
    cards = ""
    for info_film in info_films:
        rating = filmsparsing.info_film_facade.InfoFilmFacade.get_ratings_film(info_film.id)
        cards+= render_template("card.html", ID=info_film.id, title=info_film.title, description=info_film.description, rating=rating)
    display = render_template("films.html",cards=cards)
    return display

@app.route("/film/<ID>")
def film(ID):
    ID = escape(ID)
    info_film = filmsparsing.info_film_facade.InfoFilmFacade.get_all_info_film(ID)
    display = render_template("film_all.html", info_film=info_film)
    return display

@app.errorhandler(HTTPException)
def HTTPError(e):
    return redirect(url_for('error', error_description=escape(e.description)))

@app.route('/error/')
@app.route('/error/<error_description>')
def error(error_description=""):
    return render_template('error.html', error_description=escape(error_description))

if __name__ == "__main__":
    app.run()

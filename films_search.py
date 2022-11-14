from flask import Flask, request, render_template, redirect, url_for
from markupsafe import escape # to escape user inputs and so avoid injection attacks
import filmsparsing.info_film_facade

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    print(request.method)
    if request.method == 'POST':
        filmName=escape(request.form.get("filmName"))
        print(filmName)
        if filmName is not None:
            return redirect(url_for('films', filmName=filmName))
    return render_template("search_films.html")
    

@app.route("/films/<filmName>")
def films(filmName):
    todisplay = "<h1>Films Infos</h1>\n"
    info_films = filmsparsing.info_film_facade.InfoFilmFacade.get_info_films(filmName)

    for info_film in info_films:
        todisplay+=f"<p>{info_film}"
        rating = filmsparsing.info_film_facade.InfoFilmFacade.get_ratings_film(info_film.id)
        todisplay+=f"<b>Rating:</b> {rating}</p>\n"
    return todisplay

if __name__ == "__main__":
    app.run()
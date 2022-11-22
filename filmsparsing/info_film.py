class InfoFilm:
    def __init__(self, title, description, id):
        self.title = title
        self.description = description
        self.id = id
    
    def __repr__(self) -> str:
        return f"title: {self.title}\ndescription: {self.description}\n"


class InfoFilmAll:
    def __init__(self, fullTitle, plot, imDbRating):
        self.title = fullTitle
        self.plot = plot
        self.imDbRating = imDbRating
    
    def __repr__(self) -> str:
        return f"fulltitle: {self.fullTitle}\rimDbrating: {self.imDbRating}\n"
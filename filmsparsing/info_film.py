class InfoFilm:
    def __init__(self, title, description, id):
        self.title = title
        self.description = description
        self.id = id
    
    def __repr__(self) -> str:
        return f"Title: {self.title}\nDescription: {self.description}\n"


class InfoFilmAll:
    def __init__(self, fullTitle, plot, imDbRating, runtimeStr, directors, image, actorList):
        self.fullTitle = fullTitle
        self.plot = plot
        self.imDbRating = imDbRating
        self.runtimeStr = runtimeStr
        self.directors = directors
        self.image = image
        self.actorList = actorList
        
    
    def __repr__(self) -> str:
        return f"fulltitle: {self.fullTitle}\rimDbrating: {self.imDbRating}\n"
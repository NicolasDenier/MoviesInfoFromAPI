class InfoFilm:
    def __init__(self, title, description, id):
        self.title = title
        self.description = description
        self.id = id
    
    def __repr__(self) -> str:
        return f"Title: {self.title}\nDescription: {self.description}\n"
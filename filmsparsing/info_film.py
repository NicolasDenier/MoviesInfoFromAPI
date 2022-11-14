class InfoFilm:
    def __init__(self, title, description, id):
        self.title = title
        self.description = description
        self.id = id
    
    def __repr__(self) -> str:
        return f"<b>title:</b> {self.title}<br><b>description:</b> {self.description}<br>"
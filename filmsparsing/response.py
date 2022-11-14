class Response:
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}\n status_code:{self.status_code}\n content:{self.content}"
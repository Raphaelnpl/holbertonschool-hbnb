from models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

def __repr__(self):
        return f"User(id={self.id}, name='{self.name}')"
    
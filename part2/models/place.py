from models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, name, location, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.location = location

    def __repr__(self):
        return f"Place(id={self.id}, name='{self.name}')"

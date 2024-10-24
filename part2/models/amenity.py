from models.base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

def __repr__(self):
        return f"Amenity(id={self.id}, name='{self.name}')"

from models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text, user_id, place_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = text
        self.user_id = user_id
        self.place_id = place_id

    def __repr__(self):
        return f"Review(id={self.id}, text='{self.text}')"

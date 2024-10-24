import unittest
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User(id="1234", name="Alice")
        self.assertEqual(user.name, "Alice")

class TestPlace(unittest.TestCase):
    def test_place_creation(self):
        place = Place(name="The Plaza", location="NYC")
        self.assertEqual(place.name, "The Plaza")

class TestReview(unittest.TestCase):
    def test_review_creation(self):
        review = Review(text="Great place!", user_id="1234", place_id="5678")
        self.assertEqual(review.text, "Great place!")

class TestAmenity(unittest.TestCase):
    def test_amenity_creation(self):
        amenity = Amenity(name="WiFi")
        self.assertEqual(amenity.name, "WiFi")

if __name__ == '__main__':
    unittest.main()

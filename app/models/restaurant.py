from app import db

class Restaurant(db.Model):
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        name = db.Column(db.String)
        rating = db.Column(db.Integer)
        cuisine = db.Column(db.String)
        distance_from_ada = db.Column(db.Integer)

        def to_dict(self): 
                return {
            "id": self.id,
            "name": self.name,
            "rating": self.rating,
            "cuisine": self.cuisine,
            "distance_from_ada": self.distance_from_ada
        }
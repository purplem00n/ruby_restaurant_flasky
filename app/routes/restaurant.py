from flask import Blueprint, jsonify

restaurant_bp = Blueprint("restaurant", __name__, url_prefix="/restaurant")

class Restaurant():
    def __init__(self, id, name, rating, cuisine, distance_from_ada):
        self.id = id
        self.name = name
        self.rating = rating
        self.cuisine = cuisine
        self.distance_from_ada = distance_from_ada

restaurant1 = Restaurant(1, "Pizza Hut", 5, "Italian", 3.6)
restaurant2 = Restaurant(15, "Dominos", 2, "American", .2)
restaurant3 = Restaurant(9, "Hong Kong Bistro", 4.5, "Chinese", .1)

restaurants = [restaurant1, restaurant2, restaurant3]

@restaurant_bp.route("", methods=["GET"])
def get_restaurants():
    response = []
    for restaurant in restaurants:
        restaurant_dict = {
            "id": restaurant.id,
            "name": restaurant.name,
            "rating": restaurant.rating,
            "cuisine": restaurant.cuisine,
            "distance_from_ada": restaurant.distance_from_ada
        }
        response.append(restaurant_dict)
    return jsonify(response), 200



from flask import Blueprint, jsonify, request, make_response
from app import db
from app.models.restaurant import Restaurant

restaurant_bp = Blueprint("restaurant", __name__, url_prefix="/restaurant")

@restaurant_bp.route("", methods=["POST"])
def add_restaurant():
    request_body = request.get_json()
    new_restaurant = Restaurant(
        name = request_body["name"],
        rating = request_body["rating"],
        cuisine = request_body["cuisine"],
        distance_from_ada = request_body["distance_from_ada"]
        )
    
    db.session.add(new_restaurant)
    db.session.commit()
    return make_response(f"id: {new_restaurant.id}", 201)


# restaurant1 = Restaurant(1, "Pizza Hut", 5, "Italian", 3.6)
# restaurant2 = Restaurant(15, "Dominos", 2, "American", .2)
# restaurant3 = Restaurant(9, "Hong Kong Bistro", 4.5, "Chinese", .1)

# restaurants = [restaurant1, restaurant2, restaurant3]

@restaurant_bp.route("", methods=["GET"])
def get_restaurants():
    response = []
    all_restaurants = Restaurant.query.all() # is a list of restaurant objects
    for restaurant in all_restaurants: # to convert the object into a dict
        response.append(restaurant.to_dict())
    return jsonify(response), 200

# @restaurant_bp.route("/<id>", methods=["GET"])
# def get_one_restaurant(id):
    
#     try:
#         restaurant_id = int(id)
#     except ValueError:
#         return {"message": f"invalid id: {id}"}, 400

#     for restaurant in restaurants:
#         if restaurant.id == restaurant_id:
#             return jsonify({
#             "id": restaurant.id,
    #         "name": restaurant.name,
    #         "rating": restaurant.rating,
    #         "cuisine": restaurant.cuisine,
    #         "distance_from_ada": restaurant.distance_from_ada
    #     }), 200

    # return {"message": f"id {restaurant_id} not found"}, 404

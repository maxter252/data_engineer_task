import json

from typing import List, Tuple
from pydantic import BaseModel, validator, Field, ValidationError

from scripts.models import User, Venue, Result, PlaceToAvoid, InputUser

def prnt(item):
    print(json.dumps(item, indent=4))

def get_data(users_path: str, venues_path: str) -> Tuple[dict]:
    users, venues = None, None
    with open(users_path,'r') as f:
        users = json.load(f)
    with open(venues_path,'r') as f:
        venues = json.load(f)
    return (users, venues)

def convert_to_dict(_list: list) -> dict:
        items = {}
        for elem in _list:
            items[elem] = 0
        return items

def transform_user_data(users: dict = {}) -> dict:
    output = []
    for user in users:
        InputUser(**user)
        user_model = User(
            name=user['name'], 
            wont_eat=convert_to_dict(user['wont_eat']),
            drinks=convert_to_dict(user['drinks'])
            )
        output.append(user_model)
            
    return output

def transform_venue_data(venues: dict) -> dict:
    output = []
    for venue in venues:
        venue_model = Venue(
            name=venue['name'], 
            food=convert_to_dict(venue['food']),
            drinks=convert_to_dict(venue['drinks'])
            )
        
        output.append(venue_model)
            
    return output

def check_for_edible_meal(foods: List[str], not_edible: dict) -> bool:
    """
    Check that there is at least one food type available for each person to drink
    """
    for food in foods: 
        if food not in not_edible.keys():
            return True
    return False

def check_for_drinks(drinks: List[str], drinkables: dict) -> bool:
    """
    Check that drinks that are available are within the list of drinks that
    each person drinks.
    """
    for drink in drinkables:
        if drink in drinks.keys():
            return True
    return False

def search_compatible_locations(venues: dict = {}, users: dict = {}) -> dict:
    result = Result()
    count = 0
    for venue in venues:
        valid_place = True
        for user in users:
            canDrink, canEat = check_for_drinks(venue.drinks,user.drinks), check_for_edible_meal(venue.food,user.wont_eat)
            if canDrink and canEat:
               continue
            else:
                valid_place = False
                reasons = []
                count += 1
                if not canDrink:
                    reasons.append(f"There is nothing for {user.name} to drink")
                if not canEat:
                    reasons.append(f"There is nothing for {user.name} to eat")
                place = PlaceToAvoid(name=venue.name,reasons=reasons)
                result.add_places_to_avoid(place)

        if valid_place:
            result.add_place_to_visit(venue.name)

    return result
        
def main(users_json: str = './data/users.json', venues_json: str = './data/venues.json') -> str:
    users, venues = get_data(users_json,venues_json)
    users, venues = transform_user_data(users), transform_venue_data(venues)
    result = search_compatible_locations(venues, users)
    prnt(result.to_dict())
    return result.to_dict()

if __name__ == '__main__':
    main()
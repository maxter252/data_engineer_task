from pydantic import BaseModel, validator, Field
from typing import List


class InputUser(BaseModel):
    name: str = Field(..., description='Name of the user')
    wont_eat: list = Field(..., description='Foods that a user wont eat')
    drinks: list = Field(..., description='Drinks that a user will drink')

    @validator('name', allow_reuse=True)
    def valid_name(cls, v):
        if len(v) == 0:
            raise ValueError('Name cannot be empty')
        return v

    @validator('drinks', allow_reuse=True)
    def drinks_cannot_be_empyty(cls, v):
        if len(v) == 0:
            raise ValueError('User must specify at least one drink')
        return v


class User(BaseModel):
    name: str = None
    wont_eat: dict = Field(..., description='Foods that a user wont eat')
    drinks: dict = Field(..., description='Drinks that a user will drink')


class Venue(BaseModel):
    name: str = None
    food: dict = Field(..., description='Foods available at the venue')
    drinks: dict = Field(..., description='Drinks available at the venue')


class PlaceToAvoid(BaseModel):
    name: str = None
    reasons: List[str] = None

    # TODO: Add this to main implementation
    def add_reason(self, reason: str):
        self.reasons.append(reason)


class Result():
    def __init__(self):
        self.places_to_visit = {}
        self.places_to_avoid = {}

    def to_dict(self):
        return {
            "places_to_visit": list(self.places_to_visit.keys()),
            "places_to_avoid": [{"name": place_name, "reason": self.places_to_avoid[place_name]}
                                for place_name in self.places_to_avoid.keys()]
        }

    def add_place_to_visit(self, place_name: str):
        if place_name not in self.places_to_visit.keys():
            self.places_to_visit[place_name] = None

    def add_places_to_avoid(self, place: PlaceToAvoid):
        if place.name not in self.places_to_avoid.keys():
            self.places_to_avoid[place.name] = place.reasons
        else:
            self.places_to_avoid[place.name] += place.reasons

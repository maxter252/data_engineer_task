import unittest

from pydantic import ValidationError

from scripts.models import Result, PlaceToAvoid, User, Venue, InputUser


class test_models(unittest.TestCase):
    def test_user_input(self):
        input_user_json = {
            "name": "Karol Drewno",
            "wont_eat": ["Bread", "Pasta"],
            "drinks": []
        }

        self.assertRaises(ValidationError, InputUser, **input_user_json)

    def test_result_class(self):
        result = Result()

        place = PlaceToAvoid(name="test_venue",reasons=['reason1', 'reason2'])
        result.add_places_to_avoid(place)

        self.assertEqual(result.places_to_avoid,{"test_venue": ['reason1', 'reason2']})

    def test_user_model(self):
        user = User(name='Max',wont_eat={'food1':0,'food2':0},drinks={'drink1':0,'drink2':0})
        expected = {'name':'Max', 'wont_eat': {'food1':0,'food2':0}, 'drinks': {'drink1':0,'drink2':0}}
        self.assertEqual(user.dict(),expected)

    def test_venue_model(self):
        venue = Venue(
            name='Maxs', 
            food={'food1':0,'food2':0},
            drinks={'drink1':0,'drink2':0}
            )
        expected = {'name':'Maxs', 'food': {'food1':0,'food2':0}, 'drinks': {'drink1':0,'drink2':0}}
        self.assertEqual(venue.dict(),expected)

    def test_place_to_avoid_model(self):
        place = PlaceToAvoid( name='max', reasons=['hi'])
        expected = {'name': 'max', 'reasons': ['hi']}
        self.assertEqual(place.dict(),expected)
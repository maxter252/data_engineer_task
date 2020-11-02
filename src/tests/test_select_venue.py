import unittest

from pydantic import ValidationError

from scripts.select_venue import main


class test_select_venue(unittest.TestCase):
    def test_main_minimal(self):
        result = main('./src/tests/data/users.json', './src/tests/data/venues.json')
        expected = {
            "places_to_visit": [
                "The Cambridge"
            ],
            "places_to_avoid": [
                {
                    "name": "El Cantina",
                    "reason": [
                        "There is nothing for Karol Drewno to drink",
                        "There is nothing for Rosie Curran to eat"
                    ]
                }
            ]
        }

        self.assertEqual(result, expected)

    def test_main_full(self):
        result = main('./data/users.json', './data/venues.json')
        expected = {
            "places_to_visit": [
                "Spice of life",
                "The Cambridge"
            ],
            "places_to_avoid": [
                {
                    "name": "El Cantina",
                    "reason": [
                        "There is nothing for Karol Drewno to drink",
                        "There is nothing for Rosie Curran to eat"
                    ]
                },
                {
                    "name": "Twin Dynasty",
                    "reason": [
                        "There is nothing for Cristiana Lusitano to drink",
                        "There is nothing for Tom Mullen to drink",
                        "There is nothing for Wen Li to eat"
                    ]
                },
                {
                    "name": "Wagamama",
                    "reason": [
                        "There is nothing for Cristiana Lusitano to drink",
                        "There is nothing for Karol Drewno to drink",
                        "There is nothing for Tom Mullen to drink"
                    ]
                },
                {
                    "name": "Sultan Sofrasi",
                    "reason": [
                        "There is nothing for Cristiana Lusitano to drink",
                        "There is nothing for Karol Drewno to drink",
                        "There is nothing for Tom Mullen to drink"
                    ]
                },
                {
                    "name": "Spirit House",
                    "reason": [
                        "There is nothing for Tom Mullen to drink"
                    ]
                },
                {
                    "name": "Tally Joe",
                    "reason": [
                        "There is nothing for Cristiana Lusitano to drink",
                        "There is nothing for Karol Drewno to drink",
                        "There is nothing for Tom Mullen to drink"
                    ]
                },
                {
                    "name": "Fabrique",
                    "reason": [
                        "There is nothing for Danielle Ren to drink",
                        "There is nothing for Karol Drewno to drink",
                        "There is nothing for Gaston Chambray to drink",
                        "There is nothing for Rosie Curran to drink",
                        "There is nothing for Wen Li to drink"
                    ]
                }
            ]
        }

        self.assertEqual(result, expected)

    def test_main_malformed_data(self):
        self.assertRaises(ValidationError,
                          main,
                          './src/tests/data/malformed_users.json',
                          './src/tests/data/malformed_venues.json')

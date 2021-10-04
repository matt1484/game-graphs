from fastapi.testclient import TestClient
import unittest

from api import api

class TestGamesAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(api)

    def test_get_games_api(self):
        expected_games = [{
            "genre": "Simulation",
            "id": 5959,
            "platform": "DS",
            "na_sales": 0.27,
            "eu_sales": 0,
            "other_sales": 0.02,
            "release_year": 2020,
            "title": "Imagine: Makeup Artist",
            "publisher": "Ubisoft",
            "jp_sales": 0,
        }]
        resp = self.client.get('/api/games?release_year=2020')
        self.assertEqual(200, resp.status_code, 'had invalid status for GET /api/games')
        self.assertEqual(expected_games, resp.json(), 'had unexpected response body')

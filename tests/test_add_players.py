import unittest
from controllers.leaderboardcontroller import LeaderboardController
from models.leaderboard import Leaderboard
from models.player import Player

class TestAddPlayers(unittest.TestCase):

    leaderboard_controller = None

    def setUp(self):
        leaderboard = Leaderboard("test_leaderboard", [Player("dan"), Player("mike"), Player("sandeep")])
        leaderboards = [leaderboard]
        self.leaderboard_controller = LeaderboardController(leaderboards, "test_leaderboard")

    def test_add_players_valid(self):
        new_players = ["james", "ben", "malik"]
        existing_players = ["dan", "mike", "sandeep"]

        players_not_added = self.leaderboard_controller.add_players(new_players)
        players = self.leaderboard_controller.get_active_leaderboard().get_players()

        self.assertEquals(len(players), len(existing_players + new_players))
        self.assertListEqual(players_not_added, [])

if __name__ == '__main__':
    unittest.main()
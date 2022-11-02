import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [ 
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

#search
    def test_returns_player_that_exists(self):
        name = self.statistics.search("Semenko")
        self.assertAlmostEqual(str(name), "Semenko EDM 4 + 12 = 16")

    def test_returns_none_when_player_does_not_exist(self):
        name = self.statistics.search("Moi")
        self.assertAlmostEqual(name, None)

#team
    def test_returns_correct_amount_of_players(self):
        players = self.statistics.team("PIT")
        players_amount = len(players)
        self.assertAlmostEqual(players_amount, 1)

#top
    def test_returns_correct_amount_of_top_scorers(self):
        scorers = self.statistics.top(4)
        self.assertAlmostEqual(len(scorers), 4)

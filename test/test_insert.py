import unittest, sys
from sql_runner import SQLRunner
sys.path.insert(0, '..')
from queries import *

sql_runner = SQLRunner()
cursor = sql_runner.execute_create_file()
cursor = sql_runner.execute_insert_file()

class TestInsertData(unittest.TestCase):

    def test_leagues_insert(self):
        self.assertEqual(cursor.execute("SELECT COUNT(*) FROM leagues;").fetchone()[0], 2)

    def test_teams_insert(self):
        self.assertEqual(cursor.execute("SELECT COUNT(*) FROM teams;").fetchone()[0], 4)

    def test_players_insert(self):
        self.assertTrue(cursor.execute("SELECT COUNT(*) FROM players;").fetchone()[0] >= 4)
        self.assertTrue(len(cursor.execute("SELECT * FROM players WHERE team_id = 1;").fetchall()) >= 1)
        self.assertTrue(len(cursor.execute("SELECT * FROM players WHERE team_id = 2;").fetchall()) >= 1)
        self.assertTrue(len(cursor.execute("SELECT * FROM players WHERE team_id = 3;").fetchall()) >= 1)
        self.assertTrue(len(cursor.execute("SELECT * FROM players WHERE team_id = 4;").fetchall()) >= 1)

    def test_games_insert(self):
        self.assertEqual(cursor.execute("SELECT COUNT(*) FROM games;").fetchone()[0], 3)

    def test_team_games_insert(self):
        self.assertEqual(cursor.execute("SELECT COUNT(*) FROM team_games;").fetchone()[0], 6)

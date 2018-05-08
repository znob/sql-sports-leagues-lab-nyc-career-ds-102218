import unittest, sys
from sql_runner import SQLRunner
sys.path.insert(0, '..')
from queries import *

sql_runner = SQLRunner()
cursor = sql_runner.execute_create_file()

class TestCreateTables(unittest.TestCase):

    def test_leagues_table(self):
        leagues = cursor.execute("SELECT name FROM sqlite_master WHERE name='leagues';").fetchone()[0]
        column_data = cursor.execute("PRAGMA table_info('%s')" % leagues).fetchall()
        self.assertEqual(column_data[0][1] + " " + column_data[0][2], "id INTEGER")
        self.assertEqual(column_data[1][1] + " " + column_data[1][2], "name TEXT")

    def test_teams_table(self):
        teams = cursor.execute("SELECT name FROM sqlite_master WHERE name='teams';").fetchone()[0]
        column_data = cursor.execute("PRAGMA table_info('%s')" % teams).fetchall()
        self.assertEqual(column_data[0][1] + " " + column_data[0][2], "id INTEGER")
        self.assertEqual(column_data[1][1] + " " + column_data[1][2], "name TEXT")
        self.assertEqual(column_data[2][1] + " " + column_data[2][2], "league_id INTEGER")

    def test_players_table(self):
        players = cursor.execute("SELECT name FROM sqlite_master WHERE name='players';").fetchone()[0]
        column_data = cursor.execute("PRAGMA table_info('%s')" % players).fetchall()
        self.assertEqual(column_data[0][1] + " " + column_data[0][2], "id INTEGER")
        self.assertEqual(column_data[1][1] + " " + column_data[1][2], "name TEXT")
        self.assertEqual(column_data[2][1] + " " + column_data[2][2], "team_id INTEGER")

    def test_games_table(self):
        games = cursor.execute("SELECT name FROM sqlite_master WHERE name='games';").fetchone()[0]
        column_data = cursor.execute("PRAGMA table_info('%s')" % games).fetchall()
        self.assertEqual(column_data[0][1] + " " + column_data[0][2], "id INTEGER")
        self.assertEqual(column_data[1][1] + " " + column_data[1][2], "date DATE")
        self.assertEqual(column_data[2][1] + " " + column_data[2][2], "location TEXT")

    def test_team_games_table(self):
        team_games = cursor.execute("SELECT name FROM sqlite_master WHERE name='team_games';").fetchone()[0]
        column_data = cursor.execute("PRAGMA table_info('%s')" % team_games).fetchall()
        self.assertEqual(column_data[0][1] + " " + column_data[0][2], "id INTEGER")
        self.assertEqual(column_data[1][1] + " " + column_data[1][2], "team_id INTEGER")
        self.assertEqual(column_data[2][1] + " " + column_data[2][2], "game_id INTEGER")
        self.assertEqual(column_data[3][1] + " " + column_data[3][2], "score INTEGER")

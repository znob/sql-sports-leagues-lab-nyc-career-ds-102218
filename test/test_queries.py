import unittest, sys
from sql_runner import SQLRunner
sys.path.insert(0, '..')
from queries import *

sql_runner = SQLRunner()
cursor = sql_runner.execute_create_file()
cursor = sql_runner.execute_seed_file()

class TestSQLQueries(unittest.TestCase):

    def test_select_name_of_player_with_shortest_name(self):
        result = 'Pavel Bure'
        self.assertEqual(cursor.execute(select_name_of_player_with_shortest_name()).fetchone()[0], result)

    def test_select_all_new_york_players_names(self):
        result = [('Brian Leetch',), ('Jeff Beukeboom',), ('Mark Messier',), ('Adam Graves',), ('Alexei Kovalev',), ('Mike Richter',), ('Patrick Ewing',), ('Charles Oakley',), ('John Starks',), ('Anthony Mason',), ('Derek Harper',)]
        self.assertEqual(cursor.execute(select_all_new_york_players_names()).fetchall(), result)

    def test_select_team_name_and_total_goals_scored_for_new_york_rangers(self):
        result = [('New York Rangers', 21)]
        self.assertEqual(cursor.execute(select_team_name_and_total_goals_scored_for_new_york_rangers()).fetchall(), result)

    def test_select_all_games_date_and_info_teams_name_and_score_for_teams_in_nhl(self):
        result = [('1994-05-31', 'Stanley Cup Finals - Game 1', 'New York Rangers', 2), ('1994-05-31', 'Stanley Cup Finals - Game 1', 'Vancouver Canucks', 3), ('1994-06-02', 'Stanley Cup Finals - Game 2', 'New York Rangers', 3), ('1994-06-02', 'Stanley Cup Finals - Game 2', 'Vancouver Canucks', 1), ('1994-06-04', 'Stanley Cup Finals - Game 3', 'New York Rangers', 5), ('1994-06-04', 'Stanley Cup Finals - Game 3', 'Vancouver Canucks', 1), ('1994-06-07', 'Stanley Cup Finals - Game 4', 'New York Rangers', 4), ('1994-06-07', 'Stanley Cup Finals - Game 4', 'Vancouver Canucks', 2), ('1994-06-09', 'Stanley Cup Finals - Game 5', 'New York Rangers', 3), ('1994-06-09', 'Stanley Cup Finals - Game 5', 'Vancouver Canucks', 6), ('1994-06-11', 'Stanley Cup Finals - Game 6', 'New York Rangers', 1), ('1994-06-11', 'Stanley Cup Finals - Game 6', 'Vancouver Canucks', 4), ('1994-06-14', 'Stanley Cup Finals - Game 7', 'New York Rangers', 3), ('1994-06-14', 'Stanley Cup Finals - Game 7', 'Vancouver Canucks', 2)]
        self.assertEqual(cursor.execute(select_all_games_date_and_info_teams_name_and_score_for_teams_in_nhl()).fetchall(), result)

    def test_select_date_info_and_total_points_for_highest_scoring_nba_game(self):
        result = [('1994-06-12', 'NBA Finals - Game 3', 182)]
        self.assertEqual(cursor.execute(select_date_info_and_total_points_for_highest_scoring_nba_game()).fetchall(), result)

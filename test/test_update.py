import unittest, sys
from sql_runner import SQLRunner
sys.path.insert(0, '..')
from queries import *

sql_runner = SQLRunner()
cursor = sql_runner.execute_create_file()
cursor = sql_runner.execute_insert_file()
cursor = sql_runner.execute_update_file()

class TestUpdateTables(unittest.TestCase):

    def test_metta_world_peace(self):
        self.assertEqual(cursor.execute("SELECT name FROM players WHERE id = 1;").fetchone()[0], "Metta World Peace")

    def test_chad_ochocinco(self):
        self.assertEqual(cursor.execute("SELECT name FROM players WHERE id = 4;").fetchone()[0], "Chad OchoCinco")

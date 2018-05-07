import unittest
import sys
sys.path.insert(0, '..')
from sql_queries import *

connection = sqlite3.connect('../.db')
cursor = connection.cursor()

class TestJoinStatements(unittest.TestCase):

    file = open("../sql_queries.py", "r")
    file.read()


# SQL Sports Leagues Lab

We are going to build a SQL database to help sports leagues keep track of of their teams and players.  We also will be able to log games and keep track of scores.  In this lab we will utilize all of the tools we learned in the previous lessons and labs.  We will make tables for `leagues`, `teams`, `players`, and `games`, populate these tables with data and make the proper associations, and query from these tables to select interesting information.

## Objectives

1.  Review creating tables, altering tables, inserting data, and querying from tables
2.  Become comfortable working with common data relationships "has many"/"belongs to" and "many-to-many"
3.  Write advanced `SELECT` queries using `JOIN` statements and join tables

### Part 1: `create.sql`

Build the tables that will make up our Sports Leagues database.  Make sure the tables adhere to the following requirements:

1.  `leagues` has a name
2.  `teams` have a name and many players
3.  `players` have a name and belong to a team
4.  `games` have a date of the date datatype and a location
5.  `teams` have many games and `games` are played by many teams.  Since this relationship is "many-to-many", we will need a join table.  Let's call this join table `team_games`, and it will have foreign keys to track team and game ids.  These foreign keys are responsible for establishing the many-to-many relationship.  `team_games` will also have a column called score that keeps track of that team's score for that particular game.
6.  All tables will have an auto-incrementing `PRIMARY KEY` set to the integer data type


### Part 2: `insert.sql`

Once the tables are created, populate the database with data.  Feel free to create fictional leagues, teams, and games.  However, you tables should meet the following requirements.  There should be:

1.  2 leagues
2.  4 teams total, with 2 teams in each league
3.  1 player on each team
4.  3 total games, and teams are allowed to play teams from other leagues
5.  Lastly, we will need to log scores and the relevant team and game ids into the `team_games` join table to build out the "many-to-many" relationship

### Part 3: `update.sql`

Two players want to change their names.  Fix the `players` table so that the first player's name is switched to "Metta World Peace" and the last player's name is changed to "Chad OchoCinco".

### Part 4: `queries.py`

Write queries in the `queries.py` file to get the tests to pass.  We have seeded the database with different data, so don't expect the data your input in the above files to be returned in your queries.

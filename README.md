
# SQL Sports Leagues Lab

We are going to build a SQL database to help sports leagues keep track of of their teams and players.  We also will be able to log games and keep track of scores.  In this lab we will utilize all of the tools we learned in the previous lessons and labs.  We will make tables for `leagues`, `teams`, `players`, and `games`, populate these tables with data and make the proper associations, and query from these tables to select interesting information.

## Objectives

1.  Review creating tables, altering tables, inserting data, and querying from tables
2.  Become comfortable working with common data relationships "has many"/"belongs to" and "many-to-many"
3.  Write advanced `SELECT` queries using `JOIN` statements and join tables

### Part 1: `create.sql`

Build the tables that will make up our Sports Leagues database.  Make sure the tables adhere to the following requirements:

1.  `leagues` have a name and "have many" teams
2.  `teams` have a name and "have many" players
3.  `players` have a name and "belong to" a team
4.  `games` have a date of the *date* datatype and a location.  Each date is recorded in a string in the following format: "YYYY-MM-DD"
5.  `teams` have many games and `games` are played by many teams.  Since this relationship is "many-to-many", we will need a join table.  Let's call this join table `team_games`, and it will have foreign keys to track team and game ids.  These foreign keys are responsible for establishing the many-to-many relationship.  `team_games` will also have a column called score that keeps track of that team's score for that particular game.  The important point to remember here is that join tables can have columns that are not foreign keys.
6.  All tables will have an auto-incrementing `PRIMARY KEY` set to the integer data type


### Part 2: `insert.sql`

Once the tables are created, populate the database with data.  Feel free to create fictional leagues, teams, and games.  However, your tables should meet the following requirements.  There should be:

1.  2 leagues
2.  4 teams total, with 2 teams in each league
3.  At least 1 player per team
4.  3 total games, and teams are allowed to play teams from other leagues
5.  Lastly, we will need to log scores and the relevant team and game ids into the `team_games` join table to build out the "many-to-many" relationship

### Part 3: `update.sql`

Two players have decided to change their names.  Fix the `players` table so that the first player's name (id = 1) is switched to "Metta World Peace" and the fourth player's name (id = 4) is changed to "Chad OchoCinco".

### Part 4: `queries.py`

Write queries in the `queries.py` file to get the tests to pass.  We have seeded the database with different data, so don't expect the data your input in the above files to be returned in your queries.  Be prepared to use different sorting and grouping methods and aggregate functions.  Refer to the `seed.sql` file to understand the data populating the database.  Notice we have added a column called `info` to the `games` table.

> **Note:** `select_name_of_player_with_shortest_name`

> This query requires you to select the name of the player with the the shortest name.  Check out the [LENGTH function](https://www.w3schools.com/sql/func_mysql_length.asp).  Is there a sorting method we can use to sort the values returned by the LENGTH function?

## Summary

In this lab we started out by creating tables. We made our tables so that they would have many-to-many, has-many, and belongs-to relationships, enabling us to query information related to records accross tables. We then practiced seeding our database with information on teams, players, and games. Next, we wrote SQL statements that updated records in our database with new names. Finally, we wrote more complex SQL statements that queried and returned information from our database.

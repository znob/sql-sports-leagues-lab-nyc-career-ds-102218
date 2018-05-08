INSERT INTO leagues (name) VALUES ("NHL"), ("NBA");

INSERT INTO teams (name, league_id) VALUES ("New York Rangers", 1), ("Vancouver Canucks", 1), ("New York Knicks", 2), ("Houston Rockets", 2);

INSERT INTO players (name, team_id) VALUES ("Brian Leetch", 1), ("Pavel Bure", 2), ("Patrick Ewing", 3), ("Hakeem Olajuwon", 4), ("Mike Richter", 1);

INSERT INTO games (date, location) VALUES ("1994-06-14", "New York, NY"), ("1994-06-22", "Houston, TX"), ("1994-06-11", "Vancouver, BC");

INSERT INTO team_games (team_id, game_id, score) VALUES (1, 1, 3), (2, 1, 2), (1, 3, 1), (2, 3, 4), (3, 2, 84), (4, 2, 90);

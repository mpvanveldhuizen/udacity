-- Matt Van Veldhuizen
-- 06/06/2015
-- Udacity Full Stack Web Developer Nanodegree
-- Implementation of a Swiss-system tournament
-- tournament.sql
-- To be used with tournament.sql and tournament_test.py
-- Table definitions for the tournament project.

-- remove possible database
DROP DATABASE IF EXISTS tournament;

-- create data base tournament and connect to it
CREATE DATABASE tournament;
\c tournament;

-- create players table (player id, player name)
CREATE TABLE players (id SERIAL PRIMARY KEY, name TEXT);

-- create matches table (match id, winner id, loser id,
--                       winner id ref from players table,
--                       lossers id ref from players table)
CREATE TABLE matches (id serial PRIMARY KEY,
                      winner_id INTEGER,
		      loser_id INTEGER,
		      FOREIGN KEY (winner_id) REFERENCES players(id),
		      FOREIGN KEY (loser_id) REFERENCES players(id));
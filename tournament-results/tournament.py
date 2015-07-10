#!/usr/bin/env python
# Matt Van Veldhuizen
# 06/06/2015
# Udacity Full Stack Web Developer Nanodegree
# Implementation of a Swiss-system tournament
# tournament.py
# This Python code was given to me (partially completed)
# by the teachers at Udacity.
# To be used with tournament.sql and tournament_test.py

import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
	db = psycopg2.connect("dbname=tournament")
	cursor = db.cursor()
	return db, cursor
    except:
	raise ValueError("Can Not Connect to the Database: tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db, c = connect()
    c.execute("DELETE FROM matches;")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, c = connect()
    c.execute("DELETE FROM players;")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, c = connect()
    c.execute("SELECT count(id) from players;")
    result = c.fetchone()
    db.commit()
    db.close()
    return int(result[0])


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db, c = connect()
    c.execute("INSERT INTO players (name) VALUES (%s);", (name,))
    db.commit()
    db.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    wins_query = """
    SELECT players.id, name, COUNT(matches.id) AS wins
	FROM players LEFT JOIN matches ON players.id = winner_id
	GROUP BY players.id ORDER BY wins DESC
    """
    losses_query = """
    SELECT players.id, name, COUNT(matches.id) AS losses
	FROM players LEFT JOIN matches ON players.id = loser_id
	GROUP BY players.id ORDER BY losses DESC
    """
    query = """
    SELECT winners.id, winners.name, wins, wins+losses AS matches
        FROM ({wins_query}) AS winners LEFT JOIN ({losses_query}) AS losers
	ON winners.id = losers.id ORDER BY wins DESC;
    """.format(wins_query=wins_query, losses_query=losses_query)

    db, c = connect()
    c.execute(query)
    results = c.fetchall()
    db.commit()
    db.close()
    return results

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, c = connect()
    c.execute("""INSERT INTO matches (winner_id, loser_id) VALUES
              ({winner_id}, {loser_id});""".format(winner_id=winner,loser_id=loser))
    db.commit()
    db.close()

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    player_standings = playerStandings()
    standings = [(record[0], record[1]) for record in player_standings]
    if len(standings) < 2:
        raise ValueError("Not enough players.")
    left_pair = standings[0::2]
    right_pair = standings[1::2]
    pairings = zip(left_pair, right_pair)
    results = []
    for p in pairings:
	results.append(p[0] + p[1])

    return results


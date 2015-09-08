# Tournoment Results
### About
Project 2 from Udacity's Full Stack Web Developer Nanodegree which consitses of an implementation of a Swiss-system tournament. Where I developed a database schema to store the game matches between players. I then wrote code to query this data and determine the winners of various games.

### Setup Instructions
This will describe how to run the Swiss-system tournment
1. This system uses Vagrant with a Virtual Machine provided from the Udacity teachers
  1. To download/install Vagrant go to this [website](https://www.vagrantup.com/)
  1. Starging Vagrant by executing the command:
    1. `vagrant up` with in the `vagrant/` directory
  1. Enter the Virtual Machine by executing the command:
    1. `vagrant ssh`
    
2. Make sure the following files are in the same directory `/vagrant/tournament`
  2. `tournament.py`
  2. `tournament.sql`
  2. `tournament_test.py`
  
3. Create the database by running the following commands
  3. enter PostgreSQL interface
    3. `psql`
  3. Run the SQL script tournament.sql
    3. `\i tournament.sql`
  3. Exit the PostgreSQL interface by pressing the following keys
    3. `CTRL + D`
    
4. Run Python with the tournament_test.py file
  4. `python tournament_test.py`

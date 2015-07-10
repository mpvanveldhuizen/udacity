Matt Van Veldhuizen
06/06/2015
Udacity Full Stack Web Developer Nanodegree
Implementation of a Swiss-system tournament
README.txt

This README will describe how to run the Swiss-system tournment
	1. This system uses Vagrant with a Virtual Machine provided from the Udacity teachers
		1.1 To download/install Vagrant go to this website (https://www.vagrantup.com/)
		1.2 Starging Vagrant by executing the command:
			1.2.1 "vagrant up" with in the vagrant/ directory
		1.3 Enter the Virtual Machine by executing the command:
			1.3.1 "vagrant ssh"
	2. Make sure the following files are in the same directory /vagrant/tournament
		2.1 tournament.py
		2.2 tournament.sql
		2.3 tournament_test.py
	3. Create the database by running the following commands
		3.1 enter PostgreSQL interface
			3.1.1 "psql"
		3.2 Run the SQL script tournament.sql
			3.2.1 "\i tournament.sql"
		3.3 Exit the PostgreSQL interface by pressing the following keys
			3.3.1 CTRL + D
	3. Run Python with the tournament_test.py file
		2.1 "python tournament_test.py"
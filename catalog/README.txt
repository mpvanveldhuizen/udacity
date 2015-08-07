Matt Van Veldhuizen
08/06/2015
Udacity Full Stack Web Developer Nanodegree
Implementation of a Catalog based Website providing a list of Authors and Books
README.txt

This README will describe how to generate the "Library Catalog" web page using Python.
	1. Make Sure Python is installed
		1.1 If Not installed follow this link to download: https://www.python.org/downloads/
	2. Make sure the following libraries are installed
		2.1 flask
			2.1.1 If Not installed open a command prompt/window and type the following commands
				2.1.1.1 sudo pip install virtualenv
				2.1.1.2 mkdir myproject
				2.1.1.3 cd myproject
				2.1.1.4 virtualenv venv
				2.1.1.5 venv\scripts\activate
				2.1.1.6 pip install Flask
		2.2 sqlalchemy
			2.2.1 If Not installed open a command prompt/window and type the following commands
				2.2.1.1 pip install SQLAlchemy
		2.3 oauth2client
			2.3.1 If Not installed open a command prompt/window and type the following commands
				2.3.1.1 pip install --upgrade oauth2client
		2.4 httplib2
			2.4.1 If Not installed download the latest package from this site
				2.4.1.1 https://code.google.com/p/httplib2/downloads/list
			2.4.2 Then unpack the file and open a command prompt/window and run the following commands
				2.4.2.1 python setup.py install
	3. Make sure the following files are in the same directory
		3.1 addentries.py
		3.2 application.py
		3.3 client_secrets.json
		3.4 database_setup.py
		3.5 static
			3.5.1 styles.css
			3.5.2 top-banner.jpg
		3.6 templates
			3.6.1  application.hmtl
			3.6.2  delete_authors.html
			3.6.3  delete_books.html
			3.6.4  edit_authors.html
			3.6.5  edit_books.html
			3.6.6  footer.html
			3.6.7  header.html
			3.6.8  library.html
			3.6.9  login.html
			3.6.10 main.html
			3.6.11 new_authors.html
			3.6.12 new_books.html
	2. Setting up the Site
		2.1 First run python with database_setup.py in the command line
			2.1.1 python database_setup.py
			2.1.2 This will generate the empty database "library.db"
		2.2 Next run python with addentries.py in the command line
			2.2.1 python addentries.py
			2.2.2 This will fill the database with its starting entries
		2.3 Next run python with application.py
			2.3.1 python application.py
			2.3.2 This will start the web server for the project
	3. Open your favorite browser and navigate to the following address
		3.1 localhost:5000 or 127.0.0.1:5000
	4. Enjoy the site with its many features
		4.1 Browsing Authors and a selection of their books!
		4.2 Add New Authors!
		4.3 Add new Books for the Authors!
		4.4 Edit the Authors Information!
		4.5 Edit any of the Books Information!
		4.6 Delete Authors!
		4.7 Delete Books!
		4.8 Login provided by Google to securely manage only what you make! No One Else Can Touch Your Stuff!
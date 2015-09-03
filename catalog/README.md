# Item Catalog
### About
Project 2 of Udacity's Full Stack Web Developer Nanodegree consisting of an implementation of a Catalog based Website providing a list of Authors and Books. Where I developed an application that provides a list of items (in my case Books) within a variety of categories (in my case Authros) as well as provide a user registration and authentication system. Registered users have the ability to post, edit and delete their own items.

### Setup Instructions
This will describe how to generate the "Library Catalog" web page using Python.

1. Make Sure Python is installed
 1. If Not installed follow this [link](https://www.python.org/downloads/) to download
 
2. Make sure the following libraries are installed
 * `flask`
   2. If Not installed open a command prompt/window and type the following commands
     2. `sudo pip install virtualenv`
      2. `mkdir myproject`
      2. `cd myproject`
      2. `virtualenv venv`
      2. `venv\scripts\activate`
      2. `pip install Flask`
 * `sqlalchemy`
   2. If Not installed open a command prompt/window and type the following commands
     2. `pip install SQLAlchemy`
 2. `oauth2client`
   2. If Not installed open a command prompt/window and type the following commands
     2. `pip install --upgrade oauth2client`
 2. `httplib2`
   2. If Not installed download the latest package from this [site](https://code.google.com/p/httplib2/downloads/list)
   2. Then unpack the file and open a command prompt/window and run the following commands
     2. `python setup.py install`
   
3. Make sure the following files are in the same directory
 * `addentries.py`
 * `application.py`
 * `client_secrets.json`
 * `database_setup.py`
 * `static\`
   * `styles.css`
    * `top-banner.jpg`
 * `templates\`
   * `application.hmtl`
    * `delete_authors.html`
    * `delete_books.html`
    * `edit_authors.html`
    * `edit_books.html`
    * `footer.html`
    * `header.html`
    * `library.html`
    * `login.html`
    * `main.html`
    * `new_authors.html`
    * `new_books.html`
  
4. Setting up the Site
 4. First run `python` with `database_setup.py` in the command line
   4. `python database_setup.py`
    4. This will generate the empty database `library.db`
 4. Next run `python` with `addentries.py` in the command line
   4. `python addentries.py`
    4. This will fill the database with its starting entries
 4. Next run `python` with `application.py`
   4. `python application.py`
    4. This will start the web server for the project
  
5. Open your favorite browser and navigate to the following address
 5. `localhost:5000` or `127.0.0.1:5000`
 
6. Enjoy the site with its many features
 * Browsing Authors and a selection of their books!
 * Add New Authors!
 * Add new Books for the Authors!
 * Edit the Authors Information!
 * Edit any of the Books Information!
 * Delete Authors!
 * Delete Books!
 * Login provided by Google to securely manage only what you make! No One Else Can Touch Your Stuff!

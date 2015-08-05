from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Authors, Books
from flask import session as login_session
import random
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
import string

app = Flask(__name__)

CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Library Application"


# Connect to Database and create database session
engine = create_engine('sqlite:///library.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
	for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

    # DISCONNECT - Revoke a current user's token and reset their login_session


@app.route('/gdisconnect')
def gdisconnect():
        # Only disconnect a connected user.
    credentials = login_session.get('credentials')
    if credentials is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = credentials.access_token
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    if result['status'] == '200':
        # Reset the user's sesson.
        del login_session['credentials']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']

        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


# JSON APIs to view Authors Information
@app.route('/authors/<int:authors_id>/books/JSON')
def authorsBooksJSON(authors_id):
    authors = session.query(Authors).filter_by(id=authors_id).one()
    books = session.query(Books).filter_by(authors_id=authors_id).all()
    return jsonify(Books=[b.serialize for b in books])


@app.route('/authors/<int:authors_id>/books/<int:books_id>/JSON')
def booksJSON(authors_id, books_id):
    book_item = session.query(Books).filter_by(id=books_id).one()
    return jsonify(book_item=book_item.serialize)


@app.route('/authors/JSON')
def authorsJSON():
    authors = session.query(Authors).all()
    return jsonify(authors=[a.serialize for a in authors])


# Show all authors
@app.route('/')
@app.route('/authors/')
def showAuthors():
    authors = session.query(Authors).order_by(asc(Authors.name))
    return render_template('application.html', authors=authors)

# Create a new authors
@app.route('/authors/new/', methods=['GET', 'POST'])
def newAuthors():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newAuthors = Authors(name=request.form['name'])
        session.add(newAuthors)
        flash('New Author %s Successfully Created' % newAuthors.name)
        session.commit()
        return redirect(url_for('showAuthors'))
    else:
        return render_template('new_authors.html')

# Edit a authors
@app.route('/authors/<int:authors_id>/edit/', methods=['GET', 'POST'])
def editAuthors(authors_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedAuthors = session.query(
        Authors).filter_by(id=authors_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedAuthors.name = request.form['name']
            flash('Author Successfully Edited %s' % editedAuthors.name)
            return redirect(url_for('showAuthors'))
    else:
        return render_template('edit_authors.html', authors=editedAuthors)


# Delete a authors
@app.route('/authors/<int:authors_id>/delete/', methods=['GET', 'POST'])
def deleteAuthor(authors_id):
    if 'username' not in login_session:
        return redirect('/login')
    authorsToDelete = session.query(Authors).filter_by(id=authors_id).one()
    if request.method == 'POST':
        session.delete(authorsToDelete)
        flash('%s Successfully Deleted' % authorsToDelete.name)
        session.commit()
        return redirect(url_for('showAuthors', authors_id=authors_id))
    else:
        return render_template('delete_authors.html', authors=authorsToDelete)

# Show a authors books
@app.route('/authors/<int:authors_id>/')
@app.route('/authors/<int:authors_id>/books/')
def showBooks(authors_id):
    authors = session.query(Authors).filter_by(id=authors_id).one()
    books = session.query(Books).filter_by(authors_id=authors_id).all()
    return render_template('library.html', books=books, authors=authors)


# Create a new books
@app.route('/authors/<int:authors_id>/books/new/', methods=['GET', 'POST'])
def newBook(authors_id):
    if 'username' not in login_session:
        return redirect('/login')
    authors = session.query(Authors).filter_by(id=authors_id).one()
    if request.method == 'POST':
        newBook = Books(title=request.form['title'], cover_url=request.form['cover_url'],
			isbn=request.form['isbn'], description=request.form['description'],
			published_date=request.form['published_date'], authors_id=authors_id)
        session.add(newBook)
        session.commit()
        flash('New Book %s Successfully Created' % (newBook.title))
        return redirect(url_for('showBooks', authors_id=authors_id))
    else:
        return render_template('new_books.html', authors_id=authors_id)

# Edit a book
@app.route('/authors/<int:authors_id>/books/<int:books_id>/edit', methods=['GET', 'POST'])
def editBooks(authors_id, books_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedBooks = session.query(Books).filter_by(id=books_id).one()
    authors = session.query(Authors).filter_by(id=authors_id).one()
    if request.method == 'POST':
	if request.form['title']:
            editedItem.name = request.form['title']
        if request.form['cover_url']:
            editedItem.name = request.form['cover_url']
	if request.form['isbn']:
            editedItem.name = request.form['isbn']
        if request.form['description']:
            editedItem.description = request.form['description']
	if request.form['published_date']:
            editedItem.description = request.form['published_date']
        session.add(editedBooks)
        session.commit()
        flash('Book Successfully Edited')
        return redirect(url_for('showBooks', authors_id=authors_id))
    else:
        return render_template('edit_books.html', authors_id=authors_id, books_id=books_id, books=editedBooks)


# Delete a book
@app.route('/authors/<int:authors_id>/books/<int:books_id>/delete', methods=['GET', 'POST'])
def deleteBook(authors_id, books_id):
    if 'username' not in login_session:
        return redirect('/login')
    authors = session.query(Authors).filter_by(id=authors_id).one()
    bookToDelete = session.query(Books).filter_by(id=books_id).one()
    if request.method == 'POST':
        session.delete(bookToDelete)
        session.commit()
        flash('Book Successfully Deleted')
        return redirect(url_for('showBooks', authors_id=authors_id))
    else:
        return render_template('delete_books.html', books=bookToDelete)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
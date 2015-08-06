# Matt Van Veldhuizen
# 08/06/2015
# Udacity Full Stack Web Developer Nanodegree
# Implementation of a Catalog based Website
# providing a list of Authors and Books
# database_setup.py
# This Python code was based of the implementation
# by the teachers at Udacity.
# To be used with addentries.sql and application.py


from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# Table user to hold users who log in to edit entries
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

# Table authors to hold the list of authors
class Authors(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """ JSON serializer method """
        return {
            'name': self.name,
			'id': self.id,
        }

# Table books to hold the list of books for each author
class Books(Base):
    __tablename__ = 'books'

    title = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    cover_url = Column(String(255))
    isbn = Column(Integer)
    description = Column(String(2000))
    published_date = Column(String(9))
    authors_id = Column(Integer, ForeignKey('authors.id'))
    authors = relationship(Authors)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """ JSON serializer method """
        return {
            'id': self.id,
            'title': self.title,
            'cover_url': self.cover_url,
            'isbn': self.isbn,
            'description': self.description,
            'published_date': str(self.published_date.isoformat()),
            'authors_id': self.authors_id
        }

if __name__ == '__main__':
    engine = create_engine('sqlite:///library.db')
    Base.metadata.create_all(engine)
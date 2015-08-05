from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    access_token = Column(String(200))

    def __init__(self, access_token):
        self.access_token = access_token

class Authors(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)

    @property
    def serialize(self):
        """ JSON serializer method """
        return {
            'name': self.name,
	    'id': self.id,
        }

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
    adder_id = Column(Integer, ForeignKey('users.id'))
    adder = relationship(Users)

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
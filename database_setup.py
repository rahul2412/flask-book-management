from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


# Users table
class User(Base):
    __tablename__ = 'user'

    # Columns of User
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'picture': self.picture
            
        }


# Categories table
class Genre(Base):
    __tablename__ = 'genre'

    # Columns of Genre
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    icon = Column(String(250))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'icon': self.icon
        }


# Items table
class Book(Base):
    __tablename__ = 'book'

    # Columns of Books
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    author = Column(String(64), nullable=False)
    description = Column(String(1024))
    cover = Column(String(250))
    link = Column(String(1024))
    genre_id = Column(Integer, ForeignKey('genre.id'))
    genre = relationship(Genre)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'description': self.description,
            'cover': self.cover,
            'link': self.link,
            'genre': self.genre.name,
            'user': self.user.name
        }


engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)

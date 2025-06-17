from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    year = Column(Integer)
    genre_id = Column(Integer, ForeignKey("genres.id"))

class PlaySession(Base):
    __tablename__ = "playsessions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    game_id = Column(Integer, ForeignKey("games.id"))

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True)
    score = Column(Integer)
    comment = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    game_id = Column(Integer, ForeignKey("games.id"))

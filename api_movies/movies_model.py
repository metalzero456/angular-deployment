from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from api_movies import db

# Create movie model for inserting and retreving data from alchemy db
class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    original_title = db.Column(db.Text,nullable=False)
    budget = db.Column(db.Integer,nullable=True)
    popularity = db.Column(db.Integer,nullable=True)
    release_date = db.Column(db.Text,nullable=False)
    revenue = db.Column(db.Integer,nullable=True)
    title = db.Column(db.Text,nullable=False)
    vote_average = db.Column(db.Float, nullable=True)
    vote_count = db.Column(db.Integer, nullable=True)
    overview = db.Column(db.Text,nullable=False)
    tagline = db.Column(db.Text,nullable=False)
    uid = db.Column(db.Integer, nullable=True)
    director_id = db.Column(db.Integer, ForeignKey('directors.id'))
    director = relationship("Directors", back_populates="movies")
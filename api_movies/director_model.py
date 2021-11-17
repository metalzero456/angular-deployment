from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

from api_movies import db

# Create director model for inserting and retreving data from alchemy db
class Directors(db.Model, SerializerMixin):
    __tablename__ = 'directors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text,nullable=False)
    gender = db.Column(db.Integer,nullable=False)
    uid = db.Column(db.Integer,nullable=True)
    department = db.Column(db.Text,nullable=False)
    movies = relationship("Movie", back_populates="director")
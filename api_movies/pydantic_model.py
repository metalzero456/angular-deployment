from pydantic import BaseModel

# Model validation for Movie
class MovieBodyModel(BaseModel):
    original_title : str
    budget : int
    popularity : int
    release_date : str
    revenue : int
    title : str
    vote_average : float
    vote_count : int
    overview : str
    tagline : str
    uid : int
    director_id : int

# Model validation for Director
class DirectorBodyModel(BaseModel):
    name : str
    gender : int
    uid : int
    department : str
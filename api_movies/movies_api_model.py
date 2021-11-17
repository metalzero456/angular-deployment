from api_movies import api
from flask_restx import fields

# Create movie body model for api testing in swagger
movie_body_model = api.model(
    'Movie Body',
    {
        'original_title' : fields.String(""),
        'budget' : fields.Integer(0),
        'popularity' : fields.Integer(0),
        'release_date' : fields.String(""),
        'revenue' : fields.Integer(0),
        'title' : fields.String(""),
        'vote_average' : fields.Float(0),
        'vote_count' : fields.Integer(0),
        'overview' : fields.String(""),
        'tagline' : fields.String(""),
        'uid' : fields.Integer(0),
        'director_id' : fields.Integer(0)
    }
)

# Create movie update model for api testing in swagger
movie_update_model = api.model(
    'Movie Update/Delete',
    {
        'original_title' : fields.String(""),
        'budget' : fields.Integer(0),
        'popularity' : fields.Integer(0),
        'release_date' : fields.String(""),
        'revenue' : fields.Integer(0),
        'title' : fields.String(""),
        'vote_average' : fields.Float(0),
        'vote_count' : fields.Integer(0),
        'overview' : fields.String(""),
        'tagline' : fields.String(""),
        'uid' : fields.Integer(0),
        'director_id' : fields.Integer(0)
    }
)

# Create movie response model for api testing in swagger
movie_response_model = api.model(
    'Movie Response',
    {
        'id' : fields.Integer(),
        'original_title' : fields.String(),
        'budget' : fields.Integer(),
        'popularity' : fields.Integer(),
        'release_date' : fields.String(),
        'revenue' : fields.Integer(),
        'title' : fields.String(),
        'vote_average' : fields.Float(),
        'vote_count' : fields.Integer(),
        'overview' : fields.String(),
        'tagline' : fields.String(),
        'uid' : fields.Integer(),
        'director_name' : fields.String(attribute="director.name")
    }
)

# Create movie list model for api testing in swagger
movie_list_model = api.model(
    'Movie List',
    {
        'original_title' : fields.String(),
        'release_date' : fields.String(),
        'title' : fields.String(),
        'overview' : fields.String(),
        'tagline' : fields.String(),
    }
)
from api_movies import api
from flask_restx import fields
from api_movies.movies_api_model import movie_list_model

# Create director body model for api testing in swagger
director_body_model = api.model(
    'Director Body',
    {
        'name' : fields.String(""),
        'gender' : fields.Integer(0),
        'uid' : fields.Integer(0),
        'department' : fields.String("")
    }
)

# Create director update model for api testing in swagger
director_update_model = api.model(
    'Director Update/Delete',
    {
        'name' : fields.String(""),
        'gender' : fields.Integer(0),
        'uid' : fields.Integer(0),
        'department' : fields.String("")
    }
)

# Create director body response for api testing in swagger
director_response_model = api.model(
    'Director Response',
    {
        'id': fields.Integer(),
        'name' : fields.String(),
        'gender' : fields.Integer(),
        'uid' : fields.Integer(),
        'department' : fields.String(),
        'movies': fields.Nested(movie_list_model, attribute="movies", as_list=True)
    }
)
from flask import jsonify
from flask_pydantic import validate
from flask_restx import Resource, Namespace, abort, marshal

from api_movies import db
from api_movies.movies_api_model import movie_body_model, movie_response_model, movie_update_model
from api_movies.movies_model import Movie
from api_movies.pydantic_model import MovieBodyModel

# Create namepace for this api endpoint
api = Namespace('Movies', description='CRUD Movies', path='/')

# create endpoint /movies
@api.route('/movies')
class Movies(Resource):
    # get all method to show all movies (in this case limited up to 10 movies for time sake)
    @api.marshal_with(movie_response_model)
    def get(self):
        movies = Movie.query.limit(10).all()
        return movies

    # post method to insert a new movie
    @api.expect(movie_body_model)
    @api.response(201, 'Created', movie_response_model)
    @validate()
    def post(self, body: MovieBodyModel):
        new_movie = Movie(
            original_title = body.original_title,
            budget = body.budget,
            popularity = body.popularity,
            release_date = body.release_date,
            revenue = body.revenue,
            title = body.title,
            vote_average = body.vote_average,
            vote_count = body.vote_count,
            overview = body.overview,
            tagline = body.tagline,
            uid = body.uid,
            director_id = body.director_id
        )

        db.session.add(new_movie)
        db.session.commit()

        return marshal(new_movie, movie_response_model), 201

# create endpoint /movies/<id>
@api.route('/movie/<int:id>')
class MovieResource(Resource):
    # get id method to show specific movies based on id
    @api.marshal_with(movie_response_model, code=200)
    def get(self, id):
        movie = Movie.query.get(id)
        if movie is None:
            return abort(404, 'Id not found')
        return movie

    # put id method to update/change specific movie based on id
    @api.expect(movie_update_model)
    @validate()
    def put(self, id, body: MovieBodyModel):
        movie = Movie.query.get(id)
        if movie is None:
            return abort(404, 'Id not found')
        
        movie.original_title = body.original_title
        movie.budget = body.budget
        movie.popularity = body.popularity
        movie.release_date = body.release_date
        movie.revenue = body.revenue
        movie.title = body.title
        movie.vote_average = body.vote_average
        movie.vote_count = body.vote_count
        movie.overview = body.overview
        movie.tagline = body.tagline
        movie.uid = body.uid
        movie.director_id = body.director_id

        db.session.commit()

        return jsonify('Update Success !')

    # delete id method to delete specific movie based on id
    @validate()
    def delete(self, id):
        movie = Movie.query.get(id)
        if movie is None:
            return abort(404, 'Id not found')
        
        db.session.delete(movie)
        db.session.commit()

        return jsonify('Delete Success !')

# create endpoint /moviesByBudget
@api.route('/moviesByBudget')
class MoviesBudget(Resource):
    # get method to show all movies by highest budget (in this case limited up to 10 movies for time sake)
    @api.marshal_with(movie_response_model)
    def get(self):
        movies = Movie.query.order_by(Movie.budget.desc()).limit(10).all()
        return movies

# create endpoint /moviesByPopularity
@api.route('/moviesByPopularity')
class MoviesPopularity(Resource):
    # get method to show all movies by highest popularity (in this case limited up to 10 movies for time sake)
    @api.marshal_with(movie_response_model)
    def get(self):
        movies = Movie.query.order_by(Movie.popularity.desc()).limit(10).all()
        return movies

# create endpoint /moviesByVoteAverage
@api.route('/moviesByVoteAverage')
class MoviesVoteAverage(Resource):
    # get method to show all movies by highest vote average (in this case limited up to 10 movies for time sake)
    @api.marshal_with(movie_response_model)
    def get(self):
        movies = Movie.query.order_by(Movie.vote_average.desc()).limit(10).all()
        return movies

# create endpoint /moviesDesc
@api.route('/moviesDesc')
class MoviesDesc(Resource):
    # get method to show all movies in descending order by id (in this case limited up to 10 movies for time sake)
    @api.marshal_with(movie_response_model)
    def get(self):
        movies = Movie.query.order_by(Movie.id.desc()).limit(10).all()
        return movies
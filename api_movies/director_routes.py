from flask import jsonify
from flask_pydantic import validate
from flask_restx import Resource, Namespace, abort, marshal

from api_movies import db
from api_movies.director_api_model import director_body_model, director_response_model, director_update_model
from api_movies.director_model import Directors
from api_movies.pydantic_model import DirectorBodyModel

# Create namepace for this api endpoint
api = Namespace('Directors', description='CRUD Directors', path='/')

# create endpoint /directors
@api.route('/directors')
class Director(Resource):
    # get all method to show all directors (in this case limited up to 10 directors for time sake)
    @api.marshal_with(director_response_model)
    def get(self):
        director = Directors.query.order_by(Directors.id).limit(10).all()
        return director

    # post method to insert a new director
    @api.expect(director_body_model)
    @api.response(201, 'Created', director_response_model)
    @validate()
    def post(self, body: DirectorBodyModel):
        new_director = Directors(
            name = body.name,
            gender = body.gender,
            uid = body.uid,
            department = body.department
        )

        db.session.add(new_director)
        db.session.commit()

        return marshal(new_director, director_response_model), 201

# create endpoint /directors/<id>
@api.route('/director/<int:id>')
class DirectorResource(Resource):
    # get id method to show specific director based on id
    @api.marshal_with(director_response_model, code=200)
    def get(self, id):
        director = Directors.query.get(id)
        if director is None:
            return abort(404, 'Id not found')
        return director

    # put id method to update/change specific director based on id
    @api.expect(director_update_model)
    @validate()
    def put(self, id, body: DirectorBodyModel):
        director = Directors.query.get(id)
        if director is None:
            return abort(404, 'Id not found')
        
        director.name = body.name
        director.gender = body.gender
        director.uid = body.uid
        director.department = body.department

        db.session.commit()

        return jsonify('Update Success !')

    # delete id method to delete specific director based on id
    @validate()
    def delete(self, id):
        director = Directors.query.get(id)
        if director is None:
            return abort(404, 'Id not found')
        
        db.session.delete(director)
        db.session.commit()

        return jsonify('Delete Success !')

# create endpoint /directorsDesc
@api.route('/directorsDesc')
class DirectorDesc(Resource):
    # get method to show all directors in descending order by id (in this case limited up to 10 directors for time sake)
    @api.marshal_with(director_response_model)
    def get(self):
        director = Directors.query.order_by(Directors.id.desc()).limit(10).all()
        return director

# create endpoint /directors/<department>
@api.route('/directors/<string:department>')
class DirectorByDepartment(Resource):
    # get method to show all directors based on corresponding department
    @api.marshal_with(director_response_model, code=200)
    def get(self, department):
        director = Directors.query.filter(Directors.department.ilike(department)).limit(10).first()
        if director is None:
            return abort(404, 'Department not found')
        return director
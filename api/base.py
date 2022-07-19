from flask import Blueprint, session, jsonify, redirect
from flask_restx import Api, Resource, reqparse

blueprint = Blueprint("base", "base", url_prefix="/api")
api = Api(blueprint)
parser = reqparse.RequestParser()


@api.route("/")
class HomePage(Resource):
    def get(self):
        return jsonify({"This is a ": "HomePage"})

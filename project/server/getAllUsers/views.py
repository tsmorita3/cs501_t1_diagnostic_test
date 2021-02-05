from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

getAllUsers_blueprint = Blueprint('getAllUsers', __name__)

class ListUsers(MethodView):
    def get(self):
        all_users = User.query.all()
        responseObject = []
        for user in all_users:
            responseObject.append(user.email)
    	
        return make_response(jsonify(responseObject)), 201

listusers_view = ListUsers.as_view('listusers_api')

getAllUsers_blueprint.add_url_rule(
    '/users/index',
    view_func=listusers_view,
    methods=['GET']
)
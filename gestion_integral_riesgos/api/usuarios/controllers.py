from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .models import User
from .. import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
   data = request.json
   username = data['username']
   password = data['password']
   role = data['role']
   
   if User.query.filter_by(username=username).first():
      return jsonify({'message': 'User already exists'}), 409
   
   new_user = User(username=username, role=role)
   new_user.set_password(password)
   db.session.add(new_user)
   db.session.commit()
   
   return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
   data = request.json
   username = data.get('username')
   password = data.get('password')
   
   user = User.query.filter_by(username=username).first()
   if user and user.check_password(password):
      access_token = create_access_token(identity={'username': username, 'role': user.role})
      return jsonify(access_token=access_token)
   
   return jsonify({'message': 'Invalid credentials'}), 401

def init_app(app):
   if not hasattr(app, 'extensions') or 'sqlalchemy' not in app.extensions:
      app.config.from_pyfile('gestion_integral_riesgos/config_usuarios.py')
      db.init_app(app)
      with app.app_context():
         db.create_all()
   app.register_blueprint(auth_bp, url_prefix='/usuarios')
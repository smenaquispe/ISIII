from flask import request, jsonify
from functools import wraps
from gestion_integral_riesgos.api.usuarios.models import User
from sqlalchemy.orm.exc import NoResultFound
from flask_jwt_extended import get_jwt_identity, jwt_required

def authenticate(username, password):
   try:
      user = User.query.filter_by(username=username).one()
      if user.check_password(password):
         return user
   except NoResultFound:
      return None

def token_required(f):
   @wraps(f)
   @jwt_required()
   def wrapper(*args, **kwargs):
      identity = get_jwt_identity()  # Obtiene la identidad del JWT
      user = User.query.filter_by(username=identity['username']).first()  # Recupera el usuario
      if user is None:
         return jsonify({"msg": "User not found"}), 404
      return f(user, *args, **kwargs)  # Pasa el usuario a la vista
   return wrapper

def requires_roles(*roles):
   def decorator(fn):
      @wraps(fn)
      @jwt_required()
      def wrapped(user, *args, **kwargs):
         if user.role not in roles:
               return jsonify({"msg": "Access forbidden: insufficient role"}), 403
         return fn(user, *args, **kwargs)  # Pasa el usuario a la vista
      return wrapped
   return decorator

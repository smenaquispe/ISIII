import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "database/usuarios.db")}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "556e214785aebf694a4239fcc47abb6344e6bc8bc5ac40c6"
JWT_SECRET_KEY = "fa9d572321440b9218993a6c69cc3f51d85e8ed8657eee15"
from flask import Flask
from api.controllers import init_app

app = Flask(__name__)
init_app(app)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
